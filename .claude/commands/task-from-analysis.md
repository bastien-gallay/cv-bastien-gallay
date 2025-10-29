---
description: Créer des tâches depuis les recommandations d'une analyse
---

# Commande: task-from-analysis

Transforme les recommandations d'une analyse comparative en tâches concrètes à réaliser sur le CV.

## Utilisation

```bash
/task-from-analysis [--analysis-id=XXX-NNN] [--filter=high|medium|low|all] [--verbose]
```

## Options

- `--analysis-id`: ID de l'analyse à traiter (optionnel, sera demandé interactivement)
- `--filter`: Filtre de priorité (high, medium, low, all) - optionnel
- `--verbose`: Affiche des informations détaillées sur chaque étape

## Comportement

Cette commande automatise la création de tâches depuis les recommandations d'une analyse, en pré-remplissant les données et en maintenant la traçabilité.

### Étape 1: Sélection de l'Analyse

Si `--analysis-id` n'est pas fourni:

1. **Lire `.tasks/ANALYSES.md`**
2. **Lister les analyses avec recommandations pendantes**:

```text
Analyses disponibles avec recommandations pendantes:

1. CNT-001 - LinkedIn Audit
   - Source: linkedin.com/in/bastiengallay
   - Total: 19 recommandations
   - Pending: 19 (1 très haute, 10 hautes, 8 moyennes, 8 basses)
   - Fichier: resources/analyses/CNT-001/recommendations-status.md

Sélectionner une analyse (1-N ou ID):
```

3. **Valider la sélection**:
   - Vérifier que le fichier `recommendations-status.md` existe
   - Vérifier qu'il y a des recommandations pendantes (⏳ Pending)

Si aucune analyse avec recommandations pendantes:

```text
ℹ️  Aucune analyse avec recommandations pendantes trouvée.

Suggestions:
1. Créer une nouvelle analyse avec /analyze-source
2. Vérifier l'état dans .tasks/ANALYSES.md
```

### Étape 2: Affichage des Recommandations

1. **Lire le fichier `recommendations-status.md`**
2. **Parser les recommandations** en extrayant:
   - Numéro (RNN)
   - Titre
   - Catégorie
   - Référence CV
   - Trigramme suggéré
   - Statut (⏳ Pending uniquement)
   - Priorité (section où elle apparaît)

3. **Afficher groupé par priorité**:

```text
=== Recommandations pour CNT-001 ===

🔴🔴 TRÈS HAUTE (1 recommandation)
  1. [R01] Corriger l'écart critique sur Upwiser
     - Catégorie: Date incohérence
     - CV: src/cv.typ:122

🔴 HAUTE (10 recommandations)
  2. [R02] Corriger la date de fin CTO chez PALO IT - src/cv.typ:107
  3. [R03] Corriger les dates de Boonty - src/cv.typ:162
  4. [R04] Corriger les dates de début Freelance - src/cv.typ:169
  5. [R05] Ajouter les certifications manquantes - src/cv.typ:220-250
  [...]

🟡 MOYENNE (5 recommandations)
  12. [R12] Ajouter la langue Espagnol - src/cv.typ:66
  [...]

🟢 BASSE (3 recommandations)
  17. [R17] Ajouter Ruby Bordeaux au bénévolat
  [...]

Total: 19 recommandations pendantes
```

### Étape 3: Sélection des Recommandations

Proposer plusieurs modes de sélection:

```text
Sélection des recommandations à transformer en tâches:

Modes disponibles:
- Numéros: '1,5,6' ou '1-3,5' pour sélectionner spécifiquement
- 'all': Toutes les recommandations
- 'high': Priorité très haute + haute (🔴🔴 + 🔴)
- 'critical': Priorité très haute uniquement (🔴🔴)
- 'medium': Priorité moyenne (🟡)
- 'low': Priorité basse (🟢)

Votre sélection:
```

**Validation de la sélection**:

- Parser l'input (numéros, plages, mots-clés)
- Vérifier que tous les numéros existent
- Afficher les recommandations sélectionnées pour confirmation

```text
✓ 3 recommandations sélectionnées:
  - R01: Corriger l'écart critique sur Upwiser (🔴🔴)
  - R05: Ajouter les certifications manquantes (🔴)
  - R12: Ajouter la langue Espagnol (🟡)

Confirmer la création de 3 tâches ? (o/n):
```

### Étape 4: Création des Tâches

Pour chaque recommandation sélectionnée, **lancer une création de tâche interactive** avec des valeurs pré-remplies:

#### 4.1 Préparer les Données

Extraire du fichier `recommendations-status.md`:

