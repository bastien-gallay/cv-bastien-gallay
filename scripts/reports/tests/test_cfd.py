"""Tests pour le module CFD."""

import json
import tempfile
from datetime import datetime
from pathlib import Path

import pytest

from scripts.reports.cfd import (
    CFDConfig,
    DayData,
    calculate_metrics,
    load_json_data,
    save_json_data,
)


class TestDayData:
    """Tests pour DayData."""

    def test_create_day_data(self):
        """Création d'une instance DayData."""
        data = DayData(
            date=datetime(2025, 11, 25),
            backlog=10,
            in_progress=2,
            done=5,
        )
        assert data.backlog == 10
        assert data.in_progress == 2
        assert data.done == 5
        assert data.total == 17

    def test_day_data_with_comment(self):
        """DayData avec commentaire."""
        data = DayData(
            date=datetime(2025, 11, 25),
            backlog=10,
            in_progress=2,
            done=5,
            comment="Test comment",
        )
        assert data.comment == "Test comment"

    def test_to_dict(self):
        """Conversion en dictionnaire."""
        data = DayData(
            date=datetime(2025, 11, 25),
            backlog=10,
            in_progress=2,
            done=5,
            comment="Test",
        )
        result = data.to_dict()
        assert result["date"] == "2025-11-25"
        assert result["backlog"] == 10
        assert result["in_progress"] == 2
        assert result["done"] == 5
        assert result["comment"] == "Test"

    def test_from_dict(self):
        """Création depuis dictionnaire."""
        raw = {
            "date": "2025-11-25",
            "backlog": 10,
            "in_progress": 2,
            "done": 5,
            "comment": "Test",
        }
        data = DayData.from_dict(raw)
        assert data.date == datetime(2025, 11, 25)
        assert data.backlog == 10
        assert data.in_progress == 2
        assert data.done == 5
        assert data.comment == "Test"

    def test_from_dict_without_comment(self):
        """Création depuis dictionnaire sans commentaire."""
        raw = {
            "date": "2025-11-25",
            "backlog": 10,
            "in_progress": 2,
            "done": 5,
        }
        data = DayData.from_dict(raw)
        assert data.comment == ""

    def test_total_property(self):
        """Propriété total."""
        data = DayData(
            date=datetime(2025, 11, 25),
            backlog=10,
            in_progress=3,
            done=7,
        )
        assert data.total == 20


class TestCFDConfig:
    """Tests pour CFDConfig."""

    def test_default_config(self):
        """Configuration par défaut."""
        config = CFDConfig()
        assert config.title == "Cumulative Flow Diagram"
        assert config.figsize == (12, 6)
        assert config.dpi == 150
        assert "done" in config.colors
        assert "in_progress" in config.colors
        assert "backlog" in config.colors

    def test_custom_config(self):
        """Configuration personnalisée."""
        config = CFDConfig(
            title="Mon CFD",
            figsize=(10, 5),
            dpi=100,
        )
        assert config.title == "Mon CFD"
        assert config.figsize == (10, 5)
        assert config.dpi == 100

    def test_custom_colors(self):
        """Couleurs personnalisées."""
        colors = {"done": "#000", "in_progress": "#111", "backlog": "#222"}
        config = CFDConfig(colors=colors)
        assert config.colors == colors


class TestLoadSaveJsonData:
    """Tests pour les fonctions de chargement/sauvegarde JSON."""

    def test_save_and_load_json(self):
        """Sauvegarde et chargement JSON."""
        data = [
            DayData(datetime(2025, 11, 25), 10, 2, 5),
            DayData(datetime(2025, 11, 26), 8, 1, 8),
        ]

        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            json_path = Path(f.name)

        try:
            save_json_data(
                data,
                json_path,
                week="2025-W48",
                title="Test CFD",
            )

            loaded_data, config = load_json_data(json_path)

            assert len(loaded_data) == 2
            assert loaded_data[0].backlog == 10
            assert loaded_data[1].done == 8
            assert config.title == "Test CFD"
        finally:
            json_path.unlink()

    def test_load_json_with_summary(self):
        """Chargement JSON avec résumé."""
        raw = {
            "week": "2025-W48",
            "title": "Test",
            "data": [
                {"date": "2025-11-25", "backlog": 10, "in_progress": 2, "done": 5},
            ],
            "summary": {"throughput": 5.0},
        }

        with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
            json.dump(raw, f)
            json_path = Path(f.name)

        try:
            data, config = load_json_data(json_path)
            assert len(data) == 1
        finally:
            json_path.unlink()


