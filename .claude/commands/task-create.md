---
description: Créer une nouvelle tâche de manière interactive avec auto-génération de l'ID
---

# Commande: task-create

Crée une nouvelle tâche de manière interactive en respectant le template et les conventions du projet.

## Utilisation

```bash
/task-create [--verbose]
```

## Options

- `--verbose`: Affiche des informations détaillées sur chaque étape

## Comportement

Cette commande guide l'utilisateur à travers un processus interactif pour créer une nouvelle tâche complète.

### Étape 1: Collecte des Informations

Poser les questions suivantes à l'utilisateur:

1. **Trigramme** (obligatoire)
   - Afficher la liste des trigrammes disponibles avec leur description
   - CNT (Content), TPL (Template), QUA (Quality), PIP (Pipeline), LAY (Layout), DOC (Documentation), INF (Infrastructure)
   - Valider que le trigramme choisi est valide

2. **Titre** (obligatoire)
   - Demander un titre court et descriptif (max 80 caractères)
   - Générer automatiquement un slug à partir du titre
   - Proposer le slug et permettre de le modifier

3. **Priorité** (obligatoire, défaut: Moyenne)
   - Proposer: 🔴 Haute / 🟡 Moyenne / 🟢 Basse
   - Défaut: 🟡 Moyenne

4. **Description** (obligatoire)
   - Demander une description claire du contexte
   - Demander l'objectif à atteindre

5. **Sous-tâches** (optionnel)
   - Demander de lister les sous-tâches (une par ligne)
   - Proposer d'en ajouter d'autres

6. **Section CV** (obligatoire)
   - Experience / Education / Skills / Sidebar / General / N/A
   - Défaut: General

7. **Date cible** (optionnel)
   - Proposer YYYY-MM-DD ou "aucune"
   - Valider le format si fourni

8. **Notes spécifiques** (optionnel)
   - Pour Claude: Instructions spécifiques pour l'IA
   - Pour l'utilisateur: Rappels personnels

### Étape 2: Génération de l'ID

1. Lire TASKS.md pour trouver le prochain ID disponible pour le trigramme
2. Générer l'ID: `XXX-NNN` (ex: CNT-003)
3. Vérifier l'unicité de l'ID (scanner tous les fichiers TASKS/*.md)
4. Afficher l'ID qui sera utilisé

### Étape 3: Création du Fichier

1. Lire .tasks/tasks/TEMPLATE.md
2. Remplacer tous les placeholders par les valeurs collectées:
   - `XXX-NNN` → ID généré
   - `[Titre de la tâche]` → Titre fourni
   - `[Titre court et descriptif]` → Titre fourni
   - `⏳ À faire` → Statut initial
   - `🟡 Moyenne` → Priorité choisie
   - `[CNT / TPL / ...]` → Trigramme choisi
   - `[Experience / ...]` → Section CV choisie
   - `YYYY-MM-DD` (Créé le) → Date du jour
   - `YYYY-MM-DD` (Cible) → Date cible ou vide
   - `X heures` → Temps estimé ou vide
   - Description sections → Texte fourni
   - Sous-tâches → Liste fournie avec `- [ ]`
   - Notes → Notes fournies
3. Supprimer le bloc de citation en haut du template
4. Ajouter une entrée dans "Historique des modifications" avec date et "Création | Tâche créée"
5. Écrire le fichier: `TASKS/{ID}-{slug}.md`

### Étape 4: Mise à Jour du Dashboard

1. Lire TASKS.md
2. Ajouter une ligne dans la table "Tâches actives":
   ```
   | [{ID}](TASKS/{ID}-{slug}.md) | {Titre} | ⏳ À faire | {Priorité} | {Date} |
   ```
   - Insérer selon l'ordre de priorité (Haute > Moyenne > Basse) puis par date

3. Mettre à jour les statistiques:

   - Incrémenter "Total"
   - Incrémenter "À faire"
   - Mettre à jour le prochain ID disponible pour ce trigramme

### Étape 5: Confirmation

Afficher un résumé:

```text
✅ Tâche créée avec succès!

ID: {ID}
Titre: {Titre}
Fichier: TASKS/{ID}-{slug}.md
Statut: ⏳ À faire
Priorité: {Priorité}

La tâche a été ajoutée à TASKS.md.
Utilisez `/task-start {ID}` pour commencer à travailler dessus.
```

## Validation

Avant de créer la tâche, vérifier:
- ✓ Le trigramme est valide
- ✓ L'ID généré est unique
- ✓ Le titre n'est pas vide
- ✓ Il y a au moins 2 sous-tâches
- ✓ La description contient contexte et objectif
- ✓ Le fichier n'existe pas déjà

## Gestion des Erreurs

**ID déjà utilisé:**
- Incrémenter automatiquement au prochain numéro disponible
- Afficher un warning

**Fichier existe déjà:**
- Mode interactif:
  1. Écraser le fichier existant
  2. Choisir un autre nom/ID
  3. Annuler l'opération

**Validation échouée:**
- Afficher clairement ce qui manque
- Permettre de compléter les champs manquants
- Ne pas créer la tâche tant que la validation échoue

**Format invalide:**
- Corriger automatiquement si possible (ex: date)
- Redemander la saisie sinon

## Mode Verbose

Avec `--verbose`, afficher en plus:
- Chaque étape du processus
- Les validations effectuées
- Les modifications apportées aux fichiers
- Le contenu complet du fichier créé

## Exemple d'Utilisation

```
User: /task-create

Claude: Je vais vous guider pour créer une nouvelle tâche.

1. Trigramme:
   - CNT (Content) - Contenu, informations du CV
   - TPL (Template) - Templates, structure, architecture
   - QUA (Quality) - Qualité, vérification, validation
   - PIP (Pipeline) - CI/CD, automatisation, build
   - LAY (Layout) - Mise en page, design, style visuel
   - DOC (Documentation) - Documentation, guides
   - INF (Infrastructure) - Infrastructure technique générale

   Votre choix: CNT

2. Titre de la tâche (max 80 caractères): Mise à jour de l'expérience professionnelle

3. Slug proposé: mise-a-jour-experience-professionnelle
   Confirmer ou modifier: [confirmer]

4. Priorité (Haute/Moyenne/Basse) [Moyenne]: Haute

5. Description - Contexte:
   L'expérience actuelle ne reflète pas les derniers projets réalisés.

6. Description - Objectif:
   Mettre à jour la section expérience avec les 3 derniers projets majeurs.

7. Sous-tâches (minimum 2, une par ligne, tapez 'fin' quand terminé):
   - Ajouter projet A
   - Ajouter projet B
   - Ajouter projet C
   - Mettre à jour les dates
   - fin

8. Section CV (Experience/Education/Skills/Sidebar/General/N/A) [General]: Experience

9. Date cible (YYYY-MM-DD ou 'aucune') [aucune]: 2025-11-01

10. Temps estimé (heures) [vide]: 1.5

✅ Tâche créée avec succès!

ID: CNT-002
Titre: Mise à jour de l'expérience professionnelle
Fichier: .tasks/tasks/CNT-002-mise-a-jour-experience-professionnelle.md
Statut: ⏳ À faire
Priorité: 🔴 Haute

La tâche a été ajoutée à TASKS.md.
Utilisez `/task-start CNT-002` pour commencer à travailler dessus.
```

## Références

- [TASK_RULES.md](../.tasks/TASK_RULES.md) - Règles DoR/DoD
- [.tasks/tasks/TEMPLATE.md](../.tasks/tasks/TEMPLATE.md) - Template de tâche
- [TASKS.md](../.tasks/TASKS.md) - Dashboard des tâches
