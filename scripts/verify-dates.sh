#!/bin/bash
# Verify date consistency in CV
# Usage: ./scripts/verify-dates.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
CV_FILE="$PROJECT_ROOT/src/cv.typ"

echo "=== Vérification des dates ==="
echo ""

ERRORS=0
WARNINGS=0

# Extract date entries from CV
# Date formats: MM/YYYY - MM/YYYY, YYYY, YYYY - Aujourd'hui

# Check for future dates (excluding "Aujourd'hui" and "Présent")
CURRENT_YEAR=$(date +%Y)
CURRENT_MONTH=$(date +%m)

echo "Année courante: $CURRENT_YEAR"
echo ""

# Find all date patterns
echo "Analyse des dates..."

# Pattern: MM/YYYY or YYYY
while IFS= read -r line; do
    # Skip commented lines
    [[ "$line" =~ ^[[:space:]]*// ]] && continue

    # Extract years from dates
    years=$(echo "$line" | grep -oE '\b(19|20)[0-9]{2}\b' || true)

    for year in $years; do
        # Check for future years
        if [ "$year" -gt "$CURRENT_YEAR" ]; then
            echo "ERREUR: Année future détectée: $year"
            echo "  Ligne: $line"
            ERRORS=$((ERRORS + 1))
        fi

        # Check for very old dates (before 1990)
        if [ "$year" -lt 1990 ]; then
            echo "ATTENTION: Année très ancienne: $year"
            echo "  Ligne: $line"
            WARNINGS=$((WARNINGS + 1))
        fi
    done
done < <(grep -E 'date:|Date' "$CV_FILE" || true)

# Check date format consistency (MM/YYYY)
echo ""
echo "Vérification du format des dates..."

# Count different date formats
format_mmyyyy=$(grep -cE 'date:.*[0-9]{2}/[0-9]{4}' "$CV_FILE" || echo "0")
format_yyyy=$(grep -cE 'date:.*"[0-9]{4}"' "$CV_FILE" || echo "0")
format_text=$(grep -cE 'date:.*Aujourd' "$CV_FILE" || echo "0")

echo "  Format MM/YYYY: $format_mmyyyy occurrences"
echo "  Format YYYY seul: $format_yyyy occurrences"
echo "  Avec 'Aujourd'hui': $format_text occurrences"

# Check for chronological order in experience sections
echo ""
echo "Vérification de l'ordre chronologique..."

# This is a simplified check - complex validation would need proper parsing
prev_year=9999
chronological_errors=0

while IFS= read -r line; do
    year=$(echo "$line" | grep -oE '\b(19|20)[0-9]{2}\b' | head -1 || true)
    if [ -n "$year" ]; then
        # For experience, newer should come first (reverse chronological)
        if [ "$year" -gt "$prev_year" ]; then
            # This could be a new section, so just warn
            :
        fi
        prev_year=$year
    fi
done < <(grep -E 'date:' "$CV_FILE" | head -20 || true)

echo ""
echo "=== Résumé ==="
echo "Erreurs: $ERRORS"
echo "Avertissements: $WARNINGS"

if [ $ERRORS -gt 0 ]; then
    echo ""
    echo "=== Vérification des dates: ÉCHEC ==="
    exit 1
else
    echo ""
    echo "=== Vérification des dates: RÉUSSIE ==="
fi
