# B2_INSTRUMENT_REPAIR_09 — static instrumentation audit

Pinned source SHA-256 values were recomputed and match the prompt. The script diff was read directly. Items 5 and 6 are carried forward from the prior audit and were not re-audited.

## Findings

### 1. Held-out contamination (R2): DEFECT

The path-stage exclusion is real but is not universal as required.

- The per-seed held-out set is built at `b2_instrument_repair_09.py:406-443`; all four word arrays are unioned into `exclude_words` at lines 427-439.
- P0, P+, and P_shuf pass that set into `path_train_p0` at lines 1445-1448, 1505-1508, and 1535-1538. The sampler rejects the whole generated batch after pairing/shuffling at lines 265-276, and the training loop independently asserts disjointness at line 797. P_shuf therefore cannot re-admit a held-out word: shuffling at lines 320-330 changes pairings but not the candidate word set checked at lines 272-274.
- P0-neg passes the set at lines 1477-1479 and asserts it at lines 861-864. The trained P0/P0-neg readouts also route through exclusion-aware samplers at lines 955-983.
- However, D, P+, and P_shuf destination training receives the frozen K-set `pairs` at lines 1423-1425, 1510-1512, and 1541-1543. Neither `run_seed` nor `destination_train_with_checkpoints` (`1077-1125`) tests the individual K-set words against `heldout["exclude_words"]`; that function does not accept the exclusion set. Thus the source does not prove exclusion from **every** training batch.

This corrupts criterion 1's registered R2 held-out status if any K-set word intersects the evaluation-word set. The path curves are evaluated before the later destination stage, but the ticket's stronger “never trained on / every arm” invariant is not established.

Smallest repair: construct each seed's K-set before its held-out set, pass the union of K-set words as forbidden input to `build_heldout_batch`, and fail closed with an explicit disjointness assertion before any arm trains. Existing path/readout assertions remain. The emitted JSON does not contain the held-out or K-set word identities, so this cannot be repaired from JSON alone. **Rerun required.**

### 2. Firewall breach in the new metrics (R3): OK

The reachable call graph is clean.

- Held-out construction (`406-443`) reaches `_sample_length_matched_positive_batch_once`, `sample_length_matched_diff_batch`, and `_sample_word_at`. Those reach only `admissible_paddings`, `word_length`, `word_count`, `unrank_word`, `displacement`, deterministic stream sampling, and token/length checks. None reads `MODULUS`, fold/residue, oracle labels, panel membership, or truth.
- `road_gap_metric` (`525-552`) reads only the four held-out word arrays, `encode_word_self`/`encode_pair`, model/projector activations, normalization, cosine products, and means. `encode_pair` maps raw R/L bytes plus the separator and padding; it has no world or label input.

The assertion mechanism is weak but does not conceal a present leak: `_assert_path_clean("road_gap")` at line 531 has no inspected kwargs and is therefore vacuous, while `_assert_path_clean("build_heldout", n=HOLDOUT_PAIRS)` at line 408 checks only the harmless name `n`. The conclusion comes from tracing the actual reachable code, not from those calls. No criterion is corrupted by a forbidden read in the pinned source.

### 3. Length ruler in `road_gap` (R3): DEFECT

The equal- and different-displacement pair sets are not matched to each other by length.

For equal-displacement pairs, `build_heldout_batch` calls the positive sampler in chunks at lines 411-420; each chunk independently draws one `ell` at line 287. For different-displacement pairs, `sample_length_matched_diff_batch` independently draws a fresh `ell` for every pair at lines 377-380. The builder passes only a pair count and exclusion set at lines 427-430; it passes no equal-pair length sequence. `road_gap_metric` then subtracts the two unconditional means at lines 534-551. Each different-displacement pair is internally same-length, but its length is not matched to the corresponding equal-displacement pair or to the equal-pair empirical length distribution.

This corrupts criterion 3 (`road_gap(P0) > road_gap(init)` and `road_gap(P0) > road_gap(P_shuf)`): the registered contrast can include unequal length-mixture effects.

