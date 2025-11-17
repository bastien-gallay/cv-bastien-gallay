# Manual Tests - Session 1

Tests manuels pour valider le fonctionnement du skill task-management.

## Session 1: task-next + Infrastructure

### Test 1: Suggestion de tâche basique

**Setup:** Avoir plusieurs tâches "⏳ À faire" dans `.tasks/tasks/`

**Commande:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/algorithms/priority_scorer.py
```

**Attendu:**

- Affiche "💡 Prochaine tâche suggérée: [ID]"
- Affiche le top 3 des tâches
- Scores décroissants
- Formule WSJF visible (valeur/temps)

**Status:** [x]

---

### Test 2: Aucune tâche disponible

**Setup:** Mettre toutes les tâches en "🔄 En cours" ou "✅ Terminé" temporairement

**Commande:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/algorithms/priority_scorer.py
```

**Attendu:**

- Message: "⚠️  Aucune tâche en attente!"
- Pas d'erreur

**Status:** [ ]

*Note utilisateur:*

```markdown
Il est difficile de mettre toutes les tâches à "En cours" étant donné que ce sont de vraies tâches. Ce serait bien de revoir ce test en créant un environnement isolé (jouer sur les chemins dans `.claude/skills/task-management/config/paths.yml`)
```

---

### Test 3: Configuration YAML loading

**Commande:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/core/config_loader.py
```

**Attendu:**

- Charge priorities.yml (🔴 Haute = score 10)
- Charge trigrammes.yml (7 trigrammes)
- Charge paths.yml
- "✅ All configs loaded successfully!"

**Status:** [x]

---

### Test 4: File parser sur tâche réelle

**Commande:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/core/file_parser.py
```

**Attendu:**

- Parse une tâche de `.tasks/tasks/`
- Extrait métadonnées (ID, Statut, Priorité)
- Compte sous-tâches (X/Y completed)
- Extrait sections (Description, Notes)

**Status:** [x]

---

### Test 5: Tests unitaires

**Commande:**

```bash
cd .claude/skills/task-management && uv run --with pytest python3 -m pytest tests/test_file_parser.py -v
```

**Attendu:**

- 7 tests passent
- test_parse_metadata_table PASSED
- test_extract_subtasks PASSED
- test_parse_task_file PASSED
- Etc.

**Status:** [x]

*Note utilisateur:*

```markdown
1. il serait mieux d'utiliser la commande `uvx pytest tests/test_file_parser.py -v`, plus courte
2. Note pour plus tard: Je suis partagé par le fait d'exécuter les tests depuis `.claude/skills/task-management`. En effet, à la fois cela permet de garder une isolation de ces skills dans le but de les réutiliser, et en même temps, au sein de ce projet, utiliser une "2e racine" me semble compliqué. (ce problème est peut-être lié à l'échec du test 4)
```

---

### Test 6: Output JSON

**Commande:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/algorithms/priority_scorer.py --json --top 3
```

**Attendu:**

- Output JSON valide
- Contient id, title, priority, score, breakdown
- Top 3 tâches

**Status:** [x]

---

## Notes

- Tous les tests doivent être exécutés depuis la racine du projet (`/Users/bastiengallay/Dev/cv/neat-cv/`)
- Les chemins relatifs dans les configs supposent cette racine
- `uv run --with pyyaml` installe automatiquement les dépendances

### Tests isolés (sans affecter la production)

Pour tester sans modifier les vraies tâches, utilisez des variables d'environnement :

```bash
# Créer un répertoire de test
mkdir -p .tasks/test-tasks

# Copier une tâche d'exemple
cp .tasks/tasks/CNT-001*.md .tasks/test-tasks/

# Exécuter avec override
TASK_SYSTEM_TASKS_DIR=.tasks/test-tasks uv run --with pyyaml python3 .claude/skills/task-management/scripts/core/file_parser.py
```

Variables d'environnement disponibles :

- `TASK_SYSTEM_TASKS_DIR` - Répertoire des tâches
- `TASK_SYSTEM_ARCHIVED_DIR` - Répertoire d'archives
- `TASK_SYSTEM_DASHBOARD` - Chemin vers TASKS.md

## Validation Finale

- [ ] Tous les tests manuels passent
- [ ] Aucune erreur Python
- [ ] Output conforme aux attentes
- [x] Configuration chargée correctement
- [x] Algorithme WSJF produit des résultats cohérents

**Validé par:** _______
**Date:** _______

---

## Session 2: Core Infrastructure + Validators

### Test 7: ID Generator

**Command:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/core/id_generator.py
```

**Attendu:**

