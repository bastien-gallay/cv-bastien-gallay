"""Unit tests for dor_validator.py"""

import pytest
from pathlib import Path
import tempfile
import shutil
import sys

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from scripts.task_management.validators.dor_validator import (
    ValidationIssue,
    DorValidationResult,
    validate_file_exists,
    validate_status,
    validate_description,
    validate_acceptance_criteria,
    validate_subtasks,
    validate_metadata_complete,
    validate_dor,
)


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture
def sample_task_data_valid():
    """Valid task data for testing."""
    return {
        'metadata': {
            'ID': 'CNT-005',
            'Titre': 'Test Task',
            'Statut': '⏳ À faire',
            'Priorité': '🔴 Haute',
            'Trigramme': 'CNT',
            'Créé le': '2025-11-16',
        },
        'description': '''
### Contexte

This is the context of the task.

### Objectif

This is the objective of the task.
            ''',
        'tests': '''
- [ ] Verify X
- [ ] Verify Y
            ''',
        'subtasks': [
            (False, 'Subtask 1'),
            (False, 'Subtask 2'),
            (False, 'Subtask 3'),
        ],
        'subtasks_completed': 0,
        'subtasks_total': 3,
        'notes_claude': None,
        'notes_user': None,
    }


@pytest.fixture
def sample_task_data_incomplete():
    """Incomplete task data for testing."""
    return {
        'metadata': {
            'ID': 'CNT-005',
            'Titre': 'Test Task',
            # Missing Statut
            'Priorité': '🔴 Haute',
            'Trigramme': 'CNT',
            # Missing Créé le
        },
        'description': 'Short description',  # Too short, no subsections
        'subtasks': [],  # No subtasks
        'subtasks_completed': 0,
        'subtasks_total': 0,
        'notes_claude': None,
        'notes_user': None,
    }


@pytest.fixture
def temp_task_file():
    """Create a temporary valid task file."""
    temp_dir = Path(tempfile.mkdtemp())
    task_file = temp_dir / "CNT-005-test-task.md"

    content = """# CNT-005: Test Task

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-005 |
| **Titre** | Test Task |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-11-16 |

---

## Description

This is a complete description with proper subsections.

### Contexte

This is the context of the task explaining why it needs to be done and providing sufficient background information.

### Objectif

This is the objective explaining what the expected result is and what we want to achieve.

---

## Sous-tâches

- [ ] First subtask
- [ ] Second subtask
- [ ] Third subtask

---

## Tests / Vérifications

- [ ] Verify compilation works
- [ ] Verify PDF displays correctly
- [ ] Verify content is accurate

---
"""

    with open(task_file, 'w', encoding='utf-8') as f:
        f.write(content)

    yield task_file

    # Cleanup
    shutil.rmtree(temp_dir)


# ============================================================================
# Test ValidationIssue and Result
# ============================================================================

def test_validation_issue_creation():
    """Test creating ValidationIssue."""
    issue = ValidationIssue(
        severity='error',
        message='Test error',
        suggestion='Fix it'
    )

    assert issue.severity == 'error'
    assert issue.message == 'Test error'
    assert issue.suggestion == 'Fix it'


def test_validation_result_has_errors():
    """Test DorValidationResult error detection."""
    result = DorValidationResult(
        is_valid=False,
        task_id='CNT-005',
        issues=[
            ValidationIssue('error', 'Error 1'),
            ValidationIssue('warning', 'Warning 1'),
        ]
    )

    assert result.has_errors() is True
    assert result.has_warnings() is True


def test_validation_result_no_errors():
    """Test DorValidationResult with only warnings."""
    result = DorValidationResult(
        is_valid=True,
        task_id='CNT-005',
        issues=[
            ValidationIssue('warning', 'Warning 1'),
            ValidationIssue('warning', 'Warning 2'),
        ]
    )

    assert result.has_errors() is False
    assert result.has_warnings() is True


# ============================================================================
# Test Individual Validators
# ============================================================================

def test_validate_file_exists_success(temp_task_file):
    """Test file existence validation when file exists."""
    issue = validate_file_exists(temp_task_file)
    assert issue is None


def test_validate_file_exists_failure():
    """Test file existence validation when file doesn't exist."""
    issue = validate_file_exists(Path('/nonexistent/file.md'))

    assert issue is not None
    assert issue.severity == 'error'
    assert 'not found' in issue.message.lower()


def test_validate_status_valid(sample_task_data_valid):
    """Test status validation with valid status."""
    issue = validate_status(sample_task_data_valid)
    assert issue is None


def test_validate_status_blocked():
    """Test status validation with blocked status."""
    task_data = {
        'metadata': {'Statut': '🚫 Bloqué'}
    }
    issue = validate_status(task_data)
    assert issue is None  # Blocked is valid for starting


def test_validate_status_in_progress():
    """Test status validation when already in progress."""
    task_data = {
        'metadata': {'Statut': '🔄 En cours'}
    }
    issue = validate_status(task_data)

    assert issue is not None
    assert issue.severity == 'error'
    assert 'already in progress' in issue.message.lower()


def test_validate_status_completed():
    """Test status validation when completed."""
    task_data = {
        'metadata': {'Statut': '✅ Terminé'}
    }
    issue = validate_status(task_data)

    assert issue is not None
    assert issue.severity == 'error'
    assert 'completed' in issue.message.lower()


