"""Priority scoring algorithm (WSJF - Weighted Shortest Job First).

This module implements the value/time prioritization algorithm for task-next command.

Formula: Score = Value / Time
Where: Value = Priority + Urgency + Age

CUPID: Composable - delegates to lib/wsjf.py for scoring calculations.
"""

import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import List, Optional

from scripts.lib.dates import parse_date
from scripts.lib.wsjf import WSJFConfig, calculate_age, calculate_urgency
from scripts.task_management.core.config_loader import (
    get_priority_score,
    load_paths,
    load_priorities,
)
from scripts.task_management.core.file_parser import (
    get_task_priority,
    get_task_status,
    parse_estimated_hours,
    parse_task_file,
)

# Use standard WSJF configuration (reference: update_priority_scores.py)
WSJF_CONFIG = WSJFConfig()


@dataclass
class TaskScore:
    """Scored task with all metrics."""
    task_id: str
    title: str
    priority: str
    time_hours: float
    value: float
    score: float
    # Breakdown
    priority_value: float
    urgency: float
    age: float
    # Metadata
    created_date: str
    target_date: Optional[str]
    file_path: Path


def score_task(task_file: Path, today: Optional[date] = None) -> Optional[TaskScore]:
    """Score a single task file.

    Args:
        task_file: Path to task markdown file
        today: Current date (defaults to today)

    Returns:
        TaskScore object, or None if task should be skipped (not "À faire")

    Raises:
        FileNotFoundError: If task file doesn't exist
    """
    if today is None:
        today = date.today()

    # Parse task file
    data = parse_task_file(task_file)
    metadata = data['metadata']

    # Skip if not "À faire"
    status = get_task_status(metadata)
    if '⏳' not in status and 'À faire' not in status:
        return None

    # Extract metadata
    task_id = metadata.get('ID', task_file.stem)
    title = metadata.get('Titre', task_id)
    priority = get_task_priority(metadata)
    created_date_str = metadata.get('Créé le', '')
    target_date_str = metadata.get('Cible', '')

    # Parse dates using shared lib
    created_date = parse_date(created_date_str)
    target_date = parse_date(target_date_str)

    # Get time estimate
    time_hours = parse_estimated_hours(metadata)

    # Use default time if not set
    if time_hours is None:
        task_prio, _, _ = load_priorities()
        if '🔴' in priority or 'Haute' in priority:
            time_hours = task_prio.high.default_time_hours
        elif '🟢' in priority or 'Basse' in priority:
            time_hours = task_prio.low.default_time_hours
        else:
            time_hours = task_prio.medium.default_time_hours

    # Calculate value components using shared lib
    priority_value = float(get_priority_score(priority))
    urgency_score = calculate_urgency(target_date, today, WSJF_CONFIG)
    age_score = calculate_age(created_date, today, WSJF_CONFIG)

    total_value = priority_value + urgency_score + age_score
    score = total_value / time_hours

    return TaskScore(
        task_id=task_id,
        title=title,
        priority=priority,
        time_hours=time_hours,
        value=total_value,
        score=score,
        priority_value=priority_value,
        urgency=urgency_score,
        age=age_score,
        created_date=created_date_str,
        target_date=target_date_str if target_date_str != '-' else None,
        file_path=task_file
    )


def rank_tasks(tasks_dir: Optional[Path] = None, today: Optional[date] = None) -> List[TaskScore]:
    """Score and rank all tasks in directory.

    Args:
        tasks_dir: Directory containing task files (defaults to config)
        today: Current date (defaults to today)

    Returns:
        List of TaskScore objects, sorted by score descending
    """
    if today is None:
        today = date.today()

    # Get tasks directory from config if not provided
    if tasks_dir is None:
        paths = load_paths()
        tasks_dir = Path(paths.tasks_dir)

    # Find all task files
    task_files = list(tasks_dir.glob('*.md'))
    if not task_files:
        return []

    # Score all tasks
    scored_tasks = []
    for task_file in task_files:
        try:
            score_result = score_task(task_file, today)
            if score_result is not None:  # Only include "À faire" tasks
                scored_tasks.append(score_result)
        except Exception as e:
            # Skip tasks that fail to parse
            print(f"Warning: Failed to parse {task_file.name}: {e}", file=sys.stderr)
            continue

    # Sort by score descending
    scored_tasks.sort(key=lambda x: x.score, reverse=True)

    return scored_tasks


def format_task_output(tasks: List[TaskScore], top_n: int = 3) -> str:
    """Format task scores for display.

    Args:
        tasks: List of scored tasks
        top_n: Number of top tasks to show in detail

    Returns:
        Formatted string for display
    """
    if not tasks:
        return "⚠️  Aucune tâche en attente!\n\nToutes les tâches sont terminées ou en cours."

    output = []
    output.append(f"🔍 Analyse des tâches (méthode: valeur/temps)\n")
    output.append(f"Tâches analysées: {len(tasks)}\n")

    # Top task (detailed)
    top = tasks[0]
    output.append(f"💡 Prochaine tâche suggérée: {top.task_id}\n")
    output.append(f"📋 {top.title}")
    output.append(f"{top.priority}")
    output.append(f"⏱️  Temps estimé: {top.time_hours} heure{'s' if top.time_hours > 1 else ''}")
    if top.created_date:
        output.append(f"📅 Créée le: {top.created_date}")
    output.append(f"\n✨ Pourquoi cette tâche?")
    output.append(f"  - Ratio valeur/temps élevé (Score: {top.score:.2f})")
    output.append(f"  - Valeur: {top.value:.1f} (Priorité={top.priority_value:.0f}, Urgence={top.urgency:.0f}, Âge={top.age:.1f})")

    # Other top tasks (summary)
    if len(tasks) > 1:
        output.append(f"\nAutres tâches à considérer:")
        for i, task in enumerate(tasks[1:top_n], 2):
            output.append(f"  {i}. {task.task_id} - {task.title[:50]}")
            output.append(f"     (Score: {task.score:.2f}, {task.priority}, {task.time_hours}h)")

    output.append(f"\nCommandes:")
    output.append(f"  /task-start {top.task_id}  - Démarrer cette tâche")
    output.append(f"  /task-next --start   - Démarrer automatiquement")

    return '\n'.join(output)


# ============================================================================
# CLI
# ============================================================================

if __name__ == '__main__':
    """CLI for testing and standalone usage."""
    import argparse

    parser = argparse.ArgumentParser(description='Score and rank tasks by priority')
    parser.add_argument('--top', type=int, default=3, help='Number of top tasks to show')
    parser.add_argument('--all', action='store_true', help='Show all tasks')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()

    # Run scoring
    tasks = rank_tasks()

    if args.json:
        import json
        output = [
            {
                'id': t.task_id,
                'title': t.title,
                'priority': t.priority,
                'time_hours': t.time_hours,
                'score': round(t.score, 2),
                'value': round(t.value, 1),
                'breakdown': {
                    'priority': t.priority_value,
                    'urgency': t.urgency,
                    'age': round(t.age, 1)
                }
            }
            for t in (tasks if args.all else tasks[:args.top])
        ]
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        # Formatted output
        print(format_task_output(tasks, args.top))
