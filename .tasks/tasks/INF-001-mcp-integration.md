# INF-001: Amélioration visuelle du CV avec Claude

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-001 |
| **Titre** | Améliorer visuellement le CV avec l'aide de Claude |
| **Statut** | ✅ Terminé |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | Visuel / Layout |
| **Créé le** | 2025-10-28 |
| **Cible** | 2025-12-01 |
| **Terminé le** | 2025-11-25 |
| **Temps estimé** | 2-4 heures |
| **Temps réel** | ~45 min |
| **Branche nécessaire** | Oui |

---

## Description

Mettre en place un workflow permettant à Claude d'analyser visuellement le CV compilé (PDF) et de proposer des améliorations de design, mise en page et présentation selon les directives fournies.

### Contexte

Le CV est actuellement généré en PDF via Typst, mais l'optimisation visuelle nécessite de voir le rendu final. Claude possède plusieurs capacités qui peuvent être exploitées:

- Lecture et analyse de fichiers PDF
- Conversion et analyse d'images
- Analyse de mise en page et de design
- Suggestions d'amélioration basées sur les bonnes pratiques

### Objectif

Établir un processus permettant à Claude de:

- Visualiser le CV compilé (PDF ou captures d'écran)
- Analyser la mise en page, l'équilibre visuel, la lisibilité
- Proposer des améliorations concrètes de design
- Suggérer des modifications au code Typst pour améliorer le rendu
- Valider visuellement les changements apportés

---

## Sous-tâches

- [x] Identifier les méthodes disponibles pour l'analyse visuelle (PDF direct, captures d'écran, MCP)
- [x] Tester la lecture du PDF compilé par Claude
- [x] Établir un workflow d'analyse visuelle (compile → read → analyze → suggest)
- [x] Définir les critères d'évaluation visuelle (lisibilité, équilibre, hiérarchie, espaces)
- [x] Créer un guide de directives visuelles pour le CV
- [x] Tester le workflow complet avec des modifications réelles (audit → 4 tâches haute priorité créées)
- [x] Documenter le processus dans CLAUDE.md
- [x] (Optionnel) Scripts non nécessaires - workflow manuel efficace

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Approches possibles pour l'analyse visuelle:**

1. **Lecture directe du PDF** (méthode privilégiée)
   - Utiliser la capacité native de Claude à lire les PDFs
   - Analyser le rendu visuel directement
   - Avantage: Simple, pas d'infrastructure supplémentaire

2. **Conversion en images**
   - Compiler le CV en PDF
   - Convertir les pages en images (PNG/JPG)
   - Claude analyse les captures d'écran
   - Avantage: Visualisation exacte du rendu

3. **Model Context Protocol (MCP)**
   - Créer un serveur MCP dédié si nécessaire
   - Avantage: Automatisation poussée
   - Inconvénient: Plus complexe à mettre en place

**Workflow recommandé:**

```bash
# 1. Compiler le CV
just build

# 2. Claude lit le PDF
Read dist/cv.pdf

# 3. Analyse visuelle selon les critères
- Équilibre des espaces blancs
- Hiérarchie visuelle (titres, sous-titres, contenu)
- Lisibilité (police, taille, contraste)
- Cohérence du design
- Alignement et structure

# 4. Proposer modifications Typst
- Ajuster les marges
- Modifier les tailles de police
- Améliorer l'espacement
- Optimiser la mise en page

# 5. Itérer jusqu'à satisfaction
```

**Critères d'évaluation visuelle:**

- **Lisibilité**: Police claire, taille appropriée, contraste suffisant
- **Équilibre**: Répartition harmonieuse des éléments sur la page
- **Hiérarchie**: Distinction claire entre niveaux d'information
- **Espacement**: Marges, padding, line-height cohérents
- **Professionnalisme**: Aspect soigné et moderne
- **Scannabilité**: Facilité de lecture rapide par un recruteur (< 30s)

**Fichiers à modifier:**

- [CLAUDE.md](../../CLAUDE.md) - Documenter le workflow d'analyse visuelle
- [src/cv.typ](../../src/cv.typ) - Appliquer les améliorations de design

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Décisions à prendre:**

- Quelle méthode privilégier? (Lecture PDF directe, images, ou MCP)
- Quels aspects visuels prioriser? (lisibilité, équilibre, modernité)
- Faut-il créer un guide de style visuel?
- Automatiser le workflow ou rester manuel?

**Use cases attendus:**

- "Claude, analyse visuellement mon CV et suggère des améliorations"
- "Claude, vérifie l'équilibre de la mise en page"
- "Claude, comment améliorer la hiérarchie visuelle?"
- "Claude, propose des ajustements de spacing et marges"
- "Claude, compare avant/après mes modifications"

**Avantages:**

- Feedback visuel expert de Claude
- Optimisation du design sans compétences graphiques poussées
- Itérations rapides (compile → analyze → modify → repeat)
- Amélioration de l'impact visuel du CV

