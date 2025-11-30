# INF-013: Intégration AskUserQuestion dans les skills

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-013 |
| **Titre** | Intégration de l'outil AskUserQuestion dans les skills |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟢 Basse |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-30 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 2-3 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Intégrer l'outil `AskUserQuestion` de Claude Code dans les skills du projet pour permettre des interactions plus structurées avec l'utilisateur.

### Contexte

L'outil `AskUserQuestion` est une fonctionnalité officielle mais non documentée de Claude Code (depuis v2.0.21). Il permet de poser des questions interactives avec un format structuré :

```json
{
  "question": "string",
  "header": "string (max 12 chars)",
  "multiSelect": boolean,
  "options": ["choice1", "choice2", ...]
}
```

**Limitation actuelle :** L'outil n'est pas disponible en plan mode, uniquement dans les autres modes de conversation.

### Objectif

- Documenter l'utilisation de `AskUserQuestion` dans le projet
- Adapter les workflows pour utiliser cet outil quand disponible
- Prévoir un fallback vers des questions textuelles simples si indisponible

---

## Sous-tâches

- [ ] Documenter le fonctionnement de AskUserQuestion
- [ ] Identifier les workflows qui bénéficieraient de questions interactives
- [ ] Créer un pattern réutilisable pour les skills (avec fallback)
- [ ] Adapter le workflow job-cv pour l'utiliser
- [ ] Tester dans différents contextes (normal, plan mode)
- [ ] Surveiller la documentation officielle pour updates

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Comportement souhaité :**

1. En mode normal : utiliser `AskUserQuestion` pour les choix structurés
2. En plan mode : poser les questions en texte (fallback)
3. Détecter automatiquement le contexte si possible

**Patterns d'utilisation :**

```markdown
## Question interactive (si AskUserQuestion disponible)

Poser une question avec ces paramètres:
- question: "Quel format de CV souhaitez-vous ?"
- header: "Format CV"
- multiSelect: false
- options: ["Court (1 page)", "Long (2+ pages)", "Auto (selon le poste)"]

## Fallback (si indisponible)

Quel format de CV souhaitez-vous ?
1. Court (1 page)
2. Long (2+ pages)
3. Auto (selon le poste)

Répondez par le numéro ou le nom de l'option.
```

**Fichiers à modifier :**

- `.claude/skills/job-application/workflows/job-cv.md`
- `.claude/skills/task-management/workflows/` (si pertinent)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Situation actuelle (2025-11-30) :**

- L'outil existe mais n'est pas documenté officiellement
- Issue GitHub #10346 demande la documentation
- Le projet `severity1/claude-code-prompt-improver` l'utilise avec succès

**À surveiller :**

- Documentation officielle Claude Code
- Changelog des nouvelles versions
- Issue #10346 pour updates

---

## Références externes

### Ressources

- [GitHub Issue #10346](https://github.com/anthropics/claude-code/issues/10346) - Demande de documentation
- [claude-code-prompt-improver](https://github.com/severity1/claude-code-prompt-improver) - Exemple d'utilisation

### Tâches liées

- [INF-012](./INF-012-skill-cv-adapte.md) - Skill qui bénéficierait de cette fonctionnalité

---

## Commits Git associés

### Commit final

```bash
git commit -m "feat(skills): add AskUserQuestion integration pattern

- Document AskUserQuestion usage
- Add fallback for plan mode
- Update job-cv workflow

Closes INF-013"
```

---

## Tests / Vérifications

- [ ] AskUserQuestion fonctionne en mode normal
- [ ] Le fallback fonctionne en plan mode
- [ ] Les workflows sont clairs et documentés
- [ ] Pattern réutilisable pour d'autres skills

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-30 | Création | Tâche créée suite à erreur en plan mode |

---

## Résultat final

[À remplir une fois la tâche terminée]
