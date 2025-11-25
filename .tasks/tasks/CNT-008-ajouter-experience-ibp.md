# CNT-008: Ajouter l'expérience i-BP

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-008 |
| **Titre** | Ajouter l'expérience i-BP |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-10-29 |
| **Cible** | - |
| **Terminé le** | 2025-11-25 |
| **Temps estimé** | 0.5 heures |
| **Temps réel** | 0.3 heures |
| **Branche nécessaire** | Auto |

---

## Description

Ajouter la mission i-BP (avril 2015 - septembre 2015) dans la section "= Expérience détaillée" comme mission longue au sein d'Upwiser.

### Contexte

L'audit LinkedIn (CNT-001) a identifié une mission freelance manquante:

- **Poste:** Coach Agile (Freelance via Upwiser)
- **Dates:** avr. 2015 - sept. 2015 (6 mois)
- **Lieu:** Nantes Area, France
- **Description:**
  - Accompagnement de projets Agiles: Décisionnel, Livraison (DevOps)
  - Coaching de la communauté de pratique des équipiers Agiles
  - Participation à des travaux transverses d'organisation
  - Mise en place de Coach Dating
  - Méthodes: Scrum, Kanban, Lean Startup

Cette mission s'inscrit dans la période Upwiser (sept. 2013 - fév. 2021) et doit être ajoutée **uniquement dans la section "= Expérience détaillée"** (ligne 253+) pour enrichir la description d'Upwiser avec des missions concrètes.

**Note:** Cette tâche sera traitée en même temps que CNT-009 (DEKRA) et CNT-016 (enrichissement global).

**Origine:** Recommandation [CNT-001-R07](../resources/analyses/CNT-001/recommendations-status.md#r07---ajouter-lexpérience-i-bp) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Enrichir la section "= Expérience détaillée" avec cette mission freelance i-BP pour illustrer concrètement les activités Upwiser.

---

## Sous-tâches

- [x] Coordonner avec CNT-016 (enrichissement section détaillée)
- [x] Coordonner avec CNT-009 (mission DEKRA, même période Upwiser)
- [x] Identifier l'emplacement exact dans la section "= Expérience détaillée" (ligne 253+)
- [x] Créer une sous-section pour Upwiser avec missions détaillées
- [x] Ajouter la mission i-BP comme entrée détaillée
- [x] Rédiger une description développée basée sur les points LinkedIn
- [x] Compiler le CV avec `just build`
- [x] Vérifier le rendu dans le PDF
- [x] Vérifier que la section ne déborde pas (max 3-4 pages total)

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**IMPORTANT:** Cette mission doit être ajoutée **UNIQUEMENT dans la section "= Expérience détaillée"** (ligne 253+), PAS en page 1.

**Coordination avec autres tâches:**
- Traiter en même temps que CNT-009 (DEKRA, même logique)
- Intégrer dans CNT-016 (enrichissement global de la section détaillée)

**Format attendu (section détaillée):**

```typst
= Expérience détaillée

#entry(
  title: [Gérant & Coach Agile],
  date: [09/2013 - 02/2021],
  institution: [Upwiser],
  location: [Bordeaux, France],
)[
  === Contexte
  Création de ma société de conseil en agilité et développement logiciel...

  === Missions principales

  ==== Mission i-BP - Coach Agile (avr. 2015 - sept. 2015)
  **Client:** i-BP, Nantes

  - Accompagnement de projets Agiles (Décisionnel, DevOps)
  - Coaching de la communauté de pratique des équipiers Agiles
  - Participation à des travaux transverses d'organisation
  - Mise en place de Coach Dating
  - **Méthodes:** Scrum, Kanban, Lean Startup

  ==== Mission DEKRA - Coach Agile (oct. 2013 - janv. 2015)
  [À ajouter via CNT-009]

  === Autres activités Upwiser
  - Animation de formations et ateliers
  - Accompagnement de ~100 startups et PME
  - Création du cercle Lean Startup Bordeaux
  ...
]
```

**Outils/commandes à utiliser:**

- `just build` pour compiler
- Traiter après CNT-014 (analyse PALO IT)

**Fichiers à consulter:**

- [cv.typ:253+](../../src/cv.typ#L253) - Section "= Expérience détaillée"
- [CNT-016](./CNT-016-enrichir-section-experience-detaillee-avec-descriptions-developpees.md) - Tâche parente

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
