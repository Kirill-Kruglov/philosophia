# Officina P1 W-B v2.15 — author closure of the bounded final repair

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This closure is an untrusted
self-assessment and is normative for nothing.** Where it and the governing bytes
differ, the governing bytes govern and this file is the defect.

---

## VERDICT

```text
READY_FOR_OFFICINA_P1_WB_V2_15_FINAL_XY_CONFIRMATION
```

`T = NOT_ACTIVATED`; programme claim = `OPEN`. This verdict is an author
readiness statement and nothing else. It authorizes no acceptance, no code, no
key, no `OR` step, no install and no activation, and it does not predict either
independent line's verdict.

---

## §1. Inputs — recomputed before any analysis, all eight match

Not `BLOCKED`.

```text
3571c1f75283851e4cf1a9b04dfe67c2f35d9c52392e6b97582274195b475cf7   26921  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_14_CORRECTION.md      OK
5f2c74ff371f618039de705f21464454684da122f91e06c251e147bfc61d26be  316520  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11_DRAFT.md OK
11c8963ac3cbd4c72a90b0a1f0fdc0fe3bfb35be84a974c3a2a953ec699bbdee  627683  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_14.md OK
0b08bd3e5e49666dddb475c1e282589a0c1d940221bdebf7ca132a860d4564f1   96916  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V5_DRAFT.md                        OK
9b07b718a6f5de7c27d05bec6a205813329255b8b344adfe0447338357814a77   40819  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V5_DRAFT.md                        OK
b981a88e724c493f2d84d1a92d448394ce21f931e5584fe8f49690b0158b9f92   44264  reviews/opus5_officina_p1_wb_v2_14_governing_repair_closure.md                     OK
685bc98fa0912f78a57be2667881ee3679e9d85542d1e10839d31625049f6bea   27981  reviews/fable_officina_p1_wb_v2_14_final_x_review.md                               OK
5ad7130119ff952a2ef0939451271146c98dd52948db8156eaeb47208cfaad49   13189  reviews/sol_officina_p1_wb_v2_14_final_y_review.md                                 OK
```

Working tree at commit `bfe462c`. The two reviews were treated as **evidence**:
every finding was reproduced against the pinned bytes before any repair was
made, and the reproductions are in §3 and §4.

---

## §2. Outputs — the six deliverables, with byte lengths and digests

```text
6a00e058e35ab4f81d80b21d5a6680344596231f1299767a076813691723f26a   28791  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_15_CORRECTION.md
e156d66293a608c9090994ae1016c1055a1c9071b71ea0384c58e7ab2595f4a8  314994  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12_DRAFT.md
a41c142465c3ab0e3dfc565b6f2c1767f1b43481c28933544d72777d6e76113a  668002  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_15.md
c9db32bb8b87af691c71c51a6167883cc953a43700798c9654c39d84ad1c2ff2  102351  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V6_DRAFT.md
279f59a2de2d3d382a30463b0c72e08108f93ad3ed15473fee145d6361ebc1f1   47240  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V6_DRAFT.md
                                    this file, whose digest a reader recomputes  reviews/opus5_officina_p1_wb_v2_15_final_repair_closure.md
```

Composite region digests, extracted by `§P1-14.0`'s own algorithm:

```text
H_BODY       fdd6386b53c0ea4918ff66d49aa23c2b911e2ad72fc0481f7effed5b03f940f5   630161 bytes
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426     1816 bytes
H_NORMATIVE  0fd3d8b396a7de754f1b7df7159777e76702800b91f57b9cfbe7e17caea16c9d
H_FILE       a41c142465c3ab0e3dfc565b6f2c1767f1b43481c28933544d72777d6e76113a   668002 bytes
```

**This file contains none of its own digests**, and the composite contains none
of its own, so the custody chain stays acyclic (`§P1-14.5`).

---

## §3. One-to-one dispositions — Sol

### `Y14-M1` — KG-2 permitted a second write and P-9/P-10 overlapped

**REPRODUCED, THEN REPAIRED.** Both counterexamples were re-derived from the
pinned v1.14 bytes before anything was written; the before/after executions are
in §5.

