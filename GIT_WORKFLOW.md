# Git Workflow & Versioning Policy

This document defines the Git workflow, commit conventions, branching strategy, and versioning policy for the neat-cv project.

## 📝 Commit Message Convention

This project follows **Conventional Commits** with emojis for better readability.

### Format

```plaintext
<type>(<scope>): <emoji> <subject>

[optional body]

[optional footer]
```

### Commit Types

| Type | Emoji | Description | Example |
|------|-------|-------------|---------|
| `feat` | ✨ | New feature | `feat(cv): ✨ add certifications section` |
| `fix` | 🐛 | Bug fix | `fix(layout): 🐛 correct spacing in sidebar` |
| `docs` | 📝 | Documentation only | `docs: 📝 update CLAUDE.md` |
| `style` | 💄 | Formatting/styling | `style: 💄 adjust accent colors` |
| `refactor` | ♻️ | Content restructuring | `refactor(cv): ♻️ reorganize experience section` |
| `content` | ✏️ | Content updates | `content: ✏️ update contact information` |
| `build` | 📦 | Build system/typst | `build: 📦 upgrade neat-cv template` |
| `ci` | 👷 | CI/CD changes | `ci: 👷 add github actions workflow` |
| `chore` | 🔧 | Maintenance tasks | `chore: 🔧 update gitignore` |
| `revert` | ⏪ | Revert previous commit | `revert: ⏪ revert content update` |

### Scope (Optional)

Common scopes in this project:

- `cv` - Main CV content
- `layout` - Layout and styling changes
- `profile` - Profile section modifications
- `experience` - Professional experience section
- `education` - Education section
- `skills` - Skills and certifications
- `sidebar` - Sidebar content
- `images` - Profile images and assets
- `publications` - Publications bibliography

### Subject Guidelines

- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize first letter after emoji
- No period at the end
- Keep it concise (50 characters or less)

### Body Guidelines

- Separate from subject with blank line
- Explain **what** and **why**, not how
- Wrap at 72 characters
- Use bullet points for multiple changes

### Examples

**Simple commit:**

```plaintext
feat(cv): ✨ add certifications section
```

**Commit with body:**

```plaintext
content(experience): ✏️ update PALO IT role details

Added more specific details about CTO responsibilities and
technical leadership initiatives. Clarified timeline and key
achievements during consultant and CTO periods.
```

**Breaking change:**

```plaintext
feat(layout)!: ✨ change to single-page layout

BREAKING CHANGE: The CV now uses a single-page layout instead
of two pages. This requires regenerating the PDF and may affect
printing settings.
```

## 🌿 Branching Strategy

### Branch Types

#### Main Branches

- **`main`** - Production-ready code, always stable
  - All commits should be meaningful and tested
  - Never commit directly (except for solo work on docs/chores)
  - Tagged with version numbers

#### Supporting Branches

| Prefix | Purpose | Example | Base Branch | Merge Into |
|--------|---------|---------|-------------|------------|
| `feat/` | New sections/features | `feat/add-publications` | `main` | `main` |
| `fix/` | Layout/formatting fixes | `fix/sidebar-spacing` | `main` | `main` |
| `docs/` | Documentation | `docs/workflow-guide` | `main` | `main` |
| `refactor/` | Content restructuring | `refactor/experience-order` | `main` | `main` |
| `content/` | Content updates | `content/update-skills` | `main` | `main` |
| `style/` | Visual styling | `style/color-scheme` | `main` | `main` |
| `chore/` | Maintenance | `chore/update-images` | `main` | `main` |

### Branch Naming Rules

- Use lowercase with hyphens: `feat/publications-section`
- Be descriptive but concise: `fix/sidebar-spacing` not `fix/bug`
- Include context: `content/update-palo-it-role`

### Workflow

#### Solo Development (Current)

**Quick changes** (docs, small fixes):

```bash
# Work directly on main
git checkout main
# make changes
git add .
git commit -m "docs: 📝 update readme"
```

**Feature development** (recommended):

```bash
# Create feature branch
git checkout -b feat/new-feature

# Make commits
git add .
git commit -m "feat: ✨ implement feature"

# More commits as needed...

# Merge back to main (fast-forward)
git checkout main
git merge feat/new-feature

# Delete feature branch
git branch -d feat/new-feature
```

#### Future Collaboration Workflow

When working with others:

```bash
# Start new feature
git checkout main
git pull origin main
git checkout -b feat/new-feature

# Make commits
git add .
git commit -m "feat: ✨ implement feature"
git push -u origin feat/new-feature

# Create Pull Request on GitHub
# After PR approval and CI passes
# Merge via GitHub (squash or merge commit)

# Clean up
git checkout main
git pull origin main
git branch -d feat/new-feature
```

