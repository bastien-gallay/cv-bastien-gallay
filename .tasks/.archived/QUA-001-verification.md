# QUA-001: Étapes de vérification du CV

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | QUA-001 |
| **Titre** | Ajouter étapes de vérification du CV |
| **Statut** | ✅ Terminé |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | QUA (Quality) |
| **Section CV** | General |
| **Créé le** | 2025-10-28 |
| **Cible** | 2025-11-10 |
| **Terminé le** | 2025-11-26 |
| **Temps estimé** | 3-4 heures |
| **Temps réel** | |
| **Branche nécessaire** | Auto |

---

## Description

Créer un système de vérification qualité pour le CV afin de s'assurer qu'il respecte les standards attendus avant diffusion.

### Contexte

Un CV doit être exempt d'erreurs (orthographe, grammaire, formatage) et respecter certaines bonnes pratiques (cohérence des dates, clarté des descriptions, etc.). Un processus de vérification systématique permettra d'éviter les erreurs embarrassantes et d'améliorer la qualité globale.

### Objectif

Mettre en place un système de vérification comprenant:

- Une checklist manuelle de vérification
- Des scripts automatiques pour détecter certaines erreurs
- Un guide des bonnes pratiques
- Intégration possible dans le workflow Git (pre-commit hooks)

---

## Sous-tâches

- [x] Créer une checklist de vérification manuelle (VERIFICATION.md)
- [x] Identifier les vérifications automatisables
- [ ] Créer un script de vérification orthographique (si possible avec Typst)
- [x] Créer un script de vérification de cohérence (dates, formatage)
- [x] Créer un script de vérification de compilation (PDF généré sans erreur)
- [x] Documenter le processus de vérification dans CLAUDE.md
- [ ] (Optionnel) Créer un pre-commit hook Git
- [x] Tester l'ensemble du processus de vérification

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Actions à réaliser:**

1. **Créer `VERIFICATION.md`** - Checklist complète de vérification manuelle:
   - Orthographe et grammaire
   - Cohérence des dates (format, ordre chronologique)
   - Cohérence des descriptions (temps verbal, style)
   - Formatage (espacements, alignements, polices)
   - Informations de contact à jour
   - Liens fonctionnels (email, LinkedIn, etc.)
   - Longueur appropriée (1-2 pages selon version)
   - Pas d'informations sensibles ou confidentielles

2. **Créer scripts de vérification** dans un dossier `scripts/`:
   - `verify-build.sh` - Vérifie que la compilation réussit
   - `verify-dates.sh` - Vérifie la cohérence des dates
   - `verify-format.sh` - Vérifie le formatage de base
   - `verify-all.sh` - Lance toutes les vérifications

3. **Documenter dans CLAUDE.md** - Ajouter section sur la vérification qualité

**Outils/commandes à utiliser:**

- `typst compile` pour vérifier la compilation
- Scripts bash pour automatisation
- Expressions régulières pour détection de patterns

**Fichiers à créer:**

- `VERIFICATION.md` (checklist)
- `scripts/verify-build.sh`
- `scripts/verify-dates.sh`
- `scripts/verify-format.sh`
- `scripts/verify-all.sh`

**Fichiers à modifier:**

- [CLAUDE.md](../../CLAUDE.md) - Ajouter section vérification

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Éléments critiques à vérifier:**

- Orthographe des noms d'entreprises et technologies
- Cohérence des dates (format français: MM/YYYY ou YYYY-MM)
- Adresse email et numéro de téléphone à jour
- Lien LinkedIn fonctionnel
- Pas de fautes d'orthographe dans les titres

**Bonnes pratiques:**

- Faire relire par une tierce personne
- Vérifier sur différents lecteurs PDF
- Imprimer pour voir le rendu papier
- Vérifier que le PDF est bien searchable (texte sélectionnable)

**Après implémentation:**

- Exécuter `scripts/verify-all.sh` avant chaque export final
- Passer par la checklist VERIFICATION.md systématiquement
- Considérer automatisation dans CI/CD (voir [PIP-001](./PIP-001-cicd-pipeline.md))

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - CV à vérifier
- [CLAUDE.md](../../CLAUDE.md) - À compléter avec processus de vérification

