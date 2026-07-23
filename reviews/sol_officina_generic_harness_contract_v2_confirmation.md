REVISE_OFFICINA_GENERIC_HARNESS_V2_YLINE

# Sol Y-line — Officina generic harness contract v2 confirmation

Scope: one bounded confirmation of the complete v2 replacement and Fable's
closure against my v1 mandatory repairs 1–14, the signed activation protocol
v1+v2+v2.1, the signed charter and WP-3 packet, and the WP-4 inactive boundary.
This is not a new scientific or harness-design cycle.

## Verdict

The replacement closes most of the v1 findings, including the central
three-case charge, single global unknown pool, exact reservation formula,
worker/backend isolation rule, removal of the draft ordering channels, honest
author-stop language, and WP-6/WP-9 ownership. It is not yet confirmable,
however. Five bounded defects remain, all within the permitted blocker classes:
accounting representation, terminal ordering, durable recovery/resume
admissibility, exact-schema compatibility, and non-outcome input closure.

## One-to-one audit of mandatory repairs 1–14

| Repair | Confirmation | Result |
|---:|---|---|
| 1 | §4c restores the signed timely / known-late / unknowable cases and deletes the flat-reservation charge. Known late time is expressly untruncated. | **Confirmed subject to repair A's zero-charge contradiction.** |
| 2 | §4d defines one `D0/K/R` batch and allocates one pool, once, in deterministic stream order. | **Formula confirmed; per-stream allocation is not mapped to the signed per-process lease/event schema (repair A).** |
| 3 | §4b states `ell=min(60s,floor(E1_available/k),floor(E3_available/k))`, aggregate `k*ell`, shortened deadlines, and sibling-only recomputation without an exhaustion/review event. | **Confirmed.** |
| 4 | §2a supplies the requested dominance and invalid-cause precedence. | **Not closed:** §2a says invalidity dominates valid exhaustion, while §2c.8, §4d, and closure Example B append `T_ENVELOPE_EXHAUSTED` for the same invalid batch; E1/E3 batches also lack exact live-process terminal records (repair B). |
| 5 | §§2c.3/5 and 4e pin the start hash, pre-settlement lease hash, sole increment, successor lease, final cumulative charge, and rest-state equations. | **Confirmed for serial leases; multi-stream event aggregation remains undefined (repair A).** |
| 6 | §2c.6–7 fixes valid close order; §2c.12/12a distinguishes live-process and no-process invalidity and adds an invalid process record; 12b revokes siblings. | **Partly confirmed:** the one-process paths close, but repeated sibling invalidities and E1/E3 batch dispositions have no single artifact/event order (repair B). |
| 7 | §6b durably serializes overdue resume with the ninth-event vocabulary; §6c requires a signed disposition and fresh process id. | **Not closed:** the recovery artifact has no schema/path/order/archive/cut contract, and clean resume still has no durable G3→G1 admission transition (repair C). |
| 8 | §6a carries the complete planned-pause preconditions, changed/missing boot split, counter preservation, and per-cut test duty. | **Substantively confirmed, but its resume and incomplete-archive routes inherit repair C.** |
| 9 | §5b replaces response wrapping with isolated memory/IPC/FD/temp/backend output, no worker capability, durable settlement before atomic promotion, and one-use tokens. Invalid/escaped work cannot promote or reuse output. | **Confirmed as a contract rule; implementation review must prove the listed escape tests.** |
| 10 | §4f separates CPU wall accounting from submission-to-proven-completion off-CPU accounting and sends every unmeasurable backend fact to the unknown pool. Static reviewed imports are required. | **Confirmed; no device winner is selected.** |
| 11 | §7 honestly permits T-informed author stop while making infrastructure decisions outcome-blind. | **Policy confirmed; the promised closed input schemas are not actually enumerated (repair E).** |
| 12 | §8 removes `created_utc` and the lineage tuple, retains signed runtime schemas unchanged, rejects whole T artifacts, bars release tokens, and limits future digests to opaque identity/equality. | **Confirmed.** |
| 13 | §8 makes the draft non-normative, gives hooks no authority, permits WP-6 replacement/core review, reserves WP-6/WP-9 cells, and preserves negative destinations. | **Confirmed.** |
| 14 | §§1, 3a, 9, and 10 pin sole ownership, the sole cache completion, exact roots/CLI, static adapters, fake exclusion, and expanded probes. | **Mostly confirmed; recovery cuts and terminal-batch probes cannot be single-valued until repairs B–C.** |

