"""
Cumulative Flow Diagram (CFD) generator.

Le CFD permet de visualiser:
- WIP (Work In Progress): épaisseur de la bande "En cours"
- Lead Time: distance horizontale entre "À faire" et "Terminé"
- Throughput: pente de la courbe "Terminé"
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure


@dataclass
class DayData:
    """Données d'une journée pour le CFD."""

    date: datetime
    backlog: int  # À faire
    in_progress: int  # En cours
    done: int  # Terminé
    comment: str = ""

    @property
    def total(self) -> int:
        """Total des tâches."""
        return self.backlog + self.in_progress + self.done

    def to_dict(self) -> dict:
        """Convertit en dictionnaire pour JSON."""
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "backlog": self.backlog,
            "in_progress": self.in_progress,
            "done": self.done,
            "comment": self.comment,
        }

    @classmethod
    def from_dict(cls, data: dict) -> DayData:
        """Crée une instance depuis un dictionnaire."""
        return cls(
            date=datetime.strptime(data["date"], "%Y-%m-%d"),
            backlog=data["backlog"],
            in_progress=data["in_progress"],
            done=data["done"],
            comment=data.get("comment", ""),
        )


@dataclass
class CFDConfig:
    """Configuration pour la génération du CFD."""

    title: str = "Cumulative Flow Diagram"
    figsize: tuple[int, int] = (12, 6)
    dpi: int = 150
    colors: dict[str, str] | None = None

    def __post_init__(self):
        if self.colors is None:
            self.colors = {
                "done": "#2e7d32",  # Vert - Terminé
                "in_progress": "#f9a825",  # Jaune/Orange - En cours
                "backlog": "#4682b4",  # Bleu projet - À faire
            }


def generate_cfd(
    data: list[DayData],
    config: CFDConfig | None = None,
    output_path: Path | None = None,
    show: bool = False,
) -> Path | None:
    """
    Génère un Cumulative Flow Diagram avec aires empilées.

    Args:
        data: Liste des données journalières
        config: Configuration du graphique
        output_path: Chemin de sortie pour l'image (optionnel)
        show: Afficher le graphique interactivement

    Returns:
        Chemin du fichier généré ou None
    """
    # Import lazy pour éviter les dépendances si non utilisé
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import numpy as np

    if config is None:
        config = CFDConfig()

    # Extraction des données
    dates = [d.date for d in data]
    backlog = np.array([d.backlog for d in data])
    in_progress = np.array([d.in_progress for d in data])
    done = np.array([d.done for d in data])

    # Configuration du style
    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=config.figsize)

    # Aires empilées (ordre: done en bas, puis in_progress, puis backlog en haut)
    ax.stackplot(
        dates,
        done,
        in_progress,
        backlog,
        labels=["Terminé", "En cours", "À faire"],
        colors=[
            config.colors["done"],
            config.colors["in_progress"],
            config.colors["backlog"],
        ],
        alpha=0.8,
    )

    # Annotations WIP et Lead Time
    if len(data) > 1:
        avg_wip = np.mean(in_progress)
        if avg_wip > 0:
            mid_idx = len(dates) // 2
            mid_done = done[mid_idx]
            ax.annotate(
                f"WIP moyen: {avg_wip:.1f}",
                xy=(dates[mid_idx], mid_done + avg_wip / 2),
                xytext=(10, 0),
                textcoords="offset points",
                fontsize=9,
                color="#e65100",
                fontweight="bold",
            )

    # Configuration des axes
    ax.set_xlabel("Date", fontsize=11)
    ax.set_ylabel("Nombre de tâches", fontsize=11)
    ax.set_title(config.title, fontsize=14, fontweight="bold", pad=15)

    # Format des dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%a %d/%m"))
    ax.xaxis.set_major_locator(mdates.DayLocator())
    plt.xticks(rotation=45, ha="right")

    # Légende
    ax.legend(loc="upper left", framealpha=0.9)

    # Grille subtile
    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Limites Y
    max_total = max(d.total for d in data)
    ax.set_ylim(0, max_total * 1.1)

    # Ajustement layout
    plt.tight_layout()

    # Sauvegarde ou affichage
    result_path = None
    if output_path:
        result_path = Path(output_path)
        plt.savefig(result_path, dpi=config.dpi, bbox_inches="tight", facecolor="white")

    if show:
        plt.show()

    plt.close()
    return result_path


def load_json_data(json_path: Path) -> tuple[list[DayData], CFDConfig]:
    """
    Charge les données depuis un fichier JSON.

    Format attendu:
    {
        "title": "Mon CFD",
        "data": [
            {"date": "2025-11-25", "backlog": 10, "in_progress": 2, "done": 5},
            ...
        ]
    }

    Returns:
        Tuple (données, config)
    """
    with open(json_path) as f:
        raw = json.load(f)

    data = [DayData.from_dict(row) for row in raw["data"]]
    config = CFDConfig(title=raw.get("title", "Cumulative Flow Diagram"))

    return data, config


def save_json_data(
    data: list[DayData],
    json_path: Path,
    week: str,
    title: str | None = None,
    summary: dict | None = None,
) -> None:
    """
    Sauvegarde les données dans un fichier JSON.

    Args:
        data: Liste des données journalières
        json_path: Chemin de sortie
        week: Identifiant de semaine (ex: "2025-W48")
        title: Titre du CFD
        summary: Résumé statistique optionnel
    """
    output = {
        "week": week,
        "title": title or f"Cumulative Flow Diagram - {week}",
        "data": [d.to_dict() for d in data],
    }
    if summary:
        output["summary"] = summary

    with open(json_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)


def calculate_metrics(data: list[DayData]) -> dict:
    """
    Calcule les métriques clés du CFD.

    Returns:
        Dictionnaire avec throughput, wip_avg, lead_time_avg
    """
    if len(data) < 2:
        return {"throughput": 0, "wip_avg": 0, "lead_time_avg": 0}

    # Throughput: tâches terminées / nombre de jours
    tasks_completed = data[-1].done - data[0].done
    days = (data[-1].date - data[0].date).days or 1
    throughput = tasks_completed / days

    # WIP moyen
    wip_avg = sum(d.in_progress for d in data) / len(data)

    # Lead time approximatif (Little's Law: Lead Time = WIP / Throughput)
    lead_time_avg = wip_avg / throughput if throughput > 0 else 0

    return {
        "throughput": round(throughput, 2),
        "wip_avg": round(wip_avg, 2),
        "lead_time_avg": round(lead_time_avg, 2),
        "tasks_completed": tasks_completed,
        "days": days,
    }
