# CNT-012: Corriger écarts mineurs de dates (Cast)

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-012 |
| **Titre** | Corriger écarts mineurs de dates (Cast) |
| **Statut** | 📦 Archivé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-10-29 |
| **Cible** | - |
| **Terminé le** | 2025-11-15 |
| **Temps estimé** | 0.25 heures |
| **Temps réel** | 0.1 heures |
| **Branche nécessaire** | Auto |

---

## Description

Corriger l'écart mineur de -1 mois sur la date de début de l'expérience Cast pour assurer la cohérence absolue avec LinkedIn.

### Contexte

L'audit LinkedIn (CNT-001) a identifié un écart mineur:

- **LinkedIn:** août 2006
- **CV:** 07/2006
- **Écart:** -1 mois

Bien que négligeable, cette correction améliore la cohérence globale du CV.

**Origine:** Recommandation [CNT-001-R11](../resources/analyses/CNT-001/recommendations-status.md#r11---corriger-écarts-mineurs-de-dates-cast) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Corriger la date de début pour aligner parfaitement le CV avec LinkedIn.

---

## Sous-tâches

- [x] Modifier la date de début de 07/2006 à 08/2006 dans [src/cv.typ:150](../../src/cv.typ#L150)
- [x] Compiler le CV avec `just build`
- [x] Vérifier le rendu dans le PDF

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Correction simple et directe. Mettre à jour le mois de début de juillet à août.

**Outils/commandes à utiliser:**

- `just build` pour compiler

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) (ligne 150)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

Correction mineure mais utile pour la cohérence absolue du CV.

---

## Références externes

### Fichiers du projet

- [cv.typ:150](../../src/cv.typ#L150) - Date de début Cast

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Analyse d'origine

### Ressources

- [Recommandation CNT-001-R11](../resources/analyses/CNT-001/recommendations.md#r11---corriger-écarts-mineurs-de-dates-cast)
- LinkedIn: août 2006

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(experience): ✏️ correct Cast start date

- Update start date from 07/2006 to 08/2006
- Align with LinkedIn profile
- Fix -1 month minor discrepancy

Closes CNT-012"
```

**Format suggéré:**

- **Type**: content
- **Scope**: experience
- **Emoji**: ✏️

---

## Tests / Vérifications

- [x] Le CV compile sans erreur (`just build`)
- [x] Le PDF affiche 08/2006
- [x] La date est cohérente avec le format du CV

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis recommandation CNT-001-R11 |
| 2025-11-15 | En cours | Début du travail (pas de branche) |
| 2025-11-15 | Terminé | Tâche complétée - correction appliquée et vérifiée |
| 2025-11-15 | Archivé | Tâche archivée dans .tasks/.archived/ |

---

## Résultat final

**Ce qui a été réalisé:**

- Correction de la date de début de l'expérience Cast Consulting de 07/2006 à 08/2006
- Alignement parfait avec le profil LinkedIn (août 2006)
- Élimination de l'écart mineur de -1 mois identifié dans l'audit CNT-001
- Vérification du rendu dans le PDF généré

**Difficultés rencontrées:**

Aucune difficulté - correction simple et directe.

**Impact:**

Le CV est maintenant parfaitement cohérent avec LinkedIn pour l'expérience Cast Consulting.
