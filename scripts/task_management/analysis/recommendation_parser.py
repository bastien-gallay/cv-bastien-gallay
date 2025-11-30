"""Recommendation parser for analysis tracking.

This module provides functions to parse recommendations-status.md files,
extract pending recommendations, and update recommendation statuses when tasks are created.
"""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from scripts.task_management.core.config_loader import load_paths


# ============================================================================
# Data Structures
# ============================================================================

@dataclass
class Recommendation:
    """Single recommendation from analysis."""
    analysis_id: str  # e.g., 'CNT-001'
    rec_id: str       # e.g., 'R01'
    full_id: str      # e.g., 'CNT-001-R01'
    title: str        # e.g., 'Corriger l'écart critique sur Upwiser'
    priority: str     # e.g., '🔴🔴 Très Haute', '🔴 Haute'
    priority_emoji: str  # e.g., '🔴🔴', '🔴', '🟡', '🟢'
    category: Optional[str] = None
    source_link: Optional[str] = None
    cv_reference: Optional[str] = None
    trigramme: Optional[str] = None
    date_added: Optional[str] = None
    task_created: Optional[str] = None
    status: str = '⏳ Pending'
    is_completed: bool = False  # Based on checkbox [x] vs [ ]


# ============================================================================
# Priority Mapping
# ============================================================================

PRIORITY_HEADERS = {
    '🔴🔴 Priorité Très Haute': {'emoji': '🔴🔴', 'level': 'very_high', 'order': 0},
    '🔴 Priorité Haute': {'emoji': '🔴', 'level': 'high', 'order': 1},
    '🟡 Priorité Moyenne': {'emoji': '🟡', 'level': 'medium', 'order': 2},
    '🟢 Priorité Basse': {'emoji': '🟢', 'level': 'low', 'order': 3},
}


def parse_priority_header(line: str) -> Optional[Dict]:
    """Parse priority header line.

    Args:
        line: Line to parse (e.g., '## 🔴 Priorité Haute')

    Returns:
        Priority info dict or None
    """
    if not line.startswith('##'):
        return None

    for header, info in PRIORITY_HEADERS.items():
        if header in line:
            return info

    return None


# ============================================================================
# Recommendation Parsing
# ============================================================================

def parse_recommendation_item(lines: List[str], start_idx: int, current_priority: Dict,
                              analysis_id: str) -> Optional[Recommendation]:
    """Parse a single recommendation item from lines.

    Args:
        lines: All lines from file
        start_idx: Index where recommendation starts (checkbox line)
        current_priority: Current priority section info
        analysis_id: Analysis ID (e.g., 'CNT-001')

    Returns:
        Recommendation object or None
    """
    # First line: - [ ] **R01 - Title**
    checkbox_line = lines[start_idx]

    # Check if completed
    is_completed = '[x]' in checkbox_line or '[X]' in checkbox_line

    # Extract R number and title
    match = re.search(r'\*\*R(\d+)\s*-\s*(.+?)\*\*', checkbox_line)
    if not match:
        return None

    rec_num = match.group(1)
    title = match.group(2).strip()

    rec_id = f"R{rec_num}"
    full_id = f"{analysis_id}-{rec_id}"

    # Initialize recommendation
    rec = Recommendation(
        analysis_id=analysis_id,
        rec_id=rec_id,
        full_id=full_id,
        title=title,
        priority=f"{current_priority['emoji']} {current_priority['level'].replace('_', ' ').title()}",
        priority_emoji=current_priority['emoji'],
        is_completed=is_completed
    )

    # Parse metadata fields (indented lines)
    i = start_idx + 1
    while i < len(lines) and lines[i].strip().startswith('-'):
        line = lines[i].strip()

        # Category
        if line.startswith('- Catégorie:'):
            rec.category = line.split(':', 1)[1].strip()

        # Source link
        elif line.startswith('- Source:'):
            rec.source_link = line.split(':', 1)[1].strip()

        # CV Reference
        elif line.startswith('- Référence CV:'):
            rec.cv_reference = line.split(':', 1)[1].strip()

        # Trigramme
        elif line.startswith('- Trigramme suggéré:'):
            rec.trigramme = line.split(':', 1)[1].strip()

        # Date added
        elif line.startswith('- Date ajout:'):
            rec.date_added = line.split(':', 1)[1].strip()

        # Task created
        elif line.startswith('- Tâche créée:'):
            task_info = line.split(':', 1)[1].strip()
            if task_info != '-':
                rec.task_created = task_info

        # Status
        elif line.startswith('- Statut:'):
            rec.status = line.split(':', 1)[1].strip()

        i += 1

    return rec


