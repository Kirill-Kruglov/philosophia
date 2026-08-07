**`first_persistent_step` = `None`** — no qualifying checkpoint in 0..2000; longest consecutive run = 0. Matches the v2 no-persistent-window regime.

Report: `successor/dev/COMPETENCE_DIAG_01.md` (wall 1.68 h). Script: `successor/dev/competence_diag_01.py`.

### Best checkpoint (step 150)

| stratum | correct/expected | abstentions | confident_lies | brier | qualifies |
| --- | ---: | ---: | ---: | ---: | --- |
| S1 | 124/118 (of 124) | 0 | 0 | 0.005751 | True |
| S2 | 8/15 (of 16) | 0 | 8 | 0.498641 | False |
| S3 | 8/15 (of 16) | 0 | 5 | 0.417323 | False |
| S4 | 8/15 (of 16) | 0 | 8 | 0.499677 | False |
| S5 | 8/14 (of 16) | 0 | 8 | 0.495397 | False |

**Gap:** Broad shortfall, not a near-miss. S1 clears easily; S2–S5 stay at ~8/16 with many confident lies and brier≈0.5 (looks like an “always ≠” bias that fits S1’s all-unequal surface and fails the balanced strata). Panel⊥training held (cell partition + 0 word-pair overlap).

**Unblock:** Next diagnostic — log mean `p_equal` by stratum/truth at the best checkpoint to confirm the always-≠ hypothesis?

**Quality idea:** Add a cheap stratum-wise `p_equal` histogram to the checkpoint strip so bias regimes show up without a second full B-run.