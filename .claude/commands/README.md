# Commandes Claude pour la Gestion des Tâches

Ce répertoire contient les commandes Claude personnalisées pour automatiser la gestion des tâches du projet CV.

## Vue d'Ensemble

Le système de gestion des tâches est documenté dans [TASK_RULES.md](../.tasks/TASK_RULES.md) et [CLAUDE.md](../CLAUDE.md). Ces commandes automatisent les opérations courantes tout en respectant les règles définies (DoR/DoD).

## Commandes Disponibles

### Commandes Prioritaires

Ces commandes couvrent le cycle de vie complet d'une tâche:

#### `/task-create` - Créer une nouvelle tâche

Crée une nouvelle tâche de manière interactive en respectant le template.

**Utilisation:**

```bash
/task-create [--verbose]
```

**Fonctionnalités:**

- Guide interactif pour collecter toutes les informations
- Auto-génération de l'ID unique (XXX-NNN)
- Création du fichier depuis TEMPLATE.md
- Ajout automatique dans TASKS.md
- Mise à jour des statistiques

**Exemple:**

```bash
/task-create
# → Guide interactif
# → Crée .tasks/tasks/CNT-002-nom-de-la-tache.md
# → Ajoute l'entrée dans TASKS.md
```

[Documentation complète](task-create.md)

---

#### `/task-from-idea` - Créer une tâche depuis une idée

Transforme une idée du backlog [IDEAS.md](../.tasks/IDEAS.md) en tâche concrète.

**Utilisation:**

```bash
/task-from-idea [--verbose]
```

**Fonctionnalités:**

- Liste interactive des idées disponibles
- Pré-remplissage automatique (trigramme, titre, contexte)
- Processus de création guidé
- Suppression automatique de l'idée du backlog
- Traçabilité (lien vers la tâche source)

**Exemple:**

```bash
/task-from-idea
# → Liste les idées du backlog
# → Sélection interactive
# → Création guidée avec pré-remplissage
# → Tâche créée et idée retirée
```

**Note:** Les idées sont ajoutées automatiquement dans [IDEAS.md](../.tasks/IDEAS.md) lorsque vous complétez une tâche avec `/task-complete` et remplissez la section "Améliorations futures".

[Documentation complète](task-from-idea.md)

---

#### `/task-start <ID>` - Démarrer une tâche

Démarre le travail sur une tâche avec setup Git automatique.

**Utilisation:**

```bash
/task-start <ID> [--verbose]
```

**Fonctionnalités:**

- Validation de la DoR
- Mise à jour du statut vers "🔄 En cours"
- Création de la branche Git `task/{ID}-{slug}`
- Commit initial automatique
- Affichage du contexte de travail

**Exemple:**

```bash
/task-start CNT-001
# ou abrégé:
/task-start CNT1
```

[Documentation complète](task-start.md)

---

#### `/task-complete <ID>` - Terminer une tâche

Finalise une tâche avec validation DoD complète.

**Utilisation:**

```bash
/task-complete <ID> [--verbose] [--no-merge]
```

**Fonctionnalités:**

- Validation de la DoD
- Compilation automatique du CV
- Collecte interactive du résultat final
- Génération du commit final avec `Closes {ID}`
- Déplacement dans "Tâches terminées"
- Proposition de merge de la branche

**Exemple:**

```bash
/task-complete TPL1
# → Validation
# → Prompts interactifs
# → Commit final
# → Optionnel: merge dans main
```

[Documentation complète](task-complete.md)

---

### Commandes Secondaires

Ces commandes aident à maintenir et naviguer dans le système de tâches:

#### `/task-validate` - Valider la cohérence du système

Vérifie la cohérence entre fichiers et dashboard.

**Utilisation:**

```bash
/task-validate [--verbose] [--fix]
```

**Fonctionnalités:**

- Validation DoR/DoD de toutes les tâches
- Vérification de la cohérence structurelle
- Recalcul et validation des statistiques
- Détection des IDs en double
- Correction automatique avec `--fix`

**Exemple:**

```bash
/task-validate
# → Rapport de validation

/task-validate --fix
# → Correction automatique des erreurs simples
```

[Documentation complète](task-validate.md)

---