`P-2`'s `K5` was an **if and only if** over four conjuncts, with the explicit
sentence *"THE FOUR CONJUNCTS OF THE POPULATION PREDICATE ARE THEREFORE outcome
== STOPPED, (i), (ii) AND (iii)"*. `K1`..`K6` contained no already-written test
and no recheck. `P-10`'s reissue row and mid-attempt row each gave the opposite
answer to `P-9`'s first row for a state that satisfies all four. `P-10`
additionally placed `EINTR during the K4 read` and deadline exhaustion inside the
`STOPPED` route while both tables claimed to be disjoint.

**REPAIR.** The four-conjunct `if and only if`, the `K1`..`K6` order and the
two-table split are withdrawn. `P-2` is an ordered machine `W0`..`W8` with nine
mutually exclusive and exhaustive routes; `W0` pins handle existence, generation
validity, the state precondition, role eligibility and the **prior-write
boolean** before any observation; `W3` is the prior-write branch; `W4` holds
`EINTR` and deadline exhaustion **inside the one observation**; `W6` is the named
linearization point `L` with exactly two rechecks; `W7` is the only write. `P-9`
is the one total disjoint partition and `P-10` is the executable cross-product
that checks it. Atomicity is taken from `P-3`, `§P1-8.4`, `§P1-3.2` and
`§P1-8.6` — **no new writer, no new evidence class, no lock, no
compare-and-swap.**

### `Y14-M2` — the v5 handoff delegated authority to v4 and to composite v1.13

**REPRODUCED, THEN REPAIRED.** Handoff v5 line 76 named
`OFFICINA_P1_WB_POST_SELECTION_BINDING_V4_DRAFT.md` and said the binding governs
on disagreement; lines 90–91 and 194 named composite **v1.13** as the frozen
behaviour source, and line 91 paired that v1.13 path with the **v1.14** digest
`11c8963a…`, while the actual v1.13 digest is `15e11f0e…8fb3`. `§H1` `R-1` says
those are the **only** documents opened for behaviour.

**REPAIR.** Handoff v6 carries one current-authority table pairing every path
with its own recomputed digest, and one precedence rule over current files only.
See §6.

### `Y14-M3` — handoff `D-6` required the valid enumeration to fail

**REPRODUCED, THEN REPAIRED.** Handoff v5 `D-6` fixed `total 89` and `TS-3
member_count 89` and then required `63, 69, 73, 77, 81 or 89` to FAIL, while
binding `PR-4` and handoff `T-14` required `63, 69, 73, 77, 81, 85, 93`.

**REPAIR.** `D-6` derives the cardinality from this generation (93), requires 93
to PASS, and lists only retired values. The three loci now agree exactly.

### `Y14-L1` — the provenance narrative named the wrong review generation

**REPRODUCED, THEN REPAIRED.** Composite v1.14 line 8387 read *"the two
independent final reviews of the v2.12 pair"* while the literal rows and
normative `MS-2` named the v2.13 reviews.

**REPAIR.** The composite's `§P1-18` paragraph now names the **v2.14** pair, and
states in terms that the generation name is read off the literal rows that
entered with it.

---

## §4. One-to-one dispositions — Fable

### `X-1` — the pinned `H_HANDOFF` was the stale v1.13 value in both files

**REPRODUCED, THEN REPAIRED, AND NOT GRADED AWAY.** Running the section's own
published extraction over the pinned v1.14 bytes:

```text
HANDOFF(composite v1.14)   4168 bytes  7d5cd45363f197905f4b3d4e6fa1b470b4bb595ec00ea423775412459f340084
HANDOFF(amendment v1.11)   4168 bytes  7d5cd45363f197905f4b3d4e6fa1b470b4bb595ec00ea423775412459f340084
IDENTICAL: yes.  PINNED IN BOTH FILES: 7c5cabe2e48587ad34cd19ae0f4300f78965b27afc93cb719868aae9f5cd44a7
```

The first conjunct of the required equality held; the second was false in both
files. **The X line's reasoning about consumption is accepted and is not
disputed** — no `G-*`, `OR`, manifest, `MS`/`CK`/`IR`/`TS` or verifier rule reads
`H_HANDOFF` — and the repair is made anyway, because the pair's own clause says
*any difference is a defect in this indivisible pair* and the author declines to
keep a false normative sentence on the strength of it not being load-bearing.

**REPAIR.** Both governing files now carry the measured value and its measured
length, extracted independently from each file **after every other v2.15 change**,
and both state that the value is measured on these bytes and on no predecessor's.
See §7.

### `X-L7` — Phase 3 carries more than one terminal-bearing predicate

