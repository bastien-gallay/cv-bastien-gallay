from dataclasses import dataclass, field
from pathlib import Path

import pytest

from scripts.lib import (
    Context,
    Result,
    ValidatedContent,
    is_non_empty_content,
    is_valid_project_root,
)


class TestIsValidProjectRoot:
    def test_valid_when_cv_exists(self, tmp_path: Path):
        (tmp_path / "src").mkdir()
        (tmp_path / "src" / "cv.typ").touch()
        assert is_valid_project_root(tmp_path) is True

    def test_invalid_when_cv_missing(self, tmp_path: Path):
        assert is_valid_project_root(tmp_path) is False

    def test_invalid_when_src_missing(self, tmp_path: Path):
        (tmp_path / "cv.typ").touch()
        assert is_valid_project_root(tmp_path) is False


class TestIsNonEmptyContent:
    def test_valid_with_content(self):
        assert is_non_empty_content("hello") is True

    def test_invalid_when_empty(self):
        assert is_non_empty_content("") is False

    def test_invalid_when_whitespace_only(self):
        assert is_non_empty_content("   \n\t  ") is False


class TestResult:
    def test_default_values(self):
        result: Result[str] = Result(success=True)
        assert result.success is True
        assert result.data is None
        assert result.errors == []
        assert result.warnings == []

    def test_with_data(self):
        result: Result[int] = Result(success=True, data=42)
        assert result.data == 42

    def test_add_error_sets_success_false(self):
        result: Result[str] = Result(success=True)
        result.add_error("une erreur")
        assert result.success is False
        assert "une erreur" in result.errors

    def test_add_error_returns_self(self):
        result: Result[str] = Result(success=True)
        returned = result.add_error("erreur")
        assert returned is result

    def test_add_warning_keeps_success(self):
        result: Result[str] = Result(success=True)
        result.add_warning("attention")
        assert result.success is True
        assert "attention" in result.warnings

    def test_add_warning_returns_self(self):
        result: Result[str] = Result(success=True)
        returned = result.add_warning("warning")
        assert returned is result

    def test_chained_operations(self):
        result: Result[str] = Result(success=True)
        result.add_warning("w1").add_warning("w2").add_error("e1")
        assert result.warnings == ["w1", "w2"]
        assert result.errors == ["e1"]
        assert result.success is False


@dataclass
class MockResult:
    success: bool
    errors: list[str] = field(default_factory=list)


@dataclass
class MockContext(Context[str, MockResult]):
    pass


class TestContext:
    def test_bind_executes_on_success(self):
        ctx = MockContext(data="test", result=MockResult(success=True))

        def add_suffix(c: MockContext) -> MockContext:
            c.data = c.data + "_modified"
            return c

        result = ctx.bind(add_suffix)
        assert result.data == "test_modified"

    def test_bind_short_circuits_on_failure(self):
        ctx = MockContext(data="test", result=MockResult(success=False))

        def should_not_run(c: MockContext) -> MockContext:
            c.data = "should not appear"
            return c

        result = ctx.bind(should_not_run)
        assert result.data == "test"

    def test_map_always_executes(self):
        ctx = MockContext(data="test", result=MockResult(success=True))

        def transform(c: MockContext) -> MockContext:
            c.data = c.data.upper()
            return c

        result = ctx.map(transform)
        assert result.data == "TEST"

    def test_map_executes_even_on_failure(self):
        ctx = MockContext(data="test", result=MockResult(success=False))

        def transform(c: MockContext) -> MockContext:
            c.data = c.data.upper()
            return c

        result = ctx.map(transform)
        assert result.data == "TEST"

    def test_chained_bind_stops_after_failure(self):
        ctx = MockContext(data="test", result=MockResult(success=True))

        def fail_step(c: MockContext) -> MockContext:
            c.result.success = False
            c.data = c.data + "_failed"
            return c

        def should_not_run(c: MockContext) -> MockContext:
            c.data = c.data + "_after"
            return c

        result = ctx.bind(fail_step).bind(should_not_run)
        assert result.data == "test_failed"
        assert "_after" not in result.data

    def test_chained_map_always_runs(self):
        ctx = MockContext(data="a", result=MockResult(success=True))

        result = (
            ctx.map(lambda c: MockContext(data=c.data + "b", result=c.result))
            .map(lambda c: MockContext(data=c.data + "c", result=c.result))
            .map(lambda c: MockContext(data=c.data + "d", result=c.result))
        )
        assert result.data == "abcd"

    def test_mixed_bind_and_map(self):
        ctx = MockContext(data="start", result=MockResult(success=True))

        def fail_bind(c: MockContext) -> MockContext:
            c.result.success = False
            c.result.errors.append("failed")
            return c

        def map_upper(c: MockContext) -> MockContext:
            c.data = c.data.upper()
            return c

        def bind_after(c: MockContext) -> MockContext:
            c.data = c.data + "_bound"
            return c

        result = ctx.map(map_upper).bind(fail_bind).bind(bind_after).map(map_upper)
        assert result.result.success is False
        assert "failed" in result.result.errors
        assert "_bound" not in result.data


