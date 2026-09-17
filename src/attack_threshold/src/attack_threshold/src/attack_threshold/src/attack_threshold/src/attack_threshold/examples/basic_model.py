from attack_threshold.calculations import attack_deltas
from attack_threshold.models import AttackPath
from attack_threshold.thresholds import system_status


SEARCH_EXPONENT = 256

attacks = [
    AttackPath(
        name="Brute Force",
        cost_exponent=256,
        category="classical",
    ),
    AttackPath(
        name="Classical Cryptanalytic",
        cost_exponent=190,
        category="cryptanalytic",
    ),
    AttackPath(
        name="Quantum",
        cost_exponent=160,
        category="quantum",
    ),
    AttackPath(
        name="Lattice",
        cost_exponent=175,
        category="lattice",
    ),
    AttackPath(
        name="Implementation",
        cost_exponent=120,
        category="implementation",
    ),
]

print("Attack Threshold Matrix")
print("=======================")

for name, value in attack_deltas(SEARCH_EXPONENT, attacks).items():
    print(f"{name:28} Δ = {value}")

status = system_status(SEARCH_EXPONENT, attacks)

print("\nSystem status")
print("-------------")
print(f"Effective attack: {status['effective_attack']}")
print(f"Category:         {status['effective_category']}")
print(f"System margin:    {status['system_margin']}")
print(f"Status:           {status['status']}")
