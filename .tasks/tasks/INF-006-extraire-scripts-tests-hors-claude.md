# INF-006: Extraire scripts et tests hors de `.claude/`

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-006 |
| **Titre** | Extraire scripts, tests et paramètres hors de `.claude/` |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 3-4 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Réorganiser l'arborescence `.claude/` pour séparer les éléments de configuration (commands, skills) des éléments d'implémentation (scripts Python, tests, fichiers de paramètres).

### Contexte

Actuellement, le skill `task-management` contient :

```plaintext
.claude/skills/task-management/
├── workflows/        # Documentation workflow
├── scripts/          # Scripts Python (core/, analysis/)
├── config/           # Fichiers YAML de configuration
└── tests/            # 74 tests unitaires pytest
```

Cette structure pose plusieurs problèmes :

- **Édition difficile** : Claude Code a du mal à naviguer dans `.claude/` pour éditer les fichiers
- **Couplage fort** : Les scripts sont liés à l'implémentation Claude Code
- **Réutilisation limitée** : Difficile de packager les scripts pour d'autres assistants
- **Tests isolés** : Les tests sont cachés dans l'arborescence `.claude/`

### Objectif

Restructurer pour obtenir :

- **`.claude/`** : Uniquement les définitions de commands et skills (markdown, configuration légère)
- **`scripts/`** ou **`lib/`** : Scripts Python réutilisables
- **`tests/`** : Tests unitaires à la racine, visibles et exécutables facilement
- **`config/`** : Paramètres partagés entre skills et scripts

---

## Sous-tâches

- [ ] Analyser la structure actuelle de `.claude/skills/task-management/`
- [ ] Définir la nouvelle architecture cible
- [ ] Déplacer `scripts/` vers un répertoire à la racine
- [ ] Déplacer `tests/` vers un répertoire `tests/` à la racine
- [ ] Déplacer `config/` vers un répertoire partagé
- [ ] Mettre à jour les imports et chemins dans les scripts
- [ ] Mettre à jour les workflows pour pointer vers les nouveaux chemins
- [ ] Adapter le skill `task-management` pour utiliser la nouvelle structure
- [ ] Vérifier que tous les tests passent
- [ ] Documenter la nouvelle architecture

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Structure cible proposée :**

```plaintext
neat-cv/
├── .claude/
│   ├── commands/              # Slash commands (markdown)
│   │   └── *.md
│   └── skills/
│       └── task-management/
│           ├── skill.md       # Point d'entrée du skill
│           └── workflows/     # Documentation workflow uniquement
│               └── *.md
├── lib/                       # ou scripts/
│   └── task-management/
│       ├── core/              # Scripts Python core
│       │   ├── __init__.py
│       │   ├── config_loader.py
│       │   ├── file_parser.py
│       │   └── priority_scorer.py
│       └── analysis/          # Scripts d'analyse
│           └── *.py
├── config/
│   └── task-management/
│       ├── priorities.yml
│       ├── trigrammes.yml
│       └── paths.yml
└── tests/
    └── task-management/
        ├── conftest.py
        ├── test_config_loader.py
        ├── test_file_parser.py
        └── test_priority_scorer.py
```

**Avantages :**

1. **Édition facilitée** : Scripts et tests hors de `.claude/`
2. **Packaging** : `lib/task-management/` peut être extrait comme module
3. **Tests visibles** : `pytest tests/` depuis la racine
4. **Réutilisation** : Scripts utilisables par d'autres outils (CI, autres assistants)

**Points d'attention :**

- Mettre à jour tous les chemins relatifs dans les scripts
- Adapter `config_loader.py` pour trouver les configs au bon endroit
- Les workflows doivent appeler les scripts via `uv run` avec le bon chemin
- Possibilité d'utiliser `pyproject.toml` pour définir le package

**Fichiers à modifier :**

- Tous les fichiers dans `.claude/skills/task-management/scripts/`
- Workflows dans `.claude/skills/task-management/workflows/`
- [CLAUDE.md](../../CLAUDE.md) - Section Task Management System

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Décisions à prendre :**

- Nom du répertoire : `lib/` ou `scripts/` ?
- Conserver une copie des configs dans `.claude/` ou référence unique ?
- Créer un `pyproject.toml` pour le package ?

**Compatibilité :**

- Cette refonte doit être transparente pour l'utilisateur des commandes
- Les workflows doivent continuer à fonctionner sans changement d'interface

**Lien avec INF-005 :**

Cette tâche peut être coordonnée avec [INF-005](./INF-005-repertoire-ressources-dedie.md) pour une réorganisation globale cohérente.

---

## Références externes

### Fichiers du projet

- [.claude/skills/task-management/](../../.claude/skills/task-management/) - Structure actuelle
- [CLAUDE.md](../../CLAUDE.md) - Documentation à mettre à jour

### Tâches liées

- [INF-005](./INF-005-repertoire-ressources-dedie.md) - Répertoire ressources dédié (réorganisation similaire)
- [INF-003](./INF-003-perenniser-ameliorer-script-priorites.md) - Script priorités (sera impacté)

### Ressources

- Python packaging best practices
- pytest project structure conventions

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "refactor(infra): ♻️ move task-management scripts to lib/

Extract Python scripts from .claude/ for better accessibility.

Refs INF-006"
```

### Commit final

```bash
git commit -m "refactor(infra): ♻️ reorganize task-management architecture

- Moved scripts to lib/task-management/
- Moved tests to tests/task-management/
- Moved config to config/task-management/
- Updated all imports and paths
- Simplified .claude/ structure to definitions only

Closes INF-006"
```

**Format suggéré :**

- **Type**: refactor
- **Scope**: infra
- **Emoji**: ♻️ (restructuration)

---

## Tests / Vérifications

- [ ] Tous les 74 tests passent après migration
- [ ] Les workflows fonctionnent avec les nouveaux chemins
- [ ] `uv run pytest tests/` fonctionne depuis la racine
- [ ] Les scripts sont importables depuis `lib/`
- [ ] La configuration est chargée correctement
- [ ] CLAUDE.md reflète la nouvelle structure
- [ ] Les commandes `/task-*` fonctionnent normalement

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée pour faciliter l'édition et le packaging |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations]

**Difficultés rencontrées :**

- [Problèmes et solutions]

**Améliorations futures :**

- [Idées pour aller plus loin]
