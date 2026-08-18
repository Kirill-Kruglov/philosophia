# Philosophia successor cell — ALIASED vs SEPARABLE

**Preregistration bundle v0.2 — CANDIDATE FOR LOCK**  
**No outcome-bearing run is authorized until external review closes and the corresponding hash roots are committed.**

This bundle specifies a narrow successor experiment to the stopped-open `philosophia` programme. It does not modify, reopen, or reinterpret any prior canonical result.

## Narrow question

Does forcing one learner to traverse six sequential modular worlds **without an input channel that separates world identity** reduce later in-weights adaptation cost to a seventh unseen world more than an otherwise matched history in which world identity is available through fixed, non-trainable context codes?

The experiment does **not** claim to isolate an abstract factor called “contradiction alone.” In this construction, removing cross-world target conflict necessarily requires making world identity recoverable from the input. The causal contrast is therefore the complete regime:

- `ALIASED`: world identity unavailable from learner input during history;
- `SEPARABLE`: world identity available through a fixed non-trainable code.

A positive result is a bounded transfer result only. It is not, by itself, evidence that a general `balcony`, manufactured experience, semantic competence, or the reusable modular mechanism has been established.

## Signed SESOI

The smallest effect size of scientific interest is frozen as a **20% larger multiplicative history-to-transfer gain in ALIASED than in SEPARABLE**:

`delta_SESOI = ln(1.20) = 0.1823215567939546`.

In v0.2 the SESOI is explicitly a **point-estimate licensing threshold**. Direction is inferentially established by the preregistered confidence interval. v0.2 is not designed to prove that the unknown population effect itself exceeds the SESOI.

## Principal v0.2 changes after external review

1. `SHUFFLED_TAG` becomes a **pre-locked, conditionally mandatory** third history regime whenever a valid primary outcome is not `ALIASED_TRANSFER_ADVANTAGE`. It decomposes context variability from context informativeness without changing the primary estimand.
2. A confirmatory **heavy-cap gate** is added. If more than 10% of k=6 probes in either primary arm hit `tau`, Student-t intervals cannot alone license a direction; a locked conservative paired sign gate is required, and practical equivalence is not declared under heavy cap.
3. Power now prices two targets mechanically from the same variance-only pilot: directional superiority at `|delta| = SESOI` and practical equivalence at `delta = 0`.
4. Positional/max-position semantics, context-norm drift logging, and full deterministic replay are explicit.
5. Scientific outcome names are neutralized: `ALIASED_TRANSFER_ADVANTAGE`, `SEPARABLE_TRANSFER_ADVANTAGE`, `PRACTICALLY_EQUIVALENT`, `UNRESOLVED`.
6. `MODEL_CONFIG_REF` provenance is a first preflight gate. If it cannot be recovered exactly, terminal=`BLOCKED_CONFIG_PROVENANCE` before any calibration.

## Files

1. `PREREGISTRATION_V0.2_CANDIDATE_FOR_LOCK.md` — scientific contract.
2. `IMPLEMENTATION_CONTRACT_V0.2_CANDIDATE_FOR_LOCK.md` — world/input/training/determinism semantics.
3. `CALIBRATION_AND_POWER_PROTOCOL_V0.2_CANDIDATE_FOR_LOCK.md` — permitted development path and mechanical selection of M, budgets, and N.
4. `ANALYSIS_PLAN_V0.2_CANDIDATE_FOR_LOCK.md` — primary estimand, SESOI, CIs, heavy-cap supplement, and decision rules.
5. `CONDITIONAL_SHUFFLED_TAG_PROTOCOL_V0.2_CANDIDATE_FOR_LOCK.md` — pre-locked conditional diagnostic required for valid non-positive primary outcomes.
6. `KILL_MATRIX_V0.2_CANDIDATE_FOR_LOCK.md` — fail-closed decision surface and claim ledger.
7. `LOCK_MANIFEST_V0.2_CANDIDATE_FOR_LOCK.md` — pre-calibration, calibration, confirmatory, and conditional-diagnostic hash commitments.
8. `REVIEW_DISPOSITION_V0.2.md` — disposition of every MAJOR/MINOR from the v0.1 review.
9. `REVIEW_REQUEST_V0.2_CANDIDATE_FOR_LOCK.md` — final attack surface for candidate-for-lock review.
10. `CALIBRATION_DECISION_TEMPLATE_V0.2.json` — machine-readable development decision template.
11. `CONFIRMATORY_CONFIG_TEMPLATE_V0.2.json` — machine-readable confirmatory lock template.
12. `SHUFFLED_TAG_CONFIG_TEMPLATE_V0.2.json` — machine-readable conditional diagnostic template.

## Repository-dependent item

`MODEL_CONFIG_REF` is not a tuning choice. Before the pre-calibration root can exist, it must resolve to the exact Level 0 paper-mainline config and content hash. All inherited trajectory-relevant numerical values are taken from that config except the deviations explicitly enumerated by v0.2.
