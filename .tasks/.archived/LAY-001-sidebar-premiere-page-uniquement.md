# LAY-001: Sidebar uniquement sur la première page

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | LAY-001 |
| **Titre** | Réduire la sidebar à la première page uniquement |
| **Statut** | ✅ Terminé |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | LAY (Layout) |
| **Section CV** | Sidebar / Layout |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | 2025-11-26 |
| **Temps estimé** | 2-3 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Modifier la mise en page du CV pour que la sidebar (colonne gauche) n'apparaisse que sur la première page. Les pages suivantes doivent utiliser toute la largeur disponible.

### Contexte

Le CV actuel utilise une mise en page à deux colonnes sur toutes les pages :

- **Colonne gauche (sidebar)** : Contact, langues, compétences, intérêts
- **Colonne droite (main)** : Expériences, formation, certifications

**Observation visuelle (novembre 2025):**

L'analyse du PDF révèle que la sidebar déborde sur la page 2 avec les skills techniques (Python, Java, C#, C, Rust, Management, Développement, Architecture). Ce débordement:

- Crée une incohérence visuelle (sidebar partielle page 2)
- Gaspille de l'espace sur les pages suivantes
- Réduit l'espace disponible pour le contenu principal

Cette structure répétée:

- Réduit l'espace disponible pour le contenu principal
- Crée des espaces vides dans la sidebar sur les pages 2+
- Ne correspond pas aux conventions de CV multi-pages

### Objectif

- Sidebar présente uniquement sur la première page
- Pages 2+ : contenu principal sur toute la largeur
- Transition fluide entre les deux layouts
- Conservation de tout le contenu existant

**Note:** Si des skills doivent être retirés de la sidebar pour tenir sur une page, les conserver dans la version exhaustive (`cv-exhaustive.typ`) pour pouvoir les réutiliser selon les offres.

---

## Sous-tâches

- [x] Analyser la structure actuelle du template `neat-cv`
- [x] Identifier les options de configuration pour le layout multi-pages
- [x] Tester si `neat-cv` supporte nativement ce comportement
- [x] Si non supporté : explorer les alternatives (override, fork, custom)
- [x] Réduire/réorganiser le contenu de la sidebar si nécessaire
- [x] Implémenter le layout différencié page 1 vs pages suivantes
- [x] Vérifier le rendu sur toutes les pages
- [x] Ajuster les espacements et marges si nécessaire

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Analyse du template neat-cv :**

Le template `neat-cv` utilise une structure de sidebar fixe. Il faut vérifier :

1. Si le template offre une option pour désactiver la sidebar après la page 1
2. Si on peut conditionner l'affichage selon le numéro de page
3. Si une modification du template est nécessaire

**Approches possibles :**

1. **Option native neat-cv** (idéal)
   - Chercher dans la documentation si une option existe
   - Paramètre type `sidebar-pages: 1`

2. **Condition sur le numéro de page**

   ```typst
   #let current-page = counter(page).get().first()
   #if current-page == 1 {
     // Layout avec sidebar
   } else {
     // Layout pleine largeur
   }
   ```

3. **Restructuration manuelle**
   - Utiliser `#pagebreak()` explicitement
   - Définir deux layouts différents
   - Page 1 : `#columns(2)` avec proportions
   - Pages 2+ : layout simple

4. **Fork/Override du template**
   - Copier et modifier le template localement
   - Plus de contrôle mais maintenance plus complexe

**Contenu de la sidebar à vérifier :**

S'assurer que tout le contenu de la sidebar tient sur la première page :

- Photo de profil
- Contact
- Réseaux sociaux
- Langues
- Compétences techniques
- Centres d'intérêt

Si trop de contenu, prioriser ou déplacer certains éléments vers le corps principal.

**Fichiers à consulter :**

- [src/cv.typ](../../src/cv.typ) - Structure actuelle
- Documentation neat-cv : <https://typst.app/universe/package/neat-cv>

**Fichiers à modifier :**

- [src/cv.typ](../../src/cv.typ) - Layout principal

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Questions à considérer :**

