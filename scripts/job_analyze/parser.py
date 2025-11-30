"""Job posting parser - extracts structured information from job postings."""

import re
from dataclasses import dataclass, field


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

    lines = text.strip().split("\n")
    lines = [line.strip() for line in lines if line.strip()]

    # Extract basic info
    title = _extract_title(lines, text)
    company = _extract_company(lines, text, title)
    location = _extract_location(text)
    contract_type = _extract_contract_type(text)
    salary = _extract_salary(text)

    # Extract requirements
    must_have = _extract_must_have(text)
    nice_to_have = _extract_nice_to_have(text)

    # Extract responsibilities
    responsibilities = _extract_responsibilities(text)

    # Extract keywords
    keywords = _extract_keywords(text)

    return JobPosting(
        title=title,
        company=company,
        location=location,
        contract_type=contract_type,
        salary=salary,
        must_have=must_have,
        nice_to_have=nice_to_have,
        responsibilities=responsibilities,
        keywords=keywords,
        raw_text=text,
    )


def _extract_title(lines: list[str], text: str) -> str:
    """Extract job title from posting."""
    # Try first line (common format: "Title - Company")
    if lines:
        first_line = lines[0]

        # Pattern: "Title - Company" or "Title @ Company"
        if " - " in first_line:
            return first_line.split(" - ")[0].strip()
        if " @ " in first_line:
            return first_line.split(" @ ")[0].strip()
        if " at " in first_line.lower():
            idx = first_line.lower().index(" at ")
            return first_line[:idx].strip()

        # If first line looks like a title (no special chars, reasonable length)
        if len(first_line) < 100 and not first_line.startswith(("http", "www")):
            return first_line

    return "Unknown"


