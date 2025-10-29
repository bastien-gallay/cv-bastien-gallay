# Audit LinkedIn - Rapport d'Analyse Comparative

**Analyse:** CNT-001
**Date:** 2025-10-29
**Profil LinkedIn:** https://www.linkedin.com/in/bastiengallay/
**CV source:** [src/cv.typ](../../../src/cv.typ)

---

## Résumé Exécutif

Cet audit compare le profil LinkedIn de Bastien Gallay avec le CV actuel en Typst pour identifier les écarts, incohérences et éléments manquants.

**Statistiques:**

- ✅ **Éléments déjà présents dans le CV:** 6 expériences principales, 4 formations, 5 certifications
- ⚠️ **Éléments manquants:** 4 expériences (missions freelance), 3 certifications, 1 langue, 6 expériences bénévoles, 2 sites web
- 🔴 **Incohérences de dates:** 7 écarts identifiés (dont 2 majeurs)
- 📝 **Descriptions à enrichir:** 5 postes avec détails supplémentaires

**Priorité globale:** 🔴 HAUTE - Plusieurs incohérences de dates critiques et expériences manquantes

---

## 1. Expériences Professionnelles

### 1.1 Présentes dans les deux

| Poste | LinkedIn | CV | Statut |
|-------|----------|----|----|
| **PALO IT** | CTO + Consultant | ✅ | ⚠️ Dates différentes |
| **Upwiser** | Coach Agile / Gérant | ✅ | 🔴 Dates très différentes |
| **Cdiscount** | Project manager / Scrum master | ✅ | ⚠️ 1 mois d'écart |
| **Cast Consulting** | Engineer / Consultant | ✅ | ⚠️ 1 mois d'écart |
| **Boonty** | Development engineer | ✅ | 🔴 Dates différentes |
| **Freelance** | Web developer | ✅ | 🔴 Dates début différentes |

### 1.2 Manquantes dans le CV (4 expériences)

| # | Poste | Dates LinkedIn | Priorité | Raison |
|---|-------|---------------|----------|---------|
| 1 | **i-BP (Banque Populaire)** - Coach Agile | avr. 2015 - sept. 2015 (6 mois) | 🔴 HAUTE | Mission freelance significative avec détails riches |
| 2 | **DEKRA Automotive France** - Coach Agile | oct. 2013 - janv. 2015 (1 an 4 mois) | 🔴 HAUTE | Mission longue (16 mois) avec responsabilités importantes |
| 3 | **ITS Group** - Project manager | oct. 2010 - juin 2011 (9 mois) | 🟡 MOYENNE | Mission courte mais clarifiante (ESN pour Cdiscount) |
| 4 | **Qualia Services** - Programming engineer | juin 2004 - juin 2005 (1 an 1 mois) | 🟢 BASSE | Ancienne mission, peut être omise pour gagner de l'espace |

### 1.3 Incohérences de dates (7 écarts identifiés)

| Poste | LinkedIn | CV | Écart | Priorité |
|-------|----------|----|----|----------|
| **PALO IT - CTO (fin)** | nov. 2024 - **oct. 2025** | 10/2024 - **08/2025** | -2 mois | 🔴 CRITIQUE |
| **Upwiser (fin)** | oct. 2013 - **nov. 2024** | 09/2013 - **01/2021** | **+3 ans 10 mois** | 🔴🔴 TRÈS CRITIQUE |
| **Cdiscount (fin)** | oct. 2010 - **oct. 2013** | 10/2010 - **09/2013** | -1 mois | 🟢 Mineur |
| **Cast Consulting (début)** | **août 2006** - sept. 2010 | **07/2006** - 09/2010 | -1 mois | 🟢 Mineur |
| **Boonty (début)** | **juin 2005** - juil. 2006 | **07/2004** - 07/2006 | -13 mois | 🔴 CRITIQUE |
| **Boonty (durée)** | 1 an 2 mois | 2 ans | -10 mois | 🔴 CRITIQUE |
| **Freelance (début)** | **juin 2002** - juin 2004 | **06/1999** - 06/2004 | -3 ans | 🔴 CRITIQUE |

