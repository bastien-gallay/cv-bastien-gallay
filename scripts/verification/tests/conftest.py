"""Pytest configuration for verification tests."""

import sys
from pathlib import Path

import pytest

# Add project root to path for imports
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def sample_cv_content() -> str:
    """Return sample CV content for testing."""
    return """
#import "@preview/neat-cv:0.4.0": cv, entry

#show: cv.with(
  author: (
    firstname: "Test",
    lastname: "User",
    email: "test@example.com",
    phone: "(+33) 06 12 34 56 78",
    linkedin: "testuser",
  ),
)

= Expérience

#entry(
  title: "Senior Developer",
  date: "02/2021 - 10/2025",
  institution: "Company",
)[
  Description
]

= Etudes

#entry(
  title: "Master",
  date: "2020",
  institution: "University",
)[]

= Certifications
= Expertises
= Langues
"""


@pytest.fixture
def cv_file(tmp_path: Path, sample_cv_content: str) -> Path:
    """Create a temporary CV file for testing."""
    cv_path = tmp_path / "src" / "cv.typ"
    cv_path.parent.mkdir(parents=True)
    cv_path.write_text(sample_cv_content)
    return cv_path


@pytest.fixture
def project_with_cv(tmp_path: Path, sample_cv_content: str) -> Path:
    """Create a temporary project structure with CV file."""
    cv_path = tmp_path / "src" / "cv.typ"
    cv_path.parent.mkdir(parents=True)
    cv_path.write_text(sample_cv_content)

    dist_path = tmp_path / "dist"
    dist_path.mkdir()

    return tmp_path
