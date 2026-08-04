REVISE_OFFICINA_P1_WATCHDOG_V2_3

# Final X-line confirmation — Officina P1 watchdog-freeze author choice, v2.3

## INDEPENDENCE DEFECT — READ FIRST

**This review is not independent, and must not be recorded as an independent
X-line confirmation.**

The same model instance that authored the v2.3 packet, the peer amendment,
composite v1.3 and the v2.3 closure — in the immediately preceding turn of this
same session — produced this document. The closure under review states the rule
being broken:

> "Written by **Claude Code Opus 5 acting only as the specification author**,
> which authored the historical chain and therefore **cannot** be its
> independent X or Y reviewer. Every author closure … is an untrusted
> self-assessment."

The governing chain's whole review architecture rests on the X line and the Y
line being separate from the author. A self-review cannot discharge that. **The
verdict below is emitted because the audit found blocking defects and those
findings are useful regardless of who found them — a self-review that returns
REVISE is evidence about the artifact; a self-review that returned CONFIRMED
would have been evidence about nothing.** Had this audit come out clean, the
correct output would have been a refusal to certify, not a confirmation.

**Required:** a genuine X-line pass by a reviewer that did not author these
bytes, before any author-choice token is authorized. This document should be
filed as an author self-audit.

**Scope.** Bounded confirmation against the new governing bytes. No existing
file was modified. Nothing was committed.

---

## §1. Custody — recomputed

```text
4244e331dc7530dad743c640ae16ada048aed7cd2ec58822bf2d0dde77c8ffcc
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md   MATCHES
380b87f0524ac06ef2fb0173c83b234c3eedc34344c3c61ed9415bd2c1a63858
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_DRAFT.md   MATCHES
b510a7b504ddc370529a7d968d362ccff332538d6bb493b387a2bc0ae4e9db54
  successor/…P1_OPERATIVE_COMPOSITE_V1_3.md   MATCHES
9a5e400c4762d937072bb008b7ada9e1c3e4d7705a25ff92aa5fcfedcf76a347
  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_3_closure.md   MATCHES

HISTORICAL BYTES: `git status --porcelain successor/` reports ZERO modified
files. Composite v1.2 still hashes 2c857fa8…; …V2_1_CORRECTION.md still hashes
9f1d018e…. The claim that this round edited no history REPRODUCES.
```

---

## §2. The bounded question, answered

**Replacing historical enumeration with restatement DID create an
omitted-restatement defect.** It is not a single miss; it is a cluster of six,
four of them blocking under the standard the bounded question sets: *a
behaviourally required rule that exists only in immutable history is blocking.*

A fifth blocking defect is independent of restatement: **guard `G-10` is
unsatisfiable and would make composite v1.3 permanently non-operative.**

The architecture is sound. The execution is incomplete.

---

## §3. Blocking findings

### `X23-B1` — the quiescence loop bound and interval exist only in immutable history

```text
USED, in governing bytes, twice:
  peer amendment §A3.3 step 3 (:328)
    "Repeat at `T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS` up to
     `T_WATCHDOG_QUIESCE_MAX_PASSES`, issuing SIGKILL … after the first failed
     pass"
  peer amendment §A3.4 (:366-367)
    "take up to T_WATCHDOG_QUIESCE_MAX_PASSES further samples at
     T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS, RE-PROVING quiescence each pass"

DEFINED, in governing bytes: NOWHERE.
  peer amendment      — name only, no value
  composite v1.3      — zero occurrences of either name
  accepted harness chain (V2_DRAFT, V2_1, V2_2, V2_3, V2_3_1) — zero occurrences
  batch-settlement amendment — zero occurrences

DEFINED, in immutable provenance only:
  …SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md:60-61
      T_WATCHDOG_QUIESCE_MAX_PASSES       = 8
      T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS = 100_000_000
  …SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md:89-90   (identical)
```

Under `DA-1` and composite authority level 3 no implementer or verifier may
open those files. **The §A3.3 termination bound and the whole §A3.4
strict-progress branch are therefore not constructible from governing bytes.**
An implementer must either open a provenance document — forbidden — or invent
two constants, which changes when a freeze gives up and therefore changes which
settlements are `PROVED` versus `UNKNOWN`. That is a scientific-outcome-bearing
invention.

**Smallest exact repair — peer amendment §A3, new §A3.0, before §A3.1:**

