"""Tests pour le module weekly_report."""

import json
import tempfile
from datetime import datetime
from pathlib import Path

import pytest

from scripts.reports.weekly_report import (
    TaskSummary,
    WeeklyReport,
    generate_weekly_report,
    get_week_dates,
    load_report,
    save_report,
)


class TestTaskSummary:
    """Tests pour TaskSummary."""

    def test_create_task_summary(self):
        """Création d'une instance TaskSummary."""
        task = TaskSummary(
            id="CNT-001",
            title="Test task",
            category="CNT",
            priority="haute",
            status="terminé",
        )
        assert task.id == "CNT-001"
        assert task.title == "Test task"
        assert task.category == "CNT"
        assert task.priority == "haute"
        assert task.status == "terminé"

    def test_task_summary_with_dates(self):
        """TaskSummary avec dates."""
        task = TaskSummary(
            id="CNT-001",
            title="Test",
            category="CNT",
            priority="haute",
            status="terminé",
            created_date="2025-11-25",
            completed_date="2025-11-26",
        )
        assert task.created_date == "2025-11-25"
        assert task.completed_date == "2025-11-26"


class TestWeeklyReport:
    """Tests pour WeeklyReport."""

    @pytest.fixture
    def sample_report(self) -> WeeklyReport:
        """Rapport de test."""
        return WeeklyReport(
            week="2025-W48",
            start_date=datetime(2025, 11, 25),
            end_date=datetime(2025, 11, 27),
            tasks_completed=[
                TaskSummary("CNT-001", "Task 1", "CNT", "haute", "terminé"),
                TaskSummary("CNT-002", "Task 2", "CNT", "moyenne", "terminé"),
                TaskSummary("INF-001", "Task 3", "INF", "haute", "terminé"),
            ],
            tasks_created=[
                TaskSummary("CNT-003", "New task", "CNT", "basse", "à faire"),
            ],
            backlog_count=17,
        )

    def test_period_str(self, sample_report):
        """Formatage de la période."""
        assert "25" in sample_report.period_str
        assert "27" in sample_report.period_str
        assert "2025" in sample_report.period_str

    def test_tasks_by_category(self, sample_report):
        """Groupement par catégorie."""
        by_cat = sample_report.tasks_by_category(sample_report.tasks_completed)
        assert "CNT" in by_cat
        assert "INF" in by_cat
        assert len(by_cat["CNT"]) == 2
        assert len(by_cat["INF"]) == 1

    def test_to_dict(self, sample_report):
        """Conversion en dictionnaire."""
        result = sample_report.to_dict()
        assert result["week"] == "2025-W48"
        assert result["start_date"] == "2025-11-25"
        assert result["end_date"] == "2025-11-27"
        assert len(result["tasks_completed"]) == 3
        assert result["backlog_count"] == 17

    def test_from_dict(self):
        """Création depuis dictionnaire."""
        data = {
            "week": "2025-W48",
            "start_date": "2025-11-25",
            "end_date": "2025-11-27",
            "tasks_completed": [
                {"id": "CNT-001", "title": "Test", "category": "CNT",
                 "priority": "haute", "status": "terminé"}
            ],
            "tasks_created": [],
            "tasks_in_progress": [],
            "backlog_count": 10,
            "notes": ["Note 1"],
        }
        report = WeeklyReport.from_dict(data)
        assert report.week == "2025-W48"
        assert len(report.tasks_completed) == 1
        assert report.backlog_count == 10
        assert len(report.notes) == 1

    def test_empty_report(self):
        """Rapport vide."""
        report = WeeklyReport(
            week="2025-W48",
            start_date=datetime(2025, 11, 25),
            end_date=datetime(2025, 11, 27),
        )
        assert len(report.tasks_completed) == 0
        assert len(report.tasks_created) == 0
        assert report.backlog_count == 0


