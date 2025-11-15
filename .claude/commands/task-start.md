---
description: Démarre le travail sur une tâche existante avec setup Git automatique
---

# Commande: task-start

Démarre le travail sur une tâche existante en préparant l'environnement de travail complet.

## Utilisation

```bash
/task-start <ID> [--verbose]
```

## Arguments

- `<ID>`: Identifiant de la tâche au format `XXX-NNN` (ex: CNT-003, TPL-001).
   *Note :* L'utilisateur peut abréger en omettant le tiret et les 0 préfixes (ex:CNT3 pour CNT-003).

## Options

- `--verbose`: Affiche des informations détaillées sur chaque étape

## Comportement

Cette commande automatise toutes les étapes nécessaires pour démarrer proprement le travail sur une tâche.

### Étape 1: Validation de la DoR

Vérifier que la tâche respecte la Definition of Ready (voir [TASK_RULES.md](../.tasks/TASK_RULES.md)):

1. **Vérifier que le fichier existe**
   - Scanner `TASKS/` pour trouver le fichier `{ID}-*.md`
   - Si non trouvé, erreur bloquante

2. **Vérifier le statut actuel**
   - Lire le fichier de tâche
   - Extraire le statut depuis la table des métadonnées
   - Statuts acceptables: "⏳ À faire" ou "🚫 Bloqué"
   - Si "🔄 En cours": erreur (tâche déjà démarrée)
   - Si "✅ Terminé": erreur (tâche déjà terminée)

3. **Vérifier les sections obligatoires**
   - Description avec Contexte et Objectif remplis
   - Au moins 2 sous-tâches définies
   - Métadonnées complètes

4. **Vérifier l'unicité**
   - S'assurer qu'aucune autre tâche n'est en status "🔄 En cours" (optionnel, warning uniquement)

### Étape 2: Mise à Jour du Fichier de Tâche

1. **Mettre à jour le statut**
   - Remplacer `| **Statut** | ⏳ À faire |` par `| **Statut** | 🔄 En cours |`
   - Ou remplacer `| **Statut** | 🚫 Bloqué |` par `| **Statut** | 🔄 En cours |`

2. **Ajouter une entrée dans l'historique**
   - Dans la section "Historique des modifications"
   - Ajouter une ligne: `| {date_aujourdhui} | En cours | Début du travail |`

### Étape 3: Mise à Jour de TASKS.md

1. **Trouver l'entrée correspondante**
   - Chercher la ligne contenant `[{ID}]` dans la table "Tâches actives"

2. **Mettre à jour le statut**
   - Remplacer `⏳ À faire` ou `🚫 Bloqué` par `🔄 En cours`

3. **Mettre à jour les statistiques**
   - Décrémenter "À faire" ou "Bloquées"
   - Incrémenter "En cours"

### Étape 4: Décision et Création Conditionnelle de Branche Git

1. **Lire le champ "Branche nécessaire" des métadonnées**
   - Valeurs possibles: `Auto`, `Oui`, `Non`

2. **Déterminer si une branche est nécessaire**
   - Si paramètre `--branch` fourni → **OUI, créer branche**
   - Si métadonnées = "Oui" → **OUI, créer branche**
   - Si métadonnées = "Non" → **NON, pas de branche**
   - Si métadonnées = "Auto" → analyser critères:
     * Temps estimé > 2 heures?
     * Trigramme = TPL ou INF?
     * Description contient "expérimentation" ou "experimental"?
     * Si OUI à l'un des critères → **OUI, créer branche**
     * Sinon → **NON, pas de branche**

3. **Si branche nécessaire:**
   - Générer le nom: `task/{ID}-{slug}`
   - Slug extrait du nom de fichier ou généré depuis le titre
   - Créer et basculer: `git checkout -b task/{ID}-{slug}`
   - Afficher: `✓ Branche créée: task/{ID}-{slug}`

4. **Si pas de branche:**
   - Rester sur la branche courante (normalement `main`)
   - Afficher: `ℹ️  Pas de branche Git (commits directs sur main)`

### Étape 5: Commit Initial

1. **Générer le message de commit**
   - Format: `chore(tasks): 🔧 start {ID}`
   - Corps: vide (commit minimal)

2. **Créer le commit**
   - Ajouter les fichiers modifiés: `TASKS/{ID}-*.md` et `TASKS.md`
   - `git add TASKS/{ID}-*.md TASKS.md`
   - `git commit -m "chore(tasks): 🔧 start {ID}"`

### Étape 6: Affichage du Contexte

Afficher un résumé pour charger le contexte de travail:

```text
✅ Tâche démarrée: {ID}

📋 {Titre}
🔴 Priorité: {Priorité}
🎯 Section CV: {Section}

📝 Contexte:
{Contexte de la tâche}

🎯 Objectif:
{Objectif de la tâche}

✓ Sous-tâches:
  [ ] Sous-tâche 1
  [ ] Sous-tâche 2
  [ ] Sous-tâche 3

💡 Notes pour Claude:
{Notes pour Claude si présentes}

📊 Status:
  - Branche: task/{ID}-{slug} (si branche créée) OU "main (pas de branche)" (si pas de branche)
  - Fichier: .tasks/tasks/{ID}-{slug}.md
  - Dashboard: mis à jour

Prêt à travailler! N'oubliez pas de:
  - Cocher les sous-tâches au fur et à mesure
  - Faire des commits avec 'Refs {ID}'
  - Utiliser /task-complete {ID} quand terminé
```

