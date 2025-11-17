# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CV (curriculum vitae) project written in Typst, a modern markup-based typesetting system. The CV uses the `neat-cv` template (version 0.4.0) to generate a professional two-page resume in French.

## Key Commands

### Building the CV

```bash
# Compile the CV to PDF
just build

# Watch mode - automatically recompile on changes
just watch

# Compile with custom output name
just build output.pdf
```

### Viewing the Output

The compiled PDF is saved as `dist/cv.pdf`.

## Project Structure

```text
neat-cv/
├── CLAUDE.md                  # This file - project instructions
├── .tasks/                    # Task management system
│   ├── tasks/                 # Individual task files
│   ├── .archived/             # Archived completed tasks
│   ├── resources/             # Analysis and audit resources
│   │   ├── audits/            # Source data extractions
│   │   ├── analyses/          # Comparative analysis results
│   │   └── templates/         # Reusable templates
│   ├── ANALYSES.md            # Analysis dashboard
│   ├── IDEAS.md               # Ideas backlog
│   ├── TASKS.md               # Tasks dashboard
│   └── TASK_RULES.md          # Rules and workflow
├── dist/                      # Build outputs (gitignored)
│   └── cv.pdf                 # Generated PDF
├── docs/                      # Project documentation
│   └── GIT_WORKFLOW.md        # Git conventions
├── scripts/                   # Build scripts
│   ├── build.sh
│   └── watch.sh
├── src/                       # Typst sources
│   ├── assets/                # Images
│   │   ├── identite.png       # Profile photo
│   │   └── profile.png        # Alternative profile
│   ├── data/                  # Data files
│   │   └── publications.yml   # Bibliography data
│   ├── cv.typ                 # Main CV source
│   └── manifest.yml           # Font manifest
├── .claude/                   # Claude Code configuration
│   └── commands/              # Custom slash commands
├── justfile                   # Build automation
└── README.md                  # Project overview
```

## Typst and neat-cv Template

### Template Import

The CV uses the `neat-cv` template imported with:

```typst
#import "@preview/neat-cv:0.4.0": (
  contact-info, cv, email-link, entry, item-pills, item-with-level,
  publications, side, social-links,
)
```

### Key Components

**Document Configuration** (lines 6-37):

- Uses `cv.with()` to set global parameters
- Configures personal information (name, email, phone, address, position)
- Sets visual styling (accent color: `#4682b4`, header color: `#3b4f60`)
- Profile picture, fonts, paper size (A4), and sidebar width

**Sidebar** (`#side[]` block, lines 39-101):

- Contact information and social links
- Languages with proficiency levels using `item-with-level()`
- Skills displayed as pills using `item-pills()`
- About section and interests

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

### Publications File

The `publications.yml` file uses Typst's bibliography format with YAML structure. Currently contains placeholder data that should be replaced with actual publications if needed.

## Technical Notes

- Typst version in use: 0.14.0
- Paper size: A4
- Font size: 10pt
- Color scheme: Professional blue (#4682b4 accent, #3b4f60 headers)
- The CV is structured as a two-page document with a column break after initial education section

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

```
.claude/skills/task-management/
├── workflows/        # Concise workflow documentation
├── scripts/          # Deterministic Python logic
│   ├── core/         # ID generation, validation, dashboard, Git
│   └── analysis/     # Recommendation parsing
├── config/           # YAML configuration (priorities, paths, trigrammes)
└── tests/            # 74 unit tests (pytest)
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
.tasks/
├── resources/
│   ├── audits/                     # Source data extractions
│   │   └── {TASK-ID}/
│   │       ├── linkedin-profile.md  # Raw LinkedIn data
│   │       ├── github-profile.md    # Raw GitHub data
│   │       └── cv-snapshot.md       # CV state at audit time
│   ├── analyses/                    # Analysis results
│   │   └── {TASK-ID}/
│   │       ├── audit-report.md           # Comparative analysis
│   │       ├── recommendations.md        # Detailed recommendations
│   │       ├── recommendations-status.md # Tracking file (for /task-from-analysis)
│   │       ├── action-plan.md            # Implementation plan
│   │       └── metrics.md                # Statistics and metrics
│   └── templates/                   # Reusable templates
│       ├── audit-template.md
│       ├── recommendations-template.md
│       └── source-extraction-template.md
└── ANALYSES.md                      # Analysis dashboard
```

### Analysis Commands

**Extract Source Data:**

```bash
/analyze-source [--task-id=XXX-NNN]
```

This command provides interactive guidance to extract data from external sources:

- Supports LinkedIn, GitHub, external CVs, websites, and other sources
- Uses templates for consistent data structure
- Saves extracted data to `.tasks/resources/audits/{TASK-ID}/`
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
   - Create comparative analysis in `.tasks/resources/analyses/CNT-001/`
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
- [.tasks/resources/templates/](.tasks/resources/templates/) - Templates for audits and recommendations
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

## Git Workflow

This project follows a simple Git workflow with conventional commits and emojis. See [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md) for detailed commit conventions and guidelines, including how to reference tasks in commits.

- **IMPORTANT** Ne met pas de signature claude dans les commits
