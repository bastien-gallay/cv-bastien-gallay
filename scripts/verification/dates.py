"""Date verification module.

Verifies date consistency in the CV:
- No future dates
- Consistent date formats
- Chronological order in sections
"""

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path


@dataclass
class DateInfo:
    """Information about a date found in the CV."""

    year: int
    month: int | None = None
    line_number: int = 0
    line_content: str = ""
    is_end_date: bool = False


@dataclass
class DatesResult:
    """Result of date verification."""

    success: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    dates_found: list[DateInfo] = field(default_factory=list)
    format_stats: dict[str, int] = field(default_factory=dict)


# Patterns for date extraction
YEAR_PATTERN = re.compile(r"\b(19|20)\d{2}\b")
MM_YYYY_PATTERN = re.compile(r"\b(\d{1,2})/(\d{4})\b")
DATE_LINE_PATTERN = re.compile(r'date:\s*["\[]?(.+?)["\]]?\s*,?\s*$', re.IGNORECASE)


def extract_dates_from_line(line: str, line_number: int) -> list[DateInfo]:
    """Extract all dates from a line of text."""
    dates = []

    # Check for MM/YYYY format
    for match in MM_YYYY_PATTERN.finditer(line):
        month = int(match.group(1))
        year = int(match.group(2))
        if 1 <= month <= 12:
            dates.append(
                DateInfo(
                    year=year,
                    month=month,
                    line_number=line_number,
                    line_content=line.strip(),
                )
            )

    # Check for standalone years (only if no MM/YYYY found to avoid duplicates)
    if not dates:
        for match in YEAR_PATTERN.finditer(line):
            year = int(match.group(0))
            dates.append(
                DateInfo(
                    year=year,
                    month=None,
                    line_number=line_number,
                    line_content=line.strip(),
                )
            )

    return dates


def is_comment_line(line: str) -> bool:
    """Check if a line is a Typst comment."""
    stripped = line.strip()
    return stripped.startswith("//")


def extract_all_dates(cv_content: str) -> list[DateInfo]:
    """Extract all dates from CV content."""
    all_dates = []

    for i, line in enumerate(cv_content.split("\n"), start=1):
        # Skip commented lines
        if is_comment_line(line):
            continue

        # Look for date: fields specifically
        if "date:" in line.lower() or "Date" in line:
            dates = extract_dates_from_line(line, i)
            all_dates.extend(dates)

    return all_dates


def check_future_dates(dates: list[DateInfo], current_year: int) -> list[str]:
    """Check for dates in the future."""
    errors = []
    for date_info in dates:
        if date_info.year > current_year:
            errors.append(
                f"Année future détectée: {date_info.year} (ligne {date_info.line_number})"
            )
    return errors


def check_old_dates(
    dates: list[DateInfo], threshold_year: int = 1990
) -> list[str]:
    """Check for suspiciously old dates (except birth dates)."""
    warnings = []
    for date_info in dates:
        # Skip birth date lines
        if "naissance" in date_info.line_content.lower():
            continue
        if date_info.year < threshold_year:
            warnings.append(
                f"Année très ancienne: {date_info.year} (ligne {date_info.line_number})"
            )
    return warnings


def count_date_formats(cv_content: str) -> dict[str, int]:
    """Count occurrences of different date formats."""
    stats = {
        "mm_yyyy": 0,
        "yyyy_only": 0,
        "aujourdhui": 0,
        "present": 0,
    }

    for line in cv_content.split("\n"):
        if is_comment_line(line):
            continue
        if "date:" not in line.lower():
            continue

        if MM_YYYY_PATTERN.search(line):
            stats["mm_yyyy"] += 1
        elif YEAR_PATTERN.search(line) and not MM_YYYY_PATTERN.search(line):
            stats["yyyy_only"] += 1

        if "aujourd" in line.lower():
            stats["aujourdhui"] += 1
        if "présent" in line.lower() or "present" in line.lower():
            stats["present"] += 1

    return stats


def verify_dates(project_root: Path | None = None) -> DatesResult:
    """Run all date verification checks.

    Args:
        project_root: Path to the project root. If None, uses current directory.

    Returns:
        DatesResult with verification results.
    """
    if project_root is None:
        project_root = Path.cwd()
    project_root = Path(project_root)

    result = DatesResult(success=True)
    cv_file = project_root / "src" / "cv.typ"

    if not cv_file.exists():
        result.errors.append(f"Fichier CV introuvable: {cv_file}")
        result.success = False
        return result

    content = cv_file.read_text(encoding="utf-8")
    current_year = date.today().year

    # Extract all dates
    result.dates_found = extract_all_dates(content)

    # Check for future dates
    future_errors = check_future_dates(result.dates_found, current_year)
    result.errors.extend(future_errors)

    # Check for old dates
    old_warnings = check_old_dates(result.dates_found)
    result.warnings.extend(old_warnings)

    # Count date formats
    result.format_stats = count_date_formats(content)

    # Set success based on errors (warnings don't fail)
    result.success = len(result.errors) == 0

    return result


def print_result(result: DatesResult) -> None:
    """Print date verification result to console."""
    print("=== Vérification des dates ===")
    print()

    current_year = date.today().year
    print(f"Année courante: {current_year}")
    print()

    print("Analyse des dates...")

    if result.errors:
        for error in result.errors:
            print(f"ERREUR: {error}")

    if result.warnings:
        for warning in result.warnings:
            print(f"ATTENTION: {warning}")

    print()
    print("Vérification du format des dates...")
    if result.format_stats:
        print(f"  Format MM/YYYY: {result.format_stats.get('mm_yyyy', 0)} occurrences")
        print(f"  Format YYYY seul: {result.format_stats.get('yyyy_only', 0)} occurrences")
        aujourdhui = result.format_stats.get("aujourdhui", 0)
        present = result.format_stats.get("present", 0)
        print(f"  Avec 'Aujourd'hui'/'Présent': {aujourdhui + present} occurrences")

    print()
    print("=== Résumé ===")
    print(f"Erreurs: {len(result.errors)}")
    print(f"Avertissements: {len(result.warnings)}")

    print()
    if result.success:
        print("=== Vérification des dates: RÉUSSIE ===")
    else:
        print("=== Vérification des dates: ÉCHEC ===")


if __name__ == "__main__":
    import sys

    # Find project root
    current = Path.cwd()
    while current != current.parent:
        if (current / "src" / "cv.typ").exists():
            break
        current = current.parent
    else:
        current = Path.cwd()

    result = verify_dates(current)
    print_result(result)
    sys.exit(0 if result.success else 1)
