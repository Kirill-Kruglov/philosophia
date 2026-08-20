# Amendments

Amendments to the candidate-for-lock preregistration are recorded below.

When a locked design must change, append a signed entry here containing the date,
affected gate, old rule, new rule, reason forced by execution, and the commit that
contains the amendment. Never rewrite an earlier entry.

## 2026-08-18 — pre-data, pre-lock: PREREG §6.3 deviation 7 (single-thread)

**Date:** 2026-08-18  
**Status:** **pre-data, pre-lock**. No outcome-bearing run exists, so nothing is invalidated.  
**Affected gate:** PREREG §6.3 Allowed deviations only (documentation of an already-mandated runtime setting; not a scientific-rule change).  
**Old rule:** §6.3 enumerated deviations 1–6 only; single-thread execution was required by implementation contract §17 but was not listed among the authorized deviations from inherited Level 0 runtime.  
**New rule:** §6.3 item 7 records that execution is pinned to a single intra-op and single inter-op thread; the inherited `configure_canonical_torch_runtime()` (16 intra-op / 32 inter-op) is not invoked. The confirmatory config template now records `torch_num_threads=1` and `torch_num_interop_threads=1`.  
**Reason:** §6.3 did not enumerate the single-thread execution that impl-contract §17 mandates and that overrides the inherited 16/32-thread pin in `src/philosophia/level0/config.py`. External review flagged this as an undocumented deviation; it is reconciled here before lock.  
**Files touched:**
- `successor/v0.2/PREREGISTRATION_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/CONFIRMATORY_CONFIG_TEMPLATE_V0.2.json`
- `successor/v0.2/CANDIDATE_BUNDLE_SHA256.txt`
- `AMENDMENTS.md`

**Scientific values:** none changed (estimand, arms, SESOI, gates, N rule, module pools, interpretation unchanged). This is a runtime/determinism documentation fix only.

**Follow-up (2026-08-18, pre-lock):** preamble replaced (the previous opening sentence contradicted this entry); `SHUFFLED_TAG_CONFIG_TEMPLATE_V0.2.json` now records `torch_num_threads=1` / `torch_num_interop_threads=1` (any JSON configuring a real run carries these fields; decision/record templates do not); bundle rehashed.

## 2026-08-19 — pre-data, pre-lock: pin the six convergence items from the three-implementation cross-check

**Date:** 2026-08-19  
**Status:** **pre-data, pre-lock**. No outcome-bearing run exists, so nothing is invalidated. This is the second pre-lock amendment.  
**Prompted by:** the Phase-A cross-check of three independent implementations (A/B/C). They agreed on `config.py`/`model.py` provenance, both exact `p_flip` tables, split sizes, the `seed64` first-20 vectors for all ten namespaces, inherited architecture/optimizer numerics, intra-implementation k=1 identity, D0, and Clopper–Pearson. They diverged on every item that actually moves a trajectory — world allocation, initialization hashes, split digests, the synthetic-analysis fixture, and the SHUFFLED_TAG schedule hash — because the bundle did not pin those encodings. Two divergences were real defects rather than encoding noise: one implementation built `W_U` with width `2M-1`, dropping the `=` column from the output head; two implementations derived every role seed from `replicate_index` directly, so calibration replicate 0 and confirmatory replicate 0 would have received identical world allocation, split, initialization, and context vectors, defeating the stage disjointness that `CALIBRATION_AND_POWER_PROTOCOL` §1 requires.

**Affected gates:** implementation contract §§1, 3, 4, 6, 7, 8, 12, 13, 19; calibration protocol §5.2; analysis plan §§11, 14.1. No gate in the preregistration is touched.

**The six pins:**

