# CNT-024: Analyse CV Flash 2025

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | CNT-024 |
| **Titre** | Analyse CV Flash 2025 |
| **Statut** | ✅ Terminé |
| **Priorité** | 🔴 Haute |
| **Trigramme** | CNT |
| **Section CV** | General |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | 2025-11-25 |
| **Temps estimé** | 2 heures |
| **Temps réel** | 2h |
| **Branche nécessaire** | Non |

---

## Description

Analyser le CV Flash 2025 (format slide unique) pour identifier les informations à intégrer ou vérifier dans le CV Typst principal.

### Contexte

Un CV Flash 2025 a été fourni dans `.tasks/resources/sources-analyses/CV-Flash-2025/`. Ce CV condensé sur une seule slide présente une vision synthétique du parcours professionnel avec:

- En-tête: Coach Agile / CTO / Software Craftsman | +20 ans d'expérience
- Expériences clés: Beta.gouv, Nalo, SeLoger.com, Coach et formateur
- Expertise & Technology: Coaching Agile, Software Craftsmanship, langages (TypeScript, Java, Python, etc.)
- Certifications & Talks: SAFe SPC, PSM/PSPO/PSD/PSP/PSK, CSM, Lean Startup Bordeaux

### Objectif

1. Extraire et documenter toutes les informations du CV Flash 2025
2. Comparer avec le CV Typst actuel
3. Identifier les écarts et informations manquantes
4. Générer des recommandations d'amélioration

---

## Sous-tâches

- [x] Extraire les informations du CV Flash 2025 (image PNG et PDF)
- [x] Créer le fichier d'extraction structuré dans `resources/audits/CNT-024/`
- [x] Comparer avec le CV Typst actuel (`src/cv.typ`)
- [x] Documenter les écarts identifiés
- [x] Créer les recommandations avec priorités
- [x] Mettre à jour le dashboard des analyses (ANALYSES.md)

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

L'analyse doit comparer les éléments suivants entre le CV Flash et le CV Typst:

- Titre/positionnement professionnel
- Expériences mentionnées et leur description
- Stack technique et compétences
- Certifications listées
- Éléments de différenciation ou formulations intéressantes

**Fichiers à consulter:**

- [CV Flash 2025 PNG](../resources/sources-analyses/CV-Flash-2025/Extrait-CV-flash-2025.png)
- [CV Flash 2025 PDF](../resources/sources-analyses/CV-Flash-2025/CV-Flash-Extrait-2025-Teragone%20-%20Accompagnement%20audit%20-%20Berger%20Levrault%20Kick%20-%20Off.pdf)
- [cv.typ](../../src/cv.typ) - CV Typst actuel
- [ANALYSES.md](../ANALYSES.md) - Dashboard des analyses

---

## Notes pour l'utilisateur

- Le CV Flash 2025 est un format condensé destiné aux présentations rapides
- Certaines informations peuvent être plus récentes ou formulées différemment
- L'expérience Beta.gouv (MonEspaceNis2) est mentionnée comme "Lead developer"

---

## Références externes

### Fichiers du projet

- [cv.typ](../../src/cv.typ) - CV Typst principal
- [CNT-015](./CNT-015-analyse-cv-flash.md) - Analyse précédente du CV Flash (slide unique)

### Ressources sources

- [Extrait-CV-flash-2025.png](../resources/sources-analyses/CV-Flash-2025/Extrait-CV-flash-2025.png)
- [CV-Flash-Extrait-2025-Teragone.pdf](../resources/sources-analyses/CV-Flash-2025/CV-Flash-Extrait-2025-Teragone%20-%20Accompagnement%20audit%20-%20Berger%20Levrault%20Kick%20-%20Off.pdf)

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "chore(tasks): 📝 add CNT-024 CV Flash 2025 analysis task

Refs CNT-024"
```

### Commit final

```bash
git commit -m "chore(tasks): ✅ complete CNT-024 CV Flash 2025 analysis

- Extracted all information from CV Flash 2025
- Documented gaps with current CV
- Created prioritized recommendations

Closes CNT-024"
```

---

## Tests / Vérifications

- [x] Extraction complète des informations du CV Flash
- [x] Fichier d'audit créé dans `resources/audits/CNT-024/`
- [x] Analyse comparative documentée
- [x] Recommandations créées avec priorités
- [x] Dashboard ANALYSES.md mis à jour

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée |
| 2025-11-25 | En cours | Début du travail |
| 2025-11-25 | Terminé | Analyse complète, recommandations mappées vers tâches |

---

## Résultat final

**Ce qui a été fait:**

- Extraction complète du CV Flash 2025 (PNG et PDF)
- Analyse comparative avec le CV Typst actuel
- 8 recommandations générées avec priorités
- Mapping vers 4 tâches existantes/nouvelles

**Recommandations traitées:**

| ID | Recommandation | Résolution |
|----|----------------|------------|
| R01 | Beta.gouv | ✅ CNT-030 (terminé) |
| R02 | Nalo | ✅ CNT-030 (terminé) |
| R03 | SeLoger.com | → CNT-027 |
| R04 | Activités communautaires | → CNT-028 |
| R05 | Certification PSPO | ❌ Rejeté (non détenue) |
| R06 | Stack technique | → CNT-029 |
| R07 | Wanteeed | → CNT-027 |
| R08 | Citation | → CNT-029 |

**Tâches créées/enrichies:** CNT-027, CNT-028, CNT-029, CNT-030
