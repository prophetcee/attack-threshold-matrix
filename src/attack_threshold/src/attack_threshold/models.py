from dataclasses import dataclass


@dataclass(frozen=True)
class AttackPath:
    name: str
    cost_exponent: float
    category: str = "unknown"
    description: str = ""

    def __post_init__(self):
        if self.cost_exponent < 0:
            raise ValueError("cost_exponent must be non-negative.")


@dataclass(frozen=True)
class Snapshot:
    label: str
    attacks: tuple[AttackPath, ...]