**REPRODUCED, THEN CLOSED.** `SC-10` asserted that Phases 1, 2 and 3 each carry
exactly one. Phase 3 in fact carried `KV-6(a)`, `P3(a)`'s fail-closed route on a
non-`PRESENT_VALID` self-observation, and `P3(c)`'s fail-closed route on an
absent, unreadable or non-conforming `SPAWNING_GROUP.json` — and `P3(c)` named
**no terminal at all**, while `P3(a)`'s sentence named `T3` where `SC-8` and
`SC-10` name `T1` for the same state.

**CLOSED, NOT SUPPRESSED.** `SC-9` `P3` now enumerates **five** terminal-bearing
predicates and gives Phase 3 the same explicit shape Phase 4 has: `STEP 3A`
collects both fallible construction sources without selecting a terminal;
`STEP 3B` reduces under the same `STRUCTURAL DOMINATES FORBIDDEN` precedence and
one fixed source order that is a property of the clause rather than of any table;
`STEP 3C`'s table scan is reachable only when `G` exists. `SC-10` is corrected to
say Phases 1 and 2 carry one each and Phase 3 carries five, and the reduction is
proved total and order-invariant over all five. The multi-fault fixture that
version 1.14 would have answered two ways — an `ABSENT` own-group observation
beside a structurally faulting record read — is required at row 89 clause `(6D)`
and answers `T1`.

### `X-L8` — the watchdog written-group self-collision

**REPRODUCED, THEN CLOSED — NOT CALLED LATENT.** `P3(b)` admits every watchdog's
`pid` **and** its non-`NULL` `pgid_or_null` into `G`, and the `P3` scan then
tests every current-generation entry's recorded group against `G` regardless of
role; a watchdog whose field had been written matched `G` through its own
contribution and terminated the classifier with zero signals in that pass and
every later pass. Version 1.14's `P-4` wrote that field *"exactly as any other
handle does"* and called it *"deliberate and load-bearing"*.

**THE ROUTE IS CLOSED AT THE ELIGIBILITY GATE.** `KG-2` `P-2` `W0` (c2) refuses
population eligibility for role `WATCHDOG` before any observation is taken, and
`P-4` states that a watchdog's `pgid_or_null` is never written on any path, at
any state, at any ownership and on any outcome. **The normal `setsid = False`
lifecycle is preserved exactly as it is** (`§P1-4.1`, `§P1-9.2`, byte-unchanged)
and is explicitly no longer the argument: the gate closes the route even if a
future generation changed the spawn flags. `§P1-8.3` is **not** narrowed —
`AWAIT_STOP` remains available for a `WATCHDOG` handle and only the `KG-2` write
is refused. `SC-9` `P3(b)`'s second clause is **retained unchanged** and is now
provably vacuous, which is exactly why the collision cannot arise. The
cross-product in §5 confirms that no combination with `role = WATCHDOG` reaches a
write.

### `X-L9` — the permutation-invariance justification overclaimed

**REPRODUCED, THEN CLOSED BY REPLACING THE TIE-BREAK.** The sentence *"the
least-index member of a non-empty class is the same ENTRY under every
permutation"* is false whenever a class has two or more members; three
`PRIMITIVE_FAULT` entries record a different site under different permutations.
The narrowing option — retaining the positional rule and claiming invariance only
for the terminal tuple — was available and **is not taken**, because the signed
handle schema already supplies a stable identity.

**CLOSED.** `STEP 4A` `(o1)` now collects the entry's **`handle_id`**, the
decimal key of `§P1-8.5`'s handle model, which is carried by the entry and never
reused within or across generations. Every tie-break at Phase 3, Phase 4, Phase 6
and `SC-10` is **least `handle_id`**. No input of any reduction is positional, so
the invariance extends to the recorded site as well as the terminal tuple. No
scientific identity is added, no field is introduced, and the sentence is
withdrawn rather than re-argued.

---

## §5. Before/after executions, and the machine-generated partition proof

### §5.1 The counterexamples, executed

The `P-9` row predicates were transcribed **as written** into free-standing
booleans over the raw dimensions, independently of the `P-2` control flow, and
both were evaluated on each state. `BEFORE` is what version 1.14's own clauses
assign to that state.

