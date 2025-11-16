"""Configuration loader with YAML parsing and Python validation.

This module loads configuration from YAML files and validates them using
Python dataclasses. Configurations are cached in memory for performance.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Literal
import os
import yaml


# ============================================================================
# Dataclass Definitions
# ============================================================================

@dataclass
class PriorityLevel:
    """Single priority level configuration."""
    emoji: str
    score: int
    default_time_hours: float


@dataclass
class PriorityConfig:
    """Task priority configuration."""
    high: PriorityLevel
    medium: PriorityLevel
    low: PriorityLevel


@dataclass
class AnalysisPriorityLevel:
    """Analysis priority level (from recommendations)."""
    emoji: str
    maps_to: Literal["high", "medium", "low"]


@dataclass
class AnalysisPriorityConfig:
    """Analysis priority mapping configuration."""
    very_high: AnalysisPriorityLevel
    high: AnalysisPriorityLevel
    medium: AnalysisPriorityLevel
    low: AnalysisPriorityLevel


@dataclass
class UrgencyScores:
    """Urgency scoring for WSJF algorithm."""
    overdue: int
    week: int
    month: int
    none: int


@dataclass
class Trigramme:
    """Single trigramme configuration."""
    name: str
    description: str
    default_section: str
    requires_branch: Literal["auto", "yes", "no"]


@dataclass
class PathsConfig:
    """File paths configuration."""
    # Task management
    tasks_root: str
    tasks_dir: str
    archived_dir: str
    tasks_dashboard: str
    tasks_ideas: str
    task_rules: str
    task_template: str

    # Analysis
    analysis_root: str
    audits_dir: str
    analyses_dir: str
    templates_dir: str
    analyses_dashboard: str

    # Skill
    skill_root: str
    skill_config_dir: str
    skill_scripts_dir: str
    skill_templates_dir: str
    skill_workflows_dir: str
    skill_tests_dir: str

    # CV
    cv_source: str
    cv_output: str

    # Git
    git_branch_prefix: str
    git_main_branch: str


# ============================================================================
# Global Cache
# ============================================================================

_cache: Dict[str, any] = {}


# ============================================================================
# Helper Functions
# ============================================================================

def _get_config_path(filename: str) -> Path:
    """Get path to config file."""
    # Assume we're in scripts/core/, so config is ../../config/
    return Path(__file__).parent.parent.parent / "config" / filename


def _load_yaml(filename: str) -> dict:
    """Load and parse YAML file."""
    path = _get_config_path(filename)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


# ============================================================================
# Config Loaders
# ============================================================================

def load_priorities() -> tuple[PriorityConfig, AnalysisPriorityConfig, UrgencyScores]:
    """Load priority configuration from priorities.yml.

    Returns:
        Tuple of (task_priorities, analysis_priorities, urgency_scores)

    Raises:
        FileNotFoundError: If priorities.yml not found
        KeyError: If required keys missing in YAML
        TypeError: If data types don't match dataclass
    """
    cache_key = 'priorities'

    if cache_key in _cache:
        return _cache[cache_key]

    data = _load_yaml('priorities.yml')

    # Parse task priorities
    task_prio = PriorityConfig(
        high=PriorityLevel(**data['task_priorities']['high']),
        medium=PriorityLevel(**data['task_priorities']['medium']),
        low=PriorityLevel(**data['task_priorities']['low'])
    )

    # Parse analysis priorities
    analysis_prio = AnalysisPriorityConfig(
        very_high=AnalysisPriorityLevel(**data['analysis_priorities']['very_high']),
        high=AnalysisPriorityLevel(**data['analysis_priorities']['high']),
        medium=AnalysisPriorityLevel(**data['analysis_priorities']['medium']),
        low=AnalysisPriorityLevel(**data['analysis_priorities']['low'])
    )

    # Parse urgency scores
    urgency = UrgencyScores(**data['urgency_scores'])

    result = (task_prio, analysis_prio, urgency)
    _cache[cache_key] = result

    return result


def load_trigrammes() -> tuple[Dict[str, Trigramme], list[str]]:
    """Load trigramme configuration from trigrammes.yml.

    Returns:
        Tuple of (trigrammes_dict, cv_sections_list)

    Raises:
        FileNotFoundError: If trigrammes.yml not found
        KeyError: If required keys missing in YAML
    """
    cache_key = 'trigrammes'

    if cache_key in _cache:
        return _cache[cache_key]

    data = _load_yaml('trigrammes.yml')

    # Parse trigrammes
    trigrammes = {
        code: Trigramme(**config)
        for code, config in data['trigrammes'].items()
    }

    # Get CV sections
    cv_sections = data['cv_sections']

    result = (trigrammes, cv_sections)
    _cache[cache_key] = result

    return result


def load_paths() -> PathsConfig:
    """Load file paths configuration from paths.yml.

    Supports environment variable overrides for isolated testing:
    - TASK_SYSTEM_TASKS_DIR: Override tasks directory
    - TASK_SYSTEM_ARCHIVED_DIR: Override archived directory
    - TASK_SYSTEM_DASHBOARD: Override TASKS.md path

    Returns:
        PathsConfig instance

    Raises:
        FileNotFoundError: If paths.yml not found
        KeyError: If required keys missing in YAML
    """
    cache_key = 'paths'

    if cache_key in _cache:
        return _cache[cache_key]

    data = _load_yaml('paths.yml')

    # Apply environment variable overrides for testing
    if 'TASK_SYSTEM_TASKS_DIR' in os.environ:
        data['tasks']['tasks_dir'] = os.environ['TASK_SYSTEM_TASKS_DIR']
    if 'TASK_SYSTEM_ARCHIVED_DIR' in os.environ:
        data['tasks']['archived_dir'] = os.environ['TASK_SYSTEM_ARCHIVED_DIR']
    if 'TASK_SYSTEM_DASHBOARD' in os.environ:
        data['tasks']['dashboard'] = os.environ['TASK_SYSTEM_DASHBOARD']

    # Flatten nested structure
    config = PathsConfig(
        # Tasks
        tasks_root=data['tasks']['root'],
        tasks_dir=data['tasks']['tasks_dir'],
        archived_dir=data['tasks']['archived_dir'],
        tasks_dashboard=data['tasks']['dashboard'],
        tasks_ideas=data['tasks']['ideas'],
        task_rules=data['tasks']['task_rules'],
        task_template=data['tasks']['template'],

        # Analysis
        analysis_root=data['analysis']['root'],
        audits_dir=data['analysis']['audits_dir'],
        analyses_dir=data['analysis']['analyses_dir'],
        templates_dir=data['analysis']['templates_dir'],
        analyses_dashboard=data['analysis']['dashboard'],

        # Skill
        skill_root=data['skill']['root'],
        skill_config_dir=data['skill']['config_dir'],
        skill_scripts_dir=data['skill']['scripts_dir'],
        skill_templates_dir=data['skill']['templates_dir'],
        skill_workflows_dir=data['skill']['workflows_dir'],
        skill_tests_dir=data['skill']['tests_dir'],

        # CV
        cv_source=data['cv']['source'],
        cv_output=data['cv']['output'],

        # Git
        git_branch_prefix=data['git']['branch_prefix'],
        git_main_branch=data['git']['main_branch']
    )

    _cache[cache_key] = config
    return config


def get_priority_emoji(priority: str) -> str:
    """Get emoji for a priority level (high/medium/low).

    Args:
        priority: Priority level string

    Returns:
        Emoji string (e.g., "🔴", "🟡", "🟢")

    Raises:
        ValueError: If priority not recognized
    """
    task_prio, _, _ = load_priorities()

    priority_lower = priority.lower()

    if priority_lower in ('haute', 'high', 'h'):
        return task_prio.high.emoji
    elif priority_lower in ('moyenne', 'medium', 'm'):
        return task_prio.medium.emoji
    elif priority_lower in ('basse', 'low', 'l'):
        return task_prio.low.emoji
    else:
        raise ValueError(f"Unknown priority: {priority}")


def get_priority_score(priority: str) -> int:
    """Get numeric score for a priority level.

    Args:
        priority: Priority level string or emoji (e.g., "🔴 Haute", "Moyenne", "🟢")

    Returns:
        Numeric score (10, 5, or 2)

    Raises:
        ValueError: If priority not recognized
    """
    task_prio, _, _ = load_priorities()

    # Normalize: lowercase and check if contains emoji or keywords
    priority_lower = priority.lower()

    # High priority
    if any(x in priority_lower for x in ['haute', 'high', 'h']) or task_prio.high.emoji in priority:
        return task_prio.high.score
    # Medium priority
    elif any(x in priority_lower for x in ['moyenne', 'medium', 'm']) or task_prio.medium.emoji in priority:
        return task_prio.medium.score
    # Low priority
    elif any(x in priority_lower for x in ['basse', 'low', 'l', 'bas']) or task_prio.low.emoji in priority:
        return task_prio.low.score
    else:
        raise ValueError(f"Unknown priority: {priority}")


def clear_cache():
    """Clear configuration cache. Useful for testing."""
    global _cache
    _cache = {}


# ============================================================================
# CLI for Testing
# ============================================================================

if __name__ == '__main__':
    """Test configuration loading."""
    print("Testing config_loader.py")
    print("=" * 60)

    print("\n1. Loading priorities...")
    task_prio, analysis_prio, urgency = load_priorities()
    print(f"   High priority: {task_prio.high.emoji} (score: {task_prio.high.score})")
    print(f"   Medium priority: {task_prio.medium.emoji} (score: {task_prio.medium.score})")
    print(f"   Low priority: {task_prio.low.emoji} (score: {task_prio.low.score})")
    print(f"   Urgency overdue: {urgency.overdue} points")

    print("\n2. Loading trigrammes...")
    trigrammes, cv_sections = load_trigrammes()
    print(f"   Found {len(trigrammes)} trigrammes:")
    for code, trig in trigrammes.items():
        print(f"   - {code}: {trig.name} (branch: {trig.requires_branch})")

    print("\n3. Loading paths...")
    paths = load_paths()
    print(f"   Tasks dir: {paths.tasks_dir}")
    print(f"   Dashboard: {paths.tasks_dashboard}")
    print(f"   CV source: {paths.cv_source}")

    print("\n4. Testing helpers...")
    print(f"   get_priority_emoji('high') = {get_priority_emoji('high')}")
    print(f"   get_priority_score('🟡') = {get_priority_score('🟡')}")

    print("\n✅ All configs loaded successfully!")
    print("=" * 60)
