"""Tests for update_priority_scores module and lib functions."""

from datetime import date
from textwrap import dedent

import pytest

from scripts.lib.dates import parse_date
from scripts.lib.metadata import extract_field
from scripts.lib.wsjf import (
    WSJFConfig,
    calculate_age,
    calculate_urgency,
    calculate_wsjf_score,
)
from scripts.update_priority_scores import (
    Priority,
    TableRow,
    TaskMetadata,
    load_wsjf_config,
    parse_task_file,
    parse_tasks_table,
    parse_time_estimate,
    score_task,
    update_table_scores,
)


# =============================================================================
# Priority Enum Tests
# =============================================================================


class TestPriority:
    def test_from_label_high(self):
        assert Priority.from_label("🔴 Haute") == Priority.HIGH

    def test_from_label_medium(self):
        assert Priority.from_label("🟡 Moyenne") == Priority.MEDIUM

    def test_from_label_low(self):
        assert Priority.from_label("🟢 Basse") == Priority.LOW

    def test_from_label_unknown_defaults_to_medium(self):
        assert Priority.from_label("Unknown") == Priority.MEDIUM

    def test_priority_attributes(self):
        assert Priority.HIGH.score == 10
        assert Priority.HIGH.default_hours == 8.0
        assert Priority.MEDIUM.score == 5
        assert Priority.LOW.score == 2


# =============================================================================
# WSJFConfig Tests
# =============================================================================


class TestWSJFConfig:
    def test_default_values(self):
        config = WSJFConfig()
        assert config.age_divisor == 20.0
        assert config.age_max == 2.5
        assert config.urgency_overdue == 10.0

    def test_load_wsjf_config_missing_file(self, tmp_path):
        config = load_wsjf_config(tmp_path / "nonexistent.yml")
        assert config == WSJFConfig()

    def test_load_wsjf_config_partial(self, tmp_path):
        config_file = tmp_path / "config.yml"
        config_file.write_text("age_scoring:\n  divisor: 30\n")

        config = load_wsjf_config(config_file)
        assert config.age_divisor == 30
        assert config.age_max == 2.5  # default


# =============================================================================
# Scoring Logic Tests (Pure Functions)
# =============================================================================


class TestCalculateUrgency:
    @pytest.fixture
    def config(self):
        return WSJFConfig()

    @pytest.fixture
    def today(self):
        return date(2025, 11, 30)

    def test_no_target_date(self, today, config):
        assert calculate_urgency(None, today, config) == 0.0

    def test_overdue(self, today, config):
        target = date(2025, 11, 15)  # 15 days ago
        assert calculate_urgency(target, today, config) == 10.0

    def test_within_week(self, today, config):
        target = date(2025, 12, 3)  # 3 days from now
        assert calculate_urgency(target, today, config) == 5.0

    def test_within_month(self, today, config):
        target = date(2025, 12, 15)  # 15 days from now
        assert calculate_urgency(target, today, config) == 2.0

    def test_far_future(self, today, config):
        target = date(2026, 6, 1)  # 6 months from now
        assert calculate_urgency(target, today, config) == 0.0


class TestCalculateAge:
    @pytest.fixture
    def config(self):
        return WSJFConfig(age_divisor=20.0, age_max=2.5)

    @pytest.fixture
    def today(self):
        return date(2025, 11, 30)

    def test_no_created_date(self, today, config):
        assert calculate_age(None, today, config) == 0.0

    def test_new_task(self, today, config):
        created = date(2025, 11, 30)  # today
        assert calculate_age(created, today, config) == 0.0

    def test_20_days_old(self, today, config):
        created = date(2025, 11, 10)  # 20 days ago
        assert calculate_age(created, today, config) == 1.0

    def test_capped_at_max(self, today, config):
        created = date(2025, 1, 1)  # ~330 days ago
        assert calculate_age(created, today, config) == 2.5  # capped


class TestCalculateWsjfScore:
    @pytest.fixture
    def config(self):
        return WSJFConfig()

    def test_basic_calculation(self, config):
        # (10 + 5 + 1) / 4 = 4.0
        score = calculate_wsjf_score(
            priority_score=10, urgency=5.0, age=1.0, time_hours=4.0, config=config
        )
        assert score == 4.0

    def test_zero_time_uses_default(self, config):
        # (10 + 0 + 0) / 4.0 (default_hours from config) = 2.5
        score = calculate_wsjf_score(
            priority_score=10, urgency=0.0, age=0.0, time_hours=0.0, config=config
        )
        assert score == 2.5

    def test_rounding(self, config):
        # (5 + 2 + 1.5) / 3 = 2.833... -> 2.83
        score = calculate_wsjf_score(
            priority_score=5, urgency=2.0, age=1.5, time_hours=3.0, config=config
        )
        assert score == 2.83


class TestScoreTask:
    def test_score_task_integration(self):
        metadata = TaskMetadata(
            task_id="TEST-001",
            title="Test Task",
            status="⏳ À faire",
            priority=Priority.HIGH,
            time_estimate=4.0,
            created=date(2025, 11, 10),
            target=date(2025, 12, 5),
        )
        config = WSJFConfig()
        today = date(2025, 11, 30)

        scored = score_task(metadata, today, config)

        assert scored.task_id == "TEST-001"
        assert scored.priority == Priority.HIGH
        assert scored.priority_value == 10
        assert scored.urgency_value == 5.0  # within week
        assert scored.age_value == 1.0  # 20 days / 20
        assert scored.score == 4.0  # (10 + 5 + 1) / 4


