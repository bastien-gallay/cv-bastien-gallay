# PIP-001: CI/CD pour publication automatique du CV

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | PIP-001 |
| **Titre** | Créer chaîne CI/CD pour publication automatique |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | PIP (Pipeline) |
| **Section CV** | N/A |
| **Créé le** | 2025-10-28 |
| **Cible** | 2025-11-20 |
| **Terminé le** | |
| **Temps estimé** | 6-8 heures |
| **Temps réel** | |
| **Branche nécessaire** | Oui |

---

## Description

Mettre en place une chaîne CI/CD automatisant la compilation du CV et sa publication en ligne à chaque modification.

### Contexte

Actuellement, le CV doit être compilé manuellement avec `typst compile cv.typ`. Pour plus d'efficacité et pour garantir que la version publiée est toujours à jour, il serait utile d'automatiser:

- La compilation du CV à chaque commit
- La vérification qualité automatique
- La publication du PDF en ligne (GitHub Pages, Netlify, etc.)
- La génération de toutes les variantes (courte/longue, différents templates)

### Objectif

Créer une pipeline CI/CD complète permettant:

- Build automatique sur chaque push
- Exécution des tests de vérification ([QUA-001](./QUA-001-verification.md))
- Génération de tous les PDFs (versions, templates)
- Publication automatique sur une URL publique
- Notifications en cas d'erreur

---

## Sous-tâches

- [ ] Choisir la plateforme CI/CD (GitHub Actions recommandé)
- [ ] Créer workflow de build (`.github/workflows/build-cv.yml`)
- [ ] Installer Typst dans l'environnement CI
- [ ] Compiler toutes les versions du CV
- [ ] Intégrer les vérifications qualité (QUA-001)
- [ ] Choisir la plateforme d'hébergement (GitHub Pages / Netlify / Cloudflare Pages)
- [ ] Configurer le déploiement automatique
- [ ] Ajouter badge de build status dans README
- [ ] Tester le workflow complet
- [ ] Documenter le processus dans CLAUDE.md

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Plateforme recommandée: GitHub Actions**

Avantages:

- Intégration native avec GitHub
- Gratuit pour repos publics
- Actions Typst disponibles dans le marketplace

**Actions GitHub à créer:**

1. **`.github/workflows/build-cv.yml`** - Build principal
2. **`.github/workflows/deploy.yml`** - Déploiement

**Hébergement recommandé: GitHub Pages**

- URL: `https://bastiengallay.github.io/neat-cv/cv.pdf`

**Fichiers à créer:**

- `.github/workflows/build-cv.yml`
- `.github/workflows/deploy.yml`

**Fichiers à modifier:**

- [CLAUDE.md](../../CLAUDE.md) - Ajouter section CI/CD

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Décisions à prendre:**

- Plateforme CI/CD: GitHub Actions? GitLab CI? Circle CI?
- Plateforme d'hébergement: GitHub Pages? Netlify? Autre?
- Faut-il un domaine personnalisé (cv.bastiengallay.com)?
- Quelles versions publier automatiquement?
- Faut-il protéger certaines informations dans la version publique?

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - CV à compiler
- [CLAUDE.md](../../CLAUDE.md) - À compléter avec CI/CD

### Tâches liées

- [QUA-001](./QUA-001-verification.md) - Vérifications (à intégrer dans CI)
- [TPL-001](./TPL-001-cv-versions.md) - Versions du CV (toutes à compiler)
- [TPL-002](./TPL-002-template-system.md) - Templates (tous à compiler)

### Ressources

- GitHub Actions: <https://docs.github.com/en/actions>
- setup-typst action: <https://github.com/typst-community/setup-typst>
- GitHub Pages: <https://docs.github.com/en/pages>

---

## Commits Git associés

### Commit final

```bash
git commit -m "feat(cicd): ✨ complete CI/CD pipeline for CV publication

- Added GitHub Actions build workflow
- Added automatic deployment to GitHub Pages
- Integrated quality verifications in CI
- Updated CLAUDE.md with CI/CD documentation

Closes PIP-001"
```

---

## Tests / Vérifications

- [ ] Le workflow GitHub Actions s'exécute sans erreur
- [ ] Le CV est correctement compilé dans l'environnement CI
- [ ] Le PDF est correctement déployé sur l'hébergeur
- [ ] L'URL publique fonctionne et affiche le bon PDF
- [ ] CLAUDE.md est à jour

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-28 | Création | Tâche créée dans le cadre de l'initialisation du système de tâches |

---

## Résultat final

[À remplir une fois la tâche terminée]
