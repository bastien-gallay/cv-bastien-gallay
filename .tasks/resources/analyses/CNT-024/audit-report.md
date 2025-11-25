# Audit Report CNT-024 - CV Flash 2025 vs CV Typst

**Date:** 2025-11-25
**Tâche:** CNT-024
**Sources comparées:**

- CV Flash 2025 (slide unique)
- CV Typst actuel (`src/cv.typ`)

---

## Synthèse

| Catégorie | CV Flash 2025 | CV Typst | Écart |
|-----------|---------------|----------|-------|
| Positionnement | Coach Agile / CTO / Software Craftsman, +20 ans | Crafting Technology Officer, 25 ans | Divergence de titre |
| Expériences listées | 4 principales | 7 détaillées | Différentes expériences mises en avant |
| Certifications | 7 mentionnées | 7 présentes | PSPO manquant dans Typst |
| Technologies | 11 mentionnées | 18 pills | Couverture différente |
| Activités communautaires | 3 listées | 1 mentionnée | Lacune importante |

---

## Écarts détaillés

### 1. Positionnement professionnel

| Élément | CV Flash 2025 | CV Typst |
|---------|---------------|----------|
| Titre principal | Coach Agile / CTO / Software Craftsman | Crafting Technology Officer |
| Expérience affichée | +20 ans | 25 ans |
| Citation | Oui (Peter Drucker) | Non |

**Analyse:** Le CV Flash utilise un triple positionnement plus explicite (Coach/CTO/Craftsman) tandis que le CV Typst utilise un néologisme ("Crafting Technology Officer"). Le CV Flash est plus accessible pour un non-initié.

### 2. Expériences manquantes dans le CV Typst

#### 2.1 Beta.gouv / MonEspaceNis2 - ABSENT

| Champ | Valeur CV Flash |
|-------|-----------------|
| Rôle | Lead developer |
| Stack | React / Javascript / TypeScript |
| Projet | MonEspaceNis2 |
| Description | Création infrastructure, architecture et développement, outils de mesure |

**Impact:** Expérience récente et significative absente du CV principal.

#### 2.2 Nalo - Coaching CTO - ABSENT

| Champ | Valeur CV Flash |
|-------|-----------------|
| Rôle | Coaching CTO et équipe technique |
| Stack | Python / Django |
| Description | Mise en place de pratiques craft et agile; refonte architecture |

**Impact:** Mission de coaching CTO de haut niveau non documentée.

#### 2.3 SeLoger.com - ABSENT

| Champ | Valeur CV Flash |
|-------|-----------------|
| Rôle | Développeur senior |
| Stack | React / Typescript / Java |
| Description | Reprise de legacy, développement et animation de l'équipe |

**Impact:** Expérience significative dans une grande entreprise du digital français absente.

#### 2.4 Wanteeed - ABSENT

- Mentionné dans la liste des clients coach/formateur du CV Flash
- Non référencé dans le CV Typst

### 3. Certifications

| Certification | CV Flash | CV Typst | Écart |
|---------------|----------|----------|-------|
| SAFe SPC | ✅ | ✅ | OK |
| PSM | ✅ | ✅ | OK |
| PSPO (Product Owner) | ✅ | ❌ | **MANQUANT** |
| PSD | ✅ | ✅ | OK |
| PSK (Kanban) | ✅ | ✅ | OK |
| PSP (?) | ✅ | ❌ | **À vérifier** |
| CSM | ✅ | ✅ | OK |

**Note:** "PSP" dans le CV Flash n'est pas une certification Scrum.org standard. À clarifier (peut-être PSU - Professional Scrum with UX, ou erreur).

### 4. Technologies et compétences

#### Technologies présentes dans CV Flash, absentes dans CV Typst

| Technologie | CV Flash | CV Typst |
|-------------|----------|----------|
| Node.js | ✅ | ❌ |
| React | ✅ | ❌ |
| Storybook | ✅ | ❌ |
| Java | ✅ | ❌ |
| F# | ✅ | ❌ |
| C++ | ✅ | ❌ |
| Ruby | ✅ | ❌ |
| BDD | ✅ | ❌ |

#### Technologies présentes dans CV Typst, absentes dans CV Flash

| Technologie | CV Typst | CV Flash |
|-------------|----------|----------|
| SQL | ✅ | ❌ |
| C | ✅ | ❌ |
| Rust | ✅ | ❌ |
| IA | ✅ | ❌ |
| Spec Driven Development | ✅ | ❌ |
| Clean Code | ✅ | ❌ |

### 5. Activités communautaires

| Activité | CV Flash | CV Typst | Écart |
|----------|----------|----------|-------|
| Lead Lean Startup Bordeaux (2011-2016) | ✅ avec dates | Mention sans dates | **AMÉLIORER** |
| Agile Tour Bordeaux (orateur/organisateur) | ✅ | ❌ | **MANQUANT** |
| Orateur événements agilité/management | ✅ | ❌ | **MANQUANT** |

### 6. Formulation "À propos"

| CV Flash | CV Typst |
|----------|----------|
| Récit narratif riche (développeur, product owner, coach, entrepreneur) | Description courte factuelle |
| Mentionne "insatiable curiosité" | Pas de trait de personnalité |
| Style engageant à la 3e personne | Style sobre à la 1re personne |

---

## Observations complémentaires

### Points forts du CV Flash

1. **Positionnement clair** avec trois casquettes explicites
2. **Expériences récentes** bien mises en avant (Beta.gouv, Nalo, SeLoger)
3. **Activités communautaires** valorisées avec dates précises
4. **Citation inspirante** qui personnalise le document

### Points à intégrer dans le CV Typst

1. Ajouter les 3 expériences clés manquantes (Beta.gouv, Nalo, SeLoger)
2. Compléter la certification PSPO si détenue
3. Enrichir les activités communautaires avec dates
4. Considérer l'ajout de technologies plus modernes (React, Node.js)
5. Valoriser l'activité d'orateur et organisateur d'événements

---

## Recommandations

Voir fichier [recommendations.md](./recommendations.md) pour la liste priorisée des actions à entreprendre.
