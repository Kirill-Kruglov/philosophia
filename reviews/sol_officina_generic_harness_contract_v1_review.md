REVISE_OFFICINA_GENERIC_HARNESS_CONTRACT_YLINE

# Sol Y-line — Officina generic harness contract v1 review

Scope: one bounded governance/resource review of
`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V1_DRAFT.md` and Fable's closure
against the signed charter, activation protocol v1 as corrected by v2 and
v2.1, the WP-3 signature, and the WP-4 inactive boundary.

## Verdict

Revision is required. The draft preserves the main phase separation and makes
no learner or scientific choice, but it is not yet a conservative, total,
single-valued harness contract. In particular, it reinstates the superseded
flat-liability recovery rule; does not define a conserving concurrent terminal
settlement; treats response wrapping as sufficient to confine update and
backend state; has no durable, closed-vocabulary resolution for overdue resume
or signed recovery; and calls a timestamped, ordered lineage surface
"order-free." These are operational defects, not grounds to reopen WP-3 or
choose WP-6/WP-9 cells.

## Answers to Fable's four Y-line questions

1. **Liability accounting: no.** Normal serial settlement can be made
   conserving, but the draft undercharges a known late quiescence by replacing
   signed v2.1 section 1's actual-through-quiescence charge with the outstanding
   reservation. Conversely, it gives no global allocation rule when one or
   more concurrent intervals are unknowable, so independent per-lease readings
   of "all remaining E1" can multiply the same remainder. Reservation-only E1
   or E3 pressure from sibling liabilities can also be mistaken for a realized
   boundary. Finally, after the first concurrent close crosses E1, the draft
   does not define how the other already-revoked leases are charged before the
   one exhaustion event.

2. **Information boundary: no.** A release token proves only that a message was
   gated. It does not prevent a learner-update worker from observing its own
   mutated memory, a checkpoint writer from exposing a temporary file, or an
   off-CPU queue from completing into learner-readable storage before durable
   settlement. Nor does it say what happens to outputs of killed, escaped, or
   invalid workers. The lineage exception is also wider than the charter's
   opaque conditioning-only allowance.

3. **E3 semantics: no.** The counters are declared immutable, but the state
   machine has no durable transition by which a rebooted pause becomes
   `RESUME_REVIEW_PENDING` while the state cache still equals the last
   state-bearing ledger event. It also does not classify power loss at every
   cut of pause creation. A pre-checkpoint reboot can therefore be confused
   with an ordinary pause, and a returned in-memory pending state is not a
   durable gate.

4. **Draft-manifest neutrality: no as written.** `created_utc` is an ordering
   field, and an ordered, variable-length `checkpoint_lineage_sha256` tuple can
   carry ordering or arbitrary selected information. Recompute-from-bytes is a
   useful future duty, but it does not make the draft object itself order-free
   or authorize a pre-WP-6 exception into Q/C.

## Further Y-line findings

- The signed v2.1 recovery charge has three mutually exclusive cases: timely
  proven quiescence charges the actual interval within the liability; known
  late quiescence charges the complete actual interval even beyond the
  reservation; unknowable interval or backend cessation consumes the remaining
  lease-eligible E1. Sections 2, 4, and 5 of the draft instead repeatedly say
  to charge the outstanding liability. That is a silent policy change and can
  make deadline-resistant work free after 60 seconds.
- CPU monotonic wall time and off-CPU submitted work are not interchangeable.
  A backend queue may work after its submitting process is frozen or dead, and
  queue depth is not the number of simultaneous behavior-capable streams. The
  adapter API supplies observations but no normative conversion from them to a
  charge.
- `T_RUNTIME_INVALID` is global, yet a fault in one process does not close and
  settle its live siblings. Conversely, a no-process global fault must not
  manufacture a process record. The invalid and valid close orders are also
  incomplete: a valid `T_PROCESS_STOPPED` must hash an already durable process
  record, while an invalid process needs both the runtime-invalidity pair and
  its final invalid process record.
- The draft's global modes are not actually total. `G5` says recovery is
  possible, but no exact signed-recovery artifact, resolution predicate, or
  transition back to admission is defined. `G3`/`G4` have the analogous resume
  gap. Compound E1/E3/invalidity/author-stop/pause boundaries have no dominance
  table. An invalidity that conservatively consumes the last E1 must remain an
  invalid ending; it cannot be relabelled as a valid exhaustion.
- The claim that author stop is outcome-independent is stronger than the
  architecture can enforce. T is openly readable and adaptive, so a human
  discretionary stop may be informed by T. What can and must be mechanical is
  that E3 due/completion, validity, recovery, accounting, and resource-stop
  classification accept only closed non-outcome inputs. A possibly T-informed
  author stop remains a quarantined T decision and has no evidentiary meaning.