1. **Output head and class counts** (implementation contract §4) — makes explicit the inherited Level 0 relation with "numeric range" replacing "modulus": `vocabulary_size = training_classes = 2M`, `reporting_classes = 2M-1`, `equals_token = 2M-1`, `W_U` of shape `[d_model, vocabulary_size]` with the `=` column retained as a trained but never-correct class. Narrowing `W_U` to `2M-1` is an architecture change absent from preregistration §6.3 and is not authorized.
2. **Two-level seed derivation** (implementation contract §3, with §8 step 1 reworded to match) — resolves the §3/§8 conflict. `replicate_seed = seed64(stage, i)`; every role seed derives from `replicate_seed`, never from `i`. Only this reading satisfies §3, §8, and the stage disjointness of `CALIBRATION_AND_POWER_PROTOCOL` §1 simultaneously.
3. **World-order permutation algorithm** (implementation contract §6) — pins `numpy.random.Generator(numpy.random.PCG64(world_order_seed)).permutation(pool)` over the ascending pool, and pins the allocation hash preimage.
4. **Batch policy** (implementation contract §13, with §§1, 12, 19 aligned) — records the *inherited* full-batch policy resolved from the `MODEL_CONFIG_REF` subtree (`data.py` + `train.py`): one optimizer update consumes the entire replicate training split, `drop_last=false`, `gradient_accumulation_steps=1`, one epoch is one update. This is inheritance, not deviation, and is therefore **not** added to preregistration §6.3.
5. **Published test vectors** (new `successor/v0.2/TEST_VECTORS_V0.2.json`) — shared acceptance-vector inputs so the implementations co-fail on trajectory-relevant quantities instead of only on spec arithmetic; plus the remaining encodings: pair-split rank key and set-valued `split_hash` (implementation contract §7), tensor and state-dict hashing inherited from Level 0 `model._hash_tensor` (implementation contract §19), and the canonical `model_config_acceptance_projection` that replaces byte-identity of `v0.2_model_config.json` as an acceptance item.
6. **P0 run assignment** (calibration protocol §5.2) — a new mechanical rule where the bundle had none. It fixes, for `r = 0..15`, the replicate seed, the modulus (`pool[r mod 8]`, each pool modulus used exactly twice), the initialization, the split, the context code, and the batch row order, and states that no history, world allocation, or fork probe occurs at P0. This is a development-stage rule and no data exists, so it is legitimate pre-lock. The acceptance rule of §5.3 is unchanged.

Two clarifying notes carrying no rule change were also appended: analysis plan §11 records that k=1 bit identity is structural rather than empirical evidence of floating-point reproducibility (D0/D1 carry that), and §14.1 records that the diagnostic sign-gate implementation belongs to the pre-calibration root (lock manifest section B) on the same footing as the primary sign gate.

**Scientific values:** none changed. The primary estimand, the arms, the SESOI (`ln 1.20`), the CI levels, the heavy-cap threshold, the sign-gate rule, the N rule, the module pools, the competence rule, the kill-matrix statuses, and the interpretation fences are all unchanged. `PREREGISTRATION_V0.2_CANDIDATE_FOR_LOCK.md` is **not modified** by this edit.

**Files touched:**
- `successor/v0.2/IMPLEMENTATION_CONTRACT_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/CALIBRATION_AND_POWER_PROTOCOL_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/ANALYSIS_PLAN_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/TEST_VECTORS_V0.2.json` (new)
- `successor/v0.2/README.md`
- `successor/v0.2/CANDIDATE_BUNDLE_SHA256.txt`
- `AMENDMENTS.md`

## 2026-08-20 — pre-data, pre-lock: close the remaining free encodings

**Date:** 2026-08-20  
**Status:** **pre-data, pre-lock**. No outcome-bearing run exists, so nothing is invalidated. This is the third pre-lock amendment.  
**Cause:** external verification of amendment #2 confirmed both `.md` diffs and independently recomputed all four new fixtures (46 checks, no disagreement beyond 2.2e-16), but found two defects in the published fixtures and four encodings still free.

**Affected gates:** implementation contract §2; calibration protocol §2; conditional SHUFFLED_TAG protocol §4.1 and new §4.2; lock manifest §§A, B; `TEST_VECTORS_V0.2.json`. No gate in the preregistration is touched.

**The seven edits:**

