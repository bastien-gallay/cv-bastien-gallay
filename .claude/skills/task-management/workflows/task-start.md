# Task-Start Workflow

Start working on a task with DoR validation and Git setup.

## Usage

```
task-start <TASK-ID> [--verbose]
```

## Workflow Steps

### 1. DoR Validation

Validate task meets Definition of Ready:

```python
from scripts.task_management.validators import dor_validator

result = dor_validator.validate_dor(task_id)

if not result.is_valid:
    print(f"❌ Cannot start task {task_id}:")
    for issue in result.issues:
        if issue.severity == 'error':
            print(f"  - {issue.message}")
            if issue.suggestion:
                print(f"    → {issue.suggestion}")
    exit(1)

# Display warnings (non-blocking)
for issue in result.issues:
    if issue.severity == 'warning':
        print(f"⚠️  {issue.message}")
```

**DoR checks:**
- ✓ File exists
- ✓ Status is "⏳ À faire" or "🚫 Bloqué"
- ✓ Description has Contexte + Objectif
- ✓ At least 2 subtasks defined
- ⚠ Warning if other tasks already "🔄 En cours"

### 2. Update Task File

Update status and history:

```python
from scripts.task_management.core import file_parser
from pathlib import Path
from datetime import date

task_file = Path(f'.tasks/tasks/{task_id}-*.md')  # Find file
content = task_file.read_text()

# Update status in metadata table
content = content.replace(
    '| **Statut** | ⏳ À faire |',
    '| **Statut** | 🔄 En cours |'
)
content = content.replace(
    '| **Statut** | 🚫 Bloqué |',
    '| **Statut** | 🔄 En cours |'
)

# Add history entry
history_entry = f"| {date.today()} | En cours | Début du travail |"
# Find "## Historique des modifications" section and append

task_file.write_text(content)
```

### 3. Update Dashboard

Update TASKS.md:

```python
from scripts.task_management.core import dashboard_updater

dashboard_updater.update_task_status(task_id, '🔄 En cours')
```

### 4. Create Git Branch (Conditional)

Check if branch needed from metadata field "Branche nécessaire":

```python
from scripts.task_management.core import git_operations

# Parse metadata to get branch requirement
branch_needed = metadata.get('Branche nécessaire', 'Auto')

# Decision logic
should_create_branch = (
    branch_needed == 'Oui' or
    (branch_needed == 'Auto' and is_significant_change(task))
)

if should_create_branch:
    # Generate slug from title
    from scripts.task_management.core.id_generator import slugify
    slug = slugify(task_title)

    # Create and checkout branch
    branch_name = git_operations.create_task_branch(task_id, slug)
    print(f"📌 Branche créée: {branch_name}")
else:
    print("ℹ️  Pas de branche créée (travail sur main)")
```

### 5. Initial Commit

Create startup commit:

```python
# Stage task file and TASKS.md
git_operations.stage_files([
    f'.tasks/tasks/{task_id}-{slug}.md',
    '.tasks/TASKS.md'
])

# Create commit
message = git_operations.format_commit_message(
    commit_type='chore',
    scope='tasks',
    emoji='🔧',
    description=f'start {task_id}: {title}',
    task_ref=task_id
)

commit_hash = git_operations.create_commit(message)
```

### 6. Confirmation

Display summary:

```
✅ Tâche démarrée avec succès!

ID: CNT-005
Titre: Ajouter certifications AWS
Statut: 🔄 En cours
Branche: task/CNT-005-ajouter-certifications-aws
Commit: a1b2c3d

Prochaines étapes:
1. Travailler sur les sous-tâches
2. Commiter régulièrement avec "Refs CNT-005"
3. Utiliser /task-complete pour finaliser
```

## Scripts Used

- `scripts/task_management/validators/dor_validator.py` - Validate Definition of Ready
- `scripts/task_management/core/file_parser.py` - Read task metadata (Edit to update)
- `scripts/task_management/core/dashboard_updater.py` - Update TASKS.md
- `scripts/task_management/core/git_operations.py` - Git branch and commit operations
- `scripts/task_management/core/id_generator.py` - Slugify for branch names

## Notes

- DoR validation is blocking - must pass to start
- Warnings are displayed but don't block
- Branch creation is smart (Auto mode)
- All changes committed in single startup commit
- Task file includes history tracking
