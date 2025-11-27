# CNT-036: Condensation et impact business (version longue)

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-036 |
| **Titre** | Condensation et impact business (version longue) |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT (Content) |
| **Section CV** | General |
| **Créé le** | 2025-11-27 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 2-3 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Oui |

---

## Description

Condenser le CV long de 5 à ~3 pages (objectif flexible) tout en améliorant la lisibilité de l'impact business pour le marché français (Paris/Bordeaux).

### Contexte

Retours d'un expert recrutement tech (novembre 2025) :

- Le marché français est exigeant sur la **lisibilité de l'impact business**
- Un recruteur/CEO ne doit pas se demander "ce qu'il a fait" mais "ce qu'il a rapporté/économisé"
- L'IA Générative est le levier clé : les entreprises cherchent des leaders capables de dépasser le POC
- Le CTO "Hybride" (Tech + Business) qui comprend le P&L est recherché

### Objectif

- Réduire le CV de 5 à ~3 pages (flexible)
- Améliorer le titre et positionnement (IA Générative, mobilité)
- Réécrire le résumé/profil pour un ton "vendeur CEO"
- Mettre en gras les résultats chiffrés (€, volumes, partenariats)
- Condenser Upwiser en bloc "Achievements"
- Simplifier les expériences pré-2010
- Consolider les certifications

---

## Sous-tâches

- [ ] Améliorer titre et positionnement
- [ ] Réécrire résumé/profil vendeur
- [ ] Mettre en avant impact business Palo IT (gras sur chiffres)
- [ ] Condenser section Upwiser (2013-2021)
- [ ] Simplifier expériences pré-2010
- [ ] Consolider certifications sur 1-2 lignes
- [ ] Corrections mineures (dates, anglais)
- [ ] Vérifier compilation et rendu final

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

### Mode interactif

> **IMPORTANT** : Cette tâche nécessite une validation utilisateur avant exécution.

#### Questions au démarrage

Avant de commencer les modifications, poser les questions suivantes :

##### Positionnement

1. **Mobilité** : Quel rythme de mobilité Paris/Bordeaux réel ? (ex: "2j/semaine à Paris", "Full remote avec déplacements")
2. **Titre préféré** : Parmi ces options, laquelle préférez-vous ?
   - "CTO / VP Engineering - Expert IA Générative & Transformation"
   - "CTO - Expert IA Générative & Leadership Tech"
   - "VP Engineering - Transformation Agile & IA"
3. **Situation actuelle** : Êtes-vous toujours chez Palo IT ou en transition ?

##### Impact business

4. **Chiffres prioritaires** : Quels chiffres/résultats mettre en avant en priorité pour Palo IT ?
5. **Métriques supplémentaires** : Y a-t-il des métriques non mentionnées dans le CV actuel ? (CA généré, économies réalisées, etc.)

##### Condensation Upwiser (2013-2021)

6. **Réalisations majeures** : Parmi ces réalisations, lesquelles mettre en avant ?
   - Pilotage transformations Agiles à l'échelle (SAFe, Scrum) pour grands comptes (Dekra, i-BP)
   - Structuration R&D pour scale-ups (Dronisos, Wanteeed)
   - Coaching de CTOs et refonte architectures techniques (Nalo, SeLoger)
   - Accompagnement +100 startups et grands comptes
   - Formations et certifications délivrées
7. **Clients à mentionner** : Y a-t-il des clients à mentionner absolument ? Des clients à ne pas mentionner ?

##### Expériences anciennes

8. **Pré-2010** : Y a-t-il des clients/réalisations Cast Consulting ou Boonty à conserver absolument ?
9. **Niveau d'anglais** : C1 ou C2 ?

#### Processus

1. Poser les questions ci-dessus
2. Attendre les réponses de l'utilisateur
3. Proposer les modifications section par section
4. Demander validation avant d'appliquer chaque modification majeure
5. Itérer si nécessaire

---

### Transformations spécifiques

#### Titre CV

