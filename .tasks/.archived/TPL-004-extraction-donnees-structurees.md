# TPL-004: Extraction des données structurées du CV

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | TPL-004 |
| **Titre** | Extraire les données du CV dans un format structuré réutilisable |
| **Statut** | ✅ Terminé |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | TPL (Template) |
| **Section CV** | General |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | 2025-11-26 |
| **Temps estimé** | 2-3 heures |
| **Temps réel** | 1 heure |
| **Branche nécessaire** | Auto |

---

## Description

Extraire toutes les données du CV actuel ([cv.typ](../../src/cv.typ)) dans un fichier de données structuré, séparant le contenu de sa présentation.

### Contexte

Plusieurs tâches TPL convergent vers le besoin d'avoir les données du CV extraites :

- **TPL-001** : Versions courte/longue nécessitent de sélectionner du contenu
- **TPL-002** : Système multi-templates nécessite des données découplées
- **TPL-003** : Prototypes from scratch nécessitent les données brutes

Actuellement, le contenu est mélangé avec la mise en forme dans `cv.typ`, ce qui rend difficile :

- La réutilisation du contenu entre différentes versions
- Le changement de template
- La maintenance à long terme

### Objectif

Créer un fichier `cv-data.typ` contenant toutes les données du CV dans un format structuré Typst, prêt à être consommé par différents templates ou versions.

**Livrable principal :** `src/cv-data.typ`

---

## Sous-tâches

- [x] Analyser la structure actuelle de [cv.typ](../../src/cv.typ)
- [x] Définir le schéma de données (structure des variables)
- [x] Extraire les informations personnelles (nom, titre, contact, réseaux)
- [x] Extraire les expériences professionnelles (toutes les missions)
- [x] Extraire la formation (tous les diplômes)
- [x] Extraire les compétences (techniques, méthodologies, soft skills)
- [x] Extraire les langues et niveaux
- [x] Extraire les certifications
- [x] Extraire les centres d'intérêt
- [x] Créer `src/cv-data.typ` avec les données structurées
- [x] Vérifier que `cv.typ` peut importer et utiliser ces données
- [x] Documenter le format dans le fichier

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Format recommandé pour les données Typst :**

```typst
// cv-data.typ - Données structurées du CV
// Ce fichier contient uniquement les données, pas la mise en forme

#let cv-data = (
  // === Informations personnelles ===
  personal: (
    name: "Bastien Gallay",
    title: "Chief Technology Officer",
    email: "...",
    phone: "...",
    address: "...",
    photo: "assets/identite.png",
  ),

  // === Réseaux sociaux ===
  social: (
    linkedin: "...",
    github: "...",
  ),

  // === Expériences professionnelles ===
  experiences: (
    (
      title: "CTO",
      company: "PALO IT",
      location: "Paris",
      period: (start: "2022", end: "Présent"),
      description: "...",
      achievements: (
        "Achievement 1",
        "Achievement 2",
      ),
    ),
    // ... autres expériences
  ),

  // === Formation ===
  education: (
    (
      degree: "...",
      school: "...",
      year: "...",
      details: "...",
    ),
    // ... autres formations
  ),

  // === Compétences ===
  skills: (
    leadership: ("Management 50+", "Stratégie Tech", ...),
    technical: ("GenAI", "Python", "TypeScript", ...),
    methodology: ("SAFe SPC", "Scrum", "Lean Startup", ...),
  ),

  // === Langues ===
  languages: (
    (name: "Français", level: 5),
    (name: "Anglais", level: 4),
  ),

  // === Certifications ===
  certifications: (
    (name: "...", issuer: "...", year: "..."),
  ),

  // === Centres d'intérêt ===
  interests: ("...", "...", "..."),
)
```

**Principes à respecter :**

1. **Exhaustivité** : Extraire TOUT le contenu, même les détails
2. **Neutralité** : Pas de mise en forme, uniquement des données
3. **Hiérarchie** : Structure logique et cohérente
4. **Documentation** : Commenter le format pour faciliter l'utilisation

**Fichiers à consulter :**

- [src/cv.typ](../../src/cv.typ) - Source des données à extraire

**Fichier à créer :**

- `src/cv-data.typ` - Données structurées

**Validation :**

Après création, vérifier que `cv.typ` peut être modifié pour importer les données :

```typst
#import "cv-data.typ": cv-data

// Utilisation
#cv-data.personal.name
```

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Avantages de cette extraction :**

- Facilite TPL-001 (sélection de contenu pour versions courte/longue)
- Prépare TPL-002 (données réutilisables entre templates)
- Permet TPL-003 (prototypes avec mêmes données)
- Simplifie la maintenance future

**Points d'attention :**

- Garder une structure flexible pour évolutions futures
- Ne pas perdre d'informations dans l'extraction
- Le fichier `cv-data.typ` devient la source de vérité

**Décisions à prendre :**

- Format exact des dates (string vs objet start/end)
- Niveau de granularité des compétences
- Inclusion ou non des descriptions longues

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - CV actuel (source)

### Tâches liées

- [TPL-001](./TPL-001-cv-versions.md) - Versions courte/longue (dépend de TPL-004)
- [TPL-002](./TPL-002-template-system.md) - Système de templates (dépend de TPL-004)
- [TPL-003](./TPL-003-cv-from-scratch-alternatives.md) - CV from scratch (dépend de TPL-004)

### Ressources

- Documentation Typst scripting: <https://typst.app/docs/reference/scripting/>
- Typst data types: <https://typst.app/docs/reference/foundations/>

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "feat(data): 📦 extract CV data to structured format

Create cv-data.typ with all CV content.

Refs TPL-004"
```

### Commit final

```bash
git commit -m "feat(data): 📦 complete CV data extraction

- Created src/cv-data.typ with structured data
- Extracted all personal info, experiences, education
- Extracted skills, languages, certifications, interests
- Documented data format for reuse

Closes TPL-004"
```

**Format suggéré :**

- **Type**: feat
- **Scope**: data
- **Emoji**: 📦 (package/data)

---

## Tests / Vérifications

- [x] Le fichier `cv-data.typ` compile sans erreur
- [x] Toutes les données du CV original sont présentes
- [x] La structure est cohérente et documentée
- [x] `cv.typ` peut importer les données (test d'import)
- [x] Aucune perte d'information par rapport à l'original

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée pour harmoniser les prérequis TPL |
| 2025-11-26 | Terminé | Fichier cv-data.typ créé avec toutes les données structurées |

---

## Résultat final

Fichier `src/cv-data.typ` créé avec toutes les données du CV extraites dans un format structuré Typst.

**Ce qui a été fait :**

- Analyse complète de la structure de cv.typ
- Extraction de toutes les données dans un dictionnaire Typst structuré
- 12 sections de données : personal, social, about, interests, influence, languages, skills, experiences, experiences-detailed, education, education-detailed, certifications, volunteering, style
- Documentation inline du format
- Test d'import réussi

**Structure finale :**

```text
src/
├── cv.typ           # CV principal
├── cv-data.typ      # Données structurées (NOUVEAU - 600+ lignes)
└── assets/          # Images
```

**Usage :**

```typst
#import "cv-data.typ": cv-data
#cv-data.personal.firstname  // "Bastien"
#cv-data.skills.all          // Liste de toutes les compétences
```
