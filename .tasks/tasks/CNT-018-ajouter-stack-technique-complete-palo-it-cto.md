# CNT-018: Ajouter stack technique complète PALO IT CTO

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-018 |
| **Titre** | Ajouter stack technique complète PALO IT CTO |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | Experience |
| **Créé le** | 2025-11-25 |
| **Cible** | 2025-12-02 |
| **Terminé le** | - |
| **Temps estimé** | 45 minutes |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Ajouter la stack technique complète (cloud, AI/ML, langages, patterns d'architecture) dans la description de l'expérience CTO PALO IT.

### Contexte

L'analyse CNT-014 a révélé que le CV ne mentionne **aucune technologie spécifique** pour l'expérience CTO, alors que les données du journal montrent une stack technique très riche et diversifiée :
- **Cloud** : Azure (Databricks, SQL Hyperscale, Cosmos DB), AWS (Bedrock), Scaleway
- **AI/ML** : OpenAI, Anthropic, LangChain, OpenSearch, Pinecone, Kendra, PGVector, GitHub Copilot, Codestral
- **Langages** : Python, C#, TypeScript, Rust
- **Architecture** : MAC, BFF, REST API, microservices, multi-cloud

Cette absence nuit à la crédibilité technique du profil et réduit sa visibilité dans les recherches ATS.

### Objectif

Intégrer toutes les technologies et patterns d'architecture dans la description de l'expérience PALO IT CTO de manière structurée et lisible.

---

## Sous-tâches

- [ ] Localiser l'entrée expérience PALO IT CTO dans cv.typ (lignes 107-121)
- [ ] Ajouter la stack cloud (Azure, AWS, Scaleway)
- [ ] Ajouter la stack AI/ML (OpenAI, Anthropic, LangChain, etc.)
- [ ] Ajouter les langages de programmation (Python, C#, TypeScript, Rust)
- [ ] Ajouter les patterns d'architecture (MAC, BFF, REST API, microservices)
- [ ] Structurer l'affichage pour éviter la surcharge visuelle
- [ ] Compiler le CV et vérifier l'affichage
- [ ] Valider que les technologies sont cohérentes avec le rôle CTO

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Technologies à ajouter dans [cv.typ:107-121](../../src/cv.typ#L107-L121)** :

**Stack Cloud** :
- Azure : Databricks, SQL Hyperscale, Cosmos DB
- AWS : Bedrock
- Scaleway

**Stack AI/ML** :
- LLMs : OpenAI, Anthropic (Claude)
- Frameworks : LangChain
- Vector databases : OpenSearch, Pinecone, Kendra, PGVector
- Coding assistants : GitHub Copilot, Codestral (Mistral)

**Langages de programmation** :
- Python, C#, TypeScript, Rust

**Patterns d'architecture** :
- Managed API Composition (MAC)
- Backend for Frontend (BFF)
- REST API
- Microservices
- Multi-cloud

**Suggestions de présentation** :
- Regrouper par catégorie (Cloud / AI-ML / Langages / Architecture)
- Utiliser une présentation concise (bullet points ou liste compacte)
- Éviter la surcharge visuelle tout en montrant l'étendue technique

**Outils/commandes à utiliser:**

- `just build` pour compiler et vérifier le PDF

**Fichiers à consulter:**

- [cv.typ:107-121](../../src/cv.typ#L107-L121) - Expérience PALO IT CTO
- [Audit CNT-014](../resources/audits/CNT-014/palo-it-cto-activities.md) - Données sources

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Origine des données** :
- Analyse CNT-014 basée sur le journal CTO (mars-juillet 2025)
- Recommandations CNT-014-R03 (cloud), R04 (AI/ML), R11 (langages), R12 (architecture)

**Points d'attention** :
- Équilibrer exhaustivité et lisibilité
- Prioriser les technologies les plus significatives si l'espace est limité
- Maintenir la cohérence avec le niveau d'expertise attendu d'un CTO

---

## Références externes

### Fichiers du projet

- [cv.typ:107-121](../../src/cv.typ#L107-L121) - Expérience PALO IT CTO actuelle

### Tâches liées

- [CNT-014](./CNT-014-analyse-experience-palo-it.md) - Analyse source (terminée)
- [CNT-017](./CNT-017-corriger-donnees-critiques-experience-palo-it-cto.md) - Corrections critiques
- [CNT-019](./CNT-019-ajouter-projets-clients-et-resultats-business-palo-it-cto.md) - Projets clients

### Ressources

- [Analyse CNT-014](../resources/analyses/CNT-014/audit-report.md) - Rapport d'analyse complet
- [Recommandations CNT-014](../resources/analyses/CNT-014/recommendations-status.md) - R03, R04, R11, R12

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "content(experience): 🔧 add technical stack to PALO IT CTO

Refs CNT-018"
```

### Commit final

```bash
git commit -m "content(experience): 🔧 add complete technical stack to PALO IT CTO

- Added cloud stack: Azure (Databricks, SQL Hyperscale, Cosmos DB), AWS, Scaleway
- Added AI/ML stack: OpenAI, Anthropic, LangChain, vector databases
- Added programming languages: Python, C#, TypeScript, Rust
- Added architecture patterns: MAC, BFF, REST API, microservices

Significantly improves technical credibility and ATS visibility.

Closes CNT-018"
```

**Format suggéré:**

- **Type**: content (modification de contenu)
- **Scope**: experience
- **Emoji**: 🔧 (ajout de technologies)

---

## Tests / Vérifications

- [ ] Le CV compile sans erreur (`just build`)
- [ ] Les technologies s'affichent de manière structurée et lisible
- [ ] Pas de débordement de texte ou de mise en page cassée
- [ ] Les technologies correspondent au niveau CTO
- [ ] Cohérence avec les autres expériences techniques

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée depuis recommandations CNT-014-R03, R04, R11, R12 |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait:**

- [Liste des réalisations]

**Difficultés rencontrées:**

- [Problèmes et solutions]

**Améliorations futures:**

- [Idées pour aller plus loin]
