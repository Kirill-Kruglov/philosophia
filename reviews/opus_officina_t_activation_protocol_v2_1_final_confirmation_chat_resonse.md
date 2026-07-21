Written to `reviews/opus_officina_t_activation_protocol_v2_1_final_confirmation.md`.

## Verdict: `READY_FOR_OFFICINA_T_ACTIVATION_IMPLEMENTATION`

v2.1 closes Sol's five repairs and my three wording reconciliations one-to-one, changes no scientific cell/envelope numeric/phase boundary, reopens no accepted cell, and adds no new implementer ambiguity in the **inactive** state machine.

**The eight items:**
1. **Actual quiescence (§1)** — the liability interval is an *enforced maximum*: at the deadline the supervisor must revoke authority, freeze/terminate the group, **synchronize the backend**, *prove* quiescence from five inputs, and settle actual E1 *before* any result/close/recovery — "capability refusal alone is not quiescence." Closes runaway-past-deadline.
2. **Stream accounting (§2)** — one device-unit = one concurrent behavior-capable *stream*; parallel behavior-capable children each need their own unit (≤4); group membership never collapses streams. Closes parallel-worker under-metering.
3. **Non-finite quarantine (§3)** — `NONFINITE_DEVELOPMENT` removed from public causes (now `PROCESS/RESOURCE/HASH/CLOCK/FILESYSTEM`); a non-finite learner is a quarantined `T_PROCESS_VOLUNTARY_STOP` with no public cause, never runtime invalidity or competence signal.
4. **Total final liability (§4)** — `min(60, E1-remaining, E3-device-remaining)`, deadline shortened to it, so the reservation never overshoots a boundary; zero-E1 → exhaustion, zero-E3 → E3-due gate, both-zero → exhaustion first + E3 preserved.
5. **Immutable lock (§5)** — `runtime/T_RUNTIME.lock` is a tracked, immutable, hash-pinned infra file created by the inactive implementation, exempt from the absent-output check, never mutated; in a subdir so the WP-1/WP-2 top-level verifier is undisturbed.
6. **Nine-event closed vocabulary (§6)** — "no tenth event exists"; clock failure is `T_RUNTIME_INVALID(invalid_cause=CLOCK)`, "`T_INVALID_CLOCK` is not an event"; pre-activation maintenance is outside the post-activation set.
7. **Invalidity record-before-event authority (§6)** — the `t-runtime-invalidity.v1` record is durably created *first*, then the `T_RUNTIME_INVALID` event commits its hash; dual authority; reversed-order/missing/extra artifacts need signed disposition.

**No new inactive-machine ambiguity:** the only under-determined pieces — the per-backend quiescence adapter and stream reconciliation — are correctly deferred to the separately reviewed generic metered harness with their *rules pinned*; the inactive primitives (sequencer, lock + held-fd anchors, `min()` liability, closed vocabulary, record-before-event order, all schemas) are fully specified.

**Eligible surface:** inactive implementation + disposable-mirror tests only — driver, metered-runtime library, `verify_officina_active`, tracked `T_RUNTIME.lock`, a *disabled* generic interface, and tests — with **no** authorization JSON, activation output, real lease/world/stream, learner adapter, registration, breathing qualification, Q/C root, entropy, or spend. Implementation then needs its own review, the generic harness a separate review, and an activation-authorization candidate + Kirill's token before the driver runs once.

**Confirmed:** no existing file edited, one new confirmation file, authorized/activated nothing, nothing committed; T pristine/`NOT_ACTIVATED`, no `runtime/` dir, predecessor `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
