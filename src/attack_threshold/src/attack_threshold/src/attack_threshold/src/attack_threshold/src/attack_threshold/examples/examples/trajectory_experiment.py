from attack_threshold.models import AttackPath, Snapshot
from attack_threshold.trajectory import (
    analyze_trajectory,
    transition_points,
)


SEARCH_EXPONENT = 256

snapshots = [
    Snapshot(
        label="2026",
        attacks=(
            AttackPath("Implementation", 120, "implementation"),
            AttackPath("Lattice", 175, "lattice"),
            AttackPath("Quantum", 190, "quantum"),
        ),
    ),
    Snapshot(
        label="2027",
        attacks=(
            AttackPath("Implementation", 150, "implementation"),
            AttackPath("Lattice", 175, "lattice"),
            AttackPath("Quantum", 190, "quantum"),
        ),
    ),
    Snapshot(
        label="2028",
        attacks=(
            AttackPath("Implementation", 180, "implementation"),
            AttackPath("Lattice", 175, "lattice"),
            AttackPath("Quantum", 190, "quantum"),
        ),
    ),
    Snapshot(
        label="2029",
        attacks=(
            AttackPath("Implementation", 190, "implementation"),
            AttackPath("Lattice", 184, "lattice"),
            AttackPath("Quantum", 190, "quantum"),
        ),
    ),
    Snapshot(
        label="2030",
        attacks=(
            AttackPath("Implementation", 190, "implementation"),
            AttackPath("Lattice", 185, "lattice"),
            AttackPath("Quantum", 180, "quantum"),
        ),
    ),
]

rows = analyze_trajectory(SEARCH_EXPONENT, snapshots)

print("ATM Attack Trajectory")
print("=====================")

for row in rows:
    print(
        f"{row['label']}: "
        f"{row['effective_attack']} "
        f"(2^{row['effective_cost_exponent']}) "
        f"margin={row['system_margin']}"
    )

print("\nTransitions")
print("-----------")

for transition in transition_points(rows):
    print(
        f"{transition['at']}: "
        f"{transition['from']} -> {transition['to']}"
    )
