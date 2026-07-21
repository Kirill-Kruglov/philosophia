# Officina T activation protocol v2 correction

Status: `CANDIDATE_FOR_XY_CONFIRMATION_NOT_AUTHORIZED`.

This correction carries v1 forward except where sections A-H below replace its
language. It incorporates every Opus P-1..P-7 and Sol R1..R7 finding. It creates
no authorization or runtime artifact and does not activate T.

## A. Functional E1 boundary and immutable control surface

This replaces v1 section 7's zero-E1 paragraph.

E1 ownership is functional, not label-based. Any operation that instantiates or
queries a signed T-band world, evaluates or trains a behavior-capable learner
against it, creates a behavior-bearing checkpoint from it, or uses its
observation to alter learner, optimizer, policy, interface, stack, numerical
mode, or configuration is real-T work and requires an active lease.

Only fixed, precommitted disposable assertions and dummy fixtures that accept no
learner, candidate, draft manifest, adaptive input, or exportable observation
spend zero E1. Production activation and learner sources may not import, call,
receive, or reflectively resolve `test_world_capability`,
`issue_test_t_contact_harness`, `evaluate_test_query`, or
`record_test_t_contact`. The source verifier rejects those symbols in every
production call graph. A label containing `test`, a temporary path, or a dummy
seed never exempts behavior-capable work.

The activation record pins exact hashes for this immutable runtime-control
allowlist:

```text
scripts/officina_activate_t.py
scripts/verify_officina_active.py
src/philosophia/officina/activation.py
src/philosophia/officina/runtime.py
src/philosophia/officina/interlock.py
src/philosophia/officina/world.py
src/philosophia/officina/accounting.py
src/philosophia/officina/ledger.py
src/philosophia/officina/checkpoint.py
src/philosophia/officina/terminal.py
src/philosophia/officina/canonical.py
src/philosophia/officina/verification.py
```

The later separately reviewed generic learner harness and active verifier are
added to this list by the final activation authorization; activation is blocked
until they exist and are reviewed. Every claim, capability issue/use, heartbeat,
oracle admission, learner admission, and close revalidates every pinned control
byte. A clean HEAD is necessary but insufficient.

Adaptive learner/config/manifest paths are disjoint from the immutable list,
are hashed in each process claim, and may change only with zero open leases. A
runtime-control change blocks work and requires bounded review plus a signed
amendment/recovery; it is never an in-place T edit.

## B. Runtime lock, descriptor anchors, and durability model

All state-mutating and state-reading transactions use the dedicated file
`successor/officina/runtime/T_RUNTIME.lock`. It is opened with
`O_RDWR|O_CLOEXEC|O_NOFOLLOW`, checked as a regular file at its canonical path,
and held with `flock(LOCK_EX)` across the complete read, descriptor-anchor
validation, verify, append, cache/lease update, fsync, and post-verification
sequence. No state is read for admission outside this lock.

The runtime directory, ledger, external head, state cache, process claim, active
lease, and process record use the held-file-descriptor `samestat` discipline
accepted in WP-4. The descriptor actually opened by ledger append must equal the
held ledger anchor. Atomic head/state successors are opened and verified before
the prior anchors are released. Pathname hashes or recyclable inode tuples alone
are insufficient.

Activation is committed immediately as v1 specifies. During an open lease,
metering artifacts are working-tree-durable and may be dirty: each mutation is
file-fsynced and directory-fsynced, while git archival occurs at the fixed
boundaries below. Clean-HEAD checks exclude only these exact active runtime
paths while their owning lease is verified under the lock:

```text
successor/officina/T_LEDGER.md
successor/officina/T_LEDGER.md.head.json
successor/officina/runtime/T_STATE.json
successor/officina/runtime/T_PROCESS_CLAIMS/<process_id>.json
successor/officina/runtime/T_ACTIVE_LEASES/<process_id>.json
```

No source, configuration, manifest, authorization, or other tracked path may be
dirty or staged. The exact archival sets are:

- activation: claim, state, activation record, active envelope, ledger, head;
- normal/invalid process close: that process claim and final record, state,
  ledger, head; the active lease must be absent;