Smallest repair: record the target length of every equal-displacement held-out pair and generate its different-displacement comparator at that exact target length; assert pairwise equality of the two length sequences before evaluation. Aggregate embeddings or pair-level cosine values are not emitted, so the corrected `road_gap` cannot be recovered from JSON. **Rerun required.**

### 4. Init baseline mismatch (R4): OK

Every arm constructs its own committee with `new_committee(seed)` (`758-764`), which uses the same deterministic seed-derived key and construction. Each `probes_init` is taken on that exact local `models` object before its arm's training, and each `probe_deltas` call subtracts that same arm-local object (`1421-1434`, `1441-1464`, `1475-1493`, `1502-1522`, `1531-1552`). No D-arm init result is reused.

For road alignment, P0 and P_shuf each create their own optional projector and immediately measure `rg_init` on the exact model/projector objects later trained (`1441-1450`, `1531-1539`). The baseline therefore matches the arm's actual starting weights and architecture. Criterion 4 is not corrupted by cross-arm init reuse.

### 7. Conditional-fix discipline: DEFECT

The coefficients remain `(25, 25, 1)`, and the branch runs once, but the BN projector is not the branch's only effective change.

First, the held-out stream domain includes `run_tag` at lines 1855-1860. Main supplies `pre_fix` at lines 2058-2059 and `post_fix` at lines 2092-2093. The conditional rerun therefore uses different held-out words. Because those differing words also define `exclude_words`, any collision causes the path sampler to consume a different candidate sequence; the training data can differ as well as the projector.

Second, `mean_std` changes surfaces. Without the fix, `eval_heldout_vicreg` computes it from raw `prehead` outputs (`513-515`, then `519`). With the fix, the same variables are replaced by projector outputs at lines 516-518 before `vicreg_pair_components` computes `mean_std`. Pre-fix is therefore a 128-dimensional trunk statistic; post-fix is a 256-dimensional BN-projector statistic. The same numeric threshold `0.5` is applied to both at lines 2072-2074 and 2105-2106, so the persistence decision is not comparable to the trigger decision.

This directly corrupts criterion 2 and, if the conditional branch fires, breaches the single-change basis on which criteria 1, 3, and 4 are interpreted.

Smallest repair: domain-separate the held-out set by seed only and reuse the exact same held-out object/identities in both attempts; define the collapse statistic on one frozen surface in both attempts (the pre-projector trunk is the bounded option available in both architectures), label that surface explicitly, and use only that statistic for the `0.5` trigger/persistence test. Keep the objective components on the objective's own surface. Neither the alternative held-out measurements nor a common-surface post-fix statistic can be reconstructed from the aggregate JSON. **Rerun required if the conditional branch fires; if it does not fire, this branch defect does not affect the completed pre-fix numbers.**

### 8. Seed accounting: OK

`PILOT_SEEDS` is exactly `(0, 1)` at line 104. `run_once` iterates that tuple without filtering at lines 1855-1870, and both the pre-fix and any single post-fix attempt call the same function. There is no seed drop, replacement, or reroll branch; an exception stops the run rather than silently omitting a seed.

### 9. Destination learner: OK

At the two destination functions, the direct pilot-to-repair diff changes exactly one call each:

- Pilot `b2_path_pilot_08.py:553` to repair `b2_instrument_repair_09.py:907`.
- Pilot `b2_path_pilot_08.py:747` to repair `b2_instrument_repair_09.py:1111`.

In both cases only `memory_safe_class_balanced_feasibility_committee_step` becomes `memory_safe_feasibility_committee_step`; arguments, optimizer construction, capability, horizon, finite checks, checkpoint cadence, freeze/unfreeze behavior, and returns are unchanged within those functions. The edit is confined to destination training and introduces no call from a path-stage function. Under the prompt's accepted context, the divergence is contained.

## Rerun consequence

Defects 1 and 3 affect data/metric construction and require a rerun; they cannot be repaired from emitted aggregate JSON. Defect 7 requires a rerun only if the BN conditional branch fires; otherwise the executed pre-fix attempt never enters the defective comparison. No recomputation-only repair is available for these defects.

B2_09_STATIC_AUDIT=DEFECT
