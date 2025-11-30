"""Definition of Ready (DoR) validator.

This module validates that a task meets all criteria to be started,
according to the rules defined in TASK_RULES.md.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from scripts.task_management.core.config_loader import load_paths
from scripts.task_management.core.file_parser import get_task_status, parse_task_file


# ============================================================================
# Validation Result Types
# ============================================================================

@dataclass
class ValidationIssue:
    """Single validation issue."""
    severity: str  # 'error', 'warning'
    message: str
    suggestion: Optional[str] = None


@dataclass
class DorValidationResult:
    """Result of DoR validation."""
    is_valid: bool
    task_id: str
    issues: List[ValidationIssue]

    def has_errors(self) -> bool:
        """Check if there are any error-level issues."""
        return any(issue.severity == 'error' for issue in self.issues)

    def has_warnings(self) -> bool:
        """Check if there are any warning-level issues."""
        return any(issue.severity == 'warning' for issue in self.issues)


# ============================================================================
# Validation Functions
# ============================================================================

def validate_file_exists(task_file: Path) -> Optional[ValidationIssue]:
    """Validate that task file exists.

    Args:
        task_file: Path to task file

    Returns:
        ValidationIssue if file doesn't exist, None otherwise
    """
    if not task_file.exists():
        return ValidationIssue(
            severity='error',
            message=f"Task file not found: {task_file}",
            suggestion="Check the task ID or create the task first with /task-create"
        )
    return None


def validate_status(task_data: dict) -> Optional[ValidationIssue]:
    """Validate that task status is ready to start.

    Args:
        task_data: Parsed task data from file_parser

    Returns:
        ValidationIssue if status is invalid, None otherwise
    """
    metadata = task_data.get('metadata', {})
    if 'Statut' not in metadata:
        return ValidationIssue(
            severity='error',
            message="Task status not found in file",
            suggestion="Ensure the task file has a valid 'Statut' field in metadata"
        )

    status = get_task_status(metadata)

    # Allow starting tasks that are "À faire" or "Bloqué" (unblocking)
    valid_statuses = ['⏳ À faire', '🚫 Bloqué']

    if status not in valid_statuses:
        if status == '🔄 En cours':
            return ValidationIssue(
                severity='error',
                message=f"Task is already in progress (status: {status})",
                suggestion="Complete the task first with /task-complete or change status back to '⏳ À faire'"
            )
        elif status == '✅ Terminé':
            return ValidationIssue(
                severity='error',
                message=f"Task is already completed (status: {status})",
                suggestion="Cannot restart a completed task"
            )
        else:
            return ValidationIssue(
                severity='error',
                message=f"Invalid task status: {status}",
                suggestion=f"Status must be one of: {', '.join(valid_statuses)}"
            )

    return None


def validate_description(task_data: dict) -> List[ValidationIssue]:
    """Validate that description has required sections.

    Args:
        task_data: Parsed task data

    Returns:
        List of ValidationIssue objects (may be empty)
    """
    issues = []

    description = task_data.get('description', '')

    if not description or len(description.strip()) < 20:
        issues.append(ValidationIssue(
            severity='error',
            message="Description section is missing or too short",
            suggestion="Add a clear description with 'Contexte' and 'Objectif' sections"
        ))
        return issues

    # Check for required subsections
    has_context = 'contexte' in description.lower()
    has_objective = 'objectif' in description.lower()

    if not has_context:
        issues.append(ValidationIssue(
            severity='warning',
            message="Description missing 'Contexte' subsection",
            suggestion="Add a '### Contexte' section explaining the background"
        ))

    if not has_objective:
        issues.append(ValidationIssue(
            severity='warning',
            message="Description missing 'Objectif' subsection",
            suggestion="Add a '### Objectif' section explaining the goal"
        ))

    return issues


def validate_acceptance_criteria(task_data: dict) -> Optional[ValidationIssue]:
    """Validate that acceptance criteria exist.

    Args:
        task_data: Parsed task data

    Returns:
        ValidationIssue if criteria missing, None otherwise
    """
    # Note: parse_task_file doesn't extract Tests section by default
    # We could add it, but for now just check if it exists in content
    # For simplicity, this is just a warning, so we'll be lenient
    tests_section = task_data.get('tests', '')

    if not tests_section or len(tests_section.strip()) < 10:
        return ValidationIssue(
            severity='warning',
            message="Acceptance criteria not defined in 'Tests / Vérifications' section",
            suggestion="Add explicit test cases or verification steps"
        )

    return None


def validate_subtasks(task_data: dict) -> Optional[ValidationIssue]:
    """Validate that task has subtasks.

    Args:
        task_data: Parsed task data

    Returns:
        ValidationIssue if no subtasks, None otherwise (warning only)
    """
    subtasks = task_data.get('subtasks', [])

    if not subtasks or len(subtasks) < 2:
        return ValidationIssue(
            severity='warning',
            message=f"Task has few or no subtasks ({len(subtasks)} found)",
            suggestion="Add at least 2 subtasks to break down the work"
        )

    return None


def validate_metadata_complete(task_data: dict) -> List[ValidationIssue]:
    """Validate that required metadata fields are present.

    Args:
        task_data: Parsed task data

    Returns:
        List of ValidationIssue objects (may be empty)
    """
    issues = []
    metadata = task_data.get('metadata', {})

    required_fields = {
        'ID': 'Task ID',
        'Titre': 'Task title',
        'Statut': 'Task status',
        'Priorité': 'Priority level',
        'Trigramme': 'Category trigramme',
        'Créé le': 'Creation date',
    }

    for field, description in required_fields.items():
        if field not in metadata or not metadata[field]:
            issues.append(ValidationIssue(
                severity='error',
                message=f"Required metadata field missing: {description} ({field})",
                suggestion=f"Add '{field}' field to the metadata table"
            ))

    return issues


# ============================================================================
# Main Validation
# ============================================================================

def validate_dor(task_id: str,
                task_file: Optional[Path] = None,
                allow_blocked: bool = True) -> DorValidationResult:
    """Validate that a task meets Definition of Ready criteria.

    Args:
        task_id: Task ID (e.g., 'CNT-005')
        task_file: Optional explicit path to task file
        allow_blocked: Allow starting tasks with status '🚫 Bloqué'

    Returns:
        DorValidationResult with validation status and issues

    Examples:
        >>> result = validate_dor('CNT-005')
        >>> if result.is_valid:
        ...     print("Task is ready to start!")
        >>> else:
        ...     for issue in result.issues:
        ...         print(f"{issue.severity}: {issue.message}")
    """
    issues: List[ValidationIssue] = []

    # Determine task file path
    if task_file is None:
        paths = load_paths()
        tasks_dir = Path(paths.tasks_dir)

        # Find file matching ID
        matching_files = list(tasks_dir.glob(f'{task_id}-*.md'))

        if not matching_files:
            issues.append(ValidationIssue(
                severity='error',
                message=f"Task file not found for ID: {task_id}",
                suggestion=f"Check that a file exists in {tasks_dir} with pattern {task_id}-*.md"
            ))
            return DorValidationResult(
                is_valid=False,
                task_id=task_id,
                issues=issues
            )

        task_file = matching_files[0]

    # 1. Validate file exists
    file_issue = validate_file_exists(task_file)
    if file_issue:
        issues.append(file_issue)
        return DorValidationResult(
            is_valid=False,
            task_id=task_id,
            issues=issues
        )

    # 2. Parse task file
    try:
        task_data = parse_task_file(task_file)
    except Exception as e:
        issues.append(ValidationIssue(
            severity='error',
            message=f"Failed to parse task file: {str(e)}",
            suggestion="Check that the task file follows the correct template format"
        ))
        return DorValidationResult(
            is_valid=False,
            task_id=task_id,
            issues=issues
        )

    # 3. Validate status
    status_issue = validate_status(task_data)
    if status_issue:
        # Special handling for 🚫 Bloqué status
        if not allow_blocked and '🚫 Bloqué' in status_issue.message:
            issues.append(status_issue)
        elif '🚫 Bloqué' not in status_issue.message:
            issues.append(status_issue)

    # 4. Validate metadata completeness
    metadata_issues = validate_metadata_complete(task_data)
    issues.extend(metadata_issues)

    # 5. Validate description
    description_issues = validate_description(task_data)
    issues.extend(description_issues)

    # 6. Validate acceptance criteria (warning only)
    criteria_issue = validate_acceptance_criteria(task_data)
    if criteria_issue:
        issues.append(criteria_issue)

    # 7. Validate subtasks (warning only)
    subtask_issue = validate_subtasks(task_data)
    if subtask_issue:
        issues.append(subtask_issue)

    # Determine if valid (no error-level issues)
    is_valid = not any(issue.severity == 'error' for issue in issues)

    return DorValidationResult(
        is_valid=is_valid,
        task_id=task_id,
        issues=issues
    )


# ============================================================================
# CLI for Testing
# ============================================================================

if __name__ == '__main__':
    """Test DoR validation."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python dor_validator.py <TASK-ID>")
        print("Example: python dor_validator.py CNT-005")
        sys.exit(1)

    task_id = sys.argv[1]

    print(f"Validating DoR for task: {task_id}")
    print("=" * 60)

    result = validate_dor(task_id)

    print(f"\nTask ID: {result.task_id}")
    print(f"Valid: {'✅ Yes' if result.is_valid else '❌ No'}")
    print(f"\nIssues found: {len(result.issues)}")

    if result.issues:
        print("\nDetails:")
        for i, issue in enumerate(result.issues, 1):
            icon = "❌" if issue.severity == 'error' else "⚠️ "
            print(f"\n{i}. {icon} {issue.severity.upper()}")
            print(f"   {issue.message}")
            if issue.suggestion:
                print(f"   💡 {issue.suggestion}")
    else:
        print("\n✅ Task meets all Definition of Ready criteria!")

    print("\n" + "=" * 60)

    sys.exit(0 if result.is_valid else 1)
