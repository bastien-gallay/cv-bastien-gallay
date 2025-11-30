# Job-Fit Workflow

Analyse l'adéquation entre le profil et le poste.

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
1. Charger data/applications/{app_id}/analysis.md
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

### Étape 6: Générer le rapport

Créer `data/applications/{app_id}/fit-report.md`:

```markdown
# Adéquation : {Titre du poste} @ {Entreprise}

**Date d'analyse:** {date}
**Score global:** {score}/100 {stars}

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

## Output

### Fichiers générés

```text
data/applications/{app_id}/
`-- fit-report.md       # Rapport d'adéquation
```

### Confirmation affichée

```text
Analyse d'adéquation terminée!

Poste: {titre} @ {entreprise}
Score: {score}/100 {stars}
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
