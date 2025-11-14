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

---

## Analyses Archivées

_Aucune analyse archivée pour le moment._

Les analyses sont archivées lorsque toutes leurs recommandations ont été traitées (converties en tâches et complétées).

---

## Statistiques Globales

- **Total analyses**: 2
- **En cours**: 0
- **Terminées**: 2
- **Recommandations totales**: 33
- **Recommandations pendantes**: 22 (67%)
- **Tâches créées depuis analyses**: 11

### Répartition par priorité

| Priorité | Nombre | Pourcentage |
|----------|--------|-------------|
| 🔴🔴 Très Haute | 3 | 9% |
| 🔴 Haute | 14 | 42% |
| 🟡 Moyenne | 11 | 33% |
| 🟢 Basse | 5 | 15% |

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

## Références

- [TASKS.md](TASKS.md) - Tableau de bord des tâches
- [TASK_RULES.md](TASK_RULES.md) - Règles de gestion des tâches
- [Commandes Claude](.claude/commands/README.md) - Documentation des commandes
