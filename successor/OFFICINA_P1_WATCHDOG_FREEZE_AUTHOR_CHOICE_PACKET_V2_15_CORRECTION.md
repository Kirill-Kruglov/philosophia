# Officina P1 watchdog-freeze mechanism — author choice packet v2.15 (correction)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. Every author closure, including this
packet's companion closure, is an untrusted self-assessment.

**THIS PACKET OPENS NO AUTHOR CHOICE AND CLOSES NONE.** The watchdog-freeze
mechanism cell is **already signed**. Kirill selected

```text
I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
```

on 2026-08-05, at
`successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md`
(`ffcb4116a9171d873be773138cc2c97547f8ff919a1d71f4cbd46e328eb3a7dc`). **That
selection is not reopened, not re-run, not re-recommended and not re-argued
anywhere in this packet.** There is no option table here, no recommendation, no
comparison and no new cell.

This packet exists for one reason: the v2.15 generation is a **replacement
governing generation**, and every governing generation of this chain carries an
author-facing packet recording what its two governing files say, at what
digests, with what accounting. It is the pre-selection anchor target named by
`TS-1`'s `governing_pre_selection.packet` and the hash-read target of `TS-2B`
`A16(b)`, and nothing else.

`T` is `NOT_ACTIVATED`; the programme claim is `OPEN`.

---

## §0. Scope — a bounded governing repair after a four-finding X/Y round

### §0.1 What licensed this round

Both independent lines reviewed the v1.11/v1.14 governing pair. **Their
verdicts differed and their findings did not conflict.**

```text
685bc98fa0912f78a57be2667881ee3679e9d85542d1e10839d31625049f6bea  reviews/fable_officina_p1_wb_v2_14_final_x_review.md
    OFFICINA_P1_WB_V2_14_X_CONFIRMED_FOR_AUTHOR_ACCEPTANCE
    ONE Major-class defect of record, X-1, which that review declined to treat
    as a REVISE trigger under its own stated gate while stating it plainly and
    recommending its repair before any OR step; plus three Minors X-L7, X-L8
    and X-L9

5ad7130119ff952a2ef0939451271146c98dd52948db8156eaeb47208cfaad49  reviews/sol_officina_p1_wb_v2_14_final_y_review.md
    REVISE_OFFICINA_P1_WB_V2_14
    THREE executable Majors Y14-M1..Y14-M3, plus Y14-L1
```

**ALL FOUR MAJOR-CLASS FINDINGS GOVERN, AND THE REASON IS NOT SENIORITY.** Each
reproduces directly from the governing bytes, which is the only test this chain
has ever applied. An X-line confirmation does not neutralize a Y-line
counterexample against the same bytes — **and this chain has said so in every
generation.** The converse is now stated with equal force and acted on: **a
Y-line silence does not neutralize an X-line Major against those same bytes.**
`X-1` is repaired here whether or not it was a `REVISE` trigger, because the
pair's own clause calls any difference a defect in this indivisible pair.

