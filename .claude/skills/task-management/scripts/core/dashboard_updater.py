"""Dashboard updater for TASKS.md management.

This module provides functions to update the TASKS.md dashboard file,
including adding new tasks, moving tasks between sections, and updating statistics.
"""

import sys
from pathlib import Path
from typing import Optional, Tuple
import re
from datetime import datetime

# Try relative import (when used as module), fall back to absolute (when run as script)
try:
    from .config_loader import load_paths
except ImportError:
    # Add parent directory to path for CLI usage
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from core.config_loader import load_paths


# ============================================================================
# Dashboard Reading
# ============================================================================

def read_dashboard() -> Tuple[str, dict]:
    """Read TASKS.md and extract key sections.

    Returns:
        Tuple of (full_content, sections_dict) where sections_dict contains:
            - 'active': Lines in active tasks table
            - 'completed': Lines in completed tasks table
            - 'before_active': Content before active table
            - 'after_active': Content after active table (before completed)
            - 'after_completed': Content after completed table
    """
    paths = load_paths()
    dashboard_path = Path(paths.tasks_dashboard)

    if not dashboard_path.exists():
        raise FileNotFoundError(f"Dashboard not found: {dashboard_path}")

    content = dashboard_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    sections = {
        'active': [],
        'completed': [],
        'before_active': [],
        'after_active': [],
        'after_completed': [],
    }

    current_section = 'before_active'
    in_active_table = False
    in_completed_table = False

    for line in lines:
        # Detect table headers
        if '## Tâches actives' in line:
            sections['before_active'].append(line)
            current_section = 'active_header'
            continue
        elif '## Tâches terminées' in line:
            current_section = 'completed_header'
            sections['after_active'].append(line)
            continue

        # Detect table structure
        if current_section == 'active_header':
            sections['before_active'].append(line)
            if line.startswith('|') and '---' in line:
                in_active_table = True
                current_section = 'active'
            continue
        elif current_section == 'completed_header':
            sections['after_active'].append(line)
            if line.startswith('|') and '---' in line:
                in_completed_table = True
                current_section = 'completed'
            continue

        # Collect table rows
        if current_section == 'active':
            if line.startswith('|') and line.strip() != '|':
                sections['active'].append(line)
            else:
                in_active_table = False
                current_section = 'after_active'
                sections['after_active'].append(line)
        elif current_section == 'completed':
            if line.startswith('|') and line.strip() != '|':
                sections['completed'].append(line)
            else:
                in_completed_table = False
                current_section = 'after_completed'
                sections['after_completed'].append(line)
        else:
            sections[current_section].append(line)

    return content, sections


# ============================================================================
# Task Row Formatting
# ============================================================================

def format_task_row(task_id: str, title: str, status: str, priority: str, date: str, filename: str) -> str:
    """Format a task as a table row.

    Args:
        task_id: Task ID (e.g., 'CNT-005')
        title: Task title
        status: Task status emoji
        priority: Task priority emoji
        date: Date string (YYYY-MM-DD)
        filename: Task file name for link

    Returns:
        Markdown table row string

    Example:
        >>> format_task_row('CNT-005', 'Test Task', '⏳ À faire', '🔴 Haute', '2025-11-16', 'CNT-005-test.md')
        '| [CNT-005](tasks/CNT-005-test.md) | Test Task | ⏳ À faire | 🔴 Haute | 2025-11-16 |'
    """
    return f"| [{task_id}](tasks/{filename}) | {title} | {status} | {priority} | {date} |"


# ============================================================================
# Dashboard Updates
# ============================================================================

