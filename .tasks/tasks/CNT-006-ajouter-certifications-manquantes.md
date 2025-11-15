# CNT-006: Ajouter les certifications manquantes

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-006 |
| **Titre** | Ajouter les certifications manquantes |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Education |
| **Créé le** | 2025-10-29 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 0.5 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Ajouter deux certifications Scrum.org manquantes dans la section Certifications du CV.

### Contexte

L'audit LinkedIn (CNT-001) a identifié deux certifications présentes sur LinkedIn mais absentes du CV:

1. **Professional Scrum Developer (PSD-I)** - Scrum.org (May 2018)
2. **Scaled Professional Scrum (SPS)** - Scrum.org (Jan 2016)

Ces certifications devraient être insérées après la ligne 232, avant "Professional Scrum with Kanban".

**Origine:** Recommandation [CNT-001-R05](../resources/analyses/CNT-001/recommendations-status.md#r05---ajouter-les-certifications-manquantes) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Compléter la section Certifications avec les certifications manquantes pour refléter fidèlement le parcours de formation.

---

## Sous-tâches

- [ ] Identifier l'emplacement exact dans [src/cv.typ:220-250](../../src/cv.typ#L220-L250)
- [ ] Ajouter Professional Scrum Developer (PSD-I) - May 2018
- [ ] Ajouter Scaled Professional Scrum (SPS) - Jan 2016
- [ ] Vérifier le format et l'alignement avec les autres certifications
- [ ] Compiler le CV avec `just build`
- [ ] Vérifier le rendu dans le PDF (tient sur une page?)

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Ajouter les deux certifications en suivant le format existant des autres certifications Scrum.org. Respecter l'ordre chronologique (plus récent en haut).

**Format attendu:**

```typst
#entry(
  title: [Professional Scrum Developer (PSD-I)],
  date: [2018],
  institution: [Scrum.org],
)

#entry(
  title: [Scaled Professional Scrum (SPS)],
  date: [2016],
  institution: [Scrum.org],
)
```

**Outils/commandes à utiliser:**

- `just build` pour compiler
- Vérifier que le layout de la page n'est pas cassé

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) (lignes 220-250 - section Certifications)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

Vérifier que l'ajout de ces deux certifications ne crée pas de débordement de page.

---

## Références externes

### Fichiers du projet

- [cv.typ:220-250](../../src/cv.typ#L220-L250) - Section Certifications

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Analyse d'origine

### Ressources

- [Recommandation CNT-001-R05](../resources/analyses/CNT-001/recommendations.md#r05---ajouter-les-certifications-manquantes)
- LinkedIn: Professional Scrum Developer (May 2018), Scaled Professional Scrum (Jan 2016)

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(education): ➕ add missing Scrum certifications

- Add Professional Scrum Developer (PSD-I) - May 2018
- Add Scaled Professional Scrum (SPS) - Jan 2016
- Complete certification section identified in LinkedIn audit

Closes CNT-006"
```

**Format suggéré:**

- **Type**: content
- **Scope**: education
- **Emoji**: ➕

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Les certifications sont au bon emplacement
- [ ] Le format est cohérent avec les autres certifications
- [ ] Pas de débordement de page
- [ ] Le PDF s'affiche correctement

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis recommandation CNT-001-R05 |

---

## Résultat final

[À remplir une fois la tâche terminée]