- E3 review: review record, state, ledger, head;
- planned pause: pause checkpoint, its exact claim-enumerated artifact set,
  state, ledger, head;
- author stop or exhaustion: signed stop/exhaustion record, state, ledger, head,
  plus any process claims/records closed by that boundary.

Each commit stages exactly its enumerated set, rejects a nonempty prior index,
checks set equality independent of order, and uses these exact trailers:

```text
Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
Co-Authored-By: GPT-5.6 Sol <noreply@openai.com>
Co-Authored-By: Codex GPT-5.5 <noreply@openai.com>
```

Commit failure preserves durable working-tree facts and blocks capability; it
never erases charge or creates an automatic retry.

## C. Closed activation and state schemas

The active envelope schema is
`philosophia.officina.t-envelope-active.v1`. Its exact fields are the inactive
envelope fields plus `activated_utc`; `activated` is exactly true and every
resource value/token is byte-equal to the signed inactive envelope.

The activation claim, state, and record schemas are respectively:

```text
philosophia.officina.t-activation-claim.v1
philosophia.officina.t-state.v2
philosophia.officina.t-activation-record.v1
```

The future authorization schema has exactly these keys:

```text
schema, scientific_outcome, execution_once, token, reviewed_code_head,
reviewed_source_paths, reviewed_source_sha256, governing_sha256,
protocol_sha256, envelope_token, device_policy_token, canonical_paths, command
```

The activation claim has exactly:

```text
schema, scientific_outcome, authorization_sha256, reviewed_code_head,
reviewed_source_sha256, governing_sha256, protocol_sha256, created_utc,
canonical_paths, pre_state_sha256, planned_event, planned_t_state_sha256
```

The activation record has exactly:

```text
schema, scientific_outcome, validity, authorization_sha256, claim_sha256,
reviewed_code_head, reviewed_source_sha256, governing_sha256, protocol_sha256,
created_utc, t_state_sha256, active_envelope_sha256, ledger_entry_sha256,
ledger_head_sha256, immutable_control_sha256
```

`validity` is exactly `VALID_PROCESS_RECORD`. Hash maps use repository-relative
POSIX paths sorted by canonical JSON. Canonical path maps use the fixed logical
names `envelope`, `ledger`, `ledger_head`, `runtime_root`, `state`, `claim`, and
`record`; values are resolved absolute paths. Unknown or missing fields refuse.

The active envelope has exactly:

```text
schema, scientific_outcome, activated, activated_utc, device_hour_cap,
candidate_registration_cap, checkpoint_elapsed_calendar_hours,
checkpoint_device_hours, device_hours_are_aggregate, ledger,
strict_s_available
```

Exactly these ledger events are state-bearing and contain a full post-`t_state`:

```text
T_ACTIVATED
T_DEVICE_TIME_CHARGED
T_REVIEW_COMPLETED
T_OPERATIONAL_PAUSE
T_PROCESS_STOPPED
T_RUNTIME_INVALID
T_AUTHOR_STOP
T_ENVELOPE_EXHAUSTED
```

`T_PROCESS_STARTED` is non-state-bearing. The canonical state cache must equal
the last state-bearing event. No other event may advance or carry `t_state`.

Activation supersedes the inactive `verify_officina_wp12.py` contract for the
real tree. After activation that verifier must refuse with an explicit
`ACTIVE_TREE_REQUIRES_ACTIVE_VERIFIER`, and `verify_officina_active.py` becomes
governing. Tests exercise both modes only in disposable mirrors.

## D. Exact E1 reservation and clock contract

The reviewed engineering constants, chosen before any T observation, are:

```text
HEARTBEAT_LIABILITY_SECONDS = 60
MAX_CONCURRENT_LEASES = 4
DEVICE_UNITS_PER_LEASE = 1
MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS = 240
```

One lease represents one behavior-capable controller process tree and always
charges one device-unit, regardless of CPU/off-CPU backend or physical sharing.
Four simultaneous process trees therefore reserve four independent units and
accrue additively. Changing any constant requires review and a pre-activation
authorization amendment; it cannot be selected from T performance.

