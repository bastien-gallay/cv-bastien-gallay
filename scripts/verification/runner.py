"""Verification runner module.

Runs all verification checks and provides a summary.
"""

from dataclasses import dataclass, field
from pathlib import Path

from .build import BuildResult, print_result as print_build_result, verify_build
from .dates import DatesResult, print_result as print_dates_result, verify_dates
from .format import FormatResult, print_result as print_format_result, verify_format


@dataclass
class AllVerificationsResult:
    """Result of all verifications."""

    success: bool
    build_result: BuildResult | None = None
    dates_result: DatesResult | None = None
    format_result: FormatResult | None = None
    failed_checks: list[str] = field(default_factory=list)


def run_all_verifications(
    project_root: Path | None = None,
    verbose: bool = True,
) -> AllVerificationsResult:
    """Run all verification checks.

    Args:
        project_root: Path to the project root. If None, uses current directory.
        verbose: If True, print results to console.

    Returns:
        AllVerificationsResult with all verification results.
    """
    if project_root is None:
        project_root = Path.cwd()
    project_root = Path(project_root)

    result = AllVerificationsResult(success=True)

    if verbose:
        print("=" * 42)
        print("     VÉRIFICATION COMPLÈTE DU CV")
        print("=" * 42)
        print()

    # Build verification
    if verbose:
        print("-" * 42)
    result.build_result = verify_build(project_root)
    if verbose:
        print_build_result(result.build_result)
    if not result.build_result.success:
        result.failed_checks.append("build")

    # Dates verification
    if verbose:
        print()
        print("-" * 42)
    result.dates_result = verify_dates(project_root)
    if verbose:
        print_dates_result(result.dates_result)
    if not result.dates_result.success:
        result.failed_checks.append("dates")

    # Format verification
    if verbose:
        print()
        print("-" * 42)
    result.format_result = verify_format(project_root)
    if verbose:
        print_format_result(result.format_result)
    if not result.format_result.success:
        result.failed_checks.append("format")

    # Overall success
    result.success = len(result.failed_checks) == 0

    if verbose:
        print()
        print("=" * 42)
        print("     RÉSUMÉ FINAL")
        print("=" * 42)
        print()

        if result.success:
            print("Toutes les vérifications ont réussi!")
            print()
            print("Checklist manuelle: voir VERIFICATION.md")
        else:
            print(f"ÉCHEC: {len(result.failed_checks)} vérification(s) ont échoué")
            for check in result.failed_checks:
                print(f"  - {check}")
            print()
            print("Corrigez les erreurs et relancez la vérification.")

        print()

    return result
