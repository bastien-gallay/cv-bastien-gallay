"""Job posting parser - main orchestrator.

CUPID:
- Composable: Uses extractors as building blocks
- Unix philosophy: Orchestrates, doesn't implement
- Predictable: Single entry point, consistent output
- Idiomatic: Clean Python with type hints
- Domain-based: Returns domain object (JobPosting)
"""

from .extractors import (
    clean_lines,
    extract_bullet_points,
    extract_company,
    extract_contract_type,
    extract_first_match,
    extract_keywords,
    extract_location,
    extract_must_have,
    extract_nice_to_have,
    extract_responsibilities,
    extract_salary,
    extract_title,
    is_nice_to_have,
)
from .patterns import FRENCH_CITIES, KEYWORD_FALSE_POSITIVES
from .types import JobPosting

# =============================================================================
# Backward Compatibility Aliases
# =============================================================================
# These aliases maintain compatibility with existing tests and code
# that imports the underscore-prefixed functions.

_get_clean_lines = clean_lines
_extract_first_match = extract_first_match
_extract_bullet_points = extract_bullet_points
_extract_title = extract_title
_extract_company = extract_company
_extract_location = extract_location
_extract_contract_type = extract_contract_type
_extract_salary = extract_salary
_is_nice_to_have_marker = is_nice_to_have

__all__ = [
    # Main API
    "JobPosting",
    "parse_job_posting",
    # Constants (for tests)
    "FRENCH_CITIES",
    "KEYWORD_FALSE_POSITIVES",
    # Backward compatibility exports
    "_get_clean_lines",
    "_extract_first_match",
    "_extract_bullet_points",
    "_extract_title",
    "_extract_company",
    "_extract_location",
    "_extract_contract_type",
    "_extract_salary",
    "_is_nice_to_have_marker",
]


# =============================================================================
# Main Parser Function
# =============================================================================


def parse_job_posting(text: str) -> JobPosting:
    """
    Parse a job posting text and extract structured information.

    This is the main entry point for job posting analysis.
    It orchestrates the extraction process using specialized extractors.

    Args:
        text: Raw job posting text (from URL fetch or copy-paste)

    Returns:
        JobPosting with all extracted fields

    Example:
        >>> job = parse_job_posting("Software Engineer - TechCorp\\n...")
        >>> print(job.title)
        "Software Engineer"
        >>> print(job.company)
        "TechCorp"

    The parser handles:
        - French and English job postings
        - Multiple title/company formats (dash, @, "at")
        - Must-have vs nice-to-have requirements
        - ATS keyword extraction
        - Salary and contract type detection
    """
    if not text or not text.strip():
        return JobPosting(title="Unknown", company="Unknown", raw_text=text or "")

    lines = clean_lines(text)

    return JobPosting(
        title=extract_title(lines),
        company=extract_company(lines, text),
        location=extract_location(text),
        contract_type=extract_contract_type(text),
        salary=extract_salary(text),
        must_have=extract_must_have(text),
        nice_to_have=extract_nice_to_have(text),
        responsibilities=extract_responsibilities(text),
        keywords=extract_keywords(text),
        raw_text=text,
    )