# =============================================================================
# Parsing Tests
# =============================================================================


class TestParseDate:
    def test_valid_date(self):
        assert parse_date("2025-11-30") == date(2025, 11, 30)

    def test_empty_string(self):
        assert parse_date("") is None

    def test_dash(self):
        assert parse_date("-") is None

    def test_invalid_format(self):
        assert parse_date("30/11/2025") is None


class TestExtractField:
    def test_extract_existing_field(self):
        content = "| **Statut** | ⏳ À faire |"
        assert extract_field(content, "Statut") == "⏳ À faire"

    def test_extract_missing_field(self):
        content = "| **Statut** | ⏳ À faire |"
        assert extract_field(content, "Priority") == ""

    def test_extract_field_with_special_chars(self):
        content = "| **Créé le** | 2025-11-30 |"
        assert extract_field(content, "Créé le") == "2025-11-30"


class TestParseTimeEstimate:
    def test_parse_hours(self):
        assert parse_time_estimate("4h", Priority.MEDIUM) == 4.0

    def test_parse_decimal(self):
        assert parse_time_estimate("2.5 heures", Priority.MEDIUM) == 2.5

    def test_empty_uses_default(self):
        assert parse_time_estimate("", Priority.HIGH) == 8.0
        assert parse_time_estimate("", Priority.MEDIUM) == 4.0
        assert parse_time_estimate("", Priority.LOW) == 2.0


class TestParseTaskFile:
    def test_parse_pending_task(self, tmp_path):
        task_file = tmp_path / "TEST-001.md"
        task_file.write_text(
            dedent("""
            # TEST-001

            | **ID** | TEST-001 |
            | **Titre** | Test Task |
            | **Statut** | ⏳ À faire |
            | **Priorité** | 🔴 Haute |
            | **Temps estimé** | 4h |
            | **Créé le** | 2025-11-30 |
            | **Cible** | 2025-12-15 |
        """)
        )

        metadata = parse_task_file(task_file)

        assert metadata is not None
        assert metadata.task_id == "TEST-001"
        assert metadata.priority == Priority.HIGH
        assert metadata.time_estimate == 4.0

    def test_skip_completed_task(self, tmp_path):
        task_file = tmp_path / "TEST-002.md"
        task_file.write_text("| **Statut** | ✅ Terminé |")

        assert parse_task_file(task_file) is None

    def test_skip_in_progress_task(self, tmp_path):
        task_file = tmp_path / "TEST-003.md"
        task_file.write_text("| **Statut** | 🔄 En cours |")

        assert parse_task_file(task_file) is None


# =============================================================================
# Table Update Tests
# =============================================================================


class TestParseTasksTable:
    def test_parse_valid_table(self):
        content = dedent("""
            ## Tâches actives

            | ID | Titre | Statut | Priorité | Score | Créé le |
            |----|-------|--------|----------|-------|---------|
            | [TEST-001](tasks/TEST-001.md) | Test | ⏳ À faire | 🔴 Haute | 2.50 | 2025-11-30 |
        """)

        result = parse_tasks_table(content)

        assert result is not None
        header, rows, start, end = result
        assert len(rows) == 1
        assert rows[0].task_id == "TEST-001"
        assert rows[0].score == "2.50"

    def test_parse_missing_table(self):
        assert parse_tasks_table("No table here") is None


class TestUpdateTableScores:
    def test_update_scores(self):
        rows = [
            TableRow("A-001", "Task A", "⏳ À faire", "🔴", "1.00", "2025-01-01", "a.md"),
            TableRow("B-001", "Task B", "⏳ À faire", "🟡", "2.00", "2025-01-01", "b.md"),
        ]
        scores = {"A-001": 3.5, "B-001": 1.5}

        updated = update_table_scores(rows, scores)

        # Sorted by score descending
        assert updated[0].task_id == "A-001"
        assert updated[0].score == "3.50"
        assert updated[1].task_id == "B-001"
        assert updated[1].score == "1.50"

    def test_in_progress_stays_at_top(self):
        rows = [
            TableRow("A-001", "Task A", "⏳ À faire", "🔴", "1.00", "2025-01-01", "a.md"),
            TableRow("B-001", "Task B", "🔄 En cours", "🟡", "-", "2025-01-01", "b.md"),
        ]
        scores = {"A-001": 10.0}

        updated = update_table_scores(rows, scores)

        # In-progress task stays at top despite lower score
        assert updated[0].task_id == "B-001"
        assert updated[0].score == "-"


class TestTableRow:
    def test_to_markdown(self):
        row = TableRow(
            task_id="TEST-001",
            title="Test Task",
            status="⏳ À faire",
            priority="🔴 Haute",
            score="2.50",
            created="2025-11-30",
            link="tasks/TEST-001.md",
        )

        md = row.to_markdown()

        assert md == (
            "| [TEST-001](tasks/TEST-001.md) | Test Task | "
            "⏳ À faire | 🔴 Haute | 2.50 | 2025-11-30 |"
        )
