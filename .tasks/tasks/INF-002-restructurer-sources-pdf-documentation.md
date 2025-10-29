# INF-002: Restructurer les sources, PDF et documentation

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-002 |
| **Titre** | Restructurer les sources, PDF et documentation |
| **Statut** | 🔄 En cours |
| **Priorité** | 🔴 Haute |
| **Trigramme** | INF |
| **Section CV** | N/A |
| **Créé le** | 2025-10-29 |
| **Cible** | - |
| **Terminé le** | (à remplir lors de la complétion) |
| **Temps estimé** | 1 heure |
| **Temps réel** | (à remplir après) |

---

## Description

Restructurer l'arborescence du projet pour séparer clairement les concepts de Typst et ceux spécifiques au CV, améliorer l'organisation des fichiers de gestion de tâches, et mettre en place une structure de build appropriée.

### Contexte

Idée issue du backlog IDEAS.md. Le projet actuel manque d'organisation claire, avec trop de fichiers à la racine et une séparation insuffisante entre les sources Typst, les artefacts de build, et les fichiers de gestion de projet.
S'inspirer de projets Java ou Python pour créer une structure plus professionnelle.

### Objectif

Une navigation plus simple dans le repository, et une capacité à implémenter d'autres tâches de QUA et INF notamment.

---

## Sous-tâches

- [x] Réfléchir et proposer une structure correcte pour ce repo
- [x] Séparer les fichiers `*.typ` et leurs dépendances du reste des fichiers
- [x] Modifier l'infrastructure des tâches afin de les déplacer vers un dossier racine dédié (trop de fichiers de gestion à la racine)
- [x] Modifier les commandes `/task-*` en conséquences
- [ ] Modifier le fichier CLAUDE.md en conséquences
- [ ] Vérifier et ajuster les dépendances dans l'ensemble des tâches : fichier TASKS.md, TASK_RULES.md, IDEAS.md, GIT_WORKFLOW.md et `TASKS/*.md`
- [x] Disposer d'un dossier de build ou dist, qui comportera tous les CV construits dans ce repo
- [ ] Ajuster le .gitignore
- [x] Créer/adapter la configuration typst et créer des scripts ou un makefile-like afin de gérer les compilations typst correctement

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Lors de la restructuration, suivre ces principes :

1. **Proposer d'abord une structure** avant de procéder aux changements
2. **Séparer les préoccupations** : source Typst, build, gestion de projet, documentation
3. **S'inspirer des conventions** de projets bien organisés (Java, Python, etc.)
4. **Maintenir la compatibilité** avec les commandes existantes ou les mettre à jour
5. **Tester chaque étape** pour s'assurer que rien n'est cassé

**Outils/commandes à utiliser:**

- Bash pour déplacer les fichiers (`mv`, `mkdir`)
- Edit pour mettre à jour les chemins dans les fichiers
- Typst pour vérifier que la compilation fonctionne toujours
- `/task-validate` pour vérifier la cohérence du système de tâches

**Fichiers à consulter:**

- [TASKS.md](../TASKS.md) - Dashboard des tâches
- [TASK_RULES.md](../TASK_RULES.md) - Règles de gestion
- [CLAUDE.md](../CLAUDE.md) - Instructions projet
- [GIT_WORKFLOW.md](../GIT_WORKFLOW.md) - Convention Git
- [.claude/commands/](../.claude/commands/) - Commandes de tâches
- [cv.typ](../cv.typ) - Fichier source principal
- [.gitignore](../.gitignore) - Fichiers ignorés

**Structure proposée (exemple à affiner) :**

```txt
neat-cv/
├── src/               # Sources Typst
│   ├── cv.typ
│   ├── identite.png
│   └── ...
├── dist/              # Build outputs
│   └── cv.pdf
├── docs/              # Documentation projet
│   ├── CLAUDE.md
│   ├── GIT_WORKFLOW.md
│   └── ...
├── .tasks/            # Système de gestion des tâches
│   ├── TASKS.md
│   ├── TASK_RULES.md
│   ├── IDEAS.md
│   ├── tasks/         # Fichiers de tâches individuelles
│   └── .archived-tasks/
├── .claude/           # Configuration Claude
│   └── commands/
├── scripts/           # Scripts de build
│   └── build.sh
├── typst.toml         # Configuration Typst
├── .gitignore
└── README.md
```

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

- Cette restructuration est importante pour faciliter les futures tâches QUA et INF
- Penser à vérifier que tous les liens relatifs dans la documentation restent valides
- Ne pas oublier de mettre à jour le .gitignore pour exclure le dossier dist/
- Considérer l'ajout d'un Makefile ou justfile pour simplifier les commandes

---

## Références externes

### Fichiers du projet

- [cv.typ](../cv.typ) - Fichier source principal à déplacer
- [CLAUDE.md](../CLAUDE.md) - À déplacer et mettre à jour
- [TASKS.md](../TASKS.md) - À déplacer et mettre à jour
- [.claude/commands/](../.claude/commands/) - Commandes à adapter

### Tâches liées

- [INF-001](./INF-001-mcp-integration.md) - Bénéficiera d'une meilleure structure
- [QUA-001](./QUA-001-verification.md) - Bénéficiera d'une meilleure organisation

### Ressources

- Conventions de structure projet : Python, Java, Rust, etc.
- Documentation Typst sur l'organisation de projets
- [Just](https://github.com/casey/just) - Alternative moderne à Make

---

## Commits Git associés

### En cours de travail

```bash
# Exemple de commit pendant le développement
git commit -m "infra(structure): 🔧 propose new project structure

Refs INF-002"
```

### Commit final

```bash
# Exemple de commit de clôture
git commit -m "infra(structure): ♻️ restructure project organization

- Move Typst sources to src/
- Move task management to .tasks/
- Create dist/ for build outputs
- Update all documentation paths
- Add build scripts
- Update .gitignore

Closes INF-002"
```

**Format suggéré:**

- **Type**: infra
- **Scope**: structure
- **Emoji**: ♻️ (refactor) ou 🔧 (config)

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur après restructuration (`typst compile src/cv.typ`)
- [ ] Le PDF s'affiche correctement
- [ ] Toutes les commandes `/task-*` fonctionnent
- [ ] `/task-validate` ne retourne aucune erreur
- [ ] Tous les liens dans la documentation sont valides
- [ ] Le .gitignore exclut correctement les fichiers de build
- [ ] Les scripts de build fonctionnent

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis une idée du backlog |
| 2025-10-29 | En cours | Début du travail |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait:**

- [Liste des réalisations]

**Difficultés rencontrées:**

- [Problèmes et solutions]

**Améliorations futures:**

- [Idées pour aller plus loin]
