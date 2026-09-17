# Attack Threshold Matrix (ATM)

An experimental Python framework for comparing competing attack-cost estimates and tracking their logarithmic distance from a configurable security baseline.

## Research question

Does a dynamic logarithmic attack-threshold metric provide information about changing security conditions that is not captured by a static minimum-cost security estimate?

ATM does **not** claim to break AES-256, predict future attacks, or establish a new cryptographic security standard. Attack-cost estimation and minimum-cost selection are established practices. This project tests whether a normalized, time-varying representation adds useful information.

## Model

For a baseline search space represented as `2^S` and an attack pathway estimated at `2^C`:

`Δ = S - C`

`M = C - S = -Δ`

The effective attack is the pathway with minimum estimated cost:

`C_effective = min(C_1, C_2, ..., C_n)`

ATM additionally records the trajectory of those costs over time.

## Run

```bash
python examples/basic_model.py
python examples/trajectory_experiment.py
pytest
```

All example attack costs are synthetic. Thresholds are experimental parameters, not cryptographic standards.

## License

MIT
