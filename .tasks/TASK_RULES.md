# Règles de Gestion des Tâches

Ce document définit les règles et procédures pour la gestion des tâches dans le projet CV.

## Table des matières

- [Definition of Ready (DoR)](#definition-of-ready-dor)
- [Definition of Done (DoD)](#definition-of-done-dod)
- [Workflow Standard](#workflow-standard)
- [Quality Gates](#quality-gates)
- [Gestion des Erreurs](#gestion-des-erreurs)

---

## Definition of Ready (DoR)

Une tâche est considérée comme "prête à être démarrée" si elle respecte TOUS les critères suivants:

### Critères Obligatoires

- ✓ **Fichier de tâche créé** avec le template complet ([TASKS/TEMPLATE.md](TASKS/TEMPLATE.md))
- ✓ **ID unique et valide** au format `XXX-NNN` (trigramme + numéro à 3 chiffres)
- ✓ **Trigramme approprié** choisi parmi CNT, TPL, QUA, PIP, LAY, DOC, INF
- ✓ **Description claire** avec sections "Contexte" et "Objectif" remplies
- ✓ **Critères d'acceptation** explicites dans "Tests / Vérifications"
- ✓ **Entrée ajoutée** dans [TASKS.md](TASKS.md) section "Tâches actives"
- ✓ **Statistiques mises à jour** dans [TASKS.md](TASKS.md)

### Validation

Avant de démarrer une tâche, vérifier que:

1. Le fichier de tâche existe dans `TASKS/XXX-NNN-*.md`
2. Le statut est "⏳ À faire" (ou "🚫 Bloqué" si on débloque)
3. L'ID n'est pas déjà utilisé par une autre tâche
4. Toutes les sections obligatoires du template sont remplies

### Exceptions

Une tâche peut être démarrée même si tous les critères ne sont pas remplis dans les cas suivants:

- Tâche urgente nécessitant une action immédiate
- Exploration préliminaire pour mieux comprendre le besoin

Dans ces cas, documenter l'exception dans "Notes pour l'utilisateur".

---

## Definition of Done (DoD)

Une tâche est considérée comme "terminée" si elle respecte TOUS les critères suivants:

### Critères de Complétion

- ✓ **Toutes les sous-tâches cochées** dans le fichier de tâche
- ✓ **CV compile sans erreur** (`typst compile cv.typ` réussit)
- ✓ **Modifications vérifiées** dans le PDF généré
- ✓ **Section "Résultat final" complétée** avec détails des réalisations
- ✓ **Dates renseignées** ("Terminé le" et optionnellement "Temps réel")
- ✓ **Commit final créé** avec message formaté et `Closes XXX-NNN`
- ✓ **Statut "✅ Terminé"** dans le fichier de tâche
- ✓ **Entrée déplacée** vers "Tâches terminées" dans [TASKS.md](TASKS.md)
- ✓ **Statistiques actualisées** dans [TASKS.md](TASKS.md)

### Tests de Validation

Avant de considérer une tâche comme terminée, s'assurer que:

**Tests Techniques:**

1. Le CV compile sans erreur ni warning
2. Le PDF s'ouvre et s'affiche correctement
3. Les modifications sont visibles et correctes dans le PDF

**Tests de Qualité:**

1. Le contenu respecte la charte graphique existante
2. Aucune régression n'a été introduite
3. Les autres sections du CV ne sont pas affectées

**Tests Documentaires:**

1. La documentation pertinente a été mise à jour
2. Les commits respectent les conventions ([GIT_WORKFLOW.md](GIT_WORKFLOW.md))
3. Les références de fichiers dans les notes sont à jour

### Exceptions

Une tâche peut être considérée comme terminée même si tous les critères ne sont pas remplis dans les cas suivants:

- Tâche de recherche ou d'exploration sans livrable concret
- Tâche bloquée par une dépendance externe (documenter le blocage)
- Décision de ne pas implémenter (documenter la raison)

Dans ces cas, documenter l'exception dans "Résultat final".

---

## Workflow Standard

### Phase 1: Démarrage d'une Tâche

**Commande:** `/task-start XXX-NNN`

**Étapes automatisées:**

1. Validation de la DoR
2. Mise à jour du statut vers "🔄 En cours" dans le fichier de tâche
3. Mise à jour synchronisée de [TASKS.md](TASKS.md)
4. Création de la branche Git: `task/XXX-NNN-slug`
5. Commit initial: `chore(tasks): 🔧 start XXX-NNN`
6. Ajout d'une entrée dans "Historique des modifications"
7. Affichage du contexte (description, sous-tâches, notes pour Claude)

**Actions manuelles requises:**

- Aucune

**Résultat attendu:**

- Branche Git créée et active
- Fichiers mis à jour avec le bon statut
- Contexte chargé pour commencer le travail

### Phase 2: Travail sur une Tâche

**Cycle de travail:**

1. Consulter les sous-tâches dans le fichier de tâche
2. Implémenter les changements nécessaires
3. Cocher les sous-tâches au fur et à mesure
4. Faire des commits incrémentaux avec `Refs XXX-NNN`

**Format des commits incrémentaux:**

```bash
git commit -m "type(scope): emoji description

Details about the change.

Refs XXX-NNN"
```

**Bonnes pratiques:**

- Faire des commits atomiques (une fonctionnalité = un commit)
- Tester régulièrement avec `typst compile cv.typ`
- Cocher les sous-tâches dès qu'elles sont terminées
- Mettre à jour les notes si nécessaire

### Phase 3: Finalisation d'une Tâche

**Commande:** `/task-complete XXX-NNN`

**Étapes automatisées:**

1. Validation de la DoD
2. Compilation automatique du CV pour vérifier les erreurs
3. Prompt pour remplir "Résultat final" et "Temps réel"
4. Mise à jour du statut vers "✅ Terminé"
5. Remplissage automatique de "Terminé le"
6. Génération et création du commit final avec `Closes XXX-NNN`
7. Déplacement de l'entrée de "Actives" vers "Terminées" dans [TASKS.md](TASKS.md)
8. Mise à jour des statistiques
9. Proposition de merge de la branche

**Actions manuelles requises:**

- Renseigner le résultat final (prompt interactif)
- Confirmer ou éditer le message de commit généré
- Décider de merger la branche ou non

**Résultat attendu:**

- Tâche marquée comme terminée
- Dashboard mis à jour
- Commit final créé avec référence
- Branche prête à être mergée ou déjà mergée

### Phase 4: Archivage (Optionnel)

**Commande:** `/task-archive XXX-NNN`

**Étapes automatisées:**

1. Validation que la tâche est "✅ Terminé"
2. Déplacement du fichier vers `.archived-tasks/`
3. Retrait de l'entrée de [TASKS.md](TASKS.md)
4. Mise à jour des statistiques

**Actions manuelles requises:**

- Aucune

**Résultat attendu:**

- Fichier archivé mais historique Git conservé
- Dashboard nettoyé
- Statistiques actualisées

---

## Quality Gates

Points de contrôle automatiques pour garantir la qualité.

### Gate 1: Validation au Démarrage

**Quand:** Avant de démarrer une tâche avec `/task-start`

**Vérifications:**

- Le fichier de tâche existe
- Le statut est "À faire" ou "Bloqué"
- L'ID est unique
- Les sections obligatoires sont remplies

**Action en cas d'échec:**

- Afficher l'erreur avec détails
- Suggérer la correction à apporter
- Ne pas créer la branche Git

### Gate 2: Validation en Cours

**Quand:** À chaque compilation du CV

**Vérifications:**

- Le CV compile sans erreur
- Aucun warning critique
- Le PDF est généré correctement

**Action en cas d'échec:**

- Afficher l'erreur de compilation
- Ne pas permettre de terminer la tâche
- Bloquer le commit si nécessaire

### Gate 3: Validation à la Finalisation

**Quand:** Avant de terminer une tâche avec `/task-complete`

**Vérifications:**

- Toutes les sous-tâches sont cochées
- Le CV compile sans erreur
- Le fichier de tâche est complet
- Le format de commit est valide

**Action en cas d'échec:**

- Afficher les éléments manquants
- Proposer de compléter interactivement
- Ne pas créer le commit final tant que non résolu

### Gate 4: Validation de Cohérence

**Quand:** À la demande avec `/task-validate`

**Vérifications:**

- Cohérence entre task files et [TASKS.md](TASKS.md)
- Format valide de tous les task files
- Absence d'IDs en double
- Statistiques correctes

**Action en cas d'échec:**

- Lister toutes les incohérences
- Proposer des corrections automatiques
- Permettre une réparation manuelle si nécessaire

---

## Gestion des Erreurs

### Mode Interactif

Lorsqu'une erreur est détectée, les commandes adoptent un comportement interactif:

**Options proposées:**

1. **Corriger maintenant** - Claude propose de corriger l'erreur automatiquement
2. **Ignorer et continuer** - Pour les cas exceptionnels (avec warning)
3. **Annuler** - Stopper l'opération sans changement

**Exemple:**

```text
❌ Erreur: La tâche CNT-003 n'existe pas dans TASKS/

Options:
1. Créer la tâche maintenant
2. Vérifier l'ID (peut-être une faute de frappe?)
3. Annuler l'opération

Votre choix: _
```

### Types d'Erreurs

**Erreurs Bloquantes:**

- ID de tâche invalide ou inexistant
- Fichier de tâche manquant ou corrompu
- Erreur de compilation du CV
- Conflit Git non résolu

**Erreurs Non-Bloquantes (Warnings):**

- Sous-tâches incomplètes mais tâche marquée terminée
- Temps réel non renseigné
- Section "Résultat final" vide
- Statistiques légèrement désynchronisées

**Erreurs Récupérables:**

- Format de commit incorrect (correction automatique)
- Statut invalide (correction interactive)
- Entrée manquante dans [TASKS.md](TASKS.md) (ajout automatique)

### Stratégies de Récupération

**Validation Failed:**

1. Afficher clairement ce qui ne va pas
2. Proposer une correction automatique si possible
3. Permettre la correction manuelle sinon
4. Ne pas bloquer indéfiniment l'utilisateur

**Synchronisation Failed:**

1. Identifier la source de désynchronisation
2. Proposer de resynchroniser automatiquement
3. Sauvegarder l'état actuel avant correction
4. Valider après correction

**Git Conflicts:**

1. Afficher les fichiers en conflit
2. Proposer de résoudre les conflits simples
3. Guider vers la résolution manuelle si complexe
4. Ne pas forcer de merge automatique

---

## Analyses et Audits

Le système d'analyses permet de comparer le CV avec des sources externes (LinkedIn, GitHub, CVs externes) pour identifier des écarts et générer des recommandations d'amélioration.

### Définitions

**Analyse:**
- Un processus structuré de comparaison entre le CV et une source externe
- Associée à une tâche (ex: CNT-001 LinkedIn Audit)
- Produit un ensemble de recommandations tracées
- Documentée dans `ANALYSES.md`

**Recommandation:**
- Une action concrète identifiée lors d'une analyse
- Format ID: `{ANALYSIS-ID}-R{NN}` (ex: CNT-001-R05)
- Classée par priorité: 🔴🔴 Très Haute, 🔴 Haute, 🟡 Moyenne, 🟢 Basse
- Peut être transformée en tâche via `/task-from-analysis`

### Cycle de Vie d'une Analyse

#### 1. Création de l'Analyse

**Commande:** `/task-create` (trigramme CNT)

**Étapes:**
1. Créer une tâche d'analyse (ex: "CNT-001 LinkedIn Audit")
2. Démarrer la tâche avec `/task-start CNT-001`
3. Extraire les données source avec `/analyze-source --task-id=CNT-001`

**Fichiers créés:**
- `.tasks/resources/audits/CNT-001/linkedin-profile.md` (données brutes)
- `.tasks/resources/audits/CNT-001/cv-snapshot.md` (état CV au moment de l'audit)

#### 2. Analyse Comparative

**Étapes manuelles:**
1. Utiliser `audit-template.md` comme base
2. Créer `.tasks/resources/analyses/CNT-001/audit-report.md` (analyse complète)
3. Créer `.tasks/resources/analyses/CNT-001/recommendations.md` (liste détaillée)
4. Créer `.tasks/resources/analyses/CNT-001/recommendations-status.md` (suivi)
5. Créer `.tasks/resources/analyses/CNT-001/action-plan.md` (plan d'implémentation)
6. Créer `.tasks/resources/analyses/CNT-001/metrics.md` (statistiques)

**Règles:**
- Chaque recommandation doit avoir un ID unique `{ANALYSIS-ID}-R{NN}`
- Chaque recommandation doit avoir une priorité (🔴🔴, 🔴, 🟡, 🟢)
- Chaque recommandation doit référencer une ligne du CV (ex: `src/cv.typ:122`)
- Le fichier `recommendations-status.md` doit suivre le format standard

#### 3. Complétion de l'Analyse

**Commande:** `/task-complete CNT-001`

**Vérifications:**
- Tous les fichiers d'analyse sont créés
- ANALYSES.md est mis à jour avec l'entrée de l'analyse
- La tâche CNT-001 référence les fichiers créés
- Au moins 3 recommandations sont documentées

**Résultat:**
- L'analyse est documentée dans ANALYSES.md
- Les recommandations sont prêtes à être transformées en tâches

#### 4. Transformation en Tâches

**Commande:** `/task-from-analysis --analysis-id=CNT-001 --filter=high`

**Comportement:**
1. Liste les recommandations pendantes depuis `recommendations-status.md`
2. Permet la sélection batch ('1,5,6', 'all', 'high', etc.)
3. Pour chaque recommandation sélectionnée:
   - Crée une tâche avec données pré-remplies
   - Ajoute une référence dans la tâche: "Origine: CNT-001-R05"
   - Coche la recommandation dans `recommendations-status.md`
   - Ajoute l'ID de la tâche créée
4. Met à jour les statistiques dans ANALYSES.md

**Règles:**
- La tâche créée doit référencer la recommandation d'origine
- `recommendations-status.md` doit être mis à jour automatiquement
- Les statistiques dans ANALYSES.md doivent être recalculées

#### 5. Exécution et Complétion

**Workflow:**
1. `/task-start CNT-002` (tâche issue de CNT-001-R05)
2. Implémenter les changements dans le CV
3. `/task-complete CNT-002`
4. La recommandation CNT-001-R05 passe automatiquement à "✅ Completed"

**Vérifications automatiques:**
- Vérifier que la recommandation est marquée complétée
- Mettre à jour les statistiques dans ANALYSES.md
- Vérifier la traçabilité (tâche → recommandation → analyse)

### Conventions de Nommage

**IDs d'analyse:**
- Format: `XXX-NNN` (ID de la tâche d'analyse)
- Exemple: `CNT-001` pour "LinkedIn Audit"

**IDs de recommandation:**
- Format: `{ANALYSIS-ID}-R{NN}`
- Exemple: `CNT-001-R05` (5ème recommandation de l'analyse CNT-001)
- Numérotation séquentielle (R01, R02, ..., R99)

**Fichiers d'audit:**
- `linkedin-profile.md` - Profil LinkedIn extrait
- `github-profile.md` - Profil GitHub extrait
- `cv-externe-{source}.md` - CV externe
- `website-{domain}.md` - Site web personnel
- `cv-snapshot.md` - État du CV au moment de l'audit

**Fichiers d'analyse:**
- `audit-report.md` - Rapport d'analyse comparative
- `recommendations.md` - Recommandations détaillées
- `recommendations-status.md` - Suivi des recommandations (fichier de travail)
- `action-plan.md` - Plan d'implémentation par phases
- `metrics.md` - Statistiques et métriques

### Traçabilité Requise

**Analyse → Recommandations:**
- Chaque analyse doit lister toutes ses recommandations dans `recommendations.md`
- Chaque recommandation doit référencer l'analyse dans son ID

**Recommandation → Tâche:**
- Chaque tâche issue d'une recommandation doit indiquer l'origine:
  ```markdown
  **Origine:** Recommandation [CNT-001-R05](../resources/analyses/CNT-001/recommendations-status.md#r05)
  ```
- Le fichier `recommendations-status.md` doit être mis à jour avec l'ID de la tâche

**Tâche → CV:**
- Chaque recommandation doit référencer la ligne CV concernée
- Exemple: `src/cv.typ:122` ou `src/cv.typ:220-250`

**Complétion:**
- Quand une tâche est complétée, la recommandation doit passer à "✅ Completed"
- Les statistiques dans ANALYSES.md doivent refléter l'avancement

### Quality Gates pour Analyses

**Gate 1: Validation de l'Extraction**

Avant de marquer l'extraction comme terminée:
- Au moins 3 sections extraites avec du contenu
- Métadonnées complètes (date, source, type)
- Nom de fichier suit la convention
- Fichier sauvegardé dans le bon dossier

**Gate 2: Validation de l'Analyse**

Avant de compléter une tâche d'analyse:
- `audit-report.md` existe et contient au moins 3 écarts identifiés
- `recommendations.md` existe avec au moins 3 recommandations
- `recommendations-status.md` existe et suit le format standard
- ANALYSES.md est mis à jour avec l'entrée de l'analyse

**Gate 3: Validation de la Transformation**

Lors de `/task-from-analysis`:
- Vérifier que l'analyse existe dans ANALYSES.md
- Vérifier que `recommendations-status.md` existe
- Vérifier qu'il reste des recommandations pendantes
- S'assurer de la cohérence des IDs générés

**Gate 4: Validation de la Complétion**

Lors de `/task-complete` sur une tâche issue d'analyse:
- Vérifier que la recommandation d'origine existe
- Mettre à jour automatiquement `recommendations-status.md`
- Recalculer les statistiques dans ANALYSES.md
- Maintenir la traçabilité complète

### Commandes Dédiées

- `/analyze-source` - Extraire des données depuis une source externe
- `/task-from-analysis` - Créer des tâches depuis des recommandations d'analyse

Voir [.claude/commands/README.md](.claude/commands/README.md#commandes-danalyse) pour la documentation complète.

---

## Références

- [TASKS.md](TASKS.md) - Dashboard central des tâches
- [ANALYSES.md](ANALYSES.md) - Dashboard central des analyses
- [TASKS/TEMPLATE.md](TASKS/TEMPLATE.md) - Template de tâche
- [resources/templates/](resources/templates/) - Templates d'audit et recommandations
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Conventions Git
- [CLAUDE.md](CLAUDE.md) - Instructions générales
- [.claude/commands/README.md](.claude/commands/README.md) - Documentation des commandes