```text
COUNTEREXAMPLE A — reissue after a successful write, h.state still SPAWNED
  BEFORE  P-9 row 1 assigns THE ONE WRITE; P-3 and P-10's reissue row assign
          NO SECOND WRITE. TWO ANSWERS.
  AFTER   route R-D, exactly one row fires, observes = False, writes = False,
          pgid_is_leader = 1 derived only from the recorded fact.

COUNTEREXAMPLE A' — the same reissue, h.state moved out of SPAWNED
  BEFORE  the same two answers; version 1.14 did not distinguish the case.
  AFTER   route R-A0, exactly one row fires, observes = False, writes = False.
          BOTH ANSWERS ARE NAMED AND NEITHER WRITES, SO THE MACHINE IS TOTAL
          WHETHER OR NOT AN IMPLEMENTATION TRANSITIONS h.state ON STOPPED —
          a question this pair does not settle and does not need to.

COUNTEREXAMPLE B — generation invalidated after the observation, before the write
  BEFORE  the four-conjunct predicate mandates the write; P-10's mid-attempt row
          says no write lands. TWO ANSWERS.
  AFTER   route R-F, exactly one row fires, observes = True, writes = False,
          field left NULL, pgid_is_leader = 0, generation routes to §P1-11.6.

WATCHDOG POPULATION — role WATCHDOG, STOPPED, all three conjuncts available
  BEFORE  P-4: "written exactly as any other handle does" -> the X-L8 collision.
  AFTER   route R-A1, exactly one row fires, observes = False, writes = False.

ORDINARY LIVE-LEADER TIMEOUT — the retained v2.14 fixture
  BEFORE  v1.13: P-2 mandated the write, P-10 forbade it. v2.14 repaired it.
  AFTER   route R-C, exactly one row fires, observes = False, writes = False.
```

### §5.2 The machine-generated totality/disjointness table

Two independent implementations were run over the **full** twelve-dimension
product: `MACHINE`, which is `P-2`'s `W0`..`W8` written as control flow, and
`GUARDS`, which is `P-9`'s published row predicates written as free-standing
booleans with no reference to the machine. **Totality and disjointness are
decided on `GUARDS` alone.**

```text
CROSS-PRODUCT DIMENSIONS      12
  handle existence 2, generation at W0 2, role 3, state 4, prior write 2,
  outcome 4, KG-1 result 6, identity 2, group relation 2, EINTR 3,
  generation at L 2, field at L 2
COMBINATIONS ENUMERATED       110592   = 2*2*3*4*2*4*6*2*2*3*2*2

(x1) combinations with NO route                          0
(x1) combinations with TWO OR MORE routes                0
     ==> P-9 IS TOTAL AND DISJOINT
     MACHINE / GUARDS disagreements                      0

ROUTE COUNTS
  R-A0   103680     R-A1     2304     R-B      1152     R-C      2304
  R-D       576     R-E       560     R-F         8     R-G         4
  R-H         4     TOTAL 110592

(x2) combinations that WRITE                             4   all via R-H
     combinations that take an observation              576
     combinations that take NO observation           110016
(x3) route answers depending on an unconsulted dimension  0
(x4) EINTR route changes outside the R-E relabelling      0
(x5) reissues after a write that write again              0
```

`(x4)` is the specific check that `EINTR` is **not a route**: varying it across
its three values changes no route, and `retried through the deadline` only
relabels the one observation's result to `ERROR`, which `R-E`'s `ERROR` sub-row
already covers. That is the exact overlap the Y line demonstrated between `P-9`
and `P-10`, and it no longer exists because there is no second table.

`(x5)` takes the post-state of the writing route as the pre-state of a fresh
evaluation and enumerates every reissue over the remaining dimensions: **no
sequence of evaluations produces two writes for one handle.**

**Nothing in this section touched a process, a pid, a descriptor, a signal, a
clock or `/proc`.** The dimensions are invented tuples in a session scratchpad.

---

## §6. The handoff's current-path / digest authority table

Handoff v6 carries exactly this table, and states that any sentence directing the
implementer outside it is itself a defect.

```text
ROLE                    PATH                                                     DIGEST
governing, behaviour    successor/…WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12_DRAFT.md
                                                                                 e156d662…f4a8
governing, behaviour    successor/…P1_OPERATIVE_COMPOSITE_V1_15.md               a41c1424…113a
transform authority     successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V6_DRAFT.md
                                                                                 c9db32bb…2ff2
the scope contract      successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V6_DRAFT.md
```

