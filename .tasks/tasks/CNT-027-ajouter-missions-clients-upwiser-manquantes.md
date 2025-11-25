# CNT-027: Ajouter les missions clients Upwiser manquantes

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-027 |
| **Titre** | Ajouter les missions clients Upwiser manquantes |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-11-25 |
| **Cible** | 2025-11-30 |
| **Terminé le** | - |
| **Temps estimé** | 1.5h |
| **Temps réel** | - |
| **Branche nécessaire** | Non |

---

## Description

Ajouter les 5 missions clients mentionnées dans le CV Flash (2021) mais absentes du CV actuel, dans la section "Expérience détaillée" Upwiser.

### Contexte

L'analyse CNT-015 du CV Flash a identifié 5 missions clients qui démontrent la diversité des interventions mais qui ne figurent pas dans le CV actuel. Ces missions enrichiraient significativement le CV en montrant l'expérience dans différents secteurs (Fintech, E-commerce, Événementiel, Immobilier, Jeux).

### Objectif

Enrichir la section "Expérience détaillée" Upwiser avec les missions suivantes:

1. **Dronisos** - Startup événementiel (structuration R&D, innovation)
2. **Wanteeed.com** - Startup Web (Coach Agile, modèle organisationnel)
3. **Mieux Placer** - Fintech (accompagnement PO, formation)
4. **Groupe SeLoger/Logic Immo** - Immobilier (audit architecture, développement)
5. **JOA Online** - Jeux en ligne (Product Owner)

---

## Sous-tâches

- [ ] Rechercher des détails supplémentaires sur chaque mission (dates, durée, contexte)
- [ ] Ajouter mission Dronisos dans cv.typ
- [ ] Ajouter mission Wanteeed.com dans cv.typ
- [ ] Ajouter mission Mieux Placer dans cv.typ
- [ ] Ajouter mission Groupe SeLoger/Logic Immo dans cv.typ
- [ ] Ajouter mission JOA Online dans cv.typ
- [ ] Vérifier la compilation du CV
- [ ] Valider le rendu PDF

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Format à suivre:**
Utiliser le même format que les missions DEKRA et i-BP existantes dans la section "Expérience détaillée":

```typst
==== Mission [Client] - [Rôle] ([dates])
#strong[Client:] [Nom], [Ville]
#strong[Durée:] X mois/ans

- Point 1
- Point 2
- #strong[Méthodes:] Scrum, Kanban, etc.
```

**Informations disponibles (CV Flash):**

1. **Dronisos** - Startup événementiel
   - Structuration de l'équipe R&D
   - Réorganisation des démonstrations pour l'innovation technique

2. **Wanteeed.com** - Startup Web
   - Remplacement de la Product Owner
   - Coach Agile pour startup de 20 personnes
   - Élaboration d'un modèle organisationnel agile

3. **Mieux Placer** - Fintech
   - Accompagnement du Product Owner
   - Formation des équipes de production

4. **Groupe SeLoger/Logic Immo** - Immobilier
   - Audit de la solution en place et proposition d'une architecture cible
   - Développement du nouveau système

5. **JOA Online** - Jeux en ligne
   - Product Owner

**Fichiers à modifier:**

- [cv.typ](../../src/cv.typ) - Section Expérience détaillée (après ligne 300)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Points d'attention:**

- Vérifier les dates exactes de chaque mission si possible
- Les descriptions du CV Flash sont synthétiques, enrichir si des détails sont disponibles
- Respecter l'ordre chronologique inverse

**Source:**
Recommandation CNT-015-R01 de l'analyse CV Flash

---

## Références externes

### Fichiers du projet

- [cv.typ:265-301](../../src/cv.typ#L265-L301) - Section Expérience détaillée existante
- [cv-flash.md](../resources/audits/CNT-015/cv-flash.md) - Données extraites

### Tâches liées

- [CNT-015](./CNT-015-analyse-cv-flash.md) - Analyse source
- [CNT-008](./CNT-008-ajouter-experience-ibp.md) - Format de référence (i-BP)
- [CNT-009](./CNT-009-ajouter-experience-dekra.md) - Format de référence (DEKRA)

### Ressources

- Recommandation: CNT-015-R01

---

## Commits Git associés

### Commit final

```bash
git commit -m "content(experience): ➕ add missing Upwiser client missions

- Added Dronisos (event startup R&D)
- Added Wanteeed.com (Web startup coaching)
- Added Mieux Placer (Fintech PO coaching)
- Added Groupe SeLoger/Logic Immo (architecture audit)
- Added JOA Online (Product Owner)

From CV Flash 2021 analysis (CNT-015-R01)

Closes CNT-027"
```

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le PDF s'affiche correctement
- [ ] Les 5 missions sont visibles dans la section Expérience détaillée
- [ ] Le format est cohérent avec DEKRA et i-BP
- [ ] Les commits suivent la convention

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée depuis CNT-015-R01 |

---

## Résultat final

[À remplir une fois la tâche terminée]
