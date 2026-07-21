# Officina T activation and metered-runtime protocol v1 draft

Status: `CANDIDATE_FOR_XY_REVIEW_NOT_AUTHORIZED`.

This document is the separately reviewed T-activation candidate made eligible
by the WP-4 X/Y confirmations. It is a protocol for later implementation and
tests. It is not an activation record, an authorization, a real-world object, a
candidate registration, or a run. T remains `NOT_ACTIVATED` at genesis.

Review base: commit `ac7034e32396b9c027d5c59d1151b5a93ab744c6`.

## 1. Governing pins

The future implementation and driver must refuse unless the following exact
documents are present and hash-identical:

| Artifact | SHA-256 |
|---|---|
| `successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md` | `aacea407e7cb436ac2092ddb8424a2ceab94e5fb67e3d164fea2511b23ede203` |
| `successor/OFFICINA_WP3_SIGNATURE.md` | `24fd12b61d2fb75c38adee4bebda498f6ca67aade5e08b412c39530289086781` |
| `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md` | `6085d9b695e2a74c0b46c56bc61971d29dd6b646a5ae70068e33c93090735c7d` |
| `successor/OFFICINA_WP4_IMPLEMENTATION.md` | `8d27c338fc562b45bfc3179909c6d8609ff5ada1e378a04936f1e48afe530d14` |
| `reviews/sol_officina_wp4_anchor_confirmation.md` | `42b46cdb5cbd6f9a8ade99dcce165716fb87ac9488b0cb094f6e306597175804` |
| `reviews/opus_officina_wp4_anchor_confirmation.md` | `fd25a6fc3af306def242df4c1077c5eb2d75d9218b78f0c02e66d8dba23d79a2` |

The signed resource contract remains exactly E1 = 168 aggregate device-hours,
E2 = 12 behavior-distinct canonical registrations, and E3 = the first of 48
elapsed calendar hours or 40 newly consumed device-hours. Off-CPU development
is permitted. Off-CPU qualification numerics remain a WP-6 cell.

## 2. Four boundaries that must not collapse

1. **T activation** starts the E3 calendar clock and changes the public process
   state from pristine genesis to active. It is non-scientific.
2. **A real-T work lease** is the only authority that may instantiate a world
   in the signed T bands or train a registrable learner on it. Every such lease
   consumes E1 by aggregate active process time. It is non-citable development.
3. **Canonical candidate registration** consumes E2, but remains mechanically
   unavailable until the separately signed WP-6 Q contract exists. T may create
   draft manifests before WP-6; they are not registrations and convey no Q
   eligibility.
4. **Scientific evidence** can arise only in an independently locked C run.
   Neither activation, T leases, tuning observations, breathing checks, draft
   manifests, E3 reviews, nor any T ending can move C1-C6.

## 3. Future authorization artifact

Implementation review may make an exact authorization candidate eligible, but
this draft does not create it. The future tracked canonical JSON record must
contain exactly:

- schema `philosophia.officina.t-activation-authorization.v1`;
- `scientific_outcome: false`, `execution_once: true`;
- token `I_AUTHORIZE_OFFICINA_T_ACTIVATION` signed by Kirill;
- the reviewed implementation commit and exact reviewed-source path list;
- hashes of every artifact in section 1 and of this final accepted protocol;
- the selected envelope and device-policy tokens verbatim;
- the canonical runtime paths and the one invocation command.

The authorization commit must be HEAD, the index and tracked worktree must be
clean, all reviewed source bytes must match their reviewed commit, and every
activation output must be absent. A pre-existing temporary or final output is a
refusal, never a delete-and-retry instruction.

## 4. Canonical runtime artifacts

The implementation candidate must reserve these paths without creating them in
the real tree during tests:

```text
successor/officina/runtime/T_ACTIVATION_CLAIM.json
successor/officina/runtime/T_STATE.json
successor/officina/runtime/T_ACTIVATION_RECORD.json
successor/officina/runtime/T_PROCESS_CLAIMS/<process_id>.json
successor/officina/runtime/T_PROCESS_RECORDS/<process_id>.json
successor/officina/runtime/T_ACTIVE_LEASES/<process_id>.json
successor/officina/runtime/T_TRANSACTION_INVALIDITY_REQUIRED.json
```