**Note importante:** L'écart sur **Upwiser** est le plus critique - LinkedIn indique que l'activité a continué jusqu'en novembre 2024 (parallèlement à PALO IT?), alors que le CV indique janvier 2021.

### 1.4 Descriptions à enrichir

| Poste | Description LinkedIn | Description CV | Action |
|-------|---------------------|----------------|---------|
| **PALO IT - Consultant** | Audits techniques, accompagnement DDD/Clean Code/DevOps, développements (Java, Python, TS, React) | Description générale | ✅ Déjà riche, maintenir |
| **Boonty** | Travail architectural front/back office, intégration DRM (Macrovision, Starforce, SecuROM), système d'abonnement jeux vidéo | (vide) | 🔴 Ajouter détails |
| **Qualia Services** | Missions de développement pour Boonty, enseignement interne et consulting | (non présent) | 🟡 Si ajouté |
| **Cast Consulting** | First mission: PM at Fotovista (e-merchant), integration of TheLink.com | Description générale | 🟢 Optionnel |

---

## 2. Éducation

### 2.1 Incohérence institution DEA

| Diplôme | LinkedIn | CV | Écart |
|---------|----------|----|----|
| **DEA/Master Réalité Virtuelle** | **UVSQ** Université de Versailles Saint-Quentin-en-Yvelines (2001-2002) | **INSTN** Institut National de Sciences et Techniques Nucléaires, Sacclay (2002) | Institution différente |

**Analyse:** Il s'agit probablement du même diplôme avec deux institutions partenaires. L'INSTN pourrait être le lieu d'enseignement tandis que l'UVSQ délivre le diplôme. À clarifier.

### 2.2 DUT et Bac absents de LinkedIn

LinkedIn ne mentionne que les 2 diplômes universitaires (Master et Maîtrise), ce qui est normal - ces diplômes antérieurs ne sont généralement pas affichés sur les profils LinkedIn seniors.

---

## 3. Langues

### Manquante dans le CV

| Langue | Niveau LinkedIn | Présence CV | Priorité | Action |
|--------|----------------|-------------|----------|---------|
| **Espagnol** | Elementary proficiency | ❌ (commentée ligne 66) | 🟡 MOYENNE | Décommenter et ajuster |

**Note:** Le CV contient une ligne commentée pour l'espagnol ([src/cv.typ:66](../../../src/cv.typ#L66)):

```typst
// #item-with-level("Espagnol", 2, subtitle: "Notions")
```

---

## 4. Certifications

### 4.1 Présentes dans les deux

| Certification | LinkedIn | CV | Statut |
|---------------|----------|----|----|
| **Certified Scrum Master** | Oct 2008 | 2008 | ✅ Cohérent |
| **Professional Scrum Master I (PSM-I)** | May 2015 | 2015 | ✅ Cohérent |

### 4.2 Manquantes dans le CV (2 certifications)

| # | Certification | Date LinkedIn | Organisme | Priorité |
|---|---------------|---------------|-----------|----------|
| 1 | **Professional Scrum Developer (PSD-I)** | May 2018 | Scrum.org | 🔴 HAUTE |
| 2 | **Scaled Professional Scrum (SPS)** | Jan 2016 | Scrum.org | 🔴 HAUTE |

### 4.3 Incohérences

| Certification | LinkedIn | CV | Écart | Priorité |
|---------------|----------|----|----|----------|
| **Certified SAFe 5 Program Consultant** | Jun 2020 (SAFe 5) | 2018 (SPC4 et SPC5) | -2 ans, version différente | 🔴 CRITIQUE |

**Note:** Il est possible que la certification ait été obtenue en 2018 (SPC4) puis mise à jour en 2020 (SAFe 5). À clarifier.

### 4.4 Certifications dans CV mais pas sur LinkedIn (2)

