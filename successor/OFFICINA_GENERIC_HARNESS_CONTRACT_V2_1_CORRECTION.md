# Officina generic metered harness contract — v2.1 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`. This
correction carries the complete v2 contract
(`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md`) forward
verbatim except for the exact replacements below, applying every Opus
M-1..M-6 and every Sol correction A..E under the code-compatible
**no-core-amendment route**: no zero-charge invalid-close constructor
is added; `runtime.py` and every signed schema, event, constant, root,
and phase rule are unchanged. The closed v1 findings (C-1..C-4,
R5..R12) and the confirmed Sol repairs are **not reopened**. The
inactive C4 verifier gate is independently closed at `fbac493`.

Creates nothing executable; amends no code; pins no manifest; selects
no learner, candidate, architecture, optimizer, device winner,
breathing threshold, Q predicate, alpha, endpoint, margin, or
scientific result. T remains `NOT_ACTIVATED`.

**Replacement index (everything else in v2 carries forward):**

| v2 locus | Action |
|---|---|
| §2a sentence "the invalidity detail record lists every observed cause" | **deleted** (D/M-5) |
| §2c.8 exhaustion sentence | **replaced** by §B.1/§B.4 below (M-2) |
| §2c.12b sibling paragraph | **replaced** by §B.3 (M-3/M-4) |
| §4c "lost stream is never charged zero" sentence | **replaced** by the §A floor ("every unknowable live stream receives ≥ 1 ns; a known-quiesced stream is charged its actual interval") |
| §4d entire section (incl. its zero-share branch) | **replaced** by §A |
| §6b clean-resume and second-pause paragraphs | **replaced** by §C.1/§C.2 (M-6) |
| §6c recovery paragraph | **replaced** by §C.3 |
| §7 "closed input schemas" sentence | **completed** by §E |
| §10 | **extended** by §F probes |
| closure Examples B and C | **superseded** by the §A worked batches (Example C's zero-share route is deleted; Example B's terminal is G5 with no exhaustion event) |

---

## A. Representable per-process settlement (Opus M-1/M-3; Sol A)

**Aggregation rule.** A settlement batch first computes, inside one
frozen snapshot, per-stream known charges (§4c cases a/b) and unknown
shares (below), then **aggregates by process id** and appends **at most
one positive `T_DEVICE_TIME_CHARGED` event per affected process**,
bound to that process's exact pre-settlement lease hash. The single
successor lease's cumulative charge increases by that aggregate and its
prior-charge hash becomes that event hash. **No `stream_index` or any
other field is added to a signed schema.**

**Cursor rule.** By default a lease's `k` streams are coextensive with
the lease's one cursor interval (known charge `k × elapsed`). For
non-coextensive streams (e.g. staggered off-CPU submissions), the
adapter must prove each stream's individual interval and the harness
sums them before the one event; any ambiguity selects the unknowable
case for the **whole process**.

**Unknown pool (zero-share branch removed).** Let
`remaining = E1_cap − D0`, `K` = the batch's known total, and `m` = the
number of unknowable live streams. When `m > 0`:

```text
U = max(m nanoseconds, remaining − K)
share_i = floor(U/m) + 1 ns for the first (U mod m) streams
          (deterministic order: ascending (process_sequence, stream_index),
           stream_index being a batch-computation index only, never a field)
```

Since `U ≥ m`, `floor(U/m) ≥ 1`: **every unknowable live stream
receives at least 1 ns.** Σ share_i = U exactly — the pool is debited
once, never multiplied, never truncated. Known late charges are never
clipped; the batch may exceed the cap only by the known crossing plus
this necessary conservative floor.

**Ordering.** All unknown-process tuples and non-crossing known tuples
are appended **before** the final known case-(b) tuple whose charge
crosses E1 (ascending process sequence within each class). Rationale:
once realized E1 reaches the cap no further charge can append
(`charge_device_nanoseconds` refuses), so every other process must
receive its positive charge first; the crossing charge is last and
retained in full. The admission invariant (every live stream was
admitted with positive reserved liability) guarantees room for the
`m`-nanosecond floors before the crossing; **if the required floor
cannot be represented, the batch fails closed before charging** — it
never hand-builds a record.

**Invalid tuples (indivisible, interleaved).** For every invalid
process the batch appends the indivisible tuple:

```text
positive final charge (T_DEVICE_TIME_CHARGED)
→ invalidity detail record (t-runtime-invalidity.v1)
→ T_RUNTIME_INVALID  (immediate ledger successor of its own charge:
                      sequence+1, previous = that charge's hash)
→ INVALID process record (t-process-record.v1)
→ verified lease removal
```