UTC is read only as `datetime.now(timezone.utc)`, serialized to canonical whole
seconds. It may advance E3 but never precede activation, the last review, or the
last ledger timestamp. Rollback/disagreement is `T_INVALID_CLOCK`; a forward
correction may conservatively make review due.

Elapsed work uses Linux `time.clock_gettime_ns(time.CLOCK_MONOTONIC)`, which
excludes suspended time. Boot identity is the exact ASCII value read from
`/proc/sys/kernel/random/boot_id` and is stored in every lease. A lease cannot
span reboot or power-off. Missing/changed boot identity, unavailable clock, or a
non-increasing cursor invokes the outstanding-liability rule.

Each lease stores exactly: schema, scientific_outcome=false, process id and
sequence, controller PID and process-start identity, declared process-group
scope, canonical argv, behavior-source/config/stack/numerical-mode hashes,
device identity and unit count, UTC start, clock kind, boot identity, initial
and last-charged readings, cumulative actual charge, 60-second deadline,
60-device-second outstanding liability, and prior charge-event hash.

The runtime schemas are fixed as:

```text
philosophia.officina.t-process-claim.v1
philosophia.officina.t-active-lease.v1
philosophia.officina.t-process-record.v1
philosophia.officina.t-review-record.v1
philosophia.officina.t-runtime-invalidity.v1
```

The process claim keys are exactly:

```text
schema, scientific_outcome, activation_record_sha256, process_id,
process_sequence, controller_pid, controller_start_identity, process_group_id,
argv, behavior_source_sha256, config_sha256, stack_sha256,
numerical_mode_sha256, device_identity, device_units, created_utc, clock_kind,
boot_identity, start_reading_ns, immutable_control_sha256
```

The active lease keys are exactly the claim keys plus:

```text
last_charged_reading_ns, cumulative_charge_ns, heartbeat_deadline_ns,
outstanding_liability_ns, prior_charge_event_sha256
```

The final process record keys are exactly:

```text
schema, scientific_outcome, validity, disposition, invalid_cause,
activation_record_sha256, process_claim_sha256, process_id, process_sequence,
behavior_source_sha256, config_sha256, stack_sha256, numerical_mode_sha256,
device_identity, device_units, started_utc, closed_utc,
cumulative_charge_ns, final_charge_event_sha256, final_t_state_sha256,
immutable_control_sha256
```

`invalid_cause` is null for valid dispositions and one exact invalid enum value
for `T_PROCESS_INVALID`. A review record contains exactly:

```text
schema, scientific_outcome, validity, authorization_sha256,
activation_record_sha256, pre_state_sha256, post_state, post_state_sha256,
ledger_entry_sha256, ledger_head_sha256, reviewed_utc, prior_review_utc,
prior_review_device_nanoseconds, author_decision_sha256
```

The invalidity record contains exactly:

```text
schema, scientific_outcome, validity, invalid_cause, transaction_kind,
durable_step_index, affected_path_sha256, clock_kind, boot_identity,
observed_utc, outstanding_liability_ns, required_action
```

Its validity is `INVALID_PROCESS_RECORD`; required action is exactly
`SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY`.

Before a capability is issued or renewed, the global transaction reserves the
lease's 60-device-second liability. It refuses if charged E1 plus all live
liabilities would exceed 168 device-hours, or if device-time since the last E3
review plus live liabilities would exceed 40 device-hours. It also refuses a
fifth concurrent lease. The conservative reservation may leave less than 60
seconds unused at a boundary; that is an accepted resource cost, never a result.

A heartbeat under the global lock settles only the cursor delta, appends full
global and per-lease post-state, replaces state/lease cursors, and renews the
60-second liability. A watchdog revokes capability at the deadline. Oracle
answers, learner-update completion, and behavior-bearing checkpoints are
released only after a current lease and post-operation settlement. Missed
deadline, process loss, reboot, or clock ambiguity charges the full outstanding
60-device-second liability before any recovery, never zero. The crossing charge
is retained; every live lease is revoked at an E1/E3 boundary.