- Fixed `t_quarantine` and `scientific_outcome:false` labels are not evidence
  channels, but they cannot be added to the activation protocol's exact closed
  runtime schemas. They belong only to separately closed development-artifact
  schemas. A Q/C reader must reject the source artifact; copying a narrowly
  defined opaque identity digest later is not the same as admitting the T
  artifact.
- The draft does not preselect a learner, Q predicate, alpha, margin, endpoint,
  or device winner, and it preserves the WP-3 T bands and WP-4 capability
  boundary. However, the draft-manifest schema must be explicitly
  non-normative for WP-6 candidate equivalence, and the reserved Q namespace and
  registration slot must not constrain WP-6 to accept any T object or prevent a
  newly reviewed metering-core change.

## Mandatory repairs

The following list is finite and mandatory. A correction should implement each
item literally enough that two independent implementations produce the same
charge, artifact order, terminal classification, and admission decision.

1. **Replace every flat recovery charge with the signed three-case rule.** In
   sections 2.12, 4, and 5 state exactly: timely proven quiescence charges
   `units * (quiescence_reading - last_durable_reading)` and must not exceed the
   reservation; known late quiescence charges that same complete actual formula
   without clipping to the reservation or E1/E3 boundary; an unknowable
   interval or backend cessation invokes the unknown-pool rule in repair 2.
   Reboot, boot-id change, non-increasing/reset monotonic time, process loss,
   escaped or unclassifiable work, and failed backend synchronization select
   only among these cases. Delete every statement that the outstanding
   reservation itself is the recovery charge.

2. **Add one global conserving settlement algorithm.** Under one runtime-lock
   epoch, first revoke all affected capabilities, freeze/terminate all affected
   groups, synchronize every backend, and snapshot every live lease. Let `D0`
   be durable global E1 at entry. For each provably quiesced stream compute its
   known charge once from its last durable cursor. Let `K` be their sum and let
   `R=max(0,E1_cap-(D0+K))`. If any stream is unknowable, debit exactly the one
   global pool `R`, not `R` once per lease; allocate it over unknowable streams
   sorted by `(process_sequence, stream_index)` as `floor(R/m)` each plus one
   nanosecond to the first `R mod m` streams. For such an unknowable batch the
   post-total is `D0+K+R`; known overrun is retained, and the batch consumes all
   remaining E1 without multiplying it. Zero shares after a prior crossing are
   recorded as zero *additional* debit, never as evidence of zero work or as a
   valid close. Append positive charge events only, preserve every liability in
   the invalidity/process records, and forbid new admission throughout the
   batch.

3. **Make reservation arithmetic exact for multi-stream and sibling cases.** For
   a request of `k` streams, after subtracting all other live aggregate
   liabilities, set
   `ell=min(60s,floor(E1_available/k),floor(E3_device_available/k))` and reserve
   aggregate liability `k*ell`, with each deadline shortened to `ell`. A zero
   value caused only by sibling reservations refuses the request and triggers
   settlement/recomputation of those siblings; it appends neither exhaustion
   nor an early review. Append `T_ENVELOPE_EXHAUSTED` only after realized or
   conservative durable E1 reaches the cap. Enter E3 due only after durable
   charged E3 time or UTC actually reaches its boundary.

4. **Define boundary settlement as a batch and add a dominance table.** When a
   settlement reaches E1 or E3, revoke and settle every live lease before any
   terminal/gate decision; permit terminal settlement charges after the first
   numeric crossing. For a fault-free compound boundary use the fixed order
   `E1 exhaustion > E3 due > signed author stop > operational pause > ordinary
   process close`; simultaneous E1/E3 records exhaustion once and retains E3
   due in the post-state. Infrastructure invalidity dominates every valid
   ending: record the charge and invalidity, retain exhausted/due resource
   facts, but never reinterpret that process or programme ending as valid
   exhaustion, pause, censoring, voluntary stop, or author stop. Specify one
   fixed public-cause precedence for simultaneous invalid causes and test every
   pair.

5. **Pin the charge/lease hash relation and conservation equations.** Define
   `T_DEVICE_TIME_CHARGED.active_lease_sha256` as the hash of the exact
   pre-settlement lease. Its `charge_ns` is the only increment to both global
   E1 and that lease's cumulative charge. After the event is durable, the
   successor lease sets its cursor to the captured reading, cumulative charge
   to prior cumulative plus `charge_ns`, prior-charge hash to the event hash,
   and its new exact liability/deadline; no cyclic post-lease/event hash is
   allowed. Seed the initial lease's prior-charge hash with its
   `T_PROCESS_STARTED` entry hash. On final close, the process record's
   cumulative charge includes the final event even though no renewed lease is
   installed. At every rest state require global E1 to equal the sum of all
   durable per-process charges and require live liability to equal the sum of
   exact active-lease liabilities.

