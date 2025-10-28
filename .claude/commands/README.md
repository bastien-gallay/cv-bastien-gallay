# Commandes Claude pour la Gestion des Tâches

Ce répertoire contient les commandes Claude personnalisées pour automatiser la gestion des tâches du projet CV.

## Vue d'Ensemble

Le système de gestion des tâches est documenté dans [TASK_RULES.md](../TASK_RULES.md) et [CLAUDE.md](../CLAUDE.md). Ces commandes automatisent les opérations courantes tout en respectant les règles définies (DoR/DoD).

## Commandes Disponibles

### Commandes Prioritaires

Ces commandes couvrent le cycle de vie complet d'une tâche:

#### `/task-create` - Créer une nouvelle tâche

Crée une nouvelle tâche de manière interactive en respectant le template.

**Utilisation:**

```bash
/task-create [--verbose]
```

**Fonctionnalités:**

- Guide interactif pour collecter toutes les informations
- Auto-génération de l'ID unique (XXX-NNN)
- Création du fichier depuis TEMPLATE.md
- Ajout automatique dans TASKS.md
- Mise à jour des statistiques

**Exemple:**

```bash
/task-create
# → Guide interactif
# → Crée TASKS/CNT-002-nom-de-la-tache.md
# → Ajoute l'entrée dans TASKS.md
```

[Documentation complète](task-create.md)

---

#### `/task-from-idea` - Créer une tâche depuis une idée

Transforme une idée du backlog [IDEAS.md](../IDEAS.md) en tâche concrète.

**Utilisation:**

```bash
/task-from-idea [--verbose]
```

**Fonctionnalités:**

- Liste interactive des idées disponibles
- Pré-remplissage automatique (trigramme, titre, contexte)
- Processus de création guidé
- Suppression automatique de l'idée du backlog
- Traçabilité (lien vers la tâche source)

**Exemple:**

```bash
/task-from-idea
# → Liste les idées du backlog
# → Sélection interactive
# → Création guidée avec pré-remplissage
# → Tâche créée et idée retirée
```

**Note:** Les idées sont ajoutées automatiquement dans [IDEAS.md](../IDEAS.md) lorsque vous complétez une tâche avec `/task-complete` et remplissez la section "Améliorations futures".

[Documentation complète](task-from-idea.md)

---

#### `/task-start <ID>` - Démarrer une tâche

Démarre le travail sur une tâche avec setup Git automatique.

**Utilisation:**

```bash
/task-start <ID> [--verbose]
```

**Fonctionnalités:**

- Validation de la DoR
- Mise à jour du statut vers "🔄 En cours"
- Création de la branche Git `task/{ID}-{slug}`
- Commit initial automatique
- Affichage du contexte de travail

**Exemple:**

```bash
/task-start CNT-001
# ou abrégé:
/task-start CNT1
```

[Documentation complète](task-start.md)

---

#### `/task-complete <ID>` - Terminer une tâche

Finalise une tâche avec validation DoD complète.

**Utilisation:**

```bash
/task-complete <ID> [--verbose] [--no-merge]
```

**Fonctionnalités:**

- Validation de la DoD
- Compilation automatique du CV
- Collecte interactive du résultat final
- Génération du commit final avec `Closes {ID}`
- Déplacement dans "Tâches terminées"
- Proposition de merge de la branche

**Exemple:**

```bash
/task-complete TPL1
# → Validation
# → Prompts interactifs
# → Commit final
# → Optionnel: merge dans main
```

[Documentation complète](task-complete.md)

---

### Commandes Secondaires

Ces commandes aident à maintenir et naviguer dans le système de tâches:

#### `/task-validate` - Valider la cohérence du système

Vérifie la cohérence entre fichiers et dashboard.

**Utilisation:**

```bash
/task-validate [--verbose] [--fix]
```

**Fonctionnalités:**

- Validation DoR/DoD de toutes les tâches
- Vérification de la cohérence structurelle
- Recalcul et validation des statistiques
- Détection des IDs en double
- Correction automatique avec `--fix`

**Exemple:**

```bash
/task-validate
# → Rapport de validation

/task-validate --fix
# → Correction automatique des erreurs simples
```

[Documentation complète](task-validate.md)

---

#### `/task-next` - Suggérer la prochaine tâche

Suggère la prochaine tâche selon un modèle "valeur/temps".

**Utilisation:**

```bash
/task-next [--verbose] [--start]
```

**Fonctionnalités:**

- Analyse des tâches "À faire"
- Calcul du ratio valeur/temps pour chaque tâche
- Suggestion intelligente (privilégie les "quick wins")
- Affichage du top 3
- Option `--start` pour démarrer automatiquement

**Principe:** Maximise le ratio valeur/temps en privilégiant les tâches courtes et importantes.

**Exemple:**

```bash
/task-next
# → Suggère la meilleure tâche

/task-next --start
# → Démarre automatiquement la tâche suggérée
```

[Documentation complète](task-next.md)

---

#### `/task-archive <ID>` - Archiver une tâche terminée

Archive une tâche terminée vers `.archived-tasks/`.

**Utilisation:**

```bash
/task-archive <ID> [--verbose]
```

**Fonctionnalités:**

- Validation que la tâche est terminée
- Mise à jour de l'historique (entrée d'archivage)
- Changement du statut vers "📦 Archivé"
- Déplacement vers `.archived-tasks/`
- Mise à jour de TASKS.md et statistiques
- Préservation de l'historique Git