```text
Y14-M1  KG-2 STILL PERMITTED A SECOND WRITE AND P-9/P-10 WERE NOT A PARTITION.
        The four-conjunct "if and only if" carried no already-written test and
        no recheck before the write, so a reissue after a successful write and a
        mid-attempt generation invalidation each had TWO answers; and the two
        tables placed EINTR and deadline exhaustion in both at once.
Y14-M2  THE PINNED v5 HANDOFF DELEGATED AUTHORITY TO v4 AND TO COMPOSITE v1.13,
        AND PAIRED THE v1.13 PATH WITH THE v1.14 DIGEST.
Y14-M3  HANDOFF D-6 REQUIRED THE VALID 89-MEMBER ENUMERATION TO FAIL, against
        its own mandatory total and against binding PR-4 and T-14.
Y14-L1  THE NON-NORMATIVE PROVENANCE NARRATIVE NAMED THE WRONG REVIEW
        GENERATION — v2.12 where the literal rows and MS-2 named v2.13.
X-1     THE PINNED H_HANDOFF IN BOTH GOVERNING FILES WAS THE STALE v1.13 VALUE
        AND WAS FALSE AGAINST THE v1.14 BYTES. The byte-identity conjunct held
        and was verified three ways; the digest conjunct did not.
X-L7    PHASE 3 CARRIES THREE-OR-MORE TERMINAL-BEARING PREDICATES AND SC-10 SAID
        IT CARRIED ONE; one of them named no terminal at all.
X-L8    A WATCHDOG HANDLE WITH A WRITTEN GROUP SELF-COLLIDES AT PHASE 3 AND
        PERMANENTLY DISABLES THE CLASSIFIER.
X-L9    THE PERMUTATION-INVARIANCE JUSTIFICATION OVERCLAIMED ABOUT THE RECORDED
        SITE: least TABLE INDEX is positional and is not stable.
```

**EVERY ONE OF THE EIGHT IS DISPOSITIONED, NOT DROPPED.** They are repaired as
`R1`..`R4`; `Y14-L1` lands in the composite provenance narrative; the three
Minors land in the governing bytes; and `R5` regenerates every dependent byte
surface.

### §0.2 What this round is, and what it is not

```text
IT IS  a bounded governing repair of R1..R4 plus the mechanically dependent
       bytes, in the two governing files, plus a regenerated post-selection
       binding and inert-scaffold handoff, plus this packet and one author
       closure. SIX AUTHORED DELIVERABLES.
IT IS NOT  a design round, a reopening of any signed choice, an acceptance, an
       X/Y verdict, an implementation, an OR step, an install or an activation.
       No author cell is opened and none is closed. No mechanism, evidence
       class, treatment, covariate, endpoint or scientific constant moves.
       W-B REMAINS SIGNED AND IS NOT REOPENED. OR-2 ALONE IS COMPLETE.
       NO SCIENCE IS PREDICTED AND THE PROGRAMME CLAIM DOES NOT MOVE.
```

---

## §1. The v2.15 governing pair

### §1.1 Paths and digests

```text
e156d66293a608c9090994ae1016c1055a1c9071b71ea0384c58e7ab2595f4a8  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12_DRAFT.md
a41c142465c3ab0e3dfc565b6f2c1767f1b43481c28933544d72777d6e76113a  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_15.md
```

Byte lengths: amendment **314994**, composite **668002**.

Composite region digests:

```text
H_BODY       fdd6386b53c0ea4918ff66d49aa23c2b911e2ad72fc0481f7effed5b03f940f5   630161 bytes
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426     1816 bytes
H_NORMATIVE  0fd3d8b396a7de754f1b7df7159777e76702800b91f57b9cfbe7e17caea16c9d
H_FILE       a41c142465c3ab0e3dfc565b6f2c1767f1b43481c28933544d72777d6e76113a
```

`H_GUARDDATA` is **byte-unchanged from v1.13 and v1.14**. No guard pattern was
added, removed or edited by this round.

### §1.2 The two delimited byte-identical regions

**EXTRACTED INDEPENDENTLY FROM EACH GOVERNING FILE, BY ITS OWN TWO DELIMITER
LINES, AFTER EVERY OTHER v2.15 CHANGE, AND DIFFED WITH ZERO DIFFERENCE.**
Lengths are actual UTF-8 byte counts.

```text
H_HANDOFF  29a6d7e319335c6f4232d5936e24fae8b6830b83c4313bf1d882e060648e7bb4    4168 bytes
           composite lines 8529..8592     amendment lines 1333..1396
H_JOINT    dcf1473d07638a8a103769bc85238d83bfa2575bf75bf49d626ab725726fde24  225448 bytes
           composite lines 5157..8297     amendment lines 1449..4589
```

