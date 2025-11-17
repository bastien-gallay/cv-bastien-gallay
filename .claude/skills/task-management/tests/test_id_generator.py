"""Unit tests for id_generator.py"""

import pytest
from pathlib import Path
import tempfile
import shutil

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from core.id_generator import (
    slugify,
    find_existing_ids,
    get_next_number,
    generate_id,
    verify_id_unique,
    generate_filename,
    create_unique_id_and_filename,
)


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture
def temp_tasks_dir():
    """Create temporary tasks directory with sample files."""
    temp_dir = Path(tempfile.mkdtemp())
    tasks_dir = temp_dir / "tasks"
    tasks_dir.mkdir()

    # Create sample task files
    (tasks_dir / "CNT-001-sample-task.md").touch()
    (tasks_dir / "CNT-002-another-task.md").touch()
    (tasks_dir / "CNT-005-gap-in-sequence.md").touch()
    (tasks_dir / "TPL-001-template-task.md").touch()
    (tasks_dir / "TPL-002-another-template.md").touch()
    (tasks_dir / "TEMPLATE.md").touch()  # Should be ignored

    yield tasks_dir

    # Cleanup
    shutil.rmtree(temp_dir)


@pytest.fixture
def temp_dirs_with_archived():
    """Create temporary tasks and archived directories."""
    temp_dir = Path(tempfile.mkdtemp())
    tasks_dir = temp_dir / "tasks"
    archived_dir = temp_dir / "archived"
    tasks_dir.mkdir()
    archived_dir.mkdir()

    # Active tasks
    (tasks_dir / "CNT-001-active.md").touch()
    (tasks_dir / "CNT-003-active.md").touch()

    # Archived tasks
    (archived_dir / "CNT-002-archived.md").touch()
    (archived_dir / "TPL-001-archived.md").touch()

    yield tasks_dir, archived_dir

    # Cleanup
    shutil.rmtree(temp_dir)


# ============================================================================
# Test Slug Generation
# ============================================================================

def test_slugify_basic():
    """Test basic slug generation."""
    assert slugify("Hello World") == "hello-world"
    assert slugify("Test Task") == "test-task"


def test_slugify_accents():
    """Test slug generation with accented characters."""
    assert slugify("Mettre à jour l'expérience") == "mettre-a-jour-l-experience"
    assert slugify("Créer une tâche") == "creer-une-tache"


def test_slugify_special_chars():
    """Test slug generation with special characters."""
    assert slugify("Add AWS Certification (Solutions Architect)") == "add-aws-certification-solutions-architect"
    assert slugify("Fix bug #123") == "fix-bug-123"
    assert slugify("Update doc/README.md") == "update-doc-readme-md"


def test_slugify_multiple_spaces():
    """Test slug generation with multiple spaces."""
    assert slugify("Too    many     spaces") == "too-many-spaces"


def test_slugify_max_length():
    """Test slug truncation."""
    long_text = "This is a very long title that exceeds the maximum length allowed for slugs"
    slug = slugify(long_text, max_length=30)
    assert len(slug) <= 30
    assert slug.endswith('-') is False  # Should not end with hyphen


def test_slugify_edge_cases():
    """Test edge cases."""
    assert slugify("") == ""
    assert slugify("---") == ""
    assert slugify("123") == "123"


# ============================================================================
# Test ID Discovery
# ============================================================================

def test_find_existing_ids(temp_tasks_dir):
    """Test finding existing IDs in tasks directory."""
    existing = find_existing_ids(tasks_dir=temp_tasks_dir, archived_dir=None)

    assert 'CNT' in existing
    assert 'TPL' in existing
    assert sorted(existing['CNT']) == [1, 2, 5]
    assert sorted(existing['TPL']) == [1, 2]


def test_find_existing_ids_with_archived(temp_dirs_with_archived):
    """Test finding IDs across both tasks and archived directories."""
    tasks_dir, archived_dir = temp_dirs_with_archived
    existing = find_existing_ids(tasks_dir=tasks_dir, archived_dir=archived_dir)

    assert 'CNT' in existing
    assert 'TPL' in existing
    # Should combine both directories: CNT-001, CNT-002 (archived), CNT-003
    assert sorted(existing['CNT']) == [1, 2, 3]
    assert sorted(existing['TPL']) == [1]