**Exemple:**

```bash
/task-archive TPL1
# → Archive TASKS/TPL-001-*.md vers .archived-tasks/
# → Retire de TASKS.md
```

[Documentation complète](task-archive.md)

---

## Workflow Recommandé

### Créer une Tâche depuis une Idée

```bash
1. /task-from-idea
   → Liste les idées du backlog
   → Sélection interactive
   → Création guidée avec pré-remplissage
   → Tâche créée: DOC-002
   → Idée retirée de IDEAS.md

2. /task-start DOC-002
   → Branche créée: task/DOC-002-nom-tache
   → Statut: "🔄 En cours"
   → Contexte affiché
```

### Créer et Démarrer une Tâche Classique

```bash
1. /task-create
   → Suivre le guide interactif
   → Tâche créée: CNT-002

2. /task-start CNT-002
   → Branche créée: task/CNT-002-nom-tache
   → Statut: "🔄 En cours"
   → Contexte affiché
```

### Travailler sur une Tâche

```bash
# Faire des changements dans le code
# Cocher les sous-tâches au fur et à mesure

git add .
git commit -m "content(experience): ✏️ update profile

Refs CNT-002"

# Continuer jusqu'à ce que toutes les sous-tâches soient terminées
```

### Terminer et Archiver

```bash
1. /task-complete CNT-002
   → Validation DoD
   → Compilation CV
   → Prompts interactifs (dont "Améliorations futures")
   → Si améliorations renseignées: ajout automatique dans IDEAS.md
   → Commit final avec "Closes CNT-002"
   → Tâche déplacée dans "Terminées"

2. (Optionnel) /task-archive CNT-002
   → Archive dans .archived-tasks/
   → Retire de TASKS.md
```

### Maintenance

```bash
# Vérifier la cohérence du système
/task-validate

# Trouver la prochaine tâche à faire
/task-next

# Ou démarrer directement
/task-next --start
```

---

## Options Communes

### Option --verbose

Disponible sur toutes les commandes. Affiche des informations détaillées:

- Étapes intermédiaires
- Validations effectuées
- Contenu des fichiers modifiés
- Commandes Git exécutées

**Exemple:**

```bash
/task-start CNT-001 --verbose
```

### Abréviation des IDs

Toutes les commandes acceptent des IDs abrégés:

- **Format complet:** `CNT-003`
- **Format abrégé:** `CNT3` (sans tiret, sans zéros de tête)

**Exemple:**

```bash
/task-start CNT3      # équivalent à CNT-003
/task-complete TPL1   # équivalent à TPL-001
```

---

## Mode Interactif

Plusieurs commandes adoptent un comportement interactif en cas d'erreur ou de situation ambiguë:

**Exemple:**

```text
⚠️  Warning: La tâche CNT-001 est déjà en cours

Options:
1. Continuer sur cette tâche (afficher le contexte)
2. Redémarrer la tâche (reset le statut)
3. Annuler

Votre choix: _
```

Ce mode aide à gérer les cas limites sans bloquer l'utilisateur.

---

## Fichiers de Référence

- [TASK_RULES.md](../TASK_RULES.md) - Règles DoR/DoD et gestion des erreurs
- [TASKS.md](../TASKS.md) - Dashboard central des tâches
- [IDEAS.md](../IDEAS.md) - Backlog d'idées d'améliorations futures
- [TASKS/TEMPLATE.md](../TASKS/TEMPLATE.md) - Template de tâche
- [CLAUDE.md](../CLAUDE.md) - Instructions générales du projet
- [GIT_WORKFLOW.md](../GIT_WORKFLOW.md) - Conventions Git

---

## Conventions

### Commits

Les commandes respectent les conventions définies dans [GIT_WORKFLOW.md](../GIT_WORKFLOW.md):

- **Format:** `type(scope): emoji description`
- **Références:** `Refs XXX-NNN` (en cours) ou `Closes XXX-NNN` (final)
- **Emojis:** Selon le type de commit

**Exemple de commit généré:**

```bash
feat(template): ✨ add short and long CV variants

- Created cv-short.typ (1 page)
- Created cv-long.typ (2+ pages)
- Updated build script

Closes TPL-001
```

### Branches Git

Format: `task/{ID}-{slug}`

**Exemples:**

- `task/CNT-001-linkedin-audit`
- `task/TPL-002-template-system`
- `task/DOC-001-task-management-automation`

---

## Améliorations Futures

Commandes potentielles à ajouter:

- `/task-list [--status] [--trigramme]` - Lister les tâches avec filtres
- `/task-show <ID>` - Afficher les détails d'une tâche
- `/task-block <ID> <raison>` - Bloquer une tâche
- `/task-unblock <ID>` - Débloquer une tâche
- `/task-unarchive <ID>` - Restaurer une tâche archivée
- `/task-archive --all` - Archiver toutes les tâches terminées
- `/task-stats` - Statistiques détaillées
- `/task-export` - Exporter en CSV/JSON

---

## Support

Pour toute question ou suggestion d'amélioration:

1. Consulter [TASK_RULES.md](../TASK_RULES.md)
2. Consulter [CLAUDE.md](../CLAUDE.md)
3. Créer une nouvelle tâche avec `/task-create` (trigramme DOC)

---

**Version:** 1.1.0
**Dernière mise à jour:** 2025-10-28
