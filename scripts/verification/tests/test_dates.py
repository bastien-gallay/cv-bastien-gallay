"""Tests for dates verification module."""

from pathlib import Path

import pytest

from scripts.verification.dates import (
    DateInfo,
    DatesResult,
    check_future_dates,
    check_old_dates,
    count_date_formats,
    extract_all_dates,
    extract_dates_from_line,
    is_comment_line,
    verify_dates,
)


class TestExtractDatesFromLine:
    """Tests for extract_dates_from_line function."""

    def test_mm_yyyy_format(self):
        """Test extraction of MM/YYYY format."""
        dates = extract_dates_from_line('date: "02/2021 - 10/2025"', 1)
        assert len(dates) == 2
        assert dates[0].year == 2021
        assert dates[0].month == 2
        assert dates[1].year == 2025
        assert dates[1].month == 10

    def test_yyyy_only_format(self):
        """Test extraction of YYYY only format."""
        dates = extract_dates_from_line('date: "2022"', 1)
        assert len(dates) == 1
        assert dates[0].year == 2022
        assert dates[0].month is None

    def test_invalid_month(self):
        """Test that invalid months are skipped."""
        # Month 13 is invalid
        dates = extract_dates_from_line('date: "13/2021"', 1)
        # Should fall back to year-only extraction
        assert len(dates) == 1
        assert dates[0].year == 2021

    def test_no_dates(self):
        """Test line with no dates."""
        dates = extract_dates_from_line("title: Senior Developer", 1)
        assert len(dates) == 0

    def test_line_number_stored(self):
        """Test that line number is stored correctly."""
        dates = extract_dates_from_line('date: "2020"', 42)
        assert dates[0].line_number == 42


class TestIsCommentLine:
    """Tests for is_comment_line function."""

    def test_comment_line(self):
        """Test detection of comment lines."""
        assert is_comment_line("// This is a comment") is True
        assert is_comment_line("  // Indented comment") is True

    def test_not_comment_line(self):
        """Test non-comment lines."""
        assert is_comment_line("date: 2021") is False
        assert is_comment_line("") is False


class TestExtractAllDates:
    """Tests for extract_all_dates function."""

    def test_extract_from_cv_content(self):
        """Test extraction from CV-like content."""
        content = """
#entry(
  title: "Developer",
  date: "02/2021 - 10/2025",
)
// date: "commented out"
#entry(
  title: "Education",
  date: "2020",
)
"""
        dates = extract_all_dates(content)
        # Should find dates from non-commented lines only
        assert len(dates) >= 2

    def test_skip_comments(self):
        """Test that commented dates are skipped."""
        content = """
// date: "01/2020 - 12/2020"
date: "01/2021"
"""
        dates = extract_all_dates(content)
        # Only the uncommented date
        assert len(dates) == 1
        assert dates[0].year == 2021


class TestCheckFutureDates:
    """Tests for check_future_dates function."""

    def test_no_future_dates(self):
        """Test when no future dates exist."""
        dates = [
            DateInfo(year=2020, line_number=1, line_content=""),
            DateInfo(year=2023, line_number=2, line_content=""),
        ]
        errors = check_future_dates(dates, current_year=2025)
        assert len(errors) == 0

    def test_with_future_dates(self):
        """Test when future dates exist."""
        dates = [
            DateInfo(year=2025, line_number=1, line_content=""),
            DateInfo(year=2030, line_number=2, line_content=""),
        ]
        errors = check_future_dates(dates, current_year=2025)
        assert len(errors) == 1
        assert "2030" in errors[0]


class TestCheckOldDates:
    """Tests for check_old_dates function."""

    def test_no_old_dates(self):
        """Test when no old dates exist."""
        dates = [
            DateInfo(year=2000, line_number=1, line_content="date: 2000"),
            DateInfo(year=2020, line_number=2, line_content="date: 2020"),
        ]
        warnings = check_old_dates(dates, threshold_year=1990)
        assert len(warnings) == 0

    def test_with_old_dates(self):
        """Test when old dates exist."""
        dates = [
            DateInfo(year=1985, line_number=1, line_content="date: 1985"),
        ]
        warnings = check_old_dates(dates, threshold_year=1990)
        assert len(warnings) == 1
        assert "1985" in warnings[0]

    def test_skip_birth_date(self):
        """Test that birth dates are skipped."""
        dates = [
            DateInfo(
                year=1979,
                line_number=1,
                line_content="Date de naissance : 3/03/1979",
            ),
        ]
        warnings = check_old_dates(dates, threshold_year=1990)
        assert len(warnings) == 0


class TestCountDateFormats:
    """Tests for count_date_formats function."""

    def test_count_formats(self):
        """Test counting of different date formats."""
        content = """
date: "02/2021 - 10/2025",
date: "2022",
date: "01/2020 - Aujourd'hui",
// date: "ignored"
"""
        stats = count_date_formats(content)
        assert stats["mm_yyyy"] >= 1
        assert stats["yyyy_only"] >= 1
        assert stats["aujourdhui"] >= 1


class TestVerifyDates:
    """Tests for verify_dates function."""

    def test_verify_dates_success(self, tmp_path: Path):
        """Test successful date verification."""
        cv_file = tmp_path / "src" / "cv.typ"
        cv_file.parent.mkdir(parents=True)
        cv_file.write_text(
            """
date: "02/2021 - 10/2025",
date: "2020",
"""
        )

        result = verify_dates(tmp_path)
        assert result.success is True
        assert len(result.errors) == 0

    def test_verify_dates_future(self, tmp_path: Path):
        """Test date verification with future dates."""
        cv_file = tmp_path / "src" / "cv.typ"
        cv_file.parent.mkdir(parents=True)
        cv_file.write_text('date: "2050"')

        result = verify_dates(tmp_path)
        assert result.success is False
        assert any("future" in e.lower() for e in result.errors)

    def test_verify_dates_no_file(self, tmp_path: Path):
        """Test date verification when file doesn't exist."""
        result = verify_dates(tmp_path)
        assert result.success is False
        assert any("introuvable" in e.lower() for e in result.errors)


class TestDatesResult:
    """Tests for DatesResult dataclass."""

    def test_default_values(self):
        """Test default values of DatesResult."""
        result = DatesResult(success=True)
        assert result.success is True
        assert result.errors == []
        assert result.warnings == []
        assert result.dates_found == []
        assert result.format_stats == {}