6. **Correct close and invalidity ordering.** A valid close is: quiesce; final
   charge; durable final process record whose final-charge hash is that charge
   event; `T_PROCESS_STOPPED` hashing that record; head/state update; lease
   removal; post-verification; exact archival set. A live-process invalid close
   is: conservative final settlement; invalidity detail record;
   `T_RUNTIME_INVALID`; final `T_PROCESS_INVALID` record bound to the event;
   removal of that lease only after verification; invalid-close archival set.
   A global fault with no process creates no process record. Entry into global
   invalidity revokes, settles, and invalid-closes every live sibling; none may
   continue under `G5`.

7. **Specify durable resume and recovery without a tenth event.** Define a
   closed, signed recovery-disposition artifact that binds the invalidity record
   and event, exact ledger/head/state, all charges, every affected process id,
   and a fixed action token; it contains only the v2 section F fact classes.
   Admission may leave `G5` only when every unresolved invalidity has exactly
   one verified disposition and all discrepancies are durably reconciled; the
   next process uses a fresh id and no failed operation is retried or completed
   silently. For overdue reboot resume, append a second
   `T_OPERATIONAL_PAUSE` entry bound to the same verified checkpoint, with the
   fixed reason `RESUME_E3_REVIEW_PENDING`, `resets_e3:false`, and a full
   post-state whose `resume_review_pending` is true; update head and cache by the
   standard transaction before `T_REVIEW_COMPLETED` may clear the flag. This
   uses the existing vocabulary and keeps the serialized cache equal to the
   last state-bearing event. A merely returned in-memory state is insufficient.
   The correction must enumerate exact artifacts, archive sets, and crash cuts
   for both mechanisms.

8. **Make physical pause fail closed at every cut.** Only zero verified leases,
   proven CPU/backend quiescence, final durable charges, an immutable checkpoint
   of the exact claim-enumerated bytes, its state-bearing pause event, head and
   cache equality, directory `fsync`, successful post-verification, and the
   exact pause archival commit create a planned resumable pause. Power loss
   before any one of those conditions is process-loss/reboot invalidity or the
   already specified incomplete-archive signed-disposition route, never a pause
   completed after the fact. Resume accepts a changed boot identity only
   because the pause already proved zero work; missing/ambiguous boot identity
   or UTC rollback is
   record-first invalidity. Restore E1 exactly, advance only E3 calendar time,
   and make overdue review durable before any capability, output, checkpoint,
   or backend submission. Add a crash/power-cut test after every pause and
   resume durable step.

9. **Replace response wrapping with an isolation-and-promotion protocol.** Run
   each oracle result, learner update, and checkpoint operation in a supervised
   worker/backend context whose memory, IPC, file descriptors, temporary paths,
   and backend output buffers are not readable or writable by the adaptive
   controller. The worker holds no independently usable T capability and cannot
   initiate another behavior-capable operation before promotion. Revoke output
   authority before quiescence. Synchronize, capture the result hash, durably
   charge, and only then atomically promote the result
   or checkpoint and issue a one-use token bound to activation, process, lease,
   operation id, result hash, and charge-event hash. A settlement failure,
   killed child, escaped process, queue ambiguity, or invalid close exposes no
   result and cannot promote or reuse its temporary output. Any later handling
   is selected solely by the signed recovery artifact, never by inspecting the
   result. Tests must cover retained responses, mutable in-process updates,
   memory-mapped/filesystem checkpoint escape, pipe/socket inheritance, killed
   supervisor/controller/child, escaped groups, queued work after process death,
   and crash before and after each promotion cut.

10. **Give CPU and off-CPU work distinct, conservative meter contracts.** CPU
    streams may use monotonic elapsed wall time while behavior-capable, including
    blocking/waiting until proven quiescence. For off-CPU work, every submitted
    command holds one declared stream and liability from submission until
    adapter-proven completion or cancellation; overlapping commands consume
    separate units, while merely queued nonexecuting commands do not become
    free and remain liabilities. The adapter must prove active/concurrent versus
    queued state, completion/cancellation, output confinement, and the exact
    monotonic interval for each stream. If any of those facts is not exactly
    measurable, the result is not a CPU-wall-time estimate: it is the
    unknowable case in repairs 1-2. Adapters are static reviewed imports in the
    immutable production graph; reflective discovery is forbidden, and an
    unreviewed backend is ineligible.