## Accounting checks

The exact reservation equation is conservative. For positive integer `k`,

```text
ell <= floor(E1_available/k)  =>  k*ell <= E1_available
ell <= floor(E3_available/k)  =>  k*ell <= E3_available
ell <= 60 s
```

so admission cannot over-reserve either boundary. I exhaustively checked small
integer grids for `k=1..4`; no inequality failure occurred.

The unknown-pool arithmetic also conserves the one global remainder. With
`R=max(0,cap-(D0+K))`:

- if `D0+K < cap`, `D0+K+R = cap`;
- if `D0+K >= cap`, `R=0` and the known crossing remains `D0+K`;
- `floor(R/m)` plus one nanosecond for the first `R mod m` streams sums exactly
  to `R`, so the remainder is neither multiplied nor truncated;
- known late charge `K` is never clipped by the reservation, E3, or E1.

Those equations force Fable's examples A–C at the aggregate level. They do not
yet force one signed ledger representation. A signed active lease and charge
event are process-scoped: one lease has one process id, one cursor, one
`device_units` count, and one cumulative charge; the event has a process id and
one pre-lease hash, but no `stream_index`. V2 allocates known/unknown time per
stream without saying whether multiple shares for one multi-stream controller
become one event or several, which cursor each uses, or how staggered off-CPU
stream intervals fit the single lease cursor. Two conforming implementations
can therefore produce different event sequences and cumulative charges.

There is also a literal conflict between §4c's “a lost stream is never charged
zero” and §4d/Example C's permitted zero additional share. If a freshly issued
stream has no prior charge and a sibling's known-late crossing makes `R=0`, its
total debit is zero despite a live outstanding liability. More concretely, the
pinned invalid-process constructor requires a positive final
`T_DEVICE_TIME_CHARGED` immediately followed by that process's
`T_RUNTIME_INVALID`; a zero-share process cannot be closed through it. Merely
preserving liability as a fact therefore does not provide a valid artifact
route.

## Terminal and compound-boundary check

The fault-free dominance ordering itself is deterministic. Its artifact routes
are incomplete:

- On fault-free E1 exhaustion, all live leases are settled, but the contract
  never assigns their signed `T_PROCESS_E1_EXHAUSTED` dispositions or the
  record-before-`T_PROCESS_STOPPED` order before the one global exhaustion
  event.
- On E3 due, all capabilities are revoked and leases quiesced, but their signed
  `T_PROCESS_E3_DUE` records, stopped events, and lease removal are not stated.
  A durable review cannot safely reactivate while these leases are unspecified.
- On a concurrent invalidity, 12b says to apply transition 12 to every sibling,
  but does not say whether there is one global invalidity event or one
  deterministically ordered G5→G5 event per process. The exact invalidity schema
  carries one cause and one outstanding-liability scalar, and the pinned
  constructor requires each process's invalid event to be the immediate ledger
  successor of its own final positive charge, so the choice changes hashes,
  records, and recovery inputs.
- On invalidity plus E1 exhaustion, the contract both says invalidity is the
  only ending and says to append `T_ENVELOPE_EXHAUSTED`. The latter enters
  terminal G7 and makes a valid resource ending the final global event, exactly
  the relabelling the dominance rule forbids. An exhausted numeric post-state is
  sufficient to retain the resource fact while unresolved invalidity remains
  G5.

Thus the table names a winner, but does not yet give exactly one terminal
machine route for every compound condition.

## Durability, isolation, and evidence checks

The overdue-resume construction uses no tenth event and makes
`resume_review_pending:true` durable. Ordinary clean resume is different: §6b
revalidates and then describes G3→G1 without naming a durable artifact or
existing event that effects that transition. Admission can therefore depend on
an in-memory successful check. The second-pause route also reuses a checkpoint
whose serialized state was created before `resume_review_pending:true`; the
contract must state the exact verification relation, archive set, and crash
cuts for that deliberate state difference.

