"""Tests for build verification module."""

import shutil
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from scripts.verification.build import (
    BuildResult,
    check_pdf_valid,
    check_source_exists,
    check_typst_installed,
    compile_cv,
    verify_build,
)


class TestCheckTypstInstalled:
    """Tests for check_typst_installed function."""

    def test_typst_installed(self):
        """Test when typst is installed."""
        with patch.object(shutil, "which", return_value="/usr/bin/typst"):
            ok, error = check_typst_installed()
            assert ok is True
            assert error is None

    def test_typst_not_installed(self):
        """Test when typst is not installed."""
        with patch.object(shutil, "which", return_value=None):
            ok, error = check_typst_installed()
            assert ok is False
            assert "typst" in error.lower()


class TestCheckSourceExists:
    """Tests for check_source_exists function."""

    def test_source_exists(self, tmp_path: Path):
        """Test when source file exists."""
        cv_file = tmp_path / "src" / "cv.typ"
        cv_file.parent.mkdir(parents=True)
        cv_file.write_text("// CV content")

        ok, error = check_source_exists(tmp_path)
        assert ok is True
        assert error is None

    def test_source_not_exists(self, tmp_path: Path):
        """Test when source file doesn't exist."""
        ok, error = check_source_exists(tmp_path)
        assert ok is False
        assert "introuvable" in error.lower()


class TestCompileCv:
    """Tests for compile_cv function."""

    def test_compile_success(self, tmp_path: Path):
        """Test successful compilation."""
        cv_file = tmp_path / "src" / "cv.typ"
        cv_file.parent.mkdir(parents=True)
        cv_file.write_text('#import "@preview/neat-cv:0.4.0": cv\n#show: cv.with()')

        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = ""
        mock_result.stderr = ""

        with patch("subprocess.run", return_value=mock_result):
            ok, stdout, stderr = compile_cv(tmp_path)
            assert ok is True

    def test_compile_failure(self, tmp_path: Path):
        """Test compilation failure."""
        cv_file = tmp_path / "src" / "cv.typ"
        cv_file.parent.mkdir(parents=True)
        cv_file.write_text("invalid typst content")

        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "error: syntax error"

        with patch("subprocess.run", return_value=mock_result):
            ok, stdout, stderr = compile_cv(tmp_path)
            assert ok is False
            assert "error" in stderr.lower()


class TestCheckPdfValid:
    """Tests for check_pdf_valid function."""

    def test_pdf_exists_and_valid(self, tmp_path: Path):
        """Test when PDF exists and is valid."""
        pdf_path = tmp_path / "dist" / "cv.pdf"
        pdf_path.parent.mkdir(parents=True)
        pdf_path.write_bytes(b"%PDF-1.4 dummy content")

        ok, error, size = check_pdf_valid(tmp_path)
        assert ok is True
        assert error is None
        assert size > 0

    def test_pdf_not_exists(self, tmp_path: Path):
        """Test when PDF doesn't exist."""
        ok, error, size = check_pdf_valid(tmp_path)
        assert ok is False
        assert "n'a pas été généré" in error.lower()
        assert size == 0

    def test_pdf_empty(self, tmp_path: Path):
        """Test when PDF is empty."""
        pdf_path = tmp_path / "dist" / "cv.pdf"
        pdf_path.parent.mkdir(parents=True)
        pdf_path.write_bytes(b"")

        ok, error, size = check_pdf_valid(tmp_path)
        assert ok is False
        assert "vide" in error.lower()


class TestVerifyBuild:
    """Tests for verify_build function."""

    def test_verify_build_success(self, tmp_path: Path):
        """Test successful build verification."""
        # Setup
        cv_file = tmp_path / "src" / "cv.typ"
        cv_file.parent.mkdir(parents=True)
        cv_file.write_text("// CV content")

        pdf_path = tmp_path / "dist" / "cv.pdf"
        pdf_path.parent.mkdir(parents=True)
        pdf_path.write_bytes(b"%PDF-1.4 dummy")

        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = ""
        mock_result.stderr = ""

        with (
            patch.object(shutil, "which", return_value="/usr/bin/typst"),
            patch("subprocess.run", return_value=mock_result),
        ):
            result = verify_build(tmp_path)

        assert result.success is True
        assert len(result.errors) == 0
        assert result.pdf_size > 0

    def test_verify_build_no_typst(self, tmp_path: Path):
        """Test build verification when typst not installed."""
        with patch.object(shutil, "which", return_value=None):
            result = verify_build(tmp_path)

        assert result.success is False
        assert len(result.errors) > 0
        assert any("typst" in e.lower() for e in result.errors)

    def test_verify_build_no_source(self, tmp_path: Path):
        """Test build verification when source doesn't exist."""
        with patch.object(shutil, "which", return_value="/usr/bin/typst"):
            result = verify_build(tmp_path)

        assert result.success is False
        assert any("introuvable" in e.lower() for e in result.errors)


class TestBuildResult:
    """Tests for BuildResult dataclass."""

    def test_default_values(self):
        """Test default values of BuildResult."""
        result = BuildResult(success=True)
        assert result.success is True
        assert result.errors == []
        assert result.warnings == []
        assert result.pdf_path is None
        assert result.pdf_size == 0

    def test_with_errors(self):
        """Test BuildResult with errors."""
        result = BuildResult(
            success=False,
            errors=["Error 1", "Error 2"],
        )
        assert result.success is False
        assert len(result.errors) == 2
