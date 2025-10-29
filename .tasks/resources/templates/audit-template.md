# Audit [SOURCE] - Rapport d'Analyse Comparative

**Analyse:** [TASK-ID]
**Date:** [YYYY-MM-DD]
**Source analysée:** [URL ou description]
**CV source:** [src/cv.typ](../../../src/cv.typ)

---

## Résumé Exécutif

[Paragraphe décrivant l'objectif de l'audit et les principaux résultats]

**Statistiques:**

- ✅ **Éléments déjà présents dans le CV:** [X expériences, Y formations, Z certifications...]
- ⚠️ **Éléments manquants:** [Description des écarts majeurs]
- 🔴 **Incohérences identifiées:** [X écarts de dates, Y descriptions, etc.]
- 📝 **Descriptions à enrichir:** [X postes avec détails supplémentaires]

**Priorité globale:** [🔴 HAUTE / 🟡 MOYENNE / 🟢 BASSE] - [Justification]

---

## 1. [Première Catégorie d'Analyse]

### 1.1 Présents dans les deux

[Tableau comparatif des éléments présents dans la source ET dans le CV]

| Élément | Source | CV | Statut |
|---------|--------|----|----|
| **Item 1** | Description source | ✅ | [Statut/Commentaire] |
| **Item 2** | Description source | ✅ | [Statut/Commentaire] |

### 1.2 Manquants dans le CV

[Tableau des éléments présents dans la source mais ABSENTS du CV]

| # | Élément | Détails Source | Priorité | Raison |
|---|---------|---------------|----------|---------|
| 1 | **Item manquant 1** | Détails | 🔴 HAUTE | Justification |
| 2 | **Item manquant 2** | Détails | 🟡 MOYENNE | Justification |

### 1.3 Incohérences identifiées

[Tableau des éléments présents dans les deux mais avec des différences]

| Élément | Source | CV | Écart | Priorité |
|---------|--------|----|----|----------|
| **Item 1** | Valeur source | Valeur CV | Description écart | 🔴 CRITIQUE |

### 1.4 À enrichir ou préciser

[Tableau des éléments qui mériteraient plus de détails]

| Élément | Détails Source | CV Actuel | Action |
|---------|---------------|-----------|---------|
| **Item 1** | Détails disponibles | État actuel | ✅ / 🔴 / 🟡 / 🟢 |

---

## 2. [Deuxième Catégorie d'Analyse]

[Répéter la même structure que section 1]

---

## [N]. Notes Finales et Points d'Attention

### Points d'attention

1. **[Point d'attention 1]:** [Description et implications]
2. **[Point d'attention 2]:** [Description et implications]
3. **[Point d'attention 3]:** [Description et implications]

### Questions restantes

- [ ] [Question 1]
- [ ] [Question 2]
- [ ] [Question 3]

---

**Prochaine action recommandée:** [Action à entreprendre]

---

## Guide d'Utilisation de ce Template

### Sections à Adapter

1. **Résumé Exécutif:** Synthèse des principaux constats
2. **Catégories d'Analyse:** Adapter selon la source
   - LinkedIn: Expériences, Éducation, Certifications, Langues, Bénévolat, Sites
   - GitHub: Projets, Contributions, Technologies, Bio
   - CV externe: Structure, Contenu, Format
3. **Notes Finales:** Points d'attention spécifiques

### Conventions de Priorité

- 🔴🔴 **Très Haute:** Impact critique sur crédibilité
- 🔴 **Haute:** Impact important, doit être traité rapidement
- 🟡 **Moyenne:** Amélioration souhaitable
- 🟢 **Basse:** Optionnel, peut être différé

### Workflow

1. Copier ce template dans `analyses/[TASK-ID]/audit-report.md`
2. Remplir les sections avec les données comparées
3. Identifier les écarts et incohérences
4. Créer le fichier `recommendations.md` basé sur les écarts
5. Créer le fichier `recommendations-status.md` pour le suivi
6. Créer les fichiers `action-plan.md` et `metrics.md`