Section 6c does not yet define a closed recovery artifact in operational terms.
It has no schema id/key set, canonical path, signature binding, allowed terminal
actions, atomic-create order, archival set, or crash table. Nor does it say how
the unresolved-invalidity predicate becomes durably resolved without a tenth
event. This fails the v1 requirement to enumerate exact artifacts, archival
sets, and cuts, and permits two recovery implementations to make different
admission decisions.

The isolation rule itself is adequate at contract level. Worker memory,
channels, descriptors, temporary paths, and backend buffers remain outside the
controller; the worker cannot independently contact T or start another
behavior-capable operation; quiescence and backend synchronization precede
durable charge; promotion follows charge; and invalid/escaped operations do not
promote. A crash after settlement cannot create *uncharged* information. The
implementation review must establish that promoted bytes remain readable only
through the bound one-use token at every promotion cut, as §5b and §10 require.

The pre-WP-6 information repair is closed. The draft manifest contains neither
time nor lineage ordering; Q/C rejects the complete T object; release tokens
cannot enter candidate/Q/`H_preC`/`selection_scope_id`/C schemas; and a future
digest is opaque equality/identity metadata only. The draft, token, namespace,
and digest confer no registration, priority, eligibility, or evidence.

The author-stop statement is now honest: human stop may be T-informed, whereas
E3, accounting, validity, recovery, pause, and resource classification must be
mechanically non-outcome. However, §7 merely says that “closed input schemas”
exist; it does not give their schema ids or exact keys. In particular, the
signed review record and author-stop event carry decision hashes whose source
objects could otherwise commit arbitrary free text. Recursive forbidden-word
checking is not a substitute for a closed key/value grammar.

## Mandatory bounded corrections

Only the following five repairs are required; no scientific cell is reopened.

### A. Make stream accounting representable in the signed process lease

For each settlement, first compute per-stream known charges and unknown shares,
then sum them by process id and append **at most one** positive
`T_DEVICE_TIME_CHARGED` event per affected process, using that process's exact
pre-settlement lease hash. The single successor lease cumulative charge
increases by that aggregate and its prior-charge hash becomes that event hash.
State whether all `k` streams under one lease share a coextensive cursor
interval; if they do not, the adapter must prove and the harness must sum their
individual intervals before the one event, otherwise the whole process selects
the unknowable case. No stream-index field may be added to a signed schema.

Remove the zero-share branch. Let `remaining=E1_cap-D0`, let `m` be the number
of unknowable live streams, and retain the already computed known total `K`.
When `m>0`, set the one unknown pool to
`U=max(m nanoseconds, remaining-K)` and allocate it with at least one nanosecond
per unknowable stream (equal quotient after the one-nanosecond floors, then
remainder by the existing deterministic order). Append unknown-process tuples
before a known process whose charge crosses the cap, so every invalid process
has a positive final charge and the known crossing is still retained in full.
The admission invariant guarantees room for those `m` nanoseconds before the
crossing because every live stream had positive reserved liability. The batch
may exceed the cap only by the known crossing plus this necessary conservative
floor; it never multiplies the remaining envelope. Delete Example C's
zero-share route and update the equations/tests accordingly. If this exact
code-compatible rule is not adopted, the alternative is a named, reviewed
metering-core amendment for a zero-charge invalid close; the present
no-amendment claim cannot coexist with the current zero-share text.

### B. Complete every boundary and invalidity artifact route

State these exact routes:

1. Fault-free E1: batch-settle all leases; for each live process in ascending
   sequence create a valid `T_PROCESS_E1_EXHAUSTED` record and then its
   `T_PROCESS_STOPPED`, remove the verified lease; after all closes append one
   `T_ENVELOPE_EXHAUSTED` and enter G7.
2. Fault-free E3: batch-settle all leases; create each valid
   `T_PROCESS_E3_DUE` record then `T_PROCESS_STOPPED`, remove every lease; enter
   G2 and permit only the durable review transaction.
