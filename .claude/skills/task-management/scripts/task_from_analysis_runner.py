#!/usr/bin/env python3
"""
Task-from-analysis runner script.
Creates tasks from analysis recommendations.
"""

import sys
from pathlib import Path

# Add scripts directory to path
scripts_dir = Path(__file__).parent
sys.path.insert(0, str(scripts_dir))

from analysis.recommendation_parser import parse_recommendations_file, find_pending_recommendations, group_by_priority
from core.id_generator import get_next_id, generate_filename
from core.dashboard_updater import add_task_to_dashboard
from core.config_loader import load_config

def main():
    analysis_id = 'CNT-014'
    priority_filter = 'high'  # very-high + high priorities

    # Parse recommendations
    rec_file = Path(f'.tasks/resources/analyses/{analysis_id}/recommendations-status.md')
    if not rec_file.exists():
        print(f"❌ Fichier de recommandations introuvable: {rec_file}")
        return 1

    print(f"📖 Lecture des recommandations depuis {rec_file}...")
    all_recs = parse_recommendations_file(rec_file, analysis_id)
    pending = find_pending_recommendations(all_recs)

    # Filter by priority (very high + high)
    filtered = [r for r in pending if r.priority_emoji in ['🔴🔴', '🔴']]

    if not filtered:
        print(f"✅ Aucune recommandation prioritaire (très haute/haute) en attente pour {analysis_id}")
        return 0

    # Group by priority
    groups = group_by_priority(filtered)

    # Display recommendations
    print(f"\n{'='*60}")
    print(f"Recommandations prioritaires pour {analysis_id}")
    print(f"{'='*60}\n")

    count = 0
    rec_list = []

    for emoji in ['🔴🔴', '🔴']:
        recs = groups.get(emoji, [])
        if not recs:
            continue

        priority_name = 'TRÈS HAUTE' if emoji == '🔴🔴' else 'HAUTE'
        print(f"\n{emoji} {priority_name} ({len(recs)} recommandations):\n")

        for rec in recs:
            count += 1
            rec_list.append(rec)
            print(f"  {count}. [{rec.rec_id}] {rec.title}")
            if rec.category:
                print(f"     Catégorie: {rec.category}")
            if rec.cv_reference:
                print(f"     Référence CV: {rec.cv_reference}")
            print()

    print(f"\n{'='*60}")
    print(f"Total: {count} recommandations prioritaires")
    print(f"{'='*60}\n")

    # Summary for user to review
    print("📋 Prochaines étapes:")
    print(f"   - {len([r for r in filtered if r.priority_emoji == '🔴🔴'])} recommandations TRÈS HAUTE priorité")
    print(f"   - {len([r for r in filtered if r.priority_emoji == '🔴'])} recommandations HAUTE priorité")
    print(f"\n💡 Utilisez le workflow task-create interactif pour créer ces tâches.")
    print(f"   Les IDs suggérés commencent à CNT-017\n")

    return 0

if __name__ == '__main__':
    sys.exit(main())