| Certification | CV | Priorité | Action |
|---------------|----|---------| -------|
| **Professional Scrum with Kanban** | 2017 | 🟢 | Maintenir dans CV |
| **Scaled Professional Scrum (Nexus)** | 2017 | 🟢 | Maintenir dans CV (peut être lié au SPS de LinkedIn) |

---

## 5. Expérience Bénévole

### Absente du CV (6 organisations)

| # | Organisation | Rôle | Dates | Priorité | Raison |
|---|-------------|------|-------|----------|---------|
| 1 | **Agile Tour Bordeaux** (Okiwi) | Membre équipe organisation | avr. 2012 - aujourd'hui (13 ans+) | 🔴 HAUTE | Engagement long et toujours actif |
| 2 | **Agile Tour Bordeaux** (listing séparé) | Organisation actif/helper | mars 2011 - aujourd'hui (14 ans+) | 🔴 HAUTE | Doublon possible avec #1 |
| 3 | **Lean Startup Bordeaux** | Founder and Leader | janv. 2012 - janv. 2018 (6 ans) | 🔴 HAUTE | Déjà mentionné dans Upwiser (ligne 132) |
| 4 | **Collectif Quinconces** | Co-fondateur | avr. 2016 - juin 2018 (2 ans 3 mois) | 🟡 MOYENNE | Initiative entrepreneuriale |
| 5 | **Ruby Bordeaux** | Organisateur | janv. 2011 - janv. 2013 (2 ans) | 🟡 MOYENNE | Communauté technique |
| 6 | **Startup Weekend Bordeaux** | Coach Agile | oct. 2012 (1 mois) | 🟢 BASSE | Mission ponctuelle |

**Note:** Le CV mentionne "Création du cercle Lean Startup Bordeaux" dans l'expérience Upwiser ([src/cv.typ:132](../../../src/cv.typ#L132)), mais les autres engagements bénévoles ne sont pas documentés.

---

## 6. Sites Web

### Absents du CV (2 sites)

| # | URL | Type | Priorité | Action |
|---|-----|------|----------|--------|
| 1 | http://bastien.gallay.org/ | Blog personnel | 🟡 MOYENNE | Ajouter dans section contact |
| 2 | http://lemondedesparents.fr | Projet personnel | 🟢 BASSE | Optionnel |

**Note:** Le CV a une ligne commentée pour website ([src/cv.typ:15](../../../src/cv.typ#L15)):

```typst
// website: "https://docbrownlabs.com",
```

---

## 7. Notes Finales et Points d'Attention

### Points d'attention

1. **Équilibre 2 pages:** L'ajout de 2-3 expériences et d'une section bénévolat risque de faire déborder le CV sur une 3e page. Il faudra potentiellement:
   - Réduire certaines descriptions existantes
   - Déplacer le `#colbreak()` (actuellement ligne 184)
   - Ajuster la taille de police ou les marges
   - Fusionner certaines entrées (ex: ITS Group en note sous Cdiscount)

2. **Chronologie Upwiser:** L'activité semble avoir continué en parallèle de PALO IT (2021-2024). Si confirmé, il faut:
   - Clarifier dans la description (temps partiel? maintien structure?)
   - Potentiellement séparer en 2 périodes (2013-2021 puis 2021-2024)

3. **Missions freelance pendant Upwiser:** i-BP et DEKRA sont des missions freelance pendant la période Upwiser. Options:
   - Les lister séparément (meilleure visibilité)
   - Les mentionner dans la description Upwiser
   - Créer une sous-section "Missions notables"

### Questions restantes

- [ ] Upwiser: date de fin et statut parallèle avec PALO IT?
- [ ] PALO IT CTO: date de fin exacte?
- [ ] Boonty: date de début exacte et lien avec Qualia Services?
- [ ] Freelance 1999-2002: activité réelle ou études?
- [ ] DEA: INSTN vs UVSQ - diplôme délivré par qui?
- [ ] SAFe: certification obtenue en 2018 ou 2020?
- [ ] Format CV: Accepter 3 pages ou contraindre à 2 pages?

---

**Prochaine action recommandée:** Valider les dates critiques avec l'utilisateur avant toute modification du CV.
