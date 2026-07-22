# Fable 5 — Officina generic harness contract v1 closure memo

Author: Fable 5. Companion to
`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V1_DRAFT.md`. Governing
state: the independent programme validation
(`READY_FOR_OFFICINA_GENERIC_HARNESS_CONTRACT`), the signed activation
protocol v1+v2+v2.1, the WP-3 signature, the WP-4 boundary, and the
inactive implementation with its **pending** residual confirmations
(`reviews/{opus,sol}_officina_t_inactive_repair_v2_confirmation_prompt.md`)
— which may run in parallel; accordingly **no implementation hash,
reviewed HEAD, or production source set is pinned anywhere in the
contract.** Exactly two files were created; nothing else changed;
nothing committed.

## Verdict

**READY_FOR_OFFICINA_GENERIC_HARNESS_XY_REVIEW**

## 1. Traceability table (mandate requirement → contract section)

| Mandate requirement | Contract |
|---|---|
| 1 Scope/authority: sole issuer/revoker; activation vs later gates; T non-citable; E2 impossible pre-WP-6; no T→Q/C evidence; enums confer no authority | §1 |
| 2 Lifecycle state machine: all 14 named transitions, exclusive/total, no fall-through/silent retry/liability erasure/invalid-as-valid | §2 (G0–G7, P0–P5, transitions 1–14) |
| 3 Durable ordering: numbered template, crash cuts + legal recovery, canonical JSON/no-replace/held-descriptor/hash-chain/record-before-event, no Git safety precondition | §3 |
| 4 Metering/liability: monotonic units, concurrent streams, tree ownership, four-stream cap, settle-before-release, conservative unknown-interval charge, E1/E3 priority, refusal-before-overspend, meter-adapter contract without device winner or breathing numerics | §4 |
| 5 Supervisor/watchdog: controller identity, group containment, child escape, PID reuse, boot identity, watchdog, revocation, quiescence, backend sync, dead-controller guarantees, threat model | §5 |
| 6 Power-off/pause/resume: full tested pause path; refusal conditions; pause ≠ invalidity ≠ author stop | §6 |
| 7 Learner-generic boundary: narrow adapter, infrastructure-visible facts only, non-citable labels, mechanical Q/C inadmissibility, response gating | §7 |
| 8 Draft manifest + WP-6 extension points: `q_ineligible`, order-free, no E2; reserved namespaces/slots; no WP-6 numerics | §8 |
| 9 Production call-graph duty: roots, closure, reachability, no reflection/entropy/test symbols/predecessor deps, reviewed bytes; manifest absent until authorized | §9 |
| 10 Verification/fault-injection matrix incl. all fifteen mandated probe classes | §10 |
| 11 Cursor handoff: modules, APIs, tests, task separation, no Cursor authority | §11 |
| 12 Gate simplification; author-choice enumeration | §12 |

## 2. Signed-protocol compatibility table

| Contract element | Signed source | Classification |
|---|---|---|
| Nine-event vocabulary; no tenth event | v2.1 §6 | inherited verbatim |
| Liability constants (60 s / 4 / 1 / 240 s); `min()` reservation; shortened deadline | v2 §D, v2.1 §4 | inherited verbatim |
| Behavior-capable stream = concurrency unit; group reconciliation | v2.1 §2 | inherited verbatim |
| Quiescence sequence; adapter ineligibility without testable sync | v2.1 §1 | inherited verbatim |
| Learner non-finiteness → voluntary stop, quarantined | v2.1 §3 | inherited verbatim |
| Record-first invalidity, dual-artifact authority | v2.1 §6 | inherited verbatim |
| Runtime lock discipline; archival sets/trailers; functional E1 boundary; immutable-control revalidation | v2 §§A–B | inherited verbatim |
| All schemas (claim/lease/record/review/invalidity, state, envelope) | v2 §§C–D | inherited verbatim |
| Draft manifests unregistered/`q_ineligible`; `H_preC` hashes as lineage only | v2 §G | inherited verbatim |
| Pause requires zero active leases; powered-off time advances E3 not E1 | v1 §8 | inherited verbatim |
| **New:** explicit global/process state machine; crash-cut table; release-token mechanism; meter-adapter interface; draft-manifest schema key list; call-graph root list incl. harness CLI; Cursor breakdown | this contract | **clarification / implementation contract — no amendment**: each adds mechanism inside signed semantics; none changes a constant, schema key set, event, boundary, or phase rule |

