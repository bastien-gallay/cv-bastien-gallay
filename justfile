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

# Watch for changes and rebuild automatically
watch:
    @echo "Watching for changes..."
    typst watch src/cv.typ dist/cv.pdf

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

# Show available recipes
list:
    @just --list