```text
### §A3.0 Constants this section requires

QC-1  T_WATCHDOG_QUIESCE_MAX_PASSES       = 8
QC-2  T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS = 100_000_000    # 100 ms
QC-3  T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS    = 1_000_000_000  # 1 s
      T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS is defined by composite v1.3 §P1-2 and
      is not restated here.
QC-4  These values are RESTATED, not chosen. They reproduce the values the
      historical chain carried, and no value moves. They appear here because
      §A3.3 and §A3.4 require them and no live document else defines them.
```

### `X23-B2` — the forbidden-disposition rule is gone, and the live chain positively permits what it forbade

This is the most consequential finding, because the missing rule is not merely
absent — **the accepted, live harness contract states the opposite in the
neighbouring direction.**

```text
THE HISTORICAL RULE, …V2_1_CORRECTION.md §W3.4 (immutable provenance):
  "Forbidden dispositions on a watchdog freeze: T_PROCESS_CLOSED,
   T_PROCESS_VOLUNTARY_STOP, T_PROCESS_E1_EXHAUSTED, T_PROCESS_E3_DUE, and —
   named explicitly, closing X-C4.1 — T_PROCESS_RESOURCE_STOP … No valid close,
   exhaustion, pause, or review terminal may arise from an overrun."
  "Cause is single-valued: a positive confirmed watchdog overrun has [cause
   PROCESS]."

IN GOVERNING BYTES: ZERO occurrences of T_PROCESS_CLOSED,
T_PROCESS_VOLUNTARY_STOP, T_PROCESS_E1_EXHAUSTED, T_PROCESS_E3_DUE or
T_PROCESS_RESOURCE_STOP, in either the peer amendment or composite v1.3.

WHAT THE LIVE CHAIN SAYS INSTEAD:
  OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:140-142 — an ACCEPTED, LIVE
  peer contract — defines:
    "7. **Resource stop** (P3→P4): identical order, disposition
        `T_PROCESS_RESOURCE_STOP`; actual overrun recorded in full, never
        clipped."
```

The peer amendment says a freeze routes to "record-first live-process
invalidity … public cause `PROCESS`" (`S-2`, §A3.3 context). It never says which
terminals are **forbidden**. A conforming implementer reading only the governing
surfaces sees a live contract that assigns `T_PROCESS_RESOURCE_STOP` to an
overrun-bearing transition and no governing rule forbidding it on a deadline
freeze. **The closure of X-C4.1 — an explicitly named prior X finding — is lost.
A valid terminal becomes reachable from an overrun.**

**Smallest exact repair — peer amendment, new §A3.6:**

```text
### §A3.6 Forbidden dispositions and single-valued cause

FD-1  FORBIDDEN DISPOSITIONS ON A DEADLINE FREEZE — the freeze §A3 performs on
      either route. None of the following may be selected, on any path, from any
      freeze of this section:
        T_PROCESS_CLOSED          T_PROCESS_VOLUNTARY_STOP
        T_PROCESS_E1_EXHAUSTED    T_PROCESS_E3_DUE
        T_PROCESS_RESOURCE_STOP   — named explicitly, and this is the closure of
                                    X-C4.1; it is unreachable anyway because the
                                    signed cooperative quiesce→charge→record
                                    order cannot be supplied by a
                                    non-heartbeating controller
      NO VALID CLOSE, EXHAUSTION, PAUSE OR REVIEW TERMINAL MAY ARISE FROM AN
      OVERRUN. This rule binds the deadline freeze only; the accepted harness
      contract's ordinary P3→P4 resource-stop transition is untouched.

FD-2  CAUSE IS SINGLE-VALUED. A positive confirmed overrun has public cause
      PROCESS and no other, on both ROUTE-D and ROUTE-W.

FD-3  ROUTING, restated in full so no historical section is opened:
        quiescence = PROVED  ⇒ overrun_ns = freeze_ns − deadline_ns (> 0)
                             ⇒ signed record-first live-process invalidity,
                               all-live batch, public cause PROCESS
        quiescence = UNKNOWN ⇒ the same invalid route with the §4c(c)/§4d
                               unknowable pool; NO timestamp is synthesized
```

**A companion line is required in composite v1.3 invariant 89** so the
prohibition is mechanically tested, e.g. appending: *"and a freeze observation
or fallback whose settlement selects any of `T_PROCESS_CLOSED`,
`T_PROCESS_VOLUNTARY_STOP`, `T_PROCESS_E1_EXHAUSTED`, `T_PROCESS_E3_DUE` or
`T_PROCESS_RESOURCE_STOP` is rejected."*

