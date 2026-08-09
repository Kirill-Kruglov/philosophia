# WALLB_DESK_AUDIT_12D

NON-CITABLE powered mechanism screen. No ACTIVE/YOKED learner was instantiated.

## VERDICT: POWERED_SIGNAL_IN_1_OF_8_PENDING_PREREGISTERED_FRAME_AUDIT

Each presentation independently generates relevance, calibration and evaluation
panels of 192 goals; any observed overlap invalidates only that world-unit and
is reported. K=8
is the sole primary library size. B is selected only on the
calibration panel at target solve rate 0.40 +/- 0.05. Primary inference combines
one-sided exact McNemar with Holm FWER over the valid world-units,
restricted-mean gain >=0.05B and a conservative one-sided paired-bootstrap
lower bound at alpha=0.05/8. Holm over all eight units is retained as a
sensitivity analysis.
Implementation size: 856 nonblank lines.

### Primary powered screen

| presentation | B | cal rate | K=0 rate/RM | K=8 rate/RM | gains/losses | raw/Holm-valid/Holm-all p | RM gain/bootstrap lower | decision | reasons |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `39cb46a5584e` | 164 | 0.401 | 0.30 / 138 | 0.32 / 133 | 11/7 | 0.2403/n/a/1 | 5.16/1.19 | INVALID_UNIT | PANEL_GOAL_OVERLAP |
| `a8948b29abc8` | 297 | 0.401 | 0.44 / 226 | 0.43 / 220 | 13/15 | 0.7142/1/1 | 6.06/-0.42 | REJECT | NO_SOLVE_RATE_IMPROVEMENT, MCNEMAR_HOLM_NOT_SIGNIFICANT, RESTRICTED_MEAN_GAIN_BELOW_005B, PAIRED_BOOTSTRAP_LOWER_NOT_POSITIVE |
| `3ce31c0a0b4c` | 177 | 0.401 | 0.38 / 139 | 0.41 / 135 | 13/6 | 0.08353/0.4177/0.5847 | 4.59/0.60 | REJECT | MCNEMAR_HOLM_NOT_SIGNIFICANT, RESTRICTED_MEAN_GAIN_BELOW_005B |
| `6a89692d4f33` | 204 | 0.401 | 0.36 / 162 | 0.33 / 160 | 4/11 | 0.9824/1/1 | 2.54/-1.01 | REJECT | NO_SOLVE_RATE_IMPROVEMENT, MCNEMAR_HOLM_NOT_SIGNIFICANT, RESTRICTED_MEAN_GAIN_BELOW_005B, PAIRED_BOOTSTRAP_LOWER_NOT_POSITIVE |
| `f5b4899726d6` | 558 | 0.401 | 0.42 / 407 | 0.35 / 435 | 2/16 | 0.9999/1/1 | -27.85/-43.83 | REJECT | NO_SOLVE_RATE_IMPROVEMENT, MCNEMAR_HOLM_NOT_SIGNIFICANT, RESTRICTED_MEAN_GAIN_BELOW_005B, PAIRED_BOOTSTRAP_LOWER_NOT_POSITIVE |
| `3ac2b8840f14` | 792 | 0.401 | 0.35 / 616 | 0.32 / 639 | 5/11 | 0.9616/1/1 | -22.71/-43.84 | REJECT | NO_SOLVE_RATE_IMPROVEMENT, MCNEMAR_HOLM_NOT_SIGNIFICANT, RESTRICTED_MEAN_GAIN_BELOW_005B, PAIRED_BOOTSTRAP_LOWER_NOT_POSITIVE |
| `21b64bd46791` | 179 | 0.401 | 0.36 / 145 | 0.49 / 133 | 30/6 | 3.48e-05/0.0002088/0.0002784 | 12.13/7.26 | POWERED_SIGNAL | - |
| `95afdd10ecd2` | 57 | 0.401 | 0.29 / 54 | 0.28 / 53 | 3/5 | 0.8555/n/a/1 | 0.56/-0.20 | INVALID_UNIT | PANEL_GOAL_OVERLAP |

### Sensitivity

| presentation | reuse K=32 | reuse K=64 | expanded K=8 | surface K=0 |
|---|---:|---:|---:|---:|
| `39cb46a5584e` | 0.32 / 134 | 0.32 / 135 | 0.31 / 137 | 0.34 / 137 |
| `a8948b29abc8` | 0.43 / 219 | 0.43 / 220 | 0.42 / 223 | 0.51 / 219 |
| `3ce31c0a0b4c` | 0.40 / 136 | 0.40 / 136 | 0.40 / 137 | 0.40 / 138 |
| `6a89692d4f33` | 0.33 / 160 | 0.33 / 160 | 0.32 / 161 | 0.39 / 162 |
| `f5b4899726d6` | 0.34 / 439 | 0.33 / 440 | 0.27 / 460 | 0.43 / 397 |
| `3ac2b8840f14` | 0.29 / 649 | 0.29 / 649 | 0.12 / 730 | 0.39 / 599 |
| `21b64bd46791` | 0.51 / 132 | 0.51 / 132 | 0.48 / 136 | 0.38 / 145 |
| `95afdd10ecd2` | 0.26 / 53 | 0.26 / 53 | 0.28 / 53 | 0.29 / 54 |

Powered signals (1): `21b64bd46791`. This is one signal among eight
sampled presentations, not evidence of a family-wide mechanism. 2
non-signal presentations were invalidated locally; Holm over the six valid
units and conservative Holm over all eight give the same signal decision. The
next permitted step is only a preregistered, independently sampled frame audit
with its size, inclusion rule and acceptance rule frozen in advance. No result
here authorizes a world contract, ACTIVE/YOKED arm or family-wide claim.
