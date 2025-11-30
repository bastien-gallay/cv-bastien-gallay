# Job-CV Workflow

Génère une version du CV adaptée à une offre d'emploi spécifique avec questionnaire interactif.

## Usage

```bash
job-cv [--format=short|long] [--dry-run] [--application=ID]
```

**Options:**

- `--format`: Version courte (1 page) ou longue (2+ pages). Défaut: miroir de l'annonce
- `--dry-run`: Affiche les modifications sans générer les fichiers
- `--application`: ID de candidature spécifique. Défaut: dernière analyse

## Prérequis

1. Une analyse d'offre doit exister (`job-analyze`)
2. Une analyse d'adéquation doit exister et être validée (`job-fit`)

## Workflow d'exécution

### Étape 1: Charger les données

```text
Charger:
- data/applications/{app_id}/{app_id}-analysis.md
- data/applications/{app_id}/{app_id}-fit-report.md

Extraire:
- keywords: liste des mots-clés ATS
- requirements: exigences must-have et nice-to-have
- strengths: points forts identifiés
- gaps: lacunes identifiées
- job_word_count: nombre de mots de l'annonce
- company_type: type d'entreprise (startup, grand groupe, cabinet)
```

### Étape 2: Recommander le format CV (miroir de l'annonce)

**Logique de recommandation:**

| Critère annonce | Format recommandé |
|-----------------|-------------------|
| < 500 mots | Court (1 page) |
| > 500 mots | Long (2+ pages) |
| Startup, scale-up | Court |
| Grand groupe, cabinet conseil | Long |
| "CV détaillé demandé" | Long |
| Candidature spontanée | Court |

**Question de confirmation:**

```json
{
  "question": "L'annonce semble {courte/longue}. Je recommande le format {court/long}. Confirmer ?",
  "header": "Format CV",
  "multiSelect": false,
  "options": ["Oui, format {court/long}", "Non, format {long/court}", "Autre: texte libre"]
}
```

**Fallback textuel:**

```text
Format de CV recommandé

L'annonce semble {courte/longue} ({n} mots, {type_entreprise}).
Je recommande le format {court/long}.

1. Oui, format {court/long}
2. Non, format {long/court}
3. Autre (précisez)
```

### Étape 3: Questionnaire de personnalisation

**Q1 - Titre du poste:**

```json
{
  "question": "Quel titre afficher sur le CV ?",
  "header": "Titre",
  "multiSelect": false,
  "options": ["Garder : {titre_actuel}", "Adapter : {suggestion_basée_offre}", "Autre: texte libre"]
}
```

**Q2 - Ordre des expériences:**

```json
{
  "question": "Comment ordonner les expériences ?",
  "header": "Ordre XP",
  "multiSelect": false,
  "options": ["Automatique (par pertinence)", "Chronologique inverse", "Autre: texte libre"]
}
```

**Q3 - Expériences à omettre:**

```json
{
  "question": "Y a-t-il des expériences à omettre ?",
  "header": "Omettre",
  "multiSelect": true,
  "options": ["Aucune", "{exp_1_name}", "{exp_2_name}", "Autre: texte libre"]
}
```

**Q4 - Mots-clés ATS:**

```json
{
  "question": "Quels mots-clés ATS prioriser ?",
  "header": "Mots-clés",
  "multiSelect": false,
  "options": ["Tous les mots-clés identifiés", "Sélection manuelle...", "Autre: texte libre"]
}
```

**Q5 - Sidebar:**

```json
{
  "question": "Comment adapter la sidebar ?",
  "header": "Sidebar",
  "multiSelect": false,
  "options": ["Automatique (réordonner par pertinence)", "Garder l'ordre actuel", "Autre: texte libre"]
}
```

**Fallback textuel:**

```text
Personnalisation du CV

1. Titre du poste ?
   a) Garder : "{titre_actuel}"
   b) Adapter : "{suggestion}"
   c) Autre (précisez)

2. Ordre des expériences ?
   a) Automatique (par pertinence)
   b) Chronologique inverse
   c) Autre (précisez)

3. Expériences à omettre ?
   a) Aucune
   b) Liste (précisez)

4. Mots-clés ATS ?
   a) Tous les mots-clés identifiés
   b) Sélection manuelle (précisez)

5. Sidebar ?
   a) Automatique (réordonner)
   b) Garder l'ordre actuel

Répondez par les lettres ou détaillez.
```

### Étape 4: Sauvegarder les choix

Créer/mettre à jour `data/applications/{app_id}/{app_id}-modifications.md`:

```markdown
# Modifications CV : {job_title} @ {company}

**Date:** {date}
**Format choisi:** {short|long}

## Choix utilisateur

- **Titre:** {choix}
- **Ordre expériences:** {choix}
- **Expériences omises:** {choix}
- **Mots-clés ATS:** {choix}
- **Sidebar:** {choix}

## Adaptations appliquées

{détails des modifications}
```

### Étape 5: Calculer les adaptations

```text
adaptations = {
    experiences_order: [exp ranked by relevance],
    experiences_detail: {exp_name: level},
    experiences_omit: [exp to omit],
    sidebar_skills: [skills reordered],
    about_text: "texte adapté",
    keywords_to_inject: [prioritized keywords],
    format: "short" | "long",
    title: "titre adapté",
}
```

### Étape 6: Générer le fichier Typst

Créer `data/applications/{app_id}/{app_id}-cv-adapted.typ`:

```typst
// CV adapté pour: {job_title} @ {company}
// Date: {date}
// Score d'adéquation: {score}/100

#import "../../../src/neat-cv-local.typ": (...)
#import "../../../src/shared/config.typ": *
#import "../../../src/shared/experiences.typ": *
#import "../../../src/shared/sections.typ": *

// Métadonnées document
#set document(
  title: "CV - Bastien Gallay - {Poste} @ {Entreprise}",
  author: "Bastien Gallay",
  date: datetime.today(),
)

// Configuration adaptée
#let author-adapted = (
  ..author-config,
  position: "{position_adaptée}",
)

// Sidebar adaptée
#let sidebar-adapted() = [
  = A propos
  {about_text_adapted}

  // ... sections réordonnées
]

// Expériences adaptées
#let experiences-adapted = [
  = Expérience Professionnelle

  // Expériences dans le nouvel ordre
]

// Document
#show: cv-setup.with(author: author-adapted, ...)
#cv-page-one(
  profile-picture: image("../../../src/assets/photo-profile-pro.jpg"),
  sidebar-adapted(),
  [#experiences-adapted ...]
)
```

**Important - Chemins relatifs:**

- Le fichier est dans `data/applications/{app_id}/`
- Les imports doivent utiliser `../../../src/` (3 niveaux)

### Étape 7: Compiler le PDF

```bash
just build-adapted {app_id}
```

### Étape 8: Vérification visuelle

Lire le PDF généré et vérifier:

1. **Nombre de pages:** Correspond au format choisi (1 pour court, 2+ pour long)
2. **Pas de page supplémentaire:** Pas de page presque vide en fin de document
3. **Zones blanches:** Pas de grosse zone blanche en fin de colonne/page
4. **Lisibilité:** Pas de texte tronqué ou qui déborde
5. **Cohérence:** Les sections sont complètes

**Si problème détecté:**

```text
Problème détecté dans le CV généré:

- Type: {débordement|zone_blanche|page_supplémentaire|...}
- Localisation: {page X, section Y}
- Description: {détails}

Action proposée:
- {ajuster contenu|changer format|réduire expériences|...}

Voulez-vous que j'applique cette correction ?
```

Régénérer si nécessaire.

## Règles d'adaptation

### 1. Réorganisation des expériences

**Principe:** Mettre en premier les expériences les plus pertinentes pour le poste.

**Algorithme de scoring:**

```text
Pour chaque expérience:
  score = 0
  score += keywords_match(exp, job.keywords) * 3      # Mots-clés ATS
  score += skills_match(exp, job.requirements) * 2    # Compétences requises
  score += domain_match(exp, job.industry)            # Secteur d'activité
  score += recency_bonus(exp.end_date)                # Bonus récence

Réordonner par score décroissant
```

**Expériences disponibles (src/shared/experiences.typ):**

| Variable | Poste | Période | Pertinence type |
|----------|-------|---------|-----------------|
| `exp-palo-it` | CTO @ PALO IT | 2021-2025 | Tech, IA, Management |
| `exp-upwiser` | Coach Agile @ Upwiser | 2013-2021 | Agile, Coaching, Startups |
| `exp-cdiscount` | Chef projet @ CDiscount | 2010-2013 | E-commerce, Paiement |
| `exp-cast` | Consultant @ Cast | 2006-2010 | Conseil, Gestion projet |
| `exp-dev-web` | Dev Web @ Boonty | 2002-2006 | Développement |

### 2. Ajustement du niveau de détail

| Pertinence | Niveau de détail | Actions |
|------------|------------------|---------|
| Très haute | Développé | Ajouter bullet points, chiffres, stack technique |
| Haute | Standard | Garder tel quel |
| Moyenne | Condensé | Réduire à 2-3 bullet points essentiels |
| Basse | Minimal | Une ligne ou omettre |

### 3. Optimisation ATS (mots-clés)

**Sources des mots-clés:**

- `{app_id}-analysis.md` > section "Mots-clés ATS"
- `{app_id}-fit-report.md` > section "Exigences satisfaites"

**Règles d'injection:**

1. **Priorité 1 - Titres:** Inclure dans le titre du poste si pertinent
2. **Priorité 2 - Bullet points:** Reformuler pour inclure les termes exacts
3. **Priorité 3 - Sidebar:** Réordonner skills demandés en premier

**Contraintes:**

- Ne jamais ajouter de compétences non maîtrisées
- Garder un langage naturel (pas de keyword stuffing)
- Maximum 5-7 mots-clés ajoutés par section

### 4. Adaptation de la sidebar

| Section | Adaptation possible |
|---------|---------------------|
| A propos | Reformuler selon le poste ciblé |
| Leadership | Réordonner pills par pertinence |
| Tech & IA | Réordonner, ajouter/retirer pills |
| Méthodologie | Réordonner selon contexte |

## Output

### Fichiers générés

```text
data/applications/{app_id}/
├── {app_id}-modifications.md    # Choix utilisateur et modifications
├── {app_id}-cv-adapted.typ      # Source Typst adaptée
└── {app_id}-cv-adapted.pdf      # PDF compilé et vérifié
```

### Confirmation affichée

```text
CV adapté généré avec succès!

Poste: {job_title} @ {company}
Format: {short|long} ({n} pages)
Score d'adéquation: {score}/100

Modifications principales:
- {n} expériences réordonnées
- {n} mots-clés ATS intégrés
- Sidebar adaptée

Vérification visuelle: OK

Fichiers:
- [{app_id}-cv-adapted.pdf](data/applications/{app_id}/{app_id}-cv-adapted.pdf)

Vérifiez le CV avant envoi!
```

## Notes importantes

1. **Toujours vérifier** le CV généré avant envoi
2. **Ne jamais mentir** sur les compétences ou expériences
3. **Garder la cohérence** avec le CV source
4. **Documenter** les modifications pour traçabilité
5. **Vérification visuelle** systématique après compilation