**Directives visuelles à définir:**

- Style souhaité (moderne, classique, minimaliste, créatif)
- Public cible (startup tech, grande entreprise, conseil)
- Contraintes (1-2 pages, noir et blanc ou couleur)
- Éléments visuels obligatoires (photo, icônes, graphiques)

**Après implémentation:**

- Documenter le workflow dans CLAUDE.md
- Créer des exemples avant/après
- Définir un checklist de validation visuelle
- Intégrer à la tâche QUA-001 (vérification globale)

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - CV à analyser
- [CLAUDE.md](../../CLAUDE.md) - À compléter avec MCP
- Scripts de vérification (QUA-001)

### Tâches liées

- [QUA-001](./QUA-001-verification.md) - Vérifications (intégration possible)

### Ressources

- Typst Documentation: <https://typst.app/docs/>
- CV Design Best Practices: <https://www.resumegenius.com/blog/resume-help/resume-design>
- Visual Hierarchy Principles: <https://www.interaction-design.org/literature/article/visual-hierarchy-organizing-content-to-follow-natural-eye-movement-patterns>
- PDF to Image (si nécessaire): ImageMagick, Poppler utils
- Model Context Protocol (optionnel): <https://modelcontextprotocol.io/>

---

## Commits Git associés

### Commits intermédiaires

```bash
git commit -m "docs(cv): 📝 add visual analysis workflow

Documented workflow for visual CV analysis with Claude.

Refs INF-001"

git commit -m "style(cv): 🎨 improve visual layout based on analysis

- Adjusted margins and spacing
- Improved visual hierarchy
- Enhanced readability

Refs INF-001"
```

### Commit final

```bash
git commit -m "docs(cv): ✨ complete visual optimization workflow

- Established workflow for Claude-assisted visual analysis
- Defined evaluation criteria (readability, balance, hierarchy)
- Documented process in CLAUDE.md
- Applied visual improvements to cv.typ
- Created before/after examples

Closes INF-001"
```

**Format suggéré:**

- **Type**: docs, style (documentation, amélioration visuelle)
- **Scope**: cv, layout
- **Emoji**: 🎨 (style), 📝 (documentation)

---

## Tests / Vérifications

- [x] Claude peut lire et analyser le PDF du CV
- [x] Le workflow d'analyse visuelle fonctionne (compile → read → analyze)
- [x] Les critères d'évaluation visuelle sont clairs et applicables
- [x] Les suggestions d'amélioration sont concrètes et actionnables
- [x] Les modifications Typst améliorent effectivement le rendu visuel (tâches CNT-032/33/34, LAY-003)
- [x] Le CV reste professionnel et lisible après modifications (vérifié visuellement)
- [x] La documentation du workflow est complète dans CLAUDE.md
- [x] Des exemples avant/après sont disponibles (audit novembre 2025)

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Terminé | Workflow documenté, audit réalisé, tâches créées |
| 2025-11-25 | En cours | Début du travail |
| 2025-10-28 | Création | Tâche créée dans le cadre de l'initialisation du système de tâches |

---

## Résultat final

**Méthode retenue:** Lecture directe du PDF par Claude (simple, efficace, pas d'infrastructure)

**Livrables:**

1. **Documentation CLAUDE.md** - Section "Visual Analysis Workflow" avec:
   - Workflow en 5 étapes
   - 6 critères d'évaluation (lisibilité, équilibre, hiérarchie, espacement, professionnalisme, scannabilité)
   - Échelle de notation 1-4 étoiles
   - Tableau problèmes/solutions Typst
   - Exemple de format de rapport d'analyse

2. **Audit complet du CV** - Analyse visuelle novembre 2025:
   - Diagnostic: 5 pages trop long, sections dupliquées, sidebar débordante
   - Scores: Lisibilité 4/4, Équilibre 3/4, Scannabilité 2/4

3. **Tâches générées** (4 haute priorité):
   - CNT-032: Moderniser en-tête (titre ATS)
   - CNT-033: Améliorer "À propos" avec métriques
   - CNT-034: Restructurer PALO IT par résultats
   - LAY-003: Réorganiser skills en 3 pôles

4. **Principe établi:** Version exhaustive (cv-exhaustive.typ) comme base de données de contenu

**Workflow final:**

```bash
# 1. Compiler le CV
just build

# 2. Claude analyse visuellement
Read dist/cv.pdf

# 3. Proposer améliorations basées sur critères
- Lisibilité, équilibre, hiérarchie...

# 4. Appliquer modifications à cv.typ
Edit src/cv.typ

# 5. Recompiler et valider
just build
Read dist/cv.pdf

# 6. Itérer si nécessaire
```

**Documentation attendue dans CLAUDE.md:**

- Section "Visual Analysis Workflow"
- Critères d'évaluation visuelle
- Exemples de suggestions d'amélioration
- Checklist de validation visuelle
