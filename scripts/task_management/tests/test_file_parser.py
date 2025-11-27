"""Unit tests for file_parser.py"""

import pytest
from pathlib import Path
import sys

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from scripts.task_management.core.file_parser import (
    parse_metadata_table,
    extract_subtasks,
    extract_section,
    parse_task_file,
    get_task_status,
    get_task_priority,
    parse_estimated_hours
)


def test_parse_metadata_table():
    """Test metadata table parsing."""
    content = """
| **ID** | TST-001 |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
"""
    metadata = parse_metadata_table(content)

    assert metadata['ID'] == 'TST-001'
    assert metadata['Statut'] == '⏳ À faire'
    assert metadata['Priorité'] == '🟡 Moyenne'


def test_extract_subtasks():
    """Test subtask extraction."""
    content = """
- [x] Completed task
- [ ] Incomplete task
- [X] Also completed
"""
    subtasks = extract_subtasks(content)

    assert len(subtasks) == 3
    assert subtasks[0] == (True, 'Completed task')
    assert subtasks[1] == (False, 'Incomplete task')
    assert subtasks[2] == (True, 'Also completed')


def test_extract_section():
    """Test section extraction."""
    content = """
## Description

This is the description.

## Another Section

This is another section.
"""
    desc = extract_section(content, "Description")
    assert desc is not None
    assert 'This is the description.' in desc

    other = extract_section(content, "Another Section")
    assert other is not None
    assert 'This is another section.' in other

    missing = extract_section(content, "Missing")
    assert missing is None


def test_parse_task_file():
    """Test complete task file parsing."""
    fixture_path = Path(__file__).parent / "fixtures" / "sample_task.md"

    data = parse_task_file(fixture_path)

    # Check metadata
    assert data['metadata']['ID'] == 'TST-001'
    assert data['metadata']['Statut'] == '⏳ À faire'

    # Check subtasks
    assert data['subtasks_total'] == 4
    assert data['subtasks_completed'] == 2

    # Check sections
    assert data['description'] is not None
    assert 'sample task file' in data['description'].lower()


def test_get_task_status():
    """Test status extraction."""
    metadata = {'Statut': '🔄 En cours'}
    assert get_task_status(metadata) == '🔄 En cours'


def test_get_task_priority():
    """Test priority extraction."""
    metadata = {'Priorité': '🔴 Haute'}
    assert get_task_priority(metadata) == '🔴 Haute'


def test_parse_estimated_hours():
    """Test hour parsing."""
    # Valid formats
    assert parse_estimated_hours({'Temps estimé': '2 heures'}) == 2.0
    assert parse_estimated_hours({'Temps estimé': '2.5 heures'}) == 2.5
    assert parse_estimated_hours({'Temps estimé': '2.5'}) == 2.5

    # Invalid/empty
    assert parse_estimated_hours({'Temps estimé': ''}) is None
    assert parse_estimated_hours({'Temps estimé': '-'}) is None
    assert parse_estimated_hours({'Temps estimé': '(à remplir)'}) is None
    assert parse_estimated_hours({}) is None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
