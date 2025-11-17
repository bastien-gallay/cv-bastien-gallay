# Task-From-Idea Workflow

Create a task from an idea in the backlog with pre-filled data.

## Usage

```
task-from-idea [--verbose]
```

## Workflow Steps

### 1. Load Ideas Backlog

Read IDEAS.md and parse ideas:

```python
from pathlib import Path
from scripts.core import config_loader

paths = config_loader.load_paths()
ideas_file = Path(paths.tasks_ideas)

if not ideas_file.exists():
    print("❌ IDEAS.md not found")
    exit(1)

content = ideas_file.read_text()
```

### 2. Parse and Display Ideas

Extract ideas from markdown list:

```python
import re

def parse_ideas(content):
    """Parse ideas from IDEAS.md."""
    ideas = []
    lines = content.split('\n')

    for i, line in enumerate(lines):
        # Match: - [ ] Idea title (source: task-id)
        match = re.match(r'- \[ \] (.+?)(?: \(source: ([A-Z]{3}-\d{3})\))?', line)
        if match:
            title = match.group(1).strip()
            source = match.group(2) if match.group(2) else None
            ideas.append({
                'title': title,
                'source': source,
                'line_num': i
            })

    return ideas

ideas = parse_ideas(content)

if not ideas:
    print("ℹ️  No ideas found in IDEAS.md")
    exit(0)
```

**Display ideas:**

```
=== Idées disponibles ===

1. Ajouter expérience Capgemini (source: CNT-005)
2. Documenter le processus de build
3. Créer un guide de contribution (source: DOC-001)
4. Optimiser les performances de compilation
5. Ajouter support multi-langues

Total: 5 idées

Sélectionner une idée (1-5 ou 'all'):
```

### 3. Select Ideas

Parse selection:

```python
def parse_selection(input_str, ideas):
    """Parse user selection."""
    if input_str == 'all':
        return ideas

    try:
        indices = [int(x.strip()) for x in input_str.split(',')]
        return [ideas[i-1] for i in indices if 0 < i <= len(ideas)]
    except (ValueError, IndexError):
        print("❌ Invalid selection")
        return []

selected = parse_selection(user_input, ideas)
```

### 4. Infer Task Data

For each selected idea, infer task metadata:

```python
def infer_task_data(idea):
    """Infer task data from idea."""
    title = idea['title']

    # Infer trigramme from keywords
    trigramme_keywords = {
        'CNT': ['ajouter', 'corriger', 'mettre à jour', 'expérience', 'certification'],
        'DOC': ['documenter', 'guide', 'readme', 'documentation'],
        'TPL': ['template', 'structure', 'layout'],
        'QUA': ['test', 'qualité', 'validation'],
        'PIP': ['build', 'ci/cd', 'automation', 'compilation'],
        'LAY': ['design', 'style', 'visuel', 'layout'],
        'INF': ['infrastructure', 'setup', 'configuration']
    }

    inferred_trigramme = 'CNT'  # Default
    title_lower = title.lower()
    for trig, keywords in trigramme_keywords.items():
        if any(kw in title_lower for kw in keywords):
            inferred_trigramme = trig
            break

    # Infer priority (default: medium)
    inferred_priority = '🟡 Moyenne'
    if any(kw in title_lower for kw in ['urgent', 'critique', 'important']):
        inferred_priority = '🔴 Haute'
    elif any(kw in title_lower for kw in ['optionnel', 'nice', 'futur']):
        inferred_priority = '🟢 Basse'

    return {
        'trigramme': inferred_trigramme,
        'title': title,
        'priority': inferred_priority,
        'origin': f"Idée depuis backlog (source: {idea['source']})" if idea['source'] else "Idée depuis backlog"
    }
```

### 5. Interactive Task Creation

Use task-create workflow with pre-filled values:

```python
from scripts.core import id_generator

for idea in selected:
    task_data = infer_task_data(idea)

    print(f"\n=== Création de tâche depuis idée ===")
    print(f"Titre: {idea['title']}")
    print(f"Source: {idea['source'] or 'Backlog général'}\n")

    # Interactive questionnaire with inferred defaults
    trigramme = input(f"Trigramme [{task_data['trigramme']}]: ") or task_data['trigramme']
    title = input(f"Titre [{task_data['title']}]: ") or task_data['title']
    priority = input(f"Priorité [{task_data['priority']}]: ") or task_data['priority']

    # Collect description
    print("\nDescription - Contexte:")
    context = input("> ")

    print("\nDescription - Objectif:")
    objective = input("> ")

    # Generate ID and create task
    task_id, filename = id_generator.create_unique_id_and_filename(trigramme, title)

    # Create task file from template
    # Add to dashboard
    # Confirm creation

    print(f"\n✅ Tâche {task_id} créée avec succès!")
```

### 6. Remove from Ideas Backlog

Mark idea as completed in IDEAS.md:

```python
def mark_idea_completed(ideas_file, idea):
    """Mark idea as completed in IDEAS.md."""
    content = ideas_file.read_text()
    lines = content.split('\n')

    # Find the idea line and mark as completed
    line_num = idea['line_num']
    lines[line_num] = lines[line_num].replace('- [ ]', '- [x]')

    # Add task ID reference
    if '(source:' not in lines[line_num]:
        lines[line_num] = lines[line_num].rstrip() + f" (créée: {task_id})"
    else:
        lines[line_num] = lines[line_num].rstrip() + f" (créée: {task_id})"

    ideas_file.write_text('\n'.join(lines))

mark_idea_completed(ideas_file, idea)
```

### 7. Git Commit

Commit the new task and updated IDEAS.md:

```python
from scripts.core import git_operations

git_operations.stage_files([
    f'.tasks/tasks/{filename}',
    '.tasks/TASKS.md',
    '.tasks/IDEAS.md'
])

message = git_operations.format_commit_message(
    commit_type='feat',
    scope='tasks',
    emoji='✨',
    description=f'create {task_id} from idea backlog',
    body=f"Transformed idea from backlog into concrete task.\n\nOriginal idea: {idea['title']}",
    task_ref=task_id
)

git_operations.create_commit(message)
```

### 8. Summary

Display completion summary:

```
✅ 2 tâches créées depuis le backlog!

- CNT-016: Ajouter expérience Capgemini
- DOC-003: Créer un guide de contribution

Les idées ont été marquées comme complétées dans IDEAS.md.
Utilisez /task-start pour commencer le travail.
```

## Scripts Used

- `scripts/core/id_generator.py` - Generate task IDs
- `scripts/core/file_parser.py` - Parse and update files
- `scripts/core/dashboard_updater.py` - Update TASKS.md
- `scripts/core/git_operations.py` - Git operations
- `scripts/core/config_loader.py` - Get paths

## Notes

- Smart trigramme inference from keywords
- Priority inference from context
- Interactive confirmation of inferred values
- Ideas marked as completed (checkbox + task reference)
- Full traceability: idea → task
- Batch creation supported
- Simple markdown parsing (no complex parser needed)
