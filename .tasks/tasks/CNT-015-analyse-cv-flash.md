# CNT-015: Analyse CV Flash (slide unique)

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-015 |
| **Titre** | Analyse CV Flash (slide unique) |
| **Statut** | ⏳ À faire |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | General |
| **Créé le** | 2025-11-14 |
| **Cible** | 2025-11-24 |
| **Terminé le** | - |
| **Temps estimé** | 1.5-2 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Analyser le CV Flash (format slide unique) pour identifier les informations condensées et les points clés mis en avant, et comparer avec le CV actuel pour assurer la cohérence.

### Contexte

Le CV Flash est un format ultra-condensé (un slide) qui présente les informations essentielles du parcours professionnel. Ce format impose une sélection rigoureuse des éléments les plus importants : expériences clés, compétences principales, accomplissements majeurs.

L'analyse de ce CV Flash permettra de:

- Vérifier la cohérence avec le CV complet actuel
- Identifier les points forts mis en avant dans la version condensée
- S'assurer que les éléments critiques du CV Flash sont bien présents dans le CV complet
- Valider l'alignement des messages entre les deux versions

Les sources sont disponibles dans `.tasks/resources/sources-analyses/CV-Flash/`.

Cette analyse s'inscrit dans le processus complet: Source → Extraction → Analyse → Recommandations → Tâches → Modifications CV.

### Objectif

Extraire les données du CV Flash, effectuer une analyse comparative avec le CV actuel, et produire des recommandations pour assurer la cohérence et l'alignement des messages clés.

**Résultat attendu:**

- Fichier d'audit structuré dans `audits/CNT-015/`
- Analyse comparative dans `analyses/CNT-015/`
- Recommandations priorisées dans `analyses/CNT-015/recommendations.md`
- Fichier de tracking pour `/task-from-analysis`

---

## Sous-tâches

- [ ] Extraire les données de `.tasks/resources/sources-analyses/CV-Flash/`
- [ ] Identifier les expériences mentionnées dans le CV Flash
- [ ] Identifier les compétences mises en avant
- [ ] Identifier les accomplissements/résultats clés
- [ ] Créer le fichier d'audit `audits/CNT-015/cv-flash.md`
- [ ] Comparer avec le CV actuel (cohérence des messages)
- [ ] Vérifier l'alignement des dates et durées
- [ ] Identifier les incohérences ou manques
- [ ] Créer l'analyse comparative `analyses/CNT-015/audit-report.md`
- [ ] Générer les recommandations avec priorités `analyses/CNT-015/recommendations.md`
- [ ] Créer le fichier de tracking `analyses/CNT-015/recommendations-status.md`
- [ ] Mettre à jour `.tasks/ANALYSES.md`

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Processus d'analyse:**

1. **Extraction des données (utiliser `/analyze-source`):**
   - Lire le CV Flash (slide)
   - Identifier le format et la structure
   - Extraire les expériences listées
   - Extraire les compétences clés
   - Extraire les accomplissements mentionnés
   - Structurer les données selon le template d'extraction
   - Sauvegarder dans `.tasks/resources/audits/CNT-015/cv-flash.md`

2. **Points d'attention spécifiques au CV Flash:**
   - **Sélection:** Quelles expériences ont été choisies pour le format condensé?
   - **Hiérarchisation:** Quel ordre de présentation?
   - **Message clé:** Quel positionnement professionnel est mis en avant?
   - **Accomplissements:** Quels résultats/chiffres sont mis en avant?
   - **Compétences:** Quelles technologies/méthodologies sont prioritaires?

3. **Analyse comparative:**
   - Comparer chaque expérience du CV Flash avec le CV actuel
   - Vérifier la cohérence des dates
   - Vérifier la cohérence des descriptions
   - Identifier les différences de formulation
   - Identifier les informations présentes dans le Flash mais absentes du CV complet
   - Identifier les incohérences (dates, titres, entreprises)

4. **Génération des recommandations:**
   - Utiliser le template `recommendations-template.md`
   - Prioriser les incohérences critiques (🔴🔴 / 🔴)
   - Recommandations d'alignement des messages (🔴 / 🟡)
   - Suggestions d'enrichissement du CV complet (🟡 / 🟢)
   - Créer le fichier de tracking `recommendations-status.md`
   - Format des IDs: `CNT-015-R01`, `CNT-015-R02`, etc.

5. **Mise à jour du dashboard:**
   - Ajouter l'analyse dans `.tasks/ANALYSES.md`
   - Indiquer le nombre de recommandations

**Types de données à chercher:**

- Expériences professionnelles (ordre, sélection)
- Titres de postes (cohérence avec CV actuel)
- Dates et durées (cohérence)
- Compétences techniques clés
- Accomplissements mis en avant
- Formations/certifications mentionnées
- Positionnement professionnel (message global)

