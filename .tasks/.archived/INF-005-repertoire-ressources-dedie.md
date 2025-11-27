# INF-005: Répertoire dédié aux ressources d'analyse

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-005 |
| **Titre** | Créer un répertoire dédié aux ressources d'analyse hors `.tasks/` |
| **Statut** | ✅ Terminé |
| **Priorité** | 🟡 Moyenne |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-11-25 |
| **Cible** | - |
| **Terminé le** | 2025-11-27 |
| **Temps estimé** | 2-3 heures |
| **Temps réel** | - |
| **Branche nécessaire** | Auto |

---

## Description

Réorganiser la structure des répertoires pour extraire les ressources d'analyse de `.tasks/resources/` vers un répertoire dédié à la racine du projet.

### Contexte

Actuellement, les ressources d'analyse (audits, analyses comparatives, templates) sont stockées dans `.tasks/resources/`. Cette structure pose plusieurs problèmes :

- Mélange entre système de gestion de tâches et données de référence
- Risque d'écriture accidentelle lors de manipulations dans `.tasks/`
- Manque de visibilité pour les ressources importantes
- Difficulté à utiliser comme point d'entrée pour diverses analyses

### Objectif

Créer un répertoire dédié aux ressources avec les caractéristiques suivantes :

- **Protégé** : séparé de l'arborescence de travail pour éviter les modifications accidentelles
- **Repérable** : nom et emplacement clairs à la racine du projet
- **Point d'entrée** : utilisable par défaut par les tâches d'analyse si aucun chemin n'est spécifié
- **Organisé** : structure claire pour différents types de ressources

---

## Sous-tâches

- [x] Analyser la structure actuelle de `.tasks/resources/`
- [x] Définir le nom et l'emplacement du nouveau répertoire → **`resources/`** (validé)
- [x] Concevoir la nouvelle structure de répertoires
- [x] Migrer les ressources existantes vers le nouveau répertoire
- [x] Mettre à jour les références dans les fichiers de tâches
- [x] Mettre à jour CLAUDE.md avec la nouvelle structure
- [x] Configurer le chemin par défaut dans le skill task-management
- [x] Documenter les conventions d'utilisation (resources/README.md)
- [x] Tester les workflows d'analyse avec la nouvelle structure

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**Structure validée :**

```plaintext
resources/                          # Répertoire visible à la racine
├── README.md                       # Documentation du répertoire
├── audits/                         # Extractions de données sources
│   └── {TASK-ID}/                  # Organisé par tâche d'audit
│       ├── linkedin-profile.md
│       ├── github-profile.md
│       └── cv-snapshot.md
├── analyses/                       # Résultats d'analyses comparatives
│   └── {TASK-ID}/
│       ├── audit-report.md
│       ├── recommendations.md
│       └── recommendations-status.md
├── templates/                      # Templates réutilisables
│   ├── audit-template.md
│   ├── recommendations-template.md
│   └── source-extraction-template.md
└── external/                       # Ressources externes (CV de référence, etc.)
```

**Décisions validées :**

1. **Nommage** : `resources/` (visible, explicite) ✅
2. **Migration** : Toutes les ressources existantes seront migrées ✅
3. **Protection** : Simple convention (documentation) ✅

**Intégration à prévoir :**

- Mettre à jour `config/paths.yml` du skill task-management
- Adapter les workflows `/analyze-source` et `/task-from-analysis`

**Fichiers à modifier :**

- [CLAUDE.md](../../CLAUDE.md) - Section "Analysis and Audit System"
- [.tasks/ANALYSES.md](../ANALYSES.md) - Références aux ressources
- [.claude/skills/task-management/config/paths.yml](../../.claude/skills/task-management/config/paths.yml)

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Décisions prises (2025-11-25) :**

- ✅ Nom du répertoire : `resources/` (visible)
- ✅ Migration : toutes les ressources existantes
- ✅ Protection : simple convention (documentation)

**Avantages attendus :**

- Séparation claire entre gestion de tâches et données de référence
- Réduction du risque de modification accidentelle
- Meilleure visibilité pour les ressources importantes
- Point d'entrée unifié pour les analyses

---

## Références externes

### Fichiers du projet

- [.tasks/resources/](../resources/) - Structure actuelle à migrer
- [CLAUDE.md](../../CLAUDE.md) - Documentation à mettre à jour
- [.tasks/ANALYSES.md](../ANALYSES.md) - Dashboard des analyses

### Tâches liées

- [INF-006](./INF-006-extraire-scripts-tests-hors-claude.md) - Réorganisation similaire pour scripts/tests
- Analyses existantes utilisant les ressources actuelles

### Ressources

- Conventions de nommage des répertoires projets

---

## Commits Git associés

### En cours de travail

```bash
git commit -m "refactor(infra): ♻️ create dedicated resources directory

Move analysis resources from .tasks/resources/ to resources/.

Refs INF-005"
```

### Commit final

```bash
git commit -m "refactor(infra): ♻️ reorganize resources directory structure

- Created dedicated resources/ directory at project root
- Migrated audits, analyses, and templates
- Updated CLAUDE.md documentation
- Configured default path in task-management skill

Closes INF-005"
```

**Format suggéré :**

- **Type**: refactor
- **Scope**: infra
- **Emoji**: ♻️ (restructuration)

---

## Tests / Vérifications

- [ ] Le nouveau répertoire existe avec la structure attendue
- [ ] Les ressources existantes sont migrées correctement
- [ ] Les références dans les fichiers sont mises à jour
- [ ] CLAUDE.md reflète la nouvelle structure
- [ ] Les workflows d'analyse fonctionnent avec le nouveau chemin
- [ ] Le skill task-management utilise le bon chemin par défaut

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-11-25 | Création | Tâche créée pour réorganiser les ressources d'analyse |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Ce qui a été fait :**

- [Liste des réalisations]

**Difficultés rencontrées :**

- [Problèmes et solutions]

**Améliorations futures :**

- [Idées pour aller plus loin]