Tuples are deterministically ordered by process sequence
(crossing-process tuple last); later `T_RUNTIME_INVALID` events are
explicitly legal `G5→G5` transitions. No "all charges first" wording
survives anywhere; the interleaving is forced by the immutable
constructor's ancestry check.

**Worked batches** (cap 604,800 device-s):

1. **All-known.** `D0 = 100,000 s`. P1 timely +42 s (case a); P2
   late-known +95 s (case b). Two events, ascending sequence; post
   `D0 = 100,137 s`; both close valid per §2c.6. No pool.
2. **Known-late + unknowable siblings, exact cap.** `D0 = 604,700 s`
   (`remaining = 100 s`). P1 known-late 95 s; P2, P3 unknowable
   (`m = 2`): `U = max(2 ns, 100 − 95 = 5 s) = 5 s` → 2.5 s each.
   Order: P2 (2.5 s), P3 (2.5 s) tuples, then P1 (95 s) last. Post
   total = 604,800 s. **Invalid batch → no `T_ENVELOPE_EXHAUSTED`;
   terminal G5**; `device_nanoseconds = cap` retained as a numeric
   fact in every invalid post-state (§B.4).
3. **Multiple unknowables in one process.** One controller, `k = 2`
   unknowable streams, shares 2 ns each → **one** charge event of 4 ns
   for that process against its one lease; cumulative += 4 ns.
4. **Multiple processes.** P1 (k=1, known 30 s), P2 (k=2, both
   unknowable, shares 1+1 ns), P3 (k=1, unknowable, 1 ns), no
   crossing: three events — P1 30 s, P2 2 ns, P3 1 ns — ascending
   sequence; conservation `ΣU = 3 ns` exact.
5. **Invalid batch whose final known charge crosses E1.**
   `D0 = 604,760 s` (`remaining = 40 s`). P2, P3 unknowable; P1
   known-late 70 s (crossing). `K = 70`; `remaining − K < 0` →
   `U = max(2 ns, ·) = 2 ns` → 1 ns each. Order: P2 (1 ns), P3 (1 ns),
   then P1 (70 s) last. Post total = 604,830 s + 2 ns — the known
   overrun retained in full. Every invalid process has a positive
   final charge; the immutable constructor closes all three; **no
   exhaustion event; G5.**

## B. Total compound terminal routes (Opus M-2/M-4/M-5; Sol B/D)

**B.1 Fault-free E1 exhaustion.** Batch-settle all leases (§A). For
each live process in **ascending sequence**: valid process record with
disposition `T_PROCESS_E1_EXHAUSTED` (`final_charge_event` = its §A
charge) → its `T_PROCESS_STOPPED` (hashing that record) → verified
lease removal. After **all** valid closes: exactly one
`T_ENVELOPE_EXHAUSTED` → G7.

**B.2 Fault-free E3 due.** Batch-settle all leases. Per process,
ascending: valid `T_PROCESS_E3_DUE` record → `T_PROCESS_STOPPED` →
verified lease removal. Enter G2; only the durable review transaction
follows.

**B.3 Concurrent invalidity.** Freeze the whole conserving batch
first (§A snapshot), then emit the deterministic per-process invalid
tuples of §A — non-crossing/unknown tuples first, the known crossing
tuple last; later invalid events are legal `G5→G5`; **no
`T_PROCESS_STOPPED` is appended for any process in an invalid batch.**
**Every collaterally invalid-closed sibling inherits the one dominant
triggering cause selected by the §2a precedence; its exact signed
invalidity record and event carry exactly that single
`invalid_cause`.** Co-observed causes create no public or runtime
field and cannot enter recovery (the §2a "lists every observed cause"
sentence is deleted; the signed schema has one enum value).

**B.4 Invalidity with exhausted/due counters.** Every invalid
post-state retains the numeric facts (`device_nanoseconds` at or above
cap; E3 clocks) — but **no valid exhaustion, stop, or pause event is
appended while any invalidity is unresolved.** G5 is the sole terminal
route; a later signed disposition cannot convert an invalid process
into a valid ending. `T_ENVELOPE_EXHAUSTED` is appended **only when
every stream in the crossing settlement closes valid** (B.1).

**B.5 Compound-boundary table (one fixed route per pair):**

| Compound | Route |
|---|---|
| E1 + E3 simultaneous (fault-free) | B.1 once; E3-due retained in the post-state; neither resets the other |
| E1 (fault-free) + author stop pending | B.1 first (dominance); author stop is moot in G7 |
| E3 due + author stop | B.2 first; `T_AUTHOR_STOP` only after its bound completed review |
| E3 due + pause request | B.2 first; pause only from G1 |
| pause request + ordinary close | closes complete first (pause requires zero live leases) |
| invalidity + any of {E1, E3, author stop, pause, close} | B.3/B.4: invalid tuples only; numeric facts retained; no valid event until every invalidity is resolved (§C.3) |
| multiple simultaneous invalid causes (one process) | one tuple; public cause = §2a precedence `HASH > FILESYSTEM > CLOCK > PROCESS > RESOURCE` |
| invalidity in one process + healthy siblings | B.3: all siblings invalid-close with the inherited dominant cause |