- Le contenu actuel de la sidebar tient-il sur une seule page ?
- Faut-il réduire ou réorganiser certaines sections ?
- Quel élément déplacer vers le corps si nécessaire ?

**Avantages attendus :**

- Plus d'espace pour les expériences détaillées
- Meilleure lisibilité sur les pages 2+
- Structure plus conventionnelle pour CV multi-pages
- Réduction potentielle du nombre de pages

**Points d'attention :**

- Vérifier que la transition page 1 → page 2 est fluide
- S'assurer que le contenu ne "saute" pas de manière inattendue
- Tester avec différentes quantités de contenu

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - CV actuel
- [dist/cv.pdf](../../dist/cv.pdf) - Rendu actuel

### Tâches liées

- [TPL-001](./TPL-001-cv-versions.md) - Versions courte/longue (impacté par ce changement)
- [TPL-003](./TPL-003-cv-from-scratch-alternatives.md) - Structures alternatives (exploration similaire)

### Ressources

- neat-cv documentation: <https://typst.app/universe/package/neat-cv>
- Typst page counter: <https://typst.app/docs/reference/introspection/counter/>
- Typst layout: <https://typst.app/docs/reference/layout/>

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "style(layout): 🎨 configure sidebar for first page only

Modify CV layout to show sidebar only on page 1.

Refs LAY-001"
```

### Commit final

```bash
git commit -m "style(layout): 🎨 sidebar on first page only

- Configured neat-cv for single-page sidebar
- Adjusted content to fit first page
- Full-width layout on subsequent pages
- Verified multi-page rendering

Closes LAY-001"
```

**Format suggéré :**

- **Type**: style
- **Scope**: layout
- **Emoji**: 🎨 (style/design)

---

## Tests / Vérifications

- [x] La sidebar apparaît uniquement sur la page 1
- [x] Les pages 2+ utilisent toute la largeur
- [x] Tout le contenu de la sidebar est visible sur la page 1
- [x] La transition entre les pages est fluide
- [x] Le CV compile sans erreur
- [x] Le rendu PDF est correct

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée pour optimiser le layout multi-pages |
| 2025-11-26 | Terminé | Réduction des skills de 23 à 12, sidebar tient sur page 1 |

---

## Résultat final

**Ce qui a été fait :**

1. Analyse du template neat-cv : ne supporte pas nativement la sidebar sur page 1 uniquement
2. Création d'un fork local du template (`src/neat-cv-local.typ`) avec nouvelle architecture :
   - `cv-setup()` : Configuration du document
   - `cv-page-one()` : Page 1 avec sidebar + contenu principal
   - `cv-continued()` : Pages 2+ en pleine largeur
3. Restructuration de cv.typ pour utiliser cette nouvelle architecture
4. Réduction de la liste des skills de 23 à 12 éléments

**Approche retenue :**

- Fork local du template neat-cv avec séparation explicite page 1 / pages 2+
- Utilisation de `#pagebreak()` pour marquer la transition vers le layout pleine largeur
- Structure : `cv-setup` → `cv-page-one(sidebar, main)` → `pagebreak` → `cv-continued[...]`

**Fichiers créés/modifiés :**

- `src/neat-cv-local.typ` (nouveau) : Fork local de neat-cv v0.4.0 avec support sidebar page 1 uniquement
- `src/cv.typ` : Restructuré pour utiliser le nouveau template

**Ajustements de contenu :**

Skills retirés :

- BDD, Design Thinking, Management, Architecture
- Scrum, Kanban, React, eXtreme Programming
- Spec Driven Development, Java, C

Skills ajoutés :

- Agile, C#, Rust, Node.js, SQL

Skills conservés :

- Lean, IA, TDD, Clean Code, DDD, TypeScript, Python

**Liste finale (12 skills) :**
Agile, Lean, IA, TDD, Clean Code, DDD, TypeScript, Node.js, Python, C#, Rust, SQL

**Résultat PDF :**

- Page 1 : Sidebar avec photo, contact, langues, expertises + expériences principales
- Pages 2-5 : Pleine largeur (études détails, certifications, bénévolat, expérience détaillée)
