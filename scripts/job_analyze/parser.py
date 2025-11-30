"""Job posting parser - extracts structured information from job postings."""

import re
from dataclasses import dataclass, field

# =============================================================================
# Constants - Section Patterns
# =============================================================================

# Section header patterns (FR/EN)
REQUIREMENTS_SECTION_PATTERNS = [
    r"(?:Requirements|Exigences|Must-have|Compétences\s+techniques\s+recherchées|Profil\s+recherché)"
    r".*?(?=\n\n(?:[A-Z]|Compétences\s+humaines)|Compétences\s+humaines|\Z)",
]

NICE_TO_HAVE_SECTION_PATTERNS = [
    r"(?:Nice-to-have|Souhaité|Optional|Bonus|Plus).*?(?=\n\n|\n[A-Z]|\Z)",
]

RESPONSIBILITIES_SECTION_PATTERNS = [
    r"(?:Responsibilities|Responsabilités|Missions?\s+principales?|What you.ll do|Your role|Description\s+du\s+poste)"
    r".*?(?=\n\n(?:Profil|Modalités|Compétences)|Profil\s+recherché|\Z)",
]

# =============================================================================
# Constants - Keyword Patterns
# =============================================================================

TECH_KEYWORD_PATTERNS = [
    # Programming languages
    r"\b(Python|Java|JavaScript|TypeScript|C\+\+|C#|Go|Rust|Ruby|PHP|Swift|Kotlin)\b",
    # Frameworks
    r"\b(Django|FastAPI|Flask|React|Angular|Vue|Node\.?js|Spring|Rails|Next\.?js)\b",
    # Databases
    r"\b(PostgreSQL|MySQL|MongoDB|Redis|Elasticsearch|SQL Server|Oracle|GraphQL)\b",
    # Cloud
    r"\b(AWS|Azure|GCP|Kubernetes|Docker|Terraform)\b",
    # AI/ML
    r"\b(Machine Learning|ML|AI|Deep Learning|PyTorch|TensorFlow|NLP|Computer Vision)\b",
    # Methodologies
    r"\b(Agile|Scrum|Kanban|DevOps|CI/CD|TDD|DDD)\b",
    # Security/Compliance
    r"\b(RGPD|GDPR|HDS|SecNumCloud)\b",
    # Accessibility
    r"\b(RGAA|WCAG)\b",
]

KEYWORD_FALSE_POSITIVES = {
    "Technologies",
    "Inclusives",
    "Intelligence",
    "Artificielle",
    "The",
    "And",
    "For",
    "With",
    "From",
    "This",
    "That",
}

# =============================================================================
# Constants - Location Patterns
# =============================================================================

FRENCH_CITIES = ["Paris", "Lyon", "Bordeaux", "Marseille", "Toulouse", "Nantes"]

LOCATION_PATTERNS = [
    r"(?:Location|Lieu|Localisation)\s*:\s*([^\n|]+)",
    r"(?:basé|based|situé|located)\s+(?:à|in|at)\s+({cities})",
    r"({cities}),?\s*France",
    r"([A-Z][a-z]+(?:,\s*[A-Z][a-z]+)?)\s*\|\s*(?:Remote|CDI|CDD)",
]

# =============================================================================
# Constants - Contract Patterns
# =============================================================================

CONTRACT_PATTERNS = [
    r"(?:Contract|Contrat|Type)\s*:\s*(CDI|CDD|Freelance|Stage|Full-time|Part-time)",
    r"\b(CDI|CDD|Freelance|Internship|Stage)\b",
    r"\((Full-time|Part-time|Temps\s+(?:plein|partiel))\)",
]

# =============================================================================
# Constants - Salary Patterns
# =============================================================================

SALARY_PATTERNS = [
    r"(?:Salary|Salaire|Rémunération)\s*:\s*([^\n]+)",
    r"(\d{2,3}[-–]\d{2,3}\s*k?\s*(?:EUR|€|K€|K))",
    r"(\d{2,3}\s*(?:à|to)\s*\d{2,3}\s*k?\s*(?:EUR|€|K€|K))",
]

# =============================================================================
# Data Classes
# =============================================================================


@dataclass
class JobPosting:
    """Structured representation of a job posting."""

    title: str
    company: str
    location: str | None = None
    contract_type: str | None = None
    salary: str | None = None
    must_have: list[str] = field(default_factory=list)
    nice_to_have: list[str] = field(default_factory=list)
    responsibilities: list[str] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)
    raw_text: str = ""


