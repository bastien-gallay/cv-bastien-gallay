# Extraction de Source - [TYPE DE SOURCE]

**Analyse:** [TASK-ID]
**Date d'extraction:** [YYYY-MM-DD]
**Source:** [URL ou description]
**Type:** [LinkedIn / GitHub / CV Externe / Website / Autre]

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **Source URL** | [URL complète] |
| **Date d'accès** | [YYYY-MM-DD HH:MM] |
| **Méthode d'extraction** | [Scraping / Export officiel / Manuel / Autre] |
| **Complétude** | [Partielle / Complète] |
| **Notes** | [Remarques sur l'extraction] |

---

## [Section 1 - Adapter selon le type de source]

[Contenu extrait de la première section]

### Sous-section si nécessaire

[Données structurées]

---

## [Section 2]

[Contenu extrait]

---

## [Section N]

[Contenu extrait]

---

## Notes d'Extraction

### Difficultés Rencontrées

- [Liste des difficultés ou limitations]
- [Sections inaccessibles]
- [Données manquantes]

### Éléments Non Extraits

- [Liste des éléments présents mais non extraits]
- [Raisons: technique, pertinence, etc.]

### Qualité des Données

- **Complétude:** [%]
- **Fiabilité:** [Haute / Moyenne / Faible]
- **Actualité:** [À jour / Légèrement obsolète / Obsolète]

---

## Templates par Type de Source

### Template LinkedIn Profile

```markdown
# Extraction LinkedIn Profile

## 1. Informations de profil

| Champ | Valeur |
|-------|--------|
| **Nom complet** | [Nom] |
| **Headline** | [Titre professionnel] |
| **Localisation** | [Ville, Région, Pays] |
| **Réseau** | [X followers, Y connections] |
| **Emploi actuel** | [Entreprise/Statut] |

## 2. Expériences professionnelles (N postes)

### [Entreprise 1] - [Titre poste]

- **Dates:** [MM/YYYY - MM/YYYY (durée)]
- **Lieu:** [Localisation]
- **Type:** [CDI / Freelance / Stage / etc.]
- **Description:**
  - [Point 1]
  - [Point 2]
  - [Point 3]

[Répéter pour chaque expérience]

## 3. Éducation (N diplômes)

1. **[Institution]**
   - Diplôme: [Nom du diplôme, spécialisation]
   - Dates: [YYYY - YYYY]
   - Notes: [Mention, sujet de recherche, etc.]

## 4. Langues (N langues)

| Langue | Niveau |
|--------|--------|
| [Langue 1] | [Niveau descriptif] |
| [Langue 2] | [Niveau descriptif] |

## 5. Certifications (N certifications)

1. **[Nom certification]** - [Organisme] ([Date])
2. **[Nom certification]** - [Organisme] ([Date])

## 6. Compétences (Skills & Endorsements)

[Liste des compétences avec nombre d'endorsements si disponible]

## 7. Expérience bénévole (N organisations)

1. **[Organisation] - [Rôle]**
   - Dates: [MM/YYYY - MM/YYYY ou aujourd'hui]
   - Description: [Activités]

## 8. Publications / Projets

[Si applicable]

## 9. Recommandations

| Date | Nom | Rôle | Relation | Résumé |
|------|-----|------|----------|--------|
| [Date] | [Nom] | [Fonction] | [Type relation] | [Points clés] |

## 10. Sites web / Liens

- [URL 1] - [Description]
- [URL 2] - [Description]
```

### Template GitHub Profile

```markdown
# Extraction GitHub Profile

## 1. Informations de profil

| Champ | Valeur |
|-------|--------|
| **Username** | [username] |
| **Nom** | [Nom complet] |
| **Bio** | [Bio GitHub] |
| **Localisation** | [Lieu] |
| **Email public** | [Email si disponible] |
| **Site web** | [URL] |
| **Entreprise** | [Entreprise actuelle] |

## 2. Statistiques Globales

- **Repositories publics:** [N]
- **Contributions dernière année:** [N]
- **Followers:** [N]
- **Following:** [N]
- **Stars reçues:** [N total]
- **Member since:** [Date]

## 3. Repositories Principaux

### [Nom repo 1]

- **URL:** [URL complète]
- **Description:** [Description]
- **Langage principal:** [Langage]
- **Stars:** [N] | **Forks:** [N]
- **Dernière activité:** [Date]
- **Topics:** [Liste des topics]

[Répéter pour top 5-10 repos]

## 4. Langages de Programmation

[Liste des langages utilisés avec pourcentage si disponible]

- [Langage 1]: [X%]
- [Langage 2]: [Y%]

## 5. Contributions Notables

- [Organisation/Projet 1]: [Type de contribution]
- [Organisation/Projet 2]: [Type de contribution]

## 6. Activité Récente

[Résumé de l'activité des 3-6 derniers mois]

- Commits: [N]
- PRs: [N]
- Issues: [N]
- Reviews: [N]
```

### Template CV Externe

```markdown
# Extraction CV Externe

## 1. Informations générales

| Champ | Valeur |
|-------|--------|
| **Source** | [Nom fichier / URL] |
| **Format** | [PDF / Word / Web / Autre] |
| **Date du CV** | [Date si indiquée] |
| **Nombre de pages** | [N] |
| **Structure** | [Chronologique / Par compétences / Hybride] |

## 2. Coordonnées

[Informations de contact extraites]

## 3. Résumé / Objectif

[Texte du résumé professionnel si présent]

## 4. Expériences Professionnelles

[Extraction similaire à template LinkedIn]

## 5. Formations

[Extraction des diplômes et formations]

## 6. Compétences

### Compétences techniques

[Liste]

### Compétences transversales

[Liste]

## 7. Langues

[Liste avec niveaux]

## 8. Autres sections

[Certifications, publications, bénévolat, hobbies, etc.]

## 9. Analyse de Structure

- **Points forts de la structure:** [Liste]
- **Points à améliorer:** [Liste]
- **Éléments manquants:** [Liste]
```

---

## Guide d'Utilisation

### Choix du Template

1. **LinkedIn Profile:** Pour audits de présence en ligne professionnelle
2. **GitHub Profile:** Pour validation de compétences techniques et projets
3. **CV Externe:** Pour benchmarking ou analyse de concurrent

### Workflow d'Extraction

1. **Copier le template** approprié
2. **Remplir les métadonnées** en haut du fichier
3. **Extraire les données** section par section
4. **Noter les difficultés** et limitations
5. **Sauvegarder** dans `audits/[TASK-ID]/[source-name].md`

### Bonnes Pratiques

- ✅ **Être exhaustif:** Extraire même ce qui semble non pertinent
- ✅ **Conserver le format original:** Citations, listes à puces, etc.
- ✅ **Dater l'extraction:** Les profils changent dans le temps
- ✅ **Noter les sources:** URLs, sections, etc.
- ⚠️ **Respecter la confidentialité:** Ne pas extraire de données sensibles
- ⚠️ **Vérifier l'autorisation:** Avoir le droit d'extraire ces données

### Outils Utiles

- **LinkedIn:** Export officiel (Settings → Get a copy of your data)
- **GitHub:** API GitHub pour automatisation
- **PDF:** Extraction manuelle ou outils de parsing
- **Web:** Copier/coller ou outils de scraping (avec autorisation)
