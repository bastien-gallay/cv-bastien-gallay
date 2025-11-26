# QUA-002: Vérification orthographique et grammaticale

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | QUA-002 |
| **Titre** | Vérification orthographique et grammaticale |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | QUA |
| **Section CV** | General |
| **Créé le** | 2025-11-26 |
| **Cible** | - |
| **Terminé le** | - |
| **Temps estimé** | 3 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Oui |

---

## Description

Ajouter un outil de vérification orthographique et grammaticale au système de vérification du CV, intégré au module Python existant dans `scripts/verification/`.

### Contexte

Le système de vérification actuel (`scripts/verification/`) comprend:

- `build.py` - Vérification de la compilation Typst
- `dates.py` - Vérification de la cohérence des dates
- `format.py` - Vérification de la structure et du formatage

Il manque une vérification automatisée de l'orthographe et de la grammaire, qui est actuellement dans la checklist manuelle de [VERIFICATION.md](../../VERIFICATION.md).

### Objectif

Implémenter un module `spelling.py` dans `scripts/verification/` qui:

1. Extrait le texte du CV depuis le fichier source Typst
2. Effectue une vérification orthographique et grammaticale en français
3. Retourne un rapport des erreurs détectées avec suggestions de correction
4. S'intègre au runner existant (`just verify`)

---

## Sous-tâches

- [ ] Rechercher et évaluer les outils de vérification disponibles
- [ ] Choisir l'approche (outil externe CLI ou capacités LLM via Claude)
- [ ] Implémenter le module `scripts/verification/spelling.py`
- [ ] Ajouter les tests unitaires dans `scripts/verification/tests/`
- [ ] Intégrer au runner et au justfile (`just verify-spelling`)
- [ ] Mettre à jour VERIFICATION.md avec le nouveau check automatisé
- [ ] Documenter dans CLAUDE.md

---

## Notes pour Claude

### Approches possibles

**Option A - Outil externe (recommandé pour l'automatisation):**

- **LanguageTool** - Serveur Java, API REST, excellent pour le français
  - `languagetool-org/languagetool` ou via API en ligne
  - Avantage: Indépendant, fonctionne offline
- **Hunspell** via `enchant` ou `pyspellchecker`
  - Avantage: Simple, léger, dictionnaires français disponibles
  - Inconvénient: Orthographe uniquement, pas de grammaire
- **Grammalecte** - Spécialisé français, extension possible via CLI
  - Avantage: Excellent pour le français technique

**Option B - Capacités LLM (Claude):**

- Analyse du texte par Claude pour détecter les erreurs
- Avantage: Compréhension contextuelle supérieure
- Inconvénient: Nécessite une session Claude, non automatisable dans CI

**Recommandation:** Option A avec LanguageTool pour l'automatisation, avec possibilité d'enrichir via Claude pour les cas complexes.

### Structure du module

```python
# scripts/verification/spelling.py
from .shared import Result, Success, Failure

def check_spelling(cv_path: str) -> Result:
    """Vérifie l'orthographe et la grammaire du CV."""
    pass

def extract_text_from_typst(cv_path: str) -> str:
    """Extrait le texte brut du fichier Typst."""
    pass
```

### Commandes à utiliser

```bash
# Compiler et extraire le texte (méthode simple)
typst query src/cv.typ "<text>" --format json

# Ou analyser directement le fichier .typ (extraction regex)
```

### Fichiers à consulter

- [build.py](../../scripts/verification/build.py) - Pattern Railway existant
- [shared.py](../../scripts/verification/shared.py) - Types partagés
- [runner.py](../../scripts/verification/runner.py) - Intégration des checks
- [justfile](../../justfile) - Commandes de build

---

## Notes pour l'utilisateur

### Outils à évaluer

1. **LanguageTool** (Java/API)
   - [languagetool.org](https://languagetool.org/)
   - Package Python: `language-tool-python`

2. **Grammalecte** (Python natif)
   - [grammalecte.net](https://grammalecte.net/)
   - Excellent support du français technique

3. **pyspellchecker**
   - Simple, léger, orthographe uniquement
   - `pip install pyspellchecker`

### Décision à prendre

- Quel outil privilégier ?
- Faut-il un serveur local (LanguageTool) ou une lib pure Python ?
- Niveau de tolérance aux faux positifs (termes techniques, acronymes) ?

---

## Références externes

### Fichiers du projet

- [scripts/verification/](../../scripts/verification/) - Module de vérification
- [VERIFICATION.md](../../VERIFICATION.md) - Checklist manuelle
- [justfile](../../justfile) - Commandes de build

### Tâches liées

- [QUA-001](./QUA-001-verification.md) - Système de vérification (terminé)

### Ressources

- [LanguageTool Python](https://pypi.org/project/language-tool-python/)
- [Grammalecte](https://grammalecte.net/)
- [pyspellchecker](https://pypi.org/project/pyspellchecker/)

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "feat(quality): ✨ add spelling verification module

Refs QUA-002"
```

### Commit final

```bash
git commit -m "feat(quality): ✨ add spelling and grammar verification

- Implement spelling.py with LanguageTool/Grammalecte
- Add unit tests for spelling verification
- Integrate with just verify command
- Update VERIFICATION.md

Closes QUA-002"
```

---

## Tests / Vérifications

- [ ] Le module s'exécute sans erreur
- [ ] Les tests unitaires passent (`just test-verify`)
- [ ] La commande `just verify-spelling` fonctionne
- [ ] Le runner intègre le nouveau check
- [ ] Les termes techniques français sont gérés (faux positifs minimisés)
- [ ] La documentation est à jour

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-26 | Création | Tâche créée |

---

## Résultat final

[À remplir une fois la tâche terminée]
