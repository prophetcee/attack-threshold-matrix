from dataclasses import dataclass

from .calculations import effective_attack
from .models import AttackPath


@dataclass(frozen=True)
class ThresholdPolicy:
    warning_margin: float = -64
    critical_margin: float = -32


def classify_margin(
    margin_value: float,
    policy: ThresholdPolicy,
) -> str:
    if margin_value <= policy.critical_margin:
        return "CRITICAL"

    if margin_value <= policy.warning_margin:
        return "WARNING"

    return "NORMAL"


def system_status(
    search_exponent: float,
    attacks: list[AttackPath],
    policy: ThresholdPolicy | None = None,
) -> dict:
    policy = policy or ThresholdPolicy()
    attack = effective_attack(attacks)
    system_margin = attack.cost_exponent - search_exponent

    return {
        "effective_attack": attack.name,
        "effective_category": attack.category,
        "system_margin": system_margin,
        "status": classify_margin(system_margin, policy),
    }
