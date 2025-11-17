# Analyze-Source Workflow

Extract and structure information from external sources for CV comparison.

## Usage

```
analyze-source [--task-id=CNT-XXX] [source-type] [source-info]
```

## Workflow Steps

### 1. Select Source Type

If not provided, present options:

```
Quel type de source souhaitez-vous analyser ?

1. LinkedIn Profile
2. GitHub Profile
3. CV Externe (PDF/Word)
4. Website/Blog
5. Autre

Choix (1-5):
```

### 2. Gather Source Information

**Collect:**

1. **URL or description** (required)
   - LinkedIn: Profile URL
   - GitHub: Username or URL
   - CV: Filename or description
   - Website: URL
   - Other: Description

2. **Parent task ID** (optional)
   - Link this analysis to an existing CNT task (audit/analysis)
   - If none exists, suggest creating one with task-create

```
ID de la tâche parent (optionnel, ex: CNT-001):
```

### 3. Create Analysis Directory

**Setup directory structure:**

```bash
.tasks/resources/audits/{TASK-ID}/
├── linkedin-profile.md      # If LinkedIn
├── github-profile.md        # If GitHub
├── external-cv.md           # If external CV
├── website-content.md       # If website
└── cv-snapshot.md           # Current CV state for comparison
```

**Directory naming:**
- If parent task provided: Use task ID (e.g., `CNT-001/`)
- If no parent: Generate temp ID or use source name

### 4. Guided Data Extraction

**Load appropriate template from:**

```
.tasks/resources/templates/source-extraction-template.md
```

**Templates available:**
- LinkedIn Profile Template
- GitHub Profile Template
- External CV Template
- Website/Blog Template
- Generic Template

**Interactive extraction process:**

```markdown
=== Section 1/10: Informations de profil ===

Veuillez copier-coller ou saisir les informations suivantes:

- Nom complet:
- Headline/Title:
- Localisation:
- Contact (si visible):

[Continuer] / [Passer] / [Annuler]
```

Repeat for each section:
- Profile information
- Current position
- Work experience
- Education
- Skills
- Certifications
- Languages
- Publications/Projects
- Recommendations/Endorsements
- Additional sections (source-specific)

### 5. Save Extracted Data

**Write to audit file:**

```python
from pathlib import Path

audit_dir = Path(f'.tasks/resources/audits/{task_id}')
audit_dir.mkdir(parents=True, exist_ok=True)

source_file_map = {
    'LinkedIn': 'linkedin-profile.md',
    'GitHub': 'github-profile.md',
    'CV External': 'external-cv.md',
    'Website': 'website-content.md',
    'Other': 'other-source.md'
}

output_file = audit_dir / source_file_map[source_type]
output_file.write_text(extracted_data, encoding='utf-8')
```

**Also save CV snapshot for comparison:**

```python
import subprocess

# Export current CV structure
cv_snapshot = audit_dir / 'cv-snapshot.md'

# Could extract from src/cv.typ or compile and extract from PDF
# For now, just create a marker
cv_snapshot.write_text(f"""# CV Snapshot - {date.today()}

Source: src/cv.typ
Exported for comparison with {source_type} analysis.

[Manual extraction or automated export to be added here]
""", encoding='utf-8')
```

### 6. Next Steps Guidance

Display completion message with next steps:

```
✅ Extraction terminée!

Fichier créé: .tasks/resources/audits/{task_id}/{source_file}.md

Prochaines étapes recommandées:

1. Créer une analyse comparative:
   - Créer .tasks/resources/analyses/{task_id}/audit-report.md
   - Comparer les données extraites avec le CV actuel
   - Identifier les écarts et incohérences

2. Documenter les recommandations:
   - Créer .tasks/resources/analyses/{task_id}/recommendations.md
   - Lister les modifications suggérées
   - Prioriser les recommandations

3. Créer le fichier de suivi:
   - Créer .tasks/resources/analyses/{task_id}/recommendations-status.md
   - Utiliser le template de tracking
   - Prêt pour /task-from-analysis

4. Mettre à jour ANALYSES.md:
   - Ajouter l'analyse au dashboard
   - Mettre à jour les statistiques

Consultez les templates dans .tasks/resources/templates/ pour ces fichiers.
```

## Templates

**Available in `.tasks/resources/templates/`:**

- `source-extraction-template.md` - Generic extraction guide
- `audit-template.md` - Comparative analysis structure
- `recommendations-template.md` - Recommendations format with priorities

## Scripts

No complex Python scripts needed - this is primarily an interactive data collection workflow.

**Optional helpers:**
- File creation and directory setup
- Template loading and substitution
- Validation of required fields

## Notes

- Focus on structured data extraction
- Maintain consistent format for comparison
- Templates ensure completeness
- Links to parent task for traceability
- Prepares data for comparative analysis
- Output ready for /task-from-analysis workflow
