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

Ajouter la mission DEKRA (octobre 2013 - janvier 2015) dans la section "= Expérience détaillée" comme mission longue au sein d'Upwiser.

### Contexte

L'audit LinkedIn (CNT-001) a identifié une mission freelance manquante:

- **Poste:** Coach Agile (Freelance via Upwiser)
- **Dates:** oct. 2013 - janv. 2015 (1 an 4 mois)
- **Lieu:** Bordeaux Area, France
- **Description:**
  - Scrum Mastering pour le projet de refonte logiciel interne
  - Mise en place des feature teams, coordination multi-équipes
  - Coaching et formation des nouveaux Scrum Masters
  - Accompagnement à l'adoption de bonnes pratiques

Cette mission démarre en même temps qu'Upwiser (oct. 2013) et représente une des premières missions longues de la société. Elle doit être ajoutée **uniquement dans la section "= Expérience détaillée"** (ligne 253+) pour enrichir la description d'Upwiser avec des missions concrètes.

**Note:** Cette tâche sera traitée en même temps que CNT-008 (i-BP) et CNT-016 (enrichissement global).

**Origine:** Recommandation [CNT-001-R08](../resources/analyses/CNT-001/recommendations-status.md#r08---ajouter-lexpérience-dekra) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Enrichir la section "= Expérience détaillée" avec cette mission freelance DEKRA pour illustrer concrètement les activités Upwiser.

---

## Sous-tâches

- [ ] Coordonner avec CNT-016 (enrichissement section détaillée)
- [ ] Coordonner avec CNT-008 (mission i-BP, même période Upwiser)
- [ ] Identifier l'emplacement exact dans la section "= Expérience détaillée" (ligne 253+)
- [ ] Créer une sous-section pour Upwiser avec missions détaillées
- [ ] Ajouter la mission DEKRA comme entrée détaillée
- [ ] Rédiger une description développée basée sur les points LinkedIn
- [ ] Préciser que DEKRA était une des premières missions longues d'Upwiser
- [ ] Compiler le CV avec `just build`
- [ ] Vérifier le rendu dans le PDF
- [ ] Vérifier que la section ne déborde pas (max 3-4 pages total)

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**IMPORTANT:** Cette mission doit être ajoutée **UNIQUEMENT dans la section "= Expérience détaillée"** (ligne 253+), PAS en page 1.

**Coordination avec autres tâches:**
- Traiter en même temps que CNT-008 (i-BP, même logique)
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

  ==== Mission DEKRA - Coach Agile (oct. 2013 - janv. 2015)
  **Client:** DEKRA, Bordeaux
  **Durée:** 1 an 4 mois

  - Scrum Master pour projet de refonte logiciel interne
  - Mise en place de feature teams et coordination multi-équipes
  - Coaching et formation des nouveaux Scrum Masters
  - Accompagnement à l'adoption de bonnes pratiques Agile

  ==== Mission i-BP - Coach Agile (avr. 2015 - sept. 2015)
  [À ajouter via CNT-008]

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
