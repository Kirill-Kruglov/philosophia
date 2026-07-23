REVISE_OFFICINA_GENERIC_HARNESS_V2_XLINE

# Opus 4.8 X-line — Officina generic metered harness contract v2 confirmation

Reviewer: Opus 4.8 (X-line, adversarial engineering-contract implementability).
Repository: `/home/master/llm_projects/philosophia`. Bounded mandate: the single
governance-permitted confirmation of the complete replacement
`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md` +
`reviews/fable_officina_generic_harness_contract_v2_closure.md` against my v1
review (`reviews/opus_officina_generic_harness_contract_v1_review.md`), the
signed protocol (v1+v2+v2.1), the WP-3 signature, the WP-4 inactive boundary, and
the pinned immutable verifier at HEAD.

**I edited no existing file, created exactly one file (this confirmation),
committed nothing, ran only read-only reads/greps, implemented nothing, created
no `generic_harness.py`, CLI, manifest, authorization, or runtime artifact,
activated no T, and spent no E1/E2/E3.** The real tree remains pristine and
`NOT_ACTIVATED`. No scientific outcome is asserted or predicted.

## Verdict

**REVISE.** The v2 draft is a large, faithful improvement: **every one of my v1
findings C-1..C-4 and R5..R12 is correctly and durably closed** (Part 1), and the
roots/CLI/import/ownership contract now matches the pinned verifier byte-for-byte
in intent (Part 3). But the *new* Y-line machinery — the §4d global conserving
settlement batch, the §2a dominance rule, and the §2c.12b sibling force-close —
contains a small, finite cluster of **concrete contradictions with the immutable,
tested constructor `runtime.py:build_process_record`** and one internal
terminal-state contradiction, all in the exact compounds this confirmation was
told to verify ("known overrun, zero-share after crossing, simultaneous E1/E3,
infrastructure-invalidity dominance"). Two of them (M-1, M-2) are Critical and
make two implementers diverge on **terminal classification and the ledger event
set**; one (M-1) may not be fixable by wording alone and may require a reviewed
metering-core amendment — which, if so, falsifies the §12 "no core change / no
amendment" claim.

Per the governance rule (reopen only for a concrete Critical contradiction),
these qualify. The repairs are finite and localized to §2a / §2c.8 / §2c.12b /
§4d and Examples B–C; they do **not** reopen the resolved C-1..C-4 / R5..R12
material. This is not a redesign round.

---

## Part 1 — One-to-one disposition of C-1..C-4 and R5..R12 (all CONFIRMED closed)

| Finding | v2 location | Confirmed against code / protocol |
|---|---|---|
| **C-1** record-before-event, valid close | §2c.6–7 | Order is charge → durable final record → `T_PROCESS_STOPPED` hashing that record. Matches `runtime.py` (`_EVENT_DATA_KEYS["T_PROCESS_STOPPED"]` carries `process_record_sha256`; the valid record's `final_charge_event_sha256` is the charge event, not the stopped event). **Closed.** |
| **C-2** INVALID record + no-process split | §2c.12 / 12a | 12 builds the INVALID `t-process-record.v1` bound to the `T_RUNTIME_INVALID` event; 12a creates no process record for a global no-process fault. Matches `build_process_record` INVALID path and `activation.py:_record_activation_invalidity`. **Closed** (base case; the *sibling/batch* extension is where the new defects live — Part 2). |
| **C-3** three-case recovery charge | §4c | Reservation is "ceiling and watchdog deadline, never itself the recovery charge"; (a) actual ≤ reservation, (b) actual through known reading crossing E1 in full, (c) unknowable → §4d pool; floor = never zero. Verbatim v2.1 §1. **Closed.** |
| **C-4** roots/CLI vs pinned verifier | §9, §11 | Roots = exact `verification.py:PRODUCTION_ROOTS` tuple; `generic_harness.__main__` CLI via `python -m`; no `scripts/officina_t_process.py`. **Closed.** |
| **R5** cache-cut self-contradiction | §3, §3a | §3a is the sole silent completion (cache/lease successor one state-bearing event behind a consistent ledger+head, same lock epoch); every other mismatch is record-first invalidity; verifier authoritative only at rest. Matches `activation.py:verify_active_repository` cache-equality failure. **Closed.** |
| **R6** G5 siblings | §2c.12b | Siblings are revoked/settled/invalid-closed; no admission during the batch. **Adopted** — but under-specified (M-3/M-4) and collides with the code (M-1); see Part 2. |
| **R7** initial charge-hash seed | §2c.3, §2c.5 | Seed = `T_PROCESS_STARTED` entry hash; per-settlement successor = event hash; no cyclic hash. Matches `build_active_lease` (any SHA-256 seed accepted). **Closed.** |
| **R8** exhaustion vs reservation refusal | §2c.8, §4b | Event only at realized ≥ 168 h; sibling `ℓ=0` refuses + recomputes, appends nothing. Matches `validate_ledger_event` (`device_nanoseconds ≥ 168h`) and v2.1 §4. **Closed** at the reservation boundary (the *invalidity-crossing* interaction is M-2). |
| **R9** draft-manifest ordering | §8 | `created_utc` and the lineage tuple **removed**; no sequence/queue/priority field. Stricter branch. **Closed.** |
| **R10** static adapters | §4f | Statically imported reviewed modules; reflective discovery forbidden. Matches `verify_source_quarantine` dynamic-import ban. **Closed.** |
| **R11** import allowlist | §9 | CPU-only list (`subprocess start_new_session`, `os.killpg` int signals, `time.clock_gettime_ns`, `fcntl`, `os`) — all within `ALLOWED_ABSOLUTE_IMPORTS`; cross-module `generic_harness` import and backend imports named as future reviewed amendments. **Closed.** |
| **R12** ownership/types | §1 | Production `RealTCapability` defined/issued only in `generic_harness.py`; `runtime.py` decoys unmodified; supervisor sole lock holder and sole writer of claims/leases/records; fake types test-only. **Closed.** |

All twelve v1 dispositions are honored, in rule/schema/ordering form (not prose).
This part of the contract is X-line acceptable.

---

## Part 2 — Global settlement, dominance, and sibling closure (NOT total/single-valued)

The new §4d batch, §2a dominance, and §2c.12b sibling force-close must interoperate
with the **immutable, tested** constructor `runtime.py:build_process_record`, which
enforces (verified by `tests/test_officina_runtime.py:551-603`):

```607:639:src/philosophia/officina/runtime.py
    event = validate_ledger_event(dict(final_charge_event))
    if event["event"] != "T_DEVICE_TIME_CHARGED":
        raise ValueError("process settlement requires a device-time charge event")
    ...
        if terminal["previous_sha256"] != final_charge_event_sha256 or (
            terminal["sequence"] != event["sequence"] + 1
        ):
            raise ValueError("invalid process event ancestry differs")
```

with `T_DEVICE_TIME_CHARGED` requiring `charge_ns > 0`
(`runtime.py:882-884`) and `charge_device_nanoseconds` **refusing once E1 is at
cap** (`accounting.py:124-125`). Consequences:

### M-1 (Critical) — a zero-share / R=0 unknowable live stream cannot be invalid-closed by the pinned constructor

§4d states: "a zero-share stream's invalidity record preserves its liability facts
**without a zero charge event**," and closure **Example C** asserts that after a
prior case-(b) overrun crosses the cap (`R = 0`), "a later unknowable stream …
zero additional debit … its ending remains invalid with liability facts preserved
in its records."

But `build_process_record` for a `T_PROCESS_INVALID` close **requires** a positive
`T_DEVICE_TIME_CHARGED` (`charge_ns ≥ 1`) as `final_charge_event`, immediately
followed (`sequence+1`, `previous_sha256 = charge hash`) by the
`T_RUNTIME_INVALID`. A zero-share stream has no such charge event, and once E1 is
at cap **no charge can be appended** (`charge_device_nanoseconds` refuses). So the
intended immutable path cannot close it. The only ways out are all defective as
drafted: (i) grant it ≥1 ns — impossible when `R = 0`; (ii) hand-roll the record
past `validate_process_record` (which does not re-check ancestry) — an
**unspecified divergence** with weaker linkage that the contract neither names nor
forbids; (iii) amend `runtime.py` (a metering-core / immutable-control change),
which contradicts §12. This is the exact "zero-share after crossing" case the
mandate named, and Example C is presently **unimplementable via the intended
constructor**. Two implementers diverge (one stalls, one hand-rolls a
differently-linked record).

**Repair R-M1:** pin the close path for a conservatively-settled live stream when
no positive charge is available. The only code-compatible resolution I can see is
to forbid the state from arising: order §4d so that within one batch the
cap-crossing charge is the **last** charge and every other live stream receives a
strictly positive share **before** the cap is reached (i.e., the pool guarantees
≥1 ns per unknowable stream, which requires `R ≥ m` at the batch's charging
phase); and specify that a case-(b) overrun which crosses the cap while siblings
are live is settled in the **same** batch with the siblings charged first. If the
programme instead wants Example C's `R=0` residual stream to close invalid, that
requires a reviewed `runtime.py` amendment (a new zero-charge invalid-close
constructor) — which must be named as an amendment, not asserted as "no core
change." Pick one explicitly; both change §4d and Example C.

### M-2 (Critical) — exhaustion vs. invalidity dominance is not single-valued

§2a: "**Infrastructure invalidity dominates every valid ending**; … exhausted/due
resource facts are **retained in the post-state**, but the ending is **never
reinterpreted as valid exhaustion** … an invalidity that conservatively consumes
the last E1 **remains an invalid ending**." This says: when the crossing coincides
with invalidity, record the cap only as `device_nanoseconds = cap` inside the
invalidity post-state; terminal = **G5**; append **no** `T_ENVELOPE_EXHAUSTED`.

But §2c.8 and §4d say `T_ENVELOPE_EXHAUSTED` "is appended … when realized …
`≥ 168 h` (a crossing or **conservative settlement**)," and closure **Example B**
explicitly "**appends `T_ENVELOPE_EXHAUSTED` once**" while B and C close invalid.
These contradict §2a: appending the event enters G7 ("terminal (never)"), a valid
exhaustion ending; a following `T_RUNTIME_INVALID` then supersedes a "terminal"
state, and the global terminal (G5 vs G7 = last state-bearing event) is
under-determined. Two implementers produce different ledgers and different
terminal global states in the invalidity+crossing compound.

**Repair R-M2:** make §2c.8/§4d/Example B consistent with §2a: append
`T_ENVELOPE_EXHAUSTED` **only when every stream in the crossing settlement closes
valid**; when any stream in that settlement is invalid/unknowable, record the cap
solely as the `device_nanoseconds = cap` fact in the invalidity post-state(s),
terminal = G5, and append no exhaustion event. Correct Example B (its terminal is
G5, not "exhaustion once").

### M-3 (Major) — §4d batch order is incompatible with the pinned charge→invalid adjacency

§4d reads as "append all positive-charge events, then take terminal/gate decisions
after every lease is settled." That is unimplementable through
`build_process_record`, which forces each invalid stream's `T_RUNTIME_INVALID` to
be the **immediate** successor of **its own** final charge (`sequence+1`,
`previous = charge hash`; test `test_officina_runtime.py:578-603`). Appending
`charge_B, charge_C, invalid_B, …` fails the ancestry check for `invalid_B`.

**Repair R-M3:** state that the batch appends, per affected stream sorted by
`(process_sequence, stream_index)`, the tuple [final charge → its invalidity
detail record → its `T_RUNTIME_INVALID` → its INVALID process record], strictly
interleaved; the global terminal is the state after the last such event (subject to
M-2). This is the only order the immutable constructor accepts.

### M-4 (Major) — collateral healthy-sibling `invalid_cause` is unspecified

§2c.12b force-closes **healthy, provably-quiesced** siblings as `T_PROCESS_INVALID`
(they cannot close valid under G5). But `InvalidCause ∈ {PROCESS, RESOURCE, HASH,
CLOCK, FILESYSTEM}` has no value for "collaterally closed by a sibling's global
fail-closed," and the contract does not say which cause the sibling's
`t-runtime-invalidity.v1` record and `T_RUNTIME_INVALID` event carry. Its record
`invalid_cause` differs between implementers (PROCESS vs the triggering cause).

**Repair R-M4:** pin it — e.g., a collaterally-closed sibling inherits the
**dominant triggering cause per the §2a precedence** (so all records in one G5
batch carry the same cause), or a fixed `PROCESS`. Choose one; it is an
output-determining artifact field.

### M-5 (Minor) — "the invalidity detail record lists every observed cause" is not representable

§2a's parenthetical is not derivable from the signed `t-runtime-invalidity.v1`
schema, whose keys are fixed and whose `invalid_cause` is a **single** enum value
(`runtime.py:validate_invalidity_record`, `set(value) != expected` refuses extra
keys). Adding a causes list fails the immutable validator.

**Repair R-M5:** state the detail record carries exactly the one
precedence-selected `invalid_cause`; co-observed causes are not separately listed
(no schema field exists). (The precedence tiebreak itself is a fine deterministic
clarification.)

---

## Part 3 — Roots / CLI / import / ownership (CONFIRMED against the pinned boundary)

`verification.py:PRODUCTION_ROOTS` = exactly
`scripts/officina_activate_t.py`, `scripts/verify_officina_active.py`,
`src/philosophia/officina/generic_harness.py`, and the manifest check requires
`manifest["roots"] == list(PRODUCTION_ROOTS)`:

```56:60:src/philosophia/officina/verification.py
PRODUCTION_ROOTS = (
    "scripts/officina_activate_t.py",
    "scripts/verify_officina_active.py",
    "src/philosophia/officina/generic_harness.py",
)
```

§9/§11 match this exactly: three roots, `generic_harness.__main__` CLI via
`python -m`, **no** `scripts/officina_t_process.py` (confirmed absent), static
adapters, CPU-only import list within `ALLOWED_ABSOLUTE_IMPORTS`, and every future
expansion (cross-module `generic_harness` import, backend imports, new entry
points) named as a reviewed amendment. §1 pins sole issuance in
`generic_harness.py`, the `runtime.py` decoys unmodified, the supervisor as sole
lock holder and sole durable writer, and fake types excluded. **This part is
X-line acceptable** (C-4, R10, R11, R12 fully honored).

---

## Part 4 — Isolation/promotion, pause/resume, recovery, crash cuts

- **Isolation-and-promotion (§5b):** the worker-isolation + revoke → quiesce →
  sync → hash → charge → atomic-promote → one-use token sequence exposes no result
  on any invalid/escaped path; the token is ephemeral (no durable schema; barred
  from candidate/Q/`H_preC`/C by §8). No result leakage, no silent retry. **OK.**
- **Recovery (§6c):** closed disposition artifact, v2 §F facts only, fresh ids, no
  automatic retry; G5 exit only when every invalidity has one verified disposition.
  **OK** (subject to M-1/M-2 determining what artifacts exist to dispose of).
- **§3a sole silent completion / crash cuts:** correct and bounded. **One wording
  note (non-blocking):** the "after 4, before 5" row labels a ledger-ahead-of-head
  state "record-first invalidity," but `ledger.append` re-verifies the head before
  every append (`ledger.py:207-208`), so the `T_RUNTIME_INVALID` **event** cannot
  be appended until the head is repaired under §6c — the detail record can be
  written but the invalidity event is necessarily deferred to signed recovery.
  Both implementers fail-closed identically, so no output divergence; clarify the
  wording ("detail record writable; event deferred to §6c").
- **M-6 (Major) — overdue-resume second `T_OPERATIONAL_PAUSE` (§6b) collides with
  the immutable pause helpers.** §6b appends a second `T_OPERATIONAL_PAUSE` "bound
  to the **same** verified checkpoint" with a `resume_review_pending: true`
  post-state. But `checkpoint.py:verify_resume` requires the checkpoint's
  `ledger_head_before` to equal the immediately-prior entry hash
  (`checkpoint.py:211-213`), and `record_operational_pause`/`write_pause_checkpoint`
  refuse a `resume_review_pending` pre-state (`checkpoint.py:71-76`). A **reused**
  checkpoint's `ledger_head_before` is stale after the first pause, so a power-loss
  in G4 would fail `verify_resume`; and the second pause cannot be produced by the
  signed `record_operational_pause` helper. **Repair R-M6:** specify that the
  second pause is appended by the harness's own §3 transaction (not
  `record_operational_pause`) and binds a **freshly written** checkpoint whose
  `ledger_head_before` = the first pause's entry hash, so a G4 power-loss remains
  resumable; or pin an explicit alternate verification path.

Everything else in Part 4 (no tenth event, no Git safety precondition, no
uncharged interval outside M-1) holds.

---

## Part 5 — Compatibility-table honesty

Mostly honest, with two exceptions tied to Part 2:

- Inherited signed rules (constants, events, schemas, three-case charge,
  lock/archival discipline, E2 barrier, T bands) and the genuine deterministic
  clarifications (state machine, cut table, reservation arithmetic, hash seeding,
  isolation protocol, pause conditions, second-pause resume, recovery artifact,
  cause **precedence tiebreak**, draft-manifest key set) are classified correctly.
  The C-3/C-4 repairs are correctly "repair toward signed text," not amendments.
- **Not yet honest:** (a) **M-1** may require a reviewed `runtime.py`
  (metering-core) amendment to make Example C implementable — if so, the §12/memo-§7
  "no core change / no amendment" claim is false and must be stated as a named
  amendment; (b) **M-5** ("lists every observed cause") is a clause **not
  derivable** from the signed invalidity schema. Neither is a *stylistic*
  reopening; both are concrete non-derivabilities. The precedence ordering and
  dominance order are acceptable as deterministic tiebreaks and I do **not** call
  them amendments.

---

## Part 6 — Can two independent implementers derive identical outputs?

**No — not yet**, and only in the compounds above. They would diverge on:

1. **Terminal classification** — G5 vs G7 when a conservative/overrun crossing
   coincides with invalidity (M-2).
2. **Ledger event set/ordering** — whether `T_ENVELOPE_EXHAUSTED` is emitted
   (M-2); whether batch events are interleaved per stream (M-3).
3. **Charges/artifacts** — whether a zero-share/`R=0` live stream can close at all
   and via which construction path (M-1); the `invalid_cause` of a collaterally
   closed sibling (M-4); the detail record's cause representation (M-5).
4. **Admission after a G4 power-loss** — resumable or not, depending on the
   checkpoint binding (M-6).

Outside these, the contract is now determinate: valid close, base invalid close,
no-process fault, reservation arithmetic, hash chain, §3a completion, roots/graph,
isolation, and the draft/label boundary all force one output. Fixing M-1..M-6
(all localized to §2a/§2c.8/§2c.12b/§4d/§6b + Examples B–C) should make the whole
machine two-implementer-deterministic without touching the resolved v1 repairs.

---

## Answers to the closure's three Opus questions

1. **Do §2c.6/12/12a/12b and §3–§3a close C-1, C-2, R5, R6 exactly?** C-1, C-2
   (base), and R5: **yes, exactly.** R6 (siblings): **not exactly** — the sibling
   force-close is stated but its event order (M-3), its collateral cause (M-4), and
   its interaction with the pinned constructor and E1 crossing (M-1, M-2) are
   under-determined or contradictory.
2. **Do §9/§11 match the pinned verifier?** **Yes** — roots tuple, `__main__` CLI,
   no new entry point, static adapters, allowlist commitments, ownership; every
   future amendment is named (C-4, R10–R12 fully closed).
3. **Is the no-amendment classification correct (C-3 repaired back to v2.1)?**
   C-3 itself: **yes.** The overall "no amendment" claim: **not established**,
   because M-1 may require a metering-core amendment and M-5 states a
   non-derivable clause.

---

## Gate and negative authorization

This is a REVISE: the governance-permitted confirmation identifies concrete
Critical contradictions (M-1, M-2) plus finite Majors (M-3, M-4, M-6) and a Minor
(M-5), all localized to the new §2a/§2c.8/§2c.12b/§4d/§6b material and Examples
B–C. A v2.1 applying R-M1..R-M6 (with the concurrent Y-line confirmation) would,
on my read, be X-line confirmable and two-implementer-deterministic without
reopening C-1..C-4/R5..R12.

This confirmation authorizes **nothing** beyond, upon a future positive
confirmation, Kirill's informed contract signature; it authorizes **no**
implementation, no `generic_harness.py`, no CLI, no `runtime_control/` or
manifest, no activation authorization or activation, no capability, world,
learner, process, lease, entropy, draft-manifest instance, E1/E2/E3 spend, or any
T/Q/C datum, ledger event, lock, escrow, outcome, or claim movement. No
implementation hash, reviewed HEAD, or production source set is pinned here.

T remains `NOT_ACTIVATED` at genesis; the predecessor line remains immutable,
`OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain permanently non-citable
for C1–C6; `Q_CAP_EXHAUSTED_NO_QUALIFIER`, invalidity, author stop, and E1
exhaustion remain non-scientific destinations; only a valid, independently locked
C execution may ever move an Officina claim. No prediction is made about any
learner or about Philosophia being proved, falsified, or bounded; the programme
claim remains `OPEN`.

— Opus 4.8, X-line. No scientific outcome is asserted or predicted in this
document.
