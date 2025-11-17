# Task-Archive Workflow

Archive a completed task to the archives directory.

## Usage

```
task-archive <TASK-ID>
```

## Workflow Steps

### 1. Validate Task is Completed

Check that task can be archived:

```python
from scripts.core import file_parser
from pathlib import Path

task_file = Path(f'.tasks/tasks/{task_id}-*.md')

if not task_file.exists():
    print(f"❌ Task file not found: {task_id}")
    exit(1)

task_data = file_parser.parse_task_file(task_file)
status = file_parser.get_task_status(task_data['metadata'])

if status != '✅ Terminé':
    print(f"❌ Cannot archive task with status: {status}")
    print("   Only completed tasks (✅ Terminé) can be archived")
    exit(1)
```

### 2. Move File to Archives

Move task file to archived directory:

```python
from scripts.core import config_loader
from datetime import date

paths = config_loader.load_paths()
archived_dir = Path(paths.archived_dir)

# Create year subdirectory
year = date.today().year
year_dir = archived_dir / str(year)
year_dir.mkdir(parents=True, exist_ok=True)

# Move file
dest = year_dir / task_file.name
task_file.rename(dest)

print(f"📦 Fichier déplacé: {dest}")
```

### 3. Remove from Dashboard

Remove from TASKS.md completed section:

```python
from scripts.core import dashboard_updater

dashboard_updater.remove_task_from_dashboard(task_id)

# Or update with archived status
dashboard_updater.update_task_status(task_id, '📦 Archivé')
```

### 4. Update Archive Index (Optional)

Add entry to archive index file:

```python
archive_index = archived_dir / 'ARCHIVES.md'

entry = f"""
## {task_id} - {title}

- **Archivé le:** {date.today()}
- **Priorité:** {priority}
- **Trigramme:** {trigramme}
- **Temps réel:** {actual_time}
- **Fichier:** [{year}/{task_file.name}]({year}/{task_file.name})

---
"""

# Append or prepend to archive index
if archive_index.exists():
    content = archive_index.read_text()
    archive_index.write_text(entry + content)
else:
    archive_index.write_text(f"# Tâches Archivées\n\n{entry}")
```

### 5. Git Commit

Commit the archival:

```python
from scripts.core import git_operations

git_operations.stage_files([
    str(dest),
    '.tasks/TASKS.md',
    str(archive_index)
])

# Note: Original file is moved, Git will detect as rename
git_operations.stage_files([str(task_file)])  # Stage deletion

message = git_operations.format_commit_message(
    commit_type='chore',
    scope='tasks',
    emoji='📦',
    description=f'archive {task_id}: {title}',
    task_ref=task_id
)

git_operations.create_commit(message)
```

### 6. Confirmation

Display summary:

```
✅ Tâche archivée avec succès!

ID: CNT-003
Titre: Mettre à jour expérience
Archive: .tasks/.archived/2025/CNT-003-mettre-a-jour-experience.md
Commit: abc1234

La tâche a été retirée du dashboard actif.
```

## Scripts Used

- `scripts/core/file_parser.py` - Validate task status
- `scripts/core/config_loader.py` - Get archive paths
- `scripts/core/dashboard_updater.py` - Remove from dashboard
- `scripts/core/git_operations.py` - Commit archival

## Notes

- Only completed tasks can be archived
- Files organized by year in archive
- Archive index maintains searchable history
- Git tracks move as rename (preserves history)
- Dashboard automatically updated
- Can be reversed by moving file back