**BOTH REGIONS MOVED IN THIS GENERATION.** The joint block carries the whole
`MS`/`CK`/`IR`/`TS`/`OR`/`N` accounting surface, so the recount lands inside it;
the handoff preamble carries `H-1`, whose replacement sentence names the
superseded generation. Each was rebuilt once and copied into both files, so
their byte identity is a construction property rather than an assertion — and it
is verified independently on the produced bytes regardless.

**`H_HANDOFF` IS MEASURED, NOT CARRIED, AND THAT IS THE `X-1` REPAIR.** Composite
v1.14 and amendment v1.11 both pinned `7c5cabe2…44a7`, which is composite
v1.13's value, while their own block had moved and gained a byte and measured
`7d5cd453…0084`. Neither literal is carried forward. Both governing files now
carry the value above **and its measured length**, and both state in terms that
the value is measured on these bytes and on no predecessor's.

### §1.3 The pre-selection anchor

Exactly one line of the amendment matches `A16(d)`'s grammar:

```text
P1_WATCHDOG_V2_15_PRE_SELECTION_COMPOSITE_SHA256 = a41c142465c3ab0e3dfc565b6f2c1767f1b43481c28933544d72777d6e76113a
```

The complete token occurs **six** times in the amendment and **once** in the
composite, at `A16(d)`. The retired segments `8`, `9`, `10`, `11`, `12`, `13`
and `14` occur **zero** times in either file.

**AMENDMENT v1.11's §A0.4 SAID THE TOKEN OCCURRED SEVEN TIMES IN THAT FILE AND
ITS BYTES SAID SIX.** Neither independent line logged it; the v2.14 packet's own
§1.3 had the correct figure. The count here is derived mechanically from the
produced bytes.

---

## §2. `R1` — `KG-2` is one ordered machine and one total partition

### §2.1 What was broken

`P-2` stated the population predicate as an **if and only if** over exactly four
conjuncts — `outcome == STOPPED` and the three observation conjuncts — and
pinned a step order `K1`..`K6` containing **no already-written test** and **no
recheck between the observation and the write**. Two ordinary states were
therefore double-valued.

```text
A  A reissued AWAIT_STOP on a handle already written satisfies all four
   conjuncts. P-9 assigned THE ONE WRITE; P-3 and P-10 forbade any write.
B  A generation invalidated after the observation and before the write satisfies
   all four conjuncts. The predicate mandated the write; P-10's mid-attempt row
   said no write lands.
```

`P-9` and `P-10` were additionally **two tables over one state space**: `P-10`
placed `EINTR` during the `K4` read and deadline exhaustion inside the `STOPPED`
route while claiming the two tables were disjoint.

### §2.2 What v2.15 does