- **Titre**: Utiliser le titre de la recommandation (ex: "Corriger l'écart critique sur Upwiser")
- **Trigramme**: Utiliser le "Trigramme suggéré" (généralement CNT)
- **Catégorie**: Utiliser la "Catégorie" pour la description contextuelle
- **Référence CV**: Utiliser pour les notes techniques
- **Priorité**: Mapper selon la section:
  - 🔴🔴 Très Haute → 🔴 Haute
  - 🔴 Haute → 🔴 Haute
  - 🟡 Moyenne → 🟡 Moyenne
  - 🟢 Basse → 🟢 Basse

Lire aussi le fichier `recommendations.md` pour obtenir la **description complète** de la recommandation.

#### 4.2 Mode Interactif ou Automatique

**Mode par défaut (interactif)**:

Afficher les données pré-remplies et permettre modification:

```text
=== Création de tâche 1/3 ===

Recommandation: R01 - Corriger l'écart critique sur Upwiser

Données pré-remplies (appuyez sur Entrée pour accepter):

1. Trigramme [CNT]:
2. Titre [Corriger l'écart critique sur Upwiser]:
3. Priorité [🔴 Haute]:
4. Description (pré-remplie depuis recommendations.md)
   - Contexte: Date de fin très différente entre LinkedIn et CV
   - Objectif: Corriger la date de fin pour Upwiser

   Modifier ? (o/n): n

5. Sous-tâches suggérées:
   - [ ] Vérifier la date exacte sur LinkedIn
   - [ ] Mettre à jour src/cv.typ:122
   - [ ] Valider la cohérence avec les autres dates
   - [ ] Compiler et vérifier le PDF

   Ajouter/Modifier ? (o/n): n

6. Section CV [Experience]:
7. Date cible [aucune]:
8. Temps estimé [0.5]:

Créer cette tâche ? (o/n): o
```

**Mode automatique** (avec `--auto`):

Créer directement les tâches avec les valeurs pré-remplies, sans demander confirmation.

#### 4.3 Créer la Tâche

1. **Générer l'ID** (utiliser le workflow de `/task-create`):
   - Lire TASKS.md
   - Trouver le prochain ID pour le trigramme (ex: CNT-002)
   - Vérifier l'unicité

2. **Créer le fichier de tâche**:
   - Utiliser le template `.tasks/tasks/TEMPLATE.md`
   - Remplir tous les champs
   - **Ajouter une référence dans "Origine"**:

   ```markdown
   **Origine:** Recommandation [CNT-001-R01](../resources/analyses/CNT-001/recommendations-status.md#r01---corriger-lécart-critique-sur-upwiser) depuis l'analyse [CNT-001](../resources/analyses/CNT-001/)
   ```

3. **Mettre à jour TASKS.md**:
   - Ajouter la ligne dans "Tâches actives"
   - Mettre à jour les statistiques

4. **Confirmer la création**:

```text
✓ Tâche CNT-002 créée avec succès!
  Fichier: .tasks/tasks/CNT-002-corriger-ecart-critique-upwiser.md
  Origine: CNT-001-R01
```

### Étape 5: Mise à Jour du Suivi

Pour chaque tâche créée, mettre à jour le fichier `recommendations-status.md`:

#### 5.1 Marquer la Recommandation

Transformer:

```markdown
- [ ] **R01 - Corriger l'écart critique sur Upwiser**
  - Catégorie: Date incohérence
  - Source: [recommendations.md](./recommendations.md#r01---corriger-lécart-critique-sur-upwiser)
  - Référence CV: [src/cv.typ:122](../../../src/cv.typ#L122)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending
```

En:

```markdown
- [x] **R01 - Corriger l'écart critique sur Upwiser**
  - Catégorie: Date incohérence
  - Source: [recommendations.md](./recommendations.md#r01---corriger-lécart-critique-sur-upwiser)
  - Référence CV: [src/cv.typ:122](../../../src/cv.typ#L122)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-002](../../tasks/CNT-002-corriger-ecart-critique-upwiser.md)
  - Statut: 🔄 Task created
  - Date création tâche: 2025-10-29
```

#### 5.2 Mettre à Jour les Statistiques

Recalculer et mettre à jour la section "Statistiques" en haut du fichier:

```markdown
## Statistiques

| Statut | Nombre | Pourcentage |
|--------|--------|-------------|
| ⏳ Pending | 16 | 84% |
| 🔄 Task created | 3 | 16% |
| ✅ Completed | 0 | 0% |
```

Et aussi mettre à jour les compteurs par section de priorité:

```markdown
## 🔴🔴 Priorité TRÈS HAUTE (0/1 items pending)
## 🔴 Priorité HAUTE (8/10 items pending)
```

### Étape 6: Mise à Jour du Dashboard

#### 6.1 Mettre à Jour ANALYSES.md

