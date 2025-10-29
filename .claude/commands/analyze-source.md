---
description: Extraire et structurer des informations depuis une source externe (LinkedIn, GitHub, etc.)
---

# Commande: analyze-source

Extrait et structure des informations depuis une source externe (profil LinkedIn, GitHub, CV externe, website) pour les comparer avec le CV actuel.

## Utilisation

```bash
/analyze-source [--task-id=CNT-XXX] [source-type] [informations-source]
```

## Options

- `--task-id`: ID de la tâche parent (optionnel, sera demandé interactivement)
- `source-type`: Type de source à analyser (LinkedIn, GitHub, CV, Website, Autre)
- `informations-source`: URL ou description de la source (optionnel, sera demandé interactivement)

## Comportement

Cette commande guide l'utilisateur dans l'extraction structurée de données depuis une source externe, pour faciliter ensuite l'analyse comparative.

### Étape 1: Sélection du Type de Source (si non fourni)

Afficher les options suivantes:

```text
Quel type de source souhaitez-vous analyser ?

1. LinkedIn Profile
2. GitHub Profile
3. CV Externe (PDF/Word)
4. Website/Blog
5. Autre

Choix (1-5):
```

### Étape 2: Informations de Base

Demander:

1. **URL ou description de la source** (obligatoire)
   - Pour LinkedIn: URL du profil
   - Pour GitHub: Username ou URL
   - Pour CV: Nom du fichier ou description
   - Pour Website: URL

2. **ID de la tâche parent** (si non fourni en paramètre)
   - Chercher dans `.tasks/tasks/` les tâches CNT en cours
   - Proposer la liste ou permettre de saisir manuellement
   - Si aucune tâche: suggérer de créer d'abord une tâche d'audit avec `/task-create`

### Étape 3: Extraction Guidée

Selon le type de source choisi, charger le template approprié depuis:

- `.tasks/resources/templates/source-extraction-template.md`

Guider l'utilisateur section par section:

**Pour LinkedIn (exemple):**

```markdown
=== Section 1/10: Informations de profil ===

Veuillez copier-coller ou saisir les informations suivantes de votre profil LinkedIn:

- Nom complet:
- Headline:
- Localisation:
- Réseau (followers/connections):
- Emploi actuel:

[Continuer] / [Passer] / [Annuler]
```

Répéter pour chaque section:

- Informations de profil
- Expériences professionnelles
- Éducation
- Langues
- Certifications
- Compétences
- Bénévolat
- Publications/Projets
- Recommandations
- Sites web

**Pour GitHub (exemple):**

Sections:

- Informations de profil
- Statistiques globales
- Repositories principaux (top 10)
- Langages de programmation
- Contributions notables
- Activité récente

### Étape 4: Sauvegarde

1. **Créer le dossier d'audit** si nécessaire:

   ```bash
   mkdir -p .tasks/resources/audits/[TASK-ID]
   ```

2. **Générer le nom de fichier**:
   - LinkedIn: `linkedin-profile.md`
   - GitHub: `github-profile.md`
   - CV Externe: `cv-externe-[source].md`
   - Website: `website-[domain].md`
   - Autre: `source-[description].md`

3. **Sauvegarder le fichier** avec:
   - Métadonnées en en-tête (date, source, type, méthode)
   - Contenu structuré par sections
   - Notes d'extraction (difficultés, éléments manquants)

4. **Afficher confirmation**:

   ```markdown
   ✓ Extraction sauvegardée: .tasks/resources/audits/CNT-001/linkedin-profile.md
   ✓ 10/10 sections complétées

   Prochaines étapes:
   1. Créer le fichier d'analyse comparative (manuel)
   2. Créer les recommandations issues de l'analyse
   3. Utiliser /task-from-analysis pour créer les tâches
   ```

### Étape 5: Mise à Jour Optionnelle

Si une tâche parent existe, proposer:

```markdown
Souhaitez-vous ajouter une référence à ce fichier dans la tâche [TASK-ID] ?
(o/n):
```

Si oui, ajouter dans la section "Résultat final" de la tâche:

```markdown
**Fichiers créés:**
- [linkedin-profile.md](../../resources/audits/CNT-001/linkedin-profile.md) - Extraction du profil LinkedIn
```

## Validation

Avant de sauvegarder, vérifier:

- [ ] Au moins 3 sections ont du contenu
- [ ] Les métadonnées sont complètes (date, source, type)
- [ ] Le nom de fichier suit la convention
- [ ] Le dossier de destination existe
- [ ] Le fichier ne sera pas écrasé (ou demander confirmation)

## Gestion des Erreurs

### Erreur: Tâche parent inexistante

```markdown
❌ Erreur: La tâche CNT-XXX n'existe pas dans .tasks/tasks/

Suggestions:
1. Vérifier l'ID de la tâche dans .tasks/TASKS.md
2. Créer d'abord une tâche d'audit avec /task-create
3. Continuer sans tâche parent (extraction autonome)

Action [1-3 / annuler]:
```

### Erreur: Fichier existe déjà

```markdown
⚠️  Le fichier .tasks/resources/audits/CNT-001/linkedin-profile.md existe déjà.

Actions possibles:
1. Écraser le fichier existant
2. Créer avec un suffixe (linkedin-profile-2.md)
3. Fusionner avec l'existant (manuel)
4. Annuler l'opération

Choix [1-4]:
```

## Mode Verbose

Avec l'option `--verbose`, afficher:

- Chemin complet de chaque fichier créé
- Nombre de caractères par section
- Statistiques de complétude
- Template utilisé
- Commandes git suggérées pour commit

## Exemple d'Utilisation

```bash
$ /analyze-source --task-id=CNT-001

🔍 Analyse de Source Externe

Quel type de source ?
> 1 (LinkedIn Profile)

URL du profil LinkedIn:
> https://www.linkedin.com/in/johndoe/

=== Extraction Guidée (1/10) ===

Nom complet:
> John Doe

[... extraction interactive ...]

✓ Extraction sauvegardée dans .tasks/resources/audits/CNT-001/linkedin-profile.md
✓ Référence ajoutée à la tâche CNT-001

Prochaines étapes recommandées:
1. Lire le CV actuel pour comparaison
2. Créer le rapport d'analyse comparative
3. Identifier les recommandations
4. Utiliser /task-from-analysis
```

## Références

- [Template d'extraction](../../.tasks/resources/templates/source-extraction-template.md)
- [ANALYSES.md](../../.tasks/ANALYSES.md) - Dashboard des analyses
- [TASK_RULES.md](../../.tasks/TASK_RULES.md) - Règles de gestion

## Notes pour Claude

**Instructions pour l'exécution:**

1. **Mode interactif prioritaire:** Toujours guider l'utilisateur, ne pas essayer de deviner
2. **Validation à chaque étape:** Permettre modification avant sauvegarde
3. **Sauvegarde progressive:** Ne pas perdre les données si interruption
4. **Templates flexibles:** Adapter selon le type de source
5. **Ne pas créer de tâches:** Cette commande extrait seulement, ne crée pas de tâches
6. **WebFetch si possible:** Proposer d'utiliser WebFetch pour LinkedIn/GitHub si accessible
7. **Respecter la structure:** Utiliser les templates dans `.tasks/resources/templates/`