```text
THE FOUR-CONJUNCT IF AND ONLY IF, THE K1..K6 ORDER AND THE TWO-TABLE P-9/P-10
SPLIT ARE ALL WITHDRAWN.

P-2 IS AN ORDERED MACHINE W0..W8 WITH NINE MUTUALLY EXCLUSIVE AND EXHAUSTIVE
ROUTES — R-A0, R-A1, R-B, R-C, R-D, R-E, R-F, R-G, R-H — of which EXACTLY ONE is
taken per evaluation.

W0 PINS, BEFORE ANY OBSERVATION AND BEFORE ANY WRITE: (a) handle existence;
(b) generation validity; (c1) the operation's own state precondition; (c2) ROLE
ELIGIBILITY FOR POPULATION; and (d) THE PRIOR-WRITE BOOLEAN, read once from the
PCS's own table and pinned for the whole evaluation.

W3 IS THE PRIOR-WRITE BRANCH VERSION 1.14 DID NOT HAVE. On a STOPPED outcome
with the field already written, NO OBSERVATION IS TAKEN AT ALL and the response
operand is derived ONLY from the immutable recorded fact that the written value
IS h.pid, so pgid_is_leader is EXACTLY 1 on every evaluation that reaches R-D.

W4 TAKES THE ONE CANONICAL OBSERVATION, AND EINTR RETRY AND DEADLINE EXHAUSTION
LIVE INSIDE IT. A retry produces no second observation, no route and no row;
deadline exhaustion yields ERROR as the ONE observation's result. THAT REMOVES
THE P-9/P-10 OVERLAP THE Y LINE DEMONSTRATED.

W6 IS THE NAMED LINEARIZATION POINT L. It revalidates exactly two facts, in
order: (L1) the generation, and (L2) the NULL-ness of the field. R-F is
invalidation; R-G is a detected prior write, which is a SECOND WRITE under P-3
and a STRUCTURAL VIOLATION under SC-8.

R-G INVENTS NO SECOND WRITER AND ASSERTS THE EXISTENCE OF NONE. It is proved
UNREACHABLE on every conforming route from four clauses this pair already
carries: P-3's single writer and single site; §P1-8.4's one outstanding request
at a time; §P1-3.2's exclusion of threading, _thread, multiprocessing,
concurrent, asyncio, select and selectors from every file; and §P1-8.6 J1..J6.
NO LOCK, NO COMPARE-AND-SWAP, NO NEW PRIMITIVE AND NO NEW EVIDENCE CLASS IS
INTRODUCED.

R-H IS THE ONLY WRITING ROUTE AND ITS GUARD IS THE CONJUNCTION OF EVERY NAMED
CONJUNCT — not four of them.

P-9 IS THE ONE TOTAL, DISJOINT PARTITION over those routes, each row's predicate
being its own guard conjoined with the negation of every earlier guard.
P-10 IS THE EXECUTABLE CROSS-PRODUCT: twelve dimensions, 110592 combinations,
requiring EXACTLY ONE ROUTE for every combination, checked against the PUBLISHED
ROW PREDICATES rather than against any implementation's control flow.

BOTH Y14-M1 COUNTEREXAMPLES ARE WRITTEN OUT IN THE GOVERNING BYTES WITH THEIR
BEFORE AND AFTER ANSWERS, at KG-2 P-10 and at composite test row 89 clause (6B).
```

---

## §3. `R2` — the implementation handoff is current and self-consistent

### §3.1 What was broken

Handoff v5 named `OFFICINA_P1_WB_POST_SELECTION_BINDING_V4_DRAFT.md` as the
document it is read with and said that binding governs on disagreement; its
`§H1` `R-1` and `§H2.2` named composite **v1.13** as the frozen behaviour source
while pairing that path with the **v1.14** digest; and its `D-6` fixed the total
at 89 and `TS-3` `member_count` at 89 and then required an enumeration of 89 to
**FAIL**, against binding `PR-4` and its own `T-14`.

**TWO FURTHER STALE CONSTANTS WERE FOUND BY THE AUTHOR AND ENUMERATED BY NEITHER
LINE:** `§H4`'s resolved `H_BODY` and `H_NORMATIVE` carried the **v4-era**
values against binding v5's own `§2.2.6`, and `§H7.2` `T-10` carried the
**v4-era** `MP-1` digest against binding v5's `§2.6.5`.

### §3.2 What v2.15 does

```text
HANDOFF v6 CARRIES ONE CURRENT-AUTHORITY TABLE in which every path is paired
with its own recomputed digest, and ONE PRECEDENCE RULE stated over current
files only: this handoff yields to binding v6, and binding v6 yields to the
v1.12/v1.15 pair.

OLDER GENERATIONS APPEAR ONLY AS EXPLICITLY LABELLED HISTORY OR AS
COUNTEREXAMPLES, and the document says in terms that a sentence telling the
implementer to open, read, prefer or compare against anything outside the table
is itself a defect.

D-6 DERIVES THE CARDINALITY FROM THIS GENERATION — total 93, TS-3 member_count
93 — AND REQUIRES 93 TO PASS. The negative list is 63, 69, 73, 77, 81, 85 and 89,
which is exactly the seven RETIRED member cardinalities and contains no
look-ahead value, because a look-ahead value is precisely what became the
current value and produced Y14-M3. THE SAME SEVEN VALUES APPEAR AT D-6, AT T-14
AND AT BINDING v6 PR-4, and 93 appears in none of the three.

Y14-L1 IS REPAIRED IN THE COMPOSITE PROVENANCE NARRATIVE: the generation name in
that paragraph is now read off the literal rows that entered with it.
```

