"""Tests for recommendation_parser.py"""

from pathlib import Path

import pytest

from scripts.task_management.analysis.recommendation_parser import (
    Recommendation,
    parse_priority_header,
    parse_recommendation_item,
    parse_recommendations_file,
    find_pending_recommendations,
    group_by_priority,
    filter_by_priority,
    update_recommendation_status,
)


# ============================================================================
# Test Data
# ============================================================================

SAMPLE_RECOMMENDATIONS_FILE = """# Recommendations Status - CNT-001

## 🔴🔴 Priorité Très Haute

- [ ] **R01 - Corriger l'écart critique sur Upwiser**
  - Catégorie: Date incohérence
  - Source: [recommendations.md](./recommendations.md#r01)
  - Référence CV: [src/cv.typ:122](../../../src/cv.typ#L122)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

## 🔴 Priorité Haute

- [x] **R02 - Corriger les dates Freelance**
  - Catégorie: Date incohérence
  - Source: [recommendations.md](./recommendations.md#r02)
  - Référence CV: [src/cv.typ:169](../../../src/cv.typ#L169)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: [CNT-005](../../tasks/CNT-005-corriger-dates-freelance.md)
  - Statut: ✅ Task Created

- [ ] **R03 - Ajouter certifications manquantes**
  - Catégorie: Missing Content
  - Source: [recommendations.md](./recommendations.md#r03)
  - Référence CV: [src/cv.typ:220-250](../../../src/cv.typ#L220-L250)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

## 🟡 Priorité Moyenne

- [ ] **R04 - Ajouter langue Espagnol**
  - Catégorie: Missing Content
  - Source: [recommendations.md](./recommendations.md#r04)
  - Référence CV: [src/cv.typ:66](../../../src/cv.typ#L66)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending

## 🟢 Priorité Basse

- [ ] **R05 - Optimiser section bénévolat**
  - Catégorie: Content Enhancement
  - Source: [recommendations.md](./recommendations.md#r05)
  - Référence CV: [src/cv.typ:180](../../../src/cv.typ#L180)
  - Trigramme suggéré: CNT
  - Date ajout: 2025-10-29
  - Tâche créée: -
  - Statut: ⏳ Pending
"""


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture
def temp_recommendations_file(tmp_path):
    """Create a temporary recommendations-status.md file."""
    file_path = tmp_path / "recommendations-status.md"
    file_path.write_text(SAMPLE_RECOMMENDATIONS_FILE, encoding='utf-8')
    return file_path


# ============================================================================
# Priority Header Parsing
# ============================================================================

def test_parse_priority_header_very_high():
    """Test parsing very high priority header."""
    result = parse_priority_header("## 🔴🔴 Priorité Très Haute")
    assert result is not None
    assert result['emoji'] == '🔴🔴'
    assert result['level'] == 'very_high'
    assert result['order'] == 0


def test_parse_priority_header_high():
    """Test parsing high priority header."""
    result = parse_priority_header("## 🔴 Priorité Haute")
    assert result is not None
    assert result['emoji'] == '🔴'
    assert result['level'] == 'high'


def test_parse_priority_header_medium():
    """Test parsing medium priority header."""
    result = parse_priority_header("## 🟡 Priorité Moyenne")
    assert result is not None
    assert result['emoji'] == '🟡'
    assert result['level'] == 'medium'


def test_parse_priority_header_low():
    """Test parsing low priority header."""
    result = parse_priority_header("## 🟢 Priorité Basse")
    assert result is not None
    assert result['emoji'] == '🟢'
    assert result['level'] == 'low'


def test_parse_priority_header_invalid():
    """Test parsing invalid header."""
    result = parse_priority_header("# Not a priority header")
    assert result is None


# ============================================================================
# Recommendation Item Parsing
# ============================================================================

def test_parse_recommendation_item_pending():
    """Test parsing a pending recommendation item."""
    lines = SAMPLE_RECOMMENDATIONS_FILE.split('\n')
    priority_info = {'emoji': '🔴🔴', 'level': 'very_high', 'order': 0}

    # Find the R01 line
    start_idx = next(i for i, line in enumerate(lines) if '**R01 -' in line)

    rec = parse_recommendation_item(lines, start_idx, priority_info, 'CNT-001')

    assert rec is not None
    assert rec.rec_id == 'R01'
    assert rec.full_id == 'CNT-001-R01'
    assert rec.title == "Corriger l'écart critique sur Upwiser"
    assert rec.priority_emoji == '🔴🔴'
    assert rec.category == 'Date incohérence'
    assert rec.trigramme == 'CNT'
    assert rec.date_added == '2025-10-29'
    assert rec.task_created is None
    assert rec.status == '⏳ Pending'
    assert rec.is_completed is False


def test_parse_recommendation_item_completed():
    """Test parsing a completed recommendation item."""
    lines = SAMPLE_RECOMMENDATIONS_FILE.split('\n')
    priority_info = {'emoji': '🔴', 'level': 'high', 'order': 1}

    # Find the R02 line (completed)
    start_idx = next(i for i, line in enumerate(lines) if '**R02 -' in line)

    rec = parse_recommendation_item(lines, start_idx, priority_info, 'CNT-001')

    assert rec is not None
    assert rec.rec_id == 'R02'
    assert rec.is_completed is True
    assert rec.status == '✅ Task Created'
    assert rec.task_created == '[CNT-005](../../tasks/CNT-005-corriger-dates-freelance.md)'


