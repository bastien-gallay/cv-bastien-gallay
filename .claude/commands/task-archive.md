---
description: Archive une tâche terminée vers le répertoire d'archives
---

# Commande: task-archive

Archive une tâche terminée en la déplaçant vers `.tasks/.archived/` tout en préservant l'historique Git.

## Utilisation

```bash
/task-archive <ID> [--verbose]
```

## Arguments

- `<ID>`: Identifiant de la tâche au format `XXX-NNN` (ex: CNT-003, TPL-001)

*Note :* L'utilisateur peut abréger en omettant le tiret et les 0 préfixes (ex: CNT3 pour CNT-003).

## Options

- `--verbose`: Affiche des informations détaillées sur l'archivage

## Comportement

Cette commande déplace une tâche terminée vers les archives tout en maintenant la cohérence du système.

### Étape 1: Validation

1. **Vérifier que la tâche existe**
   - Scanner `TASKS/` pour trouver le fichier `{ID}-*.md`
   - Si non trouvé, erreur bloquante

2. **Vérifier le statut**
   - Lire le fichier de tâche
   - Extraire le statut depuis la table des métadonnées
   - Statut acceptable: "✅ Terminé" uniquement
   - Si autre statut: erreur bloquante

3. **Vérifier que la tâche est complète**
   - Section "Résultat final" remplie
   - Date de completion renseignée
   - Toutes les sous-tâches cochées

### Étape 2: Mise à Jour du Fichier de Tâche

1. **Mettre à jour le statut**
   - Remplacer `| **Statut** | ✅ Terminé |` par `| **Statut** | 📦 Archivé |`

2. **Ajouter une entrée dans l'historique**
   - Dans la section "Historique des modifications"
   - Ajouter: `| {date_aujourdhui} | Archivé | Tâche archivée dans .tasks/.archived/ |`

### Étape 3: Archivage du Fichier

1. **Créer le répertoire si nécessaire**
   - S'assurer que `.tasks/.archived/` existe
   - Le créer si absent

2. **Déplacer le fichier**
   - De: `TASKS/{ID}-{slug}.md`
   - Vers: `.tasks/.archived/{ID}-{slug}.md`
   - Utiliser `git mv` pour préserver l'historique

3. **Vérifier l'intégrité**
   - Confirmer que le fichier existe dans `.tasks/.archived/`
   - Confirmer qu'il n'existe plus dans `TASKS/`

### Étape 4: Mise à Jour de TASKS.md

1. **Retirer l'entrée de "Tâches terminées"**
   - Trouver la ligne avec `[{ID}]`
   - La supprimer complètement

2. **Mettre à jour les statistiques**
   - Décrémenter "Total"
   - Décrémenter "Terminées"

3. **Mettre à jour la note d'archivage**
   - Compter le nombre de fichiers dans `.tasks/.archived/`
   - Mettre à jour le texte si pertinent

### Étape 5: Commit Git

1. **Créer un commit d'archivage**
   ```bash
   git add .tasks/.archived/{ID}-{slug}.md
   git add TASKS.md
   git commit -m "chore(tasks): 🗄️ archive {ID}

   Archived completed task to .tasks/.archived/

   Refs {ID}"
   ```

2. **Afficher le hash du commit**

### Étape 6: Confirmation

Afficher un résumé:

```text
✅ Tâche archivée avec succès: {ID}

📋 {Titre}
📅 Terminée le: {date}
📦 Archivée le: {date_aujourdhui}

📂 Actions effectuées:
  ✓ Historique de la tâche mis à jour
  ✓ Statut changé en "📦 Archivé"
  ✓ Fichier déplacé vers .tasks/.archived/
  ✓ Entrée retirée de TASKS.md
  ✓ Statistiques mises à jour
  ✓ Commit créé ({hash})
  ✓ Historique Git préservé

📊 Statistiques mises à jour:
  - Total: 7 → 6 tâches
  - Terminées: 1 → 0
  - Archivées: 0 → 1

Note: Le fichier archivé reste accessible dans .tasks/.archived/
et l'historique Git complet est préservé.
```

## Validation

Avant d'archiver, vérifier:
- ✓ Le fichier de tâche existe
- ✓ Le statut est "✅ Terminé"
- ✓ La tâche est complète (résultat final rempli)
- ✓ Le répertoire `.tasks/.archived/` existe ou peut être créé

## Gestion des Erreurs

**Tâche inexistante:**

```text
❌ Erreur: La tâche {ID} n'existe pas

Vérifiez l'ID ou listez les tâches disponibles.
```

**Tâche pas terminée:**

```text
❌ Erreur: La tâche {ID} n'est pas terminée

Statut actuel: {statut}

Vous ne pouvez archiver que des tâches terminées.
Pour terminer la tâche: /task-complete {ID}
```

