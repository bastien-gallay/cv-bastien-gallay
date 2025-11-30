# Job Analyze Workflow

Analyse une offre d'emploi et génère un rapport structuré.

## Usage

```bash
job-analyze [URL ou texte]
```

## Input

L'utilisateur fournit :

- **URL** : Lien vers l'offre (LinkedIn, WTTJ, Indeed, etc.)
- **Texte** : Contenu copié-collé de l'offre
- **Rien** : Demander à l'utilisateur de coller le texte

## Workflow Steps

### 1. Récupérer le contenu

**Si URL fournie :**

```python
# Utiliser WebFetch pour récupérer le contenu
content = WebFetch(url, prompt="Extract the full job posting text")
```

**Si texte fourni :**

```python
content = user_input
```

**Si rien fourni :**

```text
Veuillez coller le texte de l'offre d'emploi ci-dessous :
```

### 2. Parser l'offre

Exécuter le parser Python :

```bash
uv run python -c "
from scripts.job_analyze import parse_job_posting, generate_report
import sys

text = '''
[CONTENU DE L'OFFRE]
'''

job = parse_job_posting(text)
print(generate_report(job))
"
```

### 3. Enrichir avec recherche entreprise (optionnel)

Si l'entreprise est identifiée, utiliser le module `company_research` pour générer les prompts :

```python
from scripts.job_analyze import create_company_research_prompt

# Créer les prompts de recherche
research = create_company_research_prompt(
    company="HANDIPULSE",
    sector="EdTech"  # optionnel
)

# Requêtes WebSearch suggérées :
# - "HANDIPULSE entreprise taille employés"
# - "HANDIPULSE avis salariés Glassdoor"
# - "HANDIPULSE actualités levée de fonds"
# - "HANDIPULSE EdTech innovation"
```

Utiliser WebSearch avec ces requêtes, puis analyser les résultats avec `research.analysis_prompt`.

Le module fournit aussi `format_company_section()` pour formater les résultats :

```python
from scripts.job_analyze import format_company_section

company_md = format_company_section(
    company="HANDIPULSE",
    sector="EdTech / AccessTech",
    size="10-20 employés",
    funding="En recherche de levée de fonds",
    highlights=["Mission sociale forte", "Technologie CNRS"],
    concerns=["Startup early-stage", "Équipe technique à construire"],
)
```

### 4. Générer le rapport final

Combiner les informations dans le format suivant :

```markdown
# Analyse : {Titre} @ {Entreprise}

## Informations générales
- **Poste**: ...
- **Entreprise**: ...
- **Localisation**: ...
- **Type de contrat**: ...
- **Salaire**: ... (si mentionné)

## Exigences

### Obligatoires (must-have)
- [ ] Compétence 1
- [ ] Compétence 2

### Souhaitées (nice-to-have)
- [ ] Compétence 3

## Responsabilités principales
1. ...
2. ...

## Mots-clés ATS
`keyword1`, `keyword2`, `keyword3`

## Contexte entreprise
- **Secteur**: ...
- **Taille**: ...
- **Actualités**: ...

## Points d'attention
- ⚠️ Red flag potentiel: ...
- ✅ Point positif: ...

## Recommandations
- Mettre en avant: ...
- Préparer: ...
```

### 5. Sauvegarder (optionnel)

Proposer de sauvegarder l'analyse :

```text
Voulez-vous sauvegarder cette analyse ?
→ Sera stockée dans data/applications/{entreprise}-{date}/
```

## Output

- Rapport d'analyse formaté en markdown
- Fichier sauvegardé (si demandé)

## Exemples

**Depuis URL :**

```text
> job-analyze https://www.linkedin.com/jobs/view/123456

🔍 Analyse de l'offre LinkedIn...
[Rapport généré]
```

**Depuis texte :**

```text
> job-analyze

Collez le texte de l'offre :
> [utilisateur colle le texte]

🔍 Analyse en cours...
[Rapport généré]
```

## Notes

- Le parser supporte les offres en français et anglais
- Les mots-clés ATS sont extraits automatiquement
- L'enrichissement entreprise est optionnel
- Les analyses peuvent être chaînées avec `/job-fit` (INF-010)
