# TPL-001: Créer versions courte et longue du CV

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | TPL-001 |
| **Titre** | Créer versions courte (1 page) et longue (2+ pages) du CV |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | TPL (Template) |
| **Section CV** | General |
| **Créé le** | 2025-10-28 |
| **Cible** | 2025-11-05 |
| **Terminé le** | |
| **Temps estimé** | 4-6 heures |
| **Temps réel** | |
| **Branche nécessaire** | Oui |

---

## Description

Créer deux variantes du CV à partir du fichier actuel:

- **Version courte**: 1 page, synthétique, pour candidatures rapides
- **Version longue**: 2+ pages, détaillée, pour postes seniors ou dossiers complets

### Contexte

Selon les contextes de candidature, il est nécessaire d'avoir:

1. Un CV court (1-2 pages) qui présente l'essentiel de manière percutante
2. Un CV long (3-5 pages) qui détaille davantage les expériences et accomplissements

**État actuel (novembre 2025):** Le CV fait **5 pages** avec:

- Page 1: Infos principales, expérience résumée, formation résumée
- Page 2: Suite sidebar (skills), formation détaillée, certifications, bénévolat
- Pages 3-5: Expérience détaillée par mission

Il faut donc:

- Créer une version courte (1-2 pages) en sélectionnant l'essentiel
- Considérer le CV actuel comme la version longue (à optimiser)

### Objectif

Produire une structure de fichiers permettant de générer facilement les deux versions, avec:

- Réutilisation maximale du contenu commun
- Système de conditionnels ou de fichiers séparés
- Build script pour compiler les deux versions simultanément

---

## Sous-tâches

- [ ] Analyser le contenu actuel de [cv.typ](../../src/cv.typ) (2 pages)
- [ ] Identifier les sections essentielles pour la version courte
- [ ] Concevoir l'architecture (fichiers séparés vs conditionnels)
- [ ] Créer `cv-short.typ` (version 1 page)
- [ ] Créer `cv-long.typ` (version 2+ pages)
- [ ] Optionnel: créer `cv-content.typ` pour le contenu partagé
- [ ] Adapter le build script pour compiler les deux versions
- [ ] Vérifier la mise en page des deux versions
- [ ] Mettre à jour [CLAUDE.md](../../CLAUDE.md) avec les nouvelles commandes
- [ ] Tester la génération des deux PDFs

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Approches possibles:**

### Option 1: Fichiers séparés (recommandé pour début)

```plaintext
cv-short.typ  # Version 1 page
cv-long.typ   # Version 2+ pages
```

- Plus simple à mettre en place
- Maintenance: dupliquer les changements

### Option 2: Conditionnels Typst

```typst
#let version = "short" // ou "long"

#if version == "short" {
  // Contenu court
} else {
  // Contenu détaillé
}
```

- Plus élégant
- Nécessite de comprendre la syntaxe Typst

### Option 3: Modules partagés

```plaintext
cv-content.typ  # Contenu réutilisable
cv-short.typ    # Import + sélection
cv-long.typ     # Import + tout afficher
```

- Meilleur pour maintenance long terme
- Plus complexe

**Recommandation initiale:** Commencer par Option 1 (fichiers séparés)

**Pour la version courte (1 page):**

- Garder: résumé, 2-3 dernières expériences clés, formation principale, compétences essentielles
- Retirer: détails des missions, certifications secondaires, centres d'intérêt détaillés
- Condenser: descriptions plus courtes, moins de bullet points

**Fichiers à consulter:**

- [cv.typ](../../src/cv.typ) - CV actuel (2 pages)
- [CLAUDE.md](../../CLAUDE.md) - À mettre à jour avec nouvelles commandes

**Commandes build à créer:**

```bash
# Compiler les deux versions
typst compile cv-short.typ
typst compile cv-long.typ

# Ou script unifié
./build-all.sh
```

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Décisions à prendre:**

- Quelle approche architecturale privilégier?
- Quelles expériences garder dans la version courte?
- Quel niveau de détail pour chaque version?
- Faut-il un script de build automatique?

**Critères version courte:**

- Maximum 1 page A4
- Focus sur les 3-5 dernières années
- Compétences les plus pertinentes
- Pas de centres d'intérêt détaillés

**Critères version longue:**

- 2-3 pages selon le contenu disponible
- Toutes les expériences pertinentes
- Détails des projets et accomplissements
- Certifications et formations continues

**Après la création:**

- Demander un feedback externe sur les deux versions
- Ajuster selon les retours
- Tester dans différents contextes de candidature

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - CV actuel complet
- [CLAUDE.md:16-24](../../CLAUDE.md#L16-L24) - Section commandes de build

### Tâches liées

- [CNT-001](./CNT-001-linkedin-audit.md) - Audit LinkedIn (peut influencer le contenu)
- [TPL-002](./TPL-002-template-system.md) - Système de templates (architecture similaire)

### Ressources

- Documentation Typst: <https://typst.app/docs/>
- neat-cv template: <https://typst.app/universe/package/neat-cv>

---

## Commits Git associés

### Commits intermédiaires

```bash
git commit -m "feat(versions): ✨ add short CV version (1 page)

Created cv-short.typ with condensed content.

Refs TPL-001"

git commit -m "feat(versions): ✨ add long CV version (2+ pages)

Created cv-long.typ with detailed content.

Refs TPL-001"
```

### Commit final

```bash
git commit -m "feat(versions): ✨ complete short and long CV variants

- Created cv-short.typ (1 page version)
- Created cv-long.typ (2+ pages version)
- Updated build commands in CLAUDE.md
- Added build script for both versions
- Tested PDF generation for both variants

Closes TPL-001"
```

---

## Tests / Vérifications

- [ ] cv-short.typ compile sans erreur
- [ ] cv-long.typ compile sans erreur
- [ ] La version courte fait bien 1 page
- [ ] La version longue fait 2+ pages
- [ ] Le contenu est cohérent entre les deux versions
- [ ] Les deux PDFs s'affichent correctement
- [ ] CLAUDE.md est à jour avec les nouvelles commandes
- [ ] Les noms de fichiers de sortie sont clairs (cv-short.pdf, cv-long.pdf)

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-28 | Création | Tâche créée dans le cadre de l'initialisation du système de tâches |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Structure finale:**

```plaintext
neat-cv/
├── cv-short.typ       # Version 1 page
├── cv-short.pdf       # PDF généré
├── cv-long.typ        # Version 2+ pages
├── cv-long.pdf        # PDF généré
└── cv.typ             # Original (à conserver ou supprimer?)
```
