# CNT-004: Corriger les dates de Boonty

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-004 |
| **Titre** | Corriger les dates de Boonty |
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

Corriger les dates de l'expérience Boonty qui présente un écart de -13 mois au début et -10 mois de durée totale.

### Contexte

L'audit LinkedIn (CNT-001) a révélé un écart significatif:

- **LinkedIn:** juin 2005 - juil. 2006 (1 an 2 mois)
- **CV:** 07/2004 - 07/2006 (2 ans)
- **Écart:** -13 mois de début, -10 mois de durée

Cet écart affecte également les dates de Qualia Services (non présent dans le CV actuel).

**Origine:** Recommandation [CNT-001-R03](../resources/analyses/CNT-001/recommendations-status.md#r03---corriger-les-dates-de-boonty) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Vérifier les contrats de travail et corriger les dates de Boonty pour assurer la cohérence et la véracité du parcours professionnel.

---

## Sous-tâches

- [ ] Vérifier les contrats de travail pour confirmer les dates exactes
- [ ] Clarifier l'activité 2004-2005 (Qualia Services?)
- [ ] Mettre à jour la date de début dans [src/cv.typ:162](../../src/cv.typ#L162)
- [ ] Ajuster la durée si nécessaire
- [ ] Compiler le CV avec `just build`
- [ ] Vérifier la cohérence avec les autres expériences de la période

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**IMPORTANT:** Demander à l'utilisateur de vérifier les contrats de travail pour les dates exactes. L'écart de 13 mois nécessite une confirmation avant modification.

**Question à poser:** Y a-t-il eu une autre expérience (Qualia Services) entre 2004-2005?

**Outils/commandes à utiliser:**

- `just build` pour compiler après modification

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) (ligne 162)
- Contrats de travail Boonty

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Documents à consulter:** Contrats de travail, bulletins de paie de la période 2004-2006

**Note:** Vérifier si Qualia Services (mentionné sur LinkedIn) doit apparaître dans le CV.

---

## Références externes

### Fichiers du projet

- [cv.typ:162](../../src/cv.typ#L162) - Dates Boonty à corriger

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Analyse d'origine

### Ressources

- [Recommandation CNT-001-R03](../resources/analyses/CNT-001/recommendations.md#r03---corriger-les-dates-de-boonty)
- LinkedIn: juin 2005 - juil. 2006

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(experience): ✏️ correct Boonty dates

- Update start date from 07/2004 to 06/2005
- Align duration with LinkedIn and verified contracts
- Fix -13 months discrepancy

Closes CNT-004"
```

**Format suggéré:**

- **Type**: content
- **Scope**: experience
- **Emoji**: ✏️

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Les dates sont cohérentes avec les documents officiels
- [ ] Pas de chevauchement incohérent avec les autres expériences
- [ ] Le PDF s'affiche correctement

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis recommandation CNT-001-R03 |

---

## Résultat final

[À remplir une fois la tâche terminée]