**Outils/commandes à utiliser:**

- `/analyze-source --task-id=CNT-015` pour extraction guidée
- `just build` pour vérifier le CV actuel
- Lecture des templates dans `.tasks/resources/templates/`

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) - CV actuel complet
- `.tasks/resources/sources-analyses/CV-Flash/` - Source CV Flash
- `.tasks/resources/templates/audit-template.md` - Template d'analyse
- `.tasks/resources/templates/recommendations-template.md` - Template recommandations

**Fichiers à créer:**

- `.tasks/resources/audits/CNT-015/cv-flash.md` - Extraction structurée
- `.tasks/resources/analyses/CNT-015/audit-report.md` - Analyse comparative
- `.tasks/resources/analyses/CNT-015/recommendations.md` - Recommandations
- `.tasks/resources/analyses/CNT-015/recommendations-status.md` - Tracking
- `.tasks/resources/analyses/CNT-015/metrics.md` - Statistiques

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Utilité de l'analyse CV Flash:**

- Vérifier la cohérence entre versions courte et longue
- S'assurer que les messages clés sont alignés
- Valider les choix de hiérarchisation
- Identifier les incohérences à corriger

**Points d'attention:**

- Le CV Flash est probablement une version synthétique, pas forcément exhaustive
- Les dates doivent être strictement cohérentes
- Les titres de postes doivent être identiques
- Les accomplissements mentionnés doivent être vérifiables

**Après l'analyse:**

- Utiliser `/task-from-analysis --analysis-id=CNT-015` pour créer les tâches
- Filtrer par priorité: `--filter=high` pour les incohérences critiques
- Les tâches créées aideront à aligner les versions du CV

**Lien avec TPL-001:**

Cette analyse sera utile pour la tâche [TPL-001](./TPL-001-cv-versions.md) (Versions courte et longue du CV), car elle fournira des insights sur comment condenser efficacement les informations.

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - CV actuel complet à comparer
- [CNT-001](./CNT-001-linkedin-audit.md) - Audit LinkedIn (méthodologie similaire)
- [CNT-013](./CNT-013-analyse-ancien-cv-2019.md) - Analyse ancien CV (même processus)
- [CNT-014](./CNT-014-analyse-experience-palo-it.md) - Analyse PALO IT (même processus)
- `.tasks/resources/sources-analyses/CV-Flash/` - Source CV Flash

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Audit LinkedIn (exemple d'analyse complète)
- [CNT-013](./CNT-013-analyse-ancien-cv-2019.md) - Analyse ancien CV
- [CNT-014](./CNT-014-analyse-experience-palo-it.md) - Analyse PALO IT
- [TPL-001](./TPL-001-cv-versions.md) - Versions courte et longue (bénéficiera de cette analyse)

### Ressources

- [ANALYSES.md](../ANALYSES.md) - Dashboard des analyses
- [Templates d'analyse](../resources/templates/) - Templates à utiliser
- [Analyse CNT-001 exemple](../resources/analyses/CNT-001/) - Exemple complet

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "docs(audit): 🔍 extract data from CV Flash

Extracting condensed CV data from slide format.

Refs CNT-015"
```

### Commit final

```bash
git commit -m "docs(audit): 📝 complete CV Flash analysis

- Extracted data from CV Flash (slide format)
- Created comparative analysis report
- Generated prioritized recommendations
- Created tracking file for task generation
- Updated ANALYSES.md dashboard

Identified X consistency issues and Y alignment opportunities.

Closes CNT-015"
```

**Format suggéré:**

- **Type**: docs (documentation/analyse)
- **Scope**: audit, analysis
- **Emoji**: 📝 (documentation), 🔍 (investigation)

---

## Tests / Vérifications

- [ ] Fichier `audits/CNT-015/cv-flash.md` créé et structuré
- [ ] Toutes les expériences du CV Flash extraites
- [ ] Compétences clés identifiées
- [ ] Accomplissements listés
- [ ] Fichier `analyses/CNT-015/audit-report.md` complet
- [ ] Comparaison avec CV actuel effectuée
- [ ] Fichier `analyses/CNT-015/recommendations.md` avec priorités
- [ ] Fichier `analyses/CNT-015/recommendations-status.md` au bon format
- [ ] Dashboard `.tasks/ANALYSES.md` mis à jour
- [ ] Cohérence des dates vérifiée
- [ ] Alignement des messages analysé
- [ ] Les IDs de recommandations suivent le format `CNT-015-RXX`
- [ ] Les commits suivent la convention

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-14 | Création | Tâche créée pour analyse CV Flash |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait:**

- [Liste des réalisations]

**Difficultés rencontrées:**

- [Problèmes et solutions]

**Améliorations futures:**

- [Idées pour aller plus loin]
