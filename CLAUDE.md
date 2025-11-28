# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CV (curriculum vitae) project written in Typst, a modern markup-based typesetting system. The CV uses the `neat-cv` template (version 0.4.0) to generate a professional two-page resume in French.

## Key Commands

### Building the CV

```bash
# Compile the full CV to PDF
just build

# Compile the short CV (1 page)
just build-short

# Compile all versions (full + short)
just build-all

# Watch mode - automatically recompile on changes
just watch
```

### Viewing the Output

The compiled PDFs are saved in `dist/`:

- `dist/cv.pdf` - Full version (~4 pages, exhaustive)
- `dist/cv-short.pdf` - Short version (1 page, for quick applications)

## Project Structure

```text
neat-cv/
├── CLAUDE.md                  # This file - project instructions
├── VERIFICATION.md            # Quality verification checklist
├── .tasks/                    # Task management system
│   ├── tasks/                 # Individual task files
│   ├── .archived/             # Archived completed tasks
│   ├── ANALYSES.md            # Analysis dashboard
│   ├── IDEAS.md               # Ideas backlog
│   ├── TASKS.md               # Tasks dashboard
│   └── TASK_RULES.md          # Rules and workflow
├── resources/                 # Analysis and audit resources
│   ├── audits/                # Source data extractions
│   ├── analyses/              # Comparative analysis results
│   ├── templates/             # Reusable templates
│   ├── external/              # External reference documents
│   └── profile/               # Professional profile reference
├── dist/                      # Build outputs (gitignored)
│   ├── cv.pdf                 # Full CV (~4 pages)
│   └── cv-short.pdf           # Short CV (1 page)
├── docs/                      # Project documentation
│   └── GIT_WORKFLOW.md        # Git conventions
├── scripts/                   # Build and verification scripts
│   ├── lib/                   # Shared Python utilities
│   ├── reports/               # Reporting scripts (CFD, weekly)
│   ├── task_management/       # Task management Python module
│   ├── tests/                 # Tests for lib module
│   ├── update_priority_scores.py  # WSJF priority scoring
│   └── verification/          # Python verification module
│       ├── __init__.py
│       ├── build.py           # Compilation verification
│       ├── dates.py           # Date consistency check
│       ├── format.py          # Format verification
│       ├── runner.py          # Run all verifications
│       └── tests/             # Pytest unit tests
├── src/                       # Typst sources
│   ├── assets/                # Images
│   │   ├── identite.png       # Profile photo
│   │   └── profile.png        # Alternative profile
│   ├── data/                  # Data files
│   │   └── publications.yml   # Bibliography data
│   ├── shared/                # Shared content between CV versions
│   │   ├── config.typ         # Author info, colors, layout settings
│   │   └── sidebar.typ        # Sidebar content (parameterized)
│   ├── cv.typ                 # Full CV source (exhaustive, ~4 pages)
│   ├── cv-short.typ           # Short CV source (1 page)
│   └── manifest.yml           # Font manifest
├── .claude/                   # Claude Code configuration
│   └── commands/              # Custom slash commands
├── justfile                   # Build automation
└── README.md                  # Project overview
```

## Typst and neat-cv Template

### Template Import

The CV uses a local fork of `neat-cv` template with shared configuration:

```typst
#import "neat-cv-local.typ": (cv-setup, cv-page-one, cv-continued, entry, ...)

// Shared configuration
#import "shared/config.typ": author-config, accent-color, header-color, ...
#import "shared/sidebar.typ": sidebar-content, about-long
```

### Shared Content Architecture

Both CV versions (`cv.typ` and `cv-short.typ`) share common content via `src/shared/`:

| File | Content | Usage |
|------|---------|-------|
| `config.typ` | Author info, colors, layout settings | Both versions |
| `sidebar.typ` | Sidebar content with parameterized "A propos" | Both versions |

**Modifying shared content:**

- **Author info** (name, email, phone): Edit `shared/config.typ`
- **Sidebar sections** (Contact, Skills, etc.): Edit `shared/sidebar.typ`
- **"A propos" text**: Two variants in `sidebar.typ`:
  - `about-long`: Full version with presales details (used by cv.typ)
  - `about-short`: Condensed version (used by cv-short.typ)

### Key Components

**Document Configuration**:

- Uses `cv-setup.with()` to set global parameters from shared config
- Configures personal information via `author-config` from `shared/config.typ`
- Sets visual styling (accent color: `#4682b4`, header color: `#3b4f60`)
- Profile picture, fonts, paper size (A4), and sidebar width

**Sidebar** (via `shared/sidebar.typ`):

