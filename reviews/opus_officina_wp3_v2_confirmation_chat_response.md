Written to `reviews/opus_officina_wp3_v2_confirmation.md`.

## Verdict: `REVISE_OFFICINA_WP3_V2`

Every substantive v1/Sol repair is **closed and independently verified** — but two bounded defects prevent two independent implementations from agreeing, so I cannot confirm for selection, and I don't waive them.

**Independent recomputation — all confirmed.** I recomputed all four CH-1×CH-2 branches from the generic rule: disjoint (`Q∩C=∅`), covering (`Q∪C=[n0,n0+39]`), excluding `[66,125]` and both T-dev bands, with `N_h`=3/2, `q_h`=4/6. The regression vectors match exactly (CH-2a Q = the corrected set; CH-2b C; HIGH×C-rich Q = `{128,…,163}`); §2b design rows and the `n_h=1` small-stratum rule are sound. I also built the exact `officina.frame.v1` JSON for a dummy selection — canonical, **byte-reproducible, and acyclic** (`contract_sha256` never references the frame).

**Two defects (bounded):**
- **V2-1 (Major, item 3)** — §4's oracle refusal grammar has **no priority** for a query that is *both* over-length *and* contains an illegal byte, and is not exhaustive (malformed JSON, wrong keys, non-string, non-canonical are unclassified). Two implementations return different refusal bytes → oracle transcripts aren't byte-reproducible. Since the oracle is a declared *total* function with a *typed refusal, never false*, this is a WP-3 contract-completeness gap. Fix: a total, ordered classification over all inputs.
- **V2-2 (Minor, item 7)** — §1 cites the v1 draft as `successor/officina/WP3_...V1_DRAFT.md`, which **does not exist**; the actual artifact is `successor/OFFICINA_WP3_...V1_DRAFT.md`. Must be repaired.
- Minor V2-3 (pin the exact `contract_sha256` artifact bytes) and V2-4 (the "not scale transfer" wording is generous for upper-frame worlds).

**Confirmed closures:** the capability invariant closes the caller-supplies-`n` route at the contract level (constructor band-check; Q/C capabilities nonexistent until their roots; the pure-function-simulation is the separate §6 shortcut concern); §5's T-dev rule is CH-1-invariant with a named extrapolation property and needs no author cell; donor/`B`/arms/endpoint are WP-9; the forbidden language forecloses over-claiming; no later-phase numeric is selected; no stopped-line tuning.

**Fable's three Opus questions — Yes / Yes / Yes** (with the V2-3 `contract_sha256`-pin caveat on Q1; V2-1 is a separate wire-grammar gap, independent of the capability invariant Q2).

**Checks run (read-only):** four-branch recomputation, dummy frame-JSON serialization probe, v1-path existence check (stale confirmed), `verify_officina_wp12.py` → OK, bootstrap set unchanged (v2 commit touched 0 files under `successor/officina/`).

**Packet eligibility:** the five-token packet is **not yet eligible** — a bounded Fable revision (V2-1 total refusal ordering + exhaustiveness; V2-2 path fix; V2-3 pin; V2-4 optional) **plus a focused re-confirmation** is required. This authorizes only that bounded revision — no author token, WP-4, entropy, T activation, world generation, Q/C process, lock, escrow, datum, or outcome; no qualification or direction predicted.

**Confirmed:** no existing file edited, one new confirmation file, no cell/token selected, nothing committed; predecessor stays `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
