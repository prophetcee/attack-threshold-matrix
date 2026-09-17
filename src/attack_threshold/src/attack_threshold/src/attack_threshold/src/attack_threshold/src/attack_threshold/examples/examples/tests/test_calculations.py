from attack_threshold.calculations import (
    attack_deltas,
    attack_margins,
    delta,
    effective_attack,
    margin,
)
from attack_threshold.models import AttackPath
from attack_threshold.trajectory import (
    analyze_trajectory,
    transition_points,
)


def test_delta_and_margin_are_opposites():
    attack = AttackPath("Test", 100)

    assert delta(256, attack) == 156
    assert margin(256, attack) == -156


def test_effective_attack_is_minimum_cost():
    attacks = [
        AttackPath("Expensive", 200),
        AttackPath("Cheap", 100),
        AttackPath("Medium", 150),
    ]

    assert effective_attack(attacks).name == "Cheap"


def test_empty_attack_list_is_rejected():
    try:
        effective_attack([])
    except ValueError as exc:
        assert "At least one attack pathway" in str(exc)
    else:
        raise AssertionError("Expected ValueError")


def test_trajectory_transition_is_detected():
    snapshots = [
        {
            "label": "2026",
            "effective_attack": "Implementation",
            "effective_category": "implementation",
            "effective_cost_exponent": 120,
            "system_margin": -136,
        },
        {
            "label": "2027",
            "effective_attack": "Lattice",
            "effective_category": "lattice",
            "effective_cost_exponent": 175,
            "system_margin": -81,
        },
    ]

    transitions = transition_points(snapshots)

    assert transitions == [
        {
            "from": "Implementation",
            "to": "Lattice",
            "at": "2027",
        }
    ]


def test_attack_deltas_and_margins():
    attacks = [
        AttackPath("A", 100),
        AttackPath("B", 150),
    ]

    assert attack_deltas(200, attacks) == {
        "A": 100,
        "B": 50,
    }

    assert attack_margins(200, attacks) == {
        "A": -100,
        "B": -50,
    }


def test_trajectory_analysis():
    snapshots = [
        {
            "label": "2026",
            "attacks": (
                AttackPath("Implementation", 120, "implementation"),
                AttackPath("Lattice", 175, "lattice"),
            ),
        }
    ]

    # Convert to the actual Snapshot model used by the package.
    from attack_threshold.models import Snapshot

    actual_snapshots = [
        Snapshot(
            label=s["label"],
            attacks=s["attacks"],
        )
        for s in snapshots
    ]

    rows = analyze_trajectory(256, actual_snapshots)

    assert rows[0]["effective_attack"] == "Implementation"
    assert rows[0]["effective_cost_exponent"] == 120
    assert rows[0]["system_margin"] == -136
