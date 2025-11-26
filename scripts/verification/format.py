"""Format verification module.

Verifies formatting and structure of the CV:
- Required sections present
- Contact information present
- No encoding issues
- Basic formatting checks
"""

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FormatResult:
    """Result of format verification."""

    success: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    sections_found: list[str] = field(default_factory=list)
    entry_count: int = 0
    line_count: int = 0
    char_count: int = 0


# Required sections in the CV
REQUIRED_SECTIONS = [
    "Expérience",
    "Etudes",
    "Certifications",
    "Expertises",
    "Langues",
]

# Patterns
EMAIL_PATTERN = re.compile(r"email:\s*[\"']?[\w.+-]+@[\w.-]+\.\w+[\"']?", re.IGNORECASE)
PHONE_PATTERN = re.compile(r"phone:", re.IGNORECASE)
LINKEDIN_PATTERN = re.compile(r"linkedin:", re.IGNORECASE)
ENTRY_PATTERN = re.compile(r"#entry\(")
TRAILING_WHITESPACE_PATTERN = re.compile(r"[ \t]+$", re.MULTILINE)
ENCODING_ERROR_PATTERN = re.compile(r"\?{3,}")
FRENCH_CHARS_PATTERN = re.compile(r"[éèêëàâäùûüîïôöç]", re.IGNORECASE)


def check_sections(content: str) -> tuple[list[str], list[str]]:
    """Check for required sections in the CV."""
    found = []
    missing = []

    for section in REQUIRED_SECTIONS:
        if section in content:
            found.append(section)
        else:
            missing.append(section)

    return found, missing


def check_contact_info(content: str) -> tuple[list[str], list[str]]:
    """Check for required contact information."""
    found = []
    missing = []

    if EMAIL_PATTERN.search(content):
        found.append("email")
    else:
        missing.append("email")

    if PHONE_PATTERN.search(content):
        found.append("phone")
    else:
        missing.append("phone")

    if LINKEDIN_PATTERN.search(content):
        found.append("linkedin")
    else:
        missing.append("linkedin")

    return found, missing


def count_entries(content: str) -> int:
    """Count the number of #entry() calls."""
    return len(ENTRY_PATTERN.findall(content))


def check_trailing_whitespace(content: str) -> int:
    """Count lines with trailing whitespace."""
    return len(TRAILING_WHITESPACE_PATTERN.findall(content))


def check_encoding_errors(content: str) -> bool:
    """Check for encoding error markers (???)."""
    return bool(ENCODING_ERROR_PATTERN.search(content))


def check_french_chars(content: str) -> bool:
    """Check if French accented characters are present."""
    return bool(FRENCH_CHARS_PATTERN.search(content))


def verify_format(project_root: Path | None = None) -> FormatResult:
    """Run all format verification checks.

    Args:
        project_root: Path to the project root. If None, uses current directory.

    Returns:
        FormatResult with verification results.
    """
    if project_root is None:
        project_root = Path.cwd()
    project_root = Path(project_root)

    result = FormatResult(success=True)
    cv_file = project_root / "src" / "cv.typ"

    if not cv_file.exists():
        result.errors.append(f"Fichier CV introuvable: {cv_file}")
        result.success = False
        return result

    content = cv_file.read_text(encoding="utf-8")

    # File statistics
    result.line_count = len(content.split("\n"))
    result.char_count = len(content)

    # Check sections
    found_sections, missing_sections = check_sections(content)
    result.sections_found = found_sections
    for section in missing_sections:
        result.warnings.append(f"Section '{section}' manquante")

    # Check contact info
    found_contact, missing_contact = check_contact_info(content)
    for item in missing_contact:
        if item == "email":
            result.errors.append("Email manquant ou invalide")
        else:
            result.warnings.append(f"{item.capitalize()} manquant")

    # Count entries
    result.entry_count = count_entries(content)
    if result.entry_count < 5:
        result.warnings.append(f"Peu d'entrées dans le CV ({result.entry_count})")

    # Check trailing whitespace
    trailing_ws = check_trailing_whitespace(content)
    if trailing_ws > 0:
        result.warnings.append(f"{trailing_ws} lignes avec espaces en fin de ligne")

    # Check encoding errors
    if check_encoding_errors(content):
        result.errors.append("Caractères d'encodage invalides (???) détectés")

    # Check French characters
    if not check_french_chars(content):
        result.warnings.append("Pas de caractères accentués détectés")

    # Set success based on errors
    result.success = len(result.errors) == 0

    return result


def print_result(result: FormatResult) -> None:
    """Print format verification result to console."""
    print("=== Vérification du formatage ===")
    print()

    print("1. Vérification des espaces...")
    ws_warnings = [w for w in result.warnings if "espaces en fin" in w]
    for w in ws_warnings:
        print(f"  ATTENTION: {w}")
    if not ws_warnings:
        print("  OK: Pas d'espaces en fin de ligne")

    print()
    print("2. Vérification de la structure...")
    for section in REQUIRED_SECTIONS:
        if section in result.sections_found:
            print(f"  OK: Section '{section}' présente")
        else:
            print(f"  ATTENTION: Section '{section}' manquante")

    print()
    print("3. Vérification des informations de contact...")
    for item in ["email", "phone", "linkedin"]:
        errors_for_item = [e for e in result.errors if item in e.lower()]
        warnings_for_item = [w for w in result.warnings if item in w.lower()]
        if errors_for_item:
            print(f"  ERREUR: {errors_for_item[0]}")
        elif warnings_for_item:
            print(f"  ATTENTION: {warnings_for_item[0]}")
        else:
            print(f"  OK: {item.capitalize()} présent")

    print()
    print("4. Vérification des entrées...")
    print(f"  Nombre d'entrées (#entry): {result.entry_count}")
    if result.entry_count < 5:
        print("  ATTENTION: Peu d'entrées dans le CV")

    print()
    print("5. Vérification des caractères spéciaux...")
    encoding_errors = [e for e in result.errors if "encodage" in e.lower()]
    if encoding_errors:
        print(f"  ERREUR: {encoding_errors[0]}")
    else:
        print("  OK: Pas de problème d'encodage")

    french_warnings = [w for w in result.warnings if "accentués" in w.lower()]
    if french_warnings:
        print(f"  ATTENTION: {french_warnings[0]}")
    else:
        print("  OK: Caractères français présents")

    print()
    print("6. Statistiques du fichier...")
    print(f"  Lignes: {result.line_count}")
    print(f"  Caractères: {result.char_count}")

    print()
    print("=== Résumé ===")
    print(f"Erreurs: {len(result.errors)}")
    print(f"Avertissements: {len(result.warnings)}")

    print()
    if result.success:
        print("=== Vérification du formatage: RÉUSSIE ===")
    else:
        print("=== Vérification du formatage: ÉCHEC ===")


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

    result = verify_format(current)
    print_result(result)
    sys.exit(0 if result.success else 1)
