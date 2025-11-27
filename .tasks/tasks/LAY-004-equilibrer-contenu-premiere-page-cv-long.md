# LAY-004: Équilibrer le contenu de la première page du CV long

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | LAY-004 |
| **Titre** | Équilibrer le contenu de la première page du CV long |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | LAY |
| **Section CV** | General |
| **Créé le** | 2025-11-27 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 1 heure |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

### Contexte

Dans la version longue du CV (`cv.typ`), la première page présente un déséquilibre visuel : la colonne de droite (contenu principal) se termine avec un espace blanc important en bas de page, créant une impression de vide.

### Objectif

Améliorer l'équilibre visuel de la première page en :

- Aérant le contenu existant (espacement vertical)
- Ajoutant du texte descriptif si pertinent
- Augmentant légèrement la taille de police si approprié
- Redistribuant le contenu pour remplir harmonieusement l'espace

---

## Sous-tâches

- [ ] Analyser visuellement le PDF actuel pour identifier l'étendue du problème
- [ ] Identifier les options d'amélioration (espacement, contenu, police)
- [ ] Implémenter les ajustements dans `cv.typ`
- [ ] Vérifier que le changement n'impacte pas négativement les pages suivantes
- [ ] Compiler et valider visuellement le résultat

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Lors du travail sur cette tâche :

1. **Analyser le PDF actuel** : Lire `dist/cv.pdf` pour évaluer le déséquilibre
2. **Privilégier les solutions non-destructives** : Préférer aérer plutôt qu'ajouter du contenu artificiel
3. **Respecter la cohérence** : Les changements doivent s'intégrer naturellement au style existant

**Options à explorer :**

- Augmenter les `#v()` entre les entrées d'expérience
- Enrichir les descriptions d'expérience avec plus de détails
- Ajuster `font-size` dans la configuration du template
- Revoir la répartition du contenu entre les pages

**Outils/commandes à utiliser :**

- `just build` - Compiler le CV
- `just validate` - Vérifier la compilation

**Fichiers à consulter :**

- [cv.typ](../../src/cv.typ) - Source du CV long
- [dist/cv.pdf](../../dist/cv.pdf) - PDF généré

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Points d'attention :**

- Ne pas surcharger le contenu juste pour remplir l'espace
- Vérifier l'impact sur la pagination globale (nombre de pages total)
- S'assurer que la version courte (`cv-short.typ`) n'est pas affectée

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - Source principale
- [cv-short.typ](../../src/cv-short.typ) - Version courte (pour comparaison)

### Tâches liées

- [LAY-001](./LAY-001-sidebar-premiere-page-uniquement.md) - Sidebar première page uniquement
- [LAY-002](./LAY-002-consolidation-sections-dupliquees.md) - Consolidation sections dupliquées
- [LAY-003](./LAY-003-reorganiser-competences-3-poles.md) - Réorganiser compétences

---

## Commits Git associés

### Commit final

```bash
git commit -m "style(layout): ✨ balance first page content in long CV

- Adjust vertical spacing between entries
- [Other changes]

Closes LAY-004"
```

**Format suggéré :**

- **Type**: style
- **Scope**: layout
- **Emoji**: ✨ (amélioration)

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le PDF s'affiche correctement
- [ ] La première page est visuellement équilibrée
- [ ] Les pages suivantes ne sont pas négativement impactées
- [ ] La version courte n'est pas affectée

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-27 | Création | Tâche créée |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations]

**Difficultés rencontrées :**

- [Problèmes et solutions]

**Améliorations futures :**

- [Idées pour aller plus loin]