`T_ENVELOPE.json`, `T_LEDGER.md`, and its external head remain the public
governing artifacts. Runtime state is a checked cache of the last state-bearing
ledger event, never an authority that can contradict or truncate the ledger.
All JSON is canonical ASCII with a trailing newline and is durably installed by
same-directory write, file `fsync`, atomic no-replace or replace as specified,
and parent-directory `fsync`.

## 5. Activation transaction

One timestamp is captured once from canonical system UTC and reused throughout
the transaction. The driver holds an exclusive lock on the resolved canonical
runtime directory and performs, in order:

1. validate the authorization, git state, governing pins, pristine inactive
   envelope, exact genesis ledger/head, absent runtime outputs, path quarantine,
   and no open process lease;
2. durably create `T_ACTIVATION_CLAIM.json`, binding all preflight hashes,
   reviewed HEAD, timestamp, intended event, paths, and post-state;
3. durably create `T_STATE.json` containing `TState().activate(timestamp)`;
4. append exactly one `T_ACTIVATED` event containing the authorization hash,
   claim hash, selected envelope/device-policy tokens, and full post-state;
5. atomically replace `T_ENVELOPE.json` with the identical signed envelope plus
   `activated:true` and `activated_utc:timestamp` under a new explicit schema;
6. durably create `T_ACTIVATION_RECORD.json`, binding the claim, state,
   envelope, ledger entry/head, authorization, source commit, and timestamp;
7. re-derive and verify the whole active state, then commit exactly the claim,
   state, record, envelope, ledger, and head with fixed authorship trailers.

No real-world/work capability exists before step 7's commit succeeds. A failure
before durable claim creation leaves pristine T and permits only a newly
reviewed invocation. Any failure from durable claim through successful exact
commit is `T_ACTIVATION_INVALID:PROCESS`: no automatic retry, completion,
rollback, deletion, or capability issuance. A bounded signed recovery decision
must classify the durable state. If activation became durable before a commit
failure, its recorded timestamp still governs E3; git failure never creates
free calendar time.

## 6. Active-state verification and capability issuance

A later process may receive a real-T capability only when all of these are true:

- authorization, claim, record, active envelope, state, ledger, and external
  head are tracked, canonical, hash-linked, mutually exact, and at the current
  clean HEAD;
- no activation-invalidity artifact or incomplete transaction exists;
- state is active, not author-stopped, not resume-review-pending, not exhausted,
  and not E3-due at the current canonical UTC time;
- the caller has first created a durable real-work lease as section 7 requires.

The capability is exact-type, private-token issued, bound to the activation
record, process id, source HEAD, T bands, and lease identity. Every constructor
and every oracle/learner-facing use revalidates those fixed fields. It cannot be
relabelled Q/C, copied to another process, used after lease closure, or used for
the registered frame `[26,65]` or predecessor `[66,125]`.

## 7. E1 real-work leases and parallel metering

E1 measures aggregate active time of processes that can touch real T worlds or
train a registrable learner. A process using `k` devices accrues `k * elapsed`
device-nanoseconds; `k` is a positive integer durably declared before access.
Concurrent leases accrue independently and therefore add. Tests, dummy worlds,
and code paths mechanically lacking a real-T capability spend zero E1.

For each behavior-capable process:

1. refuse if its canonical process id, claim, lease, or final record exists;
2. under the exclusive runtime lock, verify active availability and E3;
3. durably create a process claim with source/command/stack identities, device
   count, UTC start, and an explicitly non-reusable process id;
4. append `T_PROCESS_STARTED` before installing the active lease and before
   returning any real-T capability;
5. measure with a monotonic clock that excludes powered-off intervals; each
   heartbeat/close computes only the uncharged delta from the same process;
6. under the runtime lock, add the delta to the latest globally verified state,
   append a full-state `T_DEVICE_TIME_CHARGED` event, then replace `T_STATE.json`;
7. recheck E1 and E3 before every subsequent real-world/learner admission;
8. on normal close, charge through the close boundary, append
   `T_PROCESS_STOPPED`, durably create the final process record, and remove the
   active lease only after the record is verified.

