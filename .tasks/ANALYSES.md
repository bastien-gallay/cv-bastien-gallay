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
| [CNT-001](resources/analyses/CNT-001/) | LinkedIn Audit | [linkedin.com/in/bastiengallay](https://linkedin.com/in/bastiengallay/) | ✅ Terminé | 2025-10-29 | 19 total (1 très haute, 10 hautes, 8 moyennes, 8 basses) | 0/19 |

---

## Analyses Archivées

_Aucune analyse archivée pour le moment._

Les analyses sont archivées lorsque toutes leurs recommandations ont été traitées (converties en tâches et complétées).

---

## Statistiques Globales

- **Total analyses**: 1
- **En cours**: 0
- **Terminées**: 1
- **Recommandations totales**: 19
- **Recommandations pendantes**: 19 (100%)
- **Tâches créées depuis analyses**: 0

### Répartition par priorité

| Priorité | Nombre | Pourcentage |
|----------|--------|-------------|
| 🔴🔴 Très Haute | 1 | 5% |
| 🔴 Haute | 10 | 53% |
| 🟡 Moyenne | 8 | 42% |
| 🟢 Basse | 8 | 42% |

_Note: Le total dépasse 100% car certaines recommandations ont des sous-catégories._

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

## Références

- [TASKS.md](TASKS.md) - Tableau de bord des tâches
- [TASK_RULES.md](TASK_RULES.md) - Règles de gestion des tâches
- [Commandes Claude](.claude/commands/README.md) - Documentation des commandes
