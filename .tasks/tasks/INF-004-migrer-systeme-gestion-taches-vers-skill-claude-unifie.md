# INF-004: Migrer le système de gestion de tâches vers un Skill Claude unifié

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-004 |
| **Titre** | Migrer le système de gestion de tâches vers un Skill Claude unifié |
| **Statut** | 🔄 En cours |
| **Priorité** | 🔴 Haute |
| **Trigramme** | INF |
| **Section CV** | N/A |
| **Créé le** | 2025-11-16 |
| **Cible** | - |
| **Terminé le** | (à remplir lors de la complétion) |
| **Temps estimé** | 3 heures |
| **Temps réel** | (à remplir après) |
| **Branche nécessaire** | Oui |

---

## Description

Migration complète du système de gestion de tâches depuis des slash commands vers un Skill Claude unifié, avec architecture progressive disclosure, scripts Python déterministes, et configuration centralisée.

### Contexte

Les commandes de gestion de tâches actuelles (slash commands) sont des fichiers markdown volumineux (450-550 lignes chacun) qui mélangent instructions, logique et exemples. Cette approche sature le contexte à chaque invocation et rend la maintenance complexe. De plus, un mix slash commands + skills créerait de la confusion pour l'utilisateur.

### Objectif

Migrer l'ensemble des slash commands /task-* vers un Skill Claude unifié 'task-management' avec architecture progressive disclosure (3 niveaux), scripts Python pour la logique déterministe (WSJF, parsing, Git), et configuration centralisée. Le skill doit être cohérent, maintenable, testable et réutilisable sur d'autres projets.

---

## Sous-tâches

### Session 1 : Architecture + Proof of Concept (task-next)

- [x] Concevoir et valider l'architecture cible du skill avec l'utilisateur
- [x] Créer la structure de base `.claude/skills/task-management/` avec SKILL.md
- [x] Migrer `/task-next` : créer `scripts/algorithms/priority_scorer.py` avec tests unitaires
- [x] Créer le fichier de tests manuels pour `/task-next`
- [x] Tester le workflow complet avec l'utilisateur
- [x] Commit session 1 : architecture + task-next migré

### Session 2 : Commandes principales (create + complete)

- [x] Restructurer `/task-create` : workflow + scripts (id_generator.py, validator.py) avec tests
- [x] Restructurer `/task-complete` : workflow + scripts (dashboard_manager.py, git_operations.py) avec tests
- [x] Mettre à jour le fichier de tests manuels (ajout create + complete)
- [x] Tester le cycle complet : create → start → complete *(reporté à Session 4 - intégration finale)*
- [x] Commit session 2 : create + complete migrés *(2 commits: e39959f + cb53297)*

### Session 3 : Commandes d'analyse et secondaires

- [x] Restructurer `/task-from-analysis` : workflow + scripts (recommendation_parser.py) avec tests *(19 tests, tous passent)*
- [x] Migrer les commandes secondaires (task-start, task-archive, task-validate, analyze-source, task-from-idea)
- [x] Créer la configuration centralisée (config/trigrammes.yml, conventions.yml, paths.yml) *(fait en Session 1)*
- [x] Déplacer les templates vers `templates/` du skill *(documenté, migration physique en Session 4)*
- [ ] Mettre à jour le fichier de tests manuels (couverture complète)
- [x] Commit session 3 : migration complète *(2 commits: 7152ccd + à venir)*

### Session 4 : Tests finaux + Documentation + Cleanup

- [ ] Exécuter la suite complète de tests unitaires Python
- [ ] Dérouler les tests manuels complets avec l'utilisateur
- [ ] Mettre à jour CLAUDE.md avec la documentation du skill
- [ ] Supprimer les anciens slash commands de `.claude/commands/`
- [ ] Valider que tous les workflows fonctionnent end-to-end
- [ ] Commit final : cleanup + documentation

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Approche itérative obligatoire :**

- Travailler par sessions (4 sessions planifiées)
- Interagir avec l'utilisateur à chaque étape importante pour validation
- Ne pas avancer sans validation utilisateur sur l'architecture et les choix de design

**Tests critiques :**

- Créer des tests unitaires Python (pytest) pour CHAQUE script
- Maintenir un fichier `MANUAL_TESTS.md` avec les scénarios de test utilisateur
- Exécuter les tests manuels avec l'utilisateur en fin de chaque session
- Ne jamais passer à la session suivante sans validation des tests

**Commits réguliers :**

- Minimum 1 commit par session (peut être plus si nécessaire)
- Format : `refactor(tasks): ♻️ migrate [composant] to skill (session N)`
- Référencer `Refs INF-004` dans tous les commits

**Architecture cible :**

```text
.claude/skills/task-management/
├── SKILL.md                          # Point d'entrée
├── workflows/                        # Workflows markdown
│   ├── lifecycle/
│   ├── analysis/
│   └── decision/
├── scripts/                          # Scripts Python avec tests
│   ├── core/
│   ├── algorithms/
│   ├── git/
│   └── analysis/
├── templates/                        # Templates réutilisables
├── config/                           # Configuration YAML
└── tests/                            # Tests unitaires + manuels
```

