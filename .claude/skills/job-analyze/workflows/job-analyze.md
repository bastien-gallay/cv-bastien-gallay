# Job Analyze Workflow

Analyse une offre d'emploi et génère un rapport structuré.

## Usage

```
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
```
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

Si l'entreprise est identifiée, utiliser WebSearch pour :
- Taille de l'entreprise
- Secteur d'activité
- Actualités récentes
- Culture d'entreprise

```python
# WebSearch query
f"{company} entreprise taille secteur avis"
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

```
Voulez-vous sauvegarder cette analyse ?
→ Sera stockée dans data/applications/{entreprise}-{date}/
```

## Output

- Rapport d'analyse formaté en markdown
- Fichier sauvegardé (si demandé)

## Exemples

**Depuis URL :**
```
> job-analyze https://www.linkedin.com/jobs/view/123456

🔍 Analyse de l'offre LinkedIn...
[Rapport généré]
```

**Depuis texte :**
```
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
