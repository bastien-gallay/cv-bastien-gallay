# Task-From-Analysis Workflow

Create tasks from analysis recommendations with full traceability.

## Usage

```
task-from-analysis [--analysis-id=XXX-NNN] [--filter=high|medium|low|all]
```

## Workflow Steps

### 1. Select Analysis

**Find analyses with pending recommendations:**

```python
from scripts.analysis import recommendation_parser
from scripts.core import file_parser

# Scan .tasks/resources/analyses/ for recommendation files
analyses = []
for analysis_dir in Path('.tasks/resources/analyses').iterdir():
    rec_file = analysis_dir / 'recommendations-status.md'
    if rec_file.exists():
        analysis_id = analysis_dir.name  # e.g., 'CNT-001'
        recs = recommendation_parser.parse_recommendations_file(rec_file, analysis_id)
        pending = recommendation_parser.find_pending_recommendations(recs)
        if pending:
            analyses.append({
                'id': analysis_id,
                'total': len(recs),
                'pending': len(pending),
                'file': rec_file
            })
```

**If `--analysis-id` not provided, show interactive selection:**

```
Analyses disponibles avec recommandations pendantes:

1. CNT-001 - LinkedIn Audit
   - Total: 19 recommandations
   - Pending: 15 (1 très haute, 8 hautes, 4 moyennes, 2 basses)

2. CNT-002 - GitHub Profile Analysis
   - Total: 8 recommandations
   - Pending: 5 (3 hautes, 2 moyennes)

Sélectionner une analyse (1-N ou ID):
```

### 2. Load and Display Recommendations

**Parse recommendations file:**

```python
rec_file = Path(f'.tasks/resources/analyses/{analysis_id}/recommendations-status.md')
all_recs = recommendation_parser.parse_recommendations_file(rec_file, analysis_id)
pending = recommendation_parser.find_pending_recommendations(all_recs)
```

**Apply priority filter (if provided):**

```python
if filter_arg:
    pending = recommendation_parser.filter_by_priority(pending, filter_arg)
```

**Group and display:**

```python
groups = recommendation_parser.group_by_priority(pending)

print(f"=== Recommandations pour {analysis_id} ===\n")

for emoji in ['🔴🔴', '🔴', '🟡', '🟢']:
    recs = groups[emoji]
    if not recs:
        continue

    priority_name = {
        '🔴🔴': 'TRÈS HAUTE',
        '🔴': 'HAUTE',
        '🟡': 'MOYENNE',
        '🟢': 'BASSE'
    }[emoji]

    print(f"\n{emoji} {priority_name} ({len(recs)} recommandations)")
    for i, rec in enumerate(recs, 1):
        print(f"  {i}. [{rec.rec_id}] {rec.title}")
        if rec.cv_reference:
            print(f"     - {rec.cv_reference}")
```

### 3. Select Recommendations

**Interactive selection with multiple modes:**

```
Sélection des recommandations à transformer en tâches:

Modes disponibles:
- Numéros: '1,5,6' ou '1-3,5' pour sélectionner spécifiquement
- 'all': Toutes les recommandations
- 'high': Priorité très haute + haute (🔴🔴 + 🔴)
- 'critical': Priorité très haute uniquement (🔴🔴)
- 'medium': Priorité moyenne (🟡)
- 'low': Priorité basse (🟢)

Votre sélection:
```

**Parse selection and confirm:**

```python
def parse_selection(input_str, recommendations):
    """Parse selection input (numbers, ranges, keywords)."""
    if input_str == 'all':
        return recommendations
    if input_str in ['critical', 'high', 'medium', 'low']:
        return recommendation_parser.filter_by_priority(recommendations, input_str)

    # Parse numbers and ranges (e.g., '1,3-5,8')
    selected = []
    for part in input_str.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            selected.extend(range(start, end + 1))
        else:
            selected.append(int(part))

    return [recommendations[i-1] for i in selected if 0 < i <= len(recommendations)]
```

### 4. Create Tasks

For each selected recommendation, pre-fill task creation using existing workflows:

**4.1 Extract Data from Recommendation:**

```python
def prepare_task_data(rec: Recommendation):
    """Prepare data for task creation from recommendation."""
    # Map priority
    priority_map = {
        '🔴🔴': '🔴 Haute',
        '🔴': '🔴 Haute',
        '🟡': '🟡 Moyenne',
        '🟢': '🟢 Basse'
    }

    return {
        'trigramme': rec.trigramme or 'CNT',
        'title': rec.title,
        'priority': priority_map[rec.priority_emoji],
        'category': rec.category,
        'cv_reference': rec.cv_reference,
        'origin': f"Recommandation [{rec.full_id}](../resources/analyses/{rec.analysis_id}/recommendations-status.md#{rec.rec_id.lower()})",
        'source_analysis': rec.analysis_id
    }
```

**4.2 Interactive Task Creation:**

Use the task-create workflow with pre-filled values:

```python
from scripts.core import id_generator

task_data = prepare_task_data(rec)

# Interactive questionnaire with defaults
trigramme = input(f"Trigramme [{task_data['trigramme']}]: ") or task_data['trigramme']
title = input(f"Titre [{task_data['title']}]: ") or task_data['title']
priority = input(f"Priorité [{task_data['priority']}]: ") or task_data['priority']

# Generate ID and filename
task_id, filename = id_generator.create_unique_id_and_filename(trigramme, title)

# Create task file from template with origin field populated
# Add dashboard entry
# Confirm creation
```

### 5. Update Recommendation Status

After each task creation, update the recommendations-status.md file:

```python
recommendation_parser.update_recommendation_status(
    file_path=rec_file,
    rec_id=rec.rec_id,
    task_id=task_id,
    task_filename=filename
)
```

This marks the recommendation as completed (`[x]`), adds task link, and changes status to `✅ Task Created`.

### 6. Summary

Display creation summary:

```
✅ 3 tâches créées avec succès!

- CNT-016 → R01: Corriger l'écart critique sur Upwiser
- CNT-017 → R05: Ajouter certifications manquantes
- CNT-018 → R12: Ajouter langue Espagnol

Fichier de suivi mis à jour: .tasks/resources/analyses/CNT-001/recommendations-status.md
```

## Scripts Used

- `scripts/task_management/analysis/recommendation_parser.py` - Parse and update recommendations
- `scripts/task_management/core/id_generator.py` - Generate task IDs
- `scripts/task_management/core/file_parser.py` - Parse task files
- `scripts/task_management/core/dashboard_updater.py` - Update TASKS.md

## Notes

- Full traceability: recommendation → task → CV change
- Recommendations file automatically updated
- Task files include origin reference
- Interactive mode allows customization of pre-filled data
- Batch creation supported for efficiency
