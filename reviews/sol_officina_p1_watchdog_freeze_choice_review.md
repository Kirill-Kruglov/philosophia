REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_PACKET

# Independent Y-line validity review — P1 watchdog-freeze choice packet v1

## Findings

### Critical

**Y-C1 — The common PCS freeze scope is neither a constructible "leased" scope
nor total over the signed handle model.** W-A requires `table_seq` to be one
"the PCS has recorded as published" (packet lines 185–191), but watchdog lease
tables are peer-owned state. The signed layer boundary says the PCS executes
P1 only, never inspects peer state except the spawn-intent row, while watchdog
lease tables belong to the generic-harness peer layer
(`...P1_OPERATIVE_COMPOSITE_V1_2.md:1993-2007,2022-2027`). The update/ack pipes
join supervisor and watchdog; the PCS has no table-publication input. No
specified event can create the PCS record that W-A requires.

The shared `SCOPE` then selects every `SPAWNED` or `RUNNING`, `OWNED`
controller/worker handle, not every lease. It omits `STOPPED`, contains no
lease predicate, does not require the handle's `pgid_or_null` to be non-null or
kernel-verified, and does not deduplicate a group. The signed handle model
expressly permits a null pgid and allows `SIGNAL_GROUP` only after a
kernel-verified group exists (`...P1_OPERATIVE_COMPOSITE_V1_2.md:1257-1274`).
Both W-A and W-B inherit this defective scope.

The per-handle continuation is also incomplete: only an identity failure has a
named skip. `_killpg` denial/error/structural return, `/proc` unreadability,
member-enumeration failure, duplicate pgids, and an exception during the
quiescence pass have no single journal/result/invalidity continuation. Thus an
incomplete freeze can fall between "COMPLETED" and "inconclusive" without a
deterministic classification.

**Consequence:** neither option is mechanically executable as written, and the
claim that all failure routes are validity-first is not earned. The smallest
repair is to remove `leased` and peer-table language from the PCS action and
define the scope solely as the unique, ascending, kernel-verified pgids of
current-generation controller/worker handles that are unreaped and `OWNED`.
Every excluded handle and every identity/signal/enumeration/quiescence result
must have one closed result token; any unestablished or partial result must be
`ACCEPTED`/inconclusive whole-generation process invalidity, never completion,
resource success, or evidence. If exact lease scope is intended instead, a new
typed supervisor-to-PCS publication operation and its authority cost are
required; the current packet cannot claim no peer/interface change.

**Y-C2 — W-A is not the advertised one-request capability and creates an
authorized, repeatable resource/liveness channel.** The grammar permits
strictly increasing `request_seq` values up to six digits, and the journal key
contains that sequence (lines 159–170, 212–215, 258–266). Therefore request 1,
request 2, and so on are distinct fresh operations, not replay. "The watchdog
never retries" constrains only a conforming watchdog; it does not constrain the
capability held by the compromised-watchdog case used to price the boundary.
Nor does acceptance require update-pipe EOF. A compromised watchdog can request
repeated freezes while the supervisor is live.

The consequence is not merely denial of progress. Because no peer witness is
written, each affected generation is intended to take the `ABSENT` fallback,
which is record-first `PROCESS` invalidity with full §4c charging. The
capability therefore can force authorized process invalidity and resource
charge, even though it cannot select an arm or manufacture scientific evidence.
Packet §5.7's "one freeze ... per generation" and denial-only pricing are
false.

**Consequence:** W-A cannot be offered for informed selection in its current
form. The smallest repair is a constant one-shot journal key per
`(generation_id, watchdog_handle)` with no request sequence and no impossible
`table_seq`; exactly one valid request is accepted, every later record is a
replay/refusal with no syscall, and the packet must state explicitly that the
one authorized action can force fail-closed process invalidity and full charge.
If early invocation is not intended, the PCS must have a mechanically proved
precondition for peer-endpoint loss; watchdog prose alone is not such a gate.

**Y-C3 — The claimed orthogonality from the process-identity cell fails at the
load-bearing `ABSENT` fallback.** Both options say the absent-witness route
avoids numeric identity and therefore works with either identity outcome
(packet lines 238–256, 373–389, 456–470). But the signed fallback schema that
must be written at takeover requires `process_id`, numeric `pgid`, and
`start_identity` even for `rejection_conjunct = 0` / `ABSENT`
(`...V2_1_2_CORRECTION.md:830-869`). `ABSENT` makes only the rejected path and
object hash null. It does not make the identity fields absent.

Identity Option A could eventually leave those numbers in the claim. The
described identity Option B removes them and places them behind a P1 binding;
the peer fallback writer then has no authorized numeric `pgid` unless that
other cell grants a cross-layer read or changes this schema. The four-way
"compatible; no interaction" table is therefore unproved.

