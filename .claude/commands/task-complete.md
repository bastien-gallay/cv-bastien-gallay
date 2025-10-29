---
description: Finalise une tâche en cours avec validation DoD complète
---

# Commande: task-complete

Finalise une tâche en cours en validant tous les critères de completion et en mettant à jour tous les fichiers.

## Utilisation

```
/task-complete <ID> [--verbose] [--no-merge]
```

## Arguments

- `<ID>`: Identifiant de la tâche au format `XXX-NNN` (ex: CNT-003, TPL-001)

*Note :* L'utilisateur peut abréger en omettant le tiret et les 0 préfixes (ex: CNT3 pour CNT-003).

## Options

- `--verbose`: Affiche des informations détaillées sur chaque étape
- `--no-merge`: Ne pas proposer de merger la branche automatiquement

## Comportement

Cette commande automatise toutes les étapes de finalisation d'une tâche en respectant la Definition of Done.

### Étape 1: Validation de la DoD

Vérifier que la tâche respecte la Definition of Done (voir [TASK_RULES.md](../.tasks/TASK_RULES.md)):

1. **Vérifier que le fichier existe**
   - Scanner `TASKS/` pour trouver le fichier `{ID}-*.md`
   - Si non trouvé, erreur bloquante

2. **Vérifier le statut actuel**
   - Lire le fichier de tâche
   - Extraire le statut depuis la table des métadonnées
   - Statut acceptable: "🔄 En cours"
   - Si autre: erreur ou warning selon le cas

3. **Vérifier les sous-tâches**
   - Parser la section "Sous-tâches"
   - Compter les cases cochées `[x]` vs non cochées `[ ]`
   - Si des sous-tâches ne sont pas cochées: demander confirmation (voir Gestion des Erreurs)

4. **Compiler le CV**
   - Exécuter `typst compile cv.typ`
   - Si erreur de compilation: erreur bloquante
   - Afficher les warnings éventuels

5. **Vérifier le PDF**
   - Vérifier que `cv.pdf` existe et a été modifié récemment
   - Optionnel: demander confirmation visuelle à l'utilisateur

### Étape 2: Collecte des Informations

Mode interactif pour compléter les informations finales:

1. **Résultat final - Ce qui a été fait**
   - Prompt: "Décrivez ce qui a été réalisé (bullet points):"
   - Accepter plusieurs lignes
   - Validation: au moins une réalisation

2. **Résultat final - Difficultés rencontrées**
   - Prompt: "Y a-t-il eu des difficultés? (optionnel, tapez 'aucune' pour passer):"
   - Optionnel

3. **Résultat final - Améliorations futures**
   - Prompt: "Des idées d'amélioration pour plus tard? (optionnel):"
   - Optionnel
   - **Si rempli:** Ajouter automatiquement dans [IDEAS.md](../.tasks/IDEAS.md)
     - Identifier la section selon le trigramme de la tâche
     - Format: `- [ ] {idée} (source: {ID}, {date})`
     - Remplacer "*Aucune idée pour l'instant*" si présent
     - Afficher confirmation: "✓ Idée ajoutée au backlog IDEAS.md"

4. **Temps réel**
   - Prompt: "Temps réel passé en heures (optionnel):"
   - Validation: nombre décimal si fourni

5. **Message de commit**
   - Générer automatiquement un message basé sur:
     - Type de tâche (trigramme → type de commit)
     - Titre de la tâche
     - Réalisations listées
   - Afficher le message généré
   - Proposer de l'éditer ou de l'accepter

### Étape 3: Mise à Jour du Fichier de Tâche

1. **Mettre à jour le statut**
   - Remplacer `| **Statut** | 🔄 En cours |` par `| **Statut** | ✅ Terminé |`

2. **Ajouter la date de completion**
   - Remplacer `| **Terminé le** | (à remplir lors de la complétion) |`
   - Par `| **Terminé le** | {date_aujourdhui} |`

3. **Ajouter le temps réel**
   - Si fourni, remplacer `| **Temps réel** | (à remplir après) |`
   - Par `| **Temps réel** | {temps} heures |`

4. **Remplir la section "Résultat final"**
   - Remplacer `[À remplir une fois la tâche terminée]` par le contenu collecté
   - Formater en markdown avec bullet points

5. **Ajouter une entrée dans l'historique**
   - Dans la section "Historique des modifications"
   - Ajouter: `| {date_aujourdhui} | Terminé | Tâche complétée |`

### Étape 4: Mise à Jour de TASKS.md

1. **Déplacer l'entrée**
   - Trouver la ligne avec `[{ID}]` dans "Tâches actives"
   - Copier la ligne
   - Modifier le statut pour `✅ Terminé`
   - La supprimer de "Tâches actives"
   - L'ajouter dans "Tâches terminées" (en haut de la liste)