Process id is SHA-256 of canonical JSON containing activation-record hash,
monotone process sequence, exact behavior-source/config/stack/numerical-mode
hashes, canonical argv, device identity, and boot identity. A used id or
sequence is never reused.

The controller owns one declared process group. Every child worker must remain
in that group and under the same lease; child creation and membership are checked
at every admission. Device identity/count, source, configuration, numerical
mode, argv, and process group are immutable while open. A behavior-relevant
change closes and fully charges the lease, then requires a new claim. Concurrent
charges serialize into the one global state.

## E. Validity-first T reporting

Every T artifact has `scientific_outcome:false` and a closed schema containing
only authorization, lineage, source/stack/device, clock, resource, validity, and
routing fields. The allowed per-process dispositions are exactly:

```text
T_PROCESS_CLOSED
T_PROCESS_VOLUNTARY_STOP
T_PROCESS_RESOURCE_STOP
T_PROCESS_INVALID
T_PROCESS_E1_EXHAUSTED
T_PROCESS_E3_DUE
```

Invalid causes are exactly `PROCESS`, `RESOURCE`, `HASH`, `CLOCK`, `FILESYSTEM`,
and `NONFINITE_DEVELOPMENT`. The last is a quarantined development fact, never
censoring or learner impossibility. E3 due and operational pause are nonterminal
gates. `T_ENVELOPE_EXHAUSTED` is set only by E1 or, after WP-6 exists, E2.
`T_AUTHOR_STOP` requires its signed review-bound transaction.

Public records and ledgers forbid arm, contrast, score/loss/accuracy series,
competence, pass/fail, censoring, `INSUFFICIENT`, equivalence, boundary, effect,
margin, C1-C6, or outcome-summary fields. Quarantined T observations and
checkpoints may support adaptive development and eventual selected-candidate
lineage, but are never public process semantics or C analysis inputs. Every T
ending proves only its recorded process/resource history.

## F. Recovery and pre-claim disposition

Recovery packets contain only authorization, filesystem, clock, lease, charge,
hash, and process-validity facts. Learner observations and tuning metrics are
unavailable to the recovery decision. Recovery cannot delete/reuse a claim or
process id, erase charge, reset E3, change constants, or resume before every
outstanding liability and state/ledger discrepancy is durably reconciled.

A failure before durable activation claim creates no T exposure but consumes the
one invocation authorization. Another invocation requires a new exact bounded
pre-claim disposition and a newly committed one-shot authorization; there is no
standing retry. Any later failure follows v1's signed invalidity route.

## G. Evidence, E2, and learner-harness boundary

`H_preC` and `selection_scope_id` may commit hashes of T, breathing, E3, and
selection history solely as conditioning/lineage metadata. Neither a hash nor
its underlying T/Q value is a covariate, statistic, effect estimate, competence
fact, margin input, subgroup, decision input, or evidence.

Draft manifests before WP-6 are explicitly `unregistered`, `q_ineligible`, and
order-free. WP-6 later recomputes behavioral identity from exact source/stack
bytes, ignores draft eligibility or queue claims, charges E2 once, and remains
the only Q-submission route.

Inactive implementation may include a disabled generic learner/world interface,
but actual activation remains blocked until a concrete generic metered harness
and its complete oracle, subprocess, device, update, checkpoint, and test-surface
call graph receive separate bounded X/Y review. That review selects no learner,
optimizer, stack, candidate, or expected winner; it proves only that every
behavior-capable route is leased and metered.

## H. Revised gate

A positive review of v1 as corrected by v2 may authorize inactive implementation
and disposable-mirror tests only. Production authorization JSON, activation
outputs, real leases/worlds, a concrete learner adapter, candidate registration,
breathing qualification, Q/C roots, entropy, and scientific fields remain
absent. Implementation then needs X/Y review; the generic harness needs separate
review; only afterward may an exact activation authorization candidate be
prepared for Kirill.

No activation token is signable from this correction. T remains pristine and
`NOT_ACTIVATED`; no E1/E2/E3 spend or claim movement occurred.
