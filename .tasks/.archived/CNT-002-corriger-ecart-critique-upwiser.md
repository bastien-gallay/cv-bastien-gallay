# CNT-002: Corriger l'écart critique sur Upwiser

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-002 |
| **Titre** | Corriger l'écart critique sur Upwiser |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-10-29 |
| **Cible** | - |
| **Terminé le** | 2025-11-16 |
| **Temps estimé** | 0.5 heures |
| **Temps réel** | 0.1 heures |
| **Branche nécessaire** | Auto |

---

## Description

Corriger la date de fin de l'expérience Upwiser qui présente un écart critique de +3 ans 10 mois entre LinkedIn et le CV.

### Contexte

L'audit LinkedIn (CNT-001) a révélé un écart majeur sur les dates d'Upwiser:

- **LinkedIn:** oct. 2013 - nov. 2024 (11 ans 2 mois)
- **CV:** 09/2013 - 01/2021 (7 ans 4 mois)
- **Écart:** +3 ans 10 mois

Cette incohérence affecte la crédibilité du CV et doit être clarifiée. Il faut déterminer si Upwiser a continué parallèlement à PALO IT (2021-2024), si c'était une activité à temps partiel, ou quelle est la date réelle de fin.

**Origine:** Recommandation [CNT-001-R01](../resources/analyses/CNT-001/recommendations-status.md#r01---corriger-lécart-critique-sur-upwiser) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Clarifier et corriger la date de fin d'Upwiser dans le CV avec une date vérifiée et cohérente avec la réalité professionnelle.

---

## Sous-tâches

- [x] Vérifier les documents officiels (KBIS, contrats) pour confirmer la date exacte de fin
- [x] Clarifier si Upwiser a continué parallèlement à PALO IT (2021-2024)
- [x] Déterminer si c'était une activité à temps partiel ou un maintien de structure
- [x] Mettre à jour la date dans [src/cv.typ:122](../../src/cv.typ#L122)
- [x] Compiler le CV et vérifier le rendu PDF
- [x] Valider la cohérence avec les autres dates du CV

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**IMPORTANT:** Cette tâche nécessite une clarification avec l'utilisateur avant toute modification du CV. L'écart de près de 4 ans est trop important pour être corrigé sans vérification des sources officielles.

**Outils/commandes à utiliser:**

- `just build` pour compiler le CV après modification
- `git diff` pour visualiser les changements

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) (ligne 122 - expérience Upwiser)
- Documents officiels (KBIS, contrats de travail)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Questions à clarifier avant modification:**

1. Quelle est la date réelle de fin d'Upwiser?
2. Y a-t-il eu une continuation parallèle à PALO IT?
3. S'agit-il d'un maintien de structure juridique vs activité réelle?

**Documents à consulter:** KBIS de la société, contrats de travail, déclarations administratives

---

## Références externes

### Fichiers du projet

- [cv.typ:122](../../src/cv.typ#L122) - Date de fin Upwiser à corriger

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Analyse d'origine

### Ressources

- [Recommandation CNT-001-R01](../resources/analyses/CNT-001/recommendations.md#r01---corriger-lécart-critique-sur-upwiser) - Description complète
- [Statut de la recommandation](../resources/analyses/CNT-001/recommendations-status.md#r01---corriger-lécart-critique-sur-upwiser)
- LinkedIn: oct. 2013 - nov. 2024

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "content(experience): 🔍 investigate Upwiser date discrepancy

Reviewing documents to clarify end date.

Refs CNT-002"
```

### Commit final

```bash
git commit -m "content(experience): ✏️ correct Upwiser end date

- Update end date from 01/2021 to [verified date]
- Align with official documents (KBIS/contracts)
- Resolve critical discrepancy identified in LinkedIn audit

Closes CNT-002"
```

**Format suggéré:**

- **Type**: content
- **Scope**: experience
- **Emoji**: ✏️ (correction de date)

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le PDF s'affiche correctement
- [ ] La date corrigée est cohérente avec les documents officiels
- [ ] Pas de chevauchement incohérent avec PALO IT
- [ ] Les commits suivent la convention

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis recommandation CNT-001-R01 |
| 2025-11-16 | En cours | Début du travail (pas de branche) |
| 2025-11-16 | Terminé | Tâche complétée après clarification utilisateur |

---

## Résultat final

**Ce qui a été fait:**

- Clarification avec l'utilisateur sur la date réelle de fin d'Upwiser
- Confirmation que l'activité a continué en parallèle de PALO IT avec une activité minimale (maintien de structure)
- Décision de garder la date de fin à 02/2021 (activité à temps plein)
- Correction de la date dans le CV de 01/2021 à 02/2021 (src/cv.typ:122)
- Compilation et vérification du CV sans erreur

**Difficultés rencontrées:**

Aucune difficulté - clarification rapide avec l'utilisateur.

**Améliorations futures:**

- Pérenniser le script Python de calcul des priorités (scripts/priority_weight.py) utilisé dans /task-next
- Améliorer l'algorithme de scoring pour les futures évolutions
