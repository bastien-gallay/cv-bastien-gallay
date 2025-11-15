# CNT-009: Ajouter l'expérience DEKRA

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-009 |
| **Titre** | Ajouter l'expérience DEKRA |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-10-29 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 0.5 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Ajouter l'expérience de Coach Agile chez DEKRA (octobre 2013 - janvier 2015) qui est présente sur LinkedIn mais absente du CV.

### Contexte

L'audit LinkedIn (CNT-001) a identifié une mission freelance manquante:

- **Poste:** Coach Agile (Freelance)
- **Dates:** oct. 2013 - janv. 2015 (1 an 4 mois)
- **Lieu:** Bordeaux Area, France
- **Description:**
  - Scrum Mastering pour le projet de refonte logiciel interne
  - Mise en place des feature teams, coordination multi-équipes
  - Coaching et formation des nouveaux Scrum Masters
  - Accompagnement à l'adoption de bonnes pratiques

Cette mission démarre juste après le début d'Upwiser (oct. 2013). Il faut clarifier le lien entre les deux (mission freelance parallèle?).

**Origine:** Recommandation [CNT-001-R08](../resources/analyses/CNT-001/recommendations-status.md#r08---ajouter-lexpérience-dekra) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Compléter le CV avec cette mission freelance significative (1 an 4 mois) pour refléter fidèlement le parcours professionnel.

---

## Sous-tâches

- [ ] Clarifier le lien entre DEKRA et Upwiser (mission freelance parallèle?)
- [ ] Identifier l'emplacement exact dans le CV (après ligne 135, entre Upwiser et Cdiscount)
- [ ] Créer une entrée `#entry()` avec les informations DEKRA
- [ ] Rédiger une description concise basée sur les points LinkedIn
- [ ] Vérifier que l'insertion ne casse pas le layout
- [ ] Compiler le CV avec `just build`
- [ ] Vérifier le rendu dans le PDF

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Ajouter l'expérience en suivant le format existant des autres expériences professionnelles.

**Format attendu:**

```typst
#entry(
  title: [Coach Agile],
  date: [10/2013 - 01/2015],
  institution: [DEKRA],
  location: [Bordeaux],
  description: [
    - Scrum Master pour projet de refonte logiciel interne
    - Mise en place de feature teams et coordination multi-équipes
    - Coaching et formation des nouveaux Scrum Masters
    - Accompagnement à l'adoption de bonnes pratiques Agile
  ]
)
```

**Outils/commandes à utiliser:**

- `just build` pour compiler
- Vérifier le positionnement chronologique

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) (insertion après ligne 135)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Note:** Cette mission démarre en même temps qu'Upwiser (oct. 2013). Clarifier s'il s'agit d'une mission freelance parallèle ou si Upwiser était la structure juridique pour ces missions.

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - Insertion après ligne 135

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Analyse d'origine
- [CNT-002](./CNT-002-corriger-ecart-critique-upwiser.md) - Lié à la période Upwiser

### Ressources

- [Recommandation CNT-001-R08](../resources/analyses/CNT-001/recommendations.md#r08---ajouter-lexpérience-dekra)
- LinkedIn: oct. 2013 - janv. 2015

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(experience): ➕ add DEKRA mission

- Add Coach Agile mission at DEKRA (10/2013 - 01/2015)
- Include Scrum Master, feature teams, and coaching activities
- Complete experience section identified in LinkedIn audit

Closes CNT-009"
```

**Format suggéré:**

- **Type**: content
- **Scope**: experience
- **Emoji**: ➕

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] L'expérience est bien positionnée chronologiquement
- [ ] Le format est cohérent avec les autres expériences
- [ ] La relation avec Upwiser est claire
- [ ] Pas de débordement de page
- [ ] Le PDF s'affiche correctement

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis recommandation CNT-001-R08 |

---

## Résultat final

[À remplir une fois la tâche terminée]
