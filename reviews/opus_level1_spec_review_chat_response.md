Written to `reviews/opus_level1_spec_review.md`.

## Verdict: `REVISE_LEVEL1_SPEC`

The spec is careful and the **pure `Z/n` oracle + fail-closed dataflow substrate is eligible to implement now** — but three deferred choices aren't the "config fields, freeze at S-gate" items the draft treats them as. Each changes the world, estimand, or endpoint, and each gates a specific substrate module §13 wants built immediately.

**Critical**
- **CR-1 (O1) — the single-integer world's supply arithmetic is a binding, unresolved world-level tension.** Disjoint target/donor/dev blocks consume ≈ `2·N3 + N_dev` distinct `n` per stratum, while the donor breaks adaptivity only up to a residual YOKED penalty that scales with `|n_target − n_donor|` — controlled by stratum width. Narrow band → clean but few blocks; wide band → enough blocks but YOKED probing a grossly wrong modulus. This can change the world, so it must be confronted before the S-gate. It also refutes the draft's "breaks adaptivity without an easy mismatch" claim.
- **CR-2 (O2) — raw word pairs are the wrong candidate cell.** Every `{R,L}` word reduces to an integer displacement, so ACTIVE can win by *syntactic multiplicity* and RANDOM samples a different effective geometry. Canonicalizing removes the confound but *leaks the abelianization* (`net`). Fix: a locked **two-level contract** (semantic geometry balanced + arm-shared; syntax locked and arm-independent) — detailed in the review. This is not deferrable to config; the pool module must be built to it.
- **CR-3 (O4) — certified solve doesn't certify order recovery.** A class-balanced YES/NO panel is passable by memorizing seen displacement differences without representing `n`. The certificate must add held-out residue classes + explicit periodicity probes (`k·n` true, `k·n±1` false) with per-stratum accuracy/ABSTAIN caps.

**Major highlights**
- **MJ-1** — stated the exact wrap-coverage floor: `2·N2 ≥ n_max`.
- **MJ-2** — proved `n` is the *only* learner-observable parameter in `{R,L}`/origin-EQ (hidden generator step and origin both cancel), so C1 here is inherently "adapt probe scale to the modulus" — narrow scope, and its effect size confounds with stratum width.
- **MJ-3** — `|p−0.5|` single-head uncertainty is meaningless pre-calibration, exactly when budget matters; a C1 null under it isn't a clean falsification.
- **MJ-5** — low-entropy world + committed plaintext hash = a pre-outcome verification oracle; needs a secret salt with confidentiality resting on encryption.
- **MJ-7** — finite-population variance model with FPC is mandatory (blocks are drawn without replacement).

The review answers O1–O6, gives the exact mandatory revisions, the two-level candidate-pool recommendation, a partitioned gate table, and the **precise next authorization**: Codex may build only the neutral oracle + fail-closed scaffolding + salted-hash/donor bookkeeping on dummy fixtures; Cursor waits for the S-gate. Every signed negative destination is preserved (the additions only strengthen kills).

Not `BLOCKED_CYCLIC_WORLD` (world is fine) and not `REJECT_LEVEL1_IDENTIFIABILITY` (C1 is identifiable with narrowed scope). The file is uncommitted, consistent with the pre-lock discipline — say the word if you want it committed.
