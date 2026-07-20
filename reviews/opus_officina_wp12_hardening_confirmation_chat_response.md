Written to `reviews/opus_officina_wp12_hardening_confirmation.md`.

## Verdict: `REVISE_OFFICINA_WP12_HARDENING`

The hardening closes **six of Sol's seven** counterexamples cleanly and preserves the contracts I previously accepted — but it introduces **one reproducible regression** in exactly the surface I was told to scrutinize.

### The blocking defect (C-1, reproduced)
The refactor moved the old inline `_append` charge guard into `record_q_terminal`, but the new public `record_pre_entropy_disposition` appends a `charged:false` TERMINAL **without a phase guard**, and `_append` now permits `DRAW_ARMED/LAUNCHED → TERMINAL`. So a caller who armed the draw (entropy imminent/drawn) or already launched (`charged:true`) can close as **`charged:false`, escaping the mandatory charge** — defeating Sol-4's required exclusive/total partition and the "non-gameable" one-shot path.

Reproduced on temp paths (no real surface):
```
DRAW_ARMED → pre-entropy disposition ACCEPTED, charged=False
LAUNCHED   → pre-entropy disposition ACCEPTED, charged=False (contradicts launch charge)
```
The existing test named `..._can_close_only_by_signed_pre_entropy_disposition` asserts the "only" but tests only the `CLAIMED` happy path — the counterexample is untested and live.

**Bounded fix (2 lines):** guard `record_pre_entropy_disposition` to require the last phase be `CLAIMED`, plus a regression test asserting rejection from `DRAW_ARMED`/`LAUNCHED`. That restores the partition (CLAIMED→charged:false disposition; DRAW_ARMED/LAUNCHED→charged:true `record_q_terminal` only).

### The other seven surfaces — closed
- **Sol-1 laundering:** `ArtifactStore` mediates writes with content-hash-bound provenance; raw native reads now raise; no write path yields `promotable:true`, so nothing can enter Q/C.
- **Sol-2 pause/resume + overdue E3:** artifact hashes recomputed at pause and resume; `ResumeGate.admit_work()` blocks until an overdue E3 review completes; `from_mapping` exact-key/exact-type with coercion removed; pristine-inactive invariant.
- **Sol-3 typed terminals:** `CScientificTerminal` enum replaces the free C label; journal `record_q_terminal` validates a typed `QTerminal`.
- **Sol-4 (partial):** external `AttemptRegistry`/ledger heads block id-reuse and suffix deletion (confirmed) — but the charge partition is incomplete (C-1).
- **Sol-5 PRF:** type-tagged encoding (no `1`/`"1"` collision); token-gated `TestOnlyKey`, no production key type.
- **Sol-6 behavior normalization:** behavior manifest drops `provenance_commit`/`inert_metadata`; `candidate_id` keys on `behavior_source_sha256` (WP-6 must *compute*, not trust, that digest).
- **Sol-8 verifier:** alias-resolving AST scan, dynamic-import detection, fail-closed import allowlist, expanded entropy set, external ledger head in the file set.
- **Scope:** no WP-3/WP-4/WP-6/WP-9 content; committed T `NOT_ACTIVATED`; draws no entropy.

**Tests/verifiers run:** three-file suite **38 passed**, verifier **OK**, `git diff --check` **clean**, and the read-only C-1 reproduction.

**Disposition:** WP-1/WP-2 may **not** close on `6b6d55d`; apply the C-1 fix + regression test, then a focused re-confirmation of the delta. All other repairs are accepted and need not be reopened. This authorizes nothing beyond the existing signature — no entropy, T activation, real world, Q/C, lock, escrow, or outcome, and it does not open WP-3.

**Confirmed:** no existing file edited, one new review file, no open cell chosen, nothing committed; predecessor stays `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