2. **Mettre à jour les statistiques**
   - Décrémenter "En cours"
   - Incrémenter "Terminées"
   - Garder "Total" inchangé

### Étape 5: Commit Final

1. **Générer le message de commit**

   Format suggéré basé sur le trigramme:
   - CNT → `content(scope): ✏️ {titre}`
   - TPL → `feat(template): ✨ {titre}`
   - QUA → `chore(quality): 🔧 {titre}`
   - PIP → `chore(ci): 🔧 {titre}`
   - LAY → `style(layout): 💄 {titre}`
   - DOC → `docs: 📝 {titre}`
   - INF → `chore(infra): 🔧 {titre}`

   Corps du commit:
   ```
   {Réalisations sous forme de bullet points}

   Closes {ID}
   ```

2. **Afficher et permettre l'édition**
   ```
   Message de commit proposé:
   ───────────────────────────
   feat(template): ✨ Versions courte et longue du CV

   - Créé cv-short.typ (1 page)
   - Créé cv-long.typ (2+ pages)
   - Mis à jour le build script

   Closes TPL-001
   ───────────────────────────

   Options:
   1. Accepter ce message
   2. Éditer le message
   3. Annuler (ne pas committer)

   Votre choix: _
   ```

3. **Créer le commit**
   - `git add` tous les fichiers modifiés (tâche + TASKS.md + fichiers du CV)
   - `git commit` avec le message
   - Afficher le hash et le message du commit créé

### Étape 6: Gestion de la Branche

Si `--no-merge` n'est pas spécifié:

1. **Détecter la branche courante**
   - Vérifier qu'on est sur `task/{ID}-*`

2. **Proposer le merge**
   ```
   La tâche est terminée et committée.

   Voulez-vous merger la branche dans main? (o/N): _
   ```

3. **Si oui, merger**
   - `git checkout main`
   - `git merge --no-ff task/{ID}-{slug}`
   - Gérer les conflits si nécessaire
   - `git branch -d task/{ID}-{slug}` (proposer de supprimer la branche)

4. **Si non**
   - Laisser sur la branche de tâche
   - Informer l'utilisateur comment merger plus tard

### Étape 7: Confirmation Finale

Afficher un résumé complet:

```
✅ Tâche terminée avec succès: {ID}

📋 {Titre}
📅 Terminée le: {date}
⏱️  Temps réel: {temps} heures

📝 Résultat:
{Résumé des réalisations}

📊 Actions effectuées:
  ✓ Fichier de tâche mis à jour
  ✓ Dashboard synchronisé
  ✓ Statistiques actualisées
  ✓ Commit final créé ({hash})
  ✓ Branche mergée dans main

La tâche est maintenant archivée dans "Tâches terminées".
Utilisez `/task-archive {ID}` si vous voulez l'archiver définitivement.
```

## Validation

Avant de compléter la tâche, vérifier:
- ✓ Le fichier de tâche existe
- ✓ Le statut est "En cours"
- ✓ Toutes les sous-tâches sont cochées (ou confirmation utilisateur)
- ✓ Le CV compile sans erreur
- ✓ Le résultat final est documenté

## Gestion des Erreurs

**Tâche inexistante:**
```
❌ Erreur: La tâche {ID} n'existe pas

Vérifiez l'ID ou utilisez /task-list pour voir les tâches actives.
```

**Tâche pas en cours:**
```
❌ Erreur: La tâche {ID} n'est pas en cours

Statut actuel: {statut}

Vous devez démarrer la tâche avec /task-start avant de la terminer.
```

**Sous-tâches incomplètes:**
```
⚠️  Warning: Des sous-tâches ne sont pas terminées

Sous-tâches restantes:
  [ ] Sous-tâche non terminée 1
  [ ] Sous-tâche non terminée 2

Total: 2 sur 5 sous-tâches non terminées

Options:
1. Marquer toutes comme terminées (forcer)
2. Retourner compléter les sous-tâches
3. Retirer les sous-tâches non pertinentes
4. Annuler

Votre choix: _
```

**Erreur de compilation:**
```
❌ Erreur: Le CV ne compile pas

Erreur Typst:
{message d'erreur complet}

Vous devez corriger l'erreur avant de terminer la tâche.

Options:
1. Afficher le fichier avec l'erreur
2. Revenir corriger
3. Forcer la completion (⚠️  non recommandé)
4. Annuler

Votre choix: _
```