## C. Durable clean/overdue resume and recovery (Opus M-6; Sol C)

**C.1 Clean resume (G3→G1).** Successful resume verification and the
first new process claim occur **under one lock epoch**. G3→G1 becomes
durable **only** through the existing `T_PROCESS_STARTED` event
appended directly on the verified pause (or review) head; no
capability or behavior-capable work exists before it. Crash cuts:
before the claim — still paused, re-verify on next entry; after the
claim, before the event — the orphan-claim route (record-first
invalidity, fresh id thereafter); after the event — normal P2 state.
An in-memory verification result alone never admits work.

**C.2 Overdue resume (G3→G4).** The original pause checkpoint remains
**immutable and is never reused as a binding**. The harness writes a
**new pending checkpoint artifact**, schema
`philosophia.officina.t-pending-resume-checkpoint.v1`, canonical path
`successor/officina/runtime/T_PENDING_RESUME_CHECKPOINT.json`
(atomic no-replace), keys exactly:

```text
schema, scientific_outcome (false), original_checkpoint_sha256,
payload_sha256 (byte-identical model/optimizer/config/stack hash map,
equal to the original's), ledger_head_before (= the first
T_OPERATIONAL_PAUSE entry hash), created_utc
```

It then appends the second `T_OPERATIONAL_PAUSE` **through the generic
§3 transaction (not the `record_operational_pause` helper)** with
reason `RESUME_E3_REVIEW_PENDING`, `resets_e3: false`, checkpoint
binding = the pending checkpoint's hash, and a full post-state with
`resume_review_pending: true`; head and cache follow §3. **Verifier
relation (pinned):** the second pause's checkpoint binding resolves to
the pending artifact, whose `ledger_head_before` equals the entry
immediately preceding the second pause (the first pause's entry hash);
the original checkpoint is validated only through
`original_checkpoint_sha256` byte-identity of payload hashes. Archive
set: pending checkpoint, second-pause ledger entry, head, state.
Crash cuts: before the pending artifact — still G3 (first pause
governs); after the artifact, before the event — orphan artifact →
record-first invalidity naming it; after the event — durable G4; a G4
power-loss re-verifies against the pending artifact and re-enters G4.
Only the durable `T_REVIEW_COMPLETED` clears the flag; only the
event/cache carry the pending state; the original checkpoint is never
mutated.

**C.3 Recovery disposition (closed artifact; no tenth event).**
Schema `philosophia.officina.t-recovery-disposition.v1`, canonical
path
`successor/officina/runtime/T_RECOVERY_DISPOSITIONS/<invalidity_event_sha256>.json`
(one per invalidity event, atomic no-replace, file+dir fsync,
post-verify), keys exactly:

```text
schema, scientific_outcome (false), author_decision_sha256,
invalidity_record_sha256, invalidity_event_sha256,
ledger_head_sha256, state_sha256,
affected_process_ids (sorted tuple), charge_event_sha256s (sorted
tuple), resolution_action, resolved_utc
```

`resolution_action` is exactly one of the finite tokens
`READMIT_AFTER_RECONCILIATION` | `REMAIN_BLOCKED`. Contents are
restricted to signed v2 §F fact classes; free text is absent by
schema; `author_decision_sha256` binds Kirill's tracked signed
decision. **Resolution predicate:** admission leaves G5 only when
every `T_RUNTIME_INVALID` event since the last admission has exactly
one verified disposition whose head/state bindings match the current
durable tree, whose action is `READMIT_AFTER_RECONCILIATION`, and
whose named discrepancies are durably reconciled. Events and charges
remain immutable; no failed operation is completed or retried; the
next process uses a fresh id; readmission needs **no event** — the
next `T_PROCESS_STARTED` is the first post-recovery entry. Archive
set: the disposition file(s) plus any reconciled head/state. Crash
cuts: before write — G5 unchanged; after write, before archival —
disposition durable, admission evaluates the predicate at next lock
entry; archival failure blocks capability per §3 without erasing
anything.

**C.4 Ledger-ahead-of-head cut (clarified).** At the §3 "after 4,
before 5" cut the invalidity **detail record may be written**, but the
`T_RUNTIME_INVALID` **event is necessarily deferred** (ledger append
re-verifies the head) until the signed recovery route reconciles the
head; both implementers fail closed identically. No silent repair
exists outside the signed sole cache/lease-successor case (§3a).

## D. Preserved invalidity schema (Sol D / Opus M-5)

The §2a sentence "the invalidity detail record lists every observed
cause" is **deleted**. The signed
`philosophia.officina.t-runtime-invalidity.v1` record carries exactly
one `invalid_cause`, selected by the fixed precedence; co-observed
causes may be exercised by tests but create no public/runtime field
and cannot enter recovery.

## E. Closed non-outcome decision schemas (Sol E)

All five decision objects are closed generic-harness artifacts
(canonical ASCII JSON; exact key sets; no free-text field exists; no
hash selected from learner/output bytes may appear as a decision
value; signed runtime schemas/events remain unchanged and reference
these objects only through their already-permitted hash fields):

| Schema id | Exact keys | Fixed enums |
|---|---|---|
| `philosophia.officina.e3-decision.v1` | schema, scientific_outcome (false), activation_record_sha256, state_sha256, observed_utc, last_review_utc, device_ns_at_review, device_ns_now, calendar_due, device_due | calendar_due/device_due ∈ {true,false} |
| `philosophia.officina.resource-stop-decision.v1` | schema, scientific_outcome (false), process_id, lease_sha256, state_sha256, observed_utc, monotonic_reading_ns, reason | reason ∈ {E1_BUDGET, E3_BUDGET, HOST_RESOURCE} |
| `philosophia.officina.pause-decision.v1` | schema, scientific_outcome (false), activation_record_sha256, state_sha256, ledger_head_sha256, observed_utc, live_lease_count (must equal 0), checkpoint_sha256 | — |
| `philosophia.officina.t-recovery-disposition.v1` | §C.3 | resolution_action ∈ {READMIT_AFTER_RECONCILIATION, REMAIN_BLOCKED} |
| `philosophia.officina.author-stop-decision.v1` | schema, scientific_outcome (false), review_record_sha256, ledger_head_sha256, state_sha256, signed_utc, author_decision_sha256 | — |

E3, resource-stop, pause, and recovery decisions are deterministic
functions of these closed inputs only. The human author stop may
remain T-informed and permanently non-citable exactly as §7 states —
this repair closes the **machine input**, not the author's cognition.

## F. Added §10 probes

Per-process aggregation (multi-stream single event; non-coextensive
cursor → whole-process unknowable); `U = max(m ns, remaining − K)`
allocation incl. `remaining − K < 0`; ordering with the crossing tuple
last (charge-append refusal past cap demonstrated); all five §A worked
batches forced bit-exactly; B.1/B.2 per-process record→stopped→removal
order and the single exhaustion event; B.3 interleaved tuples,
inherited collateral cause, `G5→G5` legality, no stopped event; B.4 no
valid event under unresolved invalidity with cap-level numeric facts
retained; every B.5 compound pair; C.1 crash cuts (in-memory
verification never admits); C.2 pending-checkpoint relation and G4
power-loss re-entry; C.3 disposition predicate (missing/mismatched/
`REMAIN_BLOCKED` dispositions keep G5; fresh-id requirement); C.4
deferred-event behavior; §E schema rejections (free text, unknown key,
learner-derived hash value).

## G. Compatibility and determinacy

| Element | Classification |
|---|---|
| signed events (nine), runtime schemas, constants, roots, phase rules, `runtime.py`/`accounting.py`/`checkpoint.py` constructors | **unchanged** — no metering-core amendment; no zero-charge constructor added |
| per-process aggregation, U-formula and ordering, tuple interleaving, B-routes, collateral-cause inheritance, C.1 lock-epoch rule | **deterministic clarifications** forced by the immutable constructors' own constraints |
| pending-resume checkpoint, recovery disposition, five decision schemas | **new closed generic-harness artifacts** — not runtime events, not signed-schema changes; referenced only via already-permitted hash fields |
| deleted cause-list sentence; corrected Examples B/C | repair of non-derivable v2 text back toward the signed schema — not an amendment |

**Two-implementer determinacy:** per-process charge-event counts and
values are forced by the aggregation rule and U-formula (integer
nanoseconds, deterministic order); tuple/event ordering and hashes by
the interleaving and ascending-sequence rules with the crossing last;
the terminal state for every compound boundary by B.1–B.5 (exactly one
route each); invalid cause and artifact key sets by D and the exact
schemas; pause/resume/recovery admission by C.1–C.3's durable
artifacts and predicate. If any required clause had needed a signed
schema or core change, this correction would have returned `BLOCKED`
and named it; none did.

---

After one literal bounded final confirmation by each line, the only
authorized next step is Kirill's contract signature
(`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`). No implementation,
manifest, authorization, activation, capability, world, learner,
process, entropy, spend, or T/Q/C datum is created or authorized by
this correction; WP-6/WP-9 ownership and every negative destination
remain unchanged; T and Q remain permanently non-citable for C1–C6;
the programme claim remains `OPEN`.
