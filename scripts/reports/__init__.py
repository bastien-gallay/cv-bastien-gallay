"""
Module de génération de rapports hebdomadaires.

Ce module fournit des outils pour:
- Générer des Cumulative Flow Diagrams (CFD)
- Créer des rapports hebdomadaires markdown
- Analyser les données de tâches
"""

from scripts.reports.cfd import DayData, generate_cfd, load_json_data
from scripts.reports.weekly_report import WeeklyReport, generate_weekly_report

__all__ = [
    "DayData",
    "generate_cfd",
    "load_json_data",
    "WeeklyReport",
    "generate_weekly_report",
]
