# Task Management Templates

This directory will contain reusable templates for task management workflows.

## Current Template Locations

Templates are currently located in the main project structure:

### Task Templates

- **Main task template:** `.tasks/tasks/TEMPLATE.md`
  - Used by task-create workflow
  - Contains all metadata fields
  - Includes standard sections (Description, Sous-tâches, etc.)

### Analysis Templates

Located in `.tasks/resources/templates/`:

- **source-extraction-template.md** - Guide for extracting data from external sources
- **audit-template.md** - Structure for comparative analysis
- **recommendations-template.md** - Format for analysis recommendations

## Future Migration

These templates may be moved to this directory in Session 4 (cleanup phase) to consolidate all skill-related files in one location.

## Usage in Workflows

Workflows reference templates using paths from `config/paths.yml`:

```python
from scripts.core import config_loader

paths = config_loader.load_paths()
template_file = Path(paths.task_template)  # Points to .tasks/tasks/TEMPLATE.md
```

This allows flexible template location without hardcoding paths in workflows.