class TestCalculateMetrics:
    """Tests pour calculate_metrics."""

    def test_empty_data(self):
        """Données vides."""
        metrics = calculate_metrics([])
        assert metrics["throughput"] == 0
        assert metrics["wip_avg"] == 0

    def test_single_day(self):
        """Un seul jour."""
        data = [DayData(datetime(2025, 11, 25), 10, 2, 5)]
        metrics = calculate_metrics(data)
        assert metrics["throughput"] == 0

    def test_multiple_days(self):
        """Plusieurs jours."""
        data = [
            DayData(datetime(2025, 11, 25), 10, 2, 5),
            DayData(datetime(2025, 11, 26), 8, 1, 8),
            DayData(datetime(2025, 11, 27), 6, 0, 11),
        ]
        metrics = calculate_metrics(data)
        assert metrics["tasks_completed"] == 6  # 11 - 5
        assert metrics["days"] == 2
        assert metrics["throughput"] == 3.0  # 6 / 2
        assert metrics["wip_avg"] == 1.0  # (2 + 1 + 0) / 3

    def test_zero_wip(self):
        """WIP nul."""
        data = [
            DayData(datetime(2025, 11, 25), 10, 0, 5),
            DayData(datetime(2025, 11, 26), 8, 0, 7),
        ]
        metrics = calculate_metrics(data)
        assert metrics["wip_avg"] == 0
        assert metrics["lead_time_avg"] == 0

    def test_high_throughput(self):
        """Throughput élevé."""
        data = [
            DayData(datetime(2025, 11, 25), 30, 1, 10),
            DayData(datetime(2025, 11, 26), 20, 1, 20),
            DayData(datetime(2025, 11, 27), 10, 0, 30),
        ]
        metrics = calculate_metrics(data)
        assert metrics["tasks_completed"] == 20
        assert metrics["throughput"] == 10.0


class TestGenerateCFD:
    """Tests pour generate_cfd (requiert matplotlib)."""

    @pytest.fixture
    def sample_data(self) -> list[DayData]:
        """Données de test."""
        return [
            DayData(datetime(2025, 11, 25), 10, 2, 5),
            DayData(datetime(2025, 11, 26), 8, 1, 8),
            DayData(datetime(2025, 11, 27), 6, 0, 11),
        ]

    def test_generate_cfd_to_file(self, sample_data):
        """Génération vers fichier."""
        pytest.importorskip("matplotlib")
        from scripts.reports.cfd import generate_cfd

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            output_path = Path(f.name)

        try:
            result = generate_cfd(sample_data, output_path=output_path)
            assert result == output_path
            assert output_path.exists()
            assert output_path.stat().st_size > 0
        finally:
            output_path.unlink()

    def test_generate_cfd_with_config(self, sample_data):
        """Génération avec configuration personnalisée."""
        pytest.importorskip("matplotlib")
        from scripts.reports.cfd import generate_cfd

        config = CFDConfig(title="Test CFD", dpi=72)

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            output_path = Path(f.name)

        try:
            result = generate_cfd(sample_data, config=config, output_path=output_path)
            assert result == output_path
            assert output_path.exists()
        finally:
            output_path.unlink()

    def test_generate_cfd_no_output(self, sample_data):
        """Génération sans fichier de sortie."""
        pytest.importorskip("matplotlib")
        from scripts.reports.cfd import generate_cfd

        result = generate_cfd(sample_data)
        assert result is None