3. Concurrent invalidity: calculate and freeze the whole conserving batch first,
   then emit deterministic per-process tuples
   `final positive charge → detail record → T_RUNTIME_INVALID → invalid process
   record → verified lease removal`; each invalid event is the immediate ledger
   successor of its own charge. Emit non-crossing unknown tuples first, the
   known crossing tuple last, explicitly permit later invalid events as G5→G5,
   and forbid `T_PROCESS_STOPPED`. Every collaterally closed healthy sibling
   inherits the batch's dominant triggering cause; use that one cause in its
   exact signed invalidity record and event.
4. Invalidity with exhausted/due counters: retain those numeric facts in every
   invalid post-state but append no valid exhaustion/stop/pause event while an
   invalidity is unresolved. G5 remains the sole route; a later signed
   disposition cannot convert an invalid process into a valid ending.

Add these sequences, including every compound pair, to §10. This is the
operational meaning of the existing dominance table, not a new policy choice.

### C. Close clean resume and recovery durability

For clean resume, specify that successful verification and the first new claim
occur under one lock epoch and that G3→G1 becomes durable only when the existing
`T_PROCESS_STARTED` event is appended directly on the verified pause/review
head; no capability or behavior occurs before it. A crash before that event
remains paused or routes to the already specified orphan-claim invalidity, never
to an in-memory active state.

For overdue resume, state the exact relation between the original checkpoint
state and the second pause event's pending post-state, its exact archival set,
and every §3 crash cut. The checkpoint remains immutable; only the event/state
cache may carry the pending flag.

For recovery, enumerate the recovery-disposition schema id and exact keys,
canonical path, signature and invalidity/head bindings, finite action tokens,
atomic-create/verification order, exact archival set, resolved-invalidity
predicate, and every crash cut. Define how a verified disposition changes
admission while leaving the invalid event and charges immutable and without
adding an event. No failed operation may be completed or retried; a recovered
process always starts with a fresh id.

### D. Preserve the signed invalidity schema

Delete §2a's statement that the invalidity detail record “lists every observed
cause.” The exact signed `philosophia.officina.t-runtime-invalidity.v1` record
has one `invalid_cause` field and no cause list. The deterministic precedence
may choose that one value; additional causes may be exercised by tests but may
not add a public/runtime field or enter recovery. Otherwise the claimed
no-amendment classification is false.

### E. Actually close the non-outcome input schemas

Enumerate the schema ids, exact key sets, and fixed enums/tokens for the E3
decision object, resource-stop decision, pause decision, recovery disposition,
and author-stop decision. Permit only the clock/charge/identity/integrity/
authorization facts already allowed by signed v2 §F; prohibit free text and any
hash chosen from learner/output bytes as a decision value. The signed runtime
record/event schemas remain unchanged and reference these closed decision
objects only by their already permitted hashes. Human author stop may remain
T-informed and non-citable exactly as §7 states; this repair closes the machine
input, not the author's cognition.

## Confirmed boundaries and authorization

The signed charter and WP-3/WP-4 hashes match their signature pins. V2 selects
no learner, architecture, optimizer, training rule, candidate, device winner,
breathing-check numeric, Q predicate, alpha, margin, endpoint, or scientific
outcome. WP-6 retains candidate equivalence, admissibility, stack family,
breathing check, competence, attempt, promotion, and Q entropy/numerics; WP-9
retains certificate and C science. Negative destinations remain non-scientific
and T/Q remain permanently non-citable.

The no-amendment classification is justified for the adopted three-case rule,
global-pool arithmetic, dominance mechanism, isolation protocol, draft schema,
and call-graph corrections. It is not yet justified for the cause-list sentence
or the unspecified recovery/decision artifacts; repairs C–E must show that they
use closed generic-harness mechanisms without altering a signed schema, event,
constant, or phase rule.

This revision verdict authorizes only the five bounded contract corrections and
one literal confirmation. It authorizes no contract signature, implementation,
manifest, authorization, activation, capability, world, learner, process,
lease, entropy, draft-manifest instance, E1/E2/E3 spend, candidate, Q/C object,
scientific lock, escrow, datum, outcome, or claim movement. T remains
`NOT_ACTIVATED`; the predecessor and programme claims remain `OPEN`.
