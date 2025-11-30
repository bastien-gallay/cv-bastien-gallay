# Justfile for neat-cv project
# Modern command runner for build automation

# Default recipe (runs when you type `just`)
default: build

# Build the CV (default: full version)
build:
    @echo "Building CV..."
    @mkdir -p dist
    typst compile src/cv.typ dist/cv.pdf
    @echo "✓ Built dist/cv.pdf"

# Build short CV (1 page)
build-short:
    @echo "Building short CV..."
    @mkdir -p dist
    typst compile src/cv-short.typ dist/cv-short.pdf
    @echo "✓ Built dist/cv-short.pdf"

# Build all CV versions
build-all:
    @echo "Building all CV versions..."
    @mkdir -p dist
    typst compile src/cv.typ dist/cv.pdf
    typst compile src/cv-short.typ dist/cv-short.pdf
    @echo "✓ Built dist/cv.pdf and dist/cv-short.pdf"

# Watch for changes and rebuild automatically (both versions)
watch:
    @echo "Watching for changes (both CV versions)..."
    @mkdir -p dist
    typst watch src/cv.typ dist/cv.pdf &
    typst watch src/cv-short.typ dist/cv-short.pdf

# Clean build artifacts
clean:
    @echo "Cleaning build artifacts..."
    @rm -rf dist/*.pdf
    @echo "✓ Cleaned"

# Build with date in filename for release
release:
    @echo "Building release..."
    @mkdir -p dist
    typst compile src/cv.typ dist/cv-{{`date +%Y-%m-%d`}}.pdf
    @echo "✓ Built dist/cv-{{`date +%Y-%m-%d`}}.pdf"

# Build adapted CV for a specific application (slug naming convention)
build-adapted app_id:
    @echo "Building adapted CV for {{app_id}}..."
    @mkdir -p data/applications/{{app_id}}
    typst compile --root . data/applications/{{app_id}}/{{app_id}}-cv-adapted.typ data/applications/{{app_id}}/{{app_id}}-cv-adapted.pdf
    @echo "✓ Built data/applications/{{app_id}}/{{app_id}}-cv-adapted.pdf"

# Validate CV compiles without errors
validate:
    @echo "Validating CV..."
    @typst compile src/cv.typ --diagnostic-format=short > /dev/null 2>&1 && echo "✓ Validation passed" || (echo "✗ Validation failed" && exit 1)

# Run all verification scripts (Python)
verify:
    @uv run python -m scripts.verification

# Run verification with specific check
verify-build:
    @uv run python -m scripts.verification --build

verify-dates:
    @uv run python -m scripts.verification --dates

verify-format:
    @uv run python -m scripts.verification --format

# Run verification tests
test-verify:
    @uv run --extra dev pytest scripts/verification/tests/ -v

# Run all tests with coverage
test:
    @uv run --extra dev pytest scripts/ -v --cov=scripts --cov-report=term-missing

# Run mutation testing on lib/
test-mutate:
    @uv run --extra dev mutmut run

# Show mutation testing results
test-mutate-results:
    @uv run --extra dev mutmut results

# Update priority scores in TASKS.md
update-scores:
    @uv run python scripts/update_priority_scores.py

# Update priority scores (dry run)
update-scores-dry:
    @uv run python scripts/update_priority_scores.py --dry-run --verbose

# Show available recipes
list:
    @just --list
