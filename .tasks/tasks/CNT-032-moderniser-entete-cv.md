# CNT-032: Moderniser l'en-tête du CV

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-032 |
| **Titre** | Moderniser l'en-tête du CV (titre poste + coordonnées) |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT (Content) |
| **Section CV** | Header |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 30 min |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Optimiser l'en-tête du CV pour maximiser l'impact et la compatibilité ATS.

### Contexte

**Audit novembre 2025:**

Le titre actuel "Crafting Technology Officer" est original mais risqué:

- Les ATS (logiciels de tri automatique) ne reconnaissent pas ce titre
- Peut créer de la confusion chez les recruteurs
- L'adresse complète avec rue est superflue pour un CV

### Objectif

- Titre de poste optimisé pour ATS et impact humain
- Coordonnées simplifiées
- Conserver l'originalité tout en restant professionnel

---

## Sous-tâches

- [ ] Modifier le titre de "Crafting Technology Officer" vers "Chief Technology Officer (CTO) | IA & Transformation Agile"
- [ ] Simplifier l'adresse: "Bordeaux, France" (supprimer la rue)
- [ ] Vérifier que le titre reste cohérent avec le reste du CV
- [ ] Compiler et vérifier le rendu

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Modification du titre:**

Dans `src/cv.typ`, chercher la ligne avec le titre actuel et remplacer:

```typst
// Avant
position: "Crafting Technology Officer · 25 ans d'expérience en développement logiciel"

// Après
position: "Chief Technology Officer (CTO) | IA & Transformation Agile"
```

**Modification de l'adresse:**

```typst
// Avant
address: "17 rue du Petit Goave, 33000 Bordeaux, France"

// Après
address: "Bordeaux, France"
```

**Alternative conservant l'originalité:**

Si l'utilisateur souhaite garder une touche distinctive:

- "CTO & Technical Leader | IA, Cloud, Craftsmanship"
- "Chief Technology Officer | Expert IA Générative & Agilité"

**Fichiers à modifier:**

- [src/cv.typ](../../src/cv.typ) - Configuration en-tête (lignes ~10-15)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Avantages du changement:**

- Meilleure détection par les ATS (Applicant Tracking Systems)
- Clarté immédiate pour les recruteurs
- Les mots-clés "CTO", "IA", "Transformation" sont très recherchés

**Points d'attention:**

- Garder les 25 ans d'expérience? → Peut être déplacé dans "À propos"
- Conserver l'adresse complète dans cv-exhaustive.typ

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - En-tête du CV

### Tâches liées

- [CNT-033](./CNT-033-ameliorer-section-a-propos.md) - Améliorer "À propos" (complémentaire)

### Ressources

- Audit CV novembre 2025

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(header): ✏️ modernize CV header for ATS

- Changed title to 'CTO | IA & Transformation Agile'
- Simplified address to 'Bordeaux, France'

Closes CNT-032"
```

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur
- [ ] Le titre est lisible et professionnel
- [ ] L'adresse est simplifiée
- [ ] Le rendu PDF est correct

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée suite à audit CV |

---

## Résultat final

[À remplir une fois la tâche terminée]
