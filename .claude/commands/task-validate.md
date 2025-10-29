---
description: Valide la cohérence du système de gestion des tâches
---

# Commande: task-validate

Vérifie la cohérence entre les fichiers de tâches et le dashboard, détecte les erreurs structurelles et les incohérences.

## Utilisation

```bash
/task-validate [--verbose] [--fix]
```

## Options

- `--verbose`: Affiche des détails sur toutes les vérifications effectuées
- `--fix`: Corrige automatiquement les erreurs simples détectées

## Comportement

Cette commande effectue une validation complète du système de tâches en vérifiant le respect des règles définies dans [TASK_RULES.md](../.tasks/TASK_RULES.md).

### Vérifications Effectuées

1. **Validation DoR/DoD**
   - Vérifier que les tâches "À faire" respectent la DoR
   - Vérifier que les tâches "Terminées" respectent la DoD
   - Référencer les critères depuis [TASK_RULES.md](../.tasks/TASK_RULES.md)

2. **Cohérence Structurelle**
   - Chaque fichier `TASKS/XXX-NNN-*.md` a une entrée dans TASKS.md
   - Chaque entrée dans TASKS.md a un fichier correspondant
   - Les statuts sont cohérents entre fichiers et dashboard
   - Les priorités correspondent
   - Les IDs sont uniques (pas de doublons)

3. **Statistiques**
   - Recalculer le total de tâches
   - Compter par statut (À faire, En cours, Terminées, Bloquées)
   - Comparer avec les statistiques dans TASKS.md
   - Vérifier les prochains IDs disponibles par trigramme

4. **Format et Structure**
   - Noms de fichiers respectent le pattern `XXX-NNN-slug.md`
   - Trigrammes valides (CNT, TPL, QUA, PIP, LAY, DOC, INF)
   - Présence des sections obligatoires du template
   - Format des métadonnées (table markdown valide)

5. **Références et Liens**
   - Liens dans TASKS.md pointent vers des fichiers existants
   - Pas de fichiers orphelins (non référencés)
   - Références entre tâches sont valides

### Rapport de Validation

Générer un rapport structuré:

```text
🔍 Validation du système de tâches

📊 Fichiers analysés:
  - 7 fichiers de tâches
  - 1 dashboard (TASKS.md)

✅ Validations réussies:
  ✓ Tous les fichiers ont un format valide
  ✓ Tous les IDs sont uniques
  ✓ Dashboard synchronisé avec les fichiers
  ✓ Statistiques correctes
  ✓ Aucune référence cassée

⚠️  Warnings (1):
  • CNT-001 et TPL-001 sont toutes les deux en cours
    → Recommandation: terminer une tâche avant d'en démarrer une autre

❌ Erreurs détectées (0):
  (aucune)

📈 Statistiques actuelles:
  - Total: 7 tâches
  - À faire: 5 | En cours: 2 | Terminées: 0 | Bloquées: 0
  - Par trigramme: CNT(1), TPL(2), QUA(1), PIP(1), INF(1), DOC(1)

✅ Le système de tâches est cohérent!
```

### Corrections Automatiques (si --fix)

Lorsque `--fix` est activé, proposer de corriger:

**Corrections Automatiques:**

1. **Statistiques incorrectes**
   - Action: Recalculer et mettre à jour TASKS.md
   - Confirmation: Oui

2. **Fichier orphelin**
   - Action: Ajouter l'entrée dans TASKS.md (statut déduit du fichier)
   - Confirmation: Oui (montrer l'entrée à ajouter)

3. **Référence cassée**
   - Action: Retirer l'entrée de TASKS.md
   - Confirmation: Oui (montrer l'entrée à supprimer)

4. **Désynchronisation statut/priorité**
   - Action: Synchroniser (fichier = source de vérité)
   - Confirmation: Oui (montrer les changements)

5. **Prochains IDs incorrects**
   - Action: Recalculer et mettre à jour
   - Confirmation: Non (automatique)

**Corrections Manuelles Requises:**

1. **IDs en double**
   - Lister les fichiers concernés
   - Guider l'utilisateur pour renommer

2. **Tâches ne respectant pas DoR/DoD**
   - Lister les critères non respectés
   - Proposer d'utiliser /task-create ou /task-complete

3. **Conflits Git non résolus**
   - Détecter les marqueurs `<<<<<<<`, `=======`, `>>>>>>>`
   - Bloquer jusqu'à résolution

## Gestion des Erreurs

**Aucune erreur:**

```text
✅ Le système de tâches est cohérent!
Aucune action requise.
```

**Erreurs sans --fix:**

```text
❌ 3 erreurs détectées

Pour corriger automatiquement, utilisez:
/task-validate --fix
```

**Avec --fix:**

```text
❌ 3 erreurs détectées

2 peuvent être corrigées automatiquement, 1 nécessite une action manuelle.

Voulez-vous corriger automatiquement? (o/N): _
```

## Mode Verbose

Avec `--verbose`:

- Liste de chaque fichier analysé
- Détails de chaque vérification (DoR/DoD)
- Métadonnées extraites
- Calculs intermédiaires des statistiques
- Diff des corrections proposées

## Exemple d'Utilisation

```bash
User: /task-validate

Claude: 🔍 Validation du système de tâches

Analyse des fichiers...
✓ 7 fichiers de tâches
✓ TASKS.md

Vérification de la cohérence...
✓ Tous les IDs sont uniques
✓ Dashboard synchronisé
❌ Statistiques incorrectes

⚠️  Warnings (1):
  • 2 tâches en cours simultanément (CNT-001, DOC-001)

❌ Erreurs (1):
  • Statistiques incorrectes dans TASKS.md
    - À faire: affiché 6, réel 5
    - En cours: affiché 0, réel 2

Pour corriger: /task-validate --fix
```

```bash
User: /task-validate --fix

Claude: ❌ 1 erreur corrigible automatiquement

Correction proposée:
  Mettre à jour les statistiques dans TASKS.md

Changements:
  - À faire: 6 → 5
  - En cours: 0 → 2

Appliquer? (o/N): o

✓ TASKS.md mis à jour

✅ Système de tâches cohérent!
```

## Références

- [TASK_RULES.md](../.tasks/TASK_RULES.md) - Définition des règles DoR/DoD et validations
- [TASKS.md](../.tasks/TASKS.md) - Dashboard des tâches
- [.tasks/tasks/TEMPLATE.md](../.tasks/tasks/TEMPLATE.md) - Template de référence
