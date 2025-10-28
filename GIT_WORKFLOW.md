# Git Workflow

Simple Git workflow and commit conventions for this personal CV project.

## 📝 Commit Message Convention

This project uses **Conventional Commits** with emojis for better readability.

### Format

```plaintext
<type>(<scope>): <emoji> <subject>

[optional body]
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
| `chore` | 🔧 | Maintenance tasks | `chore: 🔧 update gitignore` |

### Common Scopes

- `cv` - Main CV content
- `layout` - Layout and styling changes
- `experience` - Professional experience section
- `education` - Education section
- `skills` - Skills and certifications
- `sidebar` - Sidebar content

### Guidelines

**Subject:**
- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize first letter after emoji
- No period at the end
- Keep it concise (50 characters or less)

**Body (optional):**
- Separate from subject with blank line
- Explain **what** and **why**, not how
- Use bullet points for multiple changes
- **No need** to add Claude Code co-authoring mentions

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

## 🔍 Useful Git Commands

### Viewing History

```bash
# Pretty log with graph
git log --oneline --graph --all --decorate

# Show changes in commit
git show <commit-hash>

# Show file history
git log --follow -- path/to/file
```

### Undoing Changes

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Amend last commit message
git commit --amend -m "new message"

# Discard working directory changes
git restore path/to/file
```

## 📋 Commit Checklist

Before committing:

- [ ] CV compiles successfully (`typst compile cv.typ`)
- [ ] PDF output looks correct (check cv.pdf)
- [ ] Commit message follows convention
- [ ] No personal sensitive data exposed

## 🚫 What NOT to Commit

Avoid committing:

- `.DS_Store` (macOS)
- `*.log` files
- Temporary build files
- Very large unoptimized images (>1MB)
- Backup files (`*.bak`, `*~`)

**Note:** The compiled PDF (`cv.pdf`) IS tracked as it's the main deliverable.

## 🎓 Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Gitmoji Guide](https://gitmoji.dev/)
