# CNT-011: Corriger écarts mineurs de dates (Cdiscount)

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-011 |
| **Titre** | Corriger écarts mineurs de dates (Cdiscount) |
| **Statut** | 🔄 En cours |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-10-29 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 0.25 heures |
| **Temps réel** | - |

---

## Description

Corriger l'écart mineur de -1 mois sur la date de fin de l'expérience Cdiscount pour assurer la cohérence absolue avec LinkedIn.

### Contexte

L'audit LinkedIn (CNT-001) a identifié un écart mineur:

- **LinkedIn:** oct. 2013
- **CV:** 09/2013
- **Écart:** -1 mois

Bien que négligeable, cette correction améliore la cohérence globale du CV.

**Origine:** Recommandation [CNT-001-R10](../resources/analyses/CNT-001/recommendations-status.md#r10---corriger-écarts-mineurs-de-dates-cdiscount) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Corriger la date de fin pour aligner parfaitement le CV avec LinkedIn.

---

## Sous-tâches

- [ ] Modifier la date de fin de 09/2013 à 10/2013 dans [src/cv.typ:139](../../src/cv.typ#L139)
- [ ] Compiler le CV avec `just build`
- [ ] Vérifier le rendu dans le PDF

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Correction simple et directe. Mettre à jour le mois de fin de septembre à octobre.

**Outils/commandes à utiliser:**

- `just build` pour compiler

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) (ligne 139)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

Correction mineure mais utile pour la cohérence absolue du CV.

---

## Références externes

### Fichiers du projet

- [cv.typ:139](../../src/cv.typ#L139) - Date de fin Cdiscount

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Analyse d'origine

### Ressources

- [Recommandation CNT-001-R10](../resources/analyses/CNT-001/recommendations.md#r10---corriger-écarts-mineurs-de-dates-cdiscount)
- LinkedIn: oct. 2013

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(experience): ✏️ correct Cdiscount end date

- Update end date from 09/2013 to 10/2013
- Align with LinkedIn profile
- Fix -1 month minor discrepancy

Closes CNT-011"
```

**Format suggéré:**

- **Type**: content
- **Scope**: experience
- **Emoji**: ✏️

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le PDF affiche 10/2013
- [ ] La date est cohérente avec le format du CV

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis recommandation CNT-001-R10 |
| 2025-11-15 | En cours | Début du travail |

---

## Résultat final

[À remplir une fois la tâche terminée]