- Contact information and social links
- Languages with proficiency levels
- Skills displayed as pills using `item-pills()`
- "A propos" section (parameterized for long/short versions)

**Main Content** (lines 103-255):

- Professional experience using `#entry()` components
- Education history
- Certifications
- Uses `#colbreak()` to force page breaks

### Content Guidelines

When modifying the CV:

- All content is in French
- Experience entries use `#entry()` with title, date, institution, location, and description
- Skills are displayed as pills using `item-pills()`
- Language proficiency uses `item-with-level()` with 1-5 scale
- The CV is designed for A4 paper with a 4.5cm sidebar
- Accent color scheme uses blue tones for professional appearance

### CV Decisions Reference

**IMPORTANT:** Before modifying CV content (CNT), layout (LAY), or template (TPL), consult the decisions file:

- **File:** [resources/profile/cv-decisions.md](resources/profile/cv-decisions.md)

This file contains:

- Strategic positioning decisions with justifications
- Skills organization and prioritization choices
- Alternatives reserved for targeted CV adaptations
- Historical log of all content decisions

**Workflow:**

1. **Before changes:** Check existing decisions for relevant guidance
2. **During changes:** Apply documented decisions consistently
3. **After changes:** Document new decisions with justifications in the file

### Publications File

The `publications.yml` file uses Typst's bibliography format with YAML structure. Currently contains placeholder data that should be replaced with actual publications if needed.

## Technical Notes

