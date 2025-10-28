# INF-001: Intégration MCP pour vérification Claude

---

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | INF-001 |
| **Titre** | Ajouter MCP pour vérification Claude |
| **Statut** | ⏳ À faire |
| **Priorité** | 🟢 Basse |
| **Trigramme** | INF (Infrastructure) |
| **Section CV** | N/A |
| **Créé le** | 2025-10-28 |
| **Cible** | 2025-12-01 |
| **Terminé le** | |
| **Temps estimé** | 4-6 heures |
| **Temps réel** | |

---

## Description

Créer un serveur MCP (Model Context Protocol) permettant à Claude d'analyser et de vérifier automatiquement les améliorations apportées au CV.

### Contexte

Le Model Context Protocol (MCP) permet de créer des outils personnalisés que Claude peut utiliser. Un serveur MCP dédié au CV permettrait à Claude de:
- Lire le contenu du CV
- Vérifier la qualité du contenu
- Proposer des améliorations
- Valider les modifications avant commit

### Objectif

Créer un serveur MCP avec les fonctionnalités suivantes:
- Lecture du CV Typst
- Analyse de la qualité du contenu
- Vérification de la cohérence
- Suggestions d'amélioration
- Validation pré-commit

---

## Sous-tâches

- [ ] Étudier le Model Context Protocol (MCP)
- [ ] Identifier les fonctionnalités utiles pour le CV
- [ ] Créer la structure du serveur MCP
- [ ] Implémenter les outils de lecture du CV
- [ ] Implémenter les outils de vérification
- [ ] Implémenter les outils de suggestion
- [ ] Tester le serveur avec Claude
- [ ] Documenter l'utilisation dans CLAUDE.md
- [ ] Ajouter configuration MCP au projet

---

## Notes pour Claude

> Instructions spécifiques pour l'assistance IA

**MCP - Model Context Protocol:**

Le MCP permet de créer des serveurs d'outils que Claude peut utiliser. Pour ce projet, on pourrait créer:

**Outils MCP à implémenter:**

1. **read_cv** - Lire le contenu du CV Typst
2. **analyze_quality** - Analyser la qualité du contenu
3. **check_consistency** - Vérifier la cohérence (dates, formatage)
4. **suggest_improvements** - Proposer des améliorations
5. **validate_changes** - Valider les modifications

**Structure suggérée:**
```
mcp-server/
├── package.json
├── src/
│   ├── index.ts
│   ├── tools/
│   │   ├── readCv.ts
│   │   ├── analyzeQuality.ts
│   │   ├── checkConsistency.ts
│   │   ├── suggestImprovements.ts
│   │   └── validateChanges.ts
│   └── utils/
│       └── typstParser.ts
└── README.md
```

**Technologies:**
- Node.js / TypeScript
- MCP SDK: `@modelcontextprotocol/sdk`
- Parser Typst (si disponible)

**Configuration Claude Desktop:**
```json
{
  "mcpServers": {
    "cv-helper": {
      "command": "node",
      "args": ["/path/to/mcp-server/dist/index.js"],
      "env": {
        "CV_PATH": "/Users/bastiengallay/Dev/cv/neat-cv"
      }
    }
  }
}
```

**Fichiers à créer:**
- `mcp-server/` (dossier complet)
- `mcp-server/README.md` (documentation)
- Configuration exemple

**Fichiers à modifier:**
- [CLAUDE.md](../CLAUDE.md) - Ajouter documentation MCP

---

## Notes pour l'utilisateur

> Rappels, références, notes personnelles

**Décisions à prendre:**
- Implémenter en TypeScript ou Python?
- Quelles fonctionnalités prioriser?
- Faut-il intégrer avec les scripts de vérification existants ([QUA-001](./QUA-001-verification.md))?
- Héberger le serveur MCP où? (local seulement ou distant?)

**Use cases attendus:**
- "Claude, analyse mon CV et dis-moi ce qui peut être amélioré"
- "Claude, vérifie la cohérence des dates dans mon CV"
- "Claude, suggère des reformulations pour la section expérience"
- "Claude, valide mes changements avant que je commit"

**Avantages:**
- Feedback IA contextuel et spécialisé
- Automatisation de la revue de CV
- Intégration native avec Claude Code
- Évolutif (ajout de nouvelles fonctionnalités)

**Limitations:**
- Nécessite Claude Desktop (ou API)
- Configuration locale requise
- Maintenance du serveur MCP

**Après implémentation:**
- Configurer dans Claude Desktop
- Tester toutes les fonctionnalités
- Documenter les use cases
- Partager avec la communauté?

---

## Références externes

### Fichiers du projet

- [cv.typ](../cv.typ) - CV à analyser
- [CLAUDE.md](../CLAUDE.md) - À compléter avec MCP
- Scripts de vérification (QUA-001)

### Tâches liées

- [QUA-001](./QUA-001-verification.md) - Vérifications (intégration possible)

### Ressources

- Model Context Protocol: https://modelcontextprotocol.io/
- MCP SDK: https://github.com/modelcontextprotocol/sdk
- Claude Desktop MCP: https://docs.claude.com/en/docs/claude-code/mcp
- Exemples MCP: https://github.com/modelcontextprotocol/servers

---

## Commits Git associés

### Commits intermédiaires

```bash
git commit -m "feat(mcp): ✨ add MCP server structure

Created mcp-server/ with basic structure.

Refs INF-001"

git commit -m "feat(mcp): ✨ implement CV analysis tools

Added read_cv, analyze_quality, check_consistency tools.

Refs INF-001"
```

### Commit final

```bash
git commit -m "feat(mcp): ✨ complete MCP server for CV verification

- Created MCP server with CV analysis tools
- Implemented read_cv, analyze_quality, check_consistency
- Implemented suggest_improvements, validate_changes
- Added documentation and configuration examples
- Updated CLAUDE.md with MCP setup instructions
- Tested all tools with Claude

Closes INF-001"
```

**Format suggéré:**
- **Type**: feat (nouvelle fonctionnalité)
- **Scope**: mcp, infrastructure
- **Emoji**: ✨ (feature)

---

## Tests / Vérifications

- [ ] Le serveur MCP démarre sans erreur
- [ ] Claude peut se connecter au serveur
- [ ] L'outil read_cv fonctionne
- [ ] L'outil analyze_quality fonctionne
- [ ] L'outil check_consistency fonctionne
- [ ] L'outil suggest_improvements fonctionne
- [ ] L'outil validate_changes fonctionne
- [ ] La documentation est claire
- [ ] CLAUDE.md est à jour

---

## Historique des modifications

| Date | Action | Détails |
|------|--------|---------|
| 2025-10-28 | Création | Tâche créée dans le cadre de l'initialisation du système de tâches |

---

## Résultat final

[À remplir une fois la tâche terminée]

**Structure finale attendue:**
```
neat-cv/
├── mcp-server/
│   ├── package.json
│   ├── src/
│   │   ├── index.ts
│   │   └── tools/
│   └── README.md
└── CLAUDE.md               # Mis à jour avec instructions MCP
```
