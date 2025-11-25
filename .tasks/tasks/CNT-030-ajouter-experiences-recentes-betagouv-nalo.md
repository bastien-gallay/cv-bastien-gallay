# CNT-030: Ajouter expériences récentes Beta.gouv et Nalo

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-030 |
| **Titre** | Ajouter expériences récentes Beta.gouv et Nalo |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-11-25 |
| **Cible** | 2025-11-30 |
| **Terminé le** | - |
| **Temps estimé** | 1h |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Ajouter les deux expériences récentes identifiées dans le CV Flash 2025 mais absentes du CV Typst: Beta.gouv/MonEspaceNis2 et Nalo (Coaching CTO).

### Contexte

L'analyse CNT-024 du CV Flash 2025 a identifié deux expériences majeures totalement absentes du CV actuel:

1. **Beta.gouv / MonEspaceNis2** - Mission Lead Developer dans l'incubateur d'État
2. **Nalo** - Mission Coaching CTO et équipe technique dans une fintech

Ces deux expériences valorisent des compétences de haut niveau (Lead Developer, Coaching CTO) et des environnements prestigieux (startup d'État, fintech).

### Objectif

1. Clarifier les dates exactes de ces missions avec l'utilisateur
2. Ajouter l'entrée Beta.gouv dans la section Expérience Professionnelle
3. Ajouter la mission Nalo (probablement dans la section Upwiser détaillée)

---

## Sous-tâches

- [ ] Clarifier avec l'utilisateur les dates exactes de Beta.gouv
- [ ] Clarifier avec l'utilisateur les dates exactes de Nalo
- [ ] Déterminer le placement optimal (expérience principale ou Upwiser)
- [ ] Ajouter entrée Beta.gouv / MonEspaceNis2 dans cv.typ
- [ ] Ajouter entrée Nalo dans cv.typ
- [ ] Vérifier la compilation du CV
- [ ] Valider le rendu PDF

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Beta.gouv / MonEspaceNis2:**

```typst
#entry(
  title: "Lead Developer",
  date: "[À CLARIFIER]",
  institution: "Beta.gouv - MonEspaceNis2",
  location: "France (Remote)",
)[
  - Création de l'infrastructure technique et de l'architecture applicative.
  - Développement de la plateforme en React / JavaScript / TypeScript.
  - Mise en place d'outils de mesure et de monitoring.
]
```

**Nalo (Coaching CTO):**

Option 1 - Expérience principale:

```typst
#entry(
  title: "Coach Technique CTO",
  date: "[À CLARIFIER]",
  institution: "Nalo",
  location: "Paris, France",
)[
  - Coaching du CTO et de l'équipe technique.
  - Mise en place de pratiques craft et agile.
  - Refonte de l'architecture technique (Python / Django).
]
```

Option 2 - Mission Upwiser (si période 2013-2021):

```typst
==== Mission Nalo - Coach Technique ([dates])
#strong[Client:] Nalo (Fintech), Paris
#strong[Durée:] X mois

- Coaching du CTO et accompagnement de l'équipe technique
- Mise en place de pratiques Software Craftsmanship
- Refonte de l'architecture technique
- #strong[Stack:] Python, Django
```

**Fichiers à modifier:**

- [cv.typ](../../src/cv.typ) - Section Expérience ou Expérience détaillée

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Questions à clarifier:**

1. **Beta.gouv**: Quelles sont les dates exactes? Est-ce une mission récente (2024-2025)?
2. **Nalo**: Est-ce une mission Upwiser (2013-2021) ou une mission plus récente?
3. **MonEspaceNis2**: Y a-t-il des détails supplémentaires sur le projet?

**Points d'attention:**

- Beta.gouv est l'incubateur de services numériques de l'État
- Nalo est une fintech française spécialisée dans l'assurance-vie
- Ces deux expériences valorisent un positionnement technique de haut niveau

**Source:**

- Recommandations CNT-024-R01 et CNT-024-R02 de l'analyse CV Flash 2025

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - CV principal
- [cv-flash-2025-extraction.md](../resources/audits/CNT-024/cv-flash-2025-extraction.md) - Données extraites

### Tâches liées

- [CNT-024](./CNT-024-analyse-cv-flash-2025.md) - Analyse source
- [CNT-027](./CNT-027-ajouter-missions-clients-upwiser-manquantes.md) - Missions Upwiser (si Nalo va là)

### Ressources

- Recommandations: CNT-024-R01, CNT-024-R02

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(experience): ➕ add Beta.gouv and Nalo experiences

- Added Beta.gouv/MonEspaceNis2 Lead Developer role
- Added Nalo CTO coaching mission
- Stack: React/TypeScript (Beta.gouv), Python/Django (Nalo)

From CV Flash 2025 analysis (CNT-024-R01/R02)

Closes CNT-030"
```

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le PDF s'affiche correctement
- [ ] Beta.gouv est visible dans les expériences
- [ ] Nalo est visible (expérience principale ou Upwiser)
- [ ] Les commits suivent la convention

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée depuis CNT-024-R01/R02 |

---

## Résultat final

[À remplir une fois la tâche terminée]
