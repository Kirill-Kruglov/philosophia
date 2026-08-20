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