### `X23-B3` — both route triggers are unevaluable: ack semantics are not restated

```text
GOVERNING TEXT THAT DEPENDS ON THEM:
  §A3.1 ROUTE-D precondition   "if a strictly greater table_seq is durable AND
                                ACKED"                        — "acked" undefined
  §A3.1 ROUTE-W trigger        "now_ns − updated_monotonic_ns >
                                T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS with no ack
                                for that table_seq"  — updated_monotonic_ns and
                                                       "ack" undefined
  §A8 NS-4                     "Liveness is judged on the watchdog's OWN
                                sample"                — the sample is undefined

ABSENT FROM BOTH GOVERNING FILES AND FROM THE ACCEPTED PEER CHAIN:
  the ack frame schema `philosophia.officina.t-watchdog-ack.v1` and its key set
  the predicate healthy(table_seq)
  the predicate dead
  the constant T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS
  the field ack_monotonic_ns and the field updated_monotonic_ns

PRESENT ONLY IN IMMUTABLE PROVENANCE: …V2_1_CORRECTION.md §W3.2.
```

Both entry routes of §P1-13.9 and §A3.1 turn on "acked" / "not acked". Neither
predicate is defined in any file an implementer is permitted to open. **The
route selection itself is not constructible.**

**Smallest exact repair — peer amendment, new §A2.4 or an addition to §A8:**

```text
### §A8.1 Publication, acknowledgement and liveness — restated

AK-1  The lease table `WATCHDOG/LEASES.json` is written atomic-replace with
      `table_seq` STRICTLY INCREASING, and the identical payload is published on
      the update pipe, BEFORE the first SIGCONT, BEFORE any capability becomes
      usable, and BEFORE any operation admission. The supervisor must observe
      the watchdog's ack of that exact `table_seq` first; otherwise it refuses
      START and OPERATION_ADMIT with REFUSED/WATCHDOG_UNACKED.

AK-2  ON RENEWAL the old deadline remains authoritative until the successor
      table is acked. No unacknowledged update ever extends behaviour.

AK-3  Ack frame keys exactly:
        schema ("philosophia.officina.t-watchdog-ack.v1"), scientific_outcome,
        supervisor_generation_sha256, table_seq, ack_monotonic_ns

AK-4  LIVENESS IS JUDGED ON THE WATCHDOG'S OWN SAMPLE, never on the
      supervisor's read time:
        healthy(table_seq) <=> ack_monotonic_ns − updated_monotonic_ns
                               <= T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS
        dead               <=> the supervisor has drained the ack pipe and
                               now_ns − updated_monotonic_ns >
                               T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS
                               with no ack for that table_seq
      `updated_monotonic_ns` is the supervisor's monotonic sample at which it
      published that `table_seq`. A supervisor busy inside a bounded chunk
      therefore cannot declare a healthy watchdog dead.

AK-5  "ACKED", as used by ROUTE-D's precondition, means exactly: an ack frame
      for that `table_seq` has been drained and healthy(table_seq) holds.
```

### `X23-B4` — guard `G-10` matches its own definition and can never be satisfied

Independent of restatement. **This alone prevents composite v1.3 from ever
becoming operative.**

```text
G-10, at composite v1.3 §P1-14.3, INSIDE THE BODY REGION:
  "Search the normalized body region for the two-character-bracketed markers
   "[W-A]" and "[W-B]". A single occurrence of either ⇒ "guard G-10: unresolved
   watchdog-freeze variant block"."

G-10'S OWN DEFINITION CONTAINS BOTH LITERAL MARKERS, AND IT IS IN THE BODY
REGION IT SEARCHES. After the handoff's step 3 resolves and deletes all
twenty-eight variant blocks, G-10's own text still contains "[W-A]" and "[W-B]",
so G-10 fires forever and NO BUILD EVER PASSES.

THIS VIOLATES THE COMPOSITE'S OWN STATED DESIGN RATIONALE, §P1-17:
  guard patterns "live in their own region so that they are NEVER MATCHED
   AGAINST THEMSELVES, and their digest is H_GUARDDATA".
G-1..G-5 obey it. G-10 does not.

SECOND-ORDER CONSEQUENCE: the packet's §7 step 4 and the closure's §C4 step 3
both require "guard-fire counts remain ZERO" after resolution. With G-10 as
written that requirement is unsatisfiable, so the handoff can never complete.
```

