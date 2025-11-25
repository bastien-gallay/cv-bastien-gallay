# CNT-017: Corriger données critiques expérience PALO IT CTO

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-017 |
| **Titre** | Corriger données critiques expérience PALO IT CTO |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-11-25 |
| **Cible** | 2025-11-30 |
| **Terminé le** | 2025-11-25 |
| **Temps estimé** | 15 minutes |
| **Temps réel** | 0.1 heures |
| **Branche nécessaire** | Auto |

---

## Description

Corriger les données critiques erronées dans la description de l'expérience CTO chez PALO IT : dates et taille de l'équipe.

### Contexte

L'analyse CNT-014 a révélé deux erreurs critiques dans les données de l'expérience CTO PALO IT :
- **Dates** : Le CV affiche "10/2024 - 08/2025" (~10 mois) alors que la période réelle est "11/2021 - 10/2025" (4 ans) → sous-estimation de 3+ ans
- **Taille équipe** : Le CV indique "40+" alors que le chiffre réel est "50 personnes"

Ces erreurs affectent gravement la crédibilité du CV et sous-estiment significativement l'ampleur du rôle.

### Objectif

- Corriger la date de début : 11/2021 (au lieu de 10/2024)
- Corriger la date de fin : 10/2025 (au lieu de 08/2025)
- Corriger la taille de l'équipe : 50 personnes (au lieu de 40+)

---

## Sous-tâches

- [x] Localiser l'entrée expérience PALO IT CTO dans cv.typ (lignes 107-121)
- [x] Corriger la date totale de fin : "08/2025" → "10/2025"
- [x] Corriger la date de fin CTO : "08/2025" → "10/2025"
- [x] Corriger la taille équipe : "40+" → "50"
- [x] Compiler le CV et vérifier l'affichage
- [x] Valider que les dates et chiffres sont cohérents

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Modifications à effectuer dans [cv.typ:107-121](../../src/cv.typ#L107-L121)** :

1. **Date de début** : Remplacer "10/2024" par "11/2021"
2. **Date de fin** : Remplacer "08/2025" par "10/2025"
3. **Taille équipe** : Remplacer "40+" par "50"

**Validation** :
- Vérifier que la durée affichée correspond bien à ~4 ans (nov. 2021 - oct. 2025)
- Vérifier que les chiffres sont cohérents avec les autres expériences

**Outils/commandes à utiliser:**

- `just build` pour compiler et vérifier le PDF

**Fichiers à consulter:**

- [cv.typ:107-121](../../src/cv.typ#L107-L121) - Expérience PALO IT CTO

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Origine des corrections** :
- Analyse CNT-014 basée sur le journal CTO et les données de gestion de tâches
- Recommandations CNT-014-R01 (dates) et CNT-014-R14 (taille équipe)

**Impact** :
- Ces corrections transforment l'expérience d'un court mandat de 10 mois en un rôle CTO de 4 ans
- Augmentation significative de la crédibilité et de l'expertise démontrée

---

## Références externes

### Fichiers du projet

- [cv.typ:107-121](../../src/cv.typ#L107-L121) - Expérience PALO IT CTO actuelle

### Tâches liées

- [CNT-014](./CNT-014-analyse-experience-palo-it.md) - Analyse source (terminée)
- [CNT-018](./CNT-018-ajouter-stack-technique-complete-palo-it-cto.md) - Stack technique (à créer)
- [CNT-019](./CNT-019-ajouter-projets-clients-et-resultats-business-palo-it-cto.md) - Projets clients (à créer)

### Ressources

- [Analyse CNT-014](../resources/analyses/CNT-014/audit-report.md) - Rapport d'analyse complet
- [Recommandations CNT-014](../resources/analyses/CNT-014/recommendations-status.md) - R01, R14

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "content(experience): ✏️ correct PALO IT CTO dates and team size

Refs CNT-017"
```

### Commit final

```bash
git commit -m "content(experience): ✏️ correct critical PALO IT CTO data

- Updated start date: 10/2024 → 11/2021
- Updated end date: 08/2025 → 10/2025
- Updated team size: 40+ → 50

Fixes 3+ years underestimation of CTO role duration.

Closes CNT-017"
```

**Format suggéré:**

- **Type**: content (modification de contenu)
- **Scope**: experience
- **Emoji**: ✏️ (correction de texte)

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Les dates s'affichent correctement dans le PDF
- [ ] La taille de l'équipe est mise à jour (50)
- [ ] La durée totale affichée correspond à ~4 ans
- [ ] Aucune régression sur les autres sections

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée depuis recommandations CNT-014-R01, CNT-014-R14 |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait:**

- [Liste des réalisations]

**Difficultés rencontrées:**

- [Problèmes et solutions]

**Améliorations futures:**

- [Idées pour aller plus loin]