**Section "Analyses Actives"** - modifier la ligne de l'analyse:

```markdown
| [CNT-001](resources/analyses/CNT-001/) | LinkedIn Audit | [linkedin.com/in/bastiengallay](https://linkedin.com/in/bastiengallay/) | ✅ Terminé | 2025-10-29 | 19 total (1 très haute, 10 hautes, 8 moyennes, 8 basses) | 3/19 |
```

**Section "Statistiques Globales"**:

- Incrémenter "Tâches créées depuis analyses": 0 → 3
- Mettre à jour "Recommandations pendantes": 19 → 16 (84%)

#### 6.2 Optionnel: Mettre à Jour la Tâche d'Analyse

Si la tâche d'analyse originale (ex: CNT-001) existe et est encore ouverte, proposer:

```text
Souhaitez-vous ajouter une référence aux tâches créées dans CNT-001-linkedin-audit.md ?
(o/n):
```

Si oui, ajouter dans la section "Résultat final" ou "Historique":

```markdown
**Tâches créées depuis cette analyse:**
- [CNT-002](CNT-002-corriger-ecart-critique-upwiser.md) - R01: Corriger l'écart critique sur Upwiser
- [CNT-003](CNT-003-ajouter-certifications-manquantes.md) - R05: Ajouter les certifications manquantes
- [CNT-004](CNT-004-ajouter-langue-espagnol.md) - R12: Ajouter la langue Espagnol
```

### Étape 7: Résumé Final

Afficher un résumé complet de l'opération:

```text
✅ Transformation terminée avec succès!

📊 Résumé:
   - Analyse: CNT-001 (LinkedIn Audit)
   - Recommandations sélectionnées: 3
   - Tâches créées: 3
   - Tâches échouées: 0

📝 Tâches créées:
   1. CNT-002 - Corriger l'écart critique sur Upwiser (🔴 Haute)
      Origine: CNT-001-R01
      Fichier: .tasks/tasks/CNT-002-corriger-ecart-critique-upwiser.md

   2. CNT-003 - Ajouter les certifications manquantes (🔴 Haute)
      Origine: CNT-001-R05
      Fichier: .tasks/tasks/CNT-003-ajouter-certifications-manquantes.md

   3. CNT-004 - Ajouter la langue Espagnol (🟡 Moyenne)
      Origine: CNT-001-R12
      Fichier: .tasks/tasks/CNT-004-ajouter-langue-espagnol.md

📈 État de l'analyse CNT-001:
   - Recommandations restantes: 16/19 (84%)
   - Priorité très haute: 0/1 restantes
   - Priorité haute: 8/10 restantes

🚀 Prochaines étapes:
   - Utiliser /task-start CNT-002 pour commencer
   - Consulter .tasks/TASKS.md pour voir toutes les tâches
   - Utiliser /task-from-analysis pour créer d'autres tâches depuis CNT-001
```

## Validation

Avant de créer les tâches, vérifier:

- [ ] L'analyse existe dans ANALYSES.md
- [ ] Le fichier recommendations-status.md existe
- [ ] Il y a des recommandations avec statut "⏳ Pending"
- [ ] Les recommandations sélectionnées sont valides
- [ ] Les IDs de tâches générés sont uniques
- [ ] Les trigrammes suggérés sont valides

Pendant la création:

- [ ] Chaque tâche respecte le template
- [ ] Les références croisées sont correctes (analyse ↔ recommandation ↔ tâche)
- [ ] Les statistiques sont recalculées correctement

## Gestion des Erreurs

### Erreur: Analyse inexistante

```text
❌ Erreur: L'analyse CNT-XXX n'existe pas dans ANALYSES.md

Suggestions:
1. Vérifier l'ID dans .tasks/ANALYSES.md
2. Créer une nouvelle analyse avec /analyze-source
3. Lister les analyses disponibles

Action:
```

### Erreur: Aucune recommandation pendante

```text
ℹ️  L'analyse CNT-001 n'a plus de recommandations pendantes.

Statut actuel:
- Total: 19 recommandations
- Tâches créées: 19 (100%)
- Complétées: 15 (79%)

Toutes les recommandations ont déjà été transformées en tâches.
```

### Erreur: Fichier recommendations-status.md manquant

```text
❌ Erreur: Le fichier recommendations-status.md n'existe pas pour CNT-001

Fichier attendu: .tasks/resources/analyses/CNT-001/recommendations-status.md

Suggestions:
1. Vérifier la structure de l'analyse
2. Créer le fichier depuis recommendations.md
3. Utiliser le template recommendations-template.md
```

### Erreur: Sélection invalide

```text
❌ Erreur: Sélection invalide '1,25,99'

Les recommandations suivantes n'existent pas: 25, 99
Recommandations disponibles: 1-19

Veuillez réessayer:
```

