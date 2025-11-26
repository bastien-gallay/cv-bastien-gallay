#!/bin/bash
# Verify CV compilation
# Usage: ./scripts/verify-build.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=== Vérification de la compilation ==="
echo ""

# Check if typst is available
if ! command -v typst &> /dev/null; then
    echo "ERREUR: typst n'est pas installé"
    exit 1
fi

# Check source file exists
if [ ! -f "$PROJECT_ROOT/src/cv.typ" ]; then
    echo "ERREUR: src/cv.typ introuvable"
    exit 1
fi

# Create dist directory if needed
mkdir -p "$PROJECT_ROOT/dist"

# Try to compile
echo "Compilation en cours..."
if typst compile "$PROJECT_ROOT/src/cv.typ" "$PROJECT_ROOT/dist/cv.pdf" 2>&1; then
    echo "OK: Compilation réussie"
else
    echo "ERREUR: Échec de la compilation"
    exit 1
fi

# Check PDF was created
if [ ! -f "$PROJECT_ROOT/dist/cv.pdf" ]; then
    echo "ERREUR: Le PDF n'a pas été généré"
    exit 1
fi

# Check PDF is not empty
if [ ! -s "$PROJECT_ROOT/dist/cv.pdf" ]; then
    echo "ERREUR: Le PDF est vide"
    exit 1
fi

# Get PDF info
PDF_SIZE=$(stat -f%z "$PROJECT_ROOT/dist/cv.pdf" 2>/dev/null || stat --printf="%s" "$PROJECT_ROOT/dist/cv.pdf" 2>/dev/null)
echo "OK: PDF généré ($PDF_SIZE octets)"

echo ""
echo "=== Vérification de la compilation: RÉUSSIE ==="