def parse_recommendations_file(file_path: Path, analysis_id: str) -> List[Recommendation]:
    """Parse recommendations-status.md file.

    Args:
        file_path: Path to recommendations-status.md
        analysis_id: Analysis ID (e.g., 'CNT-001')

    Returns:
        List of Recommendation objects
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Recommendations file not found: {file_path}")

    content = file_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    recommendations = []
    current_priority = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check for priority header
        priority_info = parse_priority_header(line)
        if priority_info:
            current_priority = priority_info
            i += 1
            continue

        # Check for recommendation item
        if line.strip().startswith('- [') and current_priority:
            rec = parse_recommendation_item(lines, i, current_priority, analysis_id)
            if rec:
                recommendations.append(rec)

        i += 1

    return recommendations


# ============================================================================
# Filtering and Grouping
# ============================================================================

def find_pending_recommendations(recommendations: List[Recommendation]) -> List[Recommendation]:
    """Filter recommendations that are pending (not completed).

    Args:
        recommendations: List of all recommendations

    Returns:
        List of pending recommendations
    """
    return [r for r in recommendations if not r.is_completed and r.status == '⏳ Pending']


def group_by_priority(recommendations: List[Recommendation]) -> Dict[str, List[Recommendation]]:
    """Group recommendations by priority level.

    Args:
        recommendations: List of recommendations

    Returns:
        Dict mapping priority emoji to list of recommendations
    """
    groups = {
        '🔴🔴': [],
        '🔴': [],
        '🟡': [],
        '🟢': []
    }

    for rec in recommendations:
        emoji = rec.priority_emoji
        if emoji in groups:
            groups[emoji].append(rec)

    return groups


def filter_by_priority(recommendations: List[Recommendation], priority_filter: str) -> List[Recommendation]:
    """Filter recommendations by priority.

    Args:
        recommendations: List of recommendations
        priority_filter: 'all', 'critical', 'high', 'medium', 'low'

    Returns:
        Filtered list of recommendations
    """
    if priority_filter == 'all':
        return recommendations

    filters = {
        'critical': ['🔴🔴'],
        'high': ['🔴🔴', '🔴'],
        'medium': ['🟡'],
        'low': ['🟢']
    }

    allowed_emojis = filters.get(priority_filter, [])
    return [r for r in recommendations if r.priority_emoji in allowed_emojis]


# ============================================================================
# Status Updates
# ============================================================================

def update_recommendation_status(file_path: Path, rec_id: str, task_id: str,
                                task_filename: str) -> bool:
    """Update recommendation status after task creation.

    Args:
        file_path: Path to recommendations-status.md
        rec_id: Recommendation ID (e.g., 'R01')
        task_id: Created task ID (e.g., 'CNT-005')
        task_filename: Task filename (e.g., 'CNT-005-corriger-ecart.md')

    Returns:
        True if successful
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Recommendations file not found: {file_path}")

    content = file_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    # Find the recommendation
    for i, line in enumerate(lines):
        # Match: - [ ] **R01 - Title**
        if f'**{rec_id} -' in line and line.strip().startswith('- ['):
            # Mark as completed
            lines[i] = line.replace('- [ ]', '- [x]').replace('- []', '- [x]')

            # Find and update the "Tâche créée" field
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith('-'):
                if lines[j].strip().startswith('- Tâche créée:'):
                    task_link = f"[{task_id}](../../tasks/{task_filename})"
                    lines[j] = f"  - Tâche créée: {task_link}"

                elif lines[j].strip().startswith('- Statut:'):
                    lines[j] = "  - Statut: ✅ Task Created"

                j += 1

            # Write back
            file_path.write_text('\n'.join(lines), encoding='utf-8')
            return True

    return False


# ============================================================================
# CLI for Testing
# ============================================================================

if __name__ == '__main__':
    """Test recommendation parser."""
    print("Testing recommendation_parser.py")
    print("=" * 60)

    # TODO: Add example test when we have a real recommendations-status.md file
    print("✅ Parser functions defined!")
    print("=" * 60)