class TestSaveLoadReport:
    """Tests pour save_report et load_report."""

    def test_save_and_load(self):
        """Sauvegarde et chargement."""
        report = WeeklyReport(
            week="2025-W48",
            start_date=datetime(2025, 11, 25),
            end_date=datetime(2025, 11, 27),
            tasks_completed=[
                TaskSummary("CNT-001", "Test", "CNT", "haute", "terminé")
            ],
            backlog_count=15,
            notes=["Note test"],
        )

        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            json_path = Path(f.name)

        try:
            save_report(report, json_path)
            loaded = load_report(json_path)

            assert loaded.week == report.week
            assert len(loaded.tasks_completed) == 1
            assert loaded.tasks_completed[0].id == "CNT-001"
            assert loaded.backlog_count == 15
            assert loaded.notes == ["Note test"]
        finally:
            json_path.unlink()


class TestGenerateWeeklyReport:
    """Tests pour generate_weekly_report."""

    def test_generate_report(self):
        """Génération d'un rapport markdown."""
        report = WeeklyReport(
            week="2025-W48",
            start_date=datetime(2025, 11, 25),
            end_date=datetime(2025, 11, 27),
            tasks_completed=[
                TaskSummary("CNT-001", "Task 1", "CNT", "haute", "terminé"),
                TaskSummary("INF-001", "Task 2", "INF", "moyenne", "terminé"),
            ],
            tasks_created=[
                TaskSummary("CNT-002", "New task", "CNT", "basse", "à faire"),
            ],
            backlog_count=17,
            cfd_image_path="2025-W48-cfd.png",
        )

        with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as f:
            output_path = Path(f.name)

        try:
            result = generate_weekly_report(report, output_path)
            assert result == output_path
            assert output_path.exists()

            content = output_path.read_text()
            assert "Semaine 48" in content
            assert "CNT-001" in content
            assert "INF-001" in content
            assert "CNT-002" in content
            assert "17" in content  # backlog count
            assert "2025-W48-cfd.png" in content
        finally:
            output_path.unlink()

    def test_generate_report_empty_tasks(self):
        """Génération avec tâches vides."""
        report = WeeklyReport(
            week="2025-W48",
            start_date=datetime(2025, 11, 25),
            end_date=datetime(2025, 11, 27),
            backlog_count=10,
        )

        with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as f:
            output_path = Path(f.name)

        try:
            result = generate_weekly_report(report, output_path)
            content = output_path.read_text()
            assert "Tâches terminées" in content
            assert "À compléter" in content  # Default notes
        finally:
            output_path.unlink()

    def test_generate_report_with_notes(self):
        """Génération avec notes personnalisées."""
        report = WeeklyReport(
            week="2025-W48",
            start_date=datetime(2025, 11, 25),
            end_date=datetime(2025, 11, 27),
            notes=["Note importante", "Autre note"],
        )

        with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as f:
            output_path = Path(f.name)

        try:
            generate_weekly_report(report, output_path)
            content = output_path.read_text()
            assert "Note importante" in content
            assert "Autre note" in content
        finally:
            output_path.unlink()


class TestGetWeekDates:
    """Tests pour get_week_dates."""

    def test_week_48_2025(self):
        """Semaine 48 de 2025."""
        start, end = get_week_dates("2025-W48")
        assert start.month == 11
        assert start.day == 24  # Lundi 24 novembre
        assert end.month == 11
        assert end.day == 30  # Dimanche 30 novembre

    def test_week_1_2025(self):
        """Semaine 1 de 2025."""
        start, end = get_week_dates("2025-W01")
        assert start.year == 2024 or start.year == 2025
        assert start.weekday() == 0  # Lundi

    def test_week_52_2024(self):
        """Semaine 52 de 2024."""
        start, end = get_week_dates("2024-W52")
        assert start.weekday() == 0  # Lundi
        assert (end - start).days == 6  # 7 jours

    def test_returns_monday_to_sunday(self):
        """Retourne lundi à dimanche."""
        start, end = get_week_dates("2025-W10")
        assert start.weekday() == 0  # Lundi
        assert end.weekday() == 6  # Dimanche
        assert (end - start).days == 6