**Consequence:** the blocker itself is separate from the identity claim cell,
but the proposed settlement representation is not. To preserve orthogonality,
the smallest exact repair is a bounded peer-schema amendment for the `ABSENT`
branch: `pgid` and `start_identity` are null only when
`rejection_conjunct == 0`, current quiescence is `UNKNOWN`, no instant or
overrun is synthesized, and the same dominant `PROCESS` invalidity/full-charge
route applies. The packet must then admit that this peer schema/predicate is
reopened. Otherwise this choice must be explicitly conditioned on a completed
identity selection and cannot claim orthogonality.

### Major

**Y-M1 — W-B's `PEER_EOF` proves endpoint loss, not supervisor death, and the
two EOFs are not one indivisible kernel event.** Packet E-1 equates a
zero-length `SOCK_SEQPACKET` receive with the supervisor having exited, and
§§4.2–4.3 say the PCS thereby proves the supervisor is gone. A live supervisor
can close or half-close its protocol endpoint; the update-pipe write end can
remain open. Conversely it can close the update pipe while retaining the
protocol socket. A malformed/empty message must also be classified explicitly
rather than silently promoted to a death proof. The signed A3/P1 threat model
does not permit an untrusted peer report to become a false object-bound death
fact.

This does not defeat the safer W-B architecture. Loss of the sole peer control
endpoint is itself a sufficient fail-closed trigger: after it, no authorized
peer request can arrive and the generation has no valid continuation. What is
invalid is calling it proof of process death or the "same kernel event" as the
watchdog EOF.

**Consequence:** replace `SUPERVISOR_LOST` with `PEER_CONTROL_ENDPOINT_LOST`;
state that orderly close, half-close, or an indistinguishable forbidden empty
record proves only endpoint unavailability; freeze once and route process
invalidity without inferring death. Update the death/race table and publication
wording accordingly. This keeps the trigger pre-outcome and mechanically
bounded.

**Y-M2 — W-B journals only after its side effect, so ordinary mid-freeze
failure is not record-first.** E-3 performs all signals and observations; E-4
then appends the sole journal entry. The race table discusses PCS death
mid-E-3, but not a live PCS receiving a denied/structural signal result or an
enumeration exception after some groups were stopped. No durable `ACCEPTED`
marker then proves that an autonomous operation began.

**Consequence:** use the already-selected B1 ordering: validate endpoint loss,
append/fsync the constant `(generation_id,"PEEREOF",1)` `ACCEPTED` entry,
perform the closed per-group classifier, then append/fsync `COMPLETED`. Any
restart or live failure that sees `ACCEPTED` is inconclusive process invalidity
and performs no second freeze. This also makes stale generation, replay, crash,
and partial-freeze behavior single-valued.

**Y-M3 — W-A lacks an ordering contract with the existing PCS `PEER_EOF`
terminal.** The watchdog can request only after update-pipe EOF. At the same
time the PCS observes protocol peer loss and, under signed P1, enters a
non-returning state, accepts no further supervisor request, and frees the
singleton for no one. The packet gives the new watchdog socket a dispatch path
but never states whether that path remains serviced after `PEER_EOF`, for how
long, or whether the non-returning transition can win first.

**Consequence:** if W-A remains offered, its repaired one-shot socket must have
an explicit priority/cut rule relative to protocol EOF and the non-returning
reaper transition. Watchdog death, socket EOF, or the existing bound must end
the wait in deterministic invalidity; no freeze may be inferred. This extra
liveness/ordering surface is another governance cost favoring W-B.

### Minor

**Y-m1 — The publication caveat is directionally correct but uses the packet's
overclaimed death semantics.** `L6` correctly says neither freeze occurrence
nor evidence availability after supervisor death is guaranteed. It should also
say that peer-endpoint loss is not proof of supervisor death, that PCS journal
facts are not peer freeze evidence, and that an `ABSENT` witness means evidence
is unavailable even if some or all groups were in fact stopped.

**Consequence:** make those three sentences part of the mandatory publication
wording. No qualification, comparison, Q/C, or Proof may distinguish
"journal says freeze completed" from any other `ABSENT` case.

## Required determinations

1. **Reality and separation of the blocker.** The blocker is real. `S-12`
   forbids `killpg` on `generic_harness.py` paths; P1 makes the PCS the sole
   caller of process primitives; the watchdog has no PCS endpoint or numeric
   authority; and no supervisor relay exists after update EOF. The process-
   claim identity decision does not decide who can execute the freeze. Y-C3 is
   a defect in the proposed fallback representation, not a merger of the two
   author choices.

