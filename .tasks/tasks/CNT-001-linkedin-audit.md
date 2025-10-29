# CNT-001: Audit LinkedIn et documentation des éléments manquants

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-001 |
| **Titre** | Audit LinkedIn et documentation des éléments manquants |
| **Statut** | 🔄 En cours |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT (Content) |
| **Section CV** | General |
| **Créé le** | 2025-10-28 |
| **Cible** | 2025-10-30 |
| **Terminé le** | |
| **Temps estimé** | 2 heures |
| **Temps réel** | |

---

## Description

Naviguer sur le profil LinkedIn (<https://www.linkedin.com/in/bastiengallay/>) pour identifier tous les éléments qui auraient pu être oubliés dans le CV actuel et les documenter de manière structurée.

### Contexte

Le CV actuel en Typst a été créé avec des informations de base, mais il se peut que certaines expériences, compétences, certifications, projets ou accomplissements présents sur LinkedIn n'aient pas été inclus. Un audit systématique permettra de s'assurer que le CV est complet et à jour.

### Objectif

Produire un document de référence listant tous les éléments du profil LinkedIn avec:

- Ceux déjà présents dans le CV (avec références aux lignes)
- Ceux manquants à ajouter
- Ceux à mettre à jour ou préciser

---

## Sous-tâches

- [ ] Accéder au profil LinkedIn de Bastien Gallay
- [ ] Extraire toutes les expériences professionnelles
- [ ] Extraire toutes les formations
- [ ] Extraire toutes les compétences (skills)
- [ ] Extraire toutes les certifications
- [ ] Extraire les projets, publications, langues
- [ ] Comparer avec le contenu actuel de [cv.typ](../../src/cv.typ)
- [ ] Documenter les écarts dans un fichier de sortie
- [ ] Créer une liste priorisée des éléments à ajouter

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Action à réaliser:**

1. Utiliser l'outil WebFetch pour accéder à <https://www.linkedin.com/in/bastiengallay/>
2. Extraire tout le contenu du profil (expériences, formation, compétences, certifications, etc.)
3. Lire le fichier [cv.typ](../../src/cv.typ) pour identifier ce qui est déjà présent
4. Créer un document `TASKS/BG-001-linkedin-audit-results.md` avec:
   - Section "Éléments déjà dans le CV" (avec références lignes)
   - Section "Éléments manquants à ajouter"
   - Section "Éléments à mettre à jour/préciser"
   - Recommandations de priorité

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) - Contenu actuel du CV

**Fichier de sortie:**

- `TASKS/CNT-001-linkedin-audit-results.md` (à créer)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Important:**

- Vérifier que toutes les dates sont cohérentes entre LinkedIn et le CV
- Porter une attention particulière aux accomplissements quantifiables
- Identifier les mots-clés importants qui pourraient manquer
- Noter les compétences en demande sur le marché actuel

**Après l'audit:**

- Décider quels éléments ajouter en priorité
- Créer des tâches spécifiques pour chaque mise à jour majeure
- Vérifier la cohérence des descriptions entre LinkedIn et CV

---

## Références externes

### Fichiers du projet

- [cv.typ:103-255](../../src/cv.typ#L103-L255) - Section expériences et formation
- [cv.typ:73-88](../../src/cv.typ#L73-L88) - Section compétences

### Tâches liées

- [TPL-001](./TPL-001-cv-versions.md) - Versions du CV (dépendra des résultats de l'audit)

### Ressources

- Profil LinkedIn: <https://www.linkedin.com/in/bastiengallay/>

---

## Commits Git associés

### Commit final

```bash
git commit -m "docs(audit): 📝 complete LinkedIn profile audit

- Extracted all profile information
- Compared with current CV content
- Documented gaps and recommendations
- Created prioritized action items

Closes CNT-001"
```

---

## Tests / Vérifications

- [ ] Toutes les sections du profil LinkedIn ont été analysées
- [ ] La comparaison avec cv.typ est exhaustive
- [ ] Les recommandations sont priorisées
- [ ] Le fichier de résultats est clair et exploitable

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-28 | Création | Tâche créée dans le cadre de l'initialisation du système de tâches |
| 2025-10-29 | En cours | Début du travail - Option B: LinkedIn data export |

---

## Résultat final

[À remplir une fois la tâche terminée]
