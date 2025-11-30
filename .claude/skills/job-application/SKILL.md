---
name: job-application
description: Analyse d'offres d'emploi, adéquation profil-poste, et génération de CV/lettre adaptés. Activer ce skill quand l'utilisateur parle de candidature, offre d'emploi, lettre de motivation, ou CV adapté.
version: 1.0.0
commands:
  - job-analyze
  - job-fit
  - job-cv
  - job-letter
---

# Job Application Skill

Système d'assistance au processus de candidature : analyse d'offres, évaluation de l'adéquation, génération de CV et lettres adaptés.

## Available Commands

### job-analyze

Analyse une offre d'emploi et extrait les informations structurées.

```bash
job-analyze [URL ou texte de l'offre]
```

**Fonctionnalités:**

- Parse l'offre depuis URL (LinkedIn, WTTJ, Indeed) ou texte
- Extrait exigences obligatoires vs souhaitées
- Identifie les mots-clés ATS
- Recherche des informations entreprise (optionnel)
- Génère un rapport d'analyse structuré

Voir [workflows/job-analyze.md](workflows/job-analyze.md) pour les détails.

### job-fit

Analyse l'adéquation entre le profil et le poste.

```bash
job-fit [--application=ID]
```

**Fonctionnalités:**

- Compare le CV aux exigences de l'offre
- Calcule un score d'adéquation global (0-100)
- Identifie forces et lacunes
- Génère des talking points pour l'entretien
- Fournit une recommandation go/no-go

Voir [workflows/job-fit.md](workflows/job-fit.md) pour les détails.

### job-cv

Génère une version du CV adaptée à l'offre.

```bash
job-cv [--format=short|long] [--dry-run]
```

**Fonctionnalités:**

- Réorganise les expériences par pertinence
- Intègre les mots-clés ATS de l'offre
- Ajuste les compétences de la sidebar
- Génère le fichier Typst adapté
- Compile le PDF automatiquement
- Produit un rapport des modifications

Voir [workflows/job-cv.md](workflows/job-cv.md) pour les détails.

### job-letter (Planned - INF-011)

Génère une lettre de motivation personnalisée.

```bash
job-letter [--style=formal|modern]
```

## Architecture

```text
.claude/skills/job-application/
|-- SKILL.md                    # Ce fichier (Level 1)
|-- workflows/                  # Instructions détaillées (Level 2)
|   |-- job-analyze.md
|   |-- job-fit.md
|   |-- job-cv.md
|   `-- job-letter.md
`-- templates/                  # Templates de sortie
    |-- analysis-report.md
    |-- fit-report.md
    `-- modifications-report.md

data/applications/              # Données par candidature
`-- {company-date}/
    |-- job-posting.md          # Offre originale
    |-- analysis.md             # Résultat job-analyze
    |-- fit-report.md           # Résultat job-fit
    |-- cv-adapted.typ          # CV adapté
    |-- cv-adapted.pdf          # PDF compilé
    `-- modifications.md        # Rapport des modifications
```

## Workflow typique

```text
     [Offre d'emploi]
            |
            v
    +---------------+
    | job-analyze   |  --> analysis.md
    +---------------+
            |
            v
    +---------------+
    | job-fit       |  --> fit-report.md (score + recommandations)
    +---------------+
            |
      +-----+-----+
      |           |
      v           v
+-----------+ +-----------+
| job-letter| | job-cv    |
+-----------+ +-----------+
      |           |
      v           v
  [Lettre]    [CV adapté]
```

## Modèle de données

```yaml
application:
  id: "{company}-{date}"
  job:
    title: string
    company: string
    location: string
    type: string  # CDI, CDD, freelance
    url: string
    requirements:
      must_have: []
      nice_to_have: []
    responsibilities: []
    keywords: []  # ATS keywords
  fit_analysis:
    score: number  # 0-100
    strengths: []
    gaps: []
    talking_points: []
    recommendation: string  # go/consider/no-go
  outputs:
    cv_adapted: path
    cover_letter: path
```

## Links

- **CV Source:** [src/cv.typ](../../../src/cv.typ)
- **CV Modules:** [src/shared/](../../../src/shared/)
- **Applications Data:** [data/applications/](../../../data/applications/)

---

**Version:** 1.0.0
**Last Updated:** 2025-11-30