def test_validate_status_missing():
    """Test status validation when status missing."""
    task_data = {
        'metadata': {}
    }
    issue = validate_status(task_data)

    assert issue is not None
    assert issue.severity == 'error'
    assert 'not found' in issue.message.lower()


def test_validate_description_valid(sample_task_data_valid):
    """Test description validation with valid description."""
    issues = validate_description(sample_task_data_valid)
    assert len(issues) == 0


def test_validate_description_missing_context():
    """Test description validation missing context."""
    task_data = {
        'description': '''
### Objectif

Only objective, no context.
            '''
    }
    issues = validate_description(task_data)

    assert len(issues) > 0
    assert any('Contexte' in issue.message for issue in issues)


def test_validate_description_too_short():
    """Test description validation with short description."""
    task_data = {
        'description': 'Too short'
    }
    issues = validate_description(task_data)

    assert len(issues) > 0
    assert any('too short' in issue.message.lower() for issue in issues)


def test_validate_acceptance_criteria_valid(sample_task_data_valid):
    """Test acceptance criteria validation with valid criteria."""
    issue = validate_acceptance_criteria(sample_task_data_valid)
    assert issue is None


def test_validate_acceptance_criteria_missing():
    """Test acceptance criteria validation when missing."""
    task_data = {
        'tests': None
    }
    issue = validate_acceptance_criteria(task_data)

    assert issue is not None
    assert issue.severity == 'warning'  # Only warning
    assert 'criteria' in issue.message.lower()


def test_validate_subtasks_valid(sample_task_data_valid):
    """Test subtask validation with sufficient subtasks."""
    issue = validate_subtasks(sample_task_data_valid)
    assert issue is None


def test_validate_subtasks_insufficient():
    """Test subtask validation with too few subtasks."""
    task_data = {
        'subtasks': [(False, 'Only one')]
    }
    issue = validate_subtasks(task_data)

    assert issue is not None
    assert issue.severity == 'warning'  # Only warning
    assert 'subtasks' in issue.message.lower()


def test_validate_metadata_complete_valid(sample_task_data_valid):
    """Test metadata validation with complete metadata."""
    issues = validate_metadata_complete(sample_task_data_valid)
    assert len(issues) == 0


def test_validate_metadata_complete_missing_fields(sample_task_data_incomplete):
    """Test metadata validation with missing fields."""
    issues = validate_metadata_complete(sample_task_data_incomplete)

    assert len(issues) > 0
    assert all(issue.severity == 'error' for issue in issues)
    # Should detect missing Statut and Créé le
    assert len(issues) >= 2


# ============================================================================
# Test Full DoR Validation
# ============================================================================

def test_validate_dor_valid_task(temp_task_file):
    """Test full DoR validation with valid task."""
    result = validate_dor('CNT-005', task_file=temp_task_file)

    assert result.is_valid is True
    assert result.task_id == 'CNT-005'
    # May have warnings but no errors
    assert result.has_errors() is False


def test_validate_dor_file_not_found():
    """Test DoR validation when file doesn't exist."""
    result = validate_dor('CNT-999', task_file=Path('/nonexistent/file.md'))

    assert result.is_valid is False
    assert result.has_errors() is True
    assert any('not found' in issue.message.lower() for issue in result.issues)


def test_validate_dor_invalid_status(monkeypatch, temp_task_file):
    """Test DoR validation with invalid status."""
    # Create a task with invalid status
    temp_dir = temp_task_file.parent
    invalid_task = temp_dir / "CNT-006-invalid.md"

    content = """# CNT-006: Invalid Task

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-006 |
| **Titre** | Invalid Task |
| **Statut** | 🔄 En cours |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Créé le** | 2025-11-16 |

---

## Description

This is the description section with proper subsections.

### Contexte
Test context with enough information to explain the background.

### Objectif
Test objective with clear expected outcomes.

---

## Sous-tâches

- [ ] Task 1
- [ ] Task 2

---
"""

    with open(invalid_task, 'w', encoding='utf-8') as f:
        f.write(content)

    result = validate_dor('CNT-006', task_file=invalid_task)

    assert result.is_valid is False
    assert result.has_errors() is True
    assert any('in progress' in issue.message.lower() for issue in result.issues)


def test_validate_dor_with_warnings_only(temp_task_file, monkeypatch):
    """Test DoR validation with only warnings (should still be valid)."""
    # Create task with warnings but no errors
    temp_dir = temp_task_file.parent
    warning_task = temp_dir / "CNT-007-warnings.md"

    content = """# CNT-007: Task with Warnings

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-007 |
| **Titre** | Task with Warnings |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Créé le** | 2025-11-16 |

---

## Description

This task has only the objective section.

### Objectif
Only objective section, no context, but enough text to pass the length validation.

---

## Sous-tâches

- [ ] Only one subtask

---
"""

    with open(warning_task, 'w', encoding='utf-8') as f:
        f.write(content)

    result = validate_dor('CNT-007', task_file=warning_task)

    # Should be valid despite warnings
    assert result.is_valid is True
    assert result.has_errors() is False
    assert result.has_warnings() is True
