# PIP-002: Privilégier les questionnaires interactifs dans les commandes de tâches

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | PIP-002 |
| **Titre** | Privilégier les questionnaires interactifs dans les commandes de tâches |
| **Statut** | 🔄 En cours |
| **Priorité** | 🔴 Haute |
| **Trigramme** | PIP |
| **Section CV** | N/A |
| **Créé le** | 2025-11-16 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 0.25 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Améliorer l'expérience utilisateur dans les commandes de gestion de tâches en adoptant un format de questionnaire interactif unifié, similaire à celui utilisé dans `/task-complete`.

### Contexte

Améliorer l'expérience utilisateur lors de l'utilisation des commandes de gestion de tâches en adoptant un format de questionnaire interactif similaire à celui de `/task-complete`, plutôt que des questions successives isolées.

**Problème actuel :**

- Certaines commandes posent des questions une par une de manière séquentielle
- `/task-complete` utilise un format de questionnaire interactif avec numérotation (1., 2., 3., etc.)
- Manque de cohérence dans l'UX entre les différentes commandes
- Le format questionnaire est plus lisible et plus efficace

**Exemple de bonne pratique (`/task-complete`) :**

```markdown
1. Résultat de la tâche:
   ...

2. Difficultés rencontrées:
   ...

3. Améliorations futures:
   ...
```

### Objectif

Rendre plus agréable et rapide l'exécution des tâches pour l'utilisateur.

**Résultat attendu :**

- Toutes les commandes de gestion de tâches utilisent le format questionnaire interactif
- Cohérence dans l'expérience utilisateur
- Documentation mise à jour avec les bonnes pratiques
- Templates/exemples pour faciliter la création de nouvelles commandes

---

## Sous-tâches

- [ ] Auditer toutes les commandes de gestion de tâches (task-*.md)
- [ ] Identifier celles qui n'utilisent pas le format questionnaire
- [ ] Refactorer les commandes concernées
- [ ] Mettre à jour la documentation
- [ ] Créer un template/guide pour les futures commandes

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Lors du travail sur cette tâche :

1. **Audit :** Examiner toutes les commandes dans `.claude/commands/task-*.md`
2. **Comparaison :** Utiliser `/task-complete` comme référence du format cible
3. **Cohérence :** S'assurer que toutes les commandes suivent le même format
4. **Documentation :** Mettre à jour README.md des commandes si nécessaire

**Outils/commandes à utiliser :**

- Outil Read pour examiner les commandes existantes
- Outil Edit pour refactorer les commandes

**Fichiers à consulter :**

- [.claude/commands/task-complete.md](../../.claude/commands/task-complete.md) - Référence du bon format
- [.claude/commands/task-create.md](../../.claude/commands/task-create.md) - Peut-être à refactorer
- [.claude/commands/task-start.md](../../.claude/commands/task-start.md) - À vérifier
- [.claude/commands/task-from-idea.md](../../.claude/commands/task-from-idea.md) - Déjà au bon format
- [.claude/commands/README.md](../../.claude/commands/README.md) - Documentation

**Critères de qualité :**

- Format questionnaire numéroté cohérent
- Questions claires et bien structurées
- Expérience utilisateur fluide
- Documentation complète

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Points d'attention :**

- Ne pas casser les fonctionnalités existantes
- Tester chaque commande refactorée
- Privilégier la clarté sur la concision

**Format cible :**

```markdown
1. Question 1:
   [Contexte/aide]
   Réponse: _

2. Question 2:
   [Contexte/aide]
   Réponse: _
```

---

## Références externes

### Fichiers du projet

- [.claude/commands/](../../.claude/commands/) - Toutes les commandes
- [.claude/commands/task-complete.md](../../.claude/commands/task-complete.md) - Référence
- [.claude/commands/README.md](../../.claude/commands/README.md) - Documentation

### Tâches liées

- Aucune pour l'instant

### Ressources

- [Claude Code documentation](https://code.claude.com/docs) - Bonnes pratiques pour les slash commands

---

## Commits Git associés

### En cours de travail

```bash
# Exemple de commit pendant le développement
git commit -m "refactor(commands): ♻️ improve interactive questionnaire format

Refactor task-create to use numbered questionnaire.

Refs PIP-002"
```

### Commit final

```bash
# Exemple de commit de clôture
git commit -m "refactor(commands): ♻️ standardize interactive questionnaires

- All task commands now use numbered questionnaire format
- Improved UX consistency across commands
- Updated documentation with best practices
- Added template for future commands

Closes PIP-002"
```

**Format suggéré :**

- **Type**: refactor
- **Scope**: commands
- **Emoji**: ♻️ (refactoring)

---

## Tests / Vérifications

- [ ] Toutes les commandes task-* utilisent le format questionnaire
- [ ] Les commandes fonctionnent correctement après refactoring
- [ ] La documentation est à jour
- [ ] Un template/guide existe pour les futures commandes
- [ ] L'expérience utilisateur est cohérente

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-16 | Création | Tâche créée depuis idée du backlog |
| 2025-11-16 | En cours | Début du travail |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations]

**Difficultés rencontrées :**

- [Problèmes et solutions]

**Améliorations futures :**

- [Idées pour aller plus loin]
