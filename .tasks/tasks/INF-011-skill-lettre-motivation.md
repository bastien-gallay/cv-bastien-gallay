# INF-011: Skill assistant lettre de motivation

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-011 |
| **Titre** | Skill d'assistance à la rédaction de lettre de motivation |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 3-4 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Créer un Claude skill pour assister la rédaction de lettres de motivation personnalisées et adaptées à chaque offre d'emploi.

### Contexte

Une lettre de motivation efficace doit :

- Être personnalisée pour l'entreprise et le poste
- Mettre en avant les compétences pertinentes
- Démontrer la motivation et l'intérêt pour le poste
- Avoir le bon ton (formel, dynamique, etc.)
- Être concise et percutante

### Objectif

Créer un skill qui :

- Utilise l'analyse d'offre et d'adéquation comme input
- Génère une lettre de motivation personnalisée
- Propose plusieurs variantes de ton/style
- Permet l'itération et l'amélioration
- Supporte le français (principalement) et l'anglais

### Position dans le workflow

```text
INF-009 → INF-010
              │
              ▼
     ┌────────┴────────┐
     │                 │
     ▼                 ▼
┌─────────────┐  ┌─────────────┐
│ ★ INF-011 ★ │  │   INF-012   │
│ Lettre de   │  │  CV adapté  │
│ motivation  │  └─────────────┘
└─────────────┘
     │
     ▼
  [Output]
  lettre.md
```

---

## Sous-tâches

- [ ] Définir les templates de lettre par type (classique, moderne, startup)
- [ ] Implémenter la génération personnalisée
- [ ] Ajouter le support multi-ton (formel, dynamique, créatif)
- [ ] Intégrer les talking points de l'analyse d'adéquation
- [ ] Créer le workflow `/job-cover-letter`
- [ ] Ajouter un mode itératif pour affiner
- [ ] Tester avec différents types d'offres

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Structure type d'une lettre :**

```markdown
[Coordonnées candidat]

[Ville, Date]

[Coordonnées entreprise]

Objet : Candidature au poste de {titre} - Réf. {référence}

Madame, Monsieur,

[Accroche - pourquoi cette entreprise/ce poste m'intéresse]

[Paragraphe 1 - Mes compétences clés en lien avec le poste]

[Paragraphe 2 - Mes réalisations pertinentes]

[Paragraphe 3 - Ma valeur ajoutée / Ce que j'apporte]

[Conclusion - Disponibilité, entretien]

Cordialement,

[Signature]
```

**Variantes de ton :**

1. **Classique/Formel** : Grandes entreprises, secteur traditionnel
2. **Dynamique/Moderne** : Scale-ups, entreprises tech
3. **Créatif/Original** : Startups, postes créatifs
4. **Direct/Concis** : Style anglo-saxon

**Workflow `/job-cover-letter` :**

```markdown
## Input
- Analyse d'offre (INF-009)
- Analyse d'adéquation (INF-010)
- Ton souhaité (optionnel, défaut: moderne)

## Étapes
1. Charger les analyses précédentes
2. Sélectionner les points forts à mettre en avant
3. Générer l'accroche personnalisée
4. Développer les paragraphes
5. Adapter le ton selon le contexte
6. Proposer la lettre complète

## Output
- Lettre de motivation complète
- (Optionnel) Variantes alternatives
```

**Éléments à personnaliser :**

- Nom de l'entreprise et du recruteur (si connu)
- Référence de l'offre
- Compétences spécifiques mentionnées dans l'offre
- Projets/réalisations pertinents du CV
- Actualités de l'entreprise (si recherche effectuée)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Utilisation prévue :**

```bash
# Générer avec le ton par défaut
/job-cover-letter

# Spécifier un ton
/job-cover-letter --tone=formal

# Mode itératif
/job-cover-letter --iterate
```

**Conseils d'utilisation :**

- Toujours relire et personnaliser le résultat
- Ajouter des éléments personnels spécifiques
- Vérifier les noms et références
- Adapter le format si nécessaire (PDF, mail, etc.)

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - Source des informations personnelles

### Tâches liées

- [INF-008](./INF-008-architecture-skills-candidature.md) - Architecture globale
- [INF-009](./INF-009-skill-analyse-offre-emploi.md) - Fournit l'analyse d'offre
- [INF-010](./INF-010-skill-analyse-adequation.md) - Fournit les talking points

---

## Commits Git associés

### Commit final

```bash
git commit -m "feat(skills): ✨ add cover letter assistant skill

- Generate personalized cover letters
- Support multiple tones (formal, modern, creative)
- Integrate analysis results for personalization
- Include iterative improvement mode

Closes INF-011"
```

---

## Tests / Vérifications

- [ ] La lettre est correctement personnalisée
- [ ] Les différents tons sont distincts
- [ ] Les talking points sont intégrés
- [ ] Le français est correct (grammaire, style)
- [ ] Le format est professionnel

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Skill assistant lettre de motivation |

---

## Résultat final

[À remplir une fois la tâche terminée]