1. **Canonical diagnostic labels** (defect) — `TEST_VECTORS_V0.2.json` published two label strings that exist nowhere in the preregistration. `V_RESOLVED_POSITIVE_I_NOT` becomes `VARIABILITY_COMPONENT_SUPPORTED` and `DECOMPOSITION_UNRESOLVED` becomes `COMPONENT_DECOMPOSITION_UNRESOLVED`, the strings the kill matrix and analysis plan §14.2 actually define; a `labels` object now enumerates the only four permitted values and their conditions.
2. **Capped entries are `null`, precedence explicit** (defect) — `case_diagnostic_heavy_cap` carried `0` at three capped indices and ordinary values at three others, which contradicts implementation contract §15 where `T=0` is a legitimate observed event. The array is now `null` at exactly the capped indices, and a `capped_precedence` rule in both synthetic fixtures states that `capped_indices` is authoritative and that computing `min(T,tau)` without consulting the flag is wrong. `synthetic_primary_fixture.T_separable_k6` is deliberately left unchanged because it is shared by two authoritative cases. Recomputation confirms every published value is unchanged.
3. **`MODEL_CONFIG_REF` is an ordered file set** — the bundle spoke of one path and one hash while implementation contract §13 resolves the batch policy from `data.py` and `train.py` and the architecture has never been in `config.py`. §2 now fixes the ordered set `config.py, model.py, data.py, train.py`, the per-file raw-byte hashes, the derived `MODEL_CONFIG_REF_ROOT`, and the vendor-and-verify requirement; calibration protocol §2 and lock manifest §A are aligned. `MODEL_CONFIG_REF_ROOT = aae16aa53e97cb227b82a9628936fa569efc39a382f58d839e002c643a5616e8`.
4. **SHUFFLED_TAG schedule encodings** — §4.1 left the extra-presentation subset, the within-block order, and the schedule digest free, all three trajectory-relevant. Steps 3 and 5 now pin a digest ranking and a PCG64 permutation, and a new §4.2 pins `schedule_hash`, records `P = B_history * train_size` under full batch, and states that an example receives a freshly drawn code in every epoch by construction.
5. **Acceptance projection carries value literals** — 37 key names could not prevent `"none"`/`"None"` or `"full_batch"`/`"full batch"` divergence, and `max_position` was ambiguous between a count and an index. The projection is extended to 40 keys, given a complete `required_values` object and a `conventions` note, and published with `projection_sha256 = 1210822c27baa5350f37eaf2060e69922926bf2f9182862a1425a3faccde4f15`, which is the acceptance item that replaced byte-identity of `v0.2_model_config.json`.
6. **Lock manifest seed machinery** — "first 20 values per namespace" predated the two-level scheme and no longer names a well-defined object; §B now commits the two-level derivation implementation, `TEST_VECTORS_V0.2.json` and its SHA256, and the stage and role seeds for the published shared test replicates.
7. **Four fixtures promoted to `authoritative: true`** — the two primary and two SHUFFLED_TAG fixtures added in amendment #2 were re-derived by a party that did not write them and reproduce to within 2.2e-16; `authoritative_semantics.authoritative_true` now records that every flagged fixture has been independently re-derived.

**Scientific values:** none changed. The primary estimand, the arms, the SESOI (`ln 1.20`), the CI levels, the heavy-cap threshold, the sign-gate rule, the N rule, the module pools, the competence rule, the kill-matrix statuses, and the interpretation fences are all unchanged. Edit 1 replaces two invented label strings with the preregistered ones; it does not alter the conditions under which a label is assigned. `PREREGISTRATION_V0.2_CANDIDATE_FOR_LOCK.md` is again **byte-unchanged**, still `8b669b42c57242d1369a45a90a8ae808fa9e8de1b5faa0a72f6696fd48b8d946`.

**Files touched:**
- `successor/v0.2/IMPLEMENTATION_CONTRACT_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/CALIBRATION_AND_POWER_PROTOCOL_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/CONDITIONAL_SHUFFLED_TAG_PROTOCOL_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/LOCK_MANIFEST_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/TEST_VECTORS_V0.2.json`
- `successor/v0.2/CANDIDATE_BUNDLE_SHA256.txt`
- `AMENDMENTS.md`

## 2026-08-20 — pre-data, pre-lock: final pass before the Phase-A rebuild

**Date:** 2026-08-20  
**Status:** **pre-data, pre-lock**. No outcome-bearing run exists, so nothing is invalidated. This is the fourth and final pre-lock amendment; the bundle is closed after it.  
**Cause:** external verification of amendment #3 recomputed `MODEL_CONFIG_REF_ROOT` and `projection_sha256` exactly and closed four of that amendment's open questions. Two further free encodings were found by reading an implementation rather than the bundle — the positional-table draw procedure and the position-0 representation — either of which would change every initialization hash. A third gap was an unpinned NumPy/SciPy version behind four decision-relevant numerical routines.

**Affected gates:** implementation contract §§2, 8, 9, 17; conditional SHUFFLED_TAG protocol §§4.1, 4.2; `TEST_VECTORS_V0.2.json`. No gate in the preregistration is touched.

**The seven edits:**

