# Task-Create Workflow

Create a new task interactively with auto-generated ID and validation.

## Usage

```
task-create
```

## Workflow Steps

### 1. Interactive Questionnaire

Collect task information from user:
- Trigramme (CNT, TPL, QUA, PIP, LAY, DOC, INF)
- Title (max 80 characters)
- Priority (🔴 Haute, 🟡 Moyenne, 🟢 Basse)
- Description (Contexte + Objectif)
- Subtasks (minimum 2 recommended)
- Section CV (Experience / Education / Skills / Sidebar / General / N/A)
- Date cible (optional, YYYY-MM-DD)
- Temps estimé (optional, hours)

### 2. ID Generation

Execute ID generator:

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/core/id_generator.py generate <TRIGRAMME> "<TITLE>"
```

This automatically:
- Scans existing tasks
- Finds next available ID
- Generates URL-safe slug
- Verifies uniqueness

### 3. File Creation

Use the task template (`.tasks/tasks/TEMPLATE.md`):
- Replace placeholders with collected values
- Set status to "⏳ À faire"
- Add creation date
- Save as `TASKS/{ID}-{slug}.md`

### 4. Dashboard Update

Update TASKS.md using dashboard_updater:

```python
from scripts.core import dashboard_updater

dashboard_updater.add_task_to_dashboard(
    task_id=task_id,
    title=title,
    status='⏳ À faire',
    priority=priority,
    created_date=created_date,
    filename=filename
)
```

This automatically:
- Inserts task in correct position (priority + date)
- Updates statistics
- Maintains table formatting

### 5. Confirmation

Display summary:
```
✅ Tâche créée avec succès!

ID: CNT-016
Titre: Example Task
Fichier: .tasks/tasks/CNT-016-example-task.md
Statut: ⏳ À faire
Priorité: 🔴 Haute

La tâche a été ajoutée à TASKS.md.
Utilisez `/task-start CNT-016` pour commencer.
```

## Validation

The workflow validates:
- ✓ Trigramme is valid
- ✓ ID is unique
- ✓ Title is not empty
- ✓ At least 2 subtasks (warning if not)
- ✓ Description has Contexte + Objectif
- ✓ File doesn't already exist

## Error Handling

**ID Collision:**
- Automatically increments to next available ID
- Displays warning to user

**Invalid Input:**
- Re-prompts for correction
- Provides helpful error messages

**File Exists:**
- Prevents overwriting
- Suggests alternative ID

## Scripts Used

- `scripts/core/id_generator.py` - Generate unique ID and filename
- `scripts/core/dashboard_updater.py` - Update TASKS.md
- `scripts/validators/dor_validator.py` - Validate task is ready (not used in create, but available)

## Notes

- No Git branch created during task creation
- Task must be started with `/task-start` before work begins
- ID format: XXX-NNN (trigramme + 3-digit number)
- Slug format: lowercase-hyphen-separated (max 60 chars)