### Erreur: Création de tâche échouée

Si une création de tâche échoue au milieu du batch:

```text
⚠️  Erreur lors de la création de la tâche pour R05

Statut:
- Tâches créées: 1/3 (CNT-002)
- Tâche échouée: R05 (raison: ID collision)
- Non traitées: R12

Options:
1. Continuer avec les recommandations restantes
2. Annuler toute l'opération (rollback)
3. Réessayer cette recommandation

Choix [1-3]:
```

### Erreur: Problème de mise à jour des fichiers

Si la mise à jour de recommendations-status.md ou ANALYSES.md échoue:

```text
⚠️  Avertissement: Les tâches ont été créées mais la mise à jour du suivi a échoué

Tâches créées:
- CNT-002: ✓ Créée
- CNT-003: ✓ Créée

Fichiers à mettre à jour manuellement:
- .tasks/resources/analyses/CNT-001/recommendations-status.md
- .tasks/ANALYSES.md

Voulez-vous réessayer la mise à jour automatique ? (o/n):
```

## Mode Verbose

Avec l'option `--verbose`, afficher:

- Chaque étape du parsing des fichiers
- Les données extraites pour chaque recommandation
- Les valeurs pré-remplies pour chaque tâche
- Les modifications apportées à chaque fichier (diff)
- Les statistiques avant/après
- Les chemins complets des fichiers créés/modifiés

## Mode Automatique

Avec l'option `--auto` (à documenter):

- Pas de confirmation pour chaque tâche
- Utilise toutes les valeurs pré-remplies
- Création en batch sans interruption
- Affiche uniquement le résumé final

Usage:

```bash
/task-from-analysis --analysis-id=CNT-001 --filter=high --auto
```

## Exemple d'Utilisation Complet

```bash
$ /task-from-analysis

🔍 Transformation de Recommandations en Tâches

Analyses disponibles:
1. CNT-001 - LinkedIn Audit (19 recommandations pendantes)

Sélectionner une analyse: 1

=== Recommandations pour CNT-001 ===

🔴🔴 TRÈS HAUTE (1)
  1. [R01] Corriger l'écart critique sur Upwiser

🔴 HAUTE (10)
  2. [R02] Corriger la date de fin CTO chez PALO IT
  [...]

🟡 MOYENNE (5)
  12. [R12] Ajouter la langue Espagnol
  [...]

🟢 BASSE (3)
  [...]

Sélection (numéros, 'all', 'high', 'critical', 'medium', 'low'): high

✓ 11 recommandations sélectionnées (1 très haute + 10 hautes)

Confirmer la création de 11 tâches ? (o/n): o

=== Création de tâche 1/11 ===

Recommandation: R01 - Corriger l'écart critique sur Upwiser

[... mode interactif ...]

✓ Tâche CNT-002 créée!

=== Création de tâche 2/11 ===
[...]

✅ Transformation terminée!

📊 Résumé: 11 tâches créées
📈 État: 8/19 recommandations restantes (42%)
🚀 Prochaine étape: /task-start CNT-002
```

## Références

- [ANALYSES.md](../../.tasks/ANALYSES.md) - Dashboard des analyses
- [recommendations-status.md](../../.tasks/resources/analyses/CNT-001/recommendations-status.md) - Exemple de suivi
- [task-create.md](./task-create.md) - Commande de création de tâche
- [TASK_RULES.md](../../.tasks/TASK_RULES.md) - Règles de gestion

## Notes pour Claude

**Instructions pour l'exécution:**

1. **Traçabilité absolue**: Chaque tâche doit référencer sa recommandation d'origine, et vice-versa
2. **Atomicité**: Si une création échoue, proposer de continuer ou rollback
3. **Statistiques précises**: Toujours recalculer, ne pas juste incrémenter
4. **Mode interactif par défaut**: Permettre validation/modification avant chaque création
5. **Parsing robuste**: Gérer les formats de sélection ('1-3,5,7', 'all', 'high', etc.)
6. **Pré-remplissage intelligent**:
   - Lire recommendations.md pour la description complète
   - Mapper correctement les priorités
   - Générer des sous-tâches pertinentes selon la catégorie
7. **Mise à jour synchronisée**:
   - recommendations-status.md
   - ANALYSES.md
   - TASKS.md
   - Fichier de tâche d'analyse (optionnel)
8. **Workflow itératif**: Permettre plusieurs appels à la commande pour traiter progressivement les recommandations
9. **Ne pas modifier recommendations.md**: C'est le fichier source, ne toucher que recommendations-status.md
10. **Références relatives**: Utiliser des chemins relatifs corrects pour les liens markdown entre fichiers
