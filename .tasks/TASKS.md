# CV Project Tasks

Système de gestion des tâches pour l'évolution du CV Typst.

## À propos

Ce fichier sert de tableau de bord central pour toutes les tâches liées au projet de CV. Chaque tâche possède un identifiant unique au format `XXX-NNN` (trigramme de catégorie + numéro auto-incrémenté sur 3 chiffres).

Les descriptions détaillées de chaque tâche se trouvent dans le dossier [TASKS/](tasks/).

## Convention d'identifiants

- **Format**: `XXX-NNN` où XXX est le trigramme de catégorie et NNN un numéro de 001 à 999
- **Trigrammes disponibles**:
  - **CNT** (Content) - Contenu, informations du CV
  - **LAY** (Layout) - Mise en page, design, style visuel
  - **QUA** (Quality) - Qualité, vérification, validation
  - **PIP** (Pipeline) - CI/CD, automatisation, build
  - **TPL** (Template) - Templates, structure, architecture
  - **DOC** (Documentation) - Documentation, guides
  - **INF** (Infrastructure) - Infrastructure technique générale
- **NNN**: Numéro auto-incrémenté par trigramme (001, 002, etc.)

## Statuts possibles

- ⏳ **À faire** (Todo)
- 🔄 **En cours** (In Progress)
- ✅ **Terminé** (Done)
- 🚫 **Bloqué** (Blocked)
- 📦 **Archivé** (Archived)

## Priorités

- 🔴 **Haute** (High)
- 🟡 **Moyenne** (Medium)
- 🟢 **Basse** (Low)

---

## Tâches actives

| ID | Titre | Statut | Priorité | Créé le |
|----|-------|--------|----------|---------|
| [CNT-002](tasks/CNT-002-corriger-ecart-critique-upwiser.md) | Corriger l'écart critique sur Upwiser | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-004](tasks/CNT-004-corriger-dates-boonty.md) | Corriger les dates de Boonty | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-005](tasks/CNT-005-corriger-dates-debut-freelance.md) | Corriger les dates de début Freelance | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-006](tasks/CNT-006-ajouter-certifications-manquantes.md) | Ajouter les certifications manquantes | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-007](tasks/CNT-007-corriger-date-safe.md) | Corriger la date SAFe | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-008](tasks/CNT-008-ajouter-experience-ibp.md) | Ajouter l'expérience i-BP | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-009](tasks/CNT-009-ajouter-experience-dekra.md) | Ajouter l'expérience DEKRA | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-010](tasks/CNT-010-ajouter-section-benevolat.md) | Ajouter section Bénévolat | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-011](tasks/CNT-011-corriger-ecarts-mineurs-cdiscount.md) | Corriger écarts mineurs de dates (Cdiscount) | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-012](tasks/CNT-012-corriger-ecarts-mineurs-cast.md) | Corriger écarts mineurs de dates (Cast) | ⏳ À faire | 🔴 Haute | 2025-10-29 |
| [CNT-014](tasks/CNT-014-analyse-experience-palo-it.md) | Analyse expérience PALO IT (journal/tâches CTO) | ⏳ À faire | 🔴 Haute | 2025-11-14 |
| [CNT-015](tasks/CNT-015-analyse-cv-flash.md) | Analyse CV Flash (slide unique) | ⏳ À faire | 🔴 Haute | 2025-11-14 |
| [TPL-001](tasks/TPL-001-cv-versions.md) | Versions courte et longue du CV | ⏳ À faire | 🟡 Moyenne | 2025-10-28 |
| [QUA-001](tasks/QUA-001-verification.md) | Étapes de vérification du CV | ⏳ À faire | 🟡 Moyenne | 2025-10-28 |
| [TPL-002](tasks/TPL-002-template-system.md) | Système de changement de template | ⏳ À faire | 🟢 Basse | 2025-10-28 |
| [PIP-001](tasks/PIP-001-cicd-pipeline.md) | CI/CD pour publication automatique | ⏳ À faire | 🟢 Basse | 2025-10-28 |
| [INF-001](tasks/INF-001-mcp-integration.md) | Améliorer visuellement le CV avec l'aide de Claude | ⏳ À faire | 🟡 Moyenne | 2025-10-28 |

