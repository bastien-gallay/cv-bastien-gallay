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

### Working with Tasks

**Create a new task:**
1. Choose the appropriate trigramme (e.g., CNT for content)
2. Find the next available number for that trigramme
3. Copy [TASKS/TEMPLATE.md](TASKS/TEMPLATE.md)
4. Create `TASKS/XXX-NNN-task-name.md`
5. Fill in all template fields
6. Add entry to [TASKS.md](TASKS.md)

**Work on a task:**
1. Update status to "🔄 En cours" in the task file
2. Reference the task ID in commits: `Refs XXX-NNN`
3. Check off subtasks as you complete them

**Complete a task:**
1. Mark all subtasks as done
2. Update status to "✅ Terminé"
3. Make final commit with `Closes XXX-NNN`
4. Move to "Completed" section in [TASKS.md](TASKS.md)

**Current tasks:**
See [TASKS.md](TASKS.md) for the full list of active, pending, and completed tasks.

## Git Workflow

This project follows a simple Git workflow with conventional commits and emojis. See [GIT_WORKFLOW.md](GIT_WORKFLOW.md) for detailed commit conventions and guidelines, including how to reference tasks in commits.