**Smallest exact repair — two coordinated edits, both inside composite v1.3:**

```text
(a) §P1-14.3, REPLACE G-10's body so it carries no literal marker:

  G-10 UNRESOLVED AUTHOR-CELL VARIANT BLOCKS. Match the normalized body region
       against the VARIANT_MARKER pattern set of §P1-17. A single occurrence ⇒
       "guard G-10: unresolved watchdog-freeze variant block". Before the
       watchdog-freeze author cell is signed every occurrence is expected and
       the document is not operative; after signature exactly one branch of each
       block is retained inline and no marker remains. THERE IS NO STATE IN
       WHICH A MARKER IS PRESENT AND THE DOCUMENT IS OPERATIVE.

(b) §P1-17 GUARDDATA region, ADD the pattern set alongside G-1..G-5, and amend
    that section's opening sentence to read "guard rules G-1 through G-5 and
    G-10":

  VARIANT_MARKER:
    "[W-A]"    "[W-B]"

This restores the self-matching immunity §P1-17 exists to provide, and brings
G-10's patterns under H_GUARDDATA and G-6 like every other matching guard.
```

---

## §4. Non-blocking findings requiring repair

### `X23-M1` — §A7's swap-only carve-out is not constructible

§A7 names `t-replacement-freeze.v1`, `WATCHDOG/REPLACEMENT_FREEZE/<replacement_freeze_id>.json`,
`swap_only: true` and "the recorded resume predicate". It supplies **none** of:
the `replacement_freeze_id` preimage; the record's key set; the
`.resumed.json` (`t-replacement-resume.v1`) and `.invalidated.json`
(`t-replacement-invalidation.v1`) companion objects and their key sets; the
`invalid_condition ∈ {I1..I7}` domain; or the `ACK_PENDING` state rule. All live
only at historical …V2_1_3_CORRECTION.md §U3.3. **Restate them in §A7, verbatim
in substance**, or state explicitly that the swap-only carve-out is deferred and
that no swap-only freeze is reachable until it is — the latter is not
recommended, because ROUTE-W depends on the carve-out to avoid writing a witness
for a non-overdue group.

### `X23-M2` — the total consumption order across object classes is absent

`F-4` orders **witnesses only**. Historical §N5.5 defined one total order across
witnesses, fallbacks **and** replacement-freeze records —
`(generation == current) desc, table_seq asc, process_id asc, object class:
FREEZE_FALLBACK before FREEZE, fallback_witness_id / witness_id asc`, with "if
any fallback exists, the FALLBACK is authoritative" — plus the duplicate
(`EEXIST`) and conflict (differing `rejected_object_sha256_or_null`) rules.
Governing bytes define the interaction of the three classes nowhere. **Restate
§N5.5's production / duplicate / conflict / consumption block in peer amendment
§A6.**

### `X23-M3` — the lease-table publication rule is absent

Covered by the `AK-1`/`AK-2` text of `X23-B3` above; listed separately because
it is a distinct historical rule (§W3.2) with its own consequence: without it,
nothing in governing bytes forbids admitting operations against an
unacknowledged lease table.

### `X23-M4` — the governing count 112 is not reproducible, and double-counts

```text
FILE 1 REPRODUCES EXACTLY.
  DA 4 + WA 6 + TIMING 4 + F 8 + KW 3 + S 5 + NS 4 + H 4 + N 8 = 46 named rules
  + 10 conjuncts + 6 sequence steps + 2 routes                  = 64   CONFIRMED

FILE 2 DOES NOT.
  claimed:  23 replacements + 3 sections + 2 guards + 12 tests + 8 governance = 48
  The packet enumerates the eight governance edits as "level 3, level 3a,
  peer-contract paragraph, blocking-notice cell 2, status, C1 MASTHEAD, negative
  space, provenance region".
  C1 IS DOUBLE-COUNTED: the C1 masthead edit is R1, already inside the 23.
  AND THE SET IS INCOMPLETE: the title edit, the "full replacement for v1.2"
  edit, the blocking-notice HEAD edit (distinct from the cell-2 tail) and the
  provenance-digest addition are all edits to v1.2 text and appear in neither
  the 23 nor the 8.
  Counting distinct governance edits to v1.2 text gives TEN, not eight, so
  File 2 = 23 + 3 + 2 + 12 + 10 = 50 and the total is 114, not 112.

ROOT CAUSE, and it is the Y line's `Y22-2` recurring in a new form: v2.3 states
a valid MEMBERSHIP rule (governing iff inside one of two named files) but states
NO COUNTING rule — no definition of what constitutes one locus, and no
disjointness requirement between the five File-2 categories. A cardinality
without a counting rule is not reproducible, and this one is demonstrably not.

REPAIR: state the counting rule explicitly, require the categories to be
pairwise disjoint, and recompute. The count is bookkeeping and moves no
mechanism — but v2.2 was revised in part for exactly this class of defect, so it
should not survive a second round.
```