1. **Inherited arm named** — `config.py` carries two arms and its hash covers both; `paper_mainline_arm()` (`weight_decay = 1.0`) is the grokking regime and `artifact_fidelity_arm()` (`0.1`) is its absence. §2 now fixes the paper-mainline arm as the inherited one and forbids the artifact arm from appearing in any v0.2 configuration, artifact, or log.
2. **Single authorized inheritance route** — the frozen Level 0 dataclasses validate values that v0.2 legitimately replaces (`modulus`, `vocabulary_size`, `warmup_updates`), so the override route was free. §2 now fixes inheritance **by value**: the frozen classes are never instantiated, and subclassing, validator relaxation, and construct-then-neutralize are forbidden because they record different provenance for an identical trajectory.
3. **Positional table and context injection** — §9 rule 4 now requires `W_pos` to be drawn once as a single `[4, d_model]` tensor rather than as `[3, d_model]` plus a separately drawn row, which consumes the random stream differently and would change every parameter drawn afterwards; §8 now fixes the position-0 representation as `z + W_pos[0]`, with the inherited positional term added uniformly and the context vector never added to a task position.
4. **Exact package versions pinned** — §17 now requires CPython, PyTorch, NumPy, and SciPy to be recorded as full version strings, since NumPy decides the world-order and SHUFFLED_TAG permutations and the `tau` quantile while SciPy decides the Clopper-Pearson bound and the chi-squared factor in the N rule. The two "NumPy major version" phrases are corrected to "exact NumPy version", and the resolved versions are published in `TEST_VECTORS_V0.2.json` as `locked_environment`: CPython `3.12.3`, torch `2.9.1+cpu`, NumPy `2.5.1`, SciPy `1.18.0`.
5. **SHUFFLED_TAG schedule expected values published** — `shuffled_tag_schedule_case` was the last trajectory-relevant item without an expected value. It now publishes the ranking, `extra_subset`, the code-count vector with its ordering convention, and `schedule_hash`, all authoritative.
6. **Schedule digest is incremental** — §4.2 now states that a single SHA256 state absorbs each block as it is generated, so the digest formula cannot be read as requiring all six blocks to be materialized at once.
7. **Redundant `P` derivation removed** — §4.1 step 1 no longer derives `P` from "batch size and inherited final-batch behavior" and states `P = B_history * train_size` directly.

**Scientific values:** none changed. The primary estimand, the arms, the SESOI (`ln 1.20`), the CI levels, the heavy-cap threshold, the sign-gate rule, the N rule, the module pools, the competence rule, the kill-matrix statuses, and the interpretation fences are all unchanged. `PREREGISTRATION_V0.2_CANDIDATE_FOR_LOCK.md` is again **byte-unchanged**, still `8b669b42c57242d1369a45a90a8ae808fa9e8de1b5faa0a72f6696fd48b8d946`.

**Files touched:**
- `successor/v0.2/IMPLEMENTATION_CONTRACT_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/CONDITIONAL_SHUFFLED_TAG_PROTOCOL_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/TEST_VECTORS_V0.2.json`
- `successor/v0.2/CANDIDATE_BUNDLE_SHA256.txt`
- `AMENDMENTS.md`

## 2026-08-20 — pre-data, pre-lock: index conventions and negative controls

**Date:** 2026-08-20  
**Status:** **pre-data, pre-lock**. No outcome-bearing run exists, so nothing is invalidated. This is the fifth pre-lock amendment; the bundle is closed after it and the Phase-A rebuild brief quotes the manifest this commit produces.  
**Cause:** the index conventions of the bundle were carried only implicitly, by the block labels of one digest formula, and were ambiguous in three ways rather than two. External recomputation confirmed three distinct readings of the schedule digest — fully 1-based, 0-based seeds with 1-based labels, and fully 0-based — all of which a plain reading of §4.1 step 5 admits. The same ambiguity affects `batch_order_seed(history_position, epoch)` in implementation contract §3, where no published hash enforces anything at all. Two clarity findings from amendment #4 are also closed, and the live-version assertion that had been a private checker convenience is promoted to a required test after the previous pass found one implementation built against a NumPy the repository does not resolve to.

**Affected gates:** implementation contract §§3, 9, 17; conditional SHUFFLED_TAG protocol §§4.1, 4.2; lock manifest §B; `TEST_VECTORS_V0.2.json`. No gate in the preregistration is touched.

**The five edits:**

