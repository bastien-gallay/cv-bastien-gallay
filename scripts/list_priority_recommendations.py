#!/usr/bin/env python3
"""
Simple script to list priority recommendations from CNT-014.
No dependencies required.
"""

import re
from pathlib import Path

def parse_recommendations(file_path):
    """Parse recommendations-status.md file."""
    content = Path(file_path).read_text()

    recommendations = []
    current_priority = None

    # Parse sections by priority
    for line in content.split('\n'):
        # Detect priority section
        if line.startswith('## 🔴🔴 Priorité TRÈS HAUTE'):
            current_priority = '🔴🔴'
        elif line.startswith('## 🔴 Priorité HAUTE'):
            current_priority = '🔴'
        elif line.startswith('## 🟡 Priorité MOYENNE'):
            current_priority = '🟡'
        elif line.startswith('## 🟢 Priorité BASSE'):
            current_priority = '🟢'

        # Parse recommendation item
        if line.startswith('- [ ] **CNT-014-R'):
            # Extract rec ID and title
            match = re.match(r'- \[ \] \*\*(CNT-014-R\d+) - (.+)\*\*', line)
            if match and current_priority:
                rec_id = match.group(1)
                title = match.group(2)
                recommendations.append({
                    'id': rec_id,
                    'title': title,
                    'priority': current_priority,
                    'priority_name': {
                        '🔴🔴': 'TRÈS HAUTE',
                        '🔴': 'HAUTE',
                        '🟡': 'MOYENNE',
                        '🟢': 'BASSE'
                    }.get(current_priority, 'INCONNUE')
                })

    return recommendations

def main():
    rec_file = Path('.tasks/resources/analyses/CNT-014/recommendations-status.md')

    if not rec_file.exists():
        print(f"❌ Fichier introuvable: {rec_file}")
        return 1

    recs = parse_recommendations(rec_file)

    # Filter high priority (very high + high)
    high_priority = [r for r in recs if r['priority'] in ['🔴🔴', '🔴']]

    print(f"\n{'='*70}")
    print(f"Recommandations prioritaires CNT-014 (TRÈS HAUTE + HAUTE)")
    print(f"{'='*70}\n")

    # Group by priority
    very_high = [r for r in high_priority if r['priority'] == '🔴🔴']
    high = [r for r in high_priority if r['priority'] == '🔴']

    if very_high:
        print(f"🔴🔴 TRÈS HAUTE ({len(very_high)} recommandations):\n")
        for i, rec in enumerate(very_high, 1):
            print(f"  {i}. [{rec['id']}] {rec['title']}")
        print()

    if high:
        print(f"🔴 HAUTE ({len(high)} recommandations):\n")
        for i, rec in enumerate(high, len(very_high) + 1):
            print(f"  {i}. [{rec['id']}] {rec['title']}")
        print()

    print(f"{'='*70}")
    print(f"Total: {len(high_priority)} recommandations prioritaires")
    print(f"  - {len(very_high)} TRÈS HAUTE")
    print(f"  - {len(high)} HAUTE")
    print(f"{'='*70}\n")

    return 0

if __name__ == '__main__':
    exit(main())