- Typst version in use: 0.14.0
- Paper size: A4
- Font size: 10pt
- Color scheme: Professional blue (#4682b4 accent, #3b4f60 headers)
- The CV is currently a 5-page document (as of November 2025)

## Quality Verification

The project includes a comprehensive verification system to ensure CV quality before distribution.

### Quick Commands

```bash
# Run all verification checks
just verify

# Individual checks
just verify-build   # Compilation check
just verify-dates   # Date consistency check
just verify-format  # Formatting check

# Run verification tests
just test-verify
```

### Verification Module

The verification system is implemented as a Python module in `scripts/verification/`:

| Module | Purpose |
|--------|---------|
| `build.py` | Verifies Typst compilation succeeds and PDF is generated |
| `dates.py` | Checks date consistency (format, chronological order, no future dates) |
| `format.py` | Validates structure, contact info, and formatting |
| `runner.py` | Runs all verification checks in sequence |
| `tests/` | Pytest unit tests (53 tests) |

### Manual Checklist

For comprehensive pre-distribution verification, see [VERIFICATION.md](VERIFICATION.md) which includes:

- Compilation checks
- Contact information verification
- Spelling and grammar review
- Date consistency validation
- Style consistency review
- Visual formatting check
- Content professionalism review
- Confidentiality check
- Length and readability assessment

### Recommended Workflow

1. **During Development**: Run `just validate` after each significant change
2. **Before Export**: Run `just verify` for automated checks
3. **Before Distribution**: Complete the [VERIFICATION.md](VERIFICATION.md) checklist

## Task Management System

This project uses a structured task management system to track CV evolution and improvements.

### Task Organization

All tasks are documented in [.tasks/TASKS.md](.tasks/TASKS.md), which serves as the central dashboard. Detailed task descriptions are stored in the `.tasks/tasks/` directory.

### Task ID Convention

Tasks use the format `XXX-NNN` where:

- **XXX** = 3-letter category code (trigramme)
- **NNN** = Auto-incremented number (001, 002, etc.)

**Available trigrammes:**

- **CNT** (Content) - CV content updates and information
- **TPL** (Template) - Template structure and architecture
- **QUA** (Quality) - Quality checks and verification
- **PIP** (Pipeline) - CI/CD, automation, build processes
- **INF** (Infrastructure) - Technical infrastructure
- **LAY** (Layout) - Visual layout, design, styling
- **DOC** (Documentation) - Documentation and guides

### Task Automation

The task management system is implemented as a **Claude Skill** with progressive disclosure architecture, combining workflows, Python scripts, and comprehensive testing.

**Architecture:**

```text
# Skill definition
.claude/skills/task-management/
├── workflows/        # Concise workflow documentation
└── templates/        # Reusable templates

# Implementation (at project root)
scripts/task_management/
├── core/             # ID generation, validation, dashboard, Git
├── algorithms/       # Priority scoring (WSJF)
├── validators/       # DoR/DoD validation
├── analysis/         # Recommendation parsing
└── tests/            # 74 unit tests (pytest)

config/task_management/
├── priorities.yml    # Priority scoring config
├── trigrammes.yml    # Task categories
└── paths.yml         # File paths
```

**Available Workflows:**

- `task-create` - Create a new task interactively
- `task-from-idea` - Create task from ideas backlog ([.tasks/IDEAS.md](.tasks/IDEAS.md))
- `task-start <ID>` - Start working (DoR validation, Git branch, status update)
- `task-complete <ID>` - Complete task (DoD validation, final commit, backlog ideas)
- `task-next` - WSJF-based intelligent task suggestion
- `task-from-analysis` - Create tasks from analysis recommendations
- `analyze-source` - Extract data from external sources (LinkedIn, GitHub, etc.)
- `task-validate` - Validate system consistency
- `task-archive <ID>` - Archive completed tasks

**Ideas Backlog:**

Future improvement ideas are automatically collected in [.tasks/IDEAS.md](.tasks/IDEAS.md) when completing tasks. These ideas can be transformed into concrete tasks using `/task-from-idea`, which provides:

- Interactive selection from available ideas
- Pre-filled task creation (trigramme, title, context)
- Automatic removal from backlog once transformed
- Traceability to the source task

**Rules and Quality Gates:**

The system enforces Definition of Ready (DoR) and Definition of Done (DoD) criteria. See [.tasks/TASK_RULES.md](.tasks/TASK_RULES.md) for:

- Criteria for starting a task (DoR)
- Criteria for completing a task (DoD)
- Workflow steps and quality gates
- Error handling and recovery

**Manual Workflow (if needed):**

If automation is unavailable, follow the manual process:

1. **Create:** Copy [.tasks/tasks/TEMPLATE.md](.tasks/tasks/TEMPLATE.md), fill fields, add to [.tasks/TASKS.md](.tasks/TASKS.md)
2. **Start:** Update status to "🔄 En cours", create branch `task/XXX-NNN-slug`
3. **Work:** Reference task in commits with `Refs XXX-NNN`
4. **Complete:** Update status to "✅ Terminé", commit with `Closes XXX-NNN`, move in [.tasks/TASKS.md](.tasks/TASKS.md)

**Current tasks:**
See [.tasks/TASKS.md](.tasks/TASKS.md) for the full list of active, pending, and completed tasks.

## Analysis and Audit System

This project includes a structured system for analyzing the CV against external sources (LinkedIn, GitHub, external CVs, personal websites) to identify gaps, inconsistencies, and improvement opportunities.

### System Overview

The analysis system enables:

- **Source Extraction**: Structured extraction of data from external sources
- **Comparative Analysis**: Identify gaps between CV and source data
- **Recommendation Tracking**: Track improvement recommendations with priorities
- **Task Generation**: Automatically create tasks from recommendations
- **Full Traceability**: Source → Analysis → Recommendation → Task → CV Change

### Directory Structure

```text
resources/                           # Dedicated resources directory (project root)
├── README.md                        # Documentation
├── audits/                          # Source data extractions
│   └── {TASK-ID}/
│       ├── linkedin-profile.md      # Raw LinkedIn data
│       ├── github-profile.md        # Raw GitHub data
│       └── cv-snapshot.md           # CV state at audit time
├── analyses/                        # Analysis results
│   └── {TASK-ID}/
│       ├── audit-report.md          # Comparative analysis
│       ├── recommendations.md       # Detailed recommendations
│       ├── recommendations-status.md # Tracking file (for /task-from-analysis)
│       ├── action-plan.md           # Implementation plan
│       └── metrics.md               # Statistics and metrics
├── templates/                       # Reusable templates
│   ├── audit-template.md
│   ├── recommendations-template.md
│   └── source-extraction-template.md
├── external/                        # External reference documents (CVs, etc.)
└── profile/                         # Professional profile reference
```

### Analysis Commands

**Extract Source Data:**

```bash
/analyze-source [--task-id=XXX-NNN]
```

This command provides interactive guidance to extract data from external sources:

- Supports LinkedIn, GitHub, external CVs, websites, and other sources
- Uses templates for consistent data structure
- Saves extracted data to `resources/audits/{TASK-ID}/`
- Links to parent analysis task if provided

**Create Tasks from Recommendations:**

```bash
/task-from-analysis [--analysis-id=XXX-NNN] [--filter=high|medium|low|all]
```

This command transforms analysis recommendations into concrete tasks:

- Lists analyses with pending recommendations
- Allows batch selection ('1,5,6', 'all', 'high', etc.)
- Pre-fills task creation with recommendation data
- Updates `recommendations-status.md` with task IDs
- Maintains full traceability (recommendation → task)
- Updates statistics in `ANALYSES.md`

### Typical Workflow

1. **Create Analysis Task:**

   ```bash
   /task-create
   # Choose CNT trigramme, e.g., "CNT-001 LinkedIn Audit"
   ```

2. **Extract Source Data:**

   ```bash
   /task-start CNT-001
   /analyze-source --task-id=CNT-001
   # Follow interactive prompts to extract LinkedIn/GitHub/etc. data
   ```

3. **Perform Analysis:**
   - Create comparative analysis in `resources/analyses/CNT-001/`
   - Use `audit-template.md` for structure
   - Document gaps, inconsistencies, and recommendations
   - Create `recommendations-status.md` for tracking

4. **Generate Tasks:**

   ```bash
   /task-from-analysis --analysis-id=CNT-001 --filter=high
   # Select recommendations to transform into tasks
   # Each task automatically links back to its recommendation
   ```

5. **Execute Tasks:**

   ```bash
   /task-start CNT-002  # Task created from recommendation
   # Make CV changes
   /task-complete CNT-002
   # Recommendation automatically marked as completed in recommendations-status.md
   ```

### Recommendation ID Format

Recommendations use the format `{ANALYSIS-ID}-R{NN}`:

- Example: `CNT-001-R05` (recommendation 5 from analysis CNT-001)
- Ensures unique identification across all analyses
- Enables clear traceability in task files and commit messages

### Key Files

- [.tasks/ANALYSES.md](.tasks/ANALYSES.md) - Central dashboard for all analyses
- [resources/templates/](resources/templates/) - Templates for audits and recommendations
- Individual analysis folders contain all related files (audits, analysis results, tracking)

### Priority Levels

Recommendations use a 4-level priority system:

- 🔴🔴 **Very High**: Critical issues affecting credibility
- 🔴 **High**: Important issues to address quickly
- 🟡 **Medium**: Desirable improvements
- 🟢 **Low**: Optional, can be deferred

Priority mapping for task creation:

- Very High → High priority task (🔴)
- High → High priority task (🔴)
- Medium → Medium priority task (🟡)
- Low → Low priority task (🟢)

## Visual Analysis Workflow

Claude can analyze the compiled CV visually to suggest design improvements.

### Workflow Steps

```bash
# 1. Compile the CV
just build

# 2. Read the PDF for visual analysis
# Claude reads dist/cv.pdf directly

# 3. Analyze according to evaluation criteria
# 4. Suggest Typst modifications
# 5. Iterate until satisfied
```

### Evaluation Criteria

When analyzing the CV visually, evaluate these aspects:

| Criterion | Description | Target |
|-----------|-------------|--------|
| **Readability** | Font clarity, size, contrast | Clear at arm's length |
| **Balance** | Harmonious distribution of elements | No heavy/empty zones |
| **Hierarchy** | Clear distinction between info levels | Titles > subtitles > content |
| **Spacing** | Margins, padding, line-height | Consistent throughout |
| **Professionalism** | Clean, modern appearance | Appropriate for target industry |
| **Scannability** | Easy quick reading by recruiter | Key info visible in <30s |

### Rating Scale

Use this scale for visual evaluation:

- 4 stars: Excellent, no improvement needed
- 3 stars: Good, minor improvements possible
- 2 stars: Acceptable, notable improvements needed
- 1 star: Poor, significant rework required

### Typical Issues and Solutions

| Issue | Typst Solution |
|-------|----------------|
| Too dense | Increase `#v()` spacing, reduce content |
| Unbalanced pages | Adjust `#colbreak()` or `#pagebreak()` |
| Poor hierarchy | Modify font sizes in template config |
| Sidebar overflow | Reduce skills/content or adjust `sidebar-width` |
| Inconsistent spacing | Standardize `#v()` values |

### Example Analysis Output

```markdown
## Visual Analysis - [Date]

### Scores
- Readability: 4/4
- Balance: 3/4 (page 5 has 50% whitespace)
- Hierarchy: 4/4
- Spacing: 3/4
- Professionalism: 4/4
- Scannability: 2/4 (5 pages is too long)

### Recommendations
1. [HIGH] Reduce to 2 pages for standard applications
2. [MEDIUM] Consolidate duplicate sections
3. [LOW] Add visual separators between major sections
```

### Related Tasks

- [LAY-001](.tasks/tasks/LAY-001-sidebar-premiere-page-uniquement.md) - Sidebar on first page only
- [LAY-002](.tasks/tasks/LAY-002-consolidation-sections-dupliquees.md) - Consolidate duplicate sections
- [TPL-001](.tasks/tasks/TPL-001-cv-versions.md) - Short and long CV versions

## Git Workflow

This project follows a simple Git workflow with conventional commits and emojis. See [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md) for detailed commit conventions and guidelines, including how to reference tasks in commits.

- **IMPORTANT** Ne met pas de signature claude dans les commits