**ONE PRECEDENCE RULE, OVER CURRENT FILES ONLY:** handoff v6 yields to binding
v6; binding v6 yields to the v1.12 / v1.15 pair, and both drafts are then the
defect. There is no second precedence rule in the document.

**MECHANICAL SWEEP OF THE HANDOFF.** Every occurrence of a v1.11, v1.13, v1.14,
v2.14, v4 or v5 name in handoff v6 was inspected: **all of them are inside an
explicitly labelled history sentence or a named counterexample** — `Y14-M2`'s
delegation, `Y14-M3`'s contradiction, the two author-found stale constants, the
`MS-2` supersession rows, and the "M2 rows this generation" list, which is now
read off `MS-2`'s last four literal rows. **Zero operational delegations
survive.**

**THE D / T / PR TRIPLE, CHECKED MECHANICALLY:**

```text
handoff D-6   "63, 69, 73, 77, 81, 85 or 89 FAILS"           present
handoff T-14  "63, 69, 73, 77, 81, 85 and 89 FAIL"           present
binding PR-4  "63, 69, 73, 77, 81, 85 or 89 members FAILS"   present
the current value 93 in any of the three negative lists      ABSENT
93 required to PASS at D-6 and T-14                          present
```

The list is exactly the seven **retired** member cardinalities. **No look-ahead
value appears anywhere**, and `PR-3` now names the next generation's rows without
naming its cardinality, because naming it is what produced `Y14-M3`.

---

## §7. Measured recount, region witnesses and the complete transform

### §7.1 The generation recount, from the literal lists of the produced bytes

```text
MS-2                   79 rows,  79 distinct paths,  79 distinct digests
MS-3                    7 rows,   7 distinct paths
MS-2 ∩ MS-3            empty
provenance region      87 rows,  87 distinct paths
provenance relation    MS-2 ∪ MS-3 ∪ the one non-enforced verifier baseline
                       — checked as a set equality, not asserted
recorded M2+M3 digests 86; all 86 recomputed from the files on disk; 0 mismatches
MS-8                   2 + 79 + 7 + 1 + 1 + 2 + 1 = 93
MOVEMENT               MS-2 75→79, MS-8 89→93, provenance 83→87, digests 82→86
```

### §7.2 The exhaustive stale-literal sweep

**Retired cardinals** `57, 67, 71, 74, 75, 77, 78, 79, 81, 85, 89` swept across
both governing files, the binding and the handoff. Every survivor is classified
as one of: an `MS-11` module-closure row index; a test-matrix row number; an
invariant number; the constant `67_108_864`; a current and correct accounting
value; the provenance region's own narrative of the move; or an explicit
historical citation of what version 1.13 wrongly wrote. **No stale live
accounting literal survives.** `79` and `89` are each simultaneously live and
retired in different roles and were classified occurrence by occurrence rather
than by value.

**Retired digests** swept across all four documents:

```text
11c8963a v1.14 H_FILE          composite ×2, amendment ×2, binding ×1   all MS-2 rows or labelled history
5f2c74ff v1.11 H_FILE          composite ×2, amendment ×2, binding ×1   same
15e11f0e v1.13 H_FILE          composite ×2, amendment ×1               MS-2 rows
2999e212 v1.10 H_FILE          composite ×2, amendment ×2               MS-2 rows / supersession chain
7c5cabe2 v1.13 H_HANDOFF       binding ×2                               the named X-1 defect
7d5cd453 v1.14 H_HANDOFF       binding ×2                               the X-1 measurement
9904ff3b / 731b4d66 / 313160d7 / ba513ff0 v2.14 transform figures
                               binding ×1 each where cited as retired; handoff ×1 each
                               as the named author-found stale constants
afbdb075 / f5700246 / 3bbd378d v2.13 figures   handoff ×1 each, same
dca85c8d v2.14 S1 replacement  binding ×1                               labelled as v5's value
630aa89a / d638ba7d v2.14 S10  zero occurrences anywhere
UNCLASSIFIED SURVIVORS: 0
```

**Retired anchor tokens** `P1_WATCHDOG_V2_8_…` through `P1_WATCHDOG_V2_14_…`:
**zero occurrences in either governing file.** The current token
`P1_WATCHDOG_V2_15_PRE_SELECTION_COMPOSITE_SHA256` occurs **six** times in the
amendment and **once** in the composite, and exactly **one** line of the
amendment and **zero** lines of the composite match `A16(d)`'s grammar. The one
anchor line carries `a41c1424…113a`, which is the composite's recomputed
`H_FILE`.

