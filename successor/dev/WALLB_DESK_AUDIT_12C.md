# WALLB_DESK_AUDIT_12C

NON-CITABLE final mechanism screen. No ACTIVE/YOKED learner was instantiated.

## VERDICT: UNDERPOWERED_SCREEN_RERUN_REQUIRED

The apparent singleton is not gate evidence. It changes paired solve count from
6/24 to 10/24; even in the most favorable no-loss discordance pattern, the
one-sided exact McNemar value is 0.0625 before accounting for eight screened
presentations. Restricted mean is dominated by the same censoring events and
is not independent confirmation. Audit 12d must freeze power, calibration and
multiplicity rules before execution.

Metrics are `solved-rate / restricted-mean-ISWU` at the indexed K=0 cap. One
trie transition and one emitted match each cost one ISWU; macro witnesses are
paid at admission, not reuse. `surface` changes only within-frontier order.
Goal relevance uses a separately seeded panel and never reads evaluation goals.
Implementation size: 748 nonblank lines.

### Primary: goal-relevant ordering under reusable-macro ISWU

| presentation | B | K=0 | surface | K=8 | K=32 | K=64 | decision | reasons |
|---|---:|---:|---:|---:|---:|---:|---|---|
| `39cb46a5584e` | 50 | 0.25 / 48 | 0.25 / 48 | 0.21 / 49 | 0.17 / 49 | 0.17 / 49 | REJECT | NO_HELPFUL_MACRO_REGION |
| `a8948b29abc8` | 100 | 0.21 / 88 | 0.21 / 88 | 0.21 / 89 | 0.21 / 90 | 0.21 / 90 | REJECT | NO_HELPFUL_MACRO_REGION |
| `3ce31c0a0b4c` | 100 | 0.21 / 88 | 0.21 / 88 | 0.29 / 88 | 0.29 / 89 | 0.29 / 89 | REJECT | NO_HELPFUL_MACRO_REGION |
| `6a89692d4f33` | 200 | 0.29 / 172 | 0.38 / 171 | 0.21 / 176 | 0.21 / 177 | 0.21 / 177 | REJECT | NO_HELPFUL_MACRO_REGION |
| `f5b4899726d6` | 500 | 0.29 / 422 | 0.33 / 416 | 0.25 / 454 | 0.17 / 462 | 0.17 / 462 | REJECT | NO_HELPFUL_MACRO_REGION |
| `3ac2b8840f14` | 500 | 0.38 / 398 | 0.38 / 392 | 0.38 / 408 | 0.33 / 397 | 0.33 / 400 | REJECT | NO_HELPFUL_MACRO_REGION |
| `21b64bd46791` | 200 | 0.25 / 182 | 0.25 / 182 | 0.42 / 157 | 0.42 / 158 | 0.42 / 159 | FRAME_MEMBER | - |
| `95afdd10ecd2` | 50 | 0.29 / 48 | 0.29 / 48 | 0.29 / 48 | 0.21 / 48 | 0.21 / 48 | REJECT | NO_HELPFUL_MACRO_REGION |

### Sensitivity: completion/reuse and relevant/expanded

| presentation | completion K=8 | K=32 | K=64 | expanded K=8 | K=32 | K=64 |
|---|---:|---:|---:|---:|---:|---:|
| `39cb46a5584e` | 0.21 / 49 | 0.17 / 49 | 0.17 / 49 | 0.17 / 49 | 0.04 / 50 | 0.04 / 50 |
| `a8948b29abc8` | 0.21 / 89 | 0.21 / 90 | 0.21 / 90 | 0.21 / 91 | 0.17 / 92 | 0.17 / 92 |
| `3ce31c0a0b4c` | 0.25 / 88 | 0.29 / 88 | 0.29 / 89 | 0.21 / 90 | 0.21 / 91 | 0.21 / 91 |
| `6a89692d4f33` | 0.29 / 175 | 0.21 / 176 | 0.21 / 177 | 0.21 / 176 | 0.17 / 183 | 0.17 / 183 |
| `f5b4899726d6` | 0.21 / 453 | 0.17 / 459 | 0.17 / 462 | 0.17 / 475 | 0.08 / 485 | 0.08 / 485 |
| `3ac2b8840f14` | 0.33 / 391 | 0.33 / 401 | 0.33 / 400 | 0.12 / 477 | 0.08 / 483 | 0.08 / 483 |
| `21b64bd46791` | 0.42 / 157 | 0.42 / 159 | 0.42 / 159 | 0.42 / 161 | 0.42 / 162 | 0.42 / 163 |
| `95afdd10ecd2` | 0.29 / 48 | 0.29 / 48 | 0.21 / 48 | 0.29 / 48 | 0.21 / 48 | 0.21 / 48 |

Passing development set (1 presentations): `21b64bd46791`. Every
passing presentation is retained; goals within one presentation are not
independent world replicates. A singleton cannot support a world-family claim
without an author decision restricting scope to that presentation and its
renamings. Pass requires a non-saturating surface arm and a
goal-relevant K>0 improvement of >=0.05B, plus calibration, non-convergence and
ladder checks. This audit never authorizes a scientific arm or claim.
