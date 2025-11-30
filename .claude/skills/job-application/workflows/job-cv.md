# Job-CV Workflow

Génère une version du CV adaptée à une offre d'emploi spécifique.

## Usage

```bash
job-cv [--format=short|long] [--dry-run] [--application=ID]
```

**Options:**

- `--format`: Version courte (1 page) ou longue (2+ pages). Défaut: auto selon le poste
- `--dry-run`: Affiche les modifications sans générer les fichiers
- `--application`: ID de candidature spécifique. Défaut: dernière analyse

## Prérequis

1. Une analyse d'offre doit exister (`job-analyze`)
2. Une analyse d'adéquation doit exister (`job-fit`)

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

**Règles de sélection:**

- Poste technique senior/CTO: `exp-palo-it` en premier, développer détails
- Poste coaching/transformation: `exp-upwiser` en premier
- Poste e-commerce/retail: `exp-cdiscount` plus visible
- Toujours garder les 3-4 expériences les plus récentes minimum

### 2. Ajustement du niveau de détail

**Par expérience:**

| Pertinence | Niveau de détail | Actions |
|------------|------------------|---------|
| Très haute | Développé | Ajouter bullet points, chiffres, stack technique |
| Haute | Standard | Garder tel quel |
| Moyenne | Condensé | Réduire à 2-3 bullet points essentiels |
| Basse | Minimal | Une ligne ou omettre |

### 3. Optimisation ATS (mots-clés)

**Sources des mots-clés:**

- `analysis.md` > section "Mots-clés ATS"
- `fit-report.md` > section "Exigences satisfaites"

**Règles d'injection:**

1. **Priorité 1 - Titres et headers:**
   - Inclure dans le titre du poste si pertinent
   - Exemple: "CTO | Expert IA & Cloud" si poste Cloud

2. **Priorité 2 - Bullet points d'expérience:**
   - Reformuler pour inclure les termes exacts de l'offre
   - Exemple: "DevOps" -> "CI/CD et pratiques DevOps"

3. **Priorité 3 - Section Skills sidebar:**
   - Réordonner pour mettre en premier les skills demandés
   - Ajouter des skills si possédés mais absents

**Contraintes:**

- Ne jamais ajouter de compétences non maîtrisées
- Garder un langage naturel (pas de keyword stuffing)
- Maximum 5-7 mots-clés ajoutés par section

### 4. Adaptation de la sidebar

**Sections modifiables (src/shared/sidebar.typ):**

| Section | Adaptation possible |
|---------|---------------------|
| A propos | Reformuler selon le poste ciblé |
| Leadership | Réordonner pills par pertinence |
| Tech & IA | Réordonner, ajouter/retirer pills |
| Méthodologie | Réordonner selon contexte (Agile, DevOps...) |

### 5. Choix du format

**Critères de décision:**

| Contexte | Format recommandé |
|----------|-------------------|
| Startup, scale-up | Court (1 page) |
| Grand groupe, cabinet | Long (2 pages) |
| Poste senior/direction | Long avec détails |
| Candidature spontanée | Court |
| Offre avec "CV détaillé demandé" | Long |

**Implémentation:**

- Court: utiliser `cv-short.typ` comme base
- Long: utiliser `cv.typ` comme base

## Workflow d'exécution

### Étape 1: Charger les données

```text
Charger:
- data/applications/{app_id}/analysis.md
- data/applications/{app_id}/fit-report.md

Extraire:
- keywords: liste des mots-clés ATS
- requirements: exigences must-have et nice-to-have
- strengths: points forts identifiés
- gaps: lacunes identifiées
```

### Étape 2: Calculer les adaptations

```text
adaptations = {
    experiences_order: [exp ranked by relevance],
    experiences_detail: {exp_name: level},
    sidebar_skills: [skills reordered],
    about_text: "texte adapté",
    keywords_to_inject: [prioritized keywords],
    format: "short" | "long",
}
```

### Étape 3: Générer le fichier Typst

Créer `data/applications/{app_id}/cv-adapted.typ`:

```typst
// cv-adapted.typ
// Généré automatiquement pour: {job_title} @ {company}
// Date: {date}

#import "../../src/neat-cv-local.typ": ...
#import "../../src/shared/config.typ": *

// Configuration adaptée
#let author-adapted = (
  ..author-config,
  position: "{position_adaptée}",
)

// Sidebar adaptée
#let sidebar-adapted() = [
  = A propos
  {about_text_adapted}

  // ... sections réordonnées avec skills adaptés
]

// Expériences réordonnées et adaptées
#let experiences-adapted = [
  = Expérience Professionnelle

  // Expériences dans le nouvel ordre avec détails ajustés
]

// Document
#show: cv-setup.with(author: author-adapted, ...)
#cv-page-one(sidebar-adapted(), [#experiences-adapted ...])
```

### Étape 4: Compiler le PDF

```bash
just build-adapted {app_id}
```

### Étape 5: Générer le rapport de modifications

Créer `data/applications/{app_id}/modifications.md`:

```markdown
## CV adapté pour : {job_title} @ {company}

### Modifications apportées

**Expériences réorganisées:**
1. {exp_name} -> Position 1 (était position {old_pos})
2. {exp_name} -> Développée (+{n} bullet points)

**Mots-clés intégrés:**
- "{keyword}" ajouté dans {section}
- "{keyword}" mis en avant dans sidebar

**Compétences ajustées:**
- {skill} déplacé en premier
- {skill} ajouté (présent dans profil, demandé dans offre)

**Format:**
- Version {short|long} sélectionnée
- Raison: {justification}

### Fichiers générés
- cv-adapted.typ - Source Typst
- cv-adapted.pdf - PDF compilé
```

## Output

### Fichiers générés

```text
data/applications/{app_id}/
|-- cv-adapted.typ          # Source Typst adaptée
|-- cv-adapted.pdf          # PDF compilé
`-- modifications.md        # Rapport des modifications
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

Fichiers:
- data/applications/{app_id}/cv-adapted.pdf

Vérifiez le CV avant envoi!
```

## Notes importantes

1. **Toujours vérifier** le CV généré avant envoi
2. **Ne jamais mentir** sur les compétences ou expériences
3. **Garder la cohérence** avec le CV source
4. **Documenter** les modifications pour traçabilité