## Validation

Avant de démarrer la tâche, vérifier:

- ✓ Le fichier de tâche existe
- ✓ Le statut est "À faire" ou "Bloqué"
- ✓ Les sections obligatoires sont remplies
- ✓ Au moins 2 sous-tâches sont définies
- ✓ L'ID est au bon format (XXX-NNN)

## Gestion des Erreurs

**Tâche inexistante:**

```text
❌ Erreur: La tâche {ID} n'existe pas

Vérifications effectuées:
  - Aucun fichier trouvé dans TASKS/ correspondant à {ID}
  - Vérifiez l'ID (format: XXX-NNN)

Options:
1. Créer la tâche maintenant avec /task-create
2. Vérifier l'ID (peut-être une faute de frappe?)
3. Lister les tâches disponibles

Votre choix: _
```

**Tâche déjà démarrée:**

```text
⚠️  Warning: La tâche {ID} est déjà en cours

Statut actuel: 🔄 En cours

Options:
1. Continuer sur cette tâche (afficher le contexte)
2. Redémarrer la tâche (reset le statut)
3. Annuler

Votre choix: _
```

**Tâche déjà terminée:**

```text
❌ Erreur: La tâche {ID} est déjà terminée

Statut: ✅ Terminé
Terminée le: {date}

Vous ne pouvez pas redémarrer une tâche terminée.

Options:
1. Voir les détails de la tâche
2. Créer une nouvelle tâche similaire
3. Annuler

Votre choix: _
```

**Plusieurs tâches en cours:**

```text
⚠️  Warning: Une autre tâche est déjà en cours

Tâche en cours: {autre_ID} - {autre_titre}

Bonne pratique: Terminer une tâche avant d'en démarrer une autre.

Options:
1. Continuer quand même (démarrer {ID})
2. Retourner sur {autre_ID}
3. Terminer {autre_ID} d'abord
4. Annuler

Votre choix: _
```

**Validation DoR échouée:**

```text
❌ Validation DoR échouée pour {ID}

Problèmes détectés:
  ❌ Description vide
  ❌ Moins de 2 sous-tâches (trouvées: 1)
  ⚠️  Pas de notes pour Claude

Options:
1. Compléter la tâche maintenant (mode interactif)
2. Éditer le fichier manuellement
3. Démarrer quand même (exception DoR)
4. Annuler

Votre choix: _
```

## Mode Verbose

Avec `--verbose`, afficher en plus:

- Détails de chaque validation
- Contenu exact des modifications apportées
- Sortie complète des commandes Git
- État avant/après de chaque fichier modifié

## Cas Spéciaux

### Déblocage d'une Tâche Bloquée

Si la tâche a le statut "🚫 Bloqué", demander confirmation:

```text
📦 La tâche {ID} est actuellement bloquée

Raison du blocage:
{Raison extraite des notes ou de l'historique}

Voulez-vous débloquer et démarrer cette tâche? (o/N): _
```

Si oui, procéder normalement en mettant le statut à "🔄 En cours".

## Exemple d'Utilisation

```text
User: /task-start CNT-001

Claude: Validation de la tâche CNT-001...
✓ Fichier trouvé: .tasks/tasks/CNT-001-linkedin-audit.md
✓ Statut valide: ⏳ À faire
✓ DoR respectée

Mise à jour des fichiers...
✓ .tasks/tasks/CNT-001-linkedin-audit.md - Statut mis à jour
✓ TASKS.md - Dashboard synchronisé
✓ Statistiques actualisées

Analyse de la nécessité d'une branche...
✓ Branche nécessaire (critère: temps estimé > 2h)
✓ Branche créée: task/CNT-001-linkedin-audit
✓ Commit initial créé

✅ Tâche démarrée: CNT-001

📋 Audit LinkedIn
🔴 Priorité: Haute
🎯 Section CV: Experience

📝 Contexte:
Le profil LinkedIn contient des informations plus récentes que le CV actuel.

🎯 Objectif:
Synchroniser le CV avec les informations LinkedIn pour garantir la cohérence.

✓ Sous-tâches:
  [ ] Extraire les informations du profil LinkedIn
  [ ] Comparer avec le CV actuel
  [ ] Mettre à jour les différences
  [ ] Vérifier la cohérence des dates

💡 Notes pour Claude:
Consulter le fichier cv.typ lignes 103-200 pour la section expérience.
Respecter le format de date existant.

📊 Status:
  - Branche: task/CNT-001-linkedin-audit
  - Fichier: .tasks/tasks/CNT-001-linkedin-audit.md
  - Dashboard: mis à jour

Prêt à travailler! N'oubliez pas de:
  - Cocher les sous-tâches au fur et à mesure
  - Faire des commits avec 'Refs CNT-001'
  - Utiliser /task-complete CNT-001 quand terminé
```

## Références

- [TASK_RULES.md](../.tasks/TASK_RULES.md) - Règles DoR/DoD
- [TASKS.md](../.tasks/TASKS.md) - Dashboard des tâches
- [GIT_WORKFLOW.md](../../docs/GIT_WORKFLOW.md) - Conventions Git
