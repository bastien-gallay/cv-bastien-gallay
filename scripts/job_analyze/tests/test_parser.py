"""Tests for job posting parser - TDD approach."""

import pytest
from scripts.job_analyze.parser import JobPosting, parse_job_posting


# =============================================================================
# Sample job postings for testing
# =============================================================================

SAMPLE_JOB_SIMPLE = """
Senior Python Developer - TechCorp

Location: Paris, France
Contract: CDI (Full-time)
Salary: 60-80k EUR

About the role:
We are looking for a Senior Python Developer to join our team.

Requirements:
- 5+ years of Python experience (required)
- Experience with Django or FastAPI (required)
- Knowledge of PostgreSQL (required)
- AWS experience (nice to have)
- Docker/Kubernetes (nice to have)

Responsibilities:
- Design and implement backend services
- Mentor junior developers
- Participate in code reviews
"""

SAMPLE_JOB_COMPLEX = """
Chief Technology Officer (CTO) - StartupAI

Paris, France | Remote OK | CDI

Salary: 120-150k EUR + equity

StartupAI is a fast-growing AI startup revolutionizing the healthcare industry.

Mission:
As CTO, you will lead our technical vision and build a world-class engineering team.

Must-have:
- 10+ years software development experience
- 5+ years in leadership roles
- Strong background in Machine Learning / AI
- Experience scaling systems (millions of users)
- Fluent in English

Nice-to-have:
- PhD in Computer Science or related field
- Experience in healthcare/biotech
- Previous startup experience
- Knowledge of regulatory compliance (HIPAA, GDPR)

Tech Stack:
Python, PyTorch, AWS, Kubernetes, PostgreSQL

What we offer:
- Competitive salary + equity
- Flexible working hours
- International team
"""


# =============================================================================
# Tests for JobPosting dataclass
# =============================================================================

class TestJobPostingDataclass:
    """Test JobPosting data structure."""

    def test_create_job_posting(self):
        """Should create a JobPosting with all required fields."""
        job = JobPosting(
            title="Software Engineer",
            company="TechCorp",
            location="Paris",
            contract_type="CDI",
        )
        assert job.title == "Software Engineer"
        assert job.company == "TechCorp"
        assert job.location == "Paris"
        assert job.contract_type == "CDI"

    def test_job_posting_optional_fields(self):
        """Should handle optional fields with defaults."""
        job = JobPosting(
            title="Developer",
            company="Corp",
        )
        assert job.location is None
        assert job.salary is None
        assert job.must_have == []
        assert job.nice_to_have == []
        assert job.responsibilities == []
        assert job.keywords == []

    def test_job_posting_with_requirements(self):
        """Should store requirements correctly."""
        job = JobPosting(
            title="Developer",
            company="Corp",
            must_have=["Python", "Django"],
            nice_to_have=["Docker"],
        )
        assert "Python" in job.must_have
        assert "Docker" in job.nice_to_have


# =============================================================================
# Tests for parse_job_posting function
# =============================================================================

class TestParseJobPosting:
    """Test job posting parser."""

    def test_parse_simple_job(self):
        """Should parse a simple job posting."""
        job = parse_job_posting(SAMPLE_JOB_SIMPLE)

        assert job.title == "Senior Python Developer"
        assert job.company == "TechCorp"
        assert job.location == "Paris, France"
        assert job.contract_type == "CDI"

    def test_extract_salary(self):
        """Should extract salary information."""
        job = parse_job_posting(SAMPLE_JOB_SIMPLE)
        assert job.salary == "60-80k EUR"

    def test_extract_must_have_requirements(self):
        """Should identify must-have requirements."""
        job = parse_job_posting(SAMPLE_JOB_SIMPLE)

        # Should contain key required skills
        must_have_text = " ".join(job.must_have).lower()
        assert "python" in must_have_text
        assert "django" in must_have_text or "fastapi" in must_have_text
        assert "postgresql" in must_have_text

    def test_extract_nice_to_have_requirements(self):
        """Should identify nice-to-have requirements."""
        job = parse_job_posting(SAMPLE_JOB_SIMPLE)

        nice_to_have_text = " ".join(job.nice_to_have).lower()
        assert "aws" in nice_to_have_text or "docker" in nice_to_have_text

    def test_extract_responsibilities(self):
        """Should extract responsibilities."""
        job = parse_job_posting(SAMPLE_JOB_SIMPLE)

        assert len(job.responsibilities) > 0
        resp_text = " ".join(job.responsibilities).lower()
        assert "backend" in resp_text or "mentor" in resp_text

    def test_extract_keywords(self):
        """Should extract ATS keywords."""
        job = parse_job_posting(SAMPLE_JOB_SIMPLE)

        # Should extract technical keywords
        keywords_lower = [k.lower() for k in job.keywords]
        assert "python" in keywords_lower

    def test_parse_complex_job(self):
        """Should parse a complex job posting with multiple sections."""
        job = parse_job_posting(SAMPLE_JOB_COMPLEX)

        assert job.title == "Chief Technology Officer" or "CTO" in job.title
        assert job.company == "StartupAI"
        assert "Paris" in job.location

    def test_parse_complex_requirements(self):
        """Should correctly categorize complex requirements."""
        job = parse_job_posting(SAMPLE_JOB_COMPLEX)

        # Must-have should include leadership and ML
        must_have_text = " ".join(job.must_have).lower()
        assert "leadership" in must_have_text or "years" in must_have_text

        # Nice-to-have should include PhD, startup
        nice_to_have_text = " ".join(job.nice_to_have).lower()
        assert "phd" in nice_to_have_text or "startup" in nice_to_have_text

    def test_extract_tech_stack_as_keywords(self):
        """Should extract tech stack as keywords."""
        job = parse_job_posting(SAMPLE_JOB_COMPLEX)

        keywords_lower = [k.lower() for k in job.keywords]
        # Should include items from Tech Stack section
        assert any(k in keywords_lower for k in ["python", "pytorch", "aws", "kubernetes"])


# =============================================================================
# Tests for edge cases
# =============================================================================

class TestParserEdgeCases:
    """Test edge cases and error handling."""

    def test_parse_empty_string(self):
        """Should handle empty input gracefully."""
        job = parse_job_posting("")
        assert job.title == "Unknown"
        assert job.company == "Unknown"

    def test_parse_minimal_posting(self):
        """Should handle minimal job posting."""
        minimal = "Software Engineer at Google"
        job = parse_job_posting(minimal)

        assert "Software Engineer" in job.title or "Engineer" in job.title
        assert "Google" in job.company or job.company == "Unknown"

    def test_parse_french_job_posting(self):
        """Should handle French job postings."""
        french_job = """
        Développeur Python Senior - ParisStartup

        Lieu: Paris
        Contrat: CDI

        Exigences:
        - 5 ans d'expérience Python (obligatoire)
        - Connaissance de Django (obligatoire)
        - Anglais courant (souhaité)
        """
        job = parse_job_posting(french_job)

        assert "Python" in job.title or "Développeur" in job.title
        assert len(job.must_have) > 0 or len(job.nice_to_have) > 0