**Outils/commandes à utiliser :**

- Python (uv/uvx) pour les scripts
- pytest pour les tests unitaires
- YAML pour la configuration
- Git pour le versioning par session

**Fichiers à consulter :**

- [.claude/commands/](../../.claude/commands/) - Slash commands actuelles
- [CLAUDE.md](../../CLAUDE.md) - Documentation actuelle du système
- [.tasks/TASK_RULES.md](../TASK_RULES.md) - Règles DoR/DoD

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Points d'attention :**

- Cette migration est une refonte majeure, prendre le temps de bien valider chaque session
- Les tests manuels sont essentiels : prévoir du temps pour les dérouler en fin de session
- Ne pas hésiter à ajuster l'architecture si des problèmes sont identifiés en session 1
- Garder les anciens slash commands jusqu'à validation complète du skill

**Décisions à prendre (session 1) :**

- Validation de l'architecture détaillée du skill
- Choix des bibliothèques Python pour les tests (pytest recommandé)
- Structure exacte des fichiers de configuration YAML

**Bénéfices attendus :**

- Contexte optimisé (chargement progressif)
- Meilleure maintenabilité (séparation responsabilités)
- Scripts testables et fiables
- Système réutilisable sur d'autres projets

---

## Références externes

### Fichiers du projet

- [.claude/commands/](../../.claude/commands/) - Slash commands à migrer
- [CLAUDE.md](../../CLAUDE.md) - Documentation système de tâches
- [.tasks/TASK_RULES.md](../TASK_RULES.md) - Règles DoR/DoD

### Tâches liées

- [PIP-002](./PIP-002-privilegier-questionnaires-interactifs-commandes.md) - Standardisation questionnaires interactifs (terminé)
- [INF-001](./INF-001-mcp-integration.md) - Autre tâche infrastructure

### Ressources

- [Agent Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) - Documentation officielle
- [Claude Cookbooks - Skills](https://github.com/anthropics/claude-cookbooks/tree/main/skills) - Exemples de skills
- [Anthropic Blog - Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - Architecture progressive disclosure

---

## Commits Git associés

### En cours de travail

```bash
# Session 1
git commit -m "refactor(tasks): ♻️ create skill architecture and migrate task-next (session 1)

- Created .claude/skills/task-management/ structure
- Implemented SKILL.md with progressive disclosure
- Migrated /task-next to wsjf_calculator.py with unit tests
- Created MANUAL_TESTS.md for user validation

Refs INF-004"

# Session 2
git commit -m "refactor(tasks): ♻️ migrate task-create and task-complete (session 2)

- Migrated /task-create with id_generator.py and validator.py
- Migrated /task-complete with dashboard_manager.py and git_operations.py
- Added unit tests for all new scripts
- Updated MANUAL_TESTS.md

Refs INF-004"

# Session 3
git commit -m "refactor(tasks): ♻️ migrate analysis commands and config (session 3)

- Migrated /task-from-analysis with recommendation_parser.py
- Migrated secondary commands (start, archive, validate, etc.)
- Created centralized config (YAML files)
- Moved templates to skill structure

Refs INF-004"
```

### Commit final

```bash
git commit -m "refactor(tasks): ♻️ complete migration to unified task-management skill

- All slash commands migrated to skill architecture
- Full test coverage (unit + manual tests validated)
- Updated CLAUDE.md documentation
- Removed legacy slash commands
- System validated end-to-end

Closes INF-004"
```

**Format suggéré :**

- **Type**: refactor (restructuration technique)
- **Scope**: tasks
- **Emoji**: ♻️ (refactoring)

---

## Tests / Vérifications

### Tests unitaires (pytest)

- [ ] `tests/test_wsjf_calculator.py` - Algorithme de priorisation
- [ ] `tests/test_id_generator.py` - Génération IDs uniques
- [ ] `tests/test_validator.py` - Validation DoR/DoD
- [ ] `tests/test_dashboard_manager.py` - Mises à jour TASKS.md
- [ ] `tests/test_git_operations.py` - Opérations Git
- [ ] `tests/test_recommendation_parser.py` - Parsing recommandations

### Tests manuels (MANUAL_TESTS.md)

- [ ] Test complet : création de tâche via skill
- [ ] Test complet : suggestion task-next via skill
- [ ] Test complet : démarrage de tâche via skill
- [ ] Test complet : complétion de tâche via skill
- [ ] Test complet : workflow d'analyse (source → recommandations → tâches)
- [ ] Test complet : validation système

### Validation finale

- [ ] Le skill se charge correctement (progressive disclosure)
- [ ] Tous les workflows fonctionnent end-to-end
- [ ] Les tests unitaires passent à 100%
- [ ] Les tests manuels sont validés par l'utilisateur
- [ ] La documentation (CLAUDE.md) est à jour
- [ ] Les anciens slash commands sont supprimés

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-16 | Création | Tâche créée avec approche par sessions itératives |
| 2025-11-16 | En cours | Début du travail |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations par session]

**Difficultés rencontrées :**

- [Problèmes et solutions]

**Améliorations futures :**

- [Idées pour aller plus loin]
