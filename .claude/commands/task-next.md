---
description: Suggère la prochaine tâche à traiter selon un modèle "valeur/délai"
---

# Commande: task-next

Analyse les tâches "À faire" et suggère intelligemment la prochaine tâche à démarrer en privilégiant les tâches courtes à haute valeur (principe "Weighted value divided by delay").

## Utilisation

```bash
/task-next [--verbose] [--start]
```

## Options

- `--verbose`: Affiche le raisonnement complet derrière la suggestion
- `--start`: Démarre automatiquement la tâche suggérée (équivalent à `/task-start <ID>`)

## Comportement

Cette commande aide à choisir la prochaine tâche en maximisant le ratio valeur/temps.

### Critères de Sélection

L'algorithme privilégie les tâches courtes et importantes selon cette formule:

```
Score = Valeur / Temps estimé

Où:
  Valeur = (Priorité × 10) + (Urgence × 5) + (Ancienneté × 1)

  Priorité:
    - 🔴 Haute = 10 points
    - 🟡 Moyenne = 5 points
    - 🟢 Basse = 2 points

  Urgence:
    - Retard (date cible dépassée) = 10 points
    - < 7 jours = 5 points
    - < 30 jours = 2 points
    - Pas de date = 0 points

  Ancienneté:
    - Jours depuis création / 10 (max 5 points)

  Temps estimé:
    - Extrait des métadonnées (en heures)
    - Si non renseigné: estimation par défaut selon complexité (2h pour Basse, 4h pour Moyenne, 8h pour Haute)
```

**Principe:** Une tâche haute priorité de 1h aura un meilleur score qu'une tâche moyenne priorité de 4h, favorisant les "quick wins".

### Ordre de Traitement

1. **Filtrer les tâches "⏳ À faire"**
   - Exclure les tâches bloquées
   - Vérifier si une tâche est déjà en cours

2. **Calculer le score pour chaque tâche**
   - Appliquer la formule Valeur / Temps

3. **Trier par score décroissant**
   - Les scores les plus élevés en premier

4. **Suggérer le top 3**
   - Permettre à l'utilisateur de choisir

### Format de Sortie

```text
💡 Prochaine tâche suggérée: QUA-001

📋 Étapes de vérification du CV
🟡 Priorité: Moyenne
⏱️  Temps estimé: 1 heure
📅 Créée le: 2025-10-28 (aujourd'hui)
🎯 Section: General

📝 Contexte:
Définir une checklist de vérification pour s'assurer que le CV est complet et correct.

✨ Pourquoi cette tâche?
  - Ratio valeur/temps élevé (Score: 5.0)
  - Tâche courte (1h) et impactante
  - Priorité moyenne, facile à terminer rapidement

Autres tâches à considérer:
  2. CNT-001 - Audit LinkedIn (Score: 3.75, 🔴 Haute, 4h)
  3. INF-001 - Intégration MCP (Score: 1.25, 🟡 Moyenne, 4h)

Commandes:
  /task-start QUA-001  - Démarrer cette tâche
  /task-next --start   - Démarrer automatiquement
```

### Avec --start

Si `--start` est spécifié, démarrer automatiquement la tâche suggérée:

```text
💡 Démarrage automatique de: QUA-001

[Sortie de /task-start QUA-001]
```

### Cas Particuliers

**Aucune tâche à faire:**

```text
✅ Aucune tâche en attente!

Toutes les tâches sont soit en cours, terminées ou bloquées.

Statistiques:
  - En cours: 1
  - Terminées: 5
  - Bloquées: 2

Voulez-vous:
  1. Voir les tâches en cours
  2. Voir les tâches bloquées
  3. Créer une nouvelle tâche (/task-create)

Votre choix: _
```

**Tâche déjà en cours:**

```text
⚠️  Une tâche est déjà en cours: DOC-001

📋 Système d'automatisation de gestion des tâches
🔴 Priorité: Haute
⏱️  Démarrée le: 2025-10-28

Recommandation: Terminez DOC-001 avant de démarrer une nouvelle tâche.

Voulez-vous:
  1. Continuer DOC-001 (afficher le contexte)
  2. Voir quand même la prochaine tâche suggérée
  3. Annuler

Votre choix: _
```

**Toutes les tâches bloquées:**

