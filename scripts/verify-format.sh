#!/bin/bash
# Verify formatting and consistency in CV
# Usage: ./scripts/verify-format.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
CV_FILE="$PROJECT_ROOT/src/cv.typ"

echo "=== Vérification du formatage ==="
echo ""

ERRORS=0
WARNINGS=0

# Check file exists
if [ ! -f "$CV_FILE" ]; then
    echo "ERREUR: Fichier CV introuvable: $CV_FILE"
    exit 1
fi

# Check for common formatting issues

echo "1. Vérification des espaces..."

# Trailing whitespace
trailing_ws=$(grep -cn '[[:space:]]$' "$CV_FILE" || echo "0")
if [ "$trailing_ws" -gt 0 ]; then
    echo "  ATTENTION: $trailing_ws lignes avec espaces en fin de ligne"
    WARNINGS=$((WARNINGS + 1))
fi

# Multiple consecutive spaces (except in comments)
multiple_spaces=$(grep -cvE '^[[:space:]]*//' "$CV_FILE" | xargs -I {} grep -c '  ' "$CV_FILE" 2>/dev/null || echo "0")
if [ "$multiple_spaces" -gt 5 ]; then
    echo "  ATTENTION: Espaces multiples détectés"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo "2. Vérification de la structure..."

# Check for required sections
sections=("Expérience" "Etudes" "Certifications" "Expertises" "Langues")
for section in "${sections[@]}"; do
    if grep -q "$section" "$CV_FILE"; then
        echo "  OK: Section '$section' présente"
    else
        echo "  ATTENTION: Section '$section' manquante"
        WARNINGS=$((WARNINGS + 1))
    fi
done

echo ""
echo "3. Vérification des informations de contact..."

# Email
if grep -qE 'email:.*@.*\.' "$CV_FILE"; then
    echo "  OK: Email présent"
else
    echo "  ERREUR: Email manquant ou invalide"
    ERRORS=$((ERRORS + 1))
fi

# Phone
if grep -qE 'phone:' "$CV_FILE"; then
    echo "  OK: Téléphone présent"
else
    echo "  ATTENTION: Téléphone manquant"
    WARNINGS=$((WARNINGS + 1))
fi

# LinkedIn
if grep -qE 'linkedin:' "$CV_FILE"; then
    echo "  OK: LinkedIn présent"
else
    echo "  ATTENTION: LinkedIn manquant"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo "4. Vérification des entrées..."

# Count entries
entry_count=$(grep -c '#entry(' "$CV_FILE" || echo "0")
echo "  Nombre d'entrées (#entry): $entry_count"

if [ "$entry_count" -lt 5 ]; then
    echo "  ATTENTION: Peu d'entrées dans le CV"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo "5. Vérification des caractères spéciaux..."

# Check for common typos or encoding issues
if grep -q '???' "$CV_FILE"; then
    echo "  ERREUR: Caractères d'encodage invalides (???)"
    ERRORS=$((ERRORS + 1))
fi

# Check for proper French characters
if grep -qE '[éèêëàâäùûüîïôöç]' "$CV_FILE"; then
    echo "  OK: Caractères français présents"
else
    echo "  ATTENTION: Pas de caractères accentués détectés"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo "6. Statistiques du fichier..."

lines=$(wc -l < "$CV_FILE")
chars=$(wc -c < "$CV_FILE")
echo "  Lignes: $lines"
echo "  Caractères: $chars"

echo ""
echo "=== Résumé ==="
echo "Erreurs: $ERRORS"
echo "Avertissements: $WARNINGS"

if [ $ERRORS -gt 0 ]; then
    echo ""
    echo "=== Vérification du formatage: ÉCHEC ==="
    exit 1
else
    echo ""
    echo "=== Vérification du formatage: RÉUSSIE ==="
fi
