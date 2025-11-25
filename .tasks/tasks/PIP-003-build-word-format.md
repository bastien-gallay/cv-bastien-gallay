# PIP-003: Build du CV au format Word

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | PIP-003 |
| **Titre** | Pouvoir build le CV au format Word (.docx) |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | PIP (Pipeline) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 2-4 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Ajouter la possibilité de générer le CV au format Microsoft Word (.docx) en plus du format PDF.

### Contexte

Certains recruteurs ou plateformes de candidature demandent explicitement un CV au format Word :

- Parsing automatique par les ATS (Applicant Tracking Systems)
- Modification par les agences de recrutement
- Compatibilité avec certains systèmes internes

Actuellement, seul le format PDF est généré.

### Objectif

- Ajouter une commande de build pour générer un fichier `.docx`
- Préserver au maximum la mise en page et le formatage
- Intégrer au workflow existant (`just build-word` ou équivalent)

---

## Sous-tâches

- [ ] Rechercher les options de conversion Typst → Word
- [ ] Évaluer les outils disponibles (pandoc, typst-to-docx, etc.)
- [ ] Tester la conversion avec le CV actuel
- [ ] Évaluer la qualité du rendu Word
- [ ] Créer la commande de build (`just build-word`)
- [ ] Documenter les limitations éventuelles
- [ ] Mettre à jour CLAUDE.md avec la nouvelle commande
- [ ] (Optionnel) Ajouter au workflow CI/CD

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Options de conversion à explorer :**

1. **Typst → PDF → Word**
   - Utiliser un convertisseur PDF vers DOCX
   - Outils : `pdf2docx`, LibreOffice en ligne de commande
   - Avantage : Simple
   - Inconvénient : Perte potentielle de formatage

2. **Typst → HTML → Word**
   - Exporter en HTML puis convertir avec Pandoc
   - Commande : `pandoc input.html -o output.docx`
   - Avantage : Meilleure structure sémantique
   - Inconvénient : Typst n'exporte pas nativement en HTML

3. **Typst → Markdown → Word**
   - Extraire le contenu en Markdown
   - Convertir avec Pandoc : `pandoc cv.md -o cv.docx`
   - Avantage : Contrôle sur la structure
   - Inconvénient : Perte de mise en page complexe

4. **PDF → DOCX direct**
   - `pdf2docx` : `pdf2docx convert cv.pdf cv.docx`
   - LibreOffice : `soffice --convert-to docx cv.pdf`
   - Avantage : Préserve le visuel
   - Inconvénient : Qualité variable

**Approche recommandée :**

Commencer par PDF → DOCX avec `pdf2docx` ou LibreOffice, évaluer la qualité, puis ajuster si nécessaire.

**Commandes à créer dans justfile :**

```makefile
# Build Word format
build-word:
    just build
    pdf2docx convert dist/cv.pdf dist/cv.docx
```

**Installation des dépendances :**

```bash
# Option pdf2docx (Python)
uv pip install pdf2docx

# Option LibreOffice
brew install --cask libreoffice  # macOS
```

**Fichiers à modifier :**

- [justfile](../../justfile) - Ajouter commande build-word
- [CLAUDE.md](../../CLAUDE.md) - Documenter la nouvelle commande

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Limitations attendues :**

- La conversion PDF → Word n'est jamais parfaite
- Les mises en page complexes (colonnes, sidebar) peuvent être altérées
- Les polices peuvent ne pas être embarquées
- Le fichier Word sera probablement plus lourd

**Cas d'usage :**

- Candidatures via ATS qui exigent Word
- Agences de recrutement qui modifient les CV
- Plateformes qui ne supportent que Word

**Qualité attendue :**

- Le contenu textuel doit être préservé à 100%
- La structure générale doit être reconnaissable
- Les modifications mineures de mise en page sont acceptables

---

## Références externes

### Fichiers du projet

- [justfile](../../justfile) - Configuration build actuelle
- [dist/cv.pdf](../../dist/cv.pdf) - PDF source pour conversion
- [CLAUDE.md](../../CLAUDE.md) - Documentation à mettre à jour

### Tâches liées

- [PIP-001](./PIP-001-cicd-pipeline.md) - CI/CD (intégration possible)
- [TPL-001](./TPL-001-cv-versions.md) - Versions du CV (toutes à convertir)

### Ressources

- pdf2docx: <https://github.com/dothinking/pdf2docx>
- Pandoc: <https://pandoc.org/>
- LibreOffice CLI: <https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html>

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "feat(build): ✨ add Word format conversion

Add pdf2docx dependency and build-word command.

Refs PIP-003"
```

### Commit final

```bash
git commit -m "feat(build): ✨ add Word format build support

- Added build-word command to justfile
- Integrated pdf2docx for PDF to DOCX conversion
- Updated CLAUDE.md with new command
- Documented limitations

Closes PIP-003"
```

**Format suggéré :**

- **Type**: feat
- **Scope**: build
- **Emoji**: ✨ (nouvelle feature)

---

## Tests / Vérifications

- [ ] La commande `just build-word` fonctionne
- [ ] Le fichier `dist/cv.docx` est généré
- [ ] Le contenu textuel est préservé
- [ ] Le fichier s'ouvre correctement dans Word/LibreOffice
- [ ] La mise en page est acceptable
- [ ] CLAUDE.md est à jour

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée pour ajouter le support Word |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations]

**Outil choisi :**

- [Outil retenu et pourquoi]

**Qualité du rendu :**

- [Évaluation de la conversion]

**Limitations documentées :**

- [Ce qui ne fonctionne pas parfaitement]