---

## §4. `R3` — the region witnesses are republished from current bytes

```text
AFTER ALL v2.15 CHANGES, THE HANDOFF REGION WAS EXTRACTED INDEPENDENTLY FROM THE
NEW COMPOSITE AND FROM THE NEW AMENDMENT BY ITS OWN TWO DELIMITER LINES, BYTE
IDENTITY WAS REQUIRED AND HELD, AND THE MEASURED LENGTH AND DIGEST WERE
PUBLISHED IN BOTH GOVERNING FILES AND IN EVERY DEPENDENT SURFACE.
  4168 bytes   29a6d7e319335c6f4232d5936e24fae8b6830b83c4313bf1d882e060648e7bb4
NEITHER THE 7c5cabe2… LITERAL NOR v2.14's MEASURED 7d5cd453… IS CARRIED. Both
appear in binding v6 §0.2 as the named defect and its measurement, and nowhere
as authority.

THE JOINT-REGION WITNESS IS RECOMPUTED THE SAME WAY.
  225448 bytes dcf1473d07638a8a103769bc85238d83bfa2575bf75bf49d626ab725726fde24

THE SUBSTITUTION ORDER IS ITSELF FAIL-CLOSED: both H_HANDOFF loci lie OUTSIDE
the delimited region they describe, the regions were re-extracted after the
substitution and compared again with zero difference, and the composite's
whole-file digest was fixed before the amendment's §A0.4 anchor was written, so
the custody remains acyclic (§P1-14.5).
```

---

## §5. `R4` — the three X-line boundary notes, closed rather than named

```text
X-L7  PHASE 3 CARRIES FIVE TERMINAL-BEARING PREDICATES, ENUMERATED AT SC-9 P3:
      the own-group observation raising SC-8 (T1); the same observation not
      PRESENT_VALID without raising SC-8 (T3); the SPAWNING_GROUP.json read
      raising SC-8 (T1); that record absent, unreadable or carrying a
      non-conforming process_group_id (T3) — WHICH VERSION 1.14 LEFT WITHOUT A
      NAMED TERMINAL; and KV-6(a) (T3). PHASE 3 NOW HAS THE SAME EXPLICIT SHAPE
      PHASE 4 HAS: STEP 3A collects both fallible construction sources without
      selecting a terminal, STEP 3B reduces them under the SAME
      STRUCTURAL-DOMINATES-FORBIDDEN precedence and ONE FIXED SOURCE ORDER, and
      STEP 3C's table scan is reachable only when G exists. THE REDUCTION IS
      TOTAL OVER ALL FIVE AND IS ORDER-INVARIANT. Version 1.14 would have
      answered T3 for an ABSENT own-group observation beside a structurally
      faulting record read, and T1 for its mirror; that pair is now a required
      fixture at row 89 clause (6D) and both answer T1.

X-L8  THE WATCHDOG SELF-COLLISION IS CLOSED, NOT CALLED LATENT. KG-2 P-2 W0 (c2)
      refuses POPULATION ELIGIBILITY for role WATCHDOG BEFORE any observation is
      taken, and P-4 states that a watchdog's pgid_or_null is NEVER written on
      any path, at any state, at any ownership and on any outcome. THE NORMAL
      setsid = False LIFECYCLE OF §P1-4.1 AND §P1-9.2 IS PRESERVED EXACTLY AS IT
      IS and is no longer the argument. §P1-8.3 IS NOT NARROWED: AWAIT_STOP
      remains available for a WATCHDOG handle and only the KG-2 write is
      refused. SC-9 P3's second protected-set clause is RETAINED UNCHANGED and
      is now PROVABLY VACUOUS, which is exactly why the collision cannot arise.
      NO CONFORMING ROUTE CAN POPULATE THE FIELD.

X-L9  THE TIE-BREAK IS REPLACED RATHER THAN THE CLAIM NARROWED. STEP 4A now
      collects the entry's handle_id — the decimal key of §P1-8.5's signed
      handle model, carried by the entry, never reused within or across
      generations — instead of its table index, and every tie-break at PHASE 3,
      PHASE 4, PHASE 6 and SC-10 is LEAST handle_id. NO INPUT OF ANY REDUCTION
      IS POSITIONAL, so the invariance extends to the RECORDED SITE and not only
      to the terminal tuple. NO SCIENTIFIC IDENTITY IS ADDED AND NO NEW FIELD IS
      INTRODUCED. The three-entry all-PRIMITIVE_FAULT fixture in all six
      permutations is required at row 89 clause (6A).
```

