"""WSJF (Weighted Shortest Job First) scoring algorithm.

CUPID: Predictable - pure functions with no side effects.
CUPID: Composable - functions can be combined freely.
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class WSJFConfig:
    """WSJF algorithm configuration.

    Default values match update_priority_scores.py reference implementation.
    """

    age_divisor: float = 20.0
    age_max: float = 2.5
    urgency_overdue: float = 10.0
    urgency_week: float = 5.0
    urgency_month: float = 2.0
    default_hours: float = 4.0


def calculate_urgency(
    target: Optional[date],
    today: date,
    config: WSJFConfig,
) -> float:
    """Calculate urgency score based on target date proximity.

    Args:
        target: Target/due date or None
        today: Current date
        config: WSJF configuration

    Returns:
        Urgency score (0.0 to urgency_overdue)
    """
    if target is None:
        return 0.0
    days_until = (target - today).days
    if days_until < 0:
        return config.urgency_overdue
    if days_until < 7:
        return config.urgency_week
    if days_until < 30:
        return config.urgency_month
    return 0.0


def calculate_age(
    created: Optional[date],
    today: date,
    config: WSJFConfig,
) -> float:
    """Calculate age score based on task age in days.

    Args:
        created: Creation date or None
        today: Current date
        config: WSJF configuration

    Returns:
        Age score (0.0 to age_max)
    """
    if created is None:
        return 0.0
    days_old = (today - created).days
    return min(days_old / config.age_divisor, config.age_max)


def calculate_wsjf_score(
    priority_score: float,
    urgency: float,
    age: float,
    time_hours: float,
    config: WSJFConfig,
) -> float:
    """Calculate WSJF score: (priority + urgency + age) / time.

    Args:
        priority_score: Priority value (higher = more important)
        urgency: Urgency score from calculate_urgency
        age: Age score from calculate_age
        time_hours: Estimated time in hours
        config: WSJF configuration

    Returns:
        WSJF score rounded to 2 decimal places
    """
    if time_hours <= 0:
        time_hours = config.default_hours
    total_value = priority_score + urgency + age
    return round(total_value / time_hours, 2)
