# Workflow: report-update

Met à jour un rapport hebdomadaire existant.

## Paramètres

| Paramètre | Description | Défaut |
|-----------|-------------|--------|
| `--week` | Semaine ISO (YYYY-WNN) | Semaine courante |

## Cas d'utilisation

1. **Ajouter des données CFD** - Nouveaux points de données quotidiens
2. **Mettre à jour les notes** - Observations, blocages, améliorations
3. **Corriger des erreurs** - Données incorrectes
4. **Régénérer le CFD** - Après modification du JSON

## Étapes

1. **Lire les fichiers existants**:
   - `.tasks/reports/{week}-data.json`
   - `.tasks/reports/{week}-recap.md`

2. **Proposer les actions**:
   - Ajouter données CFD
   - Modifier notes
   - Régénérer CFD

3. **Appliquer les modifications**

4. **Régénérer le CFD si nécessaire**:

   ```bash
   uv run --with matplotlib --with numpy scripts/reports/generate_cfd.py \
     --data .tasks/reports/{week}-data.json \
     --output .tasks/reports/{week}-cfd.png
   ```

## Exemple: Ajouter un point de données

```json
// Ajouter à .tasks/reports/2025-W48-data.json
{
  "date": "2025-11-28",
  "backlog": 15,
  "in_progress": 1,
  "done": 42,
  "comment": "Jeudi soir - 2 tâches terminées"
}
```

## Exemple: Mettre à jour les notes

Éditer la section "Notes et observations" dans le fichier `.tasks/reports/{week}-recap.md`.