---

## §6. `R5` — the measured recount and the complete new transform

### §6.1 The four new `M2` rows, in `MS-2` order

```text
5f2c74ff371f618039de705f21464454684da122f91e06c251e147bfc61d26be  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11_DRAFT.md
11c8963ac3cbd4c72a90b0a1f0fdc0fe3bfb35be84a974c3a2a953ec699bbdee  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_14.md
685bc98fa0912f78a57be2667881ee3679e9d85542d1e10839d31625049f6bea  reviews/fable_officina_p1_wb_v2_14_final_x_review.md
5ad7130119ff952a2ef0939451271146c98dd52948db8156eaeb47208cfaad49  reviews/sol_officina_p1_wb_v2_14_final_y_review.md
```

**BOTH v2.14 REVIEWS ENTER, INCLUDING THE CONFIRMING ONE.** What makes a review
an `M2` row is that the generation it reviewed is no longer live, not the verdict
it returned.

### §6.2 The measured atomic update

```text
MS-2                              75 -> 79
MS-3                               7      7   unchanged
MS-8 / TS-3 member_count          89 -> 93
composite provenance region       83 -> 87
recorded M2+M3 digests            82 -> 86
member classes                     7      7   only M2 grew
M1 2 + M2 79 + M3 7 + M4 1 + M5 1 + M6 2 + M7 1 = 93
```

Recounted from the **produced** bytes rather than from any predecessor: `MS-2`
carries **79 rows with 79 distinct paths and 79 distinct digests**, `MS-3`
carries **7 with 7 distinct**, their intersection is **empty**, and the
provenance region carries **87 rows with 87 distinct paths**, being exactly
`MS-2` ∪ `MS-3` ∪ the one non-enforced verifier baseline. **All 86 recorded `M2`
and `M3` digests were recomputed from the files on disk and all 86 match.**

### §6.3 The stale-cardinal sweep

Every retired cardinal — `57`, `67`, `71`, `74`, `75`, `77`, `78`, `79`, `81`,
`85` and `89` — was swept over both governing files, the binding and the handoff,
and **every surviving occurrence is classified**: an `MS-11` module-closure row
index, a test-matrix row number, an invariant number, the numeric constant
`67_108_864`, a current and correct accounting value, the non-normative
provenance region's own narrative of the move, or an explicit historical
citation. **`79` AND `89` ARE NOW EACH BOTH LIVE AND RETIRED IN DIFFERENT
ROLES** — `79` is `MS-2`'s current cardinality and the retired provenance count;
`89` is the retired member count and the current `MS-11` closure row count — so
each occurrence is classified individually rather than by value.

### §6.4 Further stale literals, author-found, reported by neither line

