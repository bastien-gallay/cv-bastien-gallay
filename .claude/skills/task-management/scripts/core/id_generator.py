"""Task ID generator with slug creation and uniqueness validation.

This module provides functions to generate unique task IDs following the
XXX-NNN format, create URL-safe slugs from titles, and verify ID uniqueness
across the task repository.
"""

import re
import sys
import unicodedata
from pathlib import Path
from typing import Optional, Tuple, List

# Try relative import (when used as module), fall back to absolute (when run as script)
try:
    from .config_loader import load_paths, load_trigrammes
except ImportError:
    # Add parent directory to path for CLI usage
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from core.config_loader import load_paths, load_trigrammes


# ============================================================================
# Slug Generation
# ============================================================================

def slugify(text: str, max_length: int = 60) -> str:
    """Convert text to URL-safe slug.

    Args:
        text: Input text to slugify
        max_length: Maximum slug length (default 60)

    Returns:
        URL-safe slug (lowercase, hyphen-separated)

    Examples:
        >>> slugify("Mettre à jour l'expérience")
        'mettre-a-jour-l-experience'
        >>> slugify("Add Certification (AWS)")
        'add-certification-aws'
    """
    # Normalize unicode characters (é -> e, etc.)
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')

    # Convert to lowercase
    text = text.lower()

    # Replace non-alphanumeric with hyphens
    text = re.sub(r'[^a-z0-9]+', '-', text)

    # Remove leading/trailing hyphens
    text = text.strip('-')

    # Collapse multiple hyphens
    text = re.sub(r'-+', '-', text)

    # Truncate to max length (at word boundary if possible)
    if len(text) > max_length:
        text = text[:max_length].rsplit('-', 1)[0]

    return text


# ============================================================================
# ID Discovery
# ============================================================================

def find_existing_ids(tasks_dir: Optional[Path] = None,
                     archived_dir: Optional[Path] = None) -> dict[str, List[int]]:
    """Find all existing task IDs in tasks and archived directories.

    Args:
        tasks_dir: Path to tasks directory (default from config)
        archived_dir: Path to archived directory (default from config)

    Returns:
        Dictionary mapping trigramme to list of used numbers
        Example: {'CNT': [1, 2, 5, 8], 'TPL': [1, 2]}

    Raises:
        FileNotFoundError: If tasks_dir doesn't exist
    """
    paths = load_paths()

    if tasks_dir is None:
        tasks_dir = Path(paths.tasks_dir)
    if archived_dir is None:
        archived_dir = Path(paths.archived_dir)

    if not tasks_dir.exists():
        raise FileNotFoundError(f"Tasks directory not found: {tasks_dir}")

    # Pattern to match task IDs: XXX-NNN
    pattern = re.compile(r'^([A-Z]{3})-(\d{3})')

    # Track IDs by trigramme
    ids_by_trigramme: dict[str, List[int]] = {}

    # Scan tasks directory
    for file_path in tasks_dir.glob('*.md'):
        if file_path.name == 'TEMPLATE.md':
            continue

        match = pattern.match(file_path.stem)
        if match:
            trigramme, number_str = match.groups()
            number = int(number_str)

            if trigramme not in ids_by_trigramme:
                ids_by_trigramme[trigramme] = []
            ids_by_trigramme[trigramme].append(number)

    # Scan archived directory if it exists
    if archived_dir.exists():
        for file_path in archived_dir.glob('*.md'):
            match = pattern.match(file_path.stem)
            if match:
                trigramme, number_str = match.groups()
                number = int(number_str)

                if trigramme not in ids_by_trigramme:
                    ids_by_trigramme[trigramme] = []
                if number not in ids_by_trigramme[trigramme]:
                    ids_by_trigramme[trigramme].append(number)

    # Sort each list
    for trigramme in ids_by_trigramme:
        ids_by_trigramme[trigramme].sort()

    return ids_by_trigramme


def get_next_number(trigramme: str,
                   existing_ids: Optional[dict[str, List[int]]] = None) -> int:
    """Get the next available number for a trigramme.

    Args:
        trigramme: 3-letter category code (e.g., 'CNT', 'TPL')
        existing_ids: Pre-computed existing IDs (default: scan directories)

    Returns:
        Next available number (1-999)

    Raises:
        ValueError: If trigramme is invalid or all numbers exhausted

    Examples:
        >>> get_next_number('CNT', {'CNT': [1, 2, 3]})
        4
        >>> get_next_number('TPL', {})
        1
    """
    # Validate trigramme
    trigrammes_dict, _ = load_trigrammes()
    if trigramme not in trigrammes_dict:
        valid = ', '.join(trigrammes_dict.keys())
        raise ValueError(f"Invalid trigramme '{trigramme}'. Valid: {valid}")

    # Get existing IDs
    if existing_ids is None:
        existing_ids = find_existing_ids()

    # Find next number
    if trigramme not in existing_ids or not existing_ids[trigramme]:
        return 1

    used_numbers = existing_ids[trigramme]

    # Check for gaps in sequence
    for i, num in enumerate(used_numbers, start=1):
        if i < num:
            return i

    # No gaps, use next sequential number
    next_num = max(used_numbers) + 1

    if next_num > 999:
        raise ValueError(f"All IDs exhausted for trigramme '{trigramme}'")

    return next_num


