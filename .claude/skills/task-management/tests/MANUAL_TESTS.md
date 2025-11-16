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