```text
⚠️  Toutes les tâches "À faire" sont bloquées

Tâches bloquées:
  - TPL-002 - Bloqué par: TPL-001 non terminé
  - PIP-001 - Bloqué par: dépendance externe

Recommandation:
  1. Terminer les tâches bloquantes
  2. Créer une nouvelle tâche non bloquée
  3. Réviser les blocages existants

Votre choix: _
```

## Mode Verbose

Avec `--verbose`, afficher le calcul détaillé:

```text
🔍 Analyse détaillée des tâches (méthode: valeur/temps)

Tâches "À faire": 5

Détail des calculs:

1. QUA-001 - Étapes de vérification du CV
   Valeur:
     - Priorité: Moyenne (5)
     - Urgence: Aucune date (0)
     - Ancienneté: 0 jours (0)
     - Total: 5

   Temps estimé: 1 heure
   Score final: 5.0 / 1 = 5.0 ⭐

   Raison: Tâche courte (1h) avec valeur correcte, excellent ratio

2. CNT-001 - Audit LinkedIn
   Valeur:
     - Priorité: Haute (10)
     - Urgence: < 7 jours (5)
     - Ancienneté: 8 jours (0.8)
     - Total: 15.8

   Temps estimé: 4 heures (estimé par défaut)
   Score final: 15.8 / 4 = 3.95

   Raison: Haute priorité mais plus longue

3. INF-001 - Intégration MCP
   Valeur:
     - Priorité: Moyenne (5)
     - Urgence: Aucune date (0)
     - Ancienneté: 0 jours (0)
     - Total: 5

   Temps estimé: 4 heures (estimé par défaut)
   Score final: 5 / 4 = 1.25

   Raison: Même valeur que QUA-001 mais 4× plus longue

[...]

Tâches bloquées (exclues): 0

Recommandation: QUA-001
  Score le plus élevé: 5.0
  "Quick win": haute valeur, faible temps

[Affichage normal de la suggestion]
```

## Optimisation du Workflow

Cette approche "valeur/temps" permet de:

- **Maximiser l'impact** en terminant plus de tâches importantes rapidement
- **Réduire le WIP** (Work In Progress) en évitant de bloquer sur des tâches longues
- **Augmenter la motivation** avec des victoires rapides
- **Maintenir le flux** en débloquant d'autres tâches plus vite

**Exemple de comparaison:**

Scénario A (ordre de priorité classique):
- 1. Haute priorité (8h) → Total après 8h: 1 tâche terminée

Scénario B (ordre valeur/temps):
- 1. Moyenne priorité (1h) → 1 tâche terminée
- 2. Moyenne priorité (2h) → 2 tâches terminées
- 3. Haute priorité (5h restantes) → 2.5/3 de la tâche haute priorité
- Total après 8h: 2 tâches terminées + progrès significatif sur la haute priorité

## Recommandations

**Si le temps estimé n'est pas renseigné:**
- Renseigner "Temps estimé" dans les métadonnées des tâches
- Améliore la précision des suggestions
- Peut être fait rétroactivement

**Si toutes les tâches ont le même score:**
- La priorité devient le critère principal
- Puis l'ancienneté (FIFO)

**Tâches urgentes:**
- Les tâches en retard ont automatiquement un score très élevé
- Elles seront suggérées en premier même si longues

## Exemple d'Utilisation

```bash
User: /task-next

Claude: 💡 Prochaine tâche suggérée: QUA-001

📋 Étapes de vérification du CV
🟡 Priorité: Moyenne
⏱️  Temps estimé: 1 heure
📅 Créée le: 2025-10-28
🎯 Section: General

📝 Contexte:
Définir une checklist de vérification pour s'assurer que le CV est complet.

✨ Pourquoi cette tâche?
  - Ratio valeur/temps élevé (Score: 5.0)
  - Tâche courte (1h) et impactante
  - "Quick win" pour progresser rapidement

Autres tâches à considérer:
  2. CNT-001 - Audit LinkedIn (Score: 3.75, 🔴 Haute, 4h)
  3. INF-001 - Intégration MCP (Score: 1.25, 🟡 Moyenne, 4h)

Commandes:
  /task-start QUA-001
  /task-next --start
```

## Références

- [TASKS.md](../.tasks/TASKS.md) - Dashboard des tâches
- [TASK_RULES.md](../.tasks/TASK_RULES.md) - Règles et workflow
- [Weighted Shortest Job First (WSJF)](https://www.scaledagileframework.com/wsjf/) - Méthodologie Agile
