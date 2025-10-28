# DOC-001: Système d'automatisation de gestion des tâches

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | DOC-001 |
| **Titre** | Système d'automatisation de gestion des tâches |
| **Statut** | 🔄 En cours |
| **Priorité** | 🔴 Haute |
| **Trigramme** | DOC |
| **Section CV** | N/A |
| **Créé le** | 2025-10-28 |
| **Cible** | 2025-10-28 |
| **Terminé le** | (à remplir lors de la complétion) |
| **Temps estimé** | 2 heures |
| **Temps réel** | (à remplir après) |

---

## Description

Créer un système complet d'automatisation pour la gestion des tâches incluant des règles formelles (DoR/DoD) et des commandes Claude pour les opérations courantes.

### Contexte

Le workflow actuel de gestion des tâches est entièrement manuel et nécessite de nombreuses étapes répétitives. Chaque interruption et reprise de travail génère une friction importante due au temps nécessaire pour:

- Mettre à jour les statuts dans les fichiers et le dashboard
- Respecter les conventions de nommage et de format
- Maintenir la cohérence entre TASKS.md et les fichiers individuels
- Générer les commits Git avec les bonnes références

Cette friction réduit la productivité et augmente le risque d'erreurs ou d'oublis dans le processus.

### Objectif

Réduire drastiquement la friction lors de la création, du démarrage, et de la finalisation des tâches grâce à:

1. Des règles formalisées (DoR/DoD) garantissant la qualité
2. 6 commandes Claude automatisant les opérations courantes
3. Une synchronisation automatique entre les fichiers et le dashboard
4. Une intégration Git simplifiée avec génération de commits conformes

---

## Sous-tâches

- [x] Créer la branche Git task/DOC-001-task-management-automation
- [x] Créer le répertoire .claude/commands/
- [x] Créer ce fichier DOC-001 et l'ajouter à TASKS.md
- [x] Créer TASK_RULES.md avec DoR/DoD
- [x] Implémenter /task-create
- [x] Implémenter /task-start
- [x] Implémenter /task-complete
- [x] Implémenter /task-validate
- [x] Implémenter /task-next
- [x] Implémenter /task-archive
- [x] Créer .claude/commands/README.md
- [x] Mettre à jour CLAUDE.md
- [x] Tester la compilation du CV
- [x] Commit final et clôture

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Principes à respecter:**

- Commandes concises par défaut avec option --verbose
- Mode interactif pour la gestion des erreurs
- Format des commandes: `/task-<action>`
- Synchronisation automatique task files ↔ TASKS.md
- Validation stricte des formats et IDs

**Outils/commandes à utiliser:**

- Read/Write/Edit pour manipuler les fichiers
- Bash pour Git (branches, commits)
- Grep/Glob pour rechercher les IDs existants

**Fichiers à consulter:**

- [TASKS.md](../TASKS.md) - Dashboard central
- [TASKS/TEMPLATE.md](./TEMPLATE.md) - Structure de référence
- [CLAUDE.md](../CLAUDE.md) - Documentation projet
- [GIT_WORKFLOW.md](../GIT_WORKFLOW.md) - Conventions Git

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Décisions prises:**

- Option A pour les règles (génériques pour toutes les tâches)
- Scénario intermédiaire pour l'automatisation (status + branche + commit)
- Priorité: terminer proprement tout en réduisant le temps
- Workflow solo (pas de collaboration)
- Friction principale: reprise de travail après interruption

**Commandes prioritaires:**

1. /task-create
2. /task-start
3. /task-complete

**Commandes secondaires:**
4. /task-validate
5. /task-next
6. /task-archive

---

## Références externes

### Fichiers du projet

- [TASKS.md](../TASKS.md) - Dashboard à maintenir synchronisé
- [TASKS/TEMPLATE.md](./TEMPLATE.md) - Template à utiliser pour création
- [CLAUDE.md:104-181](../CLAUDE.md#L104-L181) - Section task management actuelle
- [GIT_WORKFLOW.md](../GIT_WORKFLOW.md) - Conventions de commits

### Tâches liées

Aucune tâche liée directement.

### Ressources

- Documentation Claude Code: <https://docs.claude.com/en/docs/claude-code>
- Typst documentation: <https://typst.app/docs>

---

## Commits Git associés

### En cours de travail

```bash
# Commit de démarrage
git commit -m "chore(tasks): 🔧 start DOC-001 task automation system

Refs DOC-001"

# Commits incrémentaux
git commit -m "feat(tasks): ✨ add task rules and DoR/DoD

Refs DOC-001"

git commit -m "feat(tasks): ✨ implement priority commands (create/start/complete)

Refs DOC-001"
```

### Commit final

```bash
git commit -m "feat(tasks): ✨ add task automation commands and rules

- Created TASK_RULES.md with DoR/DoD definitions
- Implemented 6 Claude commands for task management
- Added comprehensive documentation in .claude/commands/README.md
- Updated CLAUDE.md with task automation references
- Automated task file ↔ TASKS.md synchronization
- Integrated Git workflow with automatic commit generation

Closes DOC-001"
```

**Format suggéré:**

- **Type**: feat (nouvelle fonctionnalité)
- **Scope**: tasks
- **Emoji**: ✨ (sparkles pour nouvelle feature)

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`typst compile cv.typ`)
- [ ] Les 6 commandes fonctionnent correctement
- [ ] La synchronisation TASKS.md fonctionne
- [ ] Les IDs sont auto-générés correctement
- [ ] Les commits Git respectent les conventions
- [ ] La documentation est claire et complète
- [ ] Mode interactif gère correctement les erreurs
- [ ] Option --verbose fonctionne

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-28 | Création | Tâche créée et ajoutée au système |
| 2025-10-28 | En cours | Début de l'implémentation |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait:**

- [Liste des réalisations]

**Difficultés rencontrées:**

- [Problèmes et solutions]

**Améliorations futures:**

- [Idées pour aller plus loin]