def test_find_existing_ids_empty_dir():
    """Test with empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        tasks_dir = Path(temp_dir) / "tasks"
        tasks_dir.mkdir()

        existing = find_existing_ids(tasks_dir=tasks_dir, archived_dir=None)
        assert existing == {}


def test_find_existing_ids_ignores_template(temp_tasks_dir):
    """Test that TEMPLATE.md is ignored."""
    existing = find_existing_ids(tasks_dir=temp_tasks_dir, archived_dir=None)

    # Should not have 'TEMPLATE' key
    for trig in existing:
        assert trig != 'TEMPLATE'


# ============================================================================
# Test Next Number Generation
# ============================================================================

def test_get_next_number_empty():
    """Test next number when no IDs exist."""
    assert get_next_number('CNT', {}) == 1
    assert get_next_number('TPL', {}) == 1


def test_get_next_number_sequential():
    """Test next number in sequential series."""
    existing = {'CNT': [1, 2, 3, 4]}
    assert get_next_number('CNT', existing) == 5


def test_get_next_number_gap():
    """Test next number when there's a gap."""
    existing = {'CNT': [1, 2, 5, 8]}
    assert get_next_number('CNT', existing) == 3  # Fill gap


def test_get_next_number_invalid_trigramme():
    """Test with invalid trigramme."""
    with pytest.raises(ValueError, match="Invalid trigramme"):
        get_next_number('XXX', {})


def test_get_next_number_exhausted():
    """Test when all numbers are exhausted."""
    existing = {'CNT': list(range(1, 1000))}
    with pytest.raises(ValueError, match="All IDs exhausted"):
        get_next_number('CNT', existing)


# ============================================================================
# Test ID Generation
# ============================================================================

def test_generate_id():
    """Test ID generation."""
    existing = {'CNT': [1, 2, 3]}
    task_id = generate_id('CNT', existing)
    assert task_id == 'CNT-004'


def test_generate_id_lowercase():
    """Test ID generation with lowercase trigramme."""
    existing = {'CNT': [1]}
    task_id = generate_id('cnt', existing)
    assert task_id == 'CNT-002'  # Should uppercase


def test_generate_id_format():
    """Test ID format is correct."""
    existing = {'TPL': [1]}
    task_id = generate_id('TPL', existing)
    assert task_id == 'TPL-002'
    assert len(task_id) == 7  # XXX-NNN
    assert task_id[3] == '-'


# ============================================================================
# Test ID Uniqueness Verification
# ============================================================================

def test_verify_id_unique_true(temp_tasks_dir):
    """Test verification when ID is unique."""
    assert verify_id_unique('CNT-999', tasks_dir=temp_tasks_dir, archived_dir=None) is True
    assert verify_id_unique('QUA-001', tasks_dir=temp_tasks_dir, archived_dir=None) is True


def test_verify_id_unique_false(temp_tasks_dir):
    """Test verification when ID already exists."""
    assert verify_id_unique('CNT-001', tasks_dir=temp_tasks_dir, archived_dir=None) is False
    assert verify_id_unique('CNT-002', tasks_dir=temp_tasks_dir, archived_dir=None) is False


def test_verify_id_unique_with_archived(temp_dirs_with_archived):
    """Test verification across both directories."""
    tasks_dir, archived_dir = temp_dirs_with_archived
    # CNT-002 is in archived
    assert verify_id_unique('CNT-002', tasks_dir=tasks_dir, archived_dir=archived_dir) is False
    # CNT-004 doesn't exist
    assert verify_id_unique('CNT-004', tasks_dir=tasks_dir, archived_dir=archived_dir) is True


# ============================================================================
# Test Filename Generation
# ============================================================================

def test_generate_filename():
    """Test filename generation."""
    filename = generate_filename('CNT-005', 'Mettre à jour expérience')
    assert filename == 'CNT-005-mettre-a-jour-experience.md'


def test_generate_filename_special_chars():
    """Test filename with special characters in title."""
    filename = generate_filename('TPL-001', 'Add Template (v2.0)')
    assert filename == 'TPL-001-add-template-v2-0.md'


# ============================================================================
# Test High-Level API
# ============================================================================

def test_create_unique_id_and_filename(monkeypatch, temp_tasks_dir):
    """Test complete ID and filename creation."""
    # Mock find_existing_ids to return temp directory data
    def mock_find_existing_ids(tasks_dir=None, archived_dir=None):
        return {'CNT': [1, 2, 5], 'TPL': [1, 2]}

    monkeypatch.setattr('core.id_generator.find_existing_ids', mock_find_existing_ids)

    # CNT has 001, 002, 005, so next should be 003 (gap fill)
    task_id, filename = create_unique_id_and_filename('CNT', 'Test Task')

    assert task_id == 'CNT-003'
    assert filename == 'CNT-003-test-task.md'


def test_create_unique_id_and_filename_new_trigramme(monkeypatch):
    """Test with trigramme that has no existing tasks."""
    # Mock find_existing_ids to return empty for QUA
    def mock_find_existing_ids(tasks_dir=None, archived_dir=None):
        return {'CNT': [1], 'TPL': [1]}  # QUA not in dict

    monkeypatch.setattr('core.id_generator.find_existing_ids', mock_find_existing_ids)

    task_id, filename = create_unique_id_and_filename('QUA', 'Quality Check')

    assert task_id == 'QUA-001'
    assert filename == 'QUA-001-quality-check.md'
