"""
Générateur de rapports hebdomadaires markdown.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


@dataclass
class TaskSummary:
    """Résumé d'une tâche pour le rapport."""

    id: str
    title: str
    category: str
    priority: str
    status: str
    completed_date: str | None = None
    created_date: str | None = None


@dataclass
class WeeklyReport:
    """Données d'un rapport hebdomadaire."""

    week: str  # Ex: "2025-W48"
    start_date: datetime
    end_date: datetime
    tasks_completed: list[TaskSummary] = field(default_factory=list)
    tasks_created: list[TaskSummary] = field(default_factory=list)
    tasks_in_progress: list[TaskSummary] = field(default_factory=list)
    backlog_count: int = 0
    notes: list[str] = field(default_factory=list)
    cfd_image_path: str | None = None

    @property
    def period_str(self) -> str:
        """Période formatée."""
        return f"{self.start_date.strftime('%d')} - {self.end_date.strftime('%d %B %Y')}"

    def tasks_by_category(self, tasks: list[TaskSummary]) -> dict[str, list[TaskSummary]]:
        """Groupe les tâches par catégorie."""
        by_cat: dict[str, list[TaskSummary]] = {}
        for task in tasks:
            cat = task.category
            if cat not in by_cat:
                by_cat[cat] = []
            by_cat[cat].append(task)
        return by_cat

    def to_dict(self) -> dict[str, Any]:
        """Convertit en dictionnaire pour JSON."""
        return {
            "week": self.week,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "tasks_completed": [t.__dict__ for t in self.tasks_completed],
            "tasks_created": [t.__dict__ for t in self.tasks_created],
            "tasks_in_progress": [t.__dict__ for t in self.tasks_in_progress],
            "backlog_count": self.backlog_count,
            "notes": self.notes,
            "cfd_image_path": self.cfd_image_path,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WeeklyReport:
        """Crée une instance depuis un dictionnaire."""
        return cls(
            week=data["week"],
            start_date=datetime.strptime(data["start_date"], "%Y-%m-%d"),
            end_date=datetime.strptime(data["end_date"], "%Y-%m-%d"),
            tasks_completed=[TaskSummary(**t) for t in data.get("tasks_completed", [])],
            tasks_created=[TaskSummary(**t) for t in data.get("tasks_created", [])],
            tasks_in_progress=[TaskSummary(**t) for t in data.get("tasks_in_progress", [])],
            backlog_count=data.get("backlog_count", 0),
            notes=data.get("notes", []),
            cfd_image_path=data.get("cfd_image_path"),
        )


CATEGORY_NAMES = {
    "CNT": "Contenu",
    "TPL": "Template",
    "INF": "Infrastructure",
    "LAY": "Layout",
    "QUA": "Qualité",
    "DOC": "Documentation",
    "PIP": "Pipeline",
}

PRIORITY_EMOJI = {
    "haute": "🔴",
    "high": "🔴",
    "moyenne": "🟡",
    "medium": "🟡",
    "basse": "🟢",
    "low": "🟢",
}


def generate_weekly_report(report: WeeklyReport, output_path: Path) -> Path:
    """
    Génère un rapport hebdomadaire en markdown.

    Args:
        report: Données du rapport
        output_path: Chemin de sortie

    Returns:
        Chemin du fichier généré
    """
    lines = [
        f"# Récapitulatif Hebdomadaire - Semaine {report.week.split('-W')[1]} ({report.period_str})",
        "",
        "## Vue d'ensemble",
        "",
        "| Métrique | Valeur |",
        "|----------|--------|",
        f"| **Période** | {report.period_str} |",
        f"| **Tâches terminées** | {len(report.tasks_completed)} |",
        f"| **Tâches créées** | {len(report.tasks_created)} |",
        f"| **Tâches en cours** | {len(report.tasks_in_progress)} |",
        f"| **Backlog actuel** | {report.backlog_count} |",
        "",
        "---",
        "",
    ]

    # CFD
    if report.cfd_image_path:
        lines.extend([
            "## Flux cumulatif (Cumulative Flow Diagram)",
            "",
            f"![CFD {report.week}]({report.cfd_image_path})",
            "",
            "**Lecture du CFD :**",
            "",
            f"- **Vert (Terminé)** : {len(report.tasks_completed)} tâches terminées cette semaine",
            "- **Orange (En cours)** : WIP actuel",
            "- **Bleu (À faire)** : Backlog restant",
            "",
            "---",
            "",
        ])

    # Tâches terminées par catégorie
    lines.extend([
        "## Tâches terminées",
        "",
    ])

    by_cat = report.tasks_by_category(report.tasks_completed)
    for cat, tasks in sorted(by_cat.items()):
        cat_name = CATEGORY_NAMES.get(cat, cat)
        lines.extend([
            f"### {cat} ({cat_name})",
            "",
            "| ID | Titre | Priorité |",
            "|----|-------|----------|",
        ])
        for task in tasks:
            priority_emoji = PRIORITY_EMOJI.get(task.priority.lower(), "")
            lines.append(f"| {task.id} | {task.title} | {priority_emoji} {task.priority.capitalize()} |")
        lines.append("")

    # Tâches créées
    if report.tasks_created:
        lines.extend([
            "---",
            "",
            "## Tâches créées cette semaine",
            "",
            "| ID | Titre | Catégorie | Priorité |",
            "|----|-------|-----------|----------|",
        ])
        for task in report.tasks_created:
            cat_name = CATEGORY_NAMES.get(task.category, task.category)
            priority_emoji = PRIORITY_EMOJI.get(task.priority.lower(), "")
            lines.append(
                f"| {task.id} | {task.title} | {cat_name} | {priority_emoji} {task.priority.capitalize()} |"
            )
        lines.append("")

    # Notes
    lines.extend([
        "---",
        "",
        "## Notes et observations",
        "",
    ])
    if report.notes:
        for note in report.notes:
            lines.append(f"- {note}")
    else:
        lines.extend([
            "- [ ] À compléter avec observations personnelles",
            "- [ ] Retours utilisateur à intégrer",
            "- [ ] Blocages rencontrés",
            "- [ ] Améliorations process suggérées",
        ])
    lines.append("")

    # Footer
    lines.extend([
        "---",
        "",
        f"*Généré le {datetime.now().strftime('%Y-%m-%d')}*",
        "",
    ])

    content = "\n".join(lines)
    output_path.write_text(content, encoding="utf-8")
    return output_path


def load_report(json_path: Path) -> WeeklyReport:
    """Charge un rapport depuis un fichier JSON."""
    with open(json_path) as f:
        data = json.load(f)
    return WeeklyReport.from_dict(data)


def save_report(report: WeeklyReport, json_path: Path) -> None:
    """Sauvegarde un rapport dans un fichier JSON."""
    with open(json_path, "w") as f:
        json.dump(report.to_dict(), f, indent=2, ensure_ascii=False)


def get_week_dates(week: str) -> tuple[datetime, datetime]:
    """
    Calcule les dates de début et fin pour une semaine ISO.

    Args:
        week: Format "YYYY-WNN" (ex: "2025-W48")

    Returns:
        Tuple (lundi, dimanche) de la semaine
    """
    year, week_num = week.split("-W")
    # Premier jour de l'année
    jan1 = datetime(int(year), 1, 1)
    # Trouver le premier lundi
    days_to_monday = (7 - jan1.weekday()) % 7
    if jan1.weekday() <= 3:  # Si Jan 1 est Lun-Jeu, c'est semaine 1
        first_monday = jan1 - timedelta(days=jan1.weekday())
    else:  # Sinon, première semaine commence le lundi suivant
        first_monday = jan1 + timedelta(days=days_to_monday)

    # Calculer le lundi de la semaine demandée
    week_monday = first_monday + timedelta(weeks=int(week_num) - 1)
    week_sunday = week_monday + timedelta(days=6)

    return week_monday, week_sunday