1. **Index conventions stated once, centrally** — implementation contract §3 now fixes `replicate_index` 0-based, `history_position` **1-based** (H1 = 1, binding in `batch_order_seed`, `shuffled_tag_seed`, the SHUFFLED_TAG block labels, and every log field of that name), `epoch` 0-based running 0..B_history-1 under the full-batch policy, and `k` unaffected. The SHUFFLED_TAG protocol §§4.1 and 4.2 now point at that clause rather than leaving the numbering to inference.
2. **Negative controls for the schedule digest** — `shuffled_tag_schedule_case.expected` now publishes the digests of both wrong conventions alongside the correct one, so an index bug identifies itself instead of surfacing as an unexplained hash difference. All three were recomputed under the locked NumPy 2.5.1 and are mutually distinct.
3. **§9 rule 3 subordinated to rule 4** — rule 3's "no parameter is added" branch does not apply to the inherited Level 0 learner, whose `W_pos` is a learned table exactly one row short; the rule now says so and states it is never a licence to skip rule 4.
4. **§9 rule 5 names the number** — `max_position = sequence_length = 4`, counted as a number of positions and not as a zero-based index, matching the projection value. The Phase-A implementations had split 4 versus 3 on this field.
5. **Locked-environment assertion becomes a required test** — implementation contract §17 now requires an acceptance test asserting at process start that live CPython, PyTorch, NumPy, and SciPy versions equal the `locked_environment` block exactly, with failure `BLOCKED_IMPLEMENTATION`; lock manifest §B lists it first under Tests/reports.

**Scientific values:** none changed. The primary estimand, the arms, the SESOI (`ln 1.20`), the CI levels, the heavy-cap threshold, the sign-gate rule, the N rule, the module pools, the competence rule, the kill-matrix statuses, and the interpretation fences are all unchanged. `PREREGISTRATION_V0.2_CANDIDATE_FOR_LOCK.md` is again **byte-unchanged**, still `8b669b42c57242d1369a45a90a8ae808fa9e8de1b5faa0a72f6696fd48b8d946`.

**Files touched:**
- `successor/v0.2/IMPLEMENTATION_CONTRACT_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/CONDITIONAL_SHUFFLED_TAG_PROTOCOL_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/LOCK_MANIFEST_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/TEST_VECTORS_V0.2.json`
- `successor/v0.2/CANDIDATE_BUNDLE_SHA256.txt`
- `AMENDMENTS.md`

## 2026-08-20 — pre-data, pre-lock: batch_order_seed literals and a code-span fix

**Date:** 2026-08-20  
**Status:** **pre-data, pre-lock**. No outcome-bearing run exists, so nothing is invalidated. This is the sixth pre-lock amendment.  
**Cause:** amendment #5 pinned the `epoch` and `history_position` conventions in prose but left `batch_order_seed` without any published literal, so a cross-implementation off-by-one in either index would have survived every acceptance item — D0 replays one implementation against itself and the k=1 gate compares two arms of the same implementation, so a self-consistent off-by-one passes both. The `history_position` convention was mechanically enforced only for the SHUFFLED_TAG schedule digest. Separately, the parenthetical inserted into §4.1 step 5 by amendment #5 split the generator expression across two code spans.

**Affected gates:** conditional SHUFFLED_TAG protocol §4.1; `TEST_VECTORS_V0.2.json`. No gate in the preregistration is touched, and no prose rule changes meaning.

**The two edits:**

1. **Code span made continuous** — the parenthetical `(with history_position 1-based, H1 = 1, as fixed by implementation contract §3)` moves from the middle of the generator expression to the end of step 5, so `numpy.random.Generator(numpy.random.PCG64(seed64(...))).permutation(multiset)` is one uninterrupted, copy-pasteable span. The rule is unchanged.
2. **`batch_order_seed` literals published** — a new top-level `batch_order_seed_examples` object gives `seed64("batch-order", replicate_seed, history_position, epoch)` for the confirmatory and deterministic-replay replicate 0 at `(h1,e0)`, `(h1,e1)`, and `(h6,e0)`, plus a negative control at `(h0,e0)` for each, which is the value an implementation numbering history positions from 0 would produce. `batch_order_seed(h1,e0)` is added to `shared_test_replicates.report`. This gives the `epoch` and `history_position` conventions of implementation contract §3 the same mechanical enforcement the schedule digest already gives `history_position` for SHUFFLED_TAG. The values are pure digest arithmetic and are version-independent.

