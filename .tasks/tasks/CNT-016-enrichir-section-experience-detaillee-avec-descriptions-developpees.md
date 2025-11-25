# CNT-016: Enrichir section Expérience détaillée avec descriptions développées

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-016 |
| **Titre** | Enrichir section Expérience détaillée avec descriptions développées |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-11-17 |
| **Cible** | - |
| **Terminé le** | 2025-11-25 |
| **Temps estimé** | 2-3 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Enrichir la section "= Expérience détaillée" (ligne 253 de cv.typ) avec des descriptions beaucoup plus développées et détaillées que celles de la section "= Expérience Professionnelle" de la page 1.

### Contexte

Actuellement, le CV contient deux sections d'expérience :

1. **"= Expérience Professionnelle"** (page 1, lignes 103-172) : Descriptions concises pour un aperçu rapide
2. **"= Expérience détaillée"** (page 2, ligne 253) : Section vide destinée à accueillir des descriptions développées

La section détaillée doit permettre aux recruteurs intéressés d'approfondir leur compréhension du parcours professionnel avec :
- Des accomplissements mesurables et chiffrés
- Des technologies et méthodologies spécifiques
- Des contextes de projets détaillés
- Des résultats business concrets
- Des transformations organisationnelles menées

Cette section sera alimentée par les analyses en cours (CNT-014 pour PALO IT, CNT-015 pour CV Flash) et les tâches d'ajout d'expériences (CNT-008, CNT-009).

### Objectif

Créer une section "= Expérience détaillée" riche et structurée qui :
1. Reprend toutes les expériences de la section principale (page 1)
2. Les enrichit avec des détails concrets et mesurables
3. Valorise les accomplissements et l'impact business
4. Reste lisible et bien structurée (max 2-3 pages pour cette section)

**Priorité sur :**
- PALO IT (CTO + Consultant Senior) : 02/2021 - 08/2025
- Upwiser + missions freelance (i-BP, DEKRA) : 09/2013 - 02/2021

---

## Sous-tâches

- [x] Planifier la structure de la section détaillée (quelles expériences détailler ?)
- [x] Attendre la finalisation de CNT-014 (analyse PALO IT) pour avoir les données
- [x] Enrichir l'expérience PALO IT CTO avec détails de CNT-014
- [x] Enrichir l'expérience PALO IT Consultant Senior avec projets concrets
- [x] Enrichir l'expérience Upwiser avec missions détaillées (i-BP, DEKRA, etc.)
- [x] Ajouter détails CDiscount (technologies, projets, équipes)
- [x] Ajouter détails Cast Consulting (projets clients, domaines métiers)
- [x] Vérifier la cohérence avec la section page 1
- [x] Compiler le CV avec `just build`
- [x] Vérifier le rendu et la pagination (max 3-4 pages au total)

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Cette tâche doit être coordonnée avec les autres tâches CNT en cours, notamment :
- **CNT-014** : Analyse expérience PALO IT (source de données)
- **CNT-015** : Analyse CV Flash (peut fournir des insights)
- **CNT-008/CNT-009** : Ajout i-BP et DEKRA (à intégrer dans section détaillée)

**Format attendu pour chaque expérience détaillée :**

```typst
#entry(
  title: [Titre du poste],
  date: [MM/YYYY - MM/YYYY],
  institution: [Entreprise],
  location: [Ville, Pays],
)[
  === Contexte
  Description du contexte de l'entreprise, du secteur, de l'équipe.

  === Missions principales
  - Mission 1 avec résultats mesurables
  - Mission 2 avec impact business
  - Mission 3 avec technologies utilisées

  === Accomplissements clés
  - Accomplissement 1 (chiffres, ROI, amélioration %)
  - Accomplissement 2 (transformations, équipes, processus)
  - Accomplissement 3 (projets livrés, délais, qualité)

  === Technologies & Méthodologies
  - Technologies : Liste des technologies maîtrisées
  - Méthodologies : Scrum, Kanban, XP, etc.
  - Outils : CI/CD, Cloud, etc.
]
```

**Ordre de priorité pour enrichissement :**

1. **PALO IT CTO** (10/2024 - 08/2025) - Attendre CNT-014
2. **PALO IT Consultant Senior** (02/2021 - 10/2024) - Utiliser CNT-014
3. **Upwiser + missions freelance** (09/2013 - 02/2021) - Intégrer CNT-008, CNT-009
4. **CDiscount** (10/2010 - 10/2013) - Utiliser mémoire + anciennes notes
5. **Cast Consulting** (08/2006 - 09/2010) - Résumé synthétique

