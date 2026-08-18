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
