# Job-Analyze Workflow

Analyse une offre d'emploi et extrait les informations structurées.

## Usage

```bash
job-analyze [URL ou texte de l'offre]
```

**Entrées acceptées:**

- URL LinkedIn, Welcome to the Jungle, Indeed, sites carrières
- Texte copié-collé de l'offre

## Workflow d'exécution

### Étape 1: Récupérer le contenu

**Si URL fournie:**

```text
1. Utiliser WebFetch pour récupérer le contenu
2. Parser le HTML/markdown
3. Extraire le texte de l'offre
```

**Si texte fourni:**

```text
1. Utiliser le texte directement
```

### Étape 2: Créer l'ID de candidature

```text
Format: {company_slug}-{YYYY-MM-DD}
Exemple: google-2025-11-30
```

### Étape 3: Extraire les informations structurées

**Informations générales:**

- Titre du poste
- Entreprise
- Localisation
- Type de contrat (CDI, CDD, freelance)
- Salaire (si mentionné)
- Télétravail (si mentionné)

**Exigences:**

- **Must-have:** Compétences/expériences obligatoires
- **Nice-to-have:** Compétences/expériences souhaitées

**Responsabilités:**

- Liste des missions principales

**Mots-clés ATS:**

- Technologies mentionnées
- Méthodologies mentionnées
- Soft skills demandés
- Termes récurrents

### Étape 4: Recherche entreprise (optionnel)

```text
1. WebSearch sur l'entreprise
2. Extraire: secteur, taille, actualités récentes
3. Identifier la stack technique si possible
```

### Étape 5: Identifier les points d'attention

- Red flags potentiels (termes vagues, exigences irréalistes)
- Points positifs (valeurs, avantages, culture)

### Étape 6: Générer le rapport

Créer `data/applications/{app_id}/analysis.md`:

```markdown
# Analyse : {Titre du poste} @ {Entreprise}

**Date d'analyse:** {date}
**Source:** {url ou "texte fourni"}

## Informations générales

| Champ | Valeur |
|-------|--------|
| **Poste** | {titre} |
| **Entreprise** | {entreprise} |
| **Localisation** | {lieu} |
| **Type de contrat** | {type} |
| **Salaire** | {salaire ou "Non communiqué"} |
| **Télétravail** | {politique} |

## Exigences

### Obligatoires (must-have)

- [ ] {compétence 1}
- [ ] {compétence 2}
- ...

### Souhaitées (nice-to-have)

- [ ] {compétence 1}
- [ ] {compétence 2}
- ...

## Responsabilités principales

1. {responsabilité 1}
2. {responsabilité 2}
3. ...

## Mots-clés ATS

`keyword1`, `keyword2`, `keyword3`, ...

## Contexte entreprise

- **Secteur:** {secteur}
- **Taille:** {taille}
- **Actualités récentes:** {news}

## Points d'attention

### Points positifs

- {point positif 1}
- {point positif 2}

### Red flags potentiels

- {red flag 1} (si applicable)

## Recommandations pour la candidature

- Mettre en avant: {compétences clés à valoriser}
- Préparer: {questions/sujets à anticiper}
```

### Étape 7: Sauvegarder l'offre originale

Créer `data/applications/{app_id}/job-posting.md`:

```markdown
# Offre originale

**Source:** {url}
**Date de capture:** {date}

---

{texte complet de l'offre}
```

## Output

### Fichiers générés

```text
data/applications/{app_id}/
|-- job-posting.md      # Offre originale
`-- analysis.md         # Analyse structurée
```

### Confirmation affichée

```text
Analyse d'offre terminée!

ID candidature: {app_id}
Poste: {titre} @ {entreprise}
Localisation: {lieu}

Exigences identifiées:
- {n} must-have
- {n} nice-to-have

Mots-clés ATS: {n} identifiés

Prochaine étape: job-fit pour évaluer l'adéquation
```

## Notes

- Conserver l'offre originale pour référence
- Les checkboxes dans les exigences permettent le suivi dans job-fit
- Les mots-clés ATS seront utilisés par job-cv pour l'optimisation
