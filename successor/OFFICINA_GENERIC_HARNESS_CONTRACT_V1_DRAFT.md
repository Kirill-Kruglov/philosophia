# Officina generic metered harness contract — v1 draft

Status: `CANDIDATE_FOR_XY_REVIEW_NOT_AUTHORIZED`. This is the
protocol-level contract for the generic metered learner harness — the
single named object on which T activation is mechanically blocked. It
is drafted under the independent programme validation
(`READY_FOR_OFFICINA_GENERIC_HARNESS_CONTRACT`) and the signed
activation protocol (v1 + v2 + v2.1), whose every constant, schema,
event, and boundary it inherits unchanged. It is generic
infrastructure: it selects no learner, architecture, optimizer,
training rule, certificate numeric, Q predicate, alpha, margin,
candidate, device winner, or scientific endpoint.

**Deliberately unpinned:** no implementation hash, reviewed code HEAD,
or production source set is pinned here; the bounded residual
confirmations of commit `2277331` are pending and pins belong to the
future implementation review and activation authorization. The current
267-test suite is engineering evidence only.

This contract creates nothing executable: no `generic_harness.py`, no
`runtime_control/PRODUCTION_CALL_GRAPH.json`, no authorization, no
activation, no capability, no world, no learner, no entropy, no
candidate, no E1/E2/E3 spend, no runtime or Q/C datum. T remains
`NOT_ACTIVATED` at genesis.

---

## 1. Scope and authority

The harness is the **only future issuer and revoker of exact real-T
capabilities.** After activation, every behavior-capable operation —
instantiating or querying a signed T-band world, evaluating or
training a behavior-capable learner, creating a behavior-bearing
checkpoint, or using a T observation to alter learner/optimizer/
policy/interface/stack/numerical mode/config (the v2 §A functional
boundary) — exists only inside a harness-issued, leased, metered
capability. No other code path may construct one; the capability type
retains no public constructor and no issuer outside the harness.

**What activation authorizes:** starting the E3 calendar clock and
admitting harness-supervised, E1-metered, ledgered, permanently
non-citable T development inside the signed T-dev bands
`[10,25] ∪ [166,205]`. **What it does not authorize:** candidate
registration or any E2 consumption (impossible before the signed WP-6
Q contract — the pre-WP-6 barrier of the inactive implementation
stands); Q attempts, entropy roots, Q/C capabilities (their types
remain issuerless); breathing-check *qualification* (its tolerance and
procedure are WP-6 cells); any scientific specification, lock, escrow,
or C activity (WP-9/WP-10); any claim movement. Preserved invariants:
T is adaptive, open, and permanently non-citable for C1–C6; no T
event, log, checkpoint, or ending can become Q/C evidence; no
implementation object, enum, or schema in this contract implies
execution authority — authority exists only as a live, valid,
harness-issued lease.

## 2. Executable lifecycle state machine

**Global T states** (exclusive, total; state-bearing events per the
closed nine-event vocabulary — no tenth event exists):

| State | Entered by | Work admission |
|---|---|---|
| G0 `GENESIS_INACTIVE` | — | none; inactive verifier governs |
| G1 `ACTIVE` | `T_ACTIVATED` | admissible |
| G2 `E3_DUE` (nonterminal gate) | either E3 clock due | refused until `T_REVIEW_COMPLETED` |
| G3 `PAUSED` | `T_OPERATIONAL_PAUSE` | refused until valid resume |
| G4 `RESUME_REVIEW_PENDING` | resume with overdue E3 | refused until durable review |
| G5 `RUNTIME_INVALID` | `T_RUNTIME_INVALID` | refused until signed bounded recovery |
| G6 `AUTHOR_STOPPED` (terminal) | `T_AUTHOR_STOP` | never |
| G7 `ENVELOPE_EXHAUSTED` (terminal) | `T_ENVELOPE_EXHAUSTED` | never (E1; E2 only after WP-6 exists) |

