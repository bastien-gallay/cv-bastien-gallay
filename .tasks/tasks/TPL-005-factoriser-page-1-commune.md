# TPL-005: Factoriser page 1 commune entre cv.typ et cv-short.typ

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | TPL-005 |
| **Titre** | Factoriser page 1 commune entre cv.typ et cv-short.typ |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | TPL |
| **Section CV** | General |
| **Créé le** | 2025-11-28 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 2 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Oui |

---

## Description

Factoriser le code de la page 1 (header + sidebar + main content) qui est quasi-identique entre `cv.typ` et `cv-short.typ` afin d'éviter la duplication et faciliter la maintenance.

### Contexte

Suite au réalignement visuel effectué entre les deux versions du CV, la page 1 est désormais très similaire :

**Éléments identiques :**

- Configuration auteur (firstname, lastname, email, etc.)
- Couleurs (accent-color, header-color)
- Photo de profil
- Sidebar complète (Contact, Informations, Leadership, Tech & IA, Méthodologie)
- Structure générale (cv-page-one avec sidebar et main content)

**Différences mineures :**

- `body-font-size` : 10.5pt (cv.typ) vs 11pt (cv-short.typ)
- Section "A propos" : légère variation de texte (mention presales dans cv.typ)
- Date de fin PALO IT : 08/2025 (cv.typ - bonne date) vs 10/2025 (cv-short.typ)
- Niveau de détail des expériences dans le main content

### Objectif

Créer un fichier partagé `cv-page-one-common.typ` (ou similaire) qui contient :

1. La configuration auteur commune
2. La sidebar complète
3. Les expériences de la page 1 avec paramétrage pour le niveau de détail

Les fichiers `cv.typ` et `cv-short.typ` importeront ce module et ne définiront que leurs spécificités.

---

## Sous-tâches

- [ ] Analyser en détail les différences entre les deux fichiers (page 1)
- [ ] Concevoir l'architecture de factorisation (variables, fonctions, fichier séparé)
- [ ] Créer le fichier commun avec les éléments partagés
- [ ] Refactoriser `cv.typ` pour utiliser le module commun
- [ ] Refactoriser `cv-short.typ` pour utiliser le module commun
- [ ] Vérifier que les deux PDFs sont identiques à l'original (page 1)
- [ ] Documenter l'architecture dans CLAUDE.md si nécessaire

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

Approches possibles à évaluer :

1. **Fichier de données partagé** : Extraire les données (auteur, skills, etc.) dans un fichier `.typ` ou `.yml`
2. **Fonctions paramétrables** : Créer des fonctions avec paramètres pour le niveau de détail
3. **Template partiel** : Un fichier qui définit la page 1 entière, appelé par les deux CV

Contraintes :

- Maintenir la flexibilité pour des ajustements spécifiques à chaque version
- Ne pas complexifier inutilement pour quelques différences mineures
- S'assurer que les builds `just build` et `just build-short` continuent de fonctionner

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ)
- [cv-short.typ](../../src/cv-short.typ)
- [neat-cv-local.typ](../../src/neat-cv-local.typ)

---

## Notes pour l'utilisateur

La factorisation permettra :

- Maintenance simplifiée (un seul endroit pour mettre à jour les infos personnelles)
- Cohérence garantie entre les deux versions
- Ajout facilité de nouvelles versions (ex: cv-executive.typ)

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - Version complète (~4 pages)
- [cv-short.typ](../../src/cv-short.typ) - Version courte (1 page)

### Tâches liées

- [TPL-001](./.archived/TPL-001-cv-versions.md) - Création des versions short/long (archivée)
- [LAY-001](./.archived/LAY-001-sidebar-premiere-page-uniquement.md) - Sidebar première page uniquement (archivée)
- [LAY-004](./LAY-004-equilibrer-contenu-premiere-page-cv-long.md) - Équilibrer contenu page 1 (travail fusionné)

### Note importante

> **2025-11-28** : Cette tâche est fusionnée avec LAY-004. La factorisation sera réalisée dans le cadre de LAY-004 pour équilibrer et aligner les deux versions du CV.

---

## Commits Git associés

### Commit final

```bash
git commit -m "refactor(template): ♻️ factorize common page 1 between CV versions

- Create shared page-one module
- Refactor cv.typ to use shared module
- Refactor cv-short.typ to use shared module

Closes TPL-005"
```

---

## Tests / Vérifications

- [ ] Le CV long compile sans erreur (`just build`)
- [ ] Le CV court compile sans erreur (`just build-short`)
- [ ] La page 1 des deux PDFs est visuellement identique à avant
- [ ] Les différences intentionnelles sont préservées
- [ ] `just verify` passe sans erreur

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-28 | Création | Tâche créée suite au réalignement visuel des deux versions |

---

## Résultat final

[À remplir une fois la tâche terminée]