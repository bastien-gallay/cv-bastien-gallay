#!/usr/bin/env python3
"""Update priority scores in TASKS.md using WSJF algorithm.

WSJF (Weighted Shortest Job First) prioritizes by value/effort ratio.

Formula: Score = Value / Time
Where: Value = Priority + Urgency + Age

Usage:
    uv run scripts/update_priority_scores.py
    uv run scripts/update_priority_scores.py --dry-run
    uv run scripts/update_priority_scores.py --verbose
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from dataclasses import dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING

import yaml

if TYPE_CHECKING:
    from collections.abc import Iterator

log = logging.getLogger(__name__)


# =============================================================================
# Domain Types
# =============================================================================


class Priority(Enum):
    """Task priority levels with their scoring values."""

    HIGH = ("🔴 Haute", 10, 8.0)
    MEDIUM = ("🟡 Moyenne", 5, 4.0)
    LOW = ("🟢 Basse", 2, 2.0)

    def __init__(self, label: str, score: int, default_hours: float) -> None:
        self.label = label
        self.score = score
        self.default_hours = default_hours

    @classmethod
    def from_label(cls, label: str) -> Priority:
        """Find priority by its label, default to MEDIUM."""
        for priority in cls:
            if priority.label == label:
                return priority
        return cls.MEDIUM


@dataclass(frozen=True)
class WSJFConfig:
    """Configuration for WSJF scoring algorithm."""

    age_divisor: float = 20.0
    age_max_score: float = 2.5
    urgency_overdue: float = 10.0
    urgency_week: float = 5.0
    urgency_month: float = 2.0

    @classmethod
    def from_yaml(cls, path: Path) -> WSJFConfig:
        """Load config from YAML file, with defaults as fallback."""
        if not path.exists():
            return cls()

        data = yaml.safe_load(path.read_text())
        age = data.get("age_scoring", {})
        urgency = data.get("urgency_scores", {})

        return cls(
            age_divisor=age.get("divisor", cls.age_divisor),
            age_max_score=age.get("max_score", cls.age_max_score),
            urgency_overdue=urgency.get("overdue", cls.urgency_overdue),
            urgency_week=urgency.get("week", cls.urgency_week),
            urgency_month=urgency.get("month", cls.urgency_month),
        )


@dataclass(frozen=True)
class TaskMetadata:
    """Raw metadata extracted from a task file."""

    task_id: str
    title: str
    status: str
    priority: Priority
    time_estimate: float
    created: date | None
    target: date | None


@dataclass(frozen=True)
class ScoredTask:
    """Task with its calculated WSJF score and components."""

    task_id: str
    title: str
    status: str
    priority: Priority
    created: date | None
    score: float
    # Score breakdown for debugging
    priority_value: float
    urgency_value: float
    age_value: float
    time_hours: float

    @property
    def is_in_progress(self) -> bool:
        return "En cours" in self.status or "🔄" in self.status


# =============================================================================
# Scoring Logic (Pure Functions)
# =============================================================================


def calculate_urgency(target: date | None, today: date, config: WSJFConfig) -> float:
    """Calculate urgency score based on target date proximity."""
    if target is None:
        return 0.0

    days_until = (target - today).days

    if days_until < 0:
        return config.urgency_overdue
    if days_until < 7:
        return config.urgency_week
    if days_until < 30:
        return config.urgency_month
    return 0.0


def calculate_age(created: date | None, today: date, config: WSJFConfig) -> float:
    """Calculate age score based on task age in days."""
    if created is None:
        return 0.0

    days_old = (today - created).days
    return min(days_old / config.age_divisor, config.age_max_score)


def calculate_wsjf_score(
    priority: Priority,
    urgency: float,
    age: float,
    time_hours: float,
) -> float:
    """Calculate WSJF score: (priority + urgency + age) / time."""
    if time_hours <= 0:
        time_hours = priority.default_hours

    total_value = priority.score + urgency + age
    return round(total_value / time_hours, 2)


def score_task(
    metadata: TaskMetadata,
    today: date,
    config: WSJFConfig,
) -> ScoredTask:
    """Score a single task using WSJF algorithm."""
    urgency = calculate_urgency(metadata.target, today, config)
    age = calculate_age(metadata.created, today, config)
    score = calculate_wsjf_score(
        metadata.priority,
        urgency,
        age,
        metadata.time_estimate,
    )

    return ScoredTask(
        task_id=metadata.task_id,
        title=metadata.title,
        status=metadata.status,
        priority=metadata.priority,
        created=metadata.created,
        score=score,
        priority_value=metadata.priority.score,
        urgency_value=urgency,
        age_value=age,
        time_hours=metadata.time_estimate,
    )


# =============================================================================
# File Parsing (IO Layer)
# =============================================================================


def parse_date(date_str: str) -> date | None:
    """Parse a date string in YYYY-MM-DD format."""
    if not date_str or date_str == "-":
        return None
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        return None


def extract_field(content: str, field: str) -> str:
    """Extract a metadata field from task file markdown table."""
    pattern = rf"\| \*\*{re.escape(field)}\*\* \| (.*?) \|"
    match = re.search(pattern, content)
    return match.group(1).strip() if match else ""


def parse_time_estimate(time_str: str, priority: Priority) -> float:
    """Parse time estimate string to hours, with priority-based default."""
    if time_str:
        numbers = re.findall(r"(\d+\.?\d*)", time_str)
        if numbers:
            return float(numbers[0])
    return priority.default_hours


def parse_task_file(path: Path) -> TaskMetadata | None:
    """Parse a task file and extract its metadata."""
    content = path.read_text()

    status = extract_field(content, "Statut")

    # Skip non-pending tasks
    if "À faire" not in status and "⏳" not in status:
        return None

    task_id = extract_field(content, "ID") or path.stem
    title = extract_field(content, "Titre") or task_id
    priority_label = extract_field(content, "Priorité") or "🟡 Moyenne"
    priority = Priority.from_label(priority_label)
    time_str = extract_field(content, "Temps estimé")
    created_str = extract_field(content, "Créé le")
    target_str = extract_field(content, "Cible")

    return TaskMetadata(
        task_id=task_id,
        title=title,
        status=status,
        priority=priority,
        time_estimate=parse_time_estimate(time_str, priority),
        created=parse_date(created_str),
        target=parse_date(target_str),
    )


def iter_task_files(tasks_dir: Path) -> Iterator[Path]:
    """Iterate over task markdown files, excluding templates."""
    for path in tasks_dir.glob("*.md"):
        if path.name != "TEMPLATE.md":
            yield path


# =============================================================================
# TASKS.md Update
# =============================================================================


@dataclass
class TableRow:
    """A parsed row from the TASKS.md table."""

    task_id: str
    title: str
    status: str
    priority: str
    score: str
    created: str
    link: str

    def to_markdown(self) -> str:
        """Render row as markdown table row."""
        return (
            f"| [{self.task_id}]({self.link}) | {self.title} | "
            f"{self.status} | {self.priority} | {self.score} | {self.created} |"
        )


def parse_tasks_table(content: str) -> tuple[str, list[TableRow], int, int] | None:
    """Parse the active tasks table from TASKS.md content.

    Returns (header, rows, start_pos, end_pos) or None if not found.
    """
    table_pattern = (
        r"(\| ID \| Titre \| Statut \| Priorité \| Score \| Créé le \|\n"
        r"\|[-|]+\|\n)"
        r"((?:\| .+\|\n)+)"
    )
    match = re.search(table_pattern, content)
    if not match:
        return None

    header = match.group(1)
    rows_text = match.group(2)

    row_pattern = (
        r"\| \[([A-Z]+-\d+)\]\(([^)]+)\) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|"
    )

    rows = [
        TableRow(
            task_id=m.group(1),
            link=m.group(2),
            title=m.group(3).strip(),
            status=m.group(4).strip(),
            priority=m.group(5).strip(),
            score=m.group(6).strip(),
            created=m.group(7).strip(),
        )
        for m in re.finditer(row_pattern, rows_text)
    ]

    return header, rows, match.start(), match.end()


def update_table_scores(
    rows: list[TableRow],
    scores: dict[str, float],
) -> list[TableRow]:
    """Update scores in table rows and sort by score descending."""
    updated = []
    for row in rows:
        is_in_progress = "En cours" in row.status or "🔄" in row.status

        if is_in_progress:
            new_score = "-"
            sort_key = float("inf")  # Keep at top
        elif row.task_id in scores:
            new_score = f"{scores[row.task_id]:.2f}"
            sort_key = scores[row.task_id]
        else:
            new_score = row.score
            sort_key = float(row.score) if row.score not in ("-", "") else 0

        updated.append(
            TableRow(
                task_id=row.task_id,
                title=row.title,
                status=row.status,
                priority=row.priority,
                score=new_score,
                created=row.created,
                link=row.link,
            )
        )
        updated[-1]._sort_key = sort_key  # type: ignore[attr-defined]

    # Sort: in-progress first (inf), then by score descending
    updated.sort(key=lambda r: -getattr(r, "_sort_key", 0))
    return updated


def render_table(header: str, rows: list[TableRow]) -> str:
    """Render table header and rows as markdown."""
    row_lines = [row.to_markdown() for row in rows]
    return header + "\n".join(row_lines) + "\n"


# =============================================================================
# Main Orchestration
# =============================================================================


def collect_scores(
    tasks_dir: Path,
    today: date,
    config: WSJFConfig,
    *,
    verbose: bool = False,
) -> list[ScoredTask]:
    """Collect and score all pending tasks."""
    scored = []

    for task_file in iter_task_files(tasks_dir):
        metadata = parse_task_file(task_file)
        if metadata is None:
            continue

        task = score_task(metadata, today, config)
        scored.append(task)

        if verbose:
            log.info(
                "  %s: %.2f (prio=%d, urg=%.0f, age=%.1f, time=%.1fh)",
                task.task_id,
                task.score,
                task.priority_value,
                task.urgency_value,
                task.age_value,
                task.time_hours,
            )

    scored.sort(key=lambda t: t.score, reverse=True)
    return scored


def update_tasks_file(
    tasks_md: Path,
    scored_tasks: list[ScoredTask],
    *,
    dry_run: bool = False,
) -> bool:
    """Update TASKS.md with new scores."""
    content = tasks_md.read_text()

    parsed = parse_tasks_table(content)
    if parsed is None:
        log.error("Could not find active tasks table in TASKS.md")
        return False

    header, rows, start, end = parsed
    score_map = {t.task_id: t.score for t in scored_tasks}

    updated_rows = update_table_scores(rows, score_map)
    new_table = render_table(header, updated_rows)
    new_content = content[:start] + new_table + content[end:]

    if dry_run:
        log.info("\n--- Dry run: would write ---\n%s", new_table)
        return True

    tasks_md.write_text(new_content)
    return True


def run(
    tasks_dir: Path,
    tasks_md: Path,
    config_path: Path,
    *,
    dry_run: bool = False,
    verbose: bool = False,
) -> int:
    """Main entry point with dependency injection."""
    config = WSJFConfig.from_yaml(config_path)
    today = date.today()

    log.info("🔄 Calculating priority scores...\n")

    scored = collect_scores(tasks_dir, today, config, verbose=verbose)

    if not scored:
        log.warning("⚠️  No pending tasks found")
        return 0

    log.info("\n📊 Scored %d tasks", len(scored))
    log.info("\nTop 5:")
    for i, task in enumerate(scored[:5], 1):
        log.info("  %d. %s: %.2f", i, task.task_id, task.score)

    if update_tasks_file(tasks_md, scored, dry_run=dry_run):
        log.info("\n✅ %s", "Dry run complete" if dry_run else "TASKS.md updated")
        return 0

    log.error("\n❌ Failed to update TASKS.md")
    return 1


def main() -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Update priority scores in TASKS.md using WSJF"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show changes without writing",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed score breakdown",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
    )

    return run(
        tasks_dir=Path(".tasks/tasks"),
        tasks_md=Path(".tasks/TASKS.md"),
        config_path=Path("config/task_management/priorities.yml"),
        dry_run=args.dry_run,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    sys.exit(main())
