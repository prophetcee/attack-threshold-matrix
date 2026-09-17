from typing import Iterable

from .models import AttackPath


def delta(search_exponent: float, attack: AttackPath) -> float:
    return search_exponent - attack.cost_exponent


def margin(search_exponent: float, attack: AttackPath) -> float:
    return attack.cost_exponent - search_exponent


def effective_attack(attacks: Iterable[AttackPath]) -> AttackPath:
    attacks = list(attacks)
    if not attacks:
        raise ValueError("At least one attack pathway is required.")
    return min(attacks, key=lambda attack: attack.cost_exponent)


def attack_deltas(
    search_exponent: float,
    attacks: Iterable[AttackPath],
) -> dict[str, float]:
    return {a.name: delta(search_exponent, a) for a in attacks}


def attack_margins(
    search_exponent: float,
    attacks: Iterable[AttackPath],
) -> dict[str, float]:
    return {a.name: margin(search_exponent, a) for a in attacks}
