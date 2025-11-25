# CNT-028: Ajouter activités communautaires et rayonnement

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-028 |
| **Titre** | Ajouter activités communautaires et rayonnement |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Sidebar / Experience |
| **Créé le** | 2025-11-25 |
| **Cible** | 2025-11-30 |
| **Terminé le** | 2025-11-25 |
| **Temps estimé** | 1h |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Ajouter les activités communautaires et de rayonnement identifiées dans le CV Flash mais absentes du CV actuel: Google Launchpad, Startup Weekend, et interventions conférences (Agile Tour, Scrum Day).

### Contexte

L'analyse CNT-015 du CV Flash a révélé plusieurs activités communautaires importantes qui valorisent l'expertise et le rayonnement professionnel mais qui ne figurent pas dans le CV actuel. Ces activités sont des marqueurs de crédibilité et d'engagement dans la communauté.

### Objectif

Intégrer les activités suivantes dans le CV:

1. **Mentor Google Launchpad** - Association marque Google, crédibilité internationale
2. **Coach Startup Weekend** - Techstars/Google for Startups, engagement communautaire
3. **Orateur Agile Tour** - Expertise reconnue, thought leadership
4. **Orateur Scrum Day** - Visibilité communauté agile française

---

## Sous-tâches

- [x] Décider de l'emplacement optimal (sidebar "Centres d'intérêt", nouvelle section, ou Upwiser)
- [x] Ajouter mention Google Launchpad Mentor
- [x] Ajouter mention Startup Weekend Coach
- [x] Ajouter mentions conférences (Agile Tour, Scrum Day)
- [x] Vérifier la compilation du CV
- [x] Valider le rendu PDF

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Options d'intégration:**

1. **Sidebar - Enrichir "Centres d'intérêt":**
   ```typst
   = Centres d'intérêt
   - Intelligence artificielle
   - Management et leadership
   - Entrepreneuriat
   - Communauté Agile (orateur, mentor)
   ```

2. **Sidebar - Nouvelle section "Rayonnement":**
   ```typst
   = Rayonnement
   - Mentor Google Launchpad
   - Coach Startup Weekend
   - Orateur Agile Tour & Scrum Day
   ```

3. **Section Upwiser - Enrichir "Autres activités":**
   Ajouter dans la section existante après les missions clients.

**Recommandation:**
Option 2 (nouvelle section) ou enrichissement de la description Upwiser pour maximiser la visibilité.

**Fichiers à modifier:**

- [cv.typ](../../src/cv.typ) - Sidebar (lignes 39-101) ou section Upwiser

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Points d'attention:**

- Google Launchpad et Startup Weekend sont des programmes prestigieux
- Les conférences Agile Tour et Scrum Day sont les principales conférences agiles françaises
- Vérifier si des sujets de conférence spécifiques sont disponibles

**Source:**
Recommandations CNT-015-R02, CNT-015-R03, CNT-015-R04 de l'analyse CV Flash

---

## Références externes

### Fichiers du projet

- [cv.typ:39-101](../../src/cv.typ#L39-L101) - Sidebar actuelle
- [cv.typ:296-300](../../src/cv.typ#L296-L300) - Section "Autres activités" Upwiser
- [cv-flash.md](../resources/audits/CNT-015/cv-flash.md) - Données extraites

### Tâches liées

- [CNT-015](./CNT-015-analyse-cv-flash.md) - Analyse source
- [CNT-027](./CNT-027-ajouter-missions-clients-upwiser-manquantes.md) - Missions clients (même analyse)

### Ressources

- Recommandations: CNT-015-R02, CNT-015-R03, CNT-015-R04

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(sidebar): ➕ add community activities and outreach

- Added Google Launchpad Mentor role
- Added Startup Weekend Coach role
- Added conference speaker mentions (Agile Tour, Scrum Day)

From CV Flash 2021 analysis (CNT-015-R02/R03/R04)

Closes CNT-028"
```

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le PDF s'affiche correctement
- [ ] Les activités communautaires sont visibles
- [ ] L'équilibre visuel de la sidebar est préservé
- [ ] Les commits suivent la convention

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée depuis CNT-015-R02/R03/R04 |

---

## Résultat final

[À remplir une fois la tâche terminée]