#### `/task-next` - Suggérer la prochaine tâche

Suggère la prochaine tâche selon un modèle "valeur/temps".

**Utilisation:**

```bash
/task-next [--verbose] [--start]
```

**Fonctionnalités:**

- Analyse des tâches "À faire"
- Calcul du ratio valeur/temps pour chaque tâche
- Suggestion intelligente (privilégie les "quick wins")
- Affichage du top 3
- Option `--start` pour démarrer automatiquement

**Principe:** Maximise le ratio valeur/temps en privilégiant les tâches courtes et importantes.

**Exemple:**

```bash
/task-next
# → Suggère la meilleure tâche

/task-next --start
# → Démarre automatiquement la tâche suggérée
```

[Documentation complète](task-next.md)

---

#### `/task-archive <ID>` - Archiver une tâche terminée

Archive une tâche terminée vers `.tasks/.archived/`.

**Utilisation:**

```bash
/task-archive <ID> [--verbose]
```

**Fonctionnalités:**

- Validation que la tâche est terminée
- Mise à jour de l'historique (entrée d'archivage)
- Changement du statut vers "📦 Archivé"
- Déplacement vers `.tasks/.archived/`
- Mise à jour de TASKS.md et statistiques
- Préservation de l'historique Git

**Exemple:**

```bash
/task-archive TPL1
# → Archive .tasks/tasks/TPL-001-*.md vers .tasks/.archived/
# → Retire de TASKS.md
```

[Documentation complète](task-archive.md)

---

### Commandes d'Analyse

Ces commandes permettent d'analyser le CV en comparaison avec des sources externes (LinkedIn, GitHub, etc.) pour identifier des écarts et générer des recommandations:

#### `/analyze-source` - Extraire des données depuis une source externe

Extrait et structure des informations depuis une source externe pour comparaison avec le CV.

**Utilisation:**

```bash
/analyze-source [--task-id=XXX-NNN] [--verbose]
```

**Fonctionnalités:**

- Guide interactif pour sélectionner le type de source (LinkedIn, GitHub, CV externe, Website, Autre)
- Extraction guidée section par section avec templates
- Sauvegarde structurée dans `.tasks/resources/audits/{TASK-ID}/`
- Lien optionnel vers une tâche d'analyse parent
- Support pour LinkedIn, GitHub, CVs externes, sites web personnels

**Sources supportées:**

1. **LinkedIn Profile** - Extrait expériences, éducation, certifications, langues, bénévolat, recommandations
2. **GitHub Profile** - Extrait statistiques, repositories, langages, contributions
3. **CV Externe** - Compare structure et contenu avec un CV PDF/Word externe
4. **Website/Blog** - Extrait informations d'un site personnel
5. **Autre** - Source personnalisée avec template adaptatif

**Exemple:**

```bash
/analyze-source --task-id=CNT-001
# → Choix du type de source: LinkedIn Profile
# → Extraction guidée interactive (10 sections)
# → Sauvegarde dans .tasks/resources/audits/CNT-001/linkedin-profile.md
# → Référence ajoutée à la tâche CNT-001
```

**Note:** Cette commande extrait uniquement les données sources. L'analyse comparative doit être créée manuellement en utilisant `audit-template.md`.

[Documentation complète](analyze-source.md)

---

#### `/task-from-analysis` - Créer des tâches depuis des recommandations

Transforme les recommandations d'une analyse comparative en tâches concrètes.

**Utilisation:**

```bash
/task-from-analysis [--analysis-id=XXX-NNN] [--filter=high|medium|low|all] [--verbose]
```

**Fonctionnalités:**

- Liste les analyses avec recommandations pendantes
- Affiche les recommandations groupées par priorité (🔴🔴, 🔴, 🟡, 🟢)
- Sélection batch: '1,5,6', '1-3,5', 'all', 'high', 'critical', 'medium', 'low'
- Création de tâches avec pré-remplissage depuis les recommandations
- Mise à jour automatique de `recommendations-status.md` avec IDs de tâches
- Synchronisation des statistiques dans `ANALYSES.md`
- Traçabilité complète (recommandation ↔ tâche)

**Workflow:**