**Avant** : "Expert IA / CTO & Engineering Manager"
**Après** : "CTO / VP Engineering - Expert IA Générative & Transformation"
**Sous-titre** : "Stratégie Tech, Efficacité Agile & Innovation (Paris / Bordeaux / Remote)"

#### Résumé/Profil

**Proposition** :
"CTO avec 25 ans d'expérience, alliant leadership technique et vision business. Expert dans l'industrialisation de l'IA Générative et la transformation Agile des organisations. Je structure les équipes tech (jusqu'à 50p) pour maximiser la vélocité et l'impact business. Mobile Paris/Bordeaux."

#### Impact business Palo IT

Mettre en **gras** les résultats chiffrés :

- "Business Development : Pilotage technique de **6 opportunités majeures (jusqu'à 500k€)** et partenariats stratégiques (Scaleway, Mistral)."
- "Framework **Gen-e2** : Accélération du développement via l'IA et déploiement de **GitHub Copilot (40 certifications)**."

#### Upwiser condensé

Format cible :

```text
Gérant & Coach Agile - Upwiser (2013-2021)
"Accompagnement de la transformation numérique de +100 startups et grands comptes"

• Pilotage de transformations Agiles à l'échelle (SAFe, Scrum) pour grands comptes (Dekra, i-BP)
• Structuration R&D et coaching CTOs pour scale-ups (Dronisos, Wanteeed, Nalo)
• Refonte d'architectures techniques et accompagnement au recrutement (SeLoger)
```

#### Certifications consolidées

Format cible :

```text
Scrum.org & Scaled Agile : PSM I & II, PSD, SPS (Nexus), SAFe Program Consultant (SPC5)
```

---

**Fichiers à modifier:**

- [src/cv.typ](../../src/cv.typ) - CV complet (5 pages → ~3 pages)

**Points d'attention:**

- Compiler après chaque modification majeure (`just build`)
- Vérifier le nombre de pages résultant
- Préserver les informations importantes (ne pas supprimer, condenser)
- Maintenir la cohérence avec cv-short.typ

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Source des retours :**

Analyse expert recrutement tech (novembre 2025) couvrant :

- Lisibilité de l'impact business
- Positionnement marché français (Paris/Bordeaux)
- Tendances IA Générative et CTO Hybride

**Décisions à prendre :**

- Titre exact du CV
- Rythme de mobilité à afficher
- Niveau de détail pour Upwiser
- Clients à mettre en avant

---

## Références externes

### Fichiers du projet

- [src/cv.typ](../../src/cv.typ) - CV complet à modifier

### Tâches liées

- [LAY-002](./LAY-002-consolidation-sections-dupliquees.md) - Consolider sections dupliquées (complémentaire)
- [LAY-003](./LAY-003-reorganiser-competences-3-poles.md) - Réorganiser compétences (complémentaire)
- [CNT-037](./CNT-037-optimisation-version-courte.md) - Optimisation version courte (à faire après)

### Ressources

- Retours expert recrutement tech (novembre 2025)

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "content(cv): ✨ improve title and positioning

Add AI expertise and mobility mention.

Refs CNT-036"
```

### Commit final

```bash
git commit -m "content(cv): ✨ condense CV and improve business impact

- Improved title: CTO / VP Engineering - Expert IA Générative
- Rewritten profile for CEO/decision-maker audience
- Bold formatting on key business metrics (€, volumes)
- Condensed Upwiser section (2013-2021) into achievements block
- Simplified pre-2010 experiences
- Consolidated certifications into 1-2 lines
- Reduced from 5 to ~3 pages

Closes CNT-036"
```

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Le nombre de pages est réduit (objectif ~3 pages)
- [ ] Le titre reflète le positionnement IA/CTO
- [ ] Les chiffres business sont en gras et visibles
- [ ] La section Upwiser est condensée mais complète
- [ ] Les certifications sont sur 1-2 lignes
- [ ] La cohérence avec cv-short.typ est préservée

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-27 | Création | Tâche créée suite aux retours expert recrutement |

---

## Résultat final

[À remplir une fois la tâche terminée]