# ============================================================================
# File Parsing
# ============================================================================

def test_parse_recommendations_file(temp_recommendations_file):
    """Test parsing full recommendations file."""
    recommendations = parse_recommendations_file(temp_recommendations_file, 'CNT-001')

    assert len(recommendations) == 5
    assert recommendations[0].rec_id == 'R01'
    assert recommendations[1].rec_id == 'R02'
    assert recommendations[2].rec_id == 'R03'
    assert recommendations[3].rec_id == 'R04'
    assert recommendations[4].rec_id == 'R05'


def test_parse_recommendations_file_not_found():
    """Test parsing non-existent file."""
    with pytest.raises(FileNotFoundError):
        parse_recommendations_file(Path('/nonexistent/file.md'), 'CNT-001')


# ============================================================================
# Filtering
# ============================================================================

def test_find_pending_recommendations(temp_recommendations_file):
    """Test finding pending recommendations."""
    all_recs = parse_recommendations_file(temp_recommendations_file, 'CNT-001')
    pending = find_pending_recommendations(all_recs)

    assert len(pending) == 4  # R01, R03, R04, R05 (not R02 which is completed)
    assert all(r.status == '⏳ Pending' for r in pending)
    assert all(not r.is_completed for r in pending)


def test_filter_by_priority_all(temp_recommendations_file):
    """Test filter with 'all'."""
    all_recs = parse_recommendations_file(temp_recommendations_file, 'CNT-001')
    filtered = filter_by_priority(all_recs, 'all')

    assert len(filtered) == 5


def test_filter_by_priority_critical(temp_recommendations_file):
    """Test filter with 'critical' (very high only)."""
    all_recs = parse_recommendations_file(temp_recommendations_file, 'CNT-001')
    filtered = filter_by_priority(all_recs, 'critical')

    assert len(filtered) == 1
    assert filtered[0].rec_id == 'R01'
    assert filtered[0].priority_emoji == '🔴🔴'


def test_filter_by_priority_high(temp_recommendations_file):
    """Test filter with 'high' (very high + high)."""
    all_recs = parse_recommendations_file(temp_recommendations_file, 'CNT-001')
    filtered = filter_by_priority(all_recs, 'high')

    assert len(filtered) == 3  # R01, R02, R03
    assert all(r.priority_emoji in ['🔴🔴', '🔴'] for r in filtered)


def test_filter_by_priority_medium(temp_recommendations_file):
    """Test filter with 'medium'."""
    all_recs = parse_recommendations_file(temp_recommendations_file, 'CNT-001')
    filtered = filter_by_priority(all_recs, 'medium')

    assert len(filtered) == 1
    assert filtered[0].rec_id == 'R04'
    assert filtered[0].priority_emoji == '🟡'


def test_filter_by_priority_low(temp_recommendations_file):
    """Test filter with 'low'."""
    all_recs = parse_recommendations_file(temp_recommendations_file, 'CNT-001')
    filtered = filter_by_priority(all_recs, 'low')

    assert len(filtered) == 1
    assert filtered[0].rec_id == 'R05'
    assert filtered[0].priority_emoji == '🟢'


# ============================================================================
# Grouping
# ============================================================================

def test_group_by_priority(temp_recommendations_file):
    """Test grouping recommendations by priority."""
    all_recs = parse_recommendations_file(temp_recommendations_file, 'CNT-001')
    groups = group_by_priority(all_recs)

    assert len(groups['🔴🔴']) == 1  # R01
    assert len(groups['🔴']) == 2   # R02, R03
    assert len(groups['🟡']) == 1   # R04
    assert len(groups['🟢']) == 1   # R05


# ============================================================================
# Status Updates
# ============================================================================

def test_update_recommendation_status(temp_recommendations_file):
    """Test updating recommendation status after task creation."""
    # Update R01
    result = update_recommendation_status(
        temp_recommendations_file,
        'R01',
        'CNT-010',
        'CNT-010-corriger-ecart-critique.md'
    )

    assert result is True

    # Re-parse and verify
    recs = parse_recommendations_file(temp_recommendations_file, 'CNT-001')
    r01 = next(r for r in recs if r.rec_id == 'R01')

    assert r01.is_completed is True
    assert r01.status == '✅ Task Created'
    assert 'CNT-010' in r01.task_created


def test_update_recommendation_status_not_found(temp_recommendations_file):
    """Test updating non-existent recommendation."""
    result = update_recommendation_status(
        temp_recommendations_file,
        'R99',  # Doesn't exist
        'CNT-010',
        'CNT-010-test.md'
    )

    assert result is False


def test_update_recommendation_status_file_not_found():
    """Test updating in non-existent file."""
    with pytest.raises(FileNotFoundError):
        update_recommendation_status(
            Path('/nonexistent/file.md'),
            'R01',
            'CNT-010',
            'CNT-010-test.md'
        )