---

## §5. What I confirm

### Mechanical derivation of composite v1.3 — CONFIRMED

```text
SOURCE  v1.2  2c857fa8…  (recomputed, unchanged)
RESULT  v1.3  b510a7b5…  (recomputed, matches)
The generator asserted each of 37 anchors matched EXACTLY ONCE and refused
otherwise; the diff resolves to 31 hunks (adjacent anchors merge).
Six sentinels, one occurrence each, in order, at 214 / 3104 / 3106 / 3141 /
3143 / 3223. Region scheme intact.

EVERY v1.2 WATCHDOG-EXECUTOR ORIGINAL IS GONE — each verified at zero
occurrences in v1.3:
  "witnesses and freezes."                    "it physically emits freeze observations"
  "freezes the groups it knows"               "writes its final observations"
  "This is the R-L5 case"                     "called from the watchdog role entry"

NO RAGGED OR CONTRADICTORY RESIDUE FOUND. One line-wrap artifact from the
generation pass had already been repaired before publication; I re-read the two
sites and both are clean.

CORRECTED ACTION ALPHABET SWEEP. Searching v1.3 for `watchdog` within 90
characters of `executes|freezes|writes|records|proves|kills|killpg`, excluding
negated constructions, returns exactly ONE hit — the `WATCHDOG_UNREAPED` reap
sentence at :1563, which assigns no freeze authority. NO SURVIVING WATCHDOG
EXECUTOR OR EVIDENCE WRITER.
```

### `ROUTE-D` / `ROUTE-W` — CONFIRMED

Both are named and declared exhaustive at peer amendment §A3.1 and composite
§P1-13.9. Both are `SIGNAL_GROUP`-mediated. Both carry `killer = SUPERVISOR`,
the same schema, the same namespace, the same predicate and the same writer.
They are enumerated consistently in row 4's executing-process block, `SW-2`,
§P1-13.7's writer row, §P1-13.8, §P1-13.9 and invariant 89(a), and are exercised
together by test 95. The "two triggers of one procedure, not two writers"
framing is correct and is the right answer to `X22-C3` / `Y22-3`. **One evidence
writer throughout.**

### Variant blocks and implicit selection — CONFIRMED

Twenty-eight `[W-A]`/`[W-B]` markers, **all inside the BODY region**; zero in
GUARDDATA or PROVENANCE. Neither option is implicitly selected: every variant
site carries both branches, the status line names both cells, and the
recommendation is stated as a recommendation, not as a default. `G-10`'s
*intent* is correct; its *implementation* is defective (`X23-B4`).

### `G-11` and the handoff unit — CONFIRMED IN SUBSTANCE

`G-11` covers the peer amendment, the composite, every provenance digest and
every accepted peer-chain digest; it runs before any process is created, any
handle is allocated or any freeze route is reachable; and it refuses with
`WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE`, with no silent degradation to the
historical behaviour. **No partial runnable state is reachable through `G-11`.**
Two minor gaps: `G-11` is defined once and referenced nowhere else in the
composite — not in §P1-14.5's reporting list, and test 103 names the refusal
token but not the guard; and the "guard-fire counts remain zero" requirement is
currently unsatisfiable for the separate reason at `X23-B4`.

### Document-level authority proof — CONFIRMED

§C2's six steps reproduce on the bytes. Composite v1.2 `:42-49` enumerates
documents; the binding sits at `:2851` inside §P1-18 PROVENANCE and nowhere
else; v2.1.10.5/.6/.7 sit at `:2852-2854` and were never classified by any prior
packet; and §W6.5's ten carrying references reproduce at every cited line.
`DL-1`..`DL-6` are a valid authority rule and are correctly applied. **Zero
historical loci carry force; zero historical bytes were edited.** The
withdrawal of 40/45/62/18 as authority cardinalities, and their retention as
occurrence data, is correct and correctly reasoned.