**Pas de modifications committées:**
```
⚠️  Warning: Aucun commit avec "Refs {ID}" trouvé

Il semble que vous n'ayez pas fait de commit de travail sur cette tâche.

Options:
1. Continuer quand même (tâche sans changements)
2. Faire un commit maintenant
3. Annuler

Votre choix: _
```

**Conflits Git lors du merge:**
```
❌ Erreur: Conflit lors du merge

Fichiers en conflit:
  - cv.typ
  - TASKS.md

Résolution:
1. Les conflits doivent être résolus manuellement
2. Puis: git add <fichiers>
3. Puis: git commit
4. La tâche est déjà marquée comme terminée dans les fichiers

Voulez-vous que je vous guide? (o/N): _
```

## Mode Verbose

Avec `--verbose`, afficher en plus:
- Détails de chaque validation DoD
- Contenu complet avant/après de chaque fichier
- Sortie complète des commandes Git
- Liste de tous les fichiers modifiés
- Diff des changements statistiques

## Cas Spéciaux

### Tâche Sans Changements Code

Si la tâche est de type documentation ou recherche:
- Permettre de compléter même sans changements dans cv.typ
- Accepter un résultat final descriptif sans commits
- Documenter dans l'historique

### Tâche Partiellement Réalisée

Si certaines sous-tâches ne peuvent pas être terminées:
- Proposer de les déplacer vers une nouvelle tâche
- Documenter pourquoi dans "Difficultés rencontrées"
- Permettre la completion avec exception

### Tâche Avec Dépendances

Si d'autres tâches dépendent de celle-ci:
- Scanner les références dans TASKS/
- Informer qu'elles peuvent maintenant être débloquées
- Proposer de démarrer la suivante

## Exemple d'Utilisation

```
User: /task-complete TPL1

Claude: Validation de la tâche TPL-001...
✓ Fichier trouvé: .tasks/tasks/TPL-001-cv-versions.md
✓ Statut valide: 🔄 En cours
✓ Toutes les sous-tâches cochées (4/4)

Compilation du CV...
✓ cv.typ compilé sans erreur
✓ cv.pdf généré (604KB)

Collecte des informations finales...

Décrivez ce qui a été réalisé (bullet points):
- Créé cv-short.typ pour version 1 page
- Créé cv-long.typ pour version 2+ pages
- Ajouté script de build pour les deux versions
- Mis à jour la documentation

Y a-t-il eu des difficultés? (optionnel):
Choix du contenu à garder pour la version courte a nécessité plusieurs itérations

Des idées d'amélioration pour plus tard? (optionnel):
Automatiser le choix du contenu selon des tags

Temps réel passé en heures (optionnel):
2.5

Message de commit proposé:
───────────────────────────
feat(template): ✨ Versions courte et longue du CV

- Créé cv-short.typ pour version 1 page
- Créé cv-long.typ pour version 2+ pages
- Ajouté script de build pour les deux versions
- Mis à jour la documentation

Closes TPL-001
───────────────────────────

Options:
1. Accepter ce message
2. Éditer le message
3. Annuler

Votre choix: 1

Mise à jour des fichiers...
✓ .tasks/tasks/TPL-001-cv-versions.md - Statut et résultat mis à jour
✓ TASKS.md - Tâche déplacée vers "Terminées"
✓ Statistiques actualisées

Création du commit final...
✓ Fichiers ajoutés: cv-short.typ, cv-long.typ, build.sh, .tasks/tasks/TPL-001-cv-versions.md, TASKS.md
✓ Commit créé: a3f5c1d

Voulez-vous merger la branche dans main? (o/N): o

✓ Basculé sur main
✓ Branche task/TPL-001-cv-versions mergée
✓ Branche locale supprimée

✅ Tâche terminée avec succès: TPL-001

📋 Versions courte et longue du CV
📅 Terminée le: 2025-10-28
⏱️  Temps réel: 2.5 heures

📝 Résultat:
- Créé cv-short.typ pour version 1 page
- Créé cv-long.typ pour version 2+ pages
- Ajouté script de build pour les deux versions
- Mis à jour la documentation

📊 Actions effectuées:
  ✓ Fichier de tâche mis à jour
  ✓ Dashboard synchronisé
  ✓ Statistiques actualisées
  ✓ Commit final créé (a3f5c1d)
  ✓ Branche mergée dans main

La tâche est maintenant archivée dans "Tâches terminées".
Utilisez `/task-archive TPL-001` si vous voulez l'archiver définitivement.
```

## Références

- [TASK_RULES.md](../.tasks/TASK_RULES.md) - Règles DoR/DoD
- [TASKS.md](../.tasks/TASKS.md) - Dashboard des tâches
- [GIT_WORKFLOW.md](../../docs/GIT_WORKFLOW.md) - Conventions Git