```text
AMENDMENT v1.11 DA-4 named "this amendment (v1.10)" and "P1 operative composite
v1.13" as THE TWO LIVE SPECIFICATION SURFACES while the file itself was v1.11
and its pair was v1.14. That is an operational delegation to a superseded
surface inside a NORMATIVE clause — the same class as Y14-M2.
AMENDMENT v1.11 §A9's preamble named composite v1.13 throughout, and its
five-locus audit note headed a v1.10-generation list with the v1.11-generation
anchor token, so the paragraph described no actual generation.
AMENDMENT v1.11 §A0.4 said the anchor token occurred SEVEN times in that file;
the bytes said SIX.
AMENDMENT v1.11 §A11 N-14 and N-16 carried MS-2 71, MS-8 85 and a provenance
region of 79 against an enforced 75, 89 and 83.
HANDOFF v5 §H4 carried the v4-era resolved H_BODY and H_NORMATIVE and §H7.2
T-10 carried the v4-era MP-1 digest, against binding v5's own §2.2.6 and §2.6.5.
ALL SIX ARE REPAIRED IN THESE BYTES AND ALL SIX ARE DECLARED HERE RATHER THAN
LEFT TO BE DISCOVERED.
```

### §6.5 The complete new `OR-4` transform

Because `R1`..`R4` change governing bytes, **v2.14's eleven spans and its
full-output hash are RETIRED**. Post-selection binding v6 publishes a complete
new transform rather than a delta on an invisible intermediate.

```text
INPUT                  668002 bytes
                       a41c142465c3ab0e3dfc565b6f2c1767f1b43481c28933544d72777d6e76113a
ELEVEN SPANS           source total 27262, replacement total 24419
FULL RESOLVED OUTPUT   665159 bytes
                       e9577809cf41cc7b97a9f22a1f2929af225e0b31bf061ae46b7aafda71bc34be
resolved H_BODY        b1edf36c36a22c6398176e223b9453e4319fe36e1b5f9d4f760d70502d4fa8d6
resolved H_GUARDDATA   faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426  UNCHANGED
resolved H_NORMATIVE   d3bc574d9c0d7a3dde53af21073d8efe8c24f1fac4f180d546eeca1d94e3f1b4
ARITHMETIC             668002 − 27262 + 24419 = 665159
```

**TEN of the eleven spans carry byte-identical SOURCE content at NEW line
numbers; one does not** — `S10`, because test row 89 gains `R1`'s `KG-2` machine
fixtures, `R4`'s Phase-3 and permutation-stable-site fixtures and the
cross-product obligation, growing from 14213 to 20238 bytes. **ONE REPLACEMENT
MOVED, BY EXACTLY ONE LINE** — `S1`'s, because the Cell-2 notice names the
generation it replaces. The full-output length and digest change for all eleven.

Both delimited regions survive `OR-4` byte-identically and were extracted from
composite v1.15, from amendment v1.12 and from the resolved output and compared
with zero difference, all three ways. Guarddata is byte-unchanged and was
compared directly against the extracted 1816-byte region rather than inferred
from a digest match.

`D1` and `D2` remain defence in depth and **their claim remains narrowed to
exact listed literal coverage**; the claim that finite literals detect arbitrary
semantic paraphrases stays **withdrawn**. Fixture `MP-1` is byte-exact: its
payload is unchanged at **195 bytes**, digest
`ee8a830d46f709ff2ffd95238600437e885c32d84bf268a1658950cd5ed63d2f`, and its
recomputed full length (`665354 = 665159 + 195`) and digest
(`6cbd6e2d…c09b`) are published. It yields zero `D1` and zero `D2` matches,
passes every marker check and the guard-data check, **and fails the full-output
identity check**, which is the proof of the boundary.

**No resolved bytes exist at any path.** The resolved output and the `MP-1`
candidate were constructed in memory, every figure was measured on them, and
both were then discarded. `OR-4` was not executed.

