# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CV (curriculum vitae) project written in Typst, a modern markup-based typesetting system. The CV uses the `neat-cv` template (version 0.4.0) to generate a professional two-page resume in French.

## Key Commands

### Building the CV
```bash
# Compile the CV to PDF
typst compile cv.typ

# Watch mode - automatically recompile on changes
typst watch cv.typ

# Compile with custom output name
typst compile cv.typ output.pdf
```

### Viewing the Output
The compiled PDF is saved as `cv.pdf` in the root directory.

## Project Structure

- **cv.typ**: Main CV source file containing all content and configuration
- **cv.pdf**: Generated PDF output (604KB)
- **identite.png**: Profile photo used in the CV header
- **profile.png**: Alternative profile image
- **publications.yml**: Bibliography data file containing example academic publications (currently contains placeholder data from "Back to the Future" theme)
- **manifest.yml**: Font manifest listing available fonts (Noto Sans, Fira Sans, Roboto with various weights)

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

All tasks are documented in [TASKS.md](TASKS.md), which serves as the central dashboard. Detailed task descriptions are stored in the `TASKS/` directory.

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

The task management system is fully automated via Claude commands. See [.claude/commands/README.md](.claude/commands/README.md) for complete documentation.

**Quick Commands:**

- `/task-create` - Create a new task interactively
- `/task-from-idea` - Create a task from an idea in the backlog ([IDEAS.md](IDEAS.md))
- `/task-start <ID>` - Start working on a task (creates Git branch, updates status)
- `/task-complete <ID>` - Complete a task (validates DoD, creates final commit, adds ideas to backlog)
- `/task-next` - Get intelligent suggestion for next task to work on
- `/task-validate` - Validate system consistency
- `/task-archive <ID>` - Archive a completed task

**Ideas Backlog:**

Future improvement ideas are automatically collected in [IDEAS.md](IDEAS.md) when completing tasks. These ideas can be transformed into concrete tasks using `/task-from-idea`, which provides:
- Interactive selection from available ideas
- Pre-filled task creation (trigramme, title, context)
- Automatic removal from backlog once transformed
- Traceability to the source task

**Rules and Quality Gates:**

The system enforces Definition of Ready (DoR) and Definition of Done (DoD) criteria. See [TASK_RULES.md](TASK_RULES.md) for:
- Criteria for starting a task (DoR)
- Criteria for completing a task (DoD)
- Workflow steps and quality gates
- Error handling and recovery

**Manual Workflow (if needed):**

If automation is unavailable, follow the manual process:

1. **Create:** Copy [TASKS/TEMPLATE.md](TASKS/TEMPLATE.md), fill fields, add to [TASKS.md](TASKS.md)
2. **Start:** Update status to "🔄 En cours", create branch `task/XXX-NNN-slug`
3. **Work:** Reference task in commits with `Refs XXX-NNN`
4. **Complete:** Update status to "✅ Terminé", commit with `Closes XXX-NNN`, move in [TASKS.md](TASKS.md)

**Current tasks:**
See [TASKS.md](TASKS.md) for the full list of active, pending, and completed tasks.

## Git Workflow

This project follows a simple Git workflow with conventional commits and emojis. See [GIT_WORKFLOW.md](GIT_WORKFLOW.md) for detailed commit conventions and guidelines, including how to reference tasks in commits.
