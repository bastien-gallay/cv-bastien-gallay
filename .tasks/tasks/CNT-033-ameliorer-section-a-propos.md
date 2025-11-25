# CNT-033: Améliorer la section "À propos" avec métriques d'impact

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-033 |
| **Titre** | Améliorer la section "À propos" avec métriques d'impact |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT (Content) |
| **Section CV** | Sidebar / À propos |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | 2025-11-25 |
| **Temps estimé** | 45 min |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Réécrire la section "À propos" pour intégrer des métriques d'impact dès les premières lignes.

### Contexte

**Audit novembre 2025:**

La section "À propos" actuelle est trop générique:

> "Passionné de logiciel depuis l'enfance, j'accompagne les équipes techniques dans l'innovation et la transformation digitale depuis plus de 25 ans."

Cette formulation:

- Ne différencie pas des milliers d'autres profils
- Ne mentionne aucune réalisation concrète
- Ne met pas en avant les compétences clés (IA, CTO, Management)

### Objectif

- Intégrer des métriques d'impact chiffrées
- Mettre en avant les compétences différenciantes
- Créer un "pitch" mémorable en 2-3 phrases

---

## Sous-tâches

- [x] Identifier les métriques clés du CV (15% croissance, 50 personnes, etc.)
- [x] Rédiger une nouvelle version orientée résultats
- [x] Valider que ça tient dans l'espace sidebar
- [x] Compiler et vérifier le rendu

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Exemple de nouvelle formulation (audit):**

> "CTO expert en IA et Agilité. Pilotage de stratégies générant **15% de croissance** et management d'équipes de **50 personnes**."

**Proposition enrichie:**

> "CTO avec 25 ans d'expérience en développement logiciel. Expert IA Générative (Gen-e2, GitHub Copilot) et transformation Agile. Management de 50 professionnels techniques, contribution à 15% de croissance CA."

**Métriques disponibles dans le CV:**

- 15% de croissance du CA (PALO IT)
- Management de 50 professionnels techniques
- 20-40 certifications GitHub Copilot délivrées
- 6+ opportunités presales (€15k-€500k+)
- ~100 startups accompagnées (Upwiser)
- 150+ participants Agile Tour Bordeaux

**Fichiers à modifier:**

- [src/cv.typ](../../src/cv.typ) - Section sidebar "À propos"

**Structure recommandée:**

1. Phrase d'accroche avec rôle + expertise principale
2. Métriques d'impact (2-3 chiffres clés)
3. Domaines de spécialisation

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Choix des métriques:**

Sélectionner les 2-3 plus impactantes selon le poste visé:

- Pour CTO: croissance CA, taille équipe, stratégie
- Pour Tech Lead: certifications, innovations (Gen-e2)
- Pour Coach: startups accompagnées, communauté

**Longueur:**

La sidebar a un espace limité. Viser 3-4 lignes maximum.

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - Section "À propos"

### Tâches liées

- [CNT-032](./CNT-032-moderniser-entete-cv.md) - Moderniser en-tête (complémentaire)
- [CNT-034](./CNT-034-restructurer-experience-palo-it.md) - Restructurer PALO IT (source métriques)

### Ressources

- Audit CV novembre 2025

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(sidebar): ✏️ add impact metrics to About section

- Added key metrics (15% growth, 50 people managed)
- Highlighted GenAI expertise
- Made profile more memorable

Closes CNT-033"
```

---

## Tests / Vérifications

- [x] Le CV compile sans erreur
- [x] Le texte tient dans la sidebar
- [x] Les métriques sont exactes et vérifiables
- [x] Le ton reste professionnel

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée suite à audit CV |

---

## Résultat final

**Avant:**
> "Passionné de logiciel depuis l'enfance, j'accompagne les équipes techniques dans l'innovation et la transformation digitale depuis plus de 25 ans."

**Après:**
> "CTO avec 25 ans d'expérience. Expert IA Générative et transformation Agile. Management de 50 professionnels techniques, contribution à 15% de croissance CA."

- Métriques clés intégrées (50 personnes, 15% croissance)
- Expertise IA mise en avant
- Texte concis et impactant
