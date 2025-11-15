# TPL-002: Système de changement de template

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | TPL-002 |
| **Titre** | Permettre de changer le template Typst |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | TPL (Template) |
| **Section CV** | General |
| **Créé le** | 2025-10-28 |
| **Cible** | 2025-11-15 |
| **Terminé le** | |
| **Temps estimé** | 5-7 heures |
| **Temps réel** | |
| **Branche nécessaire** | Oui |

---

## Description

Créer un système permettant de changer facilement le template Typst utilisé pour le CV, au lieu d'être dépendant uniquement de `neat-cv`.

### Contexte

Le CV utilise actuellement le template `neat-cv` (version 0.4.0). Pour plus de flexibilité, il serait utile de pouvoir:

- Tester différents templates disponibles sur Typst Universe
- Créer des variantes visuelles du même CV
- Faciliter la migration vers d'autres templates si nécessaire

### Objectif

Mettre en place une architecture modulaire permettant:

- De séparer le contenu du CV de sa mise en forme
- De définir plusieurs templates disponibles
- De générer le CV avec différents templates facilement
- De documenter les templates disponibles et comment en ajouter

---

## Sous-tâches

- [ ] Rechercher les templates CV disponibles sur Typst Universe
- [ ] Analyser l'architecture actuelle et identifier ce qui est spécifique à neat-cv
- [ ] Concevoir une architecture modulaire (contenu vs présentation)
- [ ] Créer un fichier de contenu réutilisable `cv-content.typ`
- [ ] Créer des adaptateurs pour différents templates
- [ ] Tester avec au moins 2 templates différents (neat-cv + 1 autre)
- [ ] Créer un script de build multi-templates
- [ ] Documenter le système dans `TEMPLATES.md`
- [ ] Mettre à jour [CLAUDE.md](../../CLAUDE.md)

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Approche recommandée:**

1. **Recherche de templates Typst:**
   - Explorer Typst Universe: <https://typst.app/universe/search/?kind=templates&category=cv>
   - Identifier 2-3 templates populaires compatibles
   - Documenter leurs caractéristiques et API

2. **Architecture modulaire:**

   ```plaintext
   cv-content.typ          # Contenu pur (données)
   templates/
     ├── neat-cv.typ       # Adapter pour neat-cv
     ├── modern-cv.typ     # Adapter pour un autre template
     └── classic-cv.typ    # Adapter pour un 3ème template
   cv.typ                  # Fichier principal (sélection template)
   ```

3. **Séparation contenu/présentation:**
   - Définir une structure de données standard
   - Chaque template consomme cette structure
   - Le fichier principal choisit quel template utiliser

**Exemple de structure de données:**

```typst
#let cv-data = (
  personal: (
    name: "Bastien Gallay",
    title: "Chief Technology Officer",
    email: "...",
    // ...
  ),
  experience: (
    (
      title: "CTO",
      company: "PALO IT",
      period: "2022 - Présent",
      description: "...",
    ),
    // ...
  ),
  // ...
)
```

**Fichiers à créer:**

- `cv-content.typ` (données structurées)
- `templates/neat-cv.typ` (adapter)
- `templates/[autre-template].typ`
- `TEMPLATES.md` (documentation)
- `scripts/build-templates.sh` (build multi-templates)

**Fichiers à modifier:**

- [cv.typ](../../src/cv.typ) - Refactoriser pour utiliser l'architecture modulaire
- [CLAUDE.md](../../CLAUDE.md) - Ajouter documentation sur les templates

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Décisions à prendre:**

- Quels templates alternatifs tester?
- Quel niveau de compatibilité maintenir?
- Faut-il pouvoir générer tous les templates en une commande?
- Quel template utiliser par défaut?

**Critères de sélection des templates:**

- Maintenance active (mises à jour récentes)
- Documentation claire
- Flexibilité de personnalisation
- Esthétique professionnelle
- Support des langues (français)

**Avantages attendus:**

- Flexibilité visuelle sans réécrire le contenu
- Facilite les tests A/B de différents styles
- Protection contre l'obsolescence d'un template spécifique
- Possibilité d'adapter le style selon le destinataire

**Après implémentation:**

- Tester chaque template visuellement
- Demander des retours sur les différents styles
- Choisir un template par défaut
- Documenter comment ajouter un nouveau template

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - CV actuel à refactoriser
- [CLAUDE.md:27-29](../../CLAUDE.md#L27-L29) - Section sur neat-cv template

### Tâches liées

- [TPL-001](./TPL-001-cv-versions.md) - Versions du CV (architecture similaire)
- [QUA-001](./QUA-001-verification.md) - Vérification (doit fonctionner avec tous les templates)

### Ressources

- Typst Universe - CV Templates: <https://typst.app/universe/search/?kind=templates&category=cv>
- neat-cv documentation: <https://typst.app/universe/package/neat-cv>
- Documentation Typst sur les packages: <https://typst.app/docs/reference/scripting/package/>

**Templates à explorer:**

- neat-cv: <https://typst.app/universe/package/neat-cv> (actuel)
- modern-cv: <https://typst.app/universe/package/modern-cv>
- brilliant-cv: <https://typst.app/universe/package/brilliant-cv>
- classic-cv (à identifier)

---

## Commits Git associés

### Commits intermédiaires

```bash
git commit -m "refactor(template): ♻️ extract CV content to separate file

Created cv-content.typ with structured data.

Refs TPL-002"

git commit -m "feat(template): ✨ add template adapter system

Created templates/ directory with neat-cv adapter.

Refs TPL-002"

git commit -m "feat(template): ✨ add alternative template support

Added modern-cv template option.

Refs TPL-002"
```

### Commit final

```bash
git commit -m "feat(template): ✨ complete multi-template system

- Extracted content to cv-content.typ
- Created template adapter architecture
- Added support for neat-cv and modern-cv
- Created build script for multi-template generation
- Added TEMPLATES.md documentation
- Updated CLAUDE.md with template system

Closes TPL-002"
```

**Format suggéré:**

- **Type**: feat (nouvelle fonctionnalité) ou refactor (restructuration)
- **Scope**: template
- **Emoji**: ✨ (feature) ou ♻️ (refactor)

---

## Tests / Vérifications

- [ ] cv-content.typ contient toutes les données du CV
- [ ] neat-cv template fonctionne avec la nouvelle architecture
- [ ] Au moins 1 template alternatif fonctionne
- [ ] Les PDFs générés sont identiques à l'original (neat-cv)
- [ ] Le script de build multi-templates fonctionne
- [ ] TEMPLATES.md est clair et complet
- [ ] CLAUDE.md est à jour
- [ ] Tous les templates compilent sans erreur

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-28 | Création | Tâche créée dans le cadre de l'initialisation du système de tâches |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Structure finale attendue:**

```plaintext
neat-cv/
├── cv-content.typ              # Contenu structuré
├── cv.typ                      # Fichier principal (sélection template)
├── templates/
│   ├── neat-cv.typ            # Adapter neat-cv
│   ├── modern-cv.typ          # Adapter moderne
│   └── ...                    # Autres templates
├── scripts/
│   └── build-templates.sh     # Build tous les templates
├── TEMPLATES.md               # Documentation templates
└── output/
    ├── cv-neat.pdf           # Généré avec neat-cv
    ├── cv-modern.pdf         # Généré avec modern-cv
    └── ...
```