def add_task_to_dashboard(task_id: str, title: str, status: str, priority: str,
                         created_date: str, filename: str) -> None:
    """Add a new task to the active tasks table in TASKS.md.

    Tasks are inserted in order: priority (Haute > Moyenne > Basse), then by date.

    Args:
        task_id: Task ID
        title: Task title
        status: Task status (default: '⏳ À faire')
        priority: Task priority
        created_date: Creation date (YYYY-MM-DD)
        filename: Task file name
    """
    content, sections = read_dashboard()

    # Create new row
    new_row = format_task_row(task_id, title, status, priority, created_date, filename)

    # Find insertion point based on priority and date
    insert_index = 0
    priority_order = {'🔴 Haute': 0, '🟡 Moyenne': 1, '🟢 Basse': 2}
    new_priority_rank = priority_order.get(priority, 1)

    for i, row in enumerate(sections['active']):
        # Extract priority from existing row
        match = re.search(r'(🔴 Haute|🟡 Moyenne|🟢 Basse)', row)
        if match:
            row_priority = match.group(1)
            row_priority_rank = priority_order.get(row_priority, 1)

            if new_priority_rank < row_priority_rank:
                # Higher priority, insert here
                break
            elif new_priority_rank > row_priority_rank:
                # Lower priority, continue
                insert_index = i + 1
            else:
                # Same priority, sort by date
                date_match = re.search(r'\d{4}-\d{2}-\d{2}', row)
                if date_match:
                    row_date = date_match.group()
                    if created_date <= row_date:
                        break
                insert_index = i + 1
        else:
            insert_index = i + 1

    # Insert the new row
    sections['active'].insert(insert_index, new_row)

    # Rebuild dashboard
    write_dashboard(sections)


def move_task_to_completed(task_id: str, completed_date: str) -> None:
    """Move a task from active to completed section.

    Args:
        task_id: Task ID to move
        completed_date: Completion date (YYYY-MM-DD)
    """
    content, sections = read_dashboard()

    # Find and remove from active
    task_row = None
    for i, row in enumerate(sections['active']):
        if task_id in row:
            task_row = sections['active'].pop(i)
            break

    if not task_row:
        raise ValueError(f"Task {task_id} not found in active tasks")

    # Update the row: change status and date
    # Replace status with "✅ Terminé"
    task_row = re.sub(r'(⏳ À faire|🔄 En cours|🚫 Bloqué)', '✅ Terminé', task_row)
    # Replace the last date with completed date
    task_row = re.sub(r'\d{4}-\d{2}-\d{2}(?=[^|]*\|[^|]*$)', completed_date, task_row)

    # Insert at beginning of completed tasks
    sections['completed'].insert(0, task_row)

    # Rebuild dashboard
    write_dashboard(sections)


def update_task_status(task_id: str, new_status: str) -> None:
    """Update the status of a task in the dashboard.

    Args:
        task_id: Task ID
        new_status: New status emoji (e.g., '🔄 En cours')
    """
    content, sections = read_dashboard()

    # Find and update in active tasks
    for i, row in enumerate(sections['active']):
        if task_id in row:
            # Replace status
            updated_row = re.sub(
                r'(⏳ À faire|🔄 En cours|🚫 Bloqué|✅ Terminé)',
                new_status,
                row
            )
            sections['active'][i] = updated_row
            break
    else:
        raise ValueError(f"Task {task_id} not found in active tasks")

    # Rebuild dashboard
    write_dashboard(sections)


def write_dashboard(sections: dict) -> None:
    """Write updated sections back to TASKS.md.

    Args:
        sections: Sections dict from read_dashboard()
    """
    paths = load_paths()
    dashboard_path = Path(paths.tasks_dashboard)

    lines = []
    lines.extend(sections['before_active'])
    lines.extend(sections['active'])
    lines.extend(sections['after_active'])
    lines.extend(sections['completed'])
    lines.extend(sections['after_completed'])

    content = '\n'.join(lines)
    dashboard_path.write_text(content, encoding='utf-8')


# ============================================================================
# CLI for Testing
# ============================================================================

if __name__ == '__main__':
    """Test dashboard operations."""
    print("Testing dashboard_updater.py")
    print("=" * 60)

    print("\n1. Reading dashboard...")
    content, sections = read_dashboard()
    print(f"   Active tasks: {len(sections['active'])}")
    print(f"   Completed tasks: {len(sections['completed'])}")

    print("\n2. Testing format_task_row...")
    row = format_task_row('CNT-999', 'Test Task', '⏳ À faire', '🔴 Haute', '2025-11-16', 'CNT-999-test.md')
    print(f"   {row}")

    print("\n✅ Dashboard operations working!")
    print("=" * 60)
