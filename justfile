# Justfile for neat-cv project
# Modern command runner for build automation

# Default recipe (runs when you type `just`)
default: build

# Build the CV
build:
    @echo "Building CV..."
    @mkdir -p dist
    typst compile src/cv.typ dist/cv.pdf
    @echo "✓ Built dist/cv.pdf"

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

# Run all verification scripts
verify:
    @scripts/verify-all.sh

# Show available recipes
list:
    @just --list