**Scientific values:** none changed. The primary estimand, the arms, the SESOI (`ln 1.20`), the CI levels, the heavy-cap threshold, the sign-gate rule, the N rule, the module pools, the competence rule, the kill-matrix statuses, and the interpretation fences are all unchanged. `PREREGISTRATION_V0.2_CANDIDATE_FOR_LOCK.md` is again **byte-unchanged**, still `8b669b42c57242d1369a45a90a8ae808fa9e8de1b5faa0a72f6696fd48b8d946`.

**Files touched:**
- `successor/v0.2/CONDITIONAL_SHUFFLED_TAG_PROTOCOL_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/TEST_VECTORS_V0.2.json`
- `successor/v0.2/CANDIDATE_BUNDLE_SHA256.txt`
- `AMENDMENTS.md`

## 2026-08-20 — pre-data, pre-lock: pin four encodings the Phase-A rebuild exposed

**Date:** 2026-08-20  
**Status:** **pre-data, pre-lock**. No outcome-bearing run exists, so nothing is invalidated. This is the seventh pre-lock amendment.  
**Cause:** the Phase-A rebuild produced a three-way agreement on every static quantity — seeds, allocation, split, initialization, and all eleven per-parameter tensor hashes — and exposed four unpinned encodings (the context-set digest, the batch digest, the probe batch-order coordinate, and the norm-ratio measurement point) plus an unpinned D0 budget. An arithmetic divergence between the three implementations is under gradient bisect and is **not** closed here; it will be addressed by a later amendment.

**Affected gates:** implementation contract §§8, 12, 17, 19; `TEST_VECTORS_V0.2.json`. No gate in the preregistration is touched.

**The four edits:**

1. **Context-set digest preimage** (implementation contract §8) — the per-world vector is hashed by the §19 tensor rule on the frozen float32 model-input tensor, not the float64 draw; `context_set_hash` concatenates those hashes over the eight worlds in allocation order C, H1..H6, spare. Published authoritative values: `calibration/0/M96` = `35d6dfef419ad048599e31f1248f74bc4d2880b534cd21dc5d31fecce6ef7ea7`; `deterministic-replay/0/M96` = `807b9cd764393fb06a18e9e5a2e5a0953b2add5d7069589fd939a487d846c9bc`.
2. **Batch and optional input digest preimages** (implementation contract §19) — `batch_hash = tensor_hash(rows)` over an int64 `[N,3]` tensor of `(a,b,y)` in `batch-order` presentation order, with no extra prefix; `input_hash` over the `[N,4,d_model]` float32 residual is optional, diagnostic, and never a gate.
3. **Probe batch-order sentinels** (implementation contract §12) — forked probes are not history worlds: every fresh-C probe uses `history_position = 0`; H1 reacquisition uses `history_position = 7`. Published `deterministic_replay_0` literals: `probe_h0_e0 = 2730718178529918974`, `reacq_h7_e0 = 5664936142307372860`.
4. **Norm-ratio measurement points and D0 budget** (implementation contract §§8, 17) — `context_norm_ratio_at_init` (always 1.0, after scale step 5) is distinct from `context_norm_ratio_at_block_end`; D0 is the k=1 identity smoke config: stage `deterministic-replay`, replicate 0, M=96, arm ALIASED, `B_history = 20`, `tau = 200`, evaluation interval 100.

**Not closed:** the arithmetic divergence among the three implementations remains under bisect and is reserved for a later amendment. No value is guessed here.

**Scientific values:** none changed. The primary estimand, the arms, the SESOI (`ln 1.20`), the CI levels, the heavy-cap threshold, the sign-gate rule, the N rule, the module pools, the competence rule, the kill-matrix statuses, and the interpretation fences are all unchanged. `PREREGISTRATION_V0.2_CANDIDATE_FOR_LOCK.md` is again **byte-unchanged**, still `8b669b42c57242d1369a45a90a8ae808fa9e8de1b5faa0a72f6696fd48b8d946`.

**Files touched:**
- `successor/v0.2/IMPLEMENTATION_CONTRACT_V0.2_CANDIDATE_FOR_LOCK.md`
- `successor/v0.2/TEST_VECTORS_V0.2.json`
- `successor/v0.2/CANDIDATE_BUNDLE_SHA256.txt`
- `AMENDMENTS.md`
