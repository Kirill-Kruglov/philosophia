Written to `reviews/opus_officina_t_activation_protocol_v2_confirmation.md`.

## Verdict: `READY_FOR_OFFICINA_T_ACTIVATION_IMPLEMENTATION`

The v2 correction closes P-1..P-7 **one-to-one and comprehensively**; two independent implementers can now build the same **inactive** state machine without selecting a deferred cell. Three Minor wording reconciliations remain, non-blocking.

**P-1..P-7 all closed:**
- **P-1** — working-tree-durable metering + committed boundaries; clean-HEAD scoped to exclude exactly the five active runtime paths; per-boundary staged sets enumerated (§B).
- **P-2** — dedicated `runtime/T_RUNTIME.lock`, `flock(LOCK_EX)`, held across the full read→anchor→verify→append→update→fsync→post-verify (§B).
- **P-3** — exactly eight state-bearing events enumerated; `T_PROCESS_STARTED` non-bearing; cache == last state-bearing event (§C).
- **P-4** — WP-4 held-fd `samestat` anchoring required for all runtime artifacts; append descriptor must equal the held anchor (§B).
- **P-5** — `CLOCK_MONOTONIC` + `boot_id`; UTC whole-seconds; a lease can't span reboot/power-off (§D).
- **P-6** — `t-envelope-active.v1` schema; activation supersedes `verify_officina_wp12` (which must then refuse `ACTIVE_TREE_REQUIRES_ACTIVE_VERIFIER`) (§C).
- **P-7** — literal staged sets + the three exact `Co-Authored-By` trailers (§B).

**New mechanisms sound:** the 60 s × 4 liability model (reserve-ahead, charge actual delta on heartbeat, charge full 60 device-seconds on crash/miss — never under-charges, bounds overshoot, amendment-locked); process-tree/device identity (SHA-256-bound, one process group, children in-group, behavior-change closes+charges); atomic head/state handoff (new anchors verified before old released); failure/recovery (facts only, no learner metrics, no auto-retry, no charge-erase); capability issuance (production sources walled off from the WP-4 test-only symbols via the source verifier; 12-file hash-pinned control allowlist revalidated at every step). **No WP-6 numeric prematurely chosen; no WP-4 cell deferred** — the liability constants are amendment-locked runtime engineering values.

**Minor (non-blocking, to honor in implementation):** V2-m1 (reconcile the prose "`T_INVALID_CLOCK`" with the authoritative `T_RUNTIME_INVALID` + `invalid_cause=CLOCK`), V2-m2 (declare the nine production ledger events a *closed* set), V2-m3 (clarify the `T_RUNTIME_INVALID` event vs `t-runtime-invalidity.v1` record relationship). None changes a schema, event, durability point, or lock rule.

**Eligible surface:** inactive implementation + disposable-mirror tests only — driver, metered-runtime state-machine library, active-state verifier, disabled generic interface, and the §10 test matrix — with **no** authorization JSON, activation output, real lease/world, learner adapter, registration, breathing qualification, Q/C root, entropy, or E1/E2/E3 spend. Implementation then needs its own X/Y review, the generic harness a separate review, and an activation-authorization candidate + Kirill's token before the driver runs once.

**Confirmed:** no existing file edited, one new confirmation file, authorized/activated nothing, nothing committed; T pristine/`NOT_ACTIVATED`, no `runtime/` dir, predecessor `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
