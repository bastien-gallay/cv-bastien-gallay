# LAY-003: Réorganiser les compétences en 3 pôles

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | LAY-003 |
| **Titre** | Réorganiser les compétences en 3 pôles thématiques |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | LAY (Layout) |
| **Section CV** | Sidebar / Skills |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 1 heure |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |
| **Prérequis** | [LAY-001](./LAY-001-sidebar-premiere-page-uniquement.md) |

---

## Description

Restructurer la section compétences pour une lecture rapide et un impact maximum.

### Contexte

**Audit novembre 2025:**

Les compétences actuelles sont situées en marge (sidebar) et dispersées. Elles doivent être centralisées pour une lecture rapide.

**Problème actuel:**

- Skills techniques mélangés (Lean, Scrum, TypeScript, Node.js...)
- Pas de hiérarchie claire
- Débordement sur page 2 (Python, Java, C#, etc.)

### Objectif

Proposer 3 pôles clairs:

1. **Leadership:** Management 50+, Recrutement, Stratégie
2. **Tech & IA:** GenAI, Python, Azure/AWS, Architecture DDD
3. **Méthodologie:** SAFe, Lean Startup, Craftsmanship

---

## Sous-tâches

- [ ] Lister toutes les compétences actuelles du CV
- [ ] Catégoriser en 3 pôles (Leadership, Tech & IA, Méthodologie)
- [ ] Prioriser les compétences les plus pertinentes par pôle (5-7 max)
- [ ] Modifier la structure dans cv.typ
- [ ] Déplacer les compétences secondaires vers cv-exhaustive.typ
- [ ] Vérifier que tout tient sur page 1 (sidebar)
- [ ] Compiler et vérifier le rendu

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

### Mode interactif

> **IMPORTANT** : Cette tâche nécessite une validation utilisateur avant exécution.

#### Questions au démarrage

Avant de commencer les modifications, poser les questions suivantes :

1. **Noms des pôles** : Les intitulés "Leadership", "Tech & IA", "Méthodologie" vous conviennent-ils ? Alternatives : "Management", "Technologie", "Agilité"
2. **Priorisation Leadership** : Quels éléments de leadership mettre en avant ? (Management 50+, COMEX, Recrutement, Stratégie Tech)
3. **Focus IA** : GenAI doit-il apparaître en premier dans "Tech & IA" pour capter l'attention des recruteurs ?
4. **Langages de programmation** : Faut-il les inclure (Python, TypeScript) ou se concentrer sur les compétences de niveau CTO ?
5. **Certifications méthodologiques** : Mentionner "SAFe SPC5" ou simplement "SAFe" ?

#### Processus

1. Poser les questions ci-dessus
2. Attendre les réponses de l'utilisateur
3. Proposer la structure complète basée sur les réponses
4. Demander validation avant d'appliquer
5. Itérer si nécessaire

---

**Structure recommandée (audit):**

```typst
== Expertises

=== Leadership
#item-pills(
  "Management 50+",
  "Stratégie Tech",
  "COMEX",
  "Recrutement",
)

=== Tech & IA
#item-pills(
  "GenAI",
  "Python",
  "TypeScript",
  "Azure/AWS",
  "DDD",
)

=== Méthodologie
#item-pills(
  "SAFe SPC",
  "Scrum",
  "Lean Startup",
  "Craftsmanship",
)
```

**Compétences actuelles à trier:**

*Méthodologies:*

- Lean, Scrum, Kanban, eXtreme Programming
- Design Thinking, TDD, BDD, Clean Code, DDD

*Techniques:*

- TypeScript, Node.js, React, SQL
- Python, Java, C#, C, Rust

*Autres:*

- Management, Développement, Architecture

**Priorisation pour profil CTO:**

- Leadership: en premier (différenciant)
- Tech & IA: GenAI prioritaire (tendance marché)
- Méthodologie: SAFe, Craftsmanship (niveau senior)

**Fichiers à modifier:**

- [src/cv.typ](../../src/cv.typ) - Section Expertises (sidebar)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Choix stratégiques:**

- Les langages de programmation (Python, TypeScript) sont moins prioritaires pour un CTO
- L'accent sur l'IA est crucial en 2024-2025
- Le management d'équipe (50 personnes) est un différenciateur fort

**Alternative:**

Si l'espace le permet, ajouter des niveaux (expert, avancé, familier) mais attention à la surcharge visuelle.

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - Section Expertises

### Tâches liées

- [LAY-001](./LAY-001-sidebar-premiere-page-uniquement.md) - **Prérequis** : sidebar doit tenir sur page 1 avant réorganisation
- [CNT-034](./CNT-034-restructurer-experience-palo-it.md) - Restructurer PALO IT (cohérence)

### Ressources

- Audit CV novembre 2025

---

## Commits Git associés

### Commit final

```bash
git commit -m "style(skills): 🎨 reorganize skills into 3 thematic poles

- Leadership: Management 50+, Strategy, COMEX
- Tech & IA: GenAI, Python, Azure/AWS, DDD
- Methodology: SAFe, Lean Startup, Craftsmanship

Closes LAY-003"
```

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur
- [ ] Les 3 pôles sont clairement distincts
- [ ] Tout tient sur la page 1 (sidebar)
- [ ] Les compétences prioritaires sont visibles
- [ ] Compétences secondaires dans cv-exhaustive.typ

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée suite à audit CV |

---

## Résultat final

[À remplir une fois la tâche terminée]