class TestValidatedContentType:
    def test_can_create_validated_content(self):
        content = ValidatedContent("some content")
        assert content == "some content"

    def test_validated_content_is_str(self):
        content = ValidatedContent("test")
        assert isinstance(content, str)


# Tests for dates module
from datetime import date

from scripts.lib.dates import parse_date


class TestParseDate:
    def test_valid_iso_date(self):
        result = parse_date("2025-11-30")
        assert result == date(2025, 11, 30)

    def test_valid_date_with_whitespace(self):
        result = parse_date("  2025-01-15  ")
        assert result == date(2025, 1, 15)

    def test_empty_string_returns_none(self):
        assert parse_date("") is None

    def test_dash_returns_none(self):
        assert parse_date("-") is None

    def test_whitespace_only_returns_none(self):
        assert parse_date("   ") is None

    def test_invalid_format_returns_none(self):
        assert parse_date("30/11/2025") is None

    def test_invalid_date_returns_none(self):
        assert parse_date("2025-13-45") is None

    def test_text_returns_none(self):
        assert parse_date("not a date") is None


# Tests for metadata module
from scripts.lib.metadata import extract_field, extract_metadata_table


class TestExtractMetadataTable:
    def test_extract_single_field(self):
        content = "| **Statut** | En cours |"
        result = extract_metadata_table(content)
        assert result == {"Statut": "En cours"}

    def test_extract_multiple_fields(self):
        content = """| **Statut** | En cours |
| **Priorité** | Haute |
| **Auteur** | Test |"""
        result = extract_metadata_table(content)
        assert result == {
            "Statut": "En cours",
            "Priorité": "Haute",
            "Auteur": "Test",
        }

    def test_ignores_separator_rows(self):
        content = """| **Champ** | Valeur |
| --- | --- |
| **Autre** | Data |"""
        result = extract_metadata_table(content)
        assert result == {"Champ": "Valeur", "Autre": "Data"}

    def test_strips_whitespace(self):
        content = "|   **Champ**   |   Valeur avec espaces   |"
        result = extract_metadata_table(content)
        assert result == {"Champ": "Valeur avec espaces"}

    def test_empty_content_returns_empty_dict(self):
        assert extract_metadata_table("") == {}

    def test_no_matches_returns_empty_dict(self):
        content = "Just some text without tables"
        assert extract_metadata_table(content) == {}


class TestExtractField:
    def test_extract_existing_field(self):
        content = "| **Statut** | À faire |"
        result = extract_field(content, "Statut")
        assert result == "À faire"

    def test_extract_missing_field_returns_empty(self):
        content = "| **Statut** | En cours |"
        result = extract_field(content, "Priorité")
        assert result == ""

    def test_extract_field_with_special_chars(self):
        content = "| **Temps estimé** | 4h |"
        result = extract_field(content, "Temps estimé")
        assert result == "4h"

    def test_extract_field_strips_value(self):
        content = "|  **Champ**  |   valeur   |"
        result = extract_field(content, "Champ")
        assert result == "valeur"


