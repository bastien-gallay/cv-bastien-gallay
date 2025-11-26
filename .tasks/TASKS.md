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

| ID | Titre | Statut | Priorité | Score | Créé le |
|----|-------|--------|----------|-------|---------|
| [CNT-035](tasks/CNT-035-ajouter-mission-fircosoft.md) | Ajouter la mission Fircosoft (LexisNexis) | ⏳ À faire | 🟡 Moyenne | - | 2025-11-25 |
| [TPL-004](tasks/TPL-004-extraction-donnees-structurees.md) | Extraire les données du CV (prérequis TPL-001/002/003) | ⏳ À faire | 🟡 Moyenne | 5.00 | 2025-11-25 |
| [TPL-001](tasks/TPL-001-cv-versions.md) | Versions courte et longue du CV | ⏳ À faire | 🟡 Moyenne | 4.45 | 2025-10-28 |
| [TPL-002](tasks/TPL-002-template-system.md) | Système de changement de template | ⏳ À faire | 🟢 Basse | 2.96 | 2025-10-28 |
| [LAY-001](tasks/LAY-001-sidebar-premiere-page-uniquement.md) | Sidebar uniquement sur la première page | ⏳ À faire | 🟡 Moyenne | 2.50 | 2025-11-25 |
| [LAY-002](tasks/LAY-002-consolidation-sections-dupliquees.md) | Consolider les sections dupliquées (Études, Expérience) | ⏳ À faire | 🟡 Moyenne | 2.50 | 2025-11-25 |
| [LAY-003](tasks/LAY-003-reorganiser-competences-3-poles.md) | Réorganiser compétences en 3 pôles thématiques | ⏳ À faire | 🟡 Moyenne | 2.50 | 2025-11-25 |
| [INF-005](tasks/INF-005-repertoire-ressources-dedie.md) | Répertoire dédié aux ressources d'analyse | ⏳ À faire | 🟡 Moyenne | 2.50 | 2025-11-25 |
| [PIP-003](tasks/PIP-003-build-word-format.md) | Build du CV au format Word | ⏳ À faire | 🟡 Moyenne | 2.50 | 2025-11-25 |
| [PIP-001](tasks/PIP-001-cicd-pipeline.md) | CI/CD pour publication automatique | ⏳ À faire | 🟢 Basse | 2.47 | 2025-10-28 |
| [INF-007](tasks/INF-007-supprimer-cta-slash-commands-skills.md) | Supprimer CTA slash commands dans skills | ⏳ À faire | 🟢 Basse | 2.00 | 2025-11-25 |
| [INF-010](tasks/INF-010-skill-analyse-adequation.md) | Skill analyse adéquation profil-poste | ⏳ À faire | 🟡 Moyenne | 1.67 | 2025-11-25 |
| [INF-009](tasks/INF-009-skill-analyse-offre-emploi.md) | Skill analyse d'offre d'emploi | ⏳ À faire | 🟡 Moyenne | 1.67 | 2025-11-25 |
| [INF-011](tasks/INF-011-skill-lettre-motivation.md) | Skill assistant lettre de motivation | ⏳ À faire | 🟡 Moyenne | 1.67 | 2025-11-25 |
| [INF-006](tasks/INF-006-extraire-scripts-tests-hors-claude.md) | Extraire scripts et tests hors de `.claude/` | ⏳ À faire | 🟡 Moyenne | 1.67 | 2025-11-25 |
| [INF-003](tasks/INF-003-perenniser-ameliorer-script-priorites.md) | Pérenniser et améliorer le script Python de calcul des priorités | ⏳ À faire | 🟢 Basse | 1.45 | 2025-11-16 |
| [INF-012](tasks/INF-012-skill-cv-adapte.md) | Skill CV adapté à l'offre | ⏳ À faire | 🟡 Moyenne | 1.25 | 2025-11-25 |
| [INF-008](tasks/INF-008-architecture-skills-candidature.md) | Architecture système skills candidature | ⏳ À faire | 🟡 Moyenne | 1.25 | 2025-11-25 |
| [TPL-003](tasks/TPL-003-cv-from-scratch-alternatives.md) | CV from scratch - Structurations alternatives | ⏳ À faire | 🟡 Moyenne | 1.25 | 2025-11-25 |

---

## Tâches terminées

| ID | Titre | Statut | Priorité | Terminé le |
|----|-------|--------|----------|------------|
| [QUA-001](tasks/QUA-001-verification.md) | Étapes de vérification du CV | ✅ Terminé | 🟡 Moyenne | 2025-11-26 |
| [CNT-034](tasks/CNT-034-restructurer-experience-palo-it.md) | Restructurer expérience PALO IT par résultats | ✅ Terminé | 🔴 Haute | 2025-11-25 |
| [CNT-033](tasks/CNT-033-ameliorer-section-a-propos.md) | Améliorer section "À propos" avec métriques | ✅ Terminé | 🔴 Haute | 2025-11-25 |
| [CNT-032](tasks/CNT-032-moderniser-entete-cv.md) | Moderniser l'en-tête du CV (titre + adresse) | ✅ Terminé | 🔴 Haute | 2025-11-25 |
| [INF-001](tasks/INF-001-mcp-integration.md) | Améliorer visuellement le CV avec l'aide de Claude | ✅ Terminé | 🟡 Moyenne | 2025-11-25 |

Les tâches archivées sont déplacées dans [.archived/](.archived/).

**Tâches archivées:** 27 tâches

- CNT-031 (2025-11-25)
- CNT-030 (2025-11-25)
- CNT-029 (2025-11-25)
- CNT-028 (2025-11-25)
- CNT-027 (2025-11-25)
- CNT-024 (2025-11-25)
- CNT-023 (2025-11-25)
- CNT-017 (2025-11-25)
- CNT-016 (2025-11-25)
- CNT-015 (2025-11-25)
- CNT-014 (2025-11-25)
- CNT-010 (2025-11-25)
- CNT-009 (2025-11-25)
- CNT-008 (2025-11-25)
- CNT-006 (2025-11-25)
- CNT-005 (2025-11-25)
- CNT-004 (2025-11-16)
- CNT-002 (2025-11-16)
- PIP-002 (2025-11-16)
- INF-004 (2025-11-17)
- CNT-013 (2025-11-14)
- CNT-012 (2025-11-15)
- CNT-011 (2025-11-15)
- CNT-007 (2025-11-15)
- CNT-003 (2025-11-15)
- CNT-001 (2025-11-05)
- INF-002 (2025-10-29)
- DOC-001 (2025-10-28)

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

- **Total**: 51 tâches
- **À faire**: 18
- **En cours**: 0
- **Terminées**: 5
- **Bloquées**: 0
- **Archivées**: 28

**Prochains IDs disponibles par trigramme**:

- CNT-036, TPL-005, QUA-002, PIP-004, INF-013, LAY-004, DOC-002

---

## Références

- [Template de tâche](tasks/TEMPLATE.md)
- [CLAUDE.md](CLAUDE.md) - Instructions pour Claude Code
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Convention de commits
