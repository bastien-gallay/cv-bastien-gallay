"""Git operations for task management workflows.

This module provides functions to handle Git operations like creating branches,
committing changes, and checking repository status.
"""

import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple
import re

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from scripts.task_management.core.config_loader import load_paths


# ============================================================================
# Git Status Checks
# ============================================================================

def get_current_branch() -> str:
    """Get the current Git branch name.

    Returns:
        Branch name (e.g., 'main', 'task/CNT-005-test')

    Raises:
        subprocess.CalledProcessError: If git command fails
    """
    result = subprocess.run(
        ['git', 'branch', '--show-current'],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()


def is_on_task_branch(task_id: str) -> bool:
    """Check if currently on the task's branch.

    Args:
        task_id: Task ID (e.g., 'CNT-005')

    Returns:
        True if on task/XXX-NNN-* branch
    """
    current = get_current_branch()
    return current.startswith(f'task/{task_id}-')


def has_uncommitted_changes() -> bool:
    """Check if there are uncommitted changes in the repository.

    Returns:
        True if there are uncommitted changes
    """
    result = subprocess.run(
        ['git', 'status', '--porcelain'],
        capture_output=True,
        text=True,
        check=True
    )
    return bool(result.stdout.strip())


# ============================================================================
# Branch Operations
# ============================================================================

def create_task_branch(task_id: str, slug: str) -> str:
    """Create and checkout a new task branch.

    Args:
        task_id: Task ID (e.g., 'CNT-005')
        slug: URL-safe slug for branch name

    Returns:
        Branch name created

    Raises:
        RuntimeError: If branch already exists or creation fails
    """
    paths = load_paths()
    prefix = paths.git_branch_prefix  # 'task/'
    branch_name = f"{prefix}{task_id}-{slug}"

    # Check if branch already exists
    result = subprocess.run(
        ['git', 'branch', '--list', branch_name],
        capture_output=True,
        text=True
    )

    if result.stdout.strip():
        raise RuntimeError(f"Branch already exists: {branch_name}")

    # Create and checkout branch
    subprocess.run(
        ['git', 'checkout', '-b', branch_name],
        check=True,
        capture_output=True
    )

    return branch_name


def checkout_branch(branch_name: str) -> None:
    """Checkout an existing branch.

    Args:
        branch_name: Name of branch to checkout

    Raises:
        subprocess.CalledProcessError: If checkout fails
    """
    subprocess.run(
        ['git', 'checkout', branch_name],
        check=True,
        capture_output=True
    )


# ============================================================================
# Commit Operations
# ============================================================================

def stage_files(file_paths: list[str]) -> None:
    """Stage files for commit.

    Args:
        file_paths: List of file paths to stage

    Raises:
        subprocess.CalledProcessError: If git add fails
    """
    subprocess.run(
        ['git', 'add'] + file_paths,
        check=True,
        capture_output=True
    )


def create_commit(message: str, allow_empty: bool = False) -> str:
    """Create a commit with the given message.

    Args:
        message: Commit message
        allow_empty: Allow empty commits

    Returns:
        Commit hash

    Raises:
        subprocess.CalledProcessError: If commit fails
    """
    cmd = ['git', 'commit', '-m', message]
    if allow_empty:
        cmd.append('--allow-empty')

    subprocess.run(cmd, check=True, capture_output=True)

    # Get commit hash
    result = subprocess.run(
        ['git', 'rev-parse', 'HEAD'],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()


# ============================================================================
# Merge Operations
# ============================================================================

def merge_to_main(task_branch: str, squash: bool = False) -> None:
    """Merge task branch into main.

    Args:
        task_branch: Task branch name to merge
        squash: Use --squash merge

    Raises:
        subprocess.CalledProcessError: If merge fails
    """
    paths = load_paths()
    main_branch = paths.git_main_branch

    # Checkout main
    checkout_branch(main_branch)

    # Merge
    cmd = ['git', 'merge', task_branch]
    if squash:
        cmd.append('--squash')

    subprocess.run(cmd, check=True, capture_output=True)


def delete_branch(branch_name: str, force: bool = False) -> None:
    """Delete a Git branch.

    Args:
        branch_name: Branch to delete
        force: Force delete even if not merged

    Raises:
        subprocess.CalledProcessError: If delete fails
    """
    flag = '-D' if force else '-d'
    subprocess.run(
        ['git', 'branch', flag, branch_name],
        check=True,
        capture_output=True
    )


# ============================================================================
# Helper Functions
# ============================================================================

def get_branch_for_task(task_id: str) -> Optional[str]:
    """Find the branch name for a task.

    Args:
        task_id: Task ID

    Returns:
        Branch name if found, None otherwise
    """
    result = subprocess.run(
        ['git', 'branch', '--list', f'task/{task_id}-*'],
        capture_output=True,
        text=True
    )

    branches = [line.strip().lstrip('* ') for line in result.stdout.split('\n') if line.strip()]
    return branches[0] if branches else None


def format_commit_message(commit_type: str, scope: str, emoji: str,
                          description: str, body: Optional[str] = None,
                          task_ref: Optional[str] = None,
                          closes: Optional[str] = None) -> str:
    """Format a conventional commit message.

    Args:
        commit_type: Type (e.g., 'feat', 'fix', 'chore')
        scope: Scope (e.g., 'tasks', 'cv')
        emoji: Emoji for commit
        description: Short description
        body: Optional commit body
        task_ref: Optional task reference (e.g., 'CNT-005')
        closes: Optional task to close (e.g., 'CNT-005')

    Returns:
        Formatted commit message

    Example:
        >>> format_commit_message('chore', 'tasks', '🔧', 'start task', task_ref='CNT-005')
        'chore(tasks): 🔧 start task\\n\\nRefs CNT-005'
    """
    # First line
    message = f"{commit_type}({scope}): {emoji} {description}"

    # Add body
    if body:
        message += f"\n\n{body}"

    # Add task reference
    if task_ref:
        message += f"\n\nRefs {task_ref}"

    # Add closes reference
    if closes:
        message += f"\n\nCloses {closes}"

    # Add co-author (optional, can be configured)
    message += "\n\n🤖 Generated with [Claude Code](https://claude.com/claude-code)\n\nCo-Authored-By: Claude <noreply@anthropic.com>"

    return message


# ============================================================================
# CLI for Testing
# ============================================================================

if __name__ == '__main__':
    """Test Git operations."""
    print("Testing git_operations.py")
    print("=" * 60)

    print("\n1. Getting current branch...")
    try:
        branch = get_current_branch()
        print(f"   Current branch: {branch}")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n2. Checking for uncommitted changes...")
    has_changes = has_uncommitted_changes()
    print(f"   Uncommitted changes: {has_changes}")

    print("\n3. Testing commit message formatting...")
    msg = format_commit_message(
        'chore',
        'tasks',
        '🔧',
        'start CNT-005',
        task_ref='CNT-005'
    )
    print(f"   Message:\n{msg}")

    print("\n✅ Git operations working!")
    print("=" * 60)
