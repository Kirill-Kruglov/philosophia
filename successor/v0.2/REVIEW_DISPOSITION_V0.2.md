# v0.1 external review disposition -> v0.2 candidate for lock

This document records how every reported MAJOR/MINOR was handled. No finding is silently dropped.

## MAJOR-1 — input variability vs informativeness

**Review finding:** SEPARABLE exposes the learner to varying context directions while ALIASED history uses one direction; a novel z_C can therefore create a pure input-perturbation shock. This cannot explain a positive ALIASED advantage, but can explain negative/equivalent/unresolved primary outcomes. SHUFFLED_TAG was optional.

**Disposition: ACCEPTED.**

Repair:

- SHUFFLED_TAG is fully specified and implementation/analysis hash-locked before primary confirmation;
- execution is mandatory for every valid primary status except ALIASED_TRANSFER_ADVANTAGE / bounded positive variant;
- same N seeds, initialization, worlds, data, batch order, B_history, tau;
- per-example context assignment independent of world/target, balanced within each block;
- only k6 C probe required;
- preregistered decomposition `V=R_ALIAS-R_SHUFFLED`, `I=R_SHUFFLED-R_SEP`; `I` is explicitly treated as a residual stable-world-informative coding contrast, not a pure identity effect because temporal stability differs necessarily;
- negative primary claims remain regime-level until diagnostic completes.

Primary estimand unchanged.

## MAJOR-2 — mass at tau / t-CI validity

**Review finding:** P2 gates only baseline ceiling; k6 can develop mass at tau, making Student-t coverage questionable in precisely the loss-of-plasticity regime.

**Disposition: ACCEPTED.**

Repair:

- report cap fraction every arm×k;
- HEAVY_CAP if >10% at k6 in either primary arm;
- primary restricted delta remains unchanged;
- t-CIs still reported but cannot alone license direction under HEAVY_CAP;
- conservative exact paired sign gate required;
- practical equivalence forbidden under HEAVY_CAP;
- bounded directional status names used when both ordinary and sign gates pass;
- otherwise UNRESOLVED_HEAVY_CAP;
- no uncapped magnitude extrapolation.

Primary estimand unchanged.

## MINOR — positional encoding/max-position

**Disposition: ACCEPTED.** Exact +1 shift semantics and one-row-only learned-table extension rule added; unit test required.

## MINOR — decision rule mixes CI direction and point SESOI

**Disposition: ACCEPTED AS EXPLICIT DESIGN CHOICE.** SESOI is now explicitly a point-estimate licensing threshold; CI establishes direction. v0.2 does not claim the true effect exceeds SESOI.

## MINOR — equivalence power

**Disposition: ACCEPTED / REPAIRED.** N is now max of directional-superiority and true-null equivalence targets, both at 90% power using variance-only sigma_U.

## MINOR — context norm drifts after init

**Disposition: ACCEPTED AS FIXED-INPUT DESIGN.** No dynamic rescaling. Initial scale remains frozen; current token-embedding norm and ratio are logged at every history boundary.

## MINOR — outcome name preloading

**Disposition: ACCEPTED.** Neutralized to ALIASED_TRANSFER_ADVANTAGE / SEPARABLE_TRANSFER_ADVANTAGE / PRACTICALLY_EQUIVALENT / UNRESOLVED.

## MINOR — determinism

**Disposition: ACCEPTED / STRENGTHENED.** In addition to short smoke, a duplicated full H1+B_history plus k1 C probe replay is mandatory after budgets are known and again under final runtime. Failure is terminal for this prereg version.

## Dependency — MODEL_CONFIG_REF

**Disposition: ACCEPTED / PROMOTED TO P-1.** Exact config provenance is the first gate. If unresolved: BLOCKED_CONFIG_PROVENANCE before calibration.

## Scientific scope after revision

The cell remains narrowly scoped to whether forced non-separability of the modulus across six sequential modular worlds produces greater subsequent restricted in-weights transfer to a seventh reserved modulus than explicit fixed world separation.

v0.2 does not claim contradiction-only causality, mechanism identification, general balcony/experience, or language transfer.