The ledger is the authority when state-cache replacement is interrupted. Any
orphaned claim, start without lease, lease without a matching start, state/ledger
disagreement, open lease after process loss, non-monotone clock, or ambiguous
charge is fail-closed `T_RUNTIME_INVALID:PROCESS`. It gets no automatic retry or
estimated zero charge. Recovery requires a signed bounded decision; actual
overrun is recorded rather than clipped or erased. New work is refused once E1
is exhausted, but the final charge that crosses E1 is retained in full.

The implementation must make the maximum uncharged interval a named engineering
constant and enforce heartbeat at every oracle contact and learner update. This
constant limits accounting loss; it is not a scientific or learner hyperparameter
and must be fixed before activation review.

## 8. E3 reviews, pause/resume, and author stop

Every work admission and heartbeat checks both E3 clocks against actual UTC and
the globally charged state. When due, elapsed E1 is charged through the boundary,
all capabilities become unusable, and only a durable `T_REVIEW_COMPLETED`
transaction can advance `last_review_utc` and its device counter.

A planned power-off requires zero active leases, a checkpoint covering all
registrable learner/runtime artifacts, full charge through quiescence, the
existing hash-linked `T_OPERATIONAL_PAUSE`, and verified `fsync` completion.
Resume uses the existing `ResumeGate`; powered-off time advances E3 but not E1.
If E3 is due, the serialized resumed state itself rejects work until the durable
review clears `resume_review_pending`.

`T_AUTHOR_STOP` is accepted only with a separately tracked Kirill signature
bound to a just-completed E3 review and exact ledger/state head. It is distinct
from `T_ENVELOPE_EXHAUSTED` and operational pause. Neither ending is science.

## 9. E2, WP-6, and breathing-check boundary

This activation package must not expose a production candidate-registration
method. The existing canonical manifest functions may be used on T drafts, but
no call may update `candidate_ids`, consume E2, arm Q, or claim eligibility.

WP-6 must first freeze candidate-blind Q numerics, attempt/depletion/alpha rules,
stack-family identity, and the off-CPU breathing-check tolerance and procedure.
Only then may a separately reviewed registry transaction consume E2. A breathing
check is non-citable engineering and cannot enter a competence predicate or C
analysis. CPU and off-CPU T development are both allowed; neither inherits a
scientific platform claim from Level 0.

## 10. Required implementation tests

All positive paths execute only in disposable repository mirrors. Tests must
cover at least:

- every activation preflight mutation, stale HEAD/source pin, dirty/staged tree,
  untracked authorization, existing output, alias, and partial transaction;
- failure injection after each durable activation step and no automatic rerun;
- exact staged-path commit set and refusal to issue capability before commit;
- active-state re-derivation from ledger and detection of every cache/head/hash
  disagreement;
- T-band endpoints and complete rejection of Q/C/predecessor moduli;
- serial and concurrent additive E1 metering, bool/zero/negative device counts,
  overshoot retention, exhausted refusal, monotonic-clock failure, and bounded
  heartbeat enforcement;
- crash/orphan/duplicate process states and no uncharged real-world access;
- E3 wall/device boundaries, review completion, author stop, planned 96-hour
  power-off pause, powered-off resume, overdue review, and immutable counters;
- proof that candidate registration, breathing qualification, Q/C entry points,
  entropy, learner policy, and scientific terminals remain absent or fail-closed;
- full repository suite, inheritance/decision verifiers, and an active-state
  verifier exercised only on a temporary mirror.

## 11. Gate and negative space

The only next action authorized by this draft is bounded X/Y review of the
protocol. Even a positive protocol review authorizes implementation and tests,
not activation. Implementation then needs its own X/Y review, followed by a
separate exact authorization candidate and Kirill's explicit token. The real
driver is invoked exactly once only after that final execution authorization.

No current token authorizes `I_AUTHORIZE_OFFICINA_T_ACTIVATION`; do not sign it
from this draft. No entropy, real world, process lease, E1/E2/E3 spend, learner,
candidate, Q/C activity, datum, outcome, or claim has been created. T and Q are
permanently non-citable for C1-C6. The programme claim remains `OPEN`.
