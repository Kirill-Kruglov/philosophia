# WALLB_POLICY_CHANNEL_AUDIT_14

NON-CITABLE preregistered policy-channel audit. No ACTIVE/YOKED learner was
instantiated. Library macros are absent from both arms; only beam order differs.

## VERDICT: POSITIVE_CONTROL_FAIL

Positive control on `21b64bd46791` (leaking oracle trained on
evaluation witness paths): FAIL. gains/losses=
0/0,
solve-rate delta=0.000,
CONTROL rate/RM=0.32 / 134,
TREATMENT rate/RM=0.32 / 134,
raw McNemar p=1,
RM gain=0.00 at B=162.
Reasons: SOLVE_RATE_GAIN_BELOW_010, RESTRICTED_MEAN_GAIN_BELOW_005B, MCNEMAR_RAW_ABOVE_0001, NO_SOLVE_RATE_IMPROVEMENT.

Under frozen beam width W=32, CONTROL and TREATMENT produced
identical paired evaluation outcomes. The forty-world frame was not drawn.
Implementation size: 1187 nonblank lines.
Preregistration commit: `ec77d3719ea2de345e3b2b7313a8ca696c008073`.

This is an instrument-power failure, not a prevalence estimate. No world
contract, ACTIVE/YOKED arm or scientific claim is authorized.