No proposed clause requires a protocol amendment. Two items X/Y should
check hardest against that claim: the draft-manifest **schema key
list** (v2 §G names the surface but not keys — I classify key
enumeration as clarification since it adds no eligibility or ordering
semantics) and the **release-token** wrapping (v2 §D requires
release-after-settlement; the token is the mechanism).

## 3. Unresolved choices

**None.** All numerics are signed; the harness adds mechanism, not
policy. Non-choices explicitly routed elsewhere: off-CPU adapter
admission (its own bounded review), breathing-check tolerance/procedure
(WP-6), activation token (separate authorization). No author token
accompanies this contract other than its eventual acceptance signature.

## 4. Bounded attack questions — Opus X-line (four)

1. **Totality:** take §2's transitions and §3's cut table and hunt for
   any reachable runtime condition with no assigned row — in
   particular compound faults (crash *during* quiescence settlement;
   reboot *between* ledger append and head replace; watchdog firing
   while the archival commit of a close is in flight). Does every such
   state resolve to exactly one of the nine events with liability
   preserved?
2. **Capability containment:** given §1 (no public constructor, no
   issuer outside the harness) plus §5's dead-controller guarantee and
   §7's release tokens, is there any sequence — including supervisor
   death after issuance but before first settlement — that leaves a
   usable capability or an uncharged behavior-capable interval?
3. **Call-graph closure:** does §9, combined with the v2 §A symbol
   ban, exclude every route by which test-only or predecessor behavior
   could reach production — including the harness CLI as a new root
   and adapters loaded for off-CPU backends?
4. **No-amendment claim:** do you accept §2 of this memo — every new
   element is clarification within signed semantics — or does any item
   (draft-manifest keys, release tokens, state-machine names) require
   a loud protocol amendment before signature?

## 5. Bounded attack questions — Sol Y-line (four)

1. **Liability accounting:** under §4's rules, construct any adaptive
   schedule of ≤4 streams with crashes, pauses, and reboots in which
   total charged E1 undercounts actual behavior-capable time, or in
   which the conservative rule can be strategically triggered to
   *overcount* into a de-facto early `T_ENVELOPE_EXHAUSTED` that
   erases the author's signed envelope meaning. Does the contract
   exclude both directions?
2. **Information boundary:** does §7 (infrastructure-visible fact
   classes; recovery blind to learner behavior; non-citable labels;
   mechanical Q/C refusal of quarantined artifacts) keep every T
   observation out of every future inferential path, including via the
   draft manifest's lineage hashes?
3. **E3 semantics:** do §2.9 and §6 preserve the signed review
   cadence under every pause/resume/exhaustion interleaving —
   specifically, can any path advance `last_review_utc` without a
   durable review, or perform work in `RESUME_REVIEW_PENDING`?
4. **Draft-manifest neutrality:** is the §8 schema provably order-free
   and eligibility-free — no field usable as a covert queue, priority,
   or pre-registration — and does WP-6's recompute-from-bytes rule
   make any draft-side gaming inert?

## 6. Negative authorization surface

This contract and this memo authorize only: bounded X/Y review of the
contract; after signature, the §11 implementation work and its bounded
implementation review. They do not authorize and did not create:
`generic_harness.py`, any CLI, `runtime_control/` or any production
manifest, any activation authorization or activation, any capability
issuance, any real world or learner, entropy, candidate registration
or draft manifest instance, E1/E2/E3 spend, runtime/Q/C data, any
scientific specification, lock, escrow, datum, outcome, or claim
movement. No implementation hash, reviewed HEAD, or production source
set was pinned (pending residual confirmations). No learner,
architecture, optimizer, training rule, certificate numeric, Q
predicate, alpha, margin, candidate, device winner, or scientific
endpoint was selected. T remains `NOT_ACTIVATED` at genesis; the
predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain permanently non-citable
for C1–C6; no prediction is made that any learner will qualify or that
Philosophia will be proved, falsified, or bounded; the programme claim
remains `OPEN`.
