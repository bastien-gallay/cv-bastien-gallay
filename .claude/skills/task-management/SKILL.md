---
name: task-management
description: Système de gestion de tâches avec workflows Git, analyse comparative, et priorisation intelligente. Activer ce skill quand l'utilisateur parle de tâches, backlog, analyses de CV, ou demande quelle tâche faire ensuite.
version: 2.0.0
commands:
  - task-next
  - task-create
  - task-from-idea
  - task-start
  - task-complete
  - task-validate
  - task-archive
  - task-from-analysis
  - analyze-source
---

# Task Management Skill

Système unifié de gestion de tâches pour le projet CV, migré depuis les slash commands vers une architecture skill avec progressive disclosure.

## Available Commands (Session 1)

### ✅ task-next

Suggère la prochaine tâche optimale selon l'algorithme WSJF (valeur/temps).

```
task-next [--verbose] [--start]
```

Voir [workflows/task-next.md](workflows/task-next.md) pour les détails.

### 🔄 task-create (Session 2)

Créer une nouvelle tâche de manière interactive.

### 🔄 task-start (Session 2)

Démarrer le travail sur une tâche (DoR validation, branche Git).

### 🔄 task-complete (Session 2)

Finaliser une tâche (DoD validation, commit, merge).

### ⏳ Other Commands (Sessions 2-3)

- `task-from-idea`: Créer depuis IDEAS.md
- `task-validate`: Valider la cohérence du système
- `task-archive`: Archiver une tâche terminée
- `task-from-analysis`: Créer depuis recommandations d'analyse
- `analyze-source`: Extraire données depuis source externe

## Architecture

Ce skill utilise **progressive disclosure** (3 niveaux):

1. **Level 1** (ce fichier): Métadonnées (~200 tokens, toujours chargé)
2. **Level 2** (`workflows/*.md`): Instructions workflow (~1-2k tokens, chargé à la demande)
3. **Level 3** (`scripts/`, `config/`): Implémentation (scripts exécutés, output seulement)

**Avantage:** Les scripts Python sont exécutés sans charger leur code en contexte (~0 tokens pour l'implémentation).

## Configuration

- `config/priorities.yml`: Niveaux de priorité (scores, emojis, temps par défaut)
- `config/trigrammes.yml`: Catégories de tâches (CNT, TPL, QUA, etc.)
- `config/paths.yml`: Chemins des fichiers

Configuration chargée via `scripts/core/config_loader.py` avec validation Python dataclasses.

## Documentation

- [README.md](README.md): Documentation utilisateur
- [skill-architecture-design.md](skill-architecture-design.md): Architecture détaillée avec diagrammes Mermaid
- [tests/MANUAL_TESTS.md](tests/MANUAL_TESTS.md): Scénarios de test utilisateur

## Migration Status

**Session 1** (Current - Completed):
- ✅ Architecture design
- ✅ Config system (YAML + Python)
- ✅ file_parser.py (parse task files)
- ✅ priority_scorer.py (WSJF algorithm)
- ✅ task-next workflow

**Session 2** (Planned):
- Core utilities (id_generator, dashboard_updater, git_operations)
- Validators (DoR, DoD, system)
- Lifecycle commands (create, start, complete)

**Session 3** (Planned):
- Analysis commands (from-analysis, analyze-source)
- Secondary commands (archive, validate, from-idea)

**Session 4** (Planned):
- Documentation update
- Remove old slash commands
- End-to-end validation

## Links

- **Task:** [INF-004](../../.tasks/tasks/INF-004-migrer-systeme-gestion-taches-vers-skill-claude-unifie.md)
- **Old Commands:** `.claude/commands/task-*.md` (will be removed in Session 4)
- **Task Rules:** `.tasks/TASK_RULES.md` (DoR/DoD definitions)

---

**Version:** 2.0.0
**Status:** Session 1 - Foundation Complete
**Last Updated:** 2025-11-16
