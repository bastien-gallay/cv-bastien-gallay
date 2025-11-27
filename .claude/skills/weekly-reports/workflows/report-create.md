# Workflow: report-create

Crée un nouveau rapport hebdomadaire complet avec CFD.

## Paramètres

| Paramètre | Description | Défaut |
|-----------|-------------|--------|
| `--week` | Semaine ISO (YYYY-WNN) | Semaine courante |

## Étapes

1. **Déterminer la semaine** (courante si non spécifiée)

2. **Collecter les données** depuis `.tasks/TASKS.md` et `.tasks/.archived/`:
   - Tâches terminées cette semaine
   - Tâches créées cette semaine
   - Backlog actuel

3. **Créer le JSON** `.tasks/reports/{week}-data.json`:

   ```json
   {
     "week": "2025-W48",
     "title": "CFD - Semaine 48",
     "data": [
       {"date": "2025-11-24", "backlog": 29, "in_progress": 0, "done": 12}
     ]
   }
   ```

4. **Générer le CFD**:

   ```bash
   uv run --with matplotlib --with numpy scripts/reports/generate_cfd.py \
     --data .tasks/reports/{week}-data.json \
     --output .tasks/reports/
   ```

5. **Créer le rapport markdown** `.tasks/reports/{week}-recap.md`

## Fichiers créés

- `.tasks/reports/{week}-recap.md`
- `.tasks/reports/{week}-cfd.png`
- `.tasks/reports/{week}-data.json`