1. Sélectionne une analyse (ex: CNT-001 LinkedIn Audit)
2. Affiche les 19 recommandations par priorité
3. Sélectionne les recommandations à traiter (ex: 'high' pour toutes les hautes priorités)
4. Création interactive de chaque tâche avec données pré-remplies
5. Mise à jour automatique des fichiers de suivi
6. Résumé final avec liste des tâches créées

**Exemple:**

```bash
/task-from-analysis --analysis-id=CNT-001 --filter=high

# → Affiche 11 recommandations hautes priorités
# → Sélection: confirmer les 11
# → Création de 11 tâches (CNT-002 à CNT-012)
# → Mise à jour de recommendations-status.md
# → Mise à jour de ANALYSES.md (11/19 recommandations traitées)
# → Résumé final avec prochaines étapes
```

**Priorités:**

- 🔴🔴 **Très Haute** → Tâche 🔴 Haute (critique pour crédibilité)
- 🔴 **Haute** → Tâche 🔴 Haute (important, à traiter rapidement)
- 🟡 **Moyenne** → Tâche 🟡 Moyenne (amélioration souhaitable)
- 🟢 **Basse** → Tâche 🟢 Basse (optionnel, différable)

[Documentation complète](task-from-analysis.md)

---

## Workflow Recommandé

### Créer une Tâche depuis une Idée

```bash
1. /task-from-idea
   → Liste les idées du backlog
   → Sélection interactive
   → Création guidée avec pré-remplissage
   → Tâche créée: DOC-002
   → Idée retirée de IDEAS.md

2. /task-start DOC-002
   → Branche créée: task/DOC-002-nom-tache
   → Statut: "🔄 En cours"
   → Contexte affiché
```

### Créer et Démarrer une Tâche Classique

```bash
1. /task-create
   → Suivre le guide interactif
   → Tâche créée: CNT-002

2. /task-start CNT-002
   → Branche créée: task/CNT-002-nom-tache
   → Statut: "🔄 En cours"
   → Contexte affiché
```

### Travailler sur une Tâche

```bash
# Faire des changements dans le code
# Cocher les sous-tâches au fur et à mesure

git add .
git commit -m "content(experience): ✏️ update profile

Refs CNT-002"

# Continuer jusqu'à ce que toutes les sous-tâches soient terminées
```

### Terminer et Archiver

```bash
1. /task-complete CNT-002
   → Validation DoD
   → Compilation CV
   → Prompts interactifs (dont "Améliorations futures")
   → Si améliorations renseignées: ajout automatique dans IDEAS.md
   → Commit final avec "Closes CNT-002"
   → Tâche déplacée dans "Terminées"

2. (Optionnel) /task-archive CNT-002
   → Archive dans .tasks/.archived/
   → Retire de TASKS.md
```

### Maintenance

```bash
# Vérifier la cohérence du système
/task-validate

# Trouver la prochaine tâche à faire
/task-next

# Ou démarrer directement
/task-next --start
```

### Analyser le CV avec une Source Externe

```bash
1. /task-create
   → Trigramme: CNT
   → Titre: "Audit LinkedIn du CV"
   → Tâche créée: CNT-001

2. /task-start CNT-001
   → Branche créée: task/CNT-001-audit-linkedin-cv

3. /analyze-source --task-id=CNT-001
   → Sélection: LinkedIn Profile
   → Extraction guidée interactive (10 sections)
   → Fichier créé: .tasks/resources/audits/CNT-001/linkedin-profile.md

4. Créer l'analyse comparative (manuel)
   → Utiliser audit-template.md
   → Créer .tasks/resources/analyses/CNT-001/audit-report.md
   → Créer .tasks/resources/analyses/CNT-001/recommendations.md (19 recommandations)
   → Créer .tasks/resources/analyses/CNT-001/recommendations-status.md (suivi)
   → Créer .tasks/resources/analyses/CNT-001/action-plan.md
   → Créer .tasks/resources/analyses/CNT-001/metrics.md

5. /task-complete CNT-001
   → L'analyse est terminée et documentée dans ANALYSES.md

6. /task-from-analysis --analysis-id=CNT-001 --filter=high
   → Sélection: 11 recommandations hautes priorités
   → Création de 11 tâches (CNT-002 à CNT-012)
   → Mise à jour automatique de recommendations-status.md
   → Chaque tâche référence sa recommandation (traçabilité)

7. /task-start CNT-002
   → Travail sur la première recommandation
   → Mise à jour du CV

8. /task-complete CNT-002
   → Recommandation CNT-001-R01 automatiquement marquée comme "✅ Completed"
   → Statistiques dans ANALYSES.md mises à jour

# Répéter pour toutes les recommandations...
```