# =============================================================================
# Main Parser Function
# =============================================================================


def parse_job_posting(text: str) -> JobPosting:
    """
    Parse a job posting text and extract structured information.

    Args:
        text: Raw job posting text (from URL fetch or copy-paste)

    Returns:
        JobPosting with extracted fields
    """
    if not text or not text.strip():
        return JobPosting(title="Unknown", company="Unknown", raw_text=text)

    lines = _get_clean_lines(text)

    return JobPosting(
        title=_extract_title(lines),
        company=_extract_company(lines, text),
        location=_extract_location(text),
        contract_type=_extract_contract_type(text),
        salary=_extract_salary(text),
        must_have=_extract_must_have(text),
        nice_to_have=_extract_nice_to_have(text),
        responsibilities=_extract_responsibilities(text),
        keywords=_extract_keywords(text),
        raw_text=text,
    )


# =============================================================================
# Helper Functions
# =============================================================================


def _get_clean_lines(text: str) -> list[str]:
    """Split text into non-empty trimmed lines."""
    lines = text.strip().split("\n")
    return [line.strip() for line in lines if line.strip()]


def _extract_first_match(text: str, patterns: list[str], group: int = 1) -> str | None:
    """Extract first matching group from a list of patterns."""
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(group).strip()
    return None


def _extract_bullet_points(section: str, min_length: int = 10) -> list[str]:
    """Extract bullet points from a section of text."""
    bullets = re.findall(r"[-•*]\s*(.+?)(?=\n[-•*]|\n\n|\Z)", section, re.DOTALL)
    results = []
    for bullet in bullets:
        cleaned = bullet.strip().replace("\n", " ")
        if cleaned and len(cleaned) >= min_length:
            results.append(cleaned)
    return results


# =============================================================================
# Extraction Functions
# =============================================================================


def _extract_title(lines: list[str]) -> str:
    """Extract job title from posting."""
    if not lines:
        return "Unknown"

    first_line = lines[0]

    # Pattern: "Title - Company" or "Title @ Company" or "Title at Company"
    for separator in [" - ", " @ "]:
        if separator in first_line:
            return first_line.split(separator)[0].strip()

    if " at " in first_line.lower():
        idx = first_line.lower().index(" at ")
        return first_line[:idx].strip()

    # If first line looks like a title (no URLs, reasonable length)
    if len(first_line) < 100 and not first_line.startswith(("http", "www")):
        return first_line

    return "Unknown"


def _extract_company(lines: list[str], text: str) -> str:
    """Extract company name from posting."""
    if lines:
        company = _extract_company_from_first_line(lines[0])
        if company:
            return company

    company = _extract_company_from_patterns(text)
    if company:
        return company

    # Try CTO/CEO pattern in first line (e.g., "CTO HANDIPULSE")
    if lines:
        title_match = re.search(r"(?:CTO|CEO|VP|Director|Lead)\s+([A-Z][A-Z0-9]+)", lines[0])
        if title_match:
            return title_match.group(1).strip()

    # French pattern: "X est une" (X is a)
    french_match = re.search(r"([A-Z][A-Za-z0-9]+)\s+est\s+un", text)
    if french_match:
        return french_match.group(1).strip()

    return "Unknown"


def _extract_company_from_first_line(first_line: str) -> str | None:
    """Try to extract company from first line patterns."""
    # Pattern: "Title - Company"
    if " - " in first_line:
        parts = first_line.split(" - ")
        if len(parts) >= 2:
            return parts[1].strip()

    # Pattern: "Title @ Company"
    if " @ " in first_line:
        parts = first_line.split(" @ ")
        if len(parts) >= 2:
            return parts[1].strip()

    # Pattern: "Title at Company"
    if " at " in first_line.lower():
        idx = first_line.lower().index(" at ")
        return first_line[idx + 4 :].strip()

    return None


def _extract_company_from_patterns(text: str) -> str | None:
    """Try to extract company from text patterns."""
    patterns = [
        r"(?:chez|at|@)\s+([A-Z][A-Za-z0-9\s]+)",
        r"(?:Company|Entreprise|Société)\s*:\s*([^\n]+)",
    ]
    return _extract_first_match(text, patterns)