**Tâche incomplète:**

```text
⚠️  Warning: La tâche {ID} semble incomplète

Problèmes détectés:
  - Section "Résultat final" vide
  - 2 sous-tâches non cochées

Recommandation: Compléter la tâche avant de l'archiver.

Options:
1. Archiver quand même (forcer)
2. Retourner compléter la tâche
3. Annuler

Votre choix: _
```

**Répertoire .tasks/.archived/ inaccessible:**

```text
❌ Erreur: Impossible de créer/accéder au répertoire .tasks/.archived/

Erreur système: {message d'erreur}

Vérifiez les permissions du système de fichiers.
```

## Mode Verbose

Avec `--verbose`, afficher:
- Contenu du fichier avant et après mise à jour du statut
- Commandes Git exactes exécutées
- Diff des changements dans TASKS.md
- Permissions et propriétés du fichier archivé
- Historique des modifications complet

## Cas Spéciaux

### Désarchivage

Pour restaurer une tâche archivée:

```bash
# Déplacer manuellement le fichier
git mv .tasks/.archived/{ID}-{slug}.md TASKS/{ID}-{slug}.md

# Mettre à jour le statut dans le fichier
# | **Statut** | 📦 Archivé | → | **Statut** | ✅ Terminé |

# Ajouter une entrée dans l'historique
# | {date} | Restauré | Tâche restaurée depuis .tasks/.archived/ |

# Mettre à jour manuellement TASKS.md
# - Ajouter l'entrée dans "Tâches terminées"
# - Mettre à jour les statistiques

# Committer
git add TASKS/{ID}-{slug}.md TASKS.md
git commit -m "chore(tasks): 🔓 unarchive {ID}"
```

Note: Une commande `/task-unarchive` pourrait être ajoutée à l'avenir pour automatiser ce processus.

### Archivage en Masse

Pour archiver plusieurs tâches terminées d'un coup:

```bash
# Actuellement non supporté, à faire une par une:
/task-archive CNT-001
/task-archive TPL-001
/task-archive QUA-001
```

Une commande future `/task-archive --all` pourrait archiver toutes les tâches terminées en une seule fois.

### Suppression Définitive

L'archivage déplace simplement les fichiers. Pour supprimer définitivement une tâche archivée:

```bash
# ⚠️  ATTENTION: Suppression irréversible (historique Git perdu aussi)
git rm .tasks/.archived/{ID}-{slug}.md
git commit -m "chore(tasks): 🗑️ delete archived {ID}"
```

Recommandation: Ne jamais supprimer définitivement, garder l'archive et l'historique.

## Organisation des Archives

Les tâches archivées dans `.tasks/.archived/` peuvent être organisées par année ou trigramme pour faciliter la navigation:

```
.tasks/.archived/
  2025/
    CNT-001-linkedin-audit.md
    TPL-001-cv-versions.md
  2024/
    QUA-001-verification.md
```

Cette organisation peut être mise en place manuellement ou via une future amélioration de la commande.

## Exemple d'Utilisation

```bash
User: /task-archive TPL-001

Claude: Validation de la tâche TPL-001...
✓ Fichier trouvé: .tasks/tasks/TPL-001-cv-versions.md
✓ Statut valide: ✅ Terminé
✓ Tâche complète (résultat final rempli)

Mise à jour du fichier de tâche...
✓ Statut changé: "✅ Terminé" → "📦 Archivé"
✓ Historique mis à jour (entrée d'archivage ajoutée)

Archivage en cours...
✓ Répertoire .tasks/.archived/ vérifié
✓ Fichier déplacé avec git mv
✓ TASKS.md mis à jour
✓ Statistiques recalculées

Commit de l'archivage...
✓ Commit créé: f7a9c2b

✅ Tâche archivée avec succès: TPL-001

📋 Versions courte et longue du CV
📅 Terminée le: 2025-10-28
📦 Archivée le: 2025-10-28

📂 Actions effectuées:
  ✓ Historique de la tâche mis à jour
  ✓ Statut changé en "📦 Archivé"
  ✓ Fichier déplacé vers .tasks/.archived/
  ✓ Entrée retirée de TASKS.md
  ✓ Statistiques mises à jour
  ✓ Commit créé (f7a9c2b)
  ✓ Historique Git préservé

📊 Statistiques mises à jour:
  - Total: 7 → 6 tâches
  - Terminées: 1 → 0
  - Archivées: 0 → 1

Note: Le fichier archivé reste accessible dans .tasks/.archived/
et l'historique Git complet est préservé.
```

## Références

- [TASKS.md](../.tasks/TASKS.md) - Dashboard des tâches
- [.tasks/.archived/](../.tasks/.archived/) - Répertoire des archives
- [TASK_RULES.md](../.tasks/TASK_RULES.md) - Règles et workflow
