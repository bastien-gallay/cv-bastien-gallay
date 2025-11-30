"""Definition of Done (DoD) validator.

This module validates that a task meets all criteria to be marked as complete,
according to the rules defined in TASK_RULES.md.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

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
class DodValidationResult:
    """Result of DoD validation."""
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

def validate_status_for_completion(task_data: dict) -> Optional[ValidationIssue]:
    """Validate that task status allows completion.

    Args:
        task_data: Parsed task data

    Returns:
        ValidationIssue if status invalid, None otherwise
    """
    metadata = task_data.get('metadata', {})
    if 'Statut' not in metadata:
        return ValidationIssue(
            severity='error',
            message="Task status not found in file",
            suggestion="Ensure the task file has a valid 'Statut' field in metadata"
        )

    status = get_task_status(metadata)

    # Can only complete tasks that are "En cours"
    if status != '🔄 En cours':
        if status == '⏳ À faire':
            return ValidationIssue(
                severity='error',
                message=f"Task has not been started yet (status: {status})",
                suggestion="Start the task first with /task-start before completing it"
            )
        elif status == '✅ Terminé':
            return ValidationIssue(
                severity='error',
                message=f"Task is already completed (status: {status})",
                suggestion="Cannot complete an already completed task"
            )
        else:
            return ValidationIssue(
                severity='error',
                message=f"Invalid task status for completion: {status}",
                suggestion="Status must be '🔄 En cours' to complete the task"
            )

    return None


def validate_all_subtasks_completed(task_data: dict) -> Optional[ValidationIssue]:
    """Validate that all subtasks are checked.

    Args:
        task_data: Parsed task data

    Returns:
        ValidationIssue if subtasks incomplete, None otherwise
    """
    subtasks = task_data.get('subtasks', [])
    subtasks_completed = task_data.get('subtasks_completed', 0)
    subtasks_total = task_data.get('subtasks_total', 0)

    if subtasks_total == 0:
        return ValidationIssue(
            severity='warning',
            message="Task has no subtasks",
            suggestion="Consider adding subtasks to break down the work"
        )

    if subtasks_completed < subtasks_total:
        incomplete_count = subtasks_total - subtasks_completed
        return ValidationIssue(
            severity='error',
            message=f"{incomplete_count}/{subtasks_total} subtask(s) not completed",
            suggestion="Complete all subtasks before marking the task as done"
        )

    return None


def validate_result_section(task_data: dict) -> Optional[ValidationIssue]:
    """Validate that "Résultat final" section has content.

    Args:
        task_data: Parsed task data

    Returns:
        ValidationIssue if section missing/empty, None otherwise
    """
    # Note: parse_task_file doesn't extract "Résultat final" by default
    # This would need to be added to file_parser, but for now we'll make it a warning
    # The actual task-complete workflow will prompt for this content

    result_section = task_data.get('result', '')

    if not result_section or len(result_section.strip()) < 10:
        return ValidationIssue(
            severity='warning',
            message="'Résultat final' section is empty or too short",
            suggestion="Add a summary of what was accomplished in this task"
        )

    return None


# ============================================================================
# Main Validation
# ============================================================================

def validate_dod(task_id: str,
                task_file: Optional[Path] = None) -> DodValidationResult:
    """Validate that a task meets Definition of Done criteria.

    Args:
        task_id: Task ID (e.g., 'CNT-005')
        task_file: Optional explicit path to task file

    Returns:
        DodValidationResult with validation status and issues

    Examples:
        >>> result = validate_dod('CNT-005')
        >>> if result.is_valid:
        ...     print("Task is ready to complete!")
        >>> else:
        ...     for issue in result.issues:
        ...         print(f"{issue.severity}: {issue.message}")
    """
    from core.config_loader import load_paths

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
            return DodValidationResult(
                is_valid=False,
                task_id=task_id,
                issues=issues
            )

        task_file = matching_files[0]

    # 1. Validate file exists
    if not task_file.exists():
        issues.append(ValidationIssue(
            severity='error',
            message=f"Task file not found: {task_file}",
            suggestion="Check the task ID or file path"
        ))
        return DodValidationResult(
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
        return DodValidationResult(
            is_valid=False,
            task_id=task_id,
            issues=issues
        )

    # 3. Validate status
    status_issue = validate_status_for_completion(task_data)
    if status_issue:
        issues.append(status_issue)

    # 4. Validate all subtasks completed
    subtasks_issue = validate_all_subtasks_completed(task_data)
    if subtasks_issue:
        issues.append(subtasks_issue)

    # 5. Validate result section (warning only)
    result_issue = validate_result_section(task_data)
    if result_issue:
        issues.append(result_issue)

    # Determine if valid (no error-level issues)
    is_valid = not any(issue.severity == 'error' for issue in issues)

    return DodValidationResult(
        is_valid=is_valid,
        task_id=task_id,
        issues=issues
    )


# ============================================================================
# CLI for Testing
# ============================================================================

if __name__ == '__main__':
    """Test DoD validation."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python dod_validator.py <TASK-ID>")
        print("Example: python dod_validator.py CNT-005")
        sys.exit(1)

    task_id = sys.argv[1]

    print(f"Validating DoD for task: {task_id}")
    print("=" * 60)

    result = validate_dod(task_id)

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
        print("\n✅ Task meets all Definition of Done criteria!")

    print("\n" + "=" * 60)

    sys.exit(0 if result.is_valid else 1)
