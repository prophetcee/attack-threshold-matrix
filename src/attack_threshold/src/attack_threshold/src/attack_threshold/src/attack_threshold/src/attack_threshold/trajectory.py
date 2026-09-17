from .models import Snapshot
from .calculations import effective_attack


def analyze_trajectory(
    search_exponent: float,
    snapshots: list[Snapshot],
) -> list[dict]:
    rows = []

    for snap in snapshots:
        attack = effective_attack(snap.attacks)

        rows.append(
            {
                "label": snap.label,
                "effective_attack": attack.name,
                "effective_category": attack.category,
                "effective_cost_exponent": attack.cost_exponent,
                "system_margin": attack.cost_exponent - search_exponent,
            }
        )

    return rows


def transition_points(rows: list[dict]) -> list[dict]:
    transitions = []

    for previous, current in zip(rows, rows[1:]):
        if previous["effective_attack"] != current["effective_attack"]:
            transitions.append(
                {
                    "from": previous["effective_attack"],
                    "to": current["effective_attack"],
                    "at": current["label"],
                }
            )

    return transitions