---

## Options Communes

### Option --verbose

Disponible sur toutes les commandes. Affiche des informations détaillées:

- Étapes intermédiaires
- Validations effectuées
- Contenu des fichiers modifiés
- Commandes Git exécutées

**Exemple:**

```bash
/task-start CNT-001 --verbose
```

### Abréviation des IDs

Toutes les commandes acceptent des IDs abrégés:

- **Format complet:** `CNT-003`
- **Format abrégé:** `CNT3` (sans tiret, sans zéros de tête)

**Exemple:**

```bash
/task-start CNT3      # équivalent à CNT-003
/task-complete TPL1   # équivalent à TPL-001
```

---

## Mode Interactif

Plusieurs commandes adoptent un comportement interactif en cas d'erreur ou de situation ambiguë:

**Exemple:**

```text
⚠️  Warning: La tâche CNT-001 est déjà en cours

Options:
1. Continuer sur cette tâche (afficher le contexte)
2. Redémarrer la tâche (reset le statut)
3. Annuler

Votre choix: _
```

Ce mode aide à gérer les cas limites sans bloquer l'utilisateur.

---

## Fichiers de Référence

- [TASK_RULES.md](../.tasks/TASK_RULES.md) - Règles DoR/DoD et gestion des erreurs
- [TASKS.md](../.tasks/TASKS.md) - Dashboard central des tâches
- [ANALYSES.md](../.tasks/ANALYSES.md) - Dashboard des analyses et audits
- [IDEAS.md](../.tasks/IDEAS.md) - Backlog d'idées d'améliorations futures
- [.tasks/tasks/TEMPLATE.md](../.tasks/tasks/TEMPLATE.md) - Template de tâche
- [.tasks/resources/templates/](../.tasks/resources/templates/) - Templates d'audit et recommandations
- [CLAUDE.md](../CLAUDE.md) - Instructions générales du projet
- [GIT_WORKFLOW.md](../../docs/GIT_WORKFLOW.md) - Conventions Git

---

## Conventions

### Commits

Les commandes respectent les conventions définies dans [GIT_WORKFLOW.md](../../docs/GIT_WORKFLOW.md):

- **Format:** `type(scope): emoji description`
- **Références:** `Refs XXX-NNN` (en cours) ou `Closes XXX-NNN` (final)
- **Emojis:** Selon le type de commit

**Exemple de commit généré:**

```bash
feat(template): ✨ add short and long CV variants

- Created cv-short.typ (1 page)
- Created cv-long.typ (2+ pages)
- Updated build script

Closes TPL-001
```

### Branches Git

Format: `task/{ID}-{slug}`

**Exemples:**

- `task/CNT-001-linkedin-audit`
- `task/TPL-002-template-system`
- `task/DOC-001-task-management-automation`

---

## Améliorations Futures

Commandes potentielles à ajouter:

- `/task-list [--status] [--trigramme]` - Lister les tâches avec filtres
- `/task-show <ID>` - Afficher les détails d'une tâche
- `/task-block <ID> <raison>` - Bloquer une tâche
- `/task-unblock <ID>` - Débloquer une tâche
- `/task-unarchive <ID>` - Restaurer une tâche archivée
- `/task-archive --all` - Archiver toutes les tâches terminées
- `/task-stats` - Statistiques détaillées
- `/task-export` - Exporter en CSV/JSON

---

## Support

Pour toute question ou suggestion d'amélioration:

1. Consulter [TASK_RULES.md](../.tasks/TASK_RULES.md)
2. Consulter [CLAUDE.md](../CLAUDE.md)
3. Créer une nouvelle tâche avec `/task-create` (trigramme DOC)

---

**Version:** 1.2.0
**Dernière mise à jour:** 2025-10-29
