# INF-007: Supprimer les CTA slash commands dans les skills

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-007 |
| **Titre** | Supprimer les call to action vers slash commands dans les skills |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟢 Basse |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 1-2 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Nettoyer les workflows des Claude skills pour supprimer les suggestions de slash commands à la fin de leur exécution.

### Contexte

Certains skills ou workflows affichent des suggestions de type "call to action" à la fin de leur exécution, proposant d'exécuter d'autres slash commands. Ces suggestions :

- Peuvent être obsolètes ou redondantes
- Ajoutent du bruit à la sortie
- Ne sont pas toujours pertinentes selon le contexte
- Peuvent référencer des commandes qui n'existent plus

### Objectif

- Identifier les skills/workflows avec des CTA en fin d'exécution
- Supprimer ou simplifier ces suggestions
- Garder uniquement les informations utiles en sortie
- Assurer une expérience plus propre et concise

---

## Sous-tâches

- [ ] Lister les skills et workflows existants
- [ ] Identifier ceux qui contiennent des CTA vers slash commands
- [ ] Évaluer la pertinence de chaque CTA
- [ ] Supprimer les CTA non essentiels
- [ ] Simplifier les messages de fin d'exécution
- [ ] Tester les workflows modifiés

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Fichiers à examiner :**

- `.claude/skills/task-management/workflows/*.md`
- `.claude/commands/*.md`

**Patterns à rechercher :**

```markdown
<!-- Exemples de CTA à identifier -->
Prochaines étapes suggérées :
- `/task-start XXX-NNN` pour commencer
- `/task-complete XXX-NNN` pour terminer

Vous pouvez maintenant exécuter :
- `/autre-commande`
```

**Approche recommandée :**

1. Grep pour identifier les patterns de CTA
2. Lire chaque fichier concerné
3. Supprimer les blocs de suggestions
4. Garder les informations de statut essentielles

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Critères de suppression :**

- CTA vers des commandes obsolètes
- Suggestions redondantes avec le contexte
- Propositions systématiques non contextuelles

**À conserver :**

- Messages de confirmation de succès/erreur
- Informations sur ce qui a été fait
- Avertissements importants

---

## Références externes

### Fichiers du projet

- [.claude/skills/task-management/](../../.claude/skills/task-management/) - Skills à examiner
- [.claude/commands/](../../.claude/commands/) - Commandes à examiner

### Tâches liées

- [INF-006](./INF-006-extraire-scripts-tests-hors-claude.md) - Réorganisation .claude/ (contexte similaire)

---

## Commits Git associés

### Commit final

```bash
git commit -m "chore(skills): 🧹 remove CTA slash commands from skill outputs

Clean up workflow outputs by removing unnecessary call-to-action
suggestions at the end of skill executions.

Closes INF-007"
```

**Format suggéré :**

- **Type**: chore
- **Scope**: skills
- **Emoji**: 🧹 (nettoyage)

---

## Tests / Vérifications

- [ ] Les workflows modifiés fonctionnent correctement
- [ ] Les sorties sont plus concises
- [ ] Aucune information essentielle n'a été supprimée
- [ ] Les messages d'erreur sont préservés

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée pour nettoyer les sorties des skills |

---

## Résultat final

[À remplir une fois la tâche terminée]