# Tests for wsjf module
from scripts.lib.wsjf import (
    WSJFConfig,
    calculate_age,
    calculate_urgency,
    calculate_wsjf_score,
)


class TestWSJFConfig:
    def test_default_values(self):
        config = WSJFConfig()
        assert config.age_divisor == 20.0
        assert config.age_max == 2.5
        assert config.urgency_overdue == 10.0
        assert config.urgency_week == 5.0
        assert config.urgency_month == 2.0
        assert config.default_hours == 4.0

    def test_custom_values(self):
        config = WSJFConfig(age_divisor=10.0, age_max=5.0)
        assert config.age_divisor == 10.0
        assert config.age_max == 5.0

    def test_frozen(self):
        config = WSJFConfig()
        with pytest.raises(Exception):
            config.age_divisor = 30.0


class TestCalculateUrgency:
    def test_no_target_returns_zero(self):
        config = WSJFConfig()
        assert calculate_urgency(None, date(2025, 11, 30), config) == 0.0

    def test_overdue_returns_overdue_value(self):
        config = WSJFConfig()
        today = date(2025, 11, 30)
        target = date(2025, 11, 25)  # 5 days ago
        assert calculate_urgency(target, today, config) == 10.0

    def test_within_week_returns_week_value(self):
        config = WSJFConfig()
        today = date(2025, 11, 30)
        target = date(2025, 12, 3)  # 3 days from now
        assert calculate_urgency(target, today, config) == 5.0

    def test_within_month_returns_month_value(self):
        config = WSJFConfig()
        today = date(2025, 11, 30)
        target = date(2025, 12, 15)  # 15 days from now
        assert calculate_urgency(target, today, config) == 2.0

    def test_far_future_returns_zero(self):
        config = WSJFConfig()
        today = date(2025, 11, 30)
        target = date(2026, 3, 1)  # 3 months away
        assert calculate_urgency(target, today, config) == 0.0


class TestCalculateAge:
    def test_no_created_date_returns_zero(self):
        config = WSJFConfig()
        assert calculate_age(None, date(2025, 11, 30), config) == 0.0

    def test_new_task_returns_low_value(self):
        config = WSJFConfig()
        today = date(2025, 11, 30)
        created = date(2025, 11, 28)  # 2 days old
        result = calculate_age(created, today, config)
        assert result == 2 / 20.0  # 0.1

    def test_20_days_old_returns_one(self):
        config = WSJFConfig()
        today = date(2025, 11, 30)
        created = date(2025, 11, 10)  # 20 days old
        result = calculate_age(created, today, config)
        assert result == 1.0

    def test_capped_at_max(self):
        config = WSJFConfig()
        today = date(2025, 11, 30)
        created = date(2025, 1, 1)  # ~330 days old
        result = calculate_age(created, today, config)
        assert result == 2.5  # capped at age_max


class TestCalculateWsjfScore:
    def test_basic_calculation(self):
        config = WSJFConfig()
        # (10 + 5 + 1) / 4 = 4.0
        result = calculate_wsjf_score(10.0, 5.0, 1.0, 4.0, config)
        assert result == 4.0

    def test_zero_time_uses_default(self):
        config = WSJFConfig()
        # (10 + 0 + 0) / 4 (default) = 2.5
        result = calculate_wsjf_score(10.0, 0.0, 0.0, 0.0, config)
        assert result == 2.5

    def test_negative_time_uses_default(self):
        config = WSJFConfig()
        result = calculate_wsjf_score(10.0, 0.0, 0.0, -2.0, config)
        assert result == 2.5

    def test_rounding(self):
        config = WSJFConfig()
        # (10 + 5 + 1) / 3 = 5.333...
        result = calculate_wsjf_score(10.0, 5.0, 1.0, 3.0, config)
        assert result == 5.33