- Shows existing IDs by trigramme
- Generates next IDs for each trigramme
- Tests slug generation
- All operations succeed

**Status:** [x]

---

### Test 8: DoR Validator (Valid Task)

**Setup:** Have a valid task in "⏳ À faire" status

**Command:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/validators/dor_validator.py CNT-005
```

**Attendu:**

- ✅ Valid: Yes
- No error-level issues
- May have warnings (acceptable)

**Status:** [x]

*Note utilisateur:*

```markdown
Il faudrait pouvoir faire ce teste de manière isolé de l'environnement de prod.
```

---

### Test 9: DoR Validator (Invalid Task)

**Setup:** Try with a task that's "🔄 En cours"

**Command:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/validators/dor_validator.py <TASK-IN-PROGRESS>
```

**Attendu:**

- ❌ Valid: No
- Error: "Task already in progress"

**Status:** [x]

*Note utilisateur:*

```markdown
Il faudrait pouvoir faire ce teste de manière isolé de l'environnement de prod.
```

---

### Test 10: DoD Validator (In Progress Task)

**Setup:** Have a task in "🔄 En cours" with all subtasks checked

**Command:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/validators/dod_validator.py INF-004
```

**Attendu:**

- Shows validation results
- Checks status, subtasks, result section
- Exit code 0 if valid, 1 if invalid

**Status:** [x]

*Note utilisateur:*

```markdown
Il faudrait pouvoir faire ce teste de manière isolé de l'environnement de prod.
```

---

### Test 11: Dashboard Updater

**Command:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/core/dashboard_updater.py
```

**Attendu:**

- Reads TASKS.md successfully
- Shows count of active/completed tasks
- No errors

**Status:** [x]

---

### Test 12: Git Operations

**Command:**

```bash
uv run --with pyyaml python3 .claude/skills/task-management/scripts/core/git_operations.py
```

**Attendu:**

- Shows current branch
- Shows if uncommitted changes
- Formats commit message correctly

**Status:** [x]

---

### Test 13: Unit Tests (ID Generator)

**Command:**

```bash
cd .claude/skills/task-management && uvx --with pyyaml pytest tests/test_id_generator.py -v
```

**Attendu:**

- 25 tests pass
- No failures

**Status:** [x]

---

### Test 14: Unit Tests (DoR Validator)

**Command:**

```bash
cd .claude/skills/task-management && uvx --with pyyaml pytest tests/test_dor_validator.py -v
```

**Attendu:**

- 23 tests pass
- No failures

**Status:** [x]

---

## Validation Finale Session 2

- [ ] All Session 1 tests still pass
- [ ] All Session 2 manual tests pass
- [ ] ID generator works correctly
- [ ] DoR validator catches invalid states
- [ ] DoD validator validates completion criteria
- [ ] Dashboard operations work
- [ ] Git operations work
- [ ] All unit tests pass

**Validé par:** _______
**Date:** _______

---

## Session 3: Analysis & Lifecycle Workflows

### Test 15: Recommendation Parser (Unit Tests)

**Command:**

```bash
cd .claude/skills/task-management && uvx --with pyyaml pytest tests/test_recommendation_parser.py -v
```

**Attendu:**

- 19 tests pass
- No failures

**Status:** [x]

---

### Test 16: All Tests Suite

**Command:**

```bash
cd .claude/skills/task-management && uvx --with pyyaml pytest tests/ -v
```

**Attendu:**

- 74 tests pass (25 id_generator + 23 dor_validator + 7 file_parser + 19 recommendation_parser)
- No failures

**Status:** [x]

---

## Validation Finale Session 3

- [x] All Session 1+2 tests still pass
- [x] Recommendation parser tests pass (19/19)
- [x] Complete test suite passes (74/74)
- [ ] Workflows documented and accessible
- [ ] No regression in existing functionality

**Validé par:** _______
**Date:** _______

---

## Notes de Migration

**Sessions complétées:**

- ✅ Session 1: Architecture + Infrastructure (config, file_parser, priority_scorer)
- ✅ Session 2: Core + Validators (id_generator, dor/dod_validator, dashboard_updater, git_operations)
- ✅ Session 3: Analysis + Lifecycle (recommendation_parser, 6 workflows)
- ⏳ Session 4: Tests + Documentation + Cleanup (en cours)

**Métriques:**

- **Tests unitaires:** 74 (tous passent)
- **Workflows:** 8 (task-next, create, complete, from-analysis, analyze-source, start, archive, validate, from-idea)
- **Scripts Python:** 10 modules
- **Réduction contexte:** ~2,340 lignes de slash commands → ~1,900 lignes de workflows (réutilisables)