**Per-process states:** P0 `ABSENT` → P1 `CLAIMED` → P2 `STARTED` →
P3 `LIVE` (lease installed, liability reserved, capability usable) →
{P4 `CLOSED_VALID`, P5 `CLOSED_INVALID`}. No other path; no state
falls through, silently retries, erases liability, or reinterprets an
invalid run as a valid terminal.

**Transition table** (preconditions → durable artifacts/events →
postconditions → legal next):

1. **Process claim creation** (P0→P1): G1, no artifact for this
   process id, E1/E3 headroom per the v2.1 §4 `min()` rule, live
   units + requested streams ≤ 4. Durable: process claim
   (`…t-process-claim.v1`, all v2 §D keys incl. controller start
   identity, process group, boot identity, immutable-control map =
   activation record's map). Next: P2 only.
2. **`T_PROCESS_STARTED`** (P1→P2): claim durable and verified.
   Durable: the non-state-bearing start event, hash-linked. Next: P3
   only; a start without a subsequent lease is fail-closed invalidity
   on next admission.
3. **Lease installation** (P2→P3): under the runtime lock, reserve
   liability = `min(60 dev-s, E1 remainder, E3-device remainder)` per
   stream; install active lease (`…t-active-lease.v1`), then and only
   then issue the capability bound to activation record, process id,
   source HEAD, T bands, lease identity. **Renewal** = heartbeat
   settlement (5). Next: P3 cycles or a close path.
4. **Behavior-capable operation** (P3): every oracle admission,
   learner-update admission, and checkpoint creation revalidates the
   pinned control bytes, lease currency, group membership, declared
   stream count, and both E3 clocks; each is followed by settlement
   before its result is released (§7 response gating).
5. **Heartbeat settlement** (P3→P3): under the lock — settle the
   monotonic cursor delta only, append full-state
   `T_DEVICE_TIME_CHARGED`, replace state cache and lease cursors,
   renew the liability and deadline. A missed deadline invokes the
   supervisor quiescence protocol (§5), never a silent extension.
6. **Voluntary stop** (P3→P4): quiesce → final charge through the
   close boundary (`T_DEVICE_TIME_CHARGED`) → `T_PROCESS_STOPPED`
   (full post-state) → final process record
   (disposition `T_PROCESS_VOLUNTARY_STOP` or `T_PROCESS_CLOSED`) →
   lease removed only after record verification → archival commit of
   the exact v2 §B close set. Learner exception/non-finiteness closes
   by exactly this route with no learner-behavior cause or metric
   (v2.1 §3) — it is quarantined development fact, never invalidity.
7. **Resource stop** (P3→P4): same route, disposition
   `T_PROCESS_RESOURCE_STOP`, actual overrun recorded in full, never
   clipped.
8. **E1 exhaustion** (P3/admission→P4 + G7): the crossing charge is
   retained in full; every live lease is quiesced and closed; the
   `T_ENVELOPE_EXHAUSTED` state event is appended exactly once. Zero
   E1 liability at reservation appends the actual exhaustion state
   rather than issuing.
9. **E3 due / completed** (G1→G2→G1): due at either clock — charge
   through the boundary, revoke usability, quiesce; only a durable
   `T_REVIEW_COMPLETED` transaction (review record with exact v2 §D
   keys) advances `last_review_utc` and its device counter. E1/E3
   simultaneous zero: exhaustion recorded first, E3 preserved due in
   the post-state; neither resets the other.
10. **Operational pause** (G1→G3): §6.
11. **Author stop** (G1/G2→G6): only with the separately tracked
    Kirill signature bound to a just-completed E3 review and exact
    ledger/state head; distinct from exhaustion and pause.
12. **Process loss / deadline miss / reboot / clock ambiguity /
    filesystem or hash fault** (P3→P5; G1→G5): record-first
    invalidity (13) with cause `PROCESS`/`CLOCK`/`FILESYSTEM`/`HASH`/
    `RESOURCE`; unknown intervals charge conservatively (§4); the
    lease's outstanding liability is charged in full before any
    recovery, never zero.
13. **Record-first `T_RUNTIME_INVALID`**: first the detailed
    `…t-runtime-invalidity.v1` record is durably created; then the
    state-bearing `T_RUNTIME_INVALID` event commits its hash, typed
    public cause, full post-state, and
    `SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY`. Missing, extra,
    mismatched, or reversed artifacts are themselves unrecoverable
    without signed disposition (v2.1 §6). Recovery packets contain
    only the v2 §F fact classes; learner observations are unavailable
    to recovery decisions.
14. **Resume after ordinary power-off** (G3→G1 or G4): §6.

## 3. Durable transaction ordering

Every transition uses the repository's discipline: canonical ASCII
JSON with trailing newline; same-directory temp write → file `fsync` →
atomic install (no-replace for creations, replace only where the
protocol says replace) → parent-directory `fsync`; the held-descriptor
`T_RUNTIME.lock` (`O_RDWR|O_CLOEXEC|O_NOFOLLOW`, `flock(LOCK_EX)`,
canonical-content check) across read → anchor validation → verify →
append → cache/lease update → fsync → post-verify; ledger append
through the descriptor equal to the held anchor; hash chain to the
external head. **No Git commit is a runtime safety precondition**: git
archival occurs only at the fixed v2 §B boundaries with the exact
staged sets and trailers; commit failure preserves every durable
working-tree fact, blocks capability, and never erases charge or
authorizes retry.

**Canonical ordering template with crash cut-points** (instantiated
per transition; the implementation must enumerate each):

```text
 1. acquire lock; validate anchors, control bytes, state/ledger equality
 2. compute transition; capture clock readings once
 3. write+fsync new dependent artifact(s) (claim / record / review /
    invalidity detail) — atomic no-replace
 4. append ledger event (state-bearing events carry full post-state);
    fsync ledger through held descriptor
 5. atomically replace external head; fsync
 6. atomically replace state cache (and lease cursors); fsync
 7. post-verify: re-derive state from ledger; release lock
[8.] at archival boundaries only: stage exact set, commit with trailers
```

| Crash cut | Durable at crash | Legal recovery |
|---|---|---|
| before 3 | nothing new | re-invoke admission; no charge existed unless a lease was live (then its liability rule governs) |
| after 3, before 4 | orphan artifact | fail-closed on next lock acquisition → record-first invalidity naming the orphan; no deletion, no reuse of the id |
| after 4, before 5 | ledger ahead of head | ledger is authority; head repair is part of signed recovery, never silent |
| after 5, before 6 | cache stale | re-derive from ledger under lock; cache replacement is idempotent and non-authoritative |
| after 6, before 7 | consistent | post-verify on next entry |
| during 8 | runtime facts durable, archival incomplete | capability blocked; commit completed under signed process disposition; charge untouched |

The ledger is always the authority; the state cache is a checked
cache; a cache/ledger disagreement at any entry is record-first
invalidity, not a repair-in-place.

## 4. Metering and liability

Inherited exactly (v2 §D, v2.1 §§1–2, 4): units are
device-nanoseconds of `CLOCK_MONOTONIC` elapsed time × declared
device-units; one unit = one concurrent behavior-capable execution
stream; children doing behavior-inert orchestration ride their
stream's unit, while any child that independently queries a world,
trains/evaluates, or writes a behavior-bearing checkpoint is another
stream requiring its own unit and slot; total live units ≤ 4;
per-stream liability 60 device-seconds; aggregate live liability ≤ 240
device-seconds assertable only when all live trees have timely
quiescence proofs; reservation = `min(60 s, E1 remainder, E3-device
remainder)` with the deadline shortened to the reserved value; refusal
happens **before** overspend — post-hoc truncation does not exist; the
boundary-crossing charge is retained in full.

**Settle-before-release:** every oracle answer, learner-update
completion, and behavior-bearing checkpoint is released to the learner
process only after its charge and integrity transition is durable
(§7). **Conservative charging:** unknown intervals — process loss,
watchdog expiry without provable quiescence, reboot (boot-identity
change), monotonic counter reset or backward motion, backend
synchronization failure — charge the full outstanding liability; if
the interval or backend cessation is unknowable, recovery consumes all
remaining lease-eligible E1 at the last durable cursor (v2.1 §1).
Clock rules: UTC only as canonical whole-second
`datetime.now(timezone.utc)`, monotone against activation/review/
ledger timestamps; violations are `T_RUNTIME_INVALID:CLOCK`.

**Device-meter adapter contract** (no device winner chosen): an
adapter binds a stack family and must provide, with tests —
`monotonic_reading_ns()`; `boot_identity()`; `device_identity()`
(exact hardware/driver/library identity string entering claims);
`declared_streams()` reconciliation against observed workers and
backend queues; `synchronize()` proving submitted work complete or
cancelled; `quiesce(group)` returning a proof object (membership,
process states, sync result, reading, unchanged boot identity). The
CPU adapter uses process/thread enumeration and `CLOCK_MONOTONIC`
directly. An off-CPU adapter must additionally prove queue/stream
synchronization for its backend. **A backend without a reviewed,
testable quiescence/synchronization adapter is ineligible for
activation** (v2.1 §1). Adapter admission is by bounded review of that
adapter; nothing here fixes a breathing-check tolerance or pass
threshold — those are WP-6 cells.

## 5. Supervisor and watchdog

Each controller tree runs under a separate supervisor that owns the
process group and the real-T capability. Contract: controller identity
= PID + kernel start-identity + boot identity, all in the claim; PID
reuse is defeated by start-identity comparison at every admission and
settlement; the declared process group is checked at every admission,
heartbeat, and quiescence proof — an escaped child, excess worker, or
unclassifiable parallelism revokes the group and invokes the
conservative charge; the watchdog owns the deadline and executes the
v2.1 §1 sequence at or before it (revoke authority → freeze/terminate
group members → backend synchronize → prove quiescence → durably
settle actual E1) — capability refusal alone is never quiescence. A
dead controller leaves no usable capability (issuance is
supervisor-held and lease-bound) and no uncharged liability (the
outstanding reservation is charged by the recovery path). Reboot
during a lease is detected by boot identity and routes to the
unknown-interval rule.

**Threat model (stated):** this machinery prevents accidental faults,
process escapes, crashes, clock and filesystem failures, and honest
operator error. It does not defend against a privileged malicious
operator, who can falsify any local measurement; that residual is
procedural (signed records, review), exactly as in every prior
Officina custody statement.

## 6. Power-off, pause, and resume

**Ordinary pause** (planned power-off; the user may need this well
before the 168-device-hour envelope is spent): (1) stop issuance; (2)
quiesce and settle every live stream (v2.1 §1 proof per tree); (3)
voluntarily close all leases (zero active leases is a pause
precondition, per v1 §8); (4) create the pause checkpoint covering
model/optimizer/config/stack bytes and every claim-enumerated runtime
artifact, hashed; (5) append `T_OPERATIONAL_PAUSE` with full
post-state; (6) archival commit of the exact pause set; (7) verified
`fsync` completion before power removal. E1 does not advance while
off; E3 calendar does; neither clock resets.

**Resume:** re-validate control bytes, ledger/head/state chain, pause
checkpoint hashes, boot identity (a *changed* boot identity is
expected and recorded; a *missing* one refuses), and clock
monotonicity against the pause record. Refuse on any mutation,
deletion, substitution, stale lease, boot/clock ambiguity, or
ledger/cache mismatch — refusal is record-first invalidity, not
repair. If E3 became due while off, resume enters
`RESUME_REVIEW_PENDING` and the serialized state itself rejects work
until the durable review clears it.

**Distinctions preserved:** ordinary pause is a non-scientific
operational state, not `T_AUTHOR_STOP` (signed, review-bound,
terminal) and not runtime invalidity (fault-triggered, record-first,
recovery-gated).

## 7. Learner-generic and scientific-data boundary

**Adapter surface (narrow, generic):** a learner process receives
exactly — the sealed contact interface of its leased T world(s)
(oracle answers via the capability), its own declared config/source
bytes, checkpoint read/write through the harness, and release tokens
(below). Infrastructure sees of the learner exactly — process facts
(argv, group, PIDs), resource facts (readings, charges), integrity
facts (source/config/stack/numerical-mode hashes, checkpoint hashes,
lineage), and deterministic-replay facts (declared seeds/streams as
opaque identifiers). **Never visible to infrastructure decisions:**
learner behavior, loss, certificate state, competence, arm labels, or
any scientific interpretation — none may enter recovery, activation,
E3, pause, or author-stop logic (v2 §F, v2.1 §3).

**Non-citable labeling:** every T-development log and checkpoint
carries `scientific_outcome: false` and a `t_quarantine:
dev-non-citable` marker in its schema; Q/C machinery (when it exists)
must mechanically refuse any artifact bearing that marker except the
promoted candidate's lineage hashes as conditioning metadata (v2 §G).

**Response gating:** the capability returns behavior-bearing results
(oracle answer, update completion, checkpoint handle) only wrapped in
a release token issued after the corresponding settlement transaction
is durable. An attempt to read a result before settlement is a
capability violation → revocation + conservative charge. Public
records and ledger events forbid, recursively, every scientific field
class enumerated in v2 §E.

## 8. Draft candidate surface and WP-6 extension points

**Draft manifest** (the only candidate-adjacent object before WP-6):
schema `philosophia.officina.t-draft-manifest.v1`, keys exactly —
`schema`, `scientific_outcome` (false), `q_eligible` (constant false),
`behavior_source_sha256`, `config_sha256`, `stack_sha256`,
`numerical_mode_sha256`, `device_identity`,
`checkpoint_lineage_sha256` (tuple), `created_utc`. It is
**unregistered, `q_ineligible`, order-free** (no sequence, queue, or
priority field exists in the schema), consumes no E2, arms nothing,
and confers no eligibility. WP-6 later recomputes behavioral identity
from exact bytes and ignores every draft-side ordering or eligibility
claim.

**Stable extension points** (names reserved; objects absent until
WP-6's own review): the `philosophia.officina.q-*` schema namespace;
a registration-transaction slot that is the **only** writer of
`candidate_ids` and E2 (absent — the inactive E2 barrier stands); a
Q-capability type with no issuer; attempt-claim ledger integration via
the same append/state machinery. WP-6 adds its reviewed objects
through these points **without modifying the metering core**; any core
change is a new bounded review, not a WP-6 side effect.

## 9. Production call-graph duty

The future implementation produces
`runtime_control/PRODUCTION_CALL_GRAPH.json` (schema
`philosophia.officina.production-call-graph.v1`) only when its own
review authorizes creation; **it must remain absent until then.**
Duties: exact executable roots (`scripts/officina_activate_t.py`,
`scripts/verify_officina_active.py`, and the harness CLI added by the
authorization); every repository-local transitive dependency
enumerated; all asserted sources reachable from roots and nothing
unreachable asserted; no ambiguous resolution, dynamic
import/reflection, hidden entropy, or test-only capability symbol
(`test_world_capability`, `issue_test_t_contact_harness`,
`evaluate_test_query`, `record_test_t_contact`) in any production
graph; no inherited Level 0/Level 1 behavior dependency (path
quarantine); exact reviewed source bytes with reviewed-commit
provenance for every node. The activation authorization then adds the
harness and manifest to the immutable-control allowlist (v2 §A), and
every admission revalidates the pinned bytes.

## 10. Verification and fault-injection matrix

All positive paths run only in disposable roots/mirrors with fake
clocks/meters and test-only worlds; no test may create a
production-compatible real-T artifact. Deterministic unit/integration
coverage is required for **every** §2 transition and **every** §3
crash cut, plus at least:

| Fault / probe | Required behavior |
|---|---|
| concurrent streams: 4 live units + 5th request; multi-stream controller under-declaring | refusal; reconciliation revokes + conservative charge |
| aggregate liability overflow near shortened E1/E3 boundaries | `min()` reservation; no over-reservation; shortened deadline |
| killed controller; killed child; PID reuse (same PID, new start identity); escaped child | conservative charge; no usable capability; record-first invalidity |
| missed heartbeat with quiescence proof / without proof | upper-bound vs full-liability (or unknowable-interval) charge |
| monotonic reset / backward motion; boot-identity change mid-lease | `CLOCK` invalidity; unknown-interval rule |
| backend synchronization failure (adapter reports incomplete) | quiescence unproven → conservative charge |
| disk-full, partial write, fsync failure, rename failure at every cut of §3 | fail-closed per the cut table; no partial artifact accepted |
| ledger/head/cache divergence (each pairwise) | ledger authority; record-first invalidity; no silent repair |
| artifact mutation, deletion, symlink, hardlink, path substitution on any runtime file | refusal via held-descriptor/`samestat`/`O_NOFOLLOW` checks |
| response read attempted before settlement durable | revocation + conservative charge |
| scientific field (loss/accuracy/competence/arm/margin…) injected into any record/event | recursive schema rejection |
| pre-WP-6 E2: candidate registration attempt; nonempty `candidate_ids`; draft manifest with queue field | refusal (the signed barrier); schema rejection |
| Q/C/test-only capability confusion: test symbol in production graph; Q-labelled capability request | graph verifier rejection; no issuer |
| E1/E3 simultaneous zero | exhaustion first, E3 preserved due |
| clean pause → simulated physical reboot → exact resume; resume after mutation; resume with E3 overdue | valid resume; refusal; `RESUME_REVIEW_PENDING` |
| every valid disposition and every invalid cause terminal | exact event/record pairing per Sol-C2 coupling; cross-kind probes refuse |

Green suites are evidence about the implementation only, never about
the programme.

## 11. Cursor implementation handoff (after contract signature)

| Item | Content | Owner |
|---|---|---|
| `src/philosophia/officina/generic_harness.py` | supervisor, lifecycle state machine (§2 tables as data), transaction helpers (§3 template), CPU meter adapter, watchdog, pause/resume, response gating, draft-manifest functions | **Cursor** (mechanical, from this contract) |
| `scripts/officina_t_process.py` | CLI: claim/start/heartbeat/close/pause/resume entry points, refusal-first | **Cursor** |
| `tests/test_officina_generic_harness.py` (+ fault-injection helpers) | the complete §10 matrix | **Cursor**, matrix rows verbatim |
| schema/state-machine review against this contract; integration; archival commits | | **Codex** |
| bounded X/Y review + confirmation | | **Opus / Sol** |
| contract signature; any future activation token | | **Kirill** |

Cursor receives **no authority** to choose scientific cells, alter
constants/schemas/events, weaken any refusal, create author tokens, or
activate T; any ambiguity Cursor finds routes back to Codex/Fable as a
contract question, never an inline decision.

## 12. Gate, governance simplification, and author choices

Per the accepted programme-audit recommendation, this engineering
contract uses the simplified cadence: **one bounded X/Y review → one
bounded confirmation after mandatory repairs → Kirill's signature**
(`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`). Multi-round reopening
occurs only for a concrete Critical contradiction. This simplification
does not apply to WP-6/WP-9 scientific contracts or one-shot drivers.

**Remaining author choices: none.** Every constant this contract uses
is already signed (E1/E2/E3, liability constants, stream cap, `min()`
rule, event vocabulary, schemas, T bands); the harness adds mechanism,
not policy. Future decisions that are *not* choices in this contract:
admitting an off-CPU meter adapter (its own bounded review),
breathing-check numerics (WP-6), and the activation token itself
(separate authorization after implementation review).

---

After signature, the only authorized next step is Cursor/Codex
implementation per §11 against this contract, followed by bounded
implementation review. Activation, worlds, learners, entropy,
candidates, spend, Q/C artifacts, and every scientific object remain
absent and unauthorized. T and Q are permanently non-citable for
C1–C6; the programme claim remains `OPEN`.