11. **Close outcome inputs without pretending open T is blind.** Define closed
    input schemas for E3 completion, resource-stop, recovery, pause, and author
    stop. E3 due/completion and resource decisions are deterministic functions
    only of clocks, charges, identities, integrity, and signed constants;
    recovery receives only v2 section F facts. Learner behavior, result hashes
    as values, update/checkpoint completion as a success signal, losses,
    competence, and free-text reasons are rejected recursively. Learner-driven
    stopping is public `T_PROCESS_VOLUNTARY_STOP`, not resource stop or
    invalidity. State explicitly that a human `T_AUTHOR_STOP` may be informed by
    readable adaptive T unless a separately reviewed blinding procedure exists;
    it is therefore a quarantined T decision whose timing and occurrence are
    conditioning history only, never Q/C evidence or a negative scientific
    destination.

12. **Eliminate every pre-WP-6 ordering/evidence channel.** Remove
    `created_utc` from the draft manifest (or cease calling it order-free and
    require WP-6 never to read it); replace the ordered variable-length lineage
    exception with no pre-WP-6 exception. Runtime exact schemas retain only
    their signed keys. Separately closed T-development schemas, including draft
    manifests and release tokens, carry fixed
    `t_quarantine:"dev-non-citable"` and are rejected as whole artifacts by all
    Q/C entry points. A future WP-6 may independently define and copy only a
    recomputed opaque behavioral-identity/lineage digest required by the
    charter; it must not accept the T artifact, its timestamp, token, tuple
    order/length, eligibility claim, or creation order. Release tokens are
    non-exportable T capabilities and cannot occur in candidate, Q, `H_preC`,
    `selection_scope_id`, or C schemas. Hash values may be tested only for
    identity/equality, never decoded, ordered, selected, or used as a statistic,
    covariate, margin, resource decision, or evidence.

13. **Keep WP-6/WP-9 ownership explicit.** State that the draft manifest is not
    the charter's canonical candidate manifest and binds no future candidate
    equivalence, admissibility, stack-family, breathing-check, competence,
    attempt, promotion, seed, endpoint, horizon, or analysis rule. Reserved
    namespaces and transaction hooks confer no schema or writer authority.
    WP-6 may replace the draft-adjacent surface and may require a newly reviewed
    metering-core change; WP-9 remains owner of all certificate/C numerics and
    science. Preserve `Q_CAP_EXHAUSTED_NO_QUALIFIER`, invalidity, author stop,
    and E1 exhaustion as distinct negative/process destinations with no success,
    equivalence, boundary, censoring, or impossibility interpretation.

14. **Reconcile transaction recovery, roots, and tests with the immutable
    implementation boundary.** Resolve the cache-cut contradiction: only an
    interrupted, fully derivable cache/lease successor in the same transaction
    may be completed idempotently; every other ledger/head/cache mismatch is
    record-first invalidity. Use the immutable verifier's exact production roots
    (`scripts/officina_activate_t.py`, `scripts/verify_officina_active.py`, and
    `src/philosophia/officina/generic_harness.py`) or obtain a separately
    reviewed control amendment; do not silently add
    `scripts/officina_t_process.py`. Pin sole capability issuance and runtime
    writers, static adapter imports, fake-type exclusion, and every durable path.
    Expand the fault matrix to the concurrent batches, unknown-pool allocation,
    all pause/resume/recovery cuts, output-isolation escapes, simultaneous
    terminal precedence, and proof that no invalid process becomes a valid
    terminal or automatic retry.

## Positive boundaries retained

The selected E1/E2/E3 constants, four-stream cap, T bands, signed frame, total
wire classifier, T/Q/C phase separation, permanent T/Q non-citability, pre-WP-6
E2 barrier, and absence of Q/C issuers are preserved. The draft chooses no
learner, architecture, optimizer, candidate, device winner, breathing-check
numeric, Q predicate, alpha, margin, endpoint, or scientific outcome. The
release-token idea and adapter abstraction may remain after the repairs; they
are implementation mechanisms, not protocol amendments.

This review authorizes only correction of the contract and one bounded
confirmation of those repairs. It authorizes no implementation, production
call-graph manifest, contract signature, activation authorization, activation,
capability, world, learner, entropy, draft-manifest instance, E1/E2/E3 spend,
candidate registration, Q/C object, scientific lock, escrow, datum, outcome, or
claim movement. T remains `NOT_ACTIVATED`; the predecessor remains immutable,
`OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; the programme claim remains `OPEN`.