## 🏷️ Versioning Strategy

This project follows **Semantic Versioning 2.0.0** (SemVer).

### Version Format

```plaintext
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
```

Example: `1.2.3-beta.1+20250128`

### Version Numbers

- **MAJOR** (1.x.x) - Major CV restructuring or format changes
  - Example: Complete career change, new template, radical redesign
- **MINOR** (x.1.x) - New sections or significant content additions
  - Example: Adding publications section, new certifications, major role
- **PATCH** (x.x.1) - Updates and fixes
  - Example: Correcting dates, fixing typos, updating contact info

### Pre-release Identifiers

- `alpha` - Early development, unstable
- `beta` - Feature complete, testing phase
- `rc` - Release candidate, final testing

Examples:

- `0.1.0-alpha.1` - First alpha release
- `1.0.0-beta.2` - Second beta for version 1.0.0
- `2.0.0-rc.1` - First release candidate for 2.0.0

### Version 1.x.x

- Current phase: **Stable CV**
- Version `1.x.x` indicates a production-ready CV
- MAJOR versions indicate significant career milestones or restructuring
- MINOR versions for adding new sections or significant updates
- PATCH versions for content updates and corrections

### Tagging Releases

```bash
# Create annotated tag
git tag -a v1.0.0 -m "feat: ✨ initial CV with complete professional history"

# Push tag to remote (when using remote)
git push origin v1.0.0

# List all tags
git tag -l

# Show tag details
git show v1.0.0
```

### When to Increment Versions

**For CV maintenance:**

- Tag significant milestones and versions sent for job applications
- Don't tag every change, only important versions
- Consider tagging before major applications or career updates

**Examples:**

- Initial complete CV → `v1.0.0`
- Add new certifications section → `v1.1.0`
- Update with new role (PALO IT CTO) → `v1.2.0`
- Major career change or restructure → `v2.0.0`
- Fix typos or update contact info → `v1.2.1`

## 🔄 Merge Strategies

### Fast-Forward Merge (Default for Solo)

```bash
git checkout main
git merge feat/new-feature  # Fast-forward if possible
```

**Use when:**

- Working solo
- Linear history preferred
- Feature branch has no conflicts

### Merge Commit

```bash
git checkout main
git merge --no-ff feat/new-feature  # Always create merge commit
```

**Use when:**

- Want to preserve feature branch context
- Multiple related commits in feature branch
- Documenting significant features

### Squash and Merge

```bash
git checkout main
git merge --squash feat/new-feature
git commit -m "feat: ✨ complete feature description"
```

**Use when:**

- Feature branch has messy commit history
- Want single commit for feature
- Cleaning up experimental commits

## 🔍 Useful Git Commands

### Viewing History

```bash
# Pretty log with graph
git log --oneline --graph --all --decorate

# Show changes in commit
git show <commit-hash>

# Show file history
git log --follow -- path/to/file

# Search commits
git log --grep="feat(vfs)"
```

### Undoing Changes

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Amend last commit message
git commit --amend -m "new message"

# Discard working directory changes
git restore path/to/file
```

### Branch Management

```bash
# List all branches
git branch -a

# Delete local branch
git branch -d feat/feature-name

# Delete remote branch (when applicable)
git push origin --delete feat/feature-name

# Rename current branch
git branch -m new-name
```

## 📋 Commit Checklist

Before committing, ensure:

- [ ] CV compiles successfully (`typst compile cv.typ`)
- [ ] PDF output looks correct (check cv.pdf)
- [ ] Commit message follows convention
- [ ] Changes are logical and atomic
- [ ] No personal sensitive data exposed (phone numbers are OK, but check other info)
- [ ] Images are optimized and not too large
- [ ] Publications file is properly formatted YAML

## 🚫 What NOT to Commit

Should avoid committing (create `.gitignore` if needed):

- `.DS_Store` (macOS)
- `*.log` files
- Temporary build files
- Very large unoptimized images (>1MB)
- Backup files (`*.bak`, `*~`)
- Editor-specific files (`.vscode/`, `.idea/`)

Note: The compiled PDF (`cv.pdf`) IS tracked in this repository as it's the main deliverable.

## 🎓 Learning Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Git Branching Strategies](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)
- [Gitmoji Guide](https://gitmoji.dev/)

## 🔄 Review and Updates

This workflow policy should be reviewed and updated as the project evolves, especially when:

- Sharing CV management with a career coach or HR consultant
- Setting up automated PDF generation via CI/CD
- Creating multiple CV variants for different positions
- Establishing contribution guidelines for collaborative editing