### Prior accepted contents — CONFIRMED UNCHANGED

W-A's gate, one-shot grammar, service window and pricing; W-B's endpoint-loss
semantics, record-first journal and crash matrix; `A-ABS-1`..`A-ABS-6`;
`SEP-1`..`SEP-3`; the `R2`/`R9` separation; `L6`..`L9`, `ND-1`..`ND-4` and the
PCS journal boundary (restated at §P1-10.7 with test 101); `_CLOCK_MONOTONIC`,
`B-1`..`B-8`, `S-25`; the two signed execution sites, `S-12` and the
sole-`killpg`-caller rule; §P1-8.7 byte-unchanged; the four read-only identity
loci carried **verbatim**; the filename and namespace conclusions; the six
tokens with none added, removed or renamed;
`I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER` not revoked, re-run or
reopened. **W-B remains recommended and nothing asymmetric moved.** Negative
space is intact in all four documents.

---

## §6. Summary against the eight audited items

| # | Item | Result |
|---|---|---|
| 1 | historical rules → new locus, stated drop, or blocking omission | **SIX OMISSIONS FOUND**, four blocking (`X23-B1`, `X23-B2`, `X23-B3`) plus `X23-M1`, `X23-M2`, `X23-M3` |
| 2 | sequence, ordering, witness production/consumption, ten conjuncts, fallback keys/routing, swap-only, strict progress, ack, timeout, recovery | Sequence, step ordering, witness production, ten conjuncts and fallback key set **CONFIRMED**. Strict-progress branch **BLOCKED** (`X23-B1`). Ack/timeout **BLOCKED** (`X23-B3`). Swap-only **NOT CONSTRUCTIBLE** (`X23-M1`). Cross-class consumption order **ABSENT** (`X23-M2`) |
| 3 | mechanical derivation, no residue, history unchanged, corrected alphabet clean | **CONFIRMED**, all four |
| 4 | two governing files, 112 loci, zero historical force, zero historical edits | Two files **CONFIRMED**; zero force and zero edits **CONFIRMED**; **112 NOT REPRODUCIBLE** (`X23-M4`) |
| 5 | routes exhaustive, both mediated, one writer, consistent counts | **CONFIRMED** |
| 6 | variant blocks non-operative, `G-10` refuses, no implicit selection | Intent and non-selection **CONFIRMED**; `G-10` **BLOCKED** (`X23-B4`) |
| 7 | `G-11` all-or-none, no partial runnable state | **CONFIRMED IN SUBSTANCE**, two minor gaps |
| 8 | prior W-A/W-B contents, recommendation, negative space | **CONFIRMED UNCHANGED** |

---

## §7. Verdict

The v2.3 architecture is correct: the document-level authority rule is valid,
the binding and v2.1.10.5/.6/.7 are correctly dispositioned, history is
byte-intact, the composite is genuinely mechanically derived, the two freeze
routes are exhaustive with one evidence writer, and every previously confirmed
cell survives.

But the move from enumeration to restatement was not carried to completion. Four
behaviourally required rules — the quiescence loop constants, the
forbidden-disposition prohibition, the ack/liveness semantics, and (with them)
the lease-publication ordering — now exist **only in immutable history**, which
the bounded question defines as blocking. The forbidden-disposition gap is worse
than an omission: the live accepted harness contract positively assigns
`T_PROCESS_RESOURCE_STOP` to an overrun-bearing transition, so losing §W3.4's
prohibition makes a valid terminal reachable from a deadline freeze and silently
reverses the closure of X-C4.1. Separately, `G-10` matches its own definition and
would make composite v1.3 permanently non-operative.

Every repair is bounded, lands only in the two governing surfaces, edits no
history, opens no author cell, adds no mechanism and moves no recommendation.
Exact text is given at §3 and §4.

```text
REVISE_OFFICINA_P1_WATCHDOG_V2_3
```

**Kirill's watchdog author-choice token is NOT authorized.** No selection token,
no per-option amendment token, no common amendment token and no acceptance token
is signable on these bytes.

**And, independently of the technical verdict: this audit was performed by the
author of the reviewed bytes and cannot serve as the X-line confirmation the
chain requires.** A reviewer that did not author these documents must repeat it.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CELL = NOT SELECTED
PROCESS-IDENTITY CELL = NOT SELECTED
```

This document modified no existing file, committed nothing, and executed no
process.
