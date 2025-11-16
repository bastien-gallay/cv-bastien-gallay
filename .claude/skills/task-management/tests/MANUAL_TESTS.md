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

**Status:** [ ]

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

**Status:** [ ]

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

**Status:** [ ]

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

**Status:** [ ]

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

**Status:** [ ]

---

## Notes

- Tous les tests doivent être exécutés depuis la racine du projet (`/Users/bastiengallay/Dev/cv/neat-cv/`)
- Les chemins relatifs dans les configs supposent cette racine
- `uv run --with pyyaml` installe automatiquement les dépendances

## Validation Finale

- [ ] Tous les tests manuels passent
- [ ] Aucune erreur Python
- [ ] Output conforme aux attentes
- [ ] Configuration chargée correctement
- [ ] Algorithme WSJF produit des résultats cohérents

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

**Status:** [ ]

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

**Status:** [ ]

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

**Status:** [ ]

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

**Status:** [ ]

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

**Status:** [ ]

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

**Status:** [ ]

---

### Test 13: Unit Tests (ID Generator)

**Command:**
```bash
cd .claude/skills/task-management && uvx --with pyyaml pytest tests/test_id_generator.py -v
```

**Attendu:**
- 25 tests pass
- No failures

**Status:** [ ]

---

### Test 14: Unit Tests (DoR Validator)

**Command:**
```bash
cd .claude/skills/task-management && uvx --with pyyaml pytest tests/test_dor_validator.py -v
```

**Attendu:**
- 23 tests pass
- No failures

**Status:** [ ]

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
