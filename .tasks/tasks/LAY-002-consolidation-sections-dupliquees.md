# LAY-002: Consolidation des sections dupliquées

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | LAY-002 |
| **Titre** | Consolider les sections répétées (Études, Expérience) |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | LAY (Layout) |
| **Section CV** | General / Structure |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 2-3 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Réorganiser la structure du CV pour éliminer les sections qui apparaissent deux fois (version résumée + version détaillée).

### Contexte

L'analyse visuelle du CV (novembre 2025) révèle une structure redondante:

**Page 1:**

- "Études" (version résumée, 1 entrée)
- "Expérience Professionnelle" (version résumée)

**Page 2:**

- "Études - Détails" (version complète, 4 entrées)

**Pages 3-5:**

- "Expérience détaillée" (missions complètes)

Cette structure crée:

- De la confusion pour le lecteur
- Un CV plus long que nécessaire
- Une incohérence visuelle entre les pages

### Objectif

- Choisir une stratégie claire: résumé OU détails (pas les deux)
- Simplifier la navigation dans le document
- Réduire le nombre de pages si possible
- Améliorer la cohérence globale

---

## Sous-tâches

- [ ] Analyser le code Typst pour identifier les sections dupliquées
- [ ] Décider de la stratégie: garder résumé ou détails pour chaque section
- [ ] Restructurer la section Études (une seule version)
- [ ] Restructurer la section Expérience (une seule version)
- [ ] Ajuster les `#colbreak()` et `#pagebreak()` si nécessaire
- [ ] Vérifier l'équilibre visuel après modifications
- [ ] Mettre à jour le footer si le nombre de pages change

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Stratégies possibles:**

### Option A: Tout en résumé (CV court)

- Garder uniquement les versions résumées
- Idéal pour version 1-2 pages
- Perd les détails des missions

### Option B: Tout en détails (CV long)

- Garder uniquement les versions détaillées
- Supprimer les résumés de page 1
- Plus cohérent mais plus long

### Option C: Structure conditionnelle

- Créer une variable `#let detailed = true`
- Afficher résumé OU détails selon la variable
- Prépare le terrain pour TPL-001 (versions)

**Recommandation:** Option C, car elle:

- Résout le problème immédiat
- Facilite TPL-001 (versions courte/longue)
- Permet flexibilité future

**Fichiers à modifier:**

- [src/cv.typ](../../src/cv.typ) - Structure principale

**Points d'attention:**

- Préserver tout le contenu (ne pas perdre d'informations)
- Vérifier les références croisées
- Tester compilation après chaque modification

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Questions à considérer:**

- Quel niveau de détail par défaut?
- Les recruteurs lisent-ils au-delà de la page 2?
- Faut-il synchroniser avec TPL-001?

**Synergie avec autres tâches:**

- LAY-001: Sidebar page 1 uniquement
- TPL-001: Versions courte/longue
- Ces 3 tâches pourraient être faites ensemble

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - CV actuel

### Tâches liées

- [LAY-001](./LAY-001-sidebar-premiere-page-uniquement.md) - Sidebar page 1 (complémentaire)
- [TPL-001](./TPL-001-cv-versions.md) - Versions courte/longue (prérequis potentiel)

### Ressources

- Analyse visuelle INF-001 (novembre 2025)

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "refactor(layout): 🔧 consolidate duplicate sections

Merge summary and detailed versions of Études/Expérience.

Refs LAY-002"
```

### Commit final

```bash
git commit -m "refactor(layout): 🔧 remove duplicate CV sections

- Consolidated Études section (summary + details merged)
- Consolidated Expérience section
- Reduced total page count
- Improved document coherence

Closes LAY-002"
```

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur
- [ ] Aucune information n'a été perdue
- [ ] Une seule version de chaque section apparaît
- [ ] L'équilibre visuel est préservé
- [ ] Le nombre de pages est optimal

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée suite à analyse visuelle INF-001 |

---

## Résultat final

[À remplir une fois la tâche terminée]
