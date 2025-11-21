# CV Analyses Dashboard

Ce fichier sert de tableau de bord central pour toutes les analyses externes effectuées sur le CV (audits LinkedIn, GitHub, comparaisons avec CVs externes, etc.).

## À propos

Chaque analyse peut générer plusieurs **recommandations** qui sont suivies individuellement. Les recommandations peuvent ensuite être transformées en **tâches concrètes** via la commande `/task-from-analysis`.

## Convention d'identifiants

- **ID Analyse**: Utilise l'ID de la tâche qui a effectué l'analyse (ex: `CNT-001`)
- **ID Recommandation**: Format `{ANALYSIS-ID}-R{NN}` (ex: `CNT-001-R05`)
- **Fichiers de ressources**:
  - Sources: `.tasks/resources/audits/{ANALYSIS-ID}/`
  - Analyses: `.tasks/resources/analyses/{ANALYSIS-ID}/`

## Statuts possibles

- 🔄 **En cours** - Analyse en cours d'exécution
- ✅ **Terminé** - Analyse complète avec recommandations
- 📋 **Partiellement traité** - Certaines recommandations converties en tâches
- ✔️ **Entièrement traité** - Toutes les recommandations converties en tâches

---

## Analyses Actives

| ID | Type | Source | Statut | Créé le | Recommandations | Tâches créées |
|----|------|--------|--------|---------|----------------|--------------|
| [CNT-001](resources/analyses/CNT-001/) | LinkedIn Audit | [linkedin.com/in/bastiengallay](https://linkedin.com/in/bastiengallay/) | ✅ Terminé | 2025-10-29 | 19 total (1 très haute, 10 hautes, 5 moyennes, 3 basses) | 11/19 (58%) |
| [CNT-013](resources/analyses/CNT-013/) | CV Comparatif | CV 2019 (Mars 2019) | ✅ Terminé | 2025-11-14 | 14 total (2 très hautes, 4 hautes, 6 moyennes, 2 basses) | 0/14 (0%) |
| [CNT-014](resources/analyses/CNT-014/) | Journal CTO | Journal CTO PALO IT (mars-juillet 2025) | ✅ Terminé | 2025-11-18 | 25 total (5 très hautes, 10 hautes, 7 moyennes, 3 basses) | 0/25 (0%) |

---

## Analyses Archivées

_Aucune analyse archivée pour le moment._

Les analyses sont archivées lorsque toutes leurs recommandations ont été traitées (converties en tâches et complétées).

---

## Statistiques Globales

- **Total analyses**: 3
- **En cours**: 0
- **Terminées**: 3
- **Recommandations totales**: 58
- **Recommandations pendantes**: 47 (81%)
- **Tâches créées depuis analyses**: 11

### Répartition par priorité

| Priorité | Nombre | Pourcentage |
|----------|--------|-------------|
| 🔴🔴 Très Haute | 8 | 14% |
| 🔴 Haute | 24 | 41% |
| 🟡 Moyenne | 18 | 31% |
| 🟢 Basse | 8 | 14% |

---

## Utilisation

### Créer une nouvelle analyse

1. Créer une tâche pour l'analyse (ex: `CNT-002`)
2. Utiliser `/analyze-source` pour extraire les données sources
3. Effectuer l'analyse comparative
4. Créer le fichier `recommendations-status.md` dans `resources/analyses/{ID}/`
5. Ajouter l'entrée dans ce fichier (section "Analyses Actives")

### Transformer des recommandations en tâches

```bash
/task-from-analysis

> Sélectionner l'analyse: CNT-001
> Sélectionner les recommandations: 1,5,6
> [Création interactive des tâches...]
```

La commande mettra automatiquement à jour:

- Le fichier `recommendations-status.md` (marquer "tâche créée")
- Ce fichier ANALYSES.md (statistiques)
- Le fichier TASKS.md (ajout des nouvelles tâches)

---

## Détails des Analyses

### CNT-001: LinkedIn Audit

**Objectif**: Identifier tous les écarts entre le profil LinkedIn et le CV actuel

**Sources analysées**:

- Profil LinkedIn: [bastiengallay](https://linkedin.com/in/bastiengallay/)
- CV actuel: [src/cv.typ](../src/cv.typ)

**Fichiers de ressources**:

- Audit: [resources/audits/CNT-001/](resources/audits/CNT-001/)
- Analyse: [resources/analyses/CNT-001/](resources/analyses/CNT-001/)

**Résultats clés**:

- 10 expériences professionnelles analysées
- 4 expériences manquantes dans le CV
- 7 incohérences de dates identifiées
- 3 certifications manquantes
- 6 expériences bénévoles non documentées

**Recommandations**:

- Voir le [fichier de recommandations](resources/analyses/CNT-001/recommendations-status.md)
- Priorité globale: 🔴 HAUTE

**Prochaines actions**:

1. Clarifier les 4 écarts critiques de dates avec l'utilisateur
2. Créer les tâches de correction via `/task-from-analysis`
3. Exécuter les corrections par ordre de priorité

---

### CNT-013: Analyse Ancien CV > 5 ans (2019)

**Objectif**: Identifier les écarts entre le CV actuel (2025) et l'ancien CV (Mars 2019) pour récupérer informations perdues et corriger incohérences

**Sources analysées**:

- CV 2019: `.tasks/resources/sources-analyses/CV-2019/CV_Bastien_GALLAY_Coach_Agile-201903.docx(1).md`
- CV actuel: `src/cv.typ`

**Fichiers de ressources**:

- Audits: [resources/audits/CNT-013/](resources/audits/CNT-013/)
  - `cv-2019.md` - Extraction structurée du CV 2019
  - `cv-snapshot.md` - Snapshot du CV actuel au moment de l'analyse
- Analyses: [resources/analyses/CNT-013/](resources/analyses/CNT-013/)
  - `audit-report.md` - Rapport d'analyse comparative (1245 lignes)
  - `recommendations-status.md` - Suivi des recommandations
  - `metrics.md` - Métriques et statistiques détaillées

**Résultats clés**:

- **Score global**: 7.5/10 (excellent positionnement, manque de contenu)
- **2 erreurs critiques de dates**:
  - Indépendant: 06/1999-06/2004 → devrait être 09/2002-06/2004 (impossible avant fin études)
  - Boonty: dates à vérifier (clarification utilisateur: Qualia Service 06/2004-07/2005, Boonty direct 07/2005-07/2006)
- **Perte de contenu massive**:
  - 12 missions détaillées Upwiser (2013-2021) absentes
  - Boonty et Indépendant sans description
  - 4 certifications manquantes (PSD, Facilitation Graphique, User Stories, Gestion de projet)
  - Engagement communautaire perdu (Lean Startup leader, Agile Tour organisateur, Ruby Bordeaux co-fondateur)
- **Évolutions positives**:
  - Titre modernisé: "Coach Agile" → "Crafting Technology Officer"
  - Expérience PALO IT ajoutée (2021-2025) avec rôle CTO valorisé
  - Technologies actualisées (TypeScript, Rust, Python, IA)

**Recommandations**: 14 total

- 🔴🔴 Très Haute: 2 (dates critiques: Indépendant, Boonty)
- 🔴 Haute: 4 (missions Upwiser majeures: Dekra, iBP, Robin Finance, autres)
- 🟡 Moyenne: 6 (CDiscount, Cast, certifications, engagement communautaire)
- 🟢 Basse: 2 (espagnol commenté, formation Amélioration User Stories)

**Impact potentiel**:

- Score avant corrections: 7.5/10, ATS 65/100, taux conversion 15-20%
- Score après corrections: 9.5/10, ATS 85-90/100, taux conversion 35-45%
- Effort estimé total: 4-6 heures
- Quick wins (très haute priorité): 56 minutes pour impact critique

**Prochaines actions**:

1. Vérifier dates officielles Boonty/Qualia avec documents (contrats de travail, bulletins de salaire)
2. Corriger immédiatement date Indépendant (1999 → 2002)
3. Créer tâches de correction via `/task-from-analysis --analysis-id=CNT-013 --filter=high`
4. Enrichir missions Upwiser prioritaires (Dekra, iBP, Robin Finance)
5. Compléter descriptions manquantes (Boonty, Indépendant, CDiscount, Cast)

---

### CNT-014: Analyse Journal CTO PALO IT

**Objectif**: Analyser les données extraites du journal et de la gestion de tâches de l'expérience CTO chez PALO IT pour enrichir le CV avec des détails concrets

**Sources analysées**:

- Journal CTO PALO IT: `.tasks/resources/sources-analyses/extract-CTO-activities/`
  - `CTO-CV-Highlights-2025.md` - Highlights CV-ready (383 lignes)
  - `CTO-Analysis-March-July-2025.md` - Analyse détaillée de travail (936 lignes)
- CV actuel: `src/cv.typ` lignes 106-118

**Fichiers de ressources**:

- Audits: [resources/audits/CNT-014/](resources/audits/CNT-014/)
  - `palo-it-cto-activities.md` - Extraction structurée des activités CTO (568 lignes)
- Analyses: [resources/analyses/CNT-014/](resources/analyses/CNT-014/)
  - `audit-report.md` - Rapport d'analyse comparative (770 lignes)
  - `recommendations.md` - 25 recommandations détaillées
  - `recommendations-status.md` - Suivi des recommandations

**Résultats clés**:

- **Période couverte**: Mars-juillet 2025 (5 mois de données détaillées)
- **Incohérences critiques identifiées**:
  - Date CTO: CV indique "10/2024 - 08/2025" (~10 mois) vs réalité "11/2021 - 10/2025" (4 ans) - **sous-estimation de 3+ ans**
  - Date fin: 08/2025 vs 10/2025 (2 mois d'écart)
  - Taille équipe: 40+ vs 50 réels
- **Écarts majeurs (absence totale dans le CV)**:
  - Aucun résultat business quantifiable (15% croissance CA disponible)
  - Aucune technologie spécifique mentionnée (Azure, AWS, Scaleway, AI/ML stack complet)
  - Aucun projet client concret (Bodic API 72ms, Systel, TopTex avec feedback "très bien, carré, propre")
  - Aucun partenariat stratégique (Scaleway, GitHub 20-40 certs, Microsoft, Mistral)
  - Aucune métrique performance (72ms API, 6+ presales €15k-€500k+, 20-40 certifications)
- **Accomplissements mesurables disponibles**:
  - Business: 15% croissance CA, 6+ opportunités presales €15k-€500k+
  - Formation: 20-40 certifications GitHub Copilot délivrées
  - Technique: Réduction temps réponse API 72ms, projets 4 clients
  - Innovation: Quantum computing (10 sem), Tech&Toast (70+ pros), Gen-e2 framework complet
  - Management: 50 professionnels, 3 recrutements, coaching quotidien 3j/5

**Recommandations**: 25 total

- 🔴🔴 Très Haute: 5 (dates CTO, croissance CA 15%, stack cloud, stack AI/ML, projets clients)
- 🔴 Haute: 10 (certifications GitHub, presales pipeline, partenariats, Gen-e2 détails, quantum, langages, patterns architecture, clients additionnels, taille équipe, feedback client)
- 🟡 Moyenne: 7 (Tech&Toast, partenariats détails, méthodologies, Hive Tech, Career Advisor)
- 🟢 Basse: 3 (game dev, 360 reviews, outils)

**Impact potentiel**:

- **Priorité globale**: 🔴🔴 TRÈS HAUTE
- **Problème**: La description actuelle (8 bullets génériques, ~150 mots) ne reflète pas l'ampleur et l'impact du rôle CTO
- **Données disponibles**: ~200+ éléments factuels (ratio 1:200 entre CV actuel et données disponibles)
- **Score CV actuel pour CTO**: Insuffisant - absence de technologies, projets concrets et résultats mesurables critiques

**Données extraites par catégorie**:

- **Business**: 15% CA, 6+ presales €15k-€500k+, budgets validés
- **Technologies**: Azure (Databricks, SQL Hyperscale, Cosmos DB), AWS (Bedrock), Scaleway, OpenAI, Anthropic, LangChain, OpenSearch, Pinecone, Kendra, PGVector, GitHub Copilot, Codestral, Python, C#, TypeScript, Rust
- **Projets**: Bodic (API 72ms, Outlook add-in), Systel (30j audit), TopTex (feedback "très bien, carré, propre"), 6+ presales (Natixis, Groupe BZ, CEVA, Cisac, Virtuos, Aviva)
- **Partenariats**: Scaleway (cloud), GitHub (20-40 certs Copilot), Microsoft, Mistral (Codestral)
- **Innovation**: Quantum computing (10 sem), Tech&Toast (70+ pros), Gen-e2 (Learn & Lunch + Hands-on hebdo)
- **Management**: 50 personnes, 3 recrutements, coaching quotidien 3j/5, Career Advisor, 360 reviews
- **Architecture**: MAC, BFF, REST API, multi-cloud, microservices

**Prochaines actions**:

1. **CRITIQUE**: Corriger immédiatement date CTO (11/2021 - 10/2025) - erreur de 3+ ans
2. Créer tâches priorité très haute via `/task-from-analysis --analysis-id=CNT-014 --filter=very-high`
3. Ajouter résultats business quantifiables (15% CA, pipeline presales)
4. Intégrer technologies cloud et AI/ML complètes
5. Ajouter projets clients concrets avec métriques
6. Phase 2: Créer tâches priorité haute (certifications, partenariats, enrichissement Gen-e2)

---

## Références

- [TASKS.md](TASKS.md) - Tableau de bord des tâches
- [TASK_RULES.md](TASK_RULES.md) - Règles de gestion des tâches
- [Commandes Claude](.claude/commands/README.md) - Documentation des commandes
