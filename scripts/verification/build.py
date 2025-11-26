"""Build verification module.

Verifies that the CV compiles successfully and generates a valid PDF.
"""

import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class BuildResult:
    """Result of build verification."""

    success: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    pdf_path: Path | None = None
    pdf_size: int = 0


def check_typst_installed() -> tuple[bool, str | None]:
    """Check if typst is installed and available."""
    if shutil.which("typst") is None:
        return False, "typst n'est pas installé ou pas dans le PATH"
    return True, None


def check_source_exists(project_root: Path) -> tuple[bool, str | None]:
    """Check if the CV source file exists."""
    cv_file = project_root / "src" / "cv.typ"
    if not cv_file.exists():
        return False, f"Fichier source introuvable: {cv_file}"
    return True, None


def compile_cv(project_root: Path) -> tuple[bool, str, str]:
    """Compile the CV and return success status, stdout, and stderr."""
    cv_file = project_root / "src" / "cv.typ"
    dist_dir = project_root / "dist"
    dist_dir.mkdir(exist_ok=True)
    pdf_path = dist_dir / "cv.pdf"

    result = subprocess.run(
        ["typst", "compile", str(cv_file), str(pdf_path)],
        capture_output=True,
        text=True,
    )

    return result.returncode == 0, result.stdout, result.stderr


def check_pdf_valid(project_root: Path) -> tuple[bool, str | None, int]:
    """Check if the generated PDF is valid."""
    pdf_path = project_root / "dist" / "cv.pdf"

    if not pdf_path.exists():
        return False, "Le PDF n'a pas été généré", 0

    size = pdf_path.stat().st_size
    if size == 0:
        return False, "Le PDF est vide", 0

    return True, None, size


def verify_build(project_root: Path | None = None) -> BuildResult:
    """Run all build verification checks.

    Args:
        project_root: Path to the project root. If None, uses current directory.

    Returns:
        BuildResult with verification results.
    """
    if project_root is None:
        project_root = Path.cwd()
    project_root = Path(project_root)

    result = BuildResult(success=True)

    # Check typst is installed
    ok, error = check_typst_installed()
    if not ok:
        result.errors.append(error)
        result.success = False
        return result

    # Check source file exists
    ok, error = check_source_exists(project_root)
    if not ok:
        result.errors.append(error)
        result.success = False
        return result

    # Compile
    ok, stdout, stderr = compile_cv(project_root)
    if not ok:
        result.errors.append(f"Échec de la compilation: {stderr}")
        result.success = False
        return result

    # Parse warnings from stderr
    if stderr:
        for line in stderr.split("\n"):
            if "warning:" in line.lower():
                result.warnings.append(line.strip())

    # Check PDF is valid
    ok, error, size = check_pdf_valid(project_root)
    if not ok:
        result.errors.append(error)
        result.success = False
        return result

    result.pdf_path = project_root / "dist" / "cv.pdf"
    result.pdf_size = size

    return result


def print_result(result: BuildResult) -> None:
    """Print build verification result to console."""
    print("=== Vérification de la compilation ===")
    print()

    if result.errors:
        for error in result.errors:
            print(f"ERREUR: {error}")
        print()
        print("=== Vérification de la compilation: ÉCHEC ===")
        return

    print("OK: Compilation réussie")

    if result.warnings:
        print()
        print("Avertissements:")
        for warning in result.warnings:
            print(f"  {warning}")

    if result.pdf_path:
        print(f"OK: PDF généré ({result.pdf_size} octets)")

    print()
    print("=== Vérification de la compilation: RÉUSSIE ===")


if __name__ == "__main__":
    import sys

    # Find project root (go up until we find src/cv.typ)
    current = Path.cwd()
    while current != current.parent:
        if (current / "src" / "cv.typ").exists():
            break
        current = current.parent
    else:
        current = Path.cwd()

    result = verify_build(current)
    print_result(result)
    sys.exit(0 if result.success else 1)