def _extract_location(text: str) -> str | None:
    """Extract location from posting."""
    cities_pattern = "|".join(FRENCH_CITIES)

    for pattern_template in LOCATION_PATTERNS:
        pattern = pattern_template.format(cities=cities_pattern)
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            location = match.group(1).strip()
            # Avoid "nice to have" false positive
            if location.lower() == "nice" and "nice to have" in text.lower():
                continue
            return location

    return None


def _extract_contract_type(text: str) -> str | None:
    """Extract contract type from posting."""
    for pattern in CONTRACT_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            contract = match.group(1).strip()
            # Normalize full-time to CDI
            if contract.lower() in ["full-time", "temps plein"]:
                return "CDI"
            return contract.upper() if len(contract) <= 4 else contract

    return None


def _extract_salary(text: str) -> str | None:
    """Extract salary information from posting."""
    for pattern in SALARY_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            salary = match.group(1).strip()
            # Avoid matching years like "2025-2030"
            if re.match(r"^20\d{2}", salary):
                continue
            return salary

    return None


def _extract_must_have(text: str) -> list[str]:
    """Extract must-have/required requirements."""
    must_have = []

    # Find requirements section
    for pattern in REQUIREMENTS_SECTION_PATTERNS:
        section_match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if section_match:
            section = section_match.group(0)
            bullets = _extract_bullet_points(section)

            for bullet in bullets:
                # Skip nice-to-have items
                if _is_nice_to_have_marker(bullet):
                    continue

                # Handle explicit (required) marker
                if re.search(r"\(required\)|\(obligatoire\)", bullet, re.IGNORECASE):
                    cleaned = re.sub(r"\s*\(.*?\)\s*", " ", bullet).strip()
                    must_have.append(cleaned)
                else:
                    must_have.append(bullet)
            break

    # Also extract items with (required) marker anywhere
    inline_required = re.findall(r"[-•*]\s*(.+?)\s*\(required\)", text, re.IGNORECASE)
    for req in inline_required:
        if req.strip() not in must_have:
            must_have.append(req.strip())

    return must_have


def _is_nice_to_have_marker(text: str) -> bool:
    """Check if text contains nice-to-have markers."""
    return bool(re.search(r"nice.to.have|souhaité|optional|atout\s*:", text, re.IGNORECASE))


def _extract_nice_to_have(text: str) -> list[str]:
    """Extract nice-to-have/optional requirements."""
    nice_to_have = []

    # Find nice-to-have section
    for pattern in NICE_TO_HAVE_SECTION_PATTERNS:
        section_match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if section_match:
            section = section_match.group(0)
            bullets = re.findall(r"[-•*]\s*(.+?)(?=\n|$)", section)
            nice_to_have.extend([b.strip() for b in bullets])
            break

    # Look for "(nice to have)" markers inline
    inline_nice = re.findall(
        r"[-•*]\s*(.+?)\s*\((?:nice.to.have|souhaité|optional)\)",
        text,
        re.IGNORECASE,
    )
    nice_to_have.extend([n.strip() for n in inline_nice])

    # Look for "Atout :" pattern (French for "Asset/Plus")
    atout_match = re.search(r"Atout\s*:\s*(.+?)(?=\n[-•*]|\n\n|\Z)", text, re.IGNORECASE)
    if atout_match:
        atout = atout_match.group(1).strip()
        if atout and atout not in nice_to_have:
            nice_to_have.append(atout)

    return nice_to_have


def _extract_responsibilities(text: str) -> list[str]:
    """Extract job responsibilities."""
    for pattern in RESPONSIBILITIES_SECTION_PATTERNS:
        section_match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if section_match:
            section = section_match.group(0)
            return _extract_bullet_points(section)

    return []


def _extract_keywords(text: str) -> list[str]:
    """Extract ATS keywords from posting."""
    keywords = set()

    # Extract from tech patterns
    for pattern in TECH_KEYWORD_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        keywords.update([m if isinstance(m, str) else m[0] for m in matches])

    # Look for Tech Stack section
    stack_match = re.search(
        r"(?:Tech Stack|Stack Technique).*?(?=\n\n|\n[A-Z]|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if stack_match:
        stack_section = stack_match.group(0)
        techs = re.findall(r"\b([A-Z][A-Za-z0-9+#.]+)\b", stack_section)
        keywords.update(techs)

    # Filter false positives
    keywords = keywords - KEYWORD_FALSE_POSITIVES

    return sorted(keywords, key=str.lower)
