#!/usr/bin/env python3
"""Update priority scores in TASKS.md using WSJF algorithm.

Formula: Score = Value / Time
Where: Value = (Priority × weight) + (Urgency × weight) + (Age × weight)

Usage:
    uv run scripts/update_priority_scores.py
    uv run scripts/update_priority_scores.py --dry-run
    uv run scripts/update_priority_scores.py --verbose
"""

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# Configuration
TASKS_DIR = Path(".tasks/tasks")
TASKS_MD = Path(".tasks/TASKS.md")

PRIORITY_SCORES = {"🔴 Haute": 10, "🟡 Moyenne": 5, "🟢 Basse": 2}
DEFAULT_TIMES = {"🔴 Haute": 8, "🟡 Moyenne": 4, "🟢 Basse": 2}


@dataclass
class TaskScore:
    """Task with calculated priority score."""

    task_id: str
    title: str
    status: str
    priority: str
    score: float
    created: str
    # For verbose output
    time_hours: float = 0
    priority_value: float = 0
    urgency: float = 0
    age: float = 0


def extract_metadata(content: str, field: str) -> str:
    """Extract a metadata field from task file content."""
    pattern = rf"\| \*\*{field}\*\* \| (.*?) \|"
    match = re.search(pattern, content)
    return match.group(1).strip() if match else ""


def parse_time_estimate(time_str: str, priority: str) -> float:
    """Parse time estimate string to hours."""
    if time_str:
        numbers = re.findall(r"(\d+\.?\d*)", time_str)
        if numbers:
            return float(numbers[0])
    return DEFAULT_TIMES.get(priority, 4)


def calculate_urgency(target: str, today: datetime) -> float:
    """Calculate urgency score based on target date."""
    if not target or target == "-":
        return 0.0
    try:
        target_date = datetime.strptime(target, "%Y-%m-%d")
        days_until = (target_date - today).days
        if days_until < 0:
            return 10.0  # Overdue
        elif days_until < 7:
            return 5.0  # Within week
        elif days_until < 30:
            return 2.0  # Within month
    except ValueError:
        pass
    return 0.0


def calculate_age(created: str, today: datetime) -> float:
    """Calculate age score based on creation date."""
    if not created:
        return 0.0
    try:
        created_date = datetime.strptime(created, "%Y-%m-%d")
        days_old = (today - created_date).days
        return min(days_old / 10.0, 5.0)  # Cap at 5 points
    except ValueError:
        pass
    return 0.0


def score_task(task_file: Path, today: datetime) -> TaskScore | None:
    """Calculate priority score for a single task."""
    content = task_file.read_text()

    # Extract metadata
    status = extract_metadata(content, "Statut")
    if "À faire" not in status and "⏳" not in status:
        return None  # Skip non-pending tasks

    task_id = extract_metadata(content, "ID") or task_file.stem
    title = extract_metadata(content, "Titre") or task_id
    priority = extract_metadata(content, "Priorité") or "🟡 Moyenne"
    time_str = extract_metadata(content, "Temps estimé")
    created = extract_metadata(content, "Créé le")
    target = extract_metadata(content, "Cible")

    # Calculate components
    time_hours = parse_time_estimate(time_str, priority)
    priority_value = PRIORITY_SCORES.get(priority, 5)
    urgency = calculate_urgency(target, today)
    age = calculate_age(created, today)

    # WSJF score
    total_value = priority_value + urgency + age
    score = round(total_value / time_hours, 2)

    return TaskScore(
        task_id=task_id,
        title=title,
        status=status,
        priority=priority,
        score=score,
        created=created,
        time_hours=time_hours,
        priority_value=priority_value,
        urgency=urgency,
        age=age,
    )


def get_all_scores(verbose: bool = False) -> list[TaskScore]:
    """Score all pending tasks and return sorted list."""
    today = datetime.now()
    scores = []

    for task_file in TASKS_DIR.glob("*.md"):
        if task_file.name == "TEMPLATE.md":
            continue
        result = score_task(task_file, today)
        if result:
            scores.append(result)
            if verbose:
                print(
                    f"  {result.task_id}: {result.score:.2f} "
                    f"(prio={result.priority_value}, urg={result.urgency:.0f}, "
                    f"age={result.age:.1f}, time={result.time_hours}h)"
                )

    scores.sort(key=lambda x: x.score, reverse=True)
    return scores


def update_tasks_md(scores: list[TaskScore], dry_run: bool = False) -> bool:
    """Update TASKS.md with new scores, preserving in-progress tasks at top."""
    content = TASKS_MD.read_text()

    # Build score lookup
    score_map = {s.task_id: s.score for s in scores}

    # Find the active tasks table
    table_pattern = r"(\| ID \| Titre \| Statut \| Priorité \| Score \| Créé le \|\n\|[-|]+\|\n)((?:\| .+\|\n)+)"
    match = re.search(table_pattern, content)

    if not match:
        print("Error: Could not find active tasks table in TASKS.md")
        return False

    header = match.group(1)
    rows = match.group(2)

    # Parse existing rows
    row_pattern = r"\| \[([A-Z]+-\d+)\].*?\| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|"
    parsed_rows = []

    for row_match in re.finditer(row_pattern, rows):
        task_id = row_match.group(1)
        title = row_match.group(2).strip()
        status = row_match.group(3).strip()
        priority = row_match.group(4).strip()
        old_score = row_match.group(5).strip()
        created = row_match.group(6).strip()

        # Update score if task is pending
        if "En cours" in status or "🔄" in status:
            new_score = "-"
            sort_key = float("-inf")  # Keep at top (smallest value sorts first)
        elif task_id in score_map:
            new_score = f"{score_map[task_id]:.2f}"
            sort_key = -score_map[task_id]  # Negative for descending sort
        else:
            new_score = old_score
            sort_key = 0

        parsed_rows.append(
            {
                "id": task_id,
                "title": title,
                "status": status,
                "priority": priority,
                "score": new_score,
                "created": created,
                "sort_key": sort_key,
            }
        )

    # Sort: in-progress first, then by score descending
    parsed_rows.sort(key=lambda x: x["sort_key"])

    # Rebuild table
    new_rows = []
    for row in parsed_rows:
        # Find the original link format
        link_match = re.search(
            rf"\| \[{row['id']}\]\(([^)]+)\)", rows
        )
        link = link_match.group(1) if link_match else f"tasks/{row['id']}.md"

        new_row = (
            f"| [{row['id']}]({link}) | {row['title']} | {row['status']} | "
            f"{row['priority']} | {row['score']} | {row['created']} |"
        )
        new_rows.append(new_row)

    new_table = header + "\n".join(new_rows) + "\n"
    new_content = content[: match.start()] + new_table + content[match.end() :]

    if dry_run:
        print("\n--- Dry run: would write ---")
        print(new_table)
        return True

    TASKS_MD.write_text(new_content)
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Update priority scores in TASKS.md"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show changes without writing",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed score breakdown",
    )
    args = parser.parse_args()

    print("🔄 Calculating priority scores...\n")

    scores = get_all_scores(verbose=args.verbose)

    if not scores:
        print("⚠️  No pending tasks found")
        return

    print(f"\n📊 Scored {len(scores)} tasks")
    print("\nTop 5:")
    for i, s in enumerate(scores[:5], 1):
        print(f"  {i}. {s.task_id}: {s.score:.2f}")

    if update_tasks_md(scores, dry_run=args.dry_run):
        if args.dry_run:
            print("\n✅ Dry run complete")
        else:
            print("\n✅ TASKS.md updated")
    else:
        print("\n❌ Failed to update TASKS.md")


if __name__ == "__main__":
    main()
