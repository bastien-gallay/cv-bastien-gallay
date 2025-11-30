# Job Analyze Skill

Analyse d'offres d'emploi pour extraire les informations structurées et les mots-clés ATS.

## Available Commands

### job-analyze

Analyse une offre d'emploi depuis une URL ou du texte.

```
job-analyze [URL ou texte]
```

Voir [workflows/job-analyze.md](workflows/job-analyze.md) pour les détails.

## Architecture

Ce skill utilise **progressive disclosure** (3 niveaux):

1. **Level 1** (ce fichier): Métadonnées (~200 tokens)
2. **Level 2** (`workflows/*.md`): Instructions workflow (~1-2k tokens)
3. **Level 3** (`scripts/job_analyze/`): Implémentation Python

## Configuration

Les analyses sont sauvegardées dans `data/applications/{id}/`.

## Scripts Python

- `scripts/job_analyze/parser.py` - Parse et extrait les informations structurées
- `scripts/job_analyze/report.py` - Génère le rapport d'analyse
- `scripts/job_analyze/tests/` - Tests unitaires (pytest)

## Links

- **Task:** [INF-009](../../.tasks/tasks/INF-009-skill-analyse-offre-emploi.md)
- **Downstream:** INF-010 (fit analysis), INF-011 (cover letter), INF-012 (adapted CV)

---

**Version:** 1.0.0
**Status:** In Development
**Last Updated:** 2025-11-29