def _extract_company(lines: list[str], text: str, title: str) -> str:
    """Extract company name from posting."""
    if lines:
        first_line = lines[0]

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

    # Look for company patterns in text
    patterns = [
        r"(?:chez|at|@)\s+([A-Z][A-Za-z0-9\s]+)",
        r"(?:Company|Entreprise|Société)\s*:\s*([^\n]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return "Unknown"


def _extract_location(text: str) -> str | None:
    """Extract location from posting."""
    patterns = [
        r"(?:Location|Lieu|Localisation)\s*:\s*([^\n|]+)",
        r"(Paris|Lyon|Bordeaux|Marseille|Toulouse|Nantes|Nice|Remote)[,\s]*(France)?",
        r"([A-Z][a-z]+(?:,\s*[A-Z][a-z]+)?)\s*\|\s*(?:Remote|CDI|CDD)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            location = match.group(1).strip()
            # Add France if mentioned separately
            if match.lastindex and match.lastindex >= 2 and match.group(2):
                location += ", " + match.group(2).strip()
            return location

    return None


def _extract_contract_type(text: str) -> str | None:
    """Extract contract type from posting."""
    patterns = [
        r"(?:Contract|Contrat|Type)\s*:\s*(CDI|CDD|Freelance|Stage|Full-time|Part-time)",
        r"\b(CDI|CDD|Freelance|Internship|Stage)\b",
        r"\((Full-time|Part-time|Temps\s+(?:plein|partiel))\)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            contract = match.group(1).strip()
            # Normalize
            if contract.lower() in ["full-time", "temps plein"]:
                return "CDI"
            return contract.upper() if len(contract) <= 4 else contract

    return None


def _extract_salary(text: str) -> str | None:
    """Extract salary information from posting."""
    patterns = [
        r"(?:Salary|Salaire|Rémunération)\s*:\s*([^\n]+)",
        r"(\d{2,3}[-–]\d{2,3}k?\s*(?:EUR|€|K€))",
        r"(\d{2,3}\s*(?:à|to|-)\s*\d{2,3}\s*k?\s*(?:EUR|€)?)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return None


def _extract_must_have(text: str) -> list[str]:
    """Extract must-have/required requirements."""
    must_have = []

    # Find sections with required requirements
    section_patterns = [
        r"(?:Requirements|Exigences|Must-have|Obligatoire|Required).*?(?=\n\n|\Z|Nice-to-have|Souhaité|Responsibilities|Tech Stack)",
        r"(?:\(required\)|\(obligatoire\))",
    ]

    # Find the requirements section
    section_match = re.search(
        r"(?:Requirements|Exigences|Must-have).*?(?=\n\n|\n[A-Z]|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )

    if section_match:
        section = section_match.group(0)
        # Extract bullet points
        bullets = re.findall(r"[-•*]\s*(.+?)(?=\n|$)", section)

        for bullet in bullets:
            # Check if it's required
            if re.search(r"\(required\)|\(obligatoire\)|obligatoire", bullet, re.IGNORECASE):
                must_have.append(re.sub(r"\s*\(.*?\)\s*", " ", bullet).strip())
            elif not re.search(r"nice.to.have|souhaité|optional", bullet, re.IGNORECASE):
                # Default to must-have if in Requirements section
                must_have.append(bullet.strip())

    return must_have


def _extract_nice_to_have(text: str) -> list[str]:
    """Extract nice-to-have/optional requirements."""
    nice_to_have = []

    # Find nice-to-have section
    section_match = re.search(
        r"(?:Nice-to-have|Souhaité|Optional|Bonus|Plus).*?(?=\n\n|\n[A-Z]|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )

    if section_match:
        section = section_match.group(0)
        bullets = re.findall(r"[-•*]\s*(.+?)(?=\n|$)", section)
        nice_to_have.extend([b.strip() for b in bullets])

    # Also look for "(nice to have)" markers in any section
    inline_nice = re.findall(
        r"[-•*]\s*(.+?)\s*\((?:nice.to.have|souhaité|optional)\)",
        text,
        re.IGNORECASE,
    )
    nice_to_have.extend([n.strip() for n in inline_nice])

    return nice_to_have


def _extract_responsibilities(text: str) -> list[str]:
    """Extract job responsibilities."""
    responsibilities = []

    # Find responsibilities section
    section_match = re.search(
        r"(?:Responsibilities|Responsabilités|Mission|Missions|What you.ll do|Your role).*?(?=\n\n|\n[A-Z]|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )

    if section_match:
        section = section_match.group(0)
        bullets = re.findall(r"[-•*]\s*(.+?)(?=\n|$)", section)
        responsibilities.extend([b.strip() for b in bullets])

    return responsibilities


def _extract_keywords(text: str) -> list[str]:
    """Extract ATS keywords from posting."""
    keywords = set()

    # Technical keywords patterns
    tech_patterns = [
        # Programming languages
        r"\b(Python|Java|JavaScript|TypeScript|C\+\+|C#|Go|Rust|Ruby|PHP|Swift|Kotlin)\b",
        # Frameworks
        r"\b(Django|FastAPI|Flask|React|Angular|Vue|Node\.?js|Spring|Rails)\b",
        # Databases
        r"\b(PostgreSQL|MySQL|MongoDB|Redis|Elasticsearch|SQL Server|Oracle)\b",
        # Cloud
        r"\b(AWS|Azure|GCP|Kubernetes|Docker|Terraform)\b",
        # AI/ML
        r"\b(Machine Learning|ML|AI|Deep Learning|PyTorch|TensorFlow|NLP)\b",
        # Methodologies
        r"\b(Agile|Scrum|Kanban|DevOps|CI/CD|TDD|DDD)\b",
    ]

    for pattern in tech_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        keywords.update([m if isinstance(m, str) else m[0] for m in matches])

    # Look for Tech Stack section
    stack_match = re.search(
        r"(?:Tech Stack|Stack Technique|Technologies?).*?(?=\n\n|\n[A-Z]|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )

    if stack_match:
        stack_section = stack_match.group(0)
        # Extract comma-separated or listed technologies
        techs = re.findall(r"\b([A-Z][A-Za-z0-9+#.]+)\b", stack_section)
        keywords.update(techs)

    return sorted(keywords, key=str.lower)
