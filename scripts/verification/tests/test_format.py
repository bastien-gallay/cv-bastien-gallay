"""Tests for format verification module."""

from pathlib import Path

import pytest

from scripts.verification.format import (
    FormatResult,
    check_contact_info,
    check_encoding_errors,
    check_french_chars,
    check_sections,
    check_trailing_whitespace,
    count_entries,
    verify_format,
)


class TestCheckSections:
    """Tests for check_sections function."""

    def test_all_sections_present(self):
        """Test when all required sections are present."""
        content = """
= Expérience
= Etudes
= Certifications
= Expertises
= Langues
"""
        found, missing = check_sections(content)
        assert len(found) == 5
        assert len(missing) == 0

    def test_some_sections_missing(self):
        """Test when some sections are missing."""
        content = """
= Expérience
= Etudes
"""
        found, missing = check_sections(content)
        assert "Expérience" in found
        assert "Etudes" in found
        assert "Certifications" in missing
        assert "Expertises" in missing
        assert "Langues" in missing

    def test_no_sections(self):
        """Test when no sections are present."""
        content = "Some random content"
        found, missing = check_sections(content)
        assert len(found) == 0
        assert len(missing) == 5


class TestCheckContactInfo:
    """Tests for check_contact_info function."""

    def test_all_contact_present(self):
        """Test when all contact info is present."""
        content = """
email: "test@example.com",
phone: "(+33) 06 12 34 56 78",
linkedin: "username",
"""
        found, missing = check_contact_info(content)
        assert len(found) == 3
        assert len(missing) == 0

    def test_email_missing(self):
        """Test when email is missing."""
        content = """
phone: "(+33) 06 12 34 56 78",
linkedin: "username",
"""
        found, missing = check_contact_info(content)
        assert "email" in missing
        assert "phone" in found
        assert "linkedin" in found

    def test_invalid_email(self):
        """Test when email format is invalid."""
        content = 'email: "not-an-email"'
        found, missing = check_contact_info(content)
        assert "email" in missing


class TestCountEntries:
    """Tests for count_entries function."""

    def test_count_multiple_entries(self):
        """Test counting multiple entries."""
        content = """
#entry(
  title: "Job 1",
)

#entry(
  title: "Job 2",
)

#entry(
  title: "Job 3",
)
"""
        count = count_entries(content)
        assert count == 3

    def test_no_entries(self):
        """Test when no entries exist."""
        content = "Some content without entries"
        count = count_entries(content)
        assert count == 0


class TestCheckTrailingWhitespace:
    """Tests for check_trailing_whitespace function."""

    def test_no_trailing_whitespace(self):
        """Test when no trailing whitespace exists."""
        content = "line1\nline2\nline3"
        count = check_trailing_whitespace(content)
        assert count == 0

    def test_with_trailing_whitespace(self):
        """Test when trailing whitespace exists."""
        content = "line1  \nline2\nline3\t"
        count = check_trailing_whitespace(content)
        assert count == 2


class TestCheckEncodingErrors:
    """Tests for check_encoding_errors function."""

    def test_no_encoding_errors(self):
        """Test when no encoding errors exist."""
        content = "Normal content with accents: éàù"
        assert check_encoding_errors(content) is False

    def test_with_encoding_errors(self):
        """Test when encoding errors exist."""
        content = "Content with ??? errors"
        assert check_encoding_errors(content) is True

    def test_few_question_marks(self):
        """Test that few question marks don't trigger error."""
        content = "Is this ok? Yes!"
        assert check_encoding_errors(content) is False


class TestCheckFrenchChars:
    """Tests for check_french_chars function."""

    def test_has_french_chars(self):
        """Test when French characters are present."""
        content = "Expérience professionnelle à Paris"
        assert check_french_chars(content) is True

    def test_no_french_chars(self):
        """Test when no French characters are present."""
        content = "Experience in Paris"
        assert check_french_chars(content) is False


class TestVerifyFormat:
    """Tests for verify_format function."""

    def test_verify_format_success(self, tmp_path: Path):
        """Test successful format verification."""
        cv_file = tmp_path / "src" / "cv.typ"
        cv_file.parent.mkdir(parents=True)
        cv_file.write_text(
            """
email: "test@example.com",
phone: "+33",
linkedin: "user",

= Expérience
#entry(title: "Job 1")
#entry(title: "Job 2")
#entry(title: "Job 3")
#entry(title: "Job 4")
#entry(title: "Job 5")

= Etudes
= Certifications
= Expertises
= Langues
"""
        )

        result = verify_format(tmp_path)
        assert result.success is True
        assert len(result.errors) == 0

    def test_verify_format_missing_email(self, tmp_path: Path):
        """Test format verification with missing email."""
        cv_file = tmp_path / "src" / "cv.typ"
        cv_file.parent.mkdir(parents=True)
        cv_file.write_text(
            """
phone: "+33",
= Expérience
"""
        )

        result = verify_format(tmp_path)
        assert result.success is False
        assert any("email" in e.lower() for e in result.errors)

    def test_verify_format_no_file(self, tmp_path: Path):
        """Test format verification when file doesn't exist."""
        result = verify_format(tmp_path)
        assert result.success is False
        assert any("introuvable" in e.lower() for e in result.errors)

    def test_verify_format_encoding_error(self, tmp_path: Path):
        """Test format verification with encoding errors."""
        cv_file = tmp_path / "src" / "cv.typ"
        cv_file.parent.mkdir(parents=True)
        cv_file.write_text(
            """
email: "test@example.com",
Content with ??? encoding errors
"""
        )

        result = verify_format(tmp_path)
        assert result.success is False
        assert any("encodage" in e.lower() for e in result.errors)


class TestFormatResult:
    """Tests for FormatResult dataclass."""

    def test_default_values(self):
        """Test default values of FormatResult."""
        result = FormatResult(success=True)
        assert result.success is True
        assert result.errors == []
        assert result.warnings == []
        assert result.sections_found == []
        assert result.entry_count == 0
        assert result.line_count == 0
        assert result.char_count == 0