### Tâches liées

- [PIP-001](./PIP-001-cicd-pipeline.md) - CI/CD (pourra intégrer les vérifications)
- [INF-001](./INF-001-mcp-integration.md) - MCP Claude (vérification assistée par IA)

### Ressources

- Documentation Typst: <https://typst.app/docs/>
- Conventional Commits: <https://www.conventionalcommits.org/>
- Git hooks: <https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks>

---

## Commits Git associés

### Commits intermédiaires

```bash
git commit -m "docs(quality): 📝 add verification checklist

Created VERIFICATION.md with comprehensive quality checks.

Refs QUA-001"

git commit -m "feat(quality): ✨ add verification scripts

- verify-build.sh: check compilation
- verify-dates.sh: check date consistency
- verify-format.sh: check formatting
- verify-all.sh: run all checks

Refs QUA-001"
```

### Commit final

```bash
git commit -m "feat(quality): ✨ complete CV verification system

- Added VERIFICATION.md checklist
- Created automated verification scripts
- Updated CLAUDE.md with verification process
- Tested all verification steps

Closes QUA-001"
```

**Format suggéré:**

- **Type**: feat (nouvelle fonctionnalité de vérification)
- **Scope**: quality
- **Emoji**: ✨ (nouvelle feature) ou 📝 (documentation)

---

## Tests / Vérifications

- [x] VERIFICATION.md est complet et clair
- [x] Tous les scripts s'exécutent sans erreur
- [x] `verify-build.sh` détecte les erreurs de compilation
- [x] `verify-dates.sh` détecte les incohérences de dates
- [x] `verify-all.sh` exécute tous les scripts correctement
- [x] La documentation dans CLAUDE.md est à jour
- [x] Les scripts sont exécutables (chmod +x)

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-28 | Création | Tâche créée dans le cadre de l'initialisation du système de tâches |
| 2025-11-26 | En cours | Début du travail |
| 2025-11-26 | Terminé | Système de vérification complet |
| 2025-11-26 | Refactoring | Railway Programming pattern appliqué (136 tests) |

---

## Résultat final

**Livrables créés:**

- `VERIFICATION.md` - Checklist complète de vérification manuelle (10 sections)
- `scripts/verify-build.sh` - Vérifie la compilation Typst et génération PDF
- `scripts/verify-dates.sh` - Vérifie la cohérence des dates (format, ordre, pas de futur)
- `scripts/verify-format.sh` - Vérifie structure, contacts et formatage
- `scripts/verify-all.sh` - Exécute toutes les vérifications
- `justfile` - Ajout de la commande `just verify`
- `CLAUDE.md` - Section "Quality Verification" documentée

**Structure finale:**

```plaintext
neat-cv/
├── VERIFICATION.md          # Checklist de vérification
├── scripts/
│   ├── verify-build.sh     # Vérification compilation
│   ├── verify-dates.sh     # Vérification dates
│   ├── verify-format.sh    # Vérification formatage
│   └── verify-all.sh       # Lancement de toutes les vérifications
└── CLAUDE.md               # Mis à jour avec processus de vérification
```

**Refactoring Railway Programming (2025-11-26):**

```plaintext
scripts/
├── lib/                          # Bibliothèque partagée
│   ├── __init__.py
│   ├── types.py                  # NewType + TypeGuard
│   ├── result.py                 # Result générique
│   └── context.py                # Context avec bind/map
├── tests/
│   └── test_lib.py               # 22 tests
└── verification/
    ├── build.py                  # BuildContext Railway
    ├── dates.py                  # DatesContext Railway
    ├── format.py                 # FormatContext Railway
    ├── runner.py                 # RunnerContext Railway
    └── tests/
        ├── conftest.py           # Fixtures partagées
        ├── test_build.py         # 20 tests
        ├── test_dates.py         # 26 tests
        ├── test_format.py        # 47 tests
        └── test_runner.py        # 21 tests
```

**Total: 136 tests passant**

**Non implémenté (optionnel):**

- Script de vérification orthographique (nécessiterait outils externes)
- Pre-commit hook Git (peut être ajouté ultérieurement)
