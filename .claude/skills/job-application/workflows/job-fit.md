# Job-Fit Workflow

Analyse l'adéquation entre le profil et le poste avec validation interactive.

## Usage

```bash
job-fit [--application=ID]
```

**Options:**

- `--application`: ID de candidature. Défaut: dernière analyse

## Prérequis

Une analyse d'offre doit exister (`job-analyze`)

## Workflow d'exécution

### Étape 1: Charger les données

```text
1. Charger data/applications/{app_id}/{app_id}-analysis.md
2. Charger le CV source (src/cv.typ + modules shared/)
3. Extraire les compétences et expériences du profil
```

### Étape 2: Comparer les exigences

**Pour chaque exigence must-have:**

```text
Statut possible:
- Satisfaite: preuve claire dans le profil
- Partiellement satisfaite: compétence proche ou en cours d'acquisition
- Non satisfaite: pas de preuve dans le profil
```

**Pour chaque exigence nice-to-have:**

```text
Même logique, mais impact moindre sur le score
```

### Étape 3: Calculer le score d'adéquation

```text
score = (
    must_have_match * 0.60 +      # 60% poids exigences obligatoires
    nice_to_have_match * 0.20 +   # 20% poids exigences souhaitées
    experience_relevance * 0.15 + # 15% pertinence expériences
    culture_fit * 0.05            # 5% adéquation culturelle
) * 100

Arrondi à l'entier
```

**Interprétation:**

| Score | Niveau | Recommandation |
|-------|--------|----------------|
| 80-100 | Excellent | Candidature prioritaire |
| 60-79 | Bon | Candidature recommandée |
| 40-59 | Moyen | À évaluer selon motivation |
| 0-39 | Faible | Candidature risquée |

### Étape 4: Identifier les forces et lacunes

**Forces:**

- Compétences qui matchent exactement
- Expériences très pertinentes
- Certifications demandées possédées

**Lacunes:**

- Exigences non satisfaites
- Écarts d'expérience
- Technologies non maîtrisées

### Étape 5: Générer les talking points

Pour chaque force/lacune, préparer un argument:

```text
Force: "Mon expérience en X démontre que..."
Lacune: "Bien que je n'aie pas Y, mon expérience en Z est transférable car..."
```

### Étape 6: Générer le rapport initial

Créer `data/applications/{app_id}/{app_id}-fit-report.md`:

```markdown
# Adéquation : {Titre du poste} @ {Entreprise}

**Date d'analyse:** {date}
**Score global:** {score}/100

## Synthèse

{Résumé en 2-3 phrases de l'adéquation}

## Correspondance des exigences

### Exigences satisfaites ({n}/{total})

| Exigence | Preuve dans le profil |
|----------|----------------------|
| {exigence} | {expérience/compétence qui prouve} |
| ... | ... |

### Exigences partiellement satisfaites ({n}/{total})

| Exigence | Situation actuelle | Recommandation |
|----------|-------------------|----------------|
| {exigence} | {état actuel} | {comment compenser} |
| ... | ... | ... |

### Exigences non satisfaites ({n}/{total})

| Exigence | Impact | Stratégie |
|----------|--------|-----------|
| {exigence} | {Faible/Moyen/Fort} | {comment adresser} |
| ... | ... | ... |

## Points forts à valoriser

1. **{titre}:** {description et preuve}
2. **{titre}:** {description et preuve}
3. ...

## Lacunes à adresser

1. **{lacune}:** {stratégie pour compenser}
2. **{lacune}:** {stratégie pour compenser}
3. ...

## Talking points pour l'entretien

### Valoriser les forces

- "{phrase d'accroche pour force 1}"
- "{phrase d'accroche pour force 2}"

### Adresser les lacunes

- "{réponse préparée pour lacune 1}"
- "{réponse préparée pour lacune 2}"

## Recommandation finale

{go|consider|no-go} Candidature {recommandée|à considérer|peu adaptée}

**Justification:** {raison principale}

## Prochaines étapes suggérées

- [ ] Adapter le CV avec job-cv
- [ ] Préparer la lettre de motivation avec job-letter
- [ ] {autre action si pertinente}
```

