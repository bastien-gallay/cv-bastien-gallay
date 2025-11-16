# Task-Complete Workflow

Finalize a task with DoD validation, final commit, and dashboard update.

## Usage

```
task-complete <TASK-ID>
```

## Workflow Steps

### 1. DoD Validation

Validate task meets Definition of Done:

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/validators/dod_validator.py <TASK-ID>
```

Checks:
- ✓ Status is "🔄 En cours"
- ✓ All subtasks are checked
- ✓ "Résultat final" section exists (warning)

If validation fails, display issues and abort.

### 2. CV Compilation Check

Compile CV to verify no errors:

```bash
typst compile src/cv.typ dist/cv.pdf
```

If compilation fails, abort with error message.

### 3. Collect Completion Data

Interactive prompts:
- "Résultat final" (summary of what was accomplished)
- "Temps réel" (actual time spent, optional)
- "Améliorations futures" (optional ideas for backlog)

### 4. Update Task File

Update task metadata:
- Status → "✅ Terminé"
- "Terminé le" → Current date
- "Temps réel" → User input (if provided)
- "Résultat final" section → User input
- Add entry to "Historique des modifications"

### 5. Final Commit

Create final commit:

```python
from scripts.core import git_operations

message = git_operations.format_commit_message(
    commit_type='feat',  # or 'fix', 'refactor', etc.
    scope='tasks',
    emoji='✅',
    description=f'complete {task_id}: {title}',
    body=result_summary,
    closes=task_id
)

git_operations.stage_files([task_file, 'dist/cv.pdf'])
git_operations.create_commit(message)
```

### 6. Dashboard Update

Move task to completed section:

```python
from scripts.core import dashboard_updater

dashboard_updater.move_task_to_completed(
    task_id=task_id,
    completed_date=completion_date
)
```

### 7. Branch Management

If on task branch (`task/XXX-NNN-*`):
- Offer to merge to main
- If yes: merge --no-ff
- Optionally delete branch

If on main: no action needed.

### 8. Backlog Ideas

If "Améliorations futures" provided:
- Append to `.tasks/IDEAS.md`
- Reference source task

### 9. Confirmation

Display summary:
```
✅ Tâche terminée avec succès!

ID: CNT-016
Titre: Example Task
Statut: ✅ Terminé
Temps réel: 2.5h
Commit: abc1234

La tâche a été déplacée vers "Tâches terminées" dans TASKS.md.
```

## Validation Stages

**Pre-flight (DoD):**
- Task status must be "🔄 En cours"
- All subtasks must be checked
- (Warning if "Résultat final" empty)

**Pre-commit:**
- CV must compile without errors
- At least one file changed
- "Résultat final" collected from user

**Post-commit:**
- Commit created successfully
- Dashboard updated correctly
- Branch merged (if applicable)

## Error Handling

**Validation Failed:**
- Display all DoD issues
- Suggest fixes
- Abort without changes

**Compilation Failed:**
- Display Typst errors
- Suggest fixing compilation
- Abort without commit

**No Changes:**
- Warn user if no files modified
- Require confirmation to proceed

**Git Conflicts:**
- Detect merge conflicts
- Guide user to resolve
- Abort automatic merge

## Scripts Used

- `scripts/validators/dod_validator.py` - Validate Definition of Done
- `scripts/core/git_operations.py` - Git branch/commit management
- `scripts/core/dashboard_updater.py` - Update TASKS.md
- `scripts/core/file_parser.py` - Read task file (Edit to update)

## Notes

- Always create final commit with `Closes XXX-NNN`
- PDF should be verified visually by user
- Branch merge is optional (user choice)
- Ideas automatically added to backlog
- Commit message follows conventional commits format
