#!/bin/bash
# Run all CV verification scripts
# Usage: ./scripts/verify-all.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=========================================="
echo "     VÉRIFICATION COMPLÈTE DU CV"
echo "=========================================="
echo ""

TOTAL_ERRORS=0

# Run each verification script
scripts=("verify-build.sh" "verify-dates.sh" "verify-format.sh")

for script in "${scripts[@]}"; do
    script_path="$SCRIPT_DIR/$script"

    if [ -f "$script_path" ]; then
        echo ""
        echo "------------------------------------------"

        if bash "$script_path"; then
            echo ""
        else
            TOTAL_ERRORS=$((TOTAL_ERRORS + 1))
            echo ""
            echo "[ÉCHEC] $script a échoué"
        fi
    else
        echo "ATTENTION: Script introuvable: $script"
    fi
done

echo ""
echo "=========================================="
echo "     RÉSUMÉ FINAL"
echo "=========================================="
echo ""

if [ $TOTAL_ERRORS -eq 0 ]; then
    echo "Toutes les vérifications ont réussi!"
    echo ""
    echo "Checklist manuelle: voir VERIFICATION.md"
    echo ""
    exit 0
else
    echo "ÉCHEC: $TOTAL_ERRORS vérification(s) ont échoué"
    echo ""
    echo "Corrigez les erreurs et relancez la vérification."
    echo ""
    exit 1
fi