---

## §7. Exact-file accounting

```text
THIS ROUND AUTHORS EXACTLY SIX DELIVERABLES:
  1  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_15_CORRECTION.md
  2  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12_DRAFT.md
  3  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_15.md
  4  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V6_DRAFT.md
  5  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V6_DRAFT.md
  6  reviews/opus5_officina_p1_wb_v2_15_final_repair_closure.md

A SEPARATELY ARCHIVED CHAT TRANSCRIPT IS PROVENANCE CREATED BY THE OPERATOR AND
IS NOT A SEVENTH AUTHORED DELIVERABLE. THIS ROUND DOES NOT CLAIM THAT NO SEVENTH
REPOSITORY FILE CAN LATER EXIST.
```

---

## §8. Tokens and invariants

### §8.1 There is no recommendation, because the cell is signed

`W-B` is selected. This packet recommends nothing, compares nothing and predicts
nothing.

### §8.2 The closed validation vocabulary is retained in full

`TS-1` must be able to name **either** option token and **either** paired
amendment token in order to refuse the wrong one. `OR-4` deletes W-A's operative
GRANTS and deletes **no** `TS-1` literal.

### §8.3 Tokens

```text
SIGNED, NOT REOPENED
  I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
  I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY

RETIRED, MUST NOT BE SIGNED
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_10
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7

THE ONE FUTURE ACCEPTANCE TOKEN, NOT SIGNABLE YET AND NOT SIGNABLE FROM THIS
AUTHORSHIP ROUND
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12
  It becomes signable only after a bounded independent X-line and Y-line round
  on the v2.15 bytes IN WHICH BOTH LINES CONFIRM THE SAME BYTES, and only
  jointly with composite v1.15 under §A9's single atomic handoff. EVEN THEN IT
  AUTHORIZES NO CODE, NO TEST, NO KEY, NO OR-3, NO OR-4, NO INSTALL AND NO
  ACTIVATION.

NOT ACCEPTED, AND NOT MADE SIGNABLE HERE
  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
```

---

## §9. Independence

The next act is a bounded independent X-line and Y-line review of the **same new
bytes**, performed by reviewers that did not author this round. Neither line's
verdict is predicted here. **This round exists because four Major-class findings
were returned against the previous pair by two independent lines, and every one
of them reproduces from the bytes.** An X-line confirmation does not neutralize
a Y-line counterexample against the same bytes, and the reverse holds equally.

---

## §10. Negative space

This packet creates nothing executable and authorizes no selection, X/Y verdict,
acceptance, implementation, commit, verifier or manifest edit, key, entropy,
seed, Stage A, Stage B, detached signature, attestation, member list, install
record, `OR` step, process, socket, pipe, fork, exec, signal, wait or `prctl`
operation, capability, world, learner, candidate, trajectory, capacity artifact,
custody disposition, result manifest, spend, datum, outcome, Proof or claim
movement.

**No `_getsid`, `_getpgid`, `_getpid` or `PGRP_OBSERVE` call was made, and
binding a name in a specification is not permission to run it.** No freeze was
executed, requested, journalled or witnessed. No `/proc` was read against any
live process. No `AWAIT_STOP` was evaluated and no handle table exists. No clock
was sampled for any contract purpose. No Philosophia production or project
module was imported, executed or compiled. **The `KG-2` cross-product of §2.2 was
enumerated over invented tuples in a session scratchpad and touched no process,
pid, descriptor or signal.** No existing file was modified: no historical or
governing document, no code, no test, no signature, no runtime artifact, no
prior review and none of the unrelated dirty or untracked working-tree work.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
XS-1 COMBINED IDENTITY BINDING = BLOCKED
WATCHDOG AUTHORITY AMENDMENT V1.12 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

The exact selected token and the formal selection signature govern. This packet
and every author closure are untrusted self-assessments and are normative for
nothing.
