#!/usr/bin/env python3
"""
CLI pour générer des Cumulative Flow Diagrams (CFD).

Usage:
    uv run --with matplotlib --with numpy scripts/reports/generate_cfd.py --week 2025-W48 --output .tasks/reports/
    uv run --with matplotlib --with numpy scripts/reports/generate_cfd.py --data data.json --output ./

Le CFD permet de visualiser:
- WIP (Work In Progress): épaisseur de la bande "En cours"
- Lead Time: distance horizontale entre "À faire" et "Terminé"
- Throughput: pente de la courbe "Terminé"
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from scripts.reports.cfd import (
    CFDConfig,
    DayData,
    calculate_metrics,
    generate_cfd,
    load_json_data,
)


# Données de référence codées en dur (pour démo et tests)
WEEK_DATA = {
    "2025-W48": {
        "title": "Cumulative Flow Diagram - Semaine 48 (25-27 nov 2025)",
        "data": [
            ("2025-11-24", 29, 0, 12),  # Dimanche soir - état initial
            ("2025-11-25", 22, 0, 32),  # Lundi soir: 20 terminées
            ("2025-11-26", 19, 0, 37),  # Mardi soir: 5 terminées
            ("2025-11-27", 17, 0, 40),  # Mercredi soir: 3 terminées
        ],
    },
}


def load_week_data(week: str) -> tuple[list[DayData], CFDConfig]:
    """
    Charge les données pour une semaine donnée.

    Args:
        week: Identifiant de semaine (ex: "2025-W48")

    Returns:
        Tuple (données, config)
    """
    if week not in WEEK_DATA:
        raise ValueError(f"Données non disponibles pour la semaine {week}. "
                        f"Utilisez --data avec un fichier JSON.")

    raw = WEEK_DATA[week]
    data = []
    for row in raw["data"]:
        date_str, backlog, in_progress, done = row
        data.append(DayData(
            date=datetime.strptime(date_str, "%Y-%m-%d"),
            backlog=backlog,
            in_progress=in_progress,
            done=done,
        ))

    config = CFDConfig(title=raw["title"])
    return data, config


def main():
    """Point d'entrée CLI."""
    parser = argparse.ArgumentParser(
        description="Génère un Cumulative Flow Diagram (CFD)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--week",
        type=str,
        help="Identifiant de semaine (ex: 2025-W48)",
    )
    parser.add_argument(
        "--data",
        type=Path,
        help="Fichier JSON avec les données",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("."),
        help="Répertoire ou fichier de sortie",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Afficher le graphique interactivement",
    )
    parser.add_argument(
        "--metrics",
        action="store_true",
        help="Afficher les métriques calculées",
    )

    args = parser.parse_args()

    # Chargement des données
    if args.data:
        data, config = load_json_data(args.data)
        output_name = args.data.stem + "-cfd.png"
    elif args.week:
        data, config = load_week_data(args.week)
        output_name = f"{args.week}-cfd.png"
    else:
        print("Aucune donnée spécifiée, utilisation des données de démo (2025-W48)")
        data, config = load_week_data("2025-W48")
        output_name = "demo-cfd.png"

    # Afficher les métriques si demandé
    if args.metrics:
        metrics = calculate_metrics(data)
        print("\nMétriques CFD:")
        print(f"  Throughput: {metrics['throughput']} tâches/jour")
        print(f"  WIP moyen: {metrics['wip_avg']}")
        print(f"  Lead Time moyen: {metrics['lead_time_avg']} jours")
        print(f"  Tâches terminées: {metrics['tasks_completed']}")
        print(f"  Durée: {metrics['days']} jours")
        print()

    # Détermination du chemin de sortie
    if args.output.is_dir():
        output_path = args.output / output_name
    else:
        output_path = args.output

    # Génération
    result = generate_cfd(data, config=config, output_path=output_path, show=args.show)
    if result:
        print(f"CFD généré: {result}")


if __name__ == "__main__":
    main()
