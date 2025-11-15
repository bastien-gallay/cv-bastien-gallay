# CNT-008: Ajouter l'expérience i-BP

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-008 |
| **Titre** | Ajouter l'expérience i-BP |
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

Ajouter l'expérience de Coach Agile chez i-BP (avril 2015 - septembre 2015) qui est présente sur LinkedIn mais absente du CV.

### Contexte

L'audit LinkedIn (CNT-001) a identifié une mission freelance manquante:

- **Poste:** Coach Agile (Freelance)
- **Dates:** avr. 2015 - sept. 2015 (6 mois)
- **Lieu:** Nantes Area, France
- **Description:**
  - Accompagnement de projets Agiles: Décisionnel, Livraison (DevOps)
  - Coaching de la communauté de pratique des équipiers Agiles
  - Participation à des travaux transverses d'organisation
  - Mise en place de Coach Dating
  - Méthodes: Scrum, Kanban, Lean Startup

Cette mission s'inscrit dans la période Upwiser et doit être insérée entre Upwiser et Cdiscount (ordre chronologique).

**Origine:** Recommandation [CNT-001-R07](../resources/analyses/CNT-001/recommendations-status.md#r07---ajouter-lexpérience-i-bp) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Compléter le CV avec cette mission freelance pour refléter fidèlement le parcours professionnel.

---

## Sous-tâches

- [ ] Identifier l'emplacement exact dans le CV (après ligne 135, entre Upwiser et Cdiscount)
- [ ] Créer une entrée `#entry()` avec les informations i-BP
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
  date: [04/2015 - 09/2015],
  institution: [i-BP],
  location: [Nantes],
  description: [
    - Accompagnement de projets Agiles (Décisionnel, DevOps)
    - Coaching de la communauté de pratique Agile
    - Mise en place de Coach Dating
    - Méthodes: Scrum, Kanban, Lean Startup
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

**Note:** Cette mission s'inscrit dans la période Upwiser (oct. 2013 - nov. 2024), il peut être utile de préciser qu'il s'agit d'une mission freelance.

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - Insertion après ligne 135

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Analyse d'origine
- [CNT-002](./CNT-002-corriger-ecart-critique-upwiser.md) - Lié à la période Upwiser

### Ressources

- [Recommandation CNT-001-R07](../resources/analyses/CNT-001/recommendations.md#r07---ajouter-lexpérience-i-bp)
- LinkedIn: avr. 2015 - sept. 2015

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(experience): ➕ add i-BP mission

- Add Coach Agile mission at i-BP (04/2015 - 09/2015)
- Include Agile coaching, DevOps, and Lean Startup activities
- Complete experience section identified in LinkedIn audit

Closes CNT-008"
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
- [ ] Pas de débordement de page
- [ ] Le PDF s'affiche correctement

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis recommandation CNT-001-R07 |

---

## Résultat final

[À remplir une fois la tâche terminée]