### Étape 7: Afficher le lien vers le rapport

```text
Rapport généré: [{app_id}-fit-report.md](data/applications/{app_id}/{app_id}-fit-report.md)

Veuillez consulter le rapport avant de valider.
```

### Étape 8: Validation interactive (AskUserQuestion)

**Q1 - Exigences must-have:**

```json
{
  "question": "Les exigences must-have sont-elles correctement identifiées ?",
  "header": "Must-have",
  "multiSelect": false,
  "options": ["Oui", "Non, il manque...", "Autre: texte libre"]
}
```

**Q2 - Points forts:**

```json
{
  "question": "Les points forts sont-ils correctement valorisés ?",
  "header": "Points forts",
  "multiSelect": false,
  "options": ["Oui", "Ajouter...", "Autre: texte libre"]
}
```

**Q3 - Lacunes:**

```json
{
  "question": "Y a-t-il des lacunes non mentionnées ?",
  "header": "Lacunes",
  "multiSelect": false,
  "options": ["Non", "Oui...", "Autre: texte libre"]
}
```

**Q4 - Score:**

```json
{
  "question": "Le score d'adéquation est-il correct ?",
  "header": "Score",
  "multiSelect": false,
  "options": ["Correct", "Trop haut", "Trop bas", "Autre: texte libre"]
}
```

**Fallback textuel (si AskUserQuestion indisponible):**

```text
Veuillez valider le rapport:

1. Les exigences must-have sont-elles correctement identifiées ?
   a) Oui
   b) Non, il manque...

2. Les points forts sont-ils correctement valorisés ?
   a) Oui
   b) Ajouter...

3. Y a-t-il des lacunes non mentionnées ?
   a) Non
   b) Oui...

4. Le score d'adéquation est-il correct ?
   a) Correct
   b) Trop haut
   c) Trop bas

Répondez par les lettres (ex: "1a, 2a, 3a, 4a") ou détaillez vos corrections.
```

### Étape 9: Mettre à jour le rapport

Si l'utilisateur a indiqué des corrections:

1. Modifier le `{app_id}-fit-report.md` avec les corrections
2. Recalculer le score si nécessaire
3. Afficher les modifications effectuées

### Étape 10: Confirmation pour continuer

**Question de confirmation:**

```json
{
  "question": "Souhaitez-vous continuer avec la génération du CV ?",
  "header": "Continuer ?",
  "multiSelect": false,
  "options": ["Oui, continuer", "Non, arrêter (fit insuffisant)"]
}
```

**Fallback textuel:**

```text
Souhaitez-vous continuer avec la génération du CV ?
1. Oui, continuer
2. Non, arrêter (fit insuffisant)
```

**Si "Non, arrêter":**

```text
Workflow arrêté par l'utilisateur.

Raison: Fit jugé insuffisant pour cette candidature.
Score: {score}/100

Le rapport d'adéquation reste disponible:
[{app_id}-fit-report.md](data/applications/{app_id}/{app_id}-fit-report.md)

Vous pouvez reprendre le processus ultérieurement avec:
job-fit --application={app_id}
```

**FIN DU WORKFLOW** (ne pas passer à job-cv)

## Output

### Fichiers générés

```text
data/applications/{app_id}/
└── {app_id}-fit-report.md   # Rapport d'adéquation validé
```

### Confirmation affichée (si continuer)

```text
Analyse d'adéquation validée!

Poste: {titre} @ {entreprise}
Score: {score}/100
Recommandation: {go|consider|no-go}

Forces principales:
- {force 1}
- {force 2}

Lacunes à adresser:
- {lacune 1}
- {lacune 2}

Prochaine étape: job-cv pour générer un CV adapté
```

## Notes

- Le score est indicatif et doit être contextualisé
- Les talking points sont des suggestions à personnaliser
- Toujours vérifier que les preuves citées sont exactes
- L'utilisateur peut arrêter le workflow si le fit est insuffisant
