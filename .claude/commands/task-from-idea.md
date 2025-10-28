---
description: Créer une nouvelle tâche depuis une idée du backlog
---

# Commande: task-from-idea

Transforme une idée du backlog [IDEAS.md](../IDEAS.md) en tâche concrète.

## Utilisation

```bash
/task-from-idea [--verbose]
```

## Options

- `--verbose`: Affiche des informations détaillées sur chaque étape

## Comportement

Cette commande facilite la création de tâches à partir des idées collectées lors de précédentes finalisations de tâches.

### Étape 1: Lecture du Backlog

1. **Lire IDEAS.md**
   - Parser le fichier pour extraire toutes les idées
   - Grouper par trigramme

2. **Vérifier qu'il y a des idées**
   - Si aucune idée: afficher message et proposer `/task-create`
   - Sinon: continuer

### Étape 2: Sélection Interactive

Afficher toutes les idées disponibles:

```text
💡 Idées disponibles dans le backlog

## Documentation (DOC)
1. Suggérer des réponses automatiques aux questions de collecte d'informations lors de la complétion des tâches
   Source: DOC-001 | Date: 2025-10-28

## Contenu (CNT)
2. Ajouter support multilingue pour le CV
   Source: CNT-002 | Date: 2025-10-25

## Template (TPL)
3. Créer variante minimaliste du template
   Source: TPL-001 | Date: 2025-10-20

Total: 3 idées

Choisissez une idée (1-3) ou 0 pour annuler: _
```