---

## Tâches terminées

| ID | Titre | Statut | Priorité | Terminé le |
|----|-------|--------|----------|------------|
| [CNT-003](tasks/CNT-003-corriger-date-fin-cto-palo-it.md) | Corriger la date de fin CTO chez PALO IT | ✅ Terminé | 🔴 Haute | 2025-11-15 |
| [CNT-013](tasks/CNT-013-analyse-ancien-cv-2019.md) | Analyse ancien CV > 5 ans (2019) | ✅ Terminé | 🔴 Haute | 2025-11-14 |
| [CNT-001](tasks/CNT-001-linkedin-audit.md) | Audit LinkedIn | ✅ Terminé | 🔴 Haute | 2025-11-05 |
| [INF-002](tasks/INF-002-restructurer-sources-pdf-documentation.md) | Restructurer les sources, PDF et documentation | ✅ Terminé | 🔴 Haute | 2025-10-29 |
| [DOC-001](tasks/DOC-001-task-management-automation.md) | Système d'automatisation de gestion des tâches | ✅ Terminé | 🔴 Haute | 2025-10-28 |

Les tâches archivées sont déplacées dans [.archived-tasks/](.archived-tasks/).

---

## Utilisation

### Créer une nouvelle tâche

1. Choisir le trigramme approprié (CNT, TPL, QUA, etc.)
2. Identifier le prochain numéro disponible pour ce trigramme (ex: TPL-003)
3. Copier le template depuis [TASKS/TEMPLATE.md](tasks/TEMPLATE.md)
4. Créer le fichier `TASKS/XXX-NNN-nom-de-la-tache.md`
5. Remplir tous les champs du template
6. Ajouter la ligne correspondante dans ce fichier (section "Tâches actives")

### Travailler sur une tâche

1. Ouvrir le fichier de la tâche dans `TASKS/`
2. Mettre à jour le statut vers "🔄 En cours"
3. Cocher les sous-tâches au fur et à mesure
4. Référencer l'ID de la tâche dans les commits Git: `Refs XXX-NNN`

### Terminer une tâche

1. Marquer toutes les sous-tâches comme complétées
2. Mettre à jour le statut vers "✅ Terminé"
3. Renseigner la date de complétion
4. Faire le commit final avec `Closes XXX-NNN`
5. Déplacer la ligne de ce fichier vers "Tâches terminées"
6. (Optionnel) Archiver le fichier dans `.archived-tasks/`

### Bloquer une tâche

1. Mettre à jour le statut vers "🚫 Bloqué"
2. Documenter la raison du blocage dans la section "Notes"
3. Créer une nouvelle tâche pour résoudre le blocage si nécessaire

---

## Intégration Git

Les tâches sont référencées dans les commits Git selon la convention définie dans [GIT_WORKFLOW.md](GIT_WORKFLOW.md).

**Exemples de commits:**

```bash
# Travail en cours sur une tâche
git commit -m "content(experience): ✏️ update LinkedIn profile details

Refs CNT-001"

# Finalisation d'une tâche
git commit -m "feat(versions): ✨ add short and long CV variants

- Created cv-short.typ (1 page)
- Created cv-long.typ (2+ pages)
- Updated build script

Closes TPL-001"
```

---

## Statistiques

- **Total**: 22 tâches
- **À faire**: 16
- **En cours**: 0
- **Terminées**: 5
- **Bloquées**: 0

**Prochains IDs disponibles par trigramme**:

- CNT-016, TPL-003, QUA-002, PIP-002, INF-003, LAY-001, DOC-002

---

## Références

- [Template de tâche](tasks/TEMPLATE.md)
- [CLAUDE.md](CLAUDE.md) - Instructions pour Claude Code
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Convention de commits