### §7.3 The two region witnesses, measured

Extracted independently from each governing file by its own two delimiter lines,
each delimiter of cardinality exactly one per file, **after every other v2.15
change**:

```text
HANDOFF   composite lines 8529..8592   amendment lines 1333..1396
          4168 bytes  29a6d7e319335c6f4232d5936e24fae8b6830b83c4313bf1d882e060648e7bb4
          BYTE-IDENTICAL
JOINT     composite lines 5157..8297   amendment lines 1449..4589
          225448 bytes dcf1473d07638a8a103769bc85238d83bfa2575bf75bf49d626ab725726fde24
          BYTE-IDENTICAL
```

**The substitution order is itself fail-closed.** Both `H_HANDOFF` loci lie
OUTSIDE the region they describe, the regions were re-extracted after the
substitution and compared again with zero difference, and the composite's
whole-file digest was fixed before the amendment's `§A0.4` anchor was written.
Neither the `7c5cabe2…` literal nor v2.14's measured `7d5cd453…` is carried as
authority anywhere.

### §7.4 The complete transform, independently reproduced

Every replacement block was lifted **from binding v6's own fenced blocks** and
re-hashed; every span was located by binding v6's own sentinels under its own
cardinality rule; non-overlap was verified as part of the algorithm.

```text
SPAN  LINES        SRCLEN  SOURCE SHA-256                       REPLEN  REPLACEMENT SHA-256
S1    55..95         2184  db66c3ad…71e8  UNCHANGED SOURCE        2120  75dc9671…f0d7  MOVED
S2    307..308        163  86d71bcd…2230  UNCHANGED SOURCE          61  fc9dd4e6…6901
S3    1769..1776      598  2c32d95b…1faf3 UNCHANGED SOURCE         207  839ca35d…723c
S4    1779..1783      298  56387570…410e  UNCHANGED SOURCE          22  7fdc2f4f…d878c
S5    2267..2270      299  31a3d866…e1c3  UNCHANGED SOURCE          47  e60732e9…b0fa
S6    2292..2294      218  fb396762…9292  UNCHANGED SOURCE          61  78ea5f79…c801d
S7    4415            982  a33c284e…fed1  UNCHANGED SOURCE         727  bc68506c…cd6b
S8    4698..4715     1329  dbbf9cbf…aa39  UNCHANGED SOURCE         440  bce8b980…0650
S9    8663            504  496d4747…849c  UNCHANGED SOURCE         271  55a62571…315b
S10   8691          20238  c11802cb…d46a  MOVED                  20148  ffaa8ca5…3052  MOVED
S11   8702            449  75ed6f6f…d47e2 UNCHANGED SOURCE         315  37b63dcd…a539

SENTINEL CARDINALITY        1 / 1 for every whole-line sentinel and every prefix
SPAN ORDER, ascending b_i   S1..S11 in name order; e_i < b_(i+1) for all ten pairs
DELETE-LITERAL CARDINALITY  1 occurrence in its uniquely identified line, S7/S9/S10/S11
TRAILING-SPACE DISCIPLINE   no line of any fenced replacement ends in 0x20 or 0x09
S1 NON-ASCII CENSUS         U+2014 ×2 and U+00A7 ×5, and no other; 37 lines, 2120 bytes
S1 REPLACEMENT REPRODUCES   from binding v6's own fence, at 2120 bytes and 75dc9671…

INPUT                       668002 bytes  a41c1424…113a
SOURCE TOTAL  27262         REPLACEMENT TOTAL  24419
FULL RESOLVED OUTPUT        665159 bytes  e9577809cf41cc7b97a9f22a1f2929af225e0b31bf061ae46b7aafda71bc34be
ARITHMETIC                  668002 − 27262 + 24419 = 665159   OK

H_BODY                      b1edf36c36a22c6398176e223b9453e4319fe36e1b5f9d4f760d70502d4fa8d6
H_GUARDDATA                 faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
                            BYTE-UNCHANGED — the 1816-byte region was compared
                            DIRECTLY against composite v1.15's own extracted
                            region, not inferred from the digest match
H_NORMATIVE                 d3bc574d9c0d7a3dde53af21073d8efe8c24f1fac4f180d546eeca1d94e3f1b4

BOTH DELIMITED REGIONS, extracted from composite v1.15, from amendment v1.12 and
from the resolved output and compared all three ways: ZERO DIFFERENCE.
  handoff 4168 bytes 29a6d7e3…7bb4     joint 225448 bytes dcf1473d…de24
No span intersects either. The highest body span before the joint block ends at
line 4715 and the next begins at line 8663, straddling it without entering.

MP-1, built from its published anchor, payload, order and newline rules
  anchor cardinality in the resolved output   1
  PAYLOAD LENGTH   195   SHA-256 ee8a830d46f709ff2ffd95238600437e885c32d84bf268a1658950cd5ed63d2f
  FULL LENGTH   665354 = 665159 + 195
  FULL SHA-256  6cbd6e2d2bea49854d63ae2108e1187fe8a210f6dc84526f8273db9a2bd8c09b
  D1 matches 0, D2 matches 0, markers outside GUARDDATA 0 and 0,
  H_GUARDDATA unchanged, no SOCK_SEQPACKET / t-wd-freeze.v1 / [W-A] / [W-B] in
  the payload  ->  PO-1, PO-2, PO-3 and D3 PASS
  PO-0 ***FAILS***, because 6cbd6e2d… is not e9577809…
  THE FIXTURE THEREFORE DEMONSTRATES EXACTLY THE §2.6.0 BOUNDARY IT CLAIMS AND
  NO MORE.

CENSUS ON THE RESOLVED OUTPUT
  t-wd-freeze.v1   pre 9 at lines 66, 1773, 1779, 2268, 2293, 4415, 4712, 8663,
                   8691 — every one inside a pinned span — post 0
  W-A option token           post 3   (class R, not F)
  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1  post 2   (R-2 + one historical mention)
  W-B option token           post 3        P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1  post 2
  "[W-A]" / "[W-B]" outside GUARDDATA      post 0 each
  "[W-A]" / "[W-B]" inside  GUARDDATA      post 1 each
  "the v1.12 amendment is installed"       pre 1, post 1, inside the joint block
  MARKER CENSUS ON v1.15: 20 marker-bearing lines = 3 preamble + 16 body + 1
  guarddata; 13 "[W-A]" and 13 "[W-B]"; 6 both-marker lines whole file, 4 in body.

NO RESOLVED BYTES AND NO MP-1 CANDIDATE WERE WRITTEN TO ANY PATH, INCLUDING A
TEMPORARY ONE. Both existed in memory in a session scratchpad and were
discarded. OR-4 WAS NOT EXECUTED.
```