**Validation:**
- Numéro entre 1 et N (nombre total d'idées)
- 0 pour annuler
- Autre input: redemander

### Étape 3: Extraction des Informations

Une fois l'idée sélectionnée, extraire:

1. **Trigramme**
   - Depuis la section où l'idée est listée
   - Sera le trigramme par défaut de la nouvelle tâche

2. **Titre de l'idée**
   - Texte avant "(source: ...)"
   - Sera le titre par défaut de la nouvelle tâche

3. **Source et date**
   - ID de la tâche source
   - Date d'ajout au backlog
   - Seront mentionnés dans le contexte

### Étape 4: Création de la Tâche

Lancer le processus de création similaire à `/task-create` mais avec **pré-remplissage**:

1. **Trigramme** (pré-rempli, éditable)
   ```
   1. Trigramme:
      Suggestion basée sur l'idée: DOC

      Confirmer DOC ou choisir un autre trigramme: [DOC]
   ```

2. **Titre** (pré-rempli, éditable)
   ```
   2. Titre de la tâche (max 80 caractères):
      Suggestion: Suggérer des réponses automatiques aux questions...

      Confirmer ou modifier: [confirmer]
   ```

3. **Slug** (auto-généré depuis le titre)
   ```
   3. Slug proposé: suggerer-reponses-automatiques
      Confirmer ou modifier: [confirmer]
   ```

4. **Priorité** (demander, défaut: Moyenne)
   ```
   4. Priorité (Haute/Moyenne/Basse) [Moyenne]:
   ```

5. **Description - Contexte** (pré-rempli avec source)
   ```
   5. Description - Contexte:
      Suggestion: Idée issue de la tâche DOC-001 (2025-10-28).

      Modifier ou compléter le contexte:
   ```

6. **Description - Objectif** (demander)
   ```
   6. Description - Objectif:
   ```

7. **Sous-tâches** (demander normalement)
   ```
   7. Sous-tâches (optionnel, une par ligne, tapez 'fin'):
   ```

8. **Section CV** (demander normalement)
   ```
   8. Section CV (Experience/Education/Skills/Sidebar/General/N/A) [General]:
   ```

9. **Date cible** (demander normalement)
   ```
   9. Date cible (YYYY-MM-DD ou 'aucune') [aucune]:
   ```

10. **Temps estimé** (demander normalement)
    ```
    10. Temps estimé (heures) [vide]:
    ```

### Étape 5: Création du Fichier de Tâche

Identique à `/task-create`:

1. Générer l'ID (prochain disponible pour le trigramme)
2. Créer le fichier depuis TEMPLATE.md avec toutes les valeurs
3. Ajouter l'entrée dans TASKS.md
4. Mettre à jour les statistiques

### Étape 6: Suppression de l'Idée du Backlog

1. **Retirer l'idée de IDEAS.md**
   - Supprimer la ligne correspondante
   - Si c'était la seule idée de la section: remettre "*Aucune idée pour l'instant*"

2. **Confirmation**
   ```text
   ✓ Idée retirée du backlog IDEAS.md
   ```

### Étape 7: Confirmation Finale

Afficher un résumé complet:

```text
✅ Tâche créée depuis une idée du backlog!

💡 Idée d'origine:
"Suggérer des réponses automatiques aux questions..."
Source: DOC-001 (2025-10-28)

📋 Nouvelle tâche:
ID: DOC-002
Titre: Suggérer des réponses automatiques
Fichier: TASKS/DOC-002-suggerer-reponses-automatiques.md
Statut: ⏳ À faire
Priorité: 🟡 Moyenne

📂 Actions effectuées:
  ✓ Tâche créée et ajoutée à TASKS.md
  ✓ Statistiques mises à jour
  ✓ Idée retirée de IDEAS.md

Utilisez `/task-start DOC-002` pour commencer à travailler dessus.
```

## Validation

Avant de créer la tâche:
- ✓ Une idée a été sélectionnée
- ✓ L'ID généré est unique
- ✓ Tous les champs obligatoires sont remplis
- ✓ Le fichier n'existe pas déjà

## Gestion des Erreurs

**Aucune idée dans le backlog:**

```text
📭 Le backlog est vide

Aucune idée n'est actuellement disponible dans IDEAS.md.

Les idées sont ajoutées automatiquement lorsque vous complétez
des tâches avec `/task-complete` et remplissez "Améliorations futures".

Options:
1. Créer une nouvelle tâche normalement (/task-create)
2. Annuler

Votre choix: _
```

**Sélection invalide:**

```text
❌ Sélection invalide: "abc"

Veuillez choisir un numéro entre 1 et 3, ou 0 pour annuler.

Votre choix: _
```

**Erreur lors de la création:**

```text
❌ Erreur lors de la création de la tâche

{Message d'erreur détaillé}

L'idée n'a pas été retirée du backlog et peut être réessayée.
```

**IDEAS.md introuvable:**

```text
❌ Erreur: Fichier IDEAS.md introuvable

Le fichier de backlog d'idées n'existe pas encore.

Il sera créé automatiquement lors de la première utilisation
de /task-complete avec une amélioration future.

Voulez-vous créer une tâche normalement? (/task-create)
```

## Mode Verbose

Avec `--verbose`, afficher:
- Contenu complet de IDEAS.md lu
- Parsing détaillé de chaque idée
- Extraction des métadonnées
- Chaque étape de création de la tâche
- Diff de IDEAS.md avant/après suppression

## Avantages de cette Approche

**Traçabilité:**
- Lien direct entre l'idée originale et la nouvelle tâche
- Contexte automatiquement rempli avec la source

**Efficacité:**
- Pas besoin de se rappeler des idées précédentes
- Titre et trigramme déjà suggérés
- Gain de temps sur la saisie

**Organisation:**
- Backlog centralisé et structuré
- Priorisation facilitée (choisir parmi toutes les idées)
- Évite les oublis

## Workflow Complet

```bash
# 1. Terminer une tâche avec une idée
/task-complete DOC-001
> Améliorations futures: Automatiser les suggestions de réponses
✓ Idée ajoutée au backlog IDEAS.md

# 2. Plus tard, transformer l'idée en tâche
/task-from-idea
> Idées disponibles: ...
> Choix: 1
> [Guide interactif avec pré-remplissage]
✓ Tâche DOC-002 créée
✓ Idée retirée du backlog

# 3. Travailler sur la nouvelle tâche
/task-start DOC-002
```

## Cas Spéciaux

### Modification du Trigramme

Si l'utilisateur change le trigramme suggéré:

```text
1. Trigramme:
   Suggestion basée sur l'idée: DOC

   Confirmer DOC ou choisir un autre trigramme: TPL

⚠️  Vous avez changé le trigramme de DOC à TPL.
L'idée était catégorisée sous "Documentation".
Confirmer ce changement? (o/N): o

✓ Trigramme changé vers TPL
```

### Idée Déjà Transformée

Si une idée a déjà été transformée mais réapparaît (édition manuelle):

```text
⚠️  Warning: L'idée sélectionnée semble déjà avoir été transformée

Une tâche DOC-002 existe déjà avec un titre similaire.

Options:
1. Créer quand même une nouvelle tâche (doublon possible)
2. Choisir une autre idée
3. Annuler

Votre choix: _
```

### Édition Avancée

Pour les utilisateurs avancés qui veulent plus de contrôle:

```text
Après sélection de l'idée, proposer:

Voulez-vous:
1. Utiliser le mode guidé (pré-remplissage automatique)
2. Passer en mode manuel complet
3. Annuler

Votre choix: _
```

## Exemple d'Utilisation

```bash
User: /task-from-idea

Claude: 💡 Idées disponibles dans le backlog

## Documentation (DOC)
1. Suggérer des réponses automatiques aux questions de collecte
   Source: DOC-001 | Date: 2025-10-28

## Contenu (CNT)
2. Ajouter support multilingue pour le CV
   Source: CNT-002 | Date: 2025-10-25

Total: 2 idées

Choisissez une idée (1-2) ou 0 pour annuler: 1

Création d'une tâche depuis l'idée sélectionnée...

1. Trigramme:
   Suggestion: DOC
   Confirmer ou modifier [DOC]: [Enter]

2. Titre:
   Suggestion: Suggérer des réponses automatiques aux questions de collecte
   Confirmer ou modifier: [Enter]

3. Slug proposé: suggerer-reponses-automatiques
   Confirmer ou modifier: [Enter]

4. Priorité (Haute/Moyenne/Basse) [Moyenne]: Haute

5. Description - Contexte:
   Pré-rempli: "Idée issue de la tâche DOC-001 (2025-10-28)."
   Compléter: Améliorer l'expérience utilisateur lors de la complétion des tâches

6. Description - Objectif:
   Analyser le contexte et l'historique Git pour suggérer automatiquement des réponses pertinentes

7. Sous-tâches (une par ligne, 'fin' pour terminer):
   - Analyser les commits liés à la tâche
   - Extraire les patterns de changements
   - Générer des suggestions contextuelles
   - fin

8. Section CV [General/N/A]: N/A

9. Date cible [aucune]: aucune

10. Temps estimé (heures) [vide]: 3

✅ Tâche créée depuis une idée du backlog!

💡 Idée d'origine:
"Suggérer des réponses automatiques aux questions de collecte"
Source: DOC-001 (2025-10-28)

📋 Nouvelle tâche:
ID: DOC-002
Titre: Suggérer des réponses automatiques aux questions de collecte
Fichier: TASKS/DOC-002-suggerer-reponses-automatiques.md
Statut: ⏳ À faire
Priorité: 🔴 Haute

📂 Actions effectuées:
  ✓ Tâche créée et ajoutée à TASKS.md
  ✓ Statistiques mises à jour
  ✓ Idée retirée de IDEAS.md

Utilisez `/task-start DOC-002` pour commencer à travailler dessus.
```

## Références

- [IDEAS.md](../IDEAS.md) - Backlog d'idées
- [task-create.md](task-create.md) - Création de tâche classique
- [task-complete.md](task-complete.md) - Ajout automatique d'idées
- [TASKS.md](../TASKS.md) - Dashboard des tâches
