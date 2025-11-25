# TPL-003: CV Typst from scratch - Structurations alternatives

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | TPL-003 |
| **Titre** | Créer un CV Typst from scratch pour explorer des structurations alternatives |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | TPL (Template) |
| **Section CV** | General |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 4-6 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Oui |
| **Prérequis** | [TPL-004](./TPL-004-extraction-donnees-structurees.md) |

---

## Description

Créer un ou plusieurs CV Typst from scratch en partant des informations brutes disponibles, afin d'explorer des structurations alternatives de l'information et de la présentation.

### Contexte

Le CV actuel utilise le template `neat-cv` avec une structure classique :

- Sidebar (contact, compétences, langues, intérêts)
- Corps principal (expériences, formation, certifications)

Cette structure est conventionnelle mais pas nécessairement optimale pour tous les contextes. Explorer des alternatives peut révéler de meilleures façons de présenter l'information.

### Objectif

- Extraire les données brutes du CV actuel
- Concevoir 2-3 structures alternatives de présentation
- Implémenter au moins un prototype Typst sans dépendance à `neat-cv`
- Évaluer les avantages/inconvénients de chaque approche
- Potentiellement identifier des améliorations pour le CV principal

---

## Sous-tâches

- [ ] Extraire les données brutes de [cv.typ](../../src/cv.typ) dans un format structuré
- [ ] Analyser les forces et faiblesses de la structure actuelle
- [ ] Rechercher des inspirations de structures CV alternatives
- [ ] Concevoir 2-3 maquettes de structures alternatives (papier/markdown)
- [ ] Choisir 1-2 structures à prototyper
- [ ] Implémenter un prototype Typst from scratch (sans template externe)
- [ ] Comparer visuellement avec le CV actuel
- [ ] Documenter les apprentissages et recommandations
- [ ] (Optionnel) Intégrer les meilleures idées dans le CV principal

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Données sources à extraire :**

1. **Informations personnelles** : nom, titre, contact, réseaux
2. **Expériences** : entreprises, postes, dates, descriptions, accomplissements
3. **Formation** : diplômes, écoles, dates
4. **Compétences** : techniques, soft skills, niveaux
5. **Langues** : niveaux de maîtrise
6. **Certifications** : organismes, dates
7. **Intérêts** : hobbies, activités

**Structures alternatives à explorer :**

1. **CV narratif** : histoire professionnelle plutôt que liste
2. **CV par compétences** : regroupement thématique plutôt que chronologique
3. **CV visuel/infographique** : timeline, graphiques de compétences
4. **CV minimaliste** : essentiel uniquement, 1 page stricte
5. **CV modulaire** : blocs réorganisables selon le contexte

**Approche recommandée :**

```typst
// cv-alt.typ - Structure from scratch
#set page(paper: "a4", margin: (x: 1.5cm, y: 2cm))
#set text(font: "...", size: 10pt)

// Définir ses propres fonctions de mise en page
#let section(title, content) = { ... }
#let experience(data) = { ... }

// Structure alternative
#columns(2)[
  // Approche différente...
]
```

**Fichiers à consulter :**

- [src/cv.typ](../../src/cv.typ) - CV actuel (source de données)
- [dist/cv.pdf](../../dist/cv.pdf) - Rendu actuel pour comparaison

**Fichiers à créer :**

- `experiments/cv-data.typ` ou `.yml` - Données structurées extraites
- `experiments/cv-alt-1.typ` - Premier prototype alternatif
- `experiments/cv-alt-2.typ` - (Optionnel) Second prototype

**Critères d'évaluation :**

- Lisibilité et scannabilité (lecture rapide)
- Hiérarchie de l'information
- Équilibre visuel
- Adaptabilité (facile à personnaliser)
- Impact professionnel

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Questions à considérer :**

- Quelle information doit sauter aux yeux en premier ?
- Comment guider le regard du recruteur ?
- Quelle histoire professionnelle raconter ?
- Quels éléments différenciateurs mettre en avant ?

**Inspirations possibles :**

- CV de designers/créatifs (pour les idées visuelles)
- CV de CTOs/leaders tech (pour le positionnement)
- Tendances CV 2024-2025

**Points d'attention :**

- Garder un rendu professionnel malgré l'expérimentation
- Ne pas sacrifier la lisibilité pour l'originalité
- Tester sur différents écrans et en impression

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - CV actuel à analyser
- [dist/cv.pdf](../../dist/cv.pdf) - Rendu PDF actuel

### Tâches liées

- [TPL-004](./TPL-004-extraction-donnees-structurees.md) - **Prérequis** : données structurées nécessaires
- [TPL-001](./TPL-001-cv-versions.md) - Versions courte/longue (complémentaire)
- [TPL-002](./TPL-002-template-system.md) - Système de templates (alternative : templates existants vs from scratch)

### Ressources

- Typst documentation: <https://typst.app/docs/>
- Typst templates gallery: <https://typst.app/universe/search/?kind=templates&category=cv>
- CV design trends: recherche à effectuer

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "feat(template): 🧪 add CV data extraction for experimentation

Extract raw CV data to structured format.

Refs TPL-003"

git commit -m "feat(template): 🧪 add alternative CV structure prototype

Create cv-alt-1.typ with [description of approach].

Refs TPL-003"
```

### Commit final

```bash
git commit -m "feat(template): 🧪 complete CV structure exploration

- Extracted CV data to structured format
- Created alternative CV prototypes
- Documented learnings and recommendations
- Identified improvements for main CV

Closes TPL-003"
```

**Format suggéré :**

- **Type**: feat
- **Scope**: template
- **Emoji**: 🧪 (expérimentation)

---

## Tests / Vérifications

- [ ] Les données brutes sont correctement extraites
- [ ] Au moins 1 prototype alternatif compile sans erreur
- [ ] Le prototype est visuellement cohérent
- [ ] La comparaison avec le CV actuel est documentée
- [ ] Les recommandations sont claires et actionnables

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée pour explorer des structures CV alternatives |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations]

**Structures explorées :**

- [Description des approches testées]

**Apprentissages clés :**

- [Ce qui fonctionne / ne fonctionne pas]

**Recommandations pour le CV principal :**

- [Améliorations à intégrer]
