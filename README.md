# CV - Bastien Gallay

Professional curriculum vitae built with [Typst](https://typst.app/) using the [neat-cv](https://typst.app/universe/package/neat-cv) template (v0.4.0).

## Quick Start

### Prerequisites

- [Typst](https://typst.app/) >= 0.14.0
- [Just](https://just.systems/) command runner (recommended)
- Git for version control

### Build the CV

```bash
# Build PDF
just build

# Watch mode (auto-rebuild on changes)
just watch

# Clean build artifacts
just clean

# Build release with date
just release

# Validate compilation
just validate
```

**Alternative (without just):**

```bash
# Use Typst directly
typst compile src/cv.typ dist/cv.pdf

# Watch mode
typst watch src/cv.typ dist/cv.pdf
```

### View the Output

The generated PDF is saved as `dist/cv.pdf`.

## Project Structure

```text
neat-cv/
├── CLAUDE.md                  # AI assistant instructions
├── .tasks/                    # Task management system
│   ├── tasks/                 # Individual task files
│   ├── .archived/             # Archived completed tasks
│   ├── IDEAS.md               # Ideas backlog
│   ├── TASKS.md               # Dashboard
│   └── TASK_RULES.md          # Rules and workflow
├── dist/                      # Build outputs (gitignored)
│   └── cv.pdf                 # Generated PDF
├── docs/                      # Project documentation
│   ├── GIT_WORKFLOW.md        # Git conventions
│   └── WEEKLY_REPORTS.md      # Weekly reports & CFD
├── scripts/                   # Python scripts and verification
│   ├── reports/               # Weekly reports module
│   ├── task_management/       # Task management module
│   └── verification/          # Verification scripts
├── src/                       # Typst sources
│   ├── assets/                # Images
│   │   ├── identite.png       # Profile photo
│   │   └── profile.png        # Alternative profile
│   ├── data/                  # Data files
│   │   └── publications.yml   # Bibliography data
│   ├── cv.typ                 # Main CV source
│   └── manifest.yml           # Font manifest
├── .claude/                   # Claude Code configuration
├── justfile                   # Build automation
└── README.md                  # This file
```

## Content Guidelines

- **Language:** French
- **Format:** A4, 2 pages
- **Template:** neat-cv 0.4.0
- **Colors:** Professional blue (#4682b4 accent, #3b4f60 headers)

## Customization

### Editing Content

The main CV content is in `src/cv.typ`. Key sections:

- **Lines 6-37:** Personal information and configuration
- **Lines 39-101:** Sidebar (contact, skills, languages, about)
- **Lines 103-255:** Main content (experience, education, certifications)

### Changing Images

- Profile photo: `src/assets/identite.png`
- Alternative: `src/assets/profile.png`

Update the image reference in `src/cv.typ`:

```typst
profile-picture: image("assets/identite.png"),
```

### Modifying Colors

In `src/cv.typ`:

```typst
accent-color: rgb("#4682b4"),    # Main accent color
header-color: rgb("#3b4f60"),    # Section headers
```

## Task Management

This project uses an automated task management system for tracking improvements.

### Quick Commands

- `/task-create` - Create a new task
- `/task-from-idea` - Create task from backlog idea
- `/task-start <ID>` - Start working on a task
- `/task-complete <ID>` - Complete a task
- `/task-next` - Get suggestion for next task
- `/task-validate` - Validate system consistency

See [.tasks/TASKS.md](.tasks/TASKS.md) for the current task list.

### Task Categories

- **CNT** (Content) - CV content updates
- **TPL** (Template) - Template structure
- **QUA** (Quality) - Quality checks
- **PIP** (Pipeline) - CI/CD, automation
- **INF** (Infrastructure) - Technical infrastructure
- **LAY** (Layout) - Visual design
- **DOC** (Documentation) - Documentation

## Weekly Reports

Track progress with Cumulative Flow Diagrams (CFD) and weekly reports.

```bash
# Generate CFD from JSON data
uv run --with matplotlib --with numpy scripts/reports/generate_cfd.py \
  --data .tasks/reports/2025-W48-data.json --output .tasks/reports/
```

Reports in `.tasks/reports/`:

- `YYYY-WNN-recap.md` - Markdown report
- `YYYY-WNN-cfd.png` - CFD visualization
- `YYYY-WNN-data.json` - Raw data

See [docs/WEEKLY_REPORTS.md](docs/WEEKLY_REPORTS.md) for documentation.

## Git Workflow

Commits follow conventional commit format with emojis:

```bash
type(scope): emoji description

- Detail 1
- Detail 2

Refs TASK-ID  # For work in progress
Closes TASK-ID  # For task completion
```

See [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md) for detailed conventions.

## Development

### Installing Just

**macOS (Homebrew):**

```bash
brew install just
```

**Other platforms:**
See [Just installation guide](https://github.com/casey/just#installation)

### Project Setup

1. Clone the repository
2. Install Typst: <https://github.com/typst/typst#installation>
3. Install Just (recommended)
4. Build: `just build`

## Technical Notes

- Typst version: 0.14.0
- Template: neat-cv 0.4.0
- Paper size: A4
- Font size: 10pt
- Sidebar width: 4.5cm

## Known Issues

- Variable fonts warning (template limitation, does not affect output)
- Consider installing static "Noto Sans" fonts for better compatibility

## Contributing

This is a personal CV project. For suggestions or improvements:

1. Check existing tasks in `.tasks/TASKS.md`
2. Add ideas to `.tasks/IDEAS.md`
3. Create a new task with `/task-create`

## License

Personal project - all rights reserved.

## Contact

For questions about this CV structure or Typst template:

- Email: <bastien@gallay.org>
- LinkedIn: [bastiengallay](https://www.linkedin.com/in/bastiengallay/)

---

**Built with:**

- [Typst](https://typst.app/) - Modern markup-based typesetting system
- [neat-cv](https://typst.app/universe/package/neat-cv) - Professional CV template
- [Just](https://just.systems/) - Command runner for build automation