---

## §8. What v2.14 repaired, confirmed intact

Each of the following was diffed **as a whole section** between composite v1.14
and composite v1.15:

```text
§P1-3.4 primitive binding, including _getsid and _getpgid   BYTE-UNCHANGED   5771 bytes
§P1-3.5 the four identity tests for both names              BYTE-UNCHANGED   2278 bytes
§P1-3.6 no rebinding and no indirection                     BYTE-UNCHANGED    657 bytes
§P1-7.5 the bootstrap sequence, c10 / c14 / m3              BYTE-UNCHANGED   5427 bytes
§P1-10.3 the one canonical parser, L0..L5, V0..V39          BYTE-UNCHANGED  16788 bytes
§P1-14.6 the code rules, S-3 / S-5 / S-6 / S-7 / S-12       BYTE-UNCHANGED   5766 bytes
§P1-17 guard pattern data                                   BYTE-UNCHANGED   1889 bytes
KG-1, the group observation                                 BYTE-UNCHANGED   2415 bytes
SC-9 P1 and P2                                              BYTE-UNCHANGED   2295 bytes
SC-9 P5                                                     BYTE-UNCHANGED    441 bytes
KV-1..KV-6 and SC-1..SC-8   ONE LINE CHANGED, and it is a locator only:
  "built by SC-9 P3 at the start of PHASE 3" -> "built by SC-9 P3 STEP 3A at the
  start of PHASE 3". No predicate, token, outcome or ordering moves.
```

`MP-1`'s payload, its anchor rule, its order rule and its newline convention are
unchanged; only the length and digest move, because the output moved. The
`MS-11.1` eighty-nine-row `reachable_closure`, its canonical length `20534` and
its digest `aa974e0c…c20ee` are unchanged, as is `MS-13`. **v1.15 binds no new
primitive name and removes none.**