**Outils/commandes à utiliser :**

- `just build` pour compiler
- Attendre résultats de `/task-from-analysis --analysis-id=CNT-014`
- Consulter `.tasks/resources/analyses/CNT-014/` quand disponible

**Fichiers à consulter :**

- [cv.typ:253-255](../../src/cv.typ#L253-L255) - Section Expérience détaillée (actuellement vide)
- [cv.typ:103-172](../../src/cv.typ#L103-L172) - Section Expérience Professionnelle (référence)
- CNT-014, CNT-015 (analyses en cours)
- CNT-008, CNT-009 (expériences à ajouter)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Dépendances :**

Cette tâche dépend fortement de :
- **CNT-014** : Analyse PALO IT (données essentielles pour enrichir PALO IT)
- **CNT-008/009** : i-BP et DEKRA (missions freelance à intégrer)

**Ordre de traitement recommandé :**

1. Finaliser CNT-014 (analyse PALO IT)
2. Créer tâches depuis `/task-from-analysis --analysis-id=CNT-014`
3. Commencer CNT-016 en intégrant les résultats de CNT-014
4. Intégrer CNT-008, CNT-009 au fur et à mesure

**Éléments à privilégier :**

- Chiffres et résultats mesurables (ROI, %, temps gagné)
- Transformations organisationnelles (avant/après)
- Taille des équipes managées (de X à Y personnes)
- Projets avec impact business identifiable
- Technologies et méthodologies maîtrisées

**Contrainte de pagination :**

Le CV complet ne doit pas dépasser 3-4 pages au total. Veiller à :
- Prioriser les expériences récentes (PALO IT, Upwiser)
- Synthétiser les expériences anciennes (Cast, Boonty)
- Utiliser un format compact et structuré

---

## Références externes

### Fichiers du projet

- [cv.typ:253-255](../../src/cv.typ#L253-L255) - Section à enrichir
- [cv.typ:103-172](../../src/cv.typ#L103-L172) - Section référence page 1

### Tâches liées

**Dépendances directes :**
- [CNT-014](./CNT-014-analyse-experience-palo-it.md) - Source principale pour PALO IT
- [CNT-015](./CNT-015-analyse-cv-flash.md) - Analyse CV Flash (insights complémentaires)
- [CNT-008](./CNT-008-ajouter-experience-ibp.md) - Mission i-BP à intégrer
- [CNT-009](./CNT-009-ajouter-experience-dekra.md) - Mission DEKRA à intégrer

**Tâches connexes :**
- [CNT-001](./CNT-001-linkedin-audit.md) - Audit LinkedIn (méthodologie)
- [CNT-002](./CNT-002-corriger-ecart-critique-upwiser.md) - Période Upwiser

### Ressources

- [ANALYSES.md](../ANALYSES.md) - Dashboard des analyses
- [Templates d'analyse](../resources/templates/) - Templates utilisés
- Section "= Expérience Professionnelle" comme référence structurelle

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "content(experience): ✏️ enrich detailed experience section (WIP)

Adding detailed descriptions for [experience name].

Refs CNT-016"
```

### Commit final

```bash
git commit -m "content(experience): ✨ add comprehensive detailed experience section

- Enriched PALO IT (CTO + Consultant) with measurable accomplishments
- Enriched Upwiser + freelance missions (i-BP, DEKRA) with details
- Added detailed CDiscount and Cast Consulting experiences
- Structured with Context, Missions, Accomplishments, Technologies
- Integrated insights from CNT-014 and CNT-015 analyses
- Maintained 3-4 pages total length

Closes CNT-016"
```

**Format suggéré :**

- **Type** : content
- **Scope** : experience
- **Emoji** : ✨ (new feature), ✏️ (content update)

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] La section "= Expérience détaillée" est bien structurée
- [ ] Toutes les expériences principales sont détaillées
- [ ] Les accomplissements sont mesurables et concrets
- [ ] Les technologies et méthodologies sont mentionnées
- [ ] La cohérence avec la section page 1 est préservée
- [ ] Le CV total ne dépasse pas 3-4 pages
- [ ] Le PDF s'affiche correctement
- [ ] La mise en page reste professionnelle et lisible

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-17 | Création | Tâche créée pour enrichir section Expérience détaillée |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations]

**Difficultés rencontrées :**

- [Problèmes et solutions]

**Améliorations futures :**

- [Idées pour aller plus loin]
