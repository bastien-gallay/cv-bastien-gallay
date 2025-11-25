# CNT-010: Ajouter section Bénévolat

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-010 |
| **Titre** | Ajouter section Bénévolat |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | General |
| **Créé le** | 2025-10-29 |
| **Cible** | - |
| **Terminé le** | 2025-11-25 |
| **Temps estimé** | 1.0 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Créer une nouvelle section "Bénévolat" dans le CV pour mettre en valeur l'engagement communautaire et associatif.

### Contexte

L'audit LinkedIn (CNT-001) a identifié plusieurs activités bénévoles importantes qui ne sont pas présentes dans le CV:

1. **Agile Tour Bordeaux** - 2011-aujourd'hui (fusionner les 2 entrées LinkedIn)
2. **Lean Startup Bordeaux** - 2012-2018 (déjà mentionné dans Upwiser, créer section dédiée)
3. **Collectif Quinconces** - 2016-2018

Cette nouvelle section devrait être insérée après la section Certifications, avant "Expérience détaillée".

**Origine:** Recommandation [CNT-001-R09](../resources/analyses/CNT-001/recommendations-status.md#r09---ajouter-section-bénévolat) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)

### Objectif

Créer une section Bénévolat complète qui valorise l'engagement communautaire dans l'écosystème Agile et tech.

---

## Sous-tâches

- [x] Déterminer l'emplacement exact (après ligne 250)
- [x] Créer la structure de la nouvelle section
- [x] Ajouter Agile Tour Bordeaux (2011-aujourd'hui)
- [x] Ajouter Lean Startup Bordeaux (2012-2018)
- [x] Ajouter Collectif Quinconces (2016-2018)
- [x] Vérifier le format et l'alignement avec le reste du CV
- [x] Compiler le CV avec `just build`
- [x] Vérifier que le layout reste sur 2 pages
- [x] Vérifier le rendu dans le PDF

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Créer une nouvelle section en suivant le format des autres sections du CV (Experience, Education, etc.).

**Format suggéré:**

```typst
== Bénévolat

#entry(
  title: [Agile Tour Bordeaux],
  date: [2011 - Aujourd'hui],
  institution: [Organisateur],
  location: [Bordeaux],
  description: [
    - Organisation de la conférence annuelle Agile Tour
    - Coordination des speakers et du programme
    - Animation de la communauté Agile locale
  ]
)

#entry(
  title: [Lean Startup Bordeaux],
  date: [2012 - 2018],
  institution: [Co-fondateur],
  location: [Bordeaux],
  description: [
    - Animation de meetups réguliers sur le Lean Startup
    - Coaching de startups et entrepreneurs
  ]
)

#entry(
  title: [Collectif Quinconces],
  date: [2016 - 2018],
  institution: [Membre actif],
  location: [Bordeaux],
  description: [
    - Participation aux activités du collectif
  ]
)
```

**Outils/commandes à utiliser:**

- `just build` pour compiler
- Vérifier que le CV reste sur 2 pages

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) (insertion après ligne 250)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Important:** Cette section valorise votre engagement dans la communauté Agile/tech de Bordeaux. Elle peut être un atout différenciant.

**Vérifier:** Que le CV reste sur 2 pages après l'ajout de cette section.

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - Insertion après ligne 250

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Analyse d'origine

### Ressources

- [Recommandation CNT-001-R09](../resources/analyses/CNT-001/recommendations.md#r09---ajouter-section-bénévolat)
- LinkedIn: Agile Tour Bordeaux, Lean Startup Bordeaux, Collectif Quinconces

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(general): ➕ add volunteer section

- Create new Bénévolat section
- Add Agile Tour Bordeaux (2011-present)
- Add Lean Startup Bordeaux (2012-2018)
- Add Collectif Quinconces (2016-2018)
- Highlight community engagement

Closes CNT-010"
```

**Format suggéré:**

- **Type**: content
- **Scope**: general
- **Emoji**: ➕

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] La section est bien positionnée
- [ ] Le format est cohérent avec les autres sections
- [ ] Le CV reste sur 2 pages
- [ ] Le PDF s'affiche correctement
- [ ] Les dates sont cohérentes

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-29 | Création | Tâche créée depuis recommandation CNT-001-R09 |

---

## Résultat final

[À remplir une fois la tâche terminée]
