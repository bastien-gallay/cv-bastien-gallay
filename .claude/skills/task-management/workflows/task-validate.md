# Task-Validate Workflow

Validate task system consistency and integrity.

## Usage

```
task-validate [--fix] [--verbose]
```

## Workflow Steps

### 1. Validate File Structure

Check directory structure exists:

```python
from scripts.core import config_loader
from pathlib import Path

paths = config_loader.load_paths()

required_dirs = [
    paths.tasks_dir,
    paths.archived_dir,
    paths.analyses_dir,
    paths.audits_dir,
    paths.templates_dir
]

for dir_path in required_dirs:
    if not Path(dir_path).exists():
        print(f"❌ Missing directory: {dir_path}")
        if args.fix:
            Path(dir_path).mkdir(parents=True)
            print(f"   ✅ Created")
```

### 2. Validate Task Files

Check all task files are well-formed:

```python
from scripts.core import file_parser
from pathlib import Path

tasks_dir = Path(paths.tasks_dir)
issues = []

for task_file in tasks_dir.glob('*.md'):
    if task_file.name == 'TEMPLATE.md':
        continue

    try:
        task_data = file_parser.parse_task_file(task_file)

        # Validate required fields
        if 'ID' not in task_data['metadata']:
            issues.append(f"{task_file.name}: Missing ID in metadata")

        if 'Statut' not in task_data['metadata']:
            issues.append(f"{task_file.name}: Missing Statut in metadata")

        # Validate ID matches filename
        file_id = task_file.stem.split('-')[0] + '-' + task_file.stem.split('-')[1]
        meta_id = task_data['metadata'].get('ID', '')
        if file_id != meta_id:
            issues.append(f"{task_file.name}: ID mismatch (file: {file_id}, meta: {meta_id})")

    except Exception as e:
        issues.append(f"{task_file.name}: Parse error - {e}")

if issues:
    print(f"❌ Found {len(issues)} task file issues:")
    for issue in issues:
        print(f"   - {issue}")
else:
    print(f"✅ All {len(list(tasks_dir.glob('*.md')))-1} task files valid")
```

### 3. Validate Dashboard Consistency

Check TASKS.md matches actual task files:

```python
from scripts.core import dashboard_updater

content, sections = dashboard_updater.read_dashboard()

# Extract task IDs from active section
dashboard_ids = set()
for row in sections['active']:
    match = re.search(r'\[([A-Z]{3}-\d{3})\]', row)
    if match:
        dashboard_ids.add(match.group(1))

# Extract task IDs from files
file_ids = set()
for task_file in tasks_dir.glob('*.md'):
    if task_file.name == 'TEMPLATE.md':
        continue
    task_data = file_parser.parse_task_file(task_file)
    file_id = task_data['metadata'].get('ID')
    if file_id and task_data['metadata'].get('Statut') != '✅ Terminé':
        file_ids.add(file_id)

# Find discrepancies
missing_from_dashboard = file_ids - dashboard_ids
missing_from_files = dashboard_ids - file_ids

if missing_from_dashboard:
    print(f"⚠️  {len(missing_from_dashboard)} tasks not in dashboard:")
    for task_id in missing_from_dashboard:
        print(f"   - {task_id}")
        if args.fix:
            # Add to dashboard
            pass

if missing_from_files:
    print(f"⚠️  {len(missing_from_files)} dashboard entries without files:")
    for task_id in missing_from_files:
        print(f"   - {task_id}")
```

### 4. Validate ID Uniqueness

Check for duplicate IDs:

```python
from scripts.core import id_generator

existing_ids = id_generator.find_existing_ids()

duplicates = {}
for trigramme, numbers in existing_ids.items():
    seen = set()
    for num in numbers:
        if num in seen:
            task_id = f"{trigramme}-{num:03d}"
            duplicates[task_id] = duplicates.get(task_id, 0) + 1
        seen.add(num)

if duplicates:
    print(f"❌ Found duplicate IDs:")
    for task_id, count in duplicates.items():
        print(f"   - {task_id} ({count} occurrences)")
else:
    print("✅ All task IDs unique")
```

### 5. Validate Trigrammes

Check all trigrammes are valid:

```python
from scripts.core import config_loader

trigrammes_dict, trigrammes_config = config_loader.load_trigrammes()
valid_trigrammes = set(trigrammes_dict.keys())

for task_file in tasks_dir.glob('*.md'):
    if task_file.name == 'TEMPLATE.md':
        continue

    task_id = task_file.stem.split('-')[0]
    if task_id not in valid_trigrammes:
        print(f"⚠️  Invalid trigramme: {task_id} in {task_file.name}")
```

### 6. Validate Recommendations Tracking

Check recommendation status files are consistent:

```python
from scripts.analysis import recommendation_parser

analyses_dir = Path(paths.analyses_dir)

for analysis_dir in analyses_dir.iterdir():
    if not analysis_dir.is_dir():
        continue

    rec_file = analysis_dir / 'recommendations-status.md'
    if not rec_file.exists():
        continue

    analysis_id = analysis_dir.name
    recs = recommendation_parser.parse_recommendations_file(rec_file, analysis_id)

    # Check tasks referenced actually exist
    for rec in recs:
        if rec.task_created and rec.task_created != '-':
            # Extract task ID from link
            match = re.search(r'\[([A-Z]{3}-\d{3})\]', rec.task_created)
            if match:
                task_id = match.group(1)
                task_file = tasks_dir / f"{task_id}*.md"
                if not list(tasks_dir.glob(f"{task_id}*.md")):
                    print(f"⚠️  {analysis_id}-{rec.rec_id}: References non-existent task {task_id}")
```

### 7. Summary Report

Display validation summary:

```
=== Task System Validation Report ===

✅ Directory structure: OK
✅ Task files: 14 files validated
✅ Dashboard consistency: OK
✅ ID uniqueness: OK
✅ Trigrammes: OK
⚠️  Recommendations: 2 warnings

Issues found: 2 warnings, 0 errors

Use --fix to automatically resolve fixable issues.
```

## Scripts Used

- `scripts/task_management/core/file_parser.py` - Parse and validate task files
- `scripts/task_management/core/id_generator.py` - Check ID uniqueness
- `scripts/task_management/core/dashboard_updater.py` - Validate dashboard
- `scripts/task_management/core/config_loader.py` - Load trigrammes
- `scripts/task_management/analysis/recommendation_parser.py` - Validate recommendation tracking

## Notes

- Non-destructive by default
- `--fix` flag auto-repairs safe issues
- Checks file-dashboard consistency
- Validates recommendation traceability
- Reports both errors (blocking) and warnings
- Can be run anytime to check system health
