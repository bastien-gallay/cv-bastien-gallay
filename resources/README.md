# Resources

Répertoire dédié aux ressources d'analyse et de référence pour le CV.

## Structure

```text
resources/
├── README.md                    # Ce fichier
├── audits/                      # Extractions de données sources
│   └── {TASK-ID}/               # Organisé par tâche d'audit
├── analyses/                    # Résultats d'analyses comparatives
│   └── {TASK-ID}/               # Organisé par tâche d'analyse
├── templates/                   # Templates réutilisables
├── external/                    # Ressources externes (CV de référence, etc.)
├── profile/                     # Profil professionnel de référence
└── linkedin-optimization-guide.md
```

## Contenu

### audits/

Données extraites de sources externes (LinkedIn, GitHub, etc.) lors d'audits comparatifs.

- Chaque audit est organisé dans un sous-dossier nommé par l'ID de la tâche (ex: `CNT-001/`)
- Contient les données brutes : `linkedin-profile.md`, `cv-snapshot.md`, exports CSV, etc.

### analyses/

Résultats d'analyses comparatives entre le CV et les sources de données.

- Chaque analyse correspond à une tâche et contient :
  - `audit-report.md` : Rapport d'analyse comparative
  - `recommendations.md` : Liste des recommandations
  - `recommendations-status.md` : Suivi des recommandations (pour `/task-from-analysis`)
  - `metrics.md` : Statistiques et métriques

### templates/

Templates réutilisables pour les audits et analyses :

- `audit-template.md` : Structure d'un rapport d'audit
- `recommendations-template.md` : Format des recommandations
- `source-extraction-template.md` : Guide d'extraction de sources

### external/

Ressources externes de référence :

- CV antérieurs (2019, 2021, 2025)
- Extraits de missions
- Documents de référence

### profile/

Profil professionnel consolidé :

- `professional-profile.md` : Profil de référence
- `SOURCE_INTERPRETATION_GUIDE.md` : Guide d'interprétation des sources

## Conventions

1. **Nommage des dossiers** : Utiliser l'ID de tâche (ex: `CNT-001/`)
2. **Protection** : Ne pas modifier les données d'audit après leur création
3. **Traçabilité** : Chaque recommandation → tâche → changement CV
4. **Organisation** : Un dossier par tâche d'analyse/audit

## Voir aussi

- [.tasks/ANALYSES.md](../.tasks/ANALYSES.md) : Dashboard des analyses
- [.tasks/TASK_RULES.md](../.tasks/TASK_RULES.md) : Règles de gestion des tâches
- [CLAUDE.md](../CLAUDE.md) : Documentation du projet
