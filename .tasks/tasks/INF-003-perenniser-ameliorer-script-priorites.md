# INF-003: Pérenniser et améliorer le script Python de calcul des priorités

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-003 |
| **Titre** | Pérenniser et améliorer le script Python de calcul des priorités |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
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

Le script `scripts/priority_weight.py` est actuellement utilisé par `/task-next` pour calculer les priorités des tâches selon un modèle "valeur/délai". Ce script nécessite une refonte pour être maintenable et évolutif.

### Contexte

Idée issue de la tâche CNT-002 (2025-11-16).

Le script scripts/priority_weight.py est actuellement utilisé par /task-next pour calculer les priorités des tâches. Il nécessite une pérennisation et des améliorations pour être maintenu dans le futur.

**Problèmes actuels identifiés :**
- Liste des task_ids hardcodée (ligne 8-10)
- Date du jour hardcodée (ligne 16 : `today = datetime(2025, 11, 16)`)
- Manque de flexibilité pour le paramétrage
- Pas de cache pour accélérer les calculs répétitifs
- Pas de tests unitaires

### Objectif

Gagner en cohérence dans le calcul de priorité, accélérer cette action et permettre des évolutions futures (paramétrage différent, ajout de cache, etc...)

**Résultat attendu :**
- Script autonome qui lit automatiquement TASKS.md
- Date calculée dynamiquement
- Paramètres configurables (poids, valeurs par défaut)
- Cache optionnel pour performances
- Tests unitaires
- Documentation claire

---

## Sous-tâches

- [ ] Analyser le code actuel et documenter les améliorations nécessaires
- [ ] Refactorer pour lecture automatique de TASKS.md (éliminer liste hardcodée)
- [ ] Remplacer la date hardcodée par `datetime.now()`
- [ ] Externaliser les paramètres de calcul (poids, valeurs par défaut)
- [ ] Implémenter un système de cache optionnel
- [ ] Ajouter des tests unitaires
- [ ] Documenter l'utilisation et les paramètres
- [ ] Mettre à jour `/task-next` si nécessaire

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

- [ ] Le script s'exécute sans erreur
- [ ] Aucune valeur hardcodée (task IDs, dates)
- [ ] Les résultats sont cohérents avec l'ancienne version
- [ ] `/task-next` fonctionne correctement avec le nouveau script
- [ ] Les tests unitaires passent
- [ ] La documentation est claire et complète
- [ ] Le code respecte les conventions Python (PEP8)

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-16 | Création | Tâche créée depuis idée du backlog (source: CNT-002) |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations]

**Difficultés rencontrées :**

- [Problèmes et solutions]

**Améliorations futures :**

- [Idées pour aller plus loin]
