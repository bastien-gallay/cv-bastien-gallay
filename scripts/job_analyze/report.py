"""Report generator for job posting analysis."""

from .parser import JobPosting


def generate_report(job: JobPosting) -> str:
    """
    Generate a formatted analysis report for a job posting.

    Args:
        job: Parsed JobPosting object

    Returns:
        Formatted markdown report
    """
    lines = [
        f"# Analyse : {job.title} @ {job.company}",
        "",
        "## Informations générales",
        f"- **Poste**: {job.title}",
        f"- **Entreprise**: {job.company}",
    ]

    if job.location:
        lines.append(f"- **Localisation**: {job.location}")
    if job.contract_type:
        lines.append(f"- **Type de contrat**: {job.contract_type}")
    if job.salary:
        lines.append(f"- **Salaire**: {job.salary}")

    lines.append("")

    # Requirements section
    lines.append("## Exigences")
    lines.append("")

    if job.must_have:
        lines.append(f"### Obligatoires ({len(job.must_have)})")
        for req in job.must_have:
            lines.append(f"- [ ] {req}")
        lines.append("")

    if job.nice_to_have:
        lines.append(f"### Souhaitées ({len(job.nice_to_have)})")
        for req in job.nice_to_have:
            lines.append(f"- [ ] {req}")
        lines.append("")

    # Responsibilities
    if job.responsibilities:
        lines.append("## Responsabilités principales")
        for i, resp in enumerate(job.responsibilities, 1):
            lines.append(f"{i}. {resp}")
        lines.append("")

    # Keywords
    if job.keywords:
        lines.append("## Mots-clés ATS")
        lines.append(f"`{'`, `'.join(job.keywords)}`")
        lines.append("")

    return "\n".join(lines)