2. **W-A authority.** A genuinely constant, one-shot, target-free watchdog
   capability could preserve numeric/process execution authority in the PCS.
   The current sequence-keyed channel does not: it authorizes repeatable early
   freezes and resulting full-charge invalidity. It creates no valid
   scientific selection channel because invalidity remains dominant, but it
   does create an underpriced capability, liveness, and resource-accounting
   channel.

3. **W-B initiative and C1.** After Y-C1/Y-M1/Y-M2 are repaired, PCS action on
   loss of the sole peer endpoint is narrow, pre-outcome, once-per-generation,
   and mechanically bounded. It is compatible with P1's sole-caller authority:
   the PCS, and no peer or watchdog, executes process control. It changes who
   initiates the action, but it does not let P1 decide a peer settlement; the
   peer later applies the mandatory `ABSENT` invalidity route. The explicit
   `P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1` author token is a real C1 role
   replacement, not a clarification. With corrected `L6` wording and the
   bounded fallback amendment, no additional scientific-claim selection is
   required.

4. **Scientific meaning of freeze and `ABSENT`.** Neither successful signalling
   nor a PCS journal timestamp is scientific evidence. `ABSENT` means the
   required peer witness is unavailable; it never means freeze success. It
   deterministically yields record-first `PROCESS` invalidity, the unknowable
   pool, full charging, no synthesized instant, no `overrun_ns`, no valid
   terminal, and no input to qualification, comparison, Q, C, or Proof.

5. **Recommendation basis.** The packet uses authority fidelity, descriptor/
   opcode surface, testability, and liveness dependencies only. It predicts no
   learner, arm, qualification, Q/C, or scientific outcome. Its statement that
   the consequence is not a resource interpretation is too broad—full charging
   is a deterministic resource-accounting consequence—but no result-dependent
   criterion is present.

6. **Failure matrix.** PCS death, simultaneous PCS/supervisor death, and an
   incomplete freeze remain whole-generation invalidity with no adoption.
   Watchdog death blocks W-A but does not affect W-B. W-A's descriptor leak
   proof is structurally plausible, but its ordering and one-shot bounds are
   incomplete. Half-close/endpoint close must be endpoint loss, not death.
   Restart may not adopt or repeat an `ACCEPTED` action. Replays perform no
   syscall; stale generations perform no action. Missing or malformed witnesses
   always take the dominant `ABSENT`/unverifiable invalid route. The repairs in
   Y-C1 and Y-M2 are required to make every signal/enumeration/partial branch
   deterministic.

7. **Sole-caller/A3 compatibility.** W-B does not change who is allowed to call
   `killpg`: only the PCS does. A3 already admits that a same-UID actor can deny
   liveness; it does not authorize converting such interference into science.
   Treating endpoint loss as a fail-closed process fact preserves that line.
   Calling endpoint loss proof of supervisor death would not.

8. **Publication.** Corrected `L6` is strong enough only if it covers both
   process death and peer-endpoint loss and states that actual freeze occurrence
   and peer evidence are independently unavailable. No later publication may
   imply that the PCS journal supplies the missing witness.

## Smallest repair and recommendation

Revise only these bounded surfaces:

1. Replace the shared scope with unique kernel-verified P1 groups and a total
   per-group failure classifier; remove unsupported lease/table claims.
2. Make W-A a constant one-shot request, price its full-charge invalidity
   effect, and order its service relative to `PEER_EOF`; otherwise mark W-A
   non-selectable.
3. Recast W-B's trigger as peer-control-endpoint loss, add a durable
   pre-action `ACCEPTED` entry, and never infer supervisor death from it.
4. Amend the `ABSENT` fallback so it is constructible without numeric identity,
   and disclose that this narrowly reopens the peer schema.
5. Strengthen `L6` as specified in Y-m1.

**After those repairs, W-B remains the Y-line validity/governance
recommendation.** It keeps process-control execution in the sole PCS, adds no
watchdog capability or descriptor, removes the W-A ordering/liveness channel,
and uses a fail-closed pre-outcome endpoint-loss trigger. This recommendation
predicts no scientific or programme outcome.

## Byte custody and authorization boundary

Recomputed SHA-256 values:

```text
15937b84b2e2a61de3d908ea014cbded902ca5ba15f58b988920c99be0702f09  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
d8d3ced2aee226673903223250d810a5e574362132aafa644515c150c05f0cdb  reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md
```

This verdict authorizes no A/B selection, implementation, activation, process,
signal, resource spend, datum, outcome, Proof, or claim movement. The identity
choice remains a separate author decision. `T = NOT_ACTIVATED`; the programme
claim remains `OPEN`.
