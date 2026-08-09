# WALLB_DESK_AUDIT_12

NON-CITABLE desk audit. No ACTIVE/YOKED learner was instantiated.

## VERDICT: WITHDRAWN_UNFAIR_COMPARATORS

This verdict supersedes the original `PROCEED_TO_WORLD_CONTRACT` line below.
The recorded numbers are retained as a failed design artifact, but carry no
gate credit: the surface arm was one-directional against bidirectional BFS, and
the completion arm normalized without search under a non-confluent partial
system. Correction `WALLB_DESK_AUDIT_12B` must use matched bidirectional search
and test completion-derived rules inside that search.

## Original report (withdrawn)

Original verdict: `PROCEED_TO_WORLD_CONTRACT`.

Metrics are `solved-rate / restricted-mean-PREW` at the calibrated BFS cap.
Completion is screened with its partial library supplied for free. Failure to saturate
under this favorable upper bound implies that cost-matched completion cannot saturate.

| presentation | B | BFS | length+Parikh | bounded completion | rules / bounded-complete | decision | reasons |
|---|---:|---:|---:|---:|---:|---|---|
| `39cb46a5584e` | 500 | 0.42 / 377 | 0.42 / 385 | 0.04 / 494 | 64 / False | DESK_CANDIDATE | - |
| `a8948b29abc8` | 500 | 0.33 / 424 | 0.29 / 434 | 0.08 / 488 | 64 / False | DESK_CANDIDATE | - |
| `3ce31c0a0b4c` | 500 | 0.21 / 431 | 0.21 / 431 | 0.04 / 495 | 64 / False | DESK_CANDIDATE | - |
| `6a89692d4f33` | none | 0.96 / 2508 | 0.50 / 13003 | 0.75 / 5887 | 64 / False | REJECT | NO_20_60_BFS_CAP |
| `f5b4899726d6` | 2000 | 0.29 / 1682 | 0.29 / 1690 | 0.21 / 1835 | 64 / False | DESK_CANDIDATE | - |
| `3ac2b8840f14` | 2000 | 0.38 / 1559 | 0.17 / 1827 | 0.08 / 1940 | 64 / False | DESK_CANDIDATE | - |
| `21b64bd46791` | none | 0.96 / 3942 | 0.79 / 6246 | 0.50 / 10574 | 64 / False | REJECT | NO_20_60_BFS_CAP |
| `95afdd10ecd2` | none | 1.00 / 549 | 1.00 / 933 | 0.62 / 7750 | 64 / False | REJECT | NO_20_60_BFS_CAP, SURFACE_SHORTCUT_SATURATES |

Desk candidates: 5 / 8.
Recommended desk candidate: `3ac2b8840f14`; rules: `aa<->cb; aac<->ba; acac<->dd; ad<->bbdb; ca<->ccc; cba<->cc; cbc<->ddd`.
Recommended BFS solve rates at witness lengths 6/10/14: `0.500 / 0.375 / 0.250`.
Post-dev selection rule: maximize BFS advantage over the stronger surface/completion shortcut, then proximity to 0.40 BFS solve rate.
Residual limits: bounded completion is not a proof that no finite completion exists; 24 goals per presentation are a calibration sample.

A desk candidate only permits a concrete world contract. It is not evidence for ACTIVE,
YOKED, manufactured experience, transfer, or the essay's scientific claim.
