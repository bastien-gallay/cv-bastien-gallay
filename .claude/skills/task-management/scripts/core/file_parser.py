"""Markdown task file parser.

This module provides utilities to parse task files in markdown format,
extracting metadata tables, subtasks, sections, and other structured data.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional


def parse_metadata_table(content: str) -> Dict[str, str]:
    """Extract metadata from markdown table format.

    Parses tables like:
        | **Key** | Value |
        |---------|-------|
        | **ID** | CNT-001 |

    Args:
        content: Markdown file content

    Returns:
        Dict mapping field names to values (e.g., {'ID': 'CNT-001', 'Statut': '⏳ À faire'})
    """
    metadata = {}

    # Match lines like: | **Key** | Value |
    pattern = r'\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]+)\s*\|'

    for match in re.finditer(pattern, content):
        key = match.group(1).strip()
        value = match.group(2).strip()

        # Skip separator rows (-----)
        if not value.startswith('-'):
            metadata[key] = value

    return metadata


def extract_subtasks(content: str) -> List[Tuple[bool, str]]:
    """Extract subtasks from checkbox list.

    Parses:
        - [ ] Uncompleted task
        - [x] Completed task
        - [X] Also completed

    Args:
        content: Markdown file content

    Returns:
        List of (is_completed, task_text) tuples
    """
    subtasks = []

    # Match - [ ] or - [x] or - [X]
    pattern = r'^- \[([ xX])\]\s*(.+)$'

    for line in content.split('\n'):
        match = re.match(pattern, line.strip())
        if match:
            is_completed = match.group(1).lower() == 'x'
            task_text = match.group(2).strip()
            subtasks.append((is_completed, task_text))

    return subtasks


def extract_section(content: str, header: str, level: int = 2) -> Optional[str]:
    """Extract content under a specific markdown header.

    Args:
        content: Markdown file content
        header: Header text to find (e.g., "Description")
        level: Header level (1-6, default 2 for ##)

    Returns:
        Content under the header, or None if not found
    """
    # Build header pattern (e.g., ## Description)
    header_marker = '#' * level
    pattern = rf'^{header_marker}\s+{re.escape(header)}\s*$'

    lines = content.split('\n')
    section_lines = []
    in_section = False

    for line in lines:
        # Check if we're starting the target section
        if re.match(pattern, line, re.IGNORECASE):
            in_section = True
            continue

        # Check if we hit another header of same or higher level (end section)
        if in_section:
            header_pattern = rf'^#{{{1},{level}}}\s+'
            if re.match(header_pattern, line):
                break
            section_lines.append(line)

    if not section_lines:
        return None

    # Join and strip whitespace
    result = '\n'.join(section_lines).strip()
    return result if result else None


def parse_task_file(file_path: Path) -> Dict[str, any]:
    """Parse a complete task file and extract all relevant data.

    Args:
        file_path: Path to task markdown file

    Returns:
        Dict with keys:
            - metadata: Dict of metadata fields
            - subtasks: List of (completed, text) tuples
            - subtasks_completed: Int count of completed subtasks
            - subtasks_total: Int count of total subtasks
            - description: Description section text (or None)
            - notes_claude: Notes for Claude section text (or None)
            - notes_user: Notes for user section text (or None)

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Task file not found: {file_path}")

    content = file_path.read_text(encoding='utf-8')

    # Parse metadata
    metadata = parse_metadata_table(content)

    # Parse subtasks
    subtasks = extract_subtasks(content)
    subtasks_completed = sum(1 for completed, _ in subtasks if completed)
    subtasks_total = len(subtasks)

    # Extract sections (level=2 for H2 headers: ##)
    description = extract_section(content, "Description", level=2)
    notes_claude = extract_section(content, "Notes pour Claude", level=2)
    notes_user = extract_section(content, "Notes pour l'utilisateur", level=2)

    return {
        'metadata': metadata,
        'subtasks': subtasks,
        'subtasks_completed': subtasks_completed,
        'subtasks_total': subtasks_total,
        'description': description,
        'notes_claude': notes_claude,
        'notes_user': notes_user,
    }


def get_task_status(metadata: Dict[str, str]) -> str:
    """Extract task status from metadata.

    Args:
        metadata: Metadata dict from parse_metadata_table()

    Returns:
        Status string (e.g., "⏳ À faire", "🔄 En cours")

    Raises:
        KeyError: If Statut field not found
    """
    return metadata['Statut']


def get_task_priority(metadata: Dict[str, str]) -> str:
    """Extract task priority from metadata.

    Args:
        metadata: Metadata dict from parse_metadata_table()

    Returns:
        Priority string (e.g., "🔴 Haute", "🟡 Moyenne")

    Raises:
        KeyError: If Priorité field not found
    """
    return metadata['Priorité']


def parse_estimated_hours(metadata: Dict[str, str]) -> Optional[float]:
    """Parse estimated hours from metadata.

    Handles formats:
        - "2 heures"
        - "2.5 heures"
        - "2"
        - "(à remplir après)"
        - ""

    Args:
        metadata: Metadata dict from parse_metadata_table()

    Returns:
        Float hours, or None if not set/parseable
    """
    if 'Temps estimé' not in metadata:
        return None

    value = metadata['Temps estimé'].strip()

    # Empty or placeholder
    if not value or value.startswith('(') or value == '-':
        return None

    # Extract number (handles "2.5 heures" or "2.5")
    match = re.search(r'(\d+(?:\.\d+)?)', value)
    if match:
        return float(match.group(1))

    return None


# ============================================================================
# CLI for Testing
# ============================================================================

if __name__ == '__main__':
    """Test file parser on actual task file."""
    import sys

    print("Testing file_parser.py")
    print("=" * 60)

    # Find a task file to test with
    tasks_dir = Path('../../../.tasks/tasks')

    if not tasks_dir.exists():
        print(f"❌ Tasks directory not found: {tasks_dir}")
        sys.exit(1)

    # Get first task file
    task_files = list(tasks_dir.glob('*.md'))
    if not task_files:
        print("❌ No task files found")
        sys.exit(1)

    test_file = task_files[0]
    print(f"Testing with: {test_file.name}")
    print("-" * 60)

    # Parse file
    data = parse_task_file(test_file)

    print("\n1. Metadata:")
    for key, value in data['metadata'].items():
        print(f"   {key}: {value}")

    print(f"\n2. Subtasks: {data['subtasks_completed']}/{data['subtasks_total']} completed")
    for completed, text in data['subtasks'][:3]:  # Show first 3
        status = "✓" if completed else "○"
        print(f"   {status} {text}")
    if len(data['subtasks']) > 3:
        print(f"   ... and {len(data['subtasks']) - 3} more")

    print("\n3. Status and Priority:")
    print(f"   Status: {get_task_status(data['metadata'])}")
    print(f"   Priority: {get_task_priority(data['metadata'])}")

    hours = parse_estimated_hours(data['metadata'])
    print(f"   Estimated: {hours} hours" if hours else "   Estimated: Not set")

    print("\n4. Sections:")
    if data['description']:
        desc_preview = data['description'][:100] + "..." if len(data['description']) > 100 else data['description']
        print(f"   Description: {desc_preview}")
    if data['notes_claude']:
        print(f"   Notes for Claude: {len(data['notes_claude'])} chars")

    print("\n✅ File parsed successfully!")
    print("=" * 60)
