# Task-Next Workflow

Suggère la prochaine tâche à traiter selon l'algorithme WSJF (Weighted Shortest Job First).

## Usage

```
task-next [--verbose] [--start]
```

## Options

- `--verbose`: Affiche le raisonnement détaillé derrière la suggestion
- `--start`: Démarre automatiquement la tâche suggérée

## Behavior

### 1. Exécution de l'Algorithme

Execute le script de scoring:

```bash
uv run --with pyyaml python3 scripts/task_management/algorithms/priority_scorer.py --top 3
```

### 2. Affichage des Résultats

Le script retourne les 3 meilleures tâches avec:
- Score WSJF (valeur/temps)
- Priorité et temps estimé
- Justification du score

**Formule:** `Score = (Priorité × 10 + Urgence × 5 + Âge × 1) / Temps`

### 3. Option --start

Si `--start` est spécifié, démarrer automatiquement la tâche suggérée:

```
task-start <ID-suggéré>
```

## Errors

**Aucune tâche disponible:**
- Toutes les tâches sont terminées ou en cours
- Message: "⚠️  Aucune tâche en attente!"

**Erreur de parsing:**
- Fichier de tâche mal formé
- Afficher warning et continuer avec les autres tâches

## Examples

**Suggestion basique:**
```
> task-next

💡 Prochaine tâche suggérée: CNT-008
📋 Ajouter l'expérience i-BP
🔴 Haute | ⏱️  0.5h | Score: 23.60
```

**Avec --start:**
```
> task-next --start

💡 Démarrage de CNT-008...
[Lance task-start CNT-008]
```

## Notes

- Algorithme implémenté dans `scripts/task_management/algorithms/priority_scorer.py`
- Configuration des priorités dans `config/priorities.yml`
- Les tâches "🔄 En cours" et "✅ Terminé" sont automatiquement filtrées
