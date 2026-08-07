Written to `reviews/opus_officina_t_inactive_implementation_review.md`.

## Verdict: `OFFICINA_T_INACTIVE_IMPLEMENTATION_ACCEPTED`

A faithful, fail-closed, **inactive** realization of the v1+v2+v2.1 protocol. No Critical or Major finding; two Minors, non-blocking. The real tree is pristine (`activated:false`, ledger genesis, `runtime/` holds only the reviewed `OFFICINA_T_RUNTIME_LOCK_V1` lock).

**Item audit:**
1. **Schemas/pins/staged-commit/claim-before-mutation** — exact key sets per §C/§D; `validate_authorization` enforces the 12 immutable-control paths ⊆ reviewed + the generic-harness gate + exact command; `_commit_activation` stages exactly the six paths with the three exact trailers; failure after the durable claim writes `INVALID_PROCESS_RECORD` (no auto-retry), pre-claim failure stays pristine.
2. **Authorization newer than `reviewed_code_head`** — `git diff --quiet reviewed HEAD -- <paths>` (empty diff) with clean worktree/empty index; unreviewed source can't enter the byte-pinned production graph.
3. **Runtime lock / substitution / verifier split** — held-descriptor `O_NOFOLLOW` + `samestat` + exact-bytes + `flock`; `verify_bootstrap` returns `ACTIVE_TREE_REQUIRES_ACTIVE_VERIFIER` once `activated:true`; partial-transaction tested.
4. **Nine-event closed vocabulary** — every state-bearing event carries `t_state`, cache == last state-bearing; `T_OPERATIONAL_PAUSE` now state-bearing without breaking pause/resume.
5. **Reservation** — `min(60s, e1_remaining//units, e3_remaining//units)`, concurrency ≤4, aggregate ≤240 device-seconds, one stream = one unit, crossing charge retained (tested).
6. **Process-id/claim/lease/record** — SHA-256 over the exact identity core, `bool` excluded, `CLOCK_MONOTONIC` + `boot_id` pinned, and `reject_scientific_fields` bars the forbidden keys **and** `c1`–`c6` recursively; `NONFINITE_DEVELOPMENT` correctly absent.
7. **Production/test boundary** — `verify_production_boundary` AST-rejects the six test-world symbols in every reviewed `.py` except `world.py`; reflection blocked by the `getattr`/`eval`/`exec` ban.
8. **Deferred harness — correctly and mechanically deferred:** `RealTCapability`/`issue_real_t_capability` **raise**, and activation is **refused until `generic_harness.py` is reviewed and pinned**; the supervisor/watchdog/backend-quiescence and real metering are the harness's job — the inactive core claims no contract it can't enforce.
9. **Suites** — 15 focused / 84 officina / **251 full** pass; inactive verifier OK; active verifier correctly refuses the inactive tree; tree pristine/`NOT_ACTIVATED`.

**Minors:** T-m1 (`reservation_for` returns `None` without encoding the §4 E1-exhausted vs E3-due vs both-zero-first terminal routing — add a testable helper or pin it to the deferred harness), T-m2 (activation's re-derive/commit/post-verify run just outside the `RuntimeLock` — benign for one-shot activation, but extend the lock or note the rationale).

**Next gate:** authorizes **only the generic metered harness design/implementation gate** (§7) under its own bounded review — **no** activation candidate, activation, entropy, real world, learner, lease, E1/E2/E3 spend, breathing check, Q/C, or scientific interpretation.

**Confirmed:** no existing file edited, one new review file, authorized/activated nothing, nothing committed; T pristine/`NOT_ACTIVATED`, predecessor `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
