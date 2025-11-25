# INF-008: Architecture du système de skills candidature

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-008 |
| **Titre** | Architecture globale du système de skills candidature |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 4-6 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Oui |

---

## Description

Concevoir et implémenter l'architecture globale d'un système de Claude skills pour accompagner le processus de candidature à des offres d'emploi.

### Contexte

Le processus de réponse à une offre d'emploi implique plusieurs étapes qui peuvent être assistées par IA :

1. **Analyse de l'offre** : comprendre les exigences, compétences recherchées
2. **Recherche entreprise** : contexte, culture, actualités
3. **Analyse d'adéquation** : correspondance profil/poste
4. **Rédaction** : lettre de motivation personnalisée
5. **Adaptation CV** : version optimisée pour l'offre

Ces étapes sont interconnectées et partagent des données. Un système cohérent de skills permettrait d'automatiser et d'améliorer ce processus.

### Objectif

Créer un écosystème de skills Claude Code pour :

- Analyser une offre d'emploi de manière structurée
- Rechercher le contexte de l'entreprise
- Évaluer l'adéquation entre le profil et le poste
- Assister la rédaction d'une lettre de motivation
- Proposer une version du CV adaptée à l'offre

---

## Sous-tâches

- [ ] Définir l'architecture globale et le flux de données entre skills
- [ ] Concevoir le modèle de données partagé (offre, entreprise, analyse)
- [ ] Créer la structure de répertoires pour les skills candidature
- [ ] Définir les interfaces entre skills (inputs/outputs)
- [ ] Implémenter le skill de base et les utilitaires partagés
- [ ] Documenter l'utilisation du système

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Architecture proposée :**

```plaintext
.claude/skills/job-application/
├── skill.md                    # Point d'entrée principal
├── workflows/
│   ├── analyze-job.md          # Analyse d'offre
│   ├── research-company.md     # Recherche entreprise
│   ├── analyze-fit.md          # Analyse adéquation
│   ├── write-cover-letter.md   # Lettre de motivation
│   └── adapt-cv.md             # CV adapté
├── templates/
│   ├── job-analysis.md         # Template résultat d'analyse
│   ├── company-profile.md      # Template profil entreprise
│   ├── fit-report.md           # Template rapport adéquation
│   └── cover-letter.md         # Template lettre motivation
└── data/
    └── applications/           # Données par candidature
        └── {COMPANY-DATE}/
            ├── job-posting.md  # Offre originale
            ├── analysis.md     # Analyse complète
            ├── cover-letter.md # Lettre générée
            └── cv-adapted.typ  # CV adapté
```

**Flux de données :**

```text
┌─────────────────┐
│  Offre d'emploi │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│ Analyse offre   │────▶│ Recherche       │
│ (INF-009)       │     │ entreprise      │
└────────┬────────┘     └────────┬────────┘
         │                       │
         └───────────┬───────────┘
                     │
                     ▼
         ┌─────────────────┐
         │ Analyse         │
         │ adéquation      │
         │ (INF-010)       │
         └────────┬────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
┌───────────────┐   ┌───────────────┐
│ Lettre de     │   │ CV adapté     │
│ motivation    │   │ (INF-012)     │
│ (INF-011)     │   └───────────────┘
└───────────────┘
```

**Modèle de données partagé :**

```yaml
# Structure d'une candidature
application:
  id: "{company}-{date}"
  job:
    title: string
    company: string
    location: string
    type: string  # CDI, CDD, freelance
    url: string
    requirements:
      must_have: []
      nice_to_have: []
    responsibilities: []
    keywords: []
  company:
    name: string
    industry: string
    size: string
    culture: []
    recent_news: []
    tech_stack: []
  fit_analysis:
    score: number  # 0-100
    strengths: []
    gaps: []
    talking_points: []
  outputs:
    cover_letter: path
    adapted_cv: path
```

**Intégration avec le projet CV :**

- Utilise les données du CV existant (`src/cv.typ`)
- Génère des versions adaptées dans un dossier dédié
- Peut être intégré au système de tâches existant

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Cas d'usage typique :**

```bash
# 1. Analyser une nouvelle offre
/job-analyze [URL ou texte de l'offre]

# 2. Obtenir le rapport d'adéquation
/job-fit

# 3. Générer la lettre de motivation
/job-cover-letter

# 4. Générer le CV adapté
/job-cv
```

**Questions à considérer :**

- Où stocker les données des candidatures ? (`.applications/` ?)
- Faut-il un historique des candidatures ?
- Intégration avec un CRM/tracker de candidatures ?
- Langues supportées (FR/EN) ?

**Évolutions futures possibles :**

- Suivi des candidatures (relances, réponses)
- Analyse de tendances sur les offres reçues
- Préparation d'entretien basée sur l'analyse
- Score de compatibilité automatique

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - CV source à adapter
- [.claude/skills/](../../.claude/skills/) - Skills existants

### Tâches liées

- [INF-009](./INF-009-skill-analyse-offre-emploi.md) - Skill analyse d'offre
- [INF-010](./INF-010-skill-analyse-adequation.md) - Skill analyse adéquation
- [INF-011](./INF-011-skill-lettre-motivation.md) - Skill lettre de motivation
- [INF-012](./INF-012-skill-cv-adapte.md) - Skill CV adapté

### Ressources

- Claude Code Skills documentation
- Best practices for job applications

---

## Commits Git associés

### Commit final

```bash
git commit -m "feat(skills): ✨ create job application skills architecture

- Define data model and workflow structure
- Create shared templates and utilities
- Establish skill integration patterns

Closes INF-008"
```

---

## Tests / Vérifications

- [ ] L'architecture est documentée et claire
- [ ] Les interfaces entre skills sont définies
- [ ] Les templates de données sont créés
- [ ] La structure de répertoires est en place
- [ ] Un exemple de flux complet est documenté

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche parent pour le système de skills candidature |

---

## Résultat final

[À remplir une fois la tâche terminée]
