# Task Management Skill

**Version:** 2.0.0
**Status:** Session 1 - In Development

Système unifié de gestion de tâches pour Claude Code, migré depuis les slash commands vers une architecture skill avec progressive disclosure.

---

## Quick Start

### Available Commands

| Command | Description | Status |
|---------|-------------|--------|
| `task-next` | Suggère la prochaine tâche (WSJF) | ✅ Session 1 |
| `task-create` | Créer une nouvelle tâche | 🔄 Session 2 |
| `task-from-idea` | Créer depuis IDEAS.md | 🔄 Session 2 |
| `task-start` | Démarrer une tâche | 🔄 Session 2 |
| `task-complete` | Finaliser une tâche | 🔄 Session 2 |
| `task-validate` | Valider le système | 🔄 Session 2 |
| `task-archive` | Archiver une tâche | ⏳ Session 3 |
| `task-from-analysis` | Créer depuis analyse | ⏳ Session 3 |
| `analyze-source` | Extraire source externe | ⏳ Session 3 |

### Usage Example

```
# Suggest next task to work on
task-next

# Start working on a task
task-start INF-004

# Complete a task
task-complete INF-004
```

---

## Architecture

This skill uses **progressive disclosure** (3 levels) to minimize context usage:

1. **Level 1** (`SKILL.md`): Metadata (~200 tokens, always loaded)
2. **Level 2** (`workflows/*.md`): Workflow instructions (~1-2k tokens, loaded on demand)
3. **Level 3** (external): Implementation scripts and config (loaded as needed or executed)

**Key benefit:** Python scripts execute and return only output, not code (~0 tokens for implementation).

**Note:** Scripts, config, and tests are now located outside `.claude/` for better accessibility:

- Scripts: `scripts/task_management/`
- Config: `config/task_management/`
- Tests: `scripts/task_management/tests/`

See [skill-architecture-design.md](./skill-architecture-design.md) for complete architecture documentation.

---

## Configuration

Configuration uses **YAML data + Python validation**:

- **`config/task_management/priorities.yml`**: Priority levels (emojis, scores, default times)
- **`config/task_management/trigrammes.yml`**: Task categories (CNT, TPL, QUA, PIP, LAY, DOC, INF)
- **`config/task_management/paths.yml`**: File paths (`.tasks/`, templates, etc.)

Configs are loaded once and cached in memory via `scripts/task_management/core/config_loader.py`.

---

## Development

### Running Tests

```bash
# Unit tests (pytest)
uv run --with pyyaml pytest scripts/task_management/tests/

# Manual tests
# See scripts/task_management/tests/MANUAL_TESTS.md for scenarios
```

### Project Structure

```text
# Skill definition (in .claude/)
.claude/skills/task-management/
├── SKILL.md                    # Entry point
├── README.md                   # This file
├── skill-architecture-design.md # Architecture docs
├── workflows/                  # Markdown workflows
└── templates/                  # Templates

# Implementation (at project root)
scripts/task_management/
├── core/                       # Core utilities
├── algorithms/                 # Algorithmic logic (WSJF)
├── validators/                 # DoR/DoD validation
├── analysis/                   # Analysis-specific
└── tests/                      # Unit tests

config/task_management/
├── priorities.yml              # Priority scoring
├── trigrammes.yml              # Task categories
└── paths.yml                   # File paths
```

---

## Migration Status

**Session 1** (Current): Foundation + Proof of Concept
- ✅ Architecture design
- 🔄 Config system (YAML + Python)
- 🔄 `/task-next` migration
- ⏳ Test patterns

**Session 2** (Planned): Core Infrastructure
- Core utilities (file_parser, id_generator, dashboard_updater)
- Validators (DoR, DoD, system)
- `/task-validate` migration

**Session 3** (Planned): Complex Commands
- Lifecycle commands (create, start, complete)
- Analysis commands (from-analysis)

**Session 4** (Planned): Cleanup
- Remaining commands
- Documentation update
- **Remove old slash commands**

---

## Links

- **Task:** [INF-004](../../.tasks/tasks/INF-004-migrer-systeme-gestion-taches-vers-skill-claude-unifie.md)
- **Design Doc:** [skill-architecture-design.md](./skill-architecture-design.md)
- **Old Commands:** `.claude/commands/task-*.md` (will be removed in Session 4)

---

**Generated:** 2025-11-16
**Last Updated:** Session 1
