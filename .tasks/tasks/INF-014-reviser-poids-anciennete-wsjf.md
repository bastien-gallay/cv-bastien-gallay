# INF-014: Réviser le poids de l'ancienneté dans le calcul WSJF

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-014 |
| **Titre** | Réviser le poids de l'ancienneté dans le calcul WSJF |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-30 |
| **Cible** | - |
| **Terminé le** | 2025-11-30 |
| **Temps estimé** | 1 heure |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Réviser la formule de calcul des priorités WSJF pour réduire l'impact de l'ancienneté des tâches sur le score final.

### Contexte

Le système actuel de priorisation WSJF (Weighted Shortest Job First) accorde un poids important à l'ancienneté des tâches. Cela peut conduire à :

- Des tâches anciennes mais peu importantes qui remontent artificiellement en priorité
- Une distorsion de la priorisation par rapport à la vraie valeur business
- Des tâches récentes mais urgentes qui sont sous-évaluées

### Objectif

- Analyser la formule actuelle et l'impact de l'ancienneté
- Proposer une nouvelle pondération avec moins d'impact de l'ancienneté
- Implémenter et tester la nouvelle formule
- Recalculer les priorités avec les nouveaux paramètres

---

## Sous-tâches

- [ ] Analyser le script `scripts/update_priority_scores.py` et la config `config/priorities.yml`
- [ ] Identifier le facteur d'ancienneté actuel et son poids
- [ ] Proposer une nouvelle pondération (ex: diviser par 2)
- [ ] Implémenter la modification
- [ ] Recalculer les priorités et vérifier les résultats
- [ ] Documenter le changement

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Fichiers à modifier:**

- [config/task_management/priorities.yml](../../config/task_management/priorities.yml) - Configuration des priorités
- [scripts/update_priority_scores.py](../../scripts/update_priority_scores.py) - Script de calcul

**Approche suggérée:**

1. Lire la config et le script pour comprendre la formule actuelle
2. Identifier le coefficient d'ancienneté
3. Proposer une réduction (ex: coefficient × 0.5)
4. Appliquer et tester avec `uv run scripts/update_priority_scores.py`

---

## Notes pour l'utilisateur

L'ancienneté ne devrait pas être le facteur dominant. Une tâche récente à haute valeur business devrait rester prioritaire face à une vieille tâche de moindre importance.

---

## Références externes

### Fichiers du projet

- [scripts/update_priority_scores.py](../../scripts/update_priority_scores.py)
- [config/task_management/priorities.yml](../../config/task_management/priorities.yml)

### Tâches liées

- [INF-003](./INF-003-perenniser-ameliorer-script-priorites.md) - Pérenniser le script de priorités

---

## Commits Git associés

### Commit final

```bash
git commit -m "chore(tasks): 🔧 reduce age weight in WSJF priority formula

Closes INF-014"
```

---

## Tests / Vérifications

- [ ] Le script de calcul s'exécute sans erreur
- [ ] Les priorités sont recalculées
- [ ] L'impact de l'ancienneté est réduit (vérifier avec tâches anciennes vs récentes)

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-30 | Création | Tâche créée |
| 2025-11-30 | En cours | Début du travail |
| 2025-11-30 | Terminé | Implémentation config YAML + script modifié |

---

## Résultat final

[À remplir une fois la tâche terminée]