# ============================================================================
# ID Generation
# ============================================================================

def generate_id(trigramme: str,
               existing_ids: Optional[dict[str, List[int]]] = None) -> str:
    """Generate next available task ID for a trigramme.

    Args:
        trigramme: 3-letter category code (e.g., 'CNT')
        existing_ids: Pre-computed existing IDs (optional)

    Returns:
        Task ID in format 'XXX-NNN' (e.g., 'CNT-005')

    Raises:
        ValueError: If trigramme is invalid

    Examples:
        >>> generate_id('CNT')
        'CNT-016'
        >>> generate_id('TPL', {'TPL': [1, 2]})
        'TPL-003'
    """
    trigramme = trigramme.upper()
    number = get_next_number(trigramme, existing_ids)
    return f"{trigramme}-{number:03d}"


def verify_id_unique(task_id: str,
                    tasks_dir: Optional[Path] = None,
                    archived_dir: Optional[Path] = None) -> bool:
    """Verify that a task ID is unique (doesn't exist in files).

    Args:
        task_id: Task ID to verify (e.g., 'CNT-005')
        tasks_dir: Path to tasks directory (default from config)
        archived_dir: Path to archived directory (default from config)

    Returns:
        True if ID is unique, False if already used

    Examples:
        >>> verify_id_unique('CNT-999')
        True
        >>> verify_id_unique('CNT-001')  # Exists
        False
    """
    paths = load_paths()

    if tasks_dir is None:
        tasks_dir = Path(paths.tasks_dir)
    if archived_dir is None:
        archived_dir = Path(paths.archived_dir)

    # Check tasks directory
    if tasks_dir.exists():
        for file_path in tasks_dir.glob(f'{task_id}-*.md'):
            return False

    # Check archived directory
    if archived_dir.exists():
        for file_path in archived_dir.glob(f'{task_id}-*.md'):
            return False

    return True


def generate_filename(task_id: str, title: str) -> str:
    """Generate task filename from ID and title.

    Args:
        task_id: Task ID (e.g., 'CNT-005')
        title: Task title

    Returns:
        Filename in format '{ID}-{slug}.md'

    Examples:
        >>> generate_filename('CNT-005', 'Mettre à jour expérience')
        'CNT-005-mettre-a-jour-experience.md'
    """
    slug = slugify(title)
    return f"{task_id}-{slug}.md"


# ============================================================================
# High-Level API
# ============================================================================

def create_unique_id_and_filename(trigramme: str, title: str) -> Tuple[str, str]:
    """Generate unique ID and filename for a new task.

    This is the main entry point for task creation workflows.

    Args:
        trigramme: 3-letter category code
        title: Task title

    Returns:
        Tuple of (task_id, filename)
        Example: ('CNT-016', 'CNT-016-ajouter-experience.md')

    Raises:
        ValueError: If trigramme is invalid or IDs exhausted
    """
    # Generate ID
    task_id = generate_id(trigramme)

    # Verify uniqueness (should always be True, but double-check)
    if not verify_id_unique(task_id):
        # Shouldn't happen, but fallback to scanning
        existing_ids = find_existing_ids()
        next_num = get_next_number(trigramme, existing_ids)
        task_id = f"{trigramme.upper()}-{next_num:03d}"

    # Generate filename
    filename = generate_filename(task_id, title)

    return task_id, filename


# ============================================================================
# CLI for Testing
# ============================================================================

if __name__ == '__main__':
    """Test ID generator."""
    print("Testing id_generator.py")
    print("=" * 60)

    print("\n1. Finding existing IDs...")
    existing = find_existing_ids()
    for trig, nums in sorted(existing.items()):
        print(f"   {trig}: {nums[:5]}{'...' if len(nums) > 5 else ''} ({len(nums)} total)")

    print("\n2. Generating next IDs...")
    trigrammes_dict, _ = load_trigrammes()
    for trig in sorted(trigrammes_dict.keys()):
        next_id = generate_id(trig, existing)
        is_unique = verify_id_unique(next_id)
        status = "✅" if is_unique else "❌"
        print(f"   {trig} -> {next_id} {status}")

    print("\n3. Testing slug generation...")
    test_titles = [
        "Mettre à jour l'expérience professionnelle",
        "Add AWS Certification (Solutions Architect)",
        "Corriger les dates de début Freelance",
    ]
    for title in test_titles:
        slug = slugify(title)
        print(f"   '{title}' -> '{slug}'")

    print("\n4. Testing full workflow...")
    test_trigramme = 'CNT'
    test_title = "Test task creation workflow"
    task_id, filename = create_unique_id_and_filename(test_trigramme, test_title)
    print(f"   Trigramme: {test_trigramme}")
    print(f"   Title: {test_title}")
    print(f"   Generated ID: {task_id}")
    print(f"   Generated filename: {filename}")
    print(f"   ID is unique: {verify_id_unique(task_id)}")

    print("\n✅ All tests completed!")
    print("=" * 60)
