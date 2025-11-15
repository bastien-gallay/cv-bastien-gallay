# CNT-005: Corriger les dates de début Freelance

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-005 |
| **Titre** | Corriger les dates de début Freelance |
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

Corriger la date de début de l'activité Freelance qui présente un écart de -3 ans avec LinkedIn.

### Contexte

L'audit LinkedIn (CNT-001) a identifié un écart majeur:

- **LinkedIn:** juin 2002 - juin 2004 (2 ans)
- **CV:** 06/1999 - 06/2004 (5 ans)
- **Écart:** -3 ans

Il faut clarifier l'activité de la période 1999-2002 (études? freelance? autre activité?).

**Origine:** Recommandation [CNT-001-R04](../resources/analyses/CNT-001/recommendations-status.md#r04---corriger-les-dates-de-début-freelance) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Clarifier et corriger la période 1999-2004 pour assurer la cohérence et la véracité du parcours professionnel.

---

## Sous-tâches

- [ ] Clarifier l'activité 1999-2002 (études? freelance? autre?)
- [ ] Vérifier si la période 1999-2002 doit apparaître dans le CV
- [ ] Décider de mettre à jour la date à 06/2002 ou de séparer les périodes
- [ ] Modifier [src/cv.typ:169](../../src/cv.typ#L169) en conséquence
- [ ] Compiler le CV avec `just build`
- [ ] Valider la cohérence avec la section Éducation

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**IMPORTANT:** Demander à l'utilisateur de clarifier la période 1999-2002 avant modification.

**Questions à poser:**

1. Quelle était l'activité entre 1999 et 2002?
2. Faut-il maintenir cette période dans le CV ou l'ajuster à 2002-2004?
3. Y avait-il une activité professionnelle pendant les études?

**Outils/commandes à utiliser:**

- `just build` pour compiler après modification

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) (ligne 169)
- Section Éducation pour vérifier les dates d'études

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**À clarifier:** Nature de l'activité entre 1999 et 2002 (études, freelance, autre).

**Documents potentiels:** Relevés URSSAF, déclarations fiscales, contrats.

---

## Références externes

### Fichiers du projet

- [cv.typ:169](../../src/cv.typ#L169) - Date de début Freelance à corriger
- [cv.typ:176-194](../../src/cv.typ#L176-L194) - Section Éducation

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Analyse d'origine

### Ressources

- [Recommandation CNT-001-R04](../resources/analyses/CNT-001/recommendations.md#r04---corriger-les-dates-de-début-freelance)
- LinkedIn: juin 2002 - juin 2004

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(experience): ✏️ correct Freelance start date

- Update start date from 06/1999 to 06/2002
- Align with LinkedIn profile and verified activity
- Clarify period 1999-2002 [add explanation if needed]

Closes CNT-005"
```

**Format suggéré:**

- **Type**: content
- **Scope**: experience
- **Emoji**: ✏️

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Les dates sont cohérentes avec la section Éducation
- [ ] Pas de chevauchement incohérent
- [ ] Le PDF s'affiche correctement

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis recommandation CNT-001-R04 |

---

## Résultat final

[À remplir une fois la tâche terminée]