---

## §9. Boundaries confirmed unchanged

```text
IDENTITY OPTION A            SIGNED and not reopened. attested_pid and
                             attested_pgid occur ZERO times in composite v1.15
                             and ZERO times in amendment v1.12.
BOUNDED WEAKENING            P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
                             remains NOT ACCEPTED and is not made signable.
XS-1                         COMBINED IDENTITY BINDING remains BLOCKED. This
                             round is not the later combined binding.
W-B                          SIGNED, not reopened, not re-argued. The W-A option
                             token and its paired amendment token remain in
                             TS-1's CLOSED VALIDATION VOCABULARY and in the
                             CK-14 fixture; OR-4 deletes no TS-1 literal.
SCIENCE                      No mechanism, evidence class, treatment, covariate,
                             endpoint, qualification input, comparison input, Q
                             fact, C fact or scientific constant moves. Nothing
                             is predicted.
OR STATE                     OR-2 COMPLETE. OR-3..OR-11 NOT AUTHORIZED. OR-4 was
                             not executed and no resolved bytes exist at any path.
ACTIVATION                   T = NOT_ACTIVATED. PROGRAMME CLAIM = OPEN.
                             INACTIVE-SCAFFOLD, RUNTIME-IMPLEMENTATION and
                             ONE-SHOT ATOMIC-HANDOFF AUTHORIZATIONS: NOT GRANTED.
NEGATIVE SPACE               No key, entropy, seed, Stage A, Stage B, signature,
                             manifest, attestation, member list or install record
                             was created, requested or made creatable. No
                             process, socket, pipe, fork, exec, signal, wait,
                             prctl or /proc operation occurred. No freeze was
                             executed, requested, journalled or witnessed.
FILES                        No existing file was modified. The unrelated dirty
                             and untracked working-tree work — accounting.py and
                             its test, generic_harness.py and its test, the
                             reviews/ prompt files and essay/OUTLINE.md — was not
                             read for authority, not edited, not staged and not
                             reverted. Nothing was committed.
```

---

## §10. The two bounded executable confirmation questions

Exactly one for each line. Both are executable against the pinned bytes. Neither
opens a design question, and neither asks for an opinion about scope.

**FOR THE X LINE (Fable).**

> Re-implement `KG-2` `P-2`'s machine `W0`..`W8` and, **separately and without
> reference to it**, `P-9`'s nine row predicates exactly as written, and drive
> both over the full twelve-dimension cross-product `P-10` publishes. Report
> whether the number of combinations to which no row applies and the number to
> which two or more apply are both zero over all 110592, whether the two
> implementations ever disagree, and whether any combination reaches a write
> other than through `R-H` — including every combination in which `role` is
> `WATCHDOG`, in which the prior-write boolean is true, and in which the field is
> non-`NULL` at `L`.

**FOR THE Y LINE (Sol).**

> Recompute, from the produced bytes alone: the `HANDOFF` and `JOINT` regions
> extracted independently from composite v1.15 and amendment v1.12 by their own
> delimiter lines, with their lengths and digests and their byte identity; the
> `MS-2`, `MS-3`, provenance-region and recorded-digest counts and the `MS-8`
> sum; and the complete `OR-4` transform of binding v6 §2.2 through §2.6.5,
> including the eleven span source and replacement digests, the full resolved
> output and `MP-1`. Report whether every published figure reproduces, and
> whether any retired member cardinality, retired digest, retired anchor token or
> superseded-generation delegation survives as a live operational literal in
> composite v1.15, amendment v1.12, binding v6 or handoff v6.

---

## §11. Exact next boundary

Only after **both** independent reviewers confirm **identical v2.15 bytes** may
Kirill consider

```text
I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12
```

**It is not signable from this author round.** The `V1_11` token is retired and
must not be signed, together with the already retired `V1_10`, `V1_9`, `V1_8` and
`V1_7` tokens.

Even acceptance authorizes **no** code, scaffold, key, entropy draw, `OR` step of
any number, install, activation, manifest or verifier edit, selection,
authorization or attestation artifact, detached signature, install record, or
resolved amendment or composite bytes at any path.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
READY_FOR_OFFICINA_P1_WB_V2_15_FINAL_XY_CONFIRMATION
```
