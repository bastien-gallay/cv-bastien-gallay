# INF-003: Pérenniser et améliorer le script Python de calcul des priorités

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-003 |
| **Titre** | Pérenniser et améliorer le script Python de calcul des priorités |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟢 Basse |
| **Trigramme** | INF |
| **Section CV** | N/A |
| **Créé le** | 2025-11-16 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | - |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

~~Le script `scripts/priority_weight.py` est actuellement utilisé par `/task-next` pour calculer les priorités des tâches selon un modèle "valeur/délai". Ce script nécessite une refonte pour être maintenable et évolutif.~~

### ⚠️ Mise à jour (2025-11-25)

**La majorité du travail a été réalisée** lors de la création du skill task-management. Le nouveau script [priority_scorer.py](../../.claude/skills/task-management/scripts/algorithms/priority_scorer.py) remplace l'ancien et implémente toutes les améliorations prévues :

| Objectif | Statut |
|----------|--------|
| Lecture automatique des tâches | ✅ Fait (`rank_tasks()`) |
| Date dynamique | ✅ Fait (`datetime.now()`) |
| Paramètres configurables | ✅ Fait (`config_loader`) |
| Documentation claire | ✅ Fait (docstrings) |
| CLI standalone | ✅ Fait (argparse) |
| Tests unitaires | ❌ **Reste à faire** |

L'ancien script `scripts/priority_weight.py` est désormais obsolète et pourra être supprimé.

### Contexte

Idée issue de la tâche CNT-002 (2025-11-16).

### Objectif résiduel

**Ajouter des tests unitaires** pour `priority_scorer.py` afin de garantir la fiabilité du calcul de priorités.

---

## Sous-tâches

- [x] Analyser le code actuel et documenter les améliorations nécessaires
- [x] Refactorer pour lecture automatique de TASKS.md (éliminer liste hardcodée)
- [x] Remplacer la date hardcodée par `datetime.now()`
- [x] Externaliser les paramètres de calcul (poids, valeurs par défaut)
- [x] Documenter l'utilisation et les paramètres
- [x] Mettre à jour `/task-next` pour utiliser le nouveau script
- [ ] Ajouter des tests unitaires pour `priority_scorer.py`
- [x] Supprimer l'ancien script `scripts/priority_weight.py`

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Lors du travail sur cette tâche :

1. **Analyse préalable :** Examiner le script actuel et identifier tous les points d'amélioration
2. **Compatibilité :** Assurer la compatibilité avec `/task-next` existant
3. **Tests :** Créer des tests unitaires avec des données fictives
4. **Documentation :** Documenter les formules de calcul et paramètres

**Outils/commandes à utiliser :**

- `uvx` ou `uv` pour exécuter Python
- Linter Python (ruff, pylint, ou équivalent)
- Tests avec pytest si disponible

**Fichiers à consulter :**

- [scripts/priority_weight.py](../../scripts/priority_weight.py) - Script actuel
- [.claude/commands/task-next.md](../../.claude/commands/task-next.md) - Commande qui utilise le script
- [.tasks/TASKS.md](../TASKS.md) - Source de données des tâches

**Critères de qualité :**

- Code maintenable et documenté
- Pas de valeurs hardcodées
- Paramètres configurables
- Performance préservée ou améliorée

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Points d'attention :**

- Ne pas casser `/task-next` pendant la refonte
- Considérer l'ajout d'un fichier de configuration (YAML/JSON) pour les paramètres
- Le cache pourrait être optionnel (flag `--no-cache`)
- Penser à la testabilité du code

**Idées d'améliorations futures :**

- Interface CLI avec argparse pour utilisation standalone
- Support de différents algorithmes de priorisation
- Visualisation graphique des scores
- Export des résultats (JSON, CSV)

---

## Références externes

### Fichiers du projet

- [scripts/priority_weight.py](../../scripts/priority_weight.py) - Script à refactorer
- [.claude/commands/task-next.md](../../.claude/commands/task-next.md) - Utilisateur du script
- [.tasks/TASKS.md](../TASKS.md) - Source de données

### Tâches liées

- [CNT-002](./CNT-002-corriger-ecart-critique-upwiser.md) - Tâche source de l'idée
- Potentiellement liée aux idées dans IDEAS.md (cache pour /task-next)

### Ressources

- [Python datetime documentation](https://docs.python.org/3/library/datetime.html)
- [Pathlib documentation](https://docs.python.org/3/library/pathlib.html)

---

## Commits Git associés

### En cours de travail

```bash
# Exemple de commit pendant le développement
git commit -m "refactor(infra): ♻️ improve priority calculation script

Remove hardcoded task IDs and date.

Refs INF-003"
```

### Commit final

```bash
# Exemple de commit de clôture
git commit -m "refactor(infra): ♻️ refactor priority calculation script

- Auto-read tasks from TASKS.md
- Dynamic date calculation
- Configurable parameters
- Added unit tests
- Improved documentation

Closes INF-003"
```

**Format suggéré :**

- **Type**: refactor
- **Scope**: infra
- **Emoji**: ♻️ (refactoring)

---

## Tests / Vérifications

- [x] Le script s'exécute sans erreur
- [x] Aucune valeur hardcodée (task IDs, dates)
- [x] `/task-next` fonctionne correctement avec le nouveau script
- [x] La documentation est claire et complète
- [ ] Les tests unitaires passent
- [x] L'ancien script est supprimé

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-16 | Création | Tâche créée depuis idée du backlog (source: CNT-002) |
| 2025-11-25 | Mise à jour | Priorité 🔴→🟢, scope réduit aux tests (refactoring déjà fait dans skill) |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations]

**Difficultés rencontrées :**

- [Problèmes et solutions]

**Améliorations futures :**

- [Idées pour aller plus loin]
