# Officina P1 W-B post-selection binding v3 (draft)

**Author:** Claude Code Opus 5, **post-selection binding author only**. Not an
independent X-line or Y-line reviewer. **This draft selects nothing, accepts
nothing, installs nothing and executes nothing.**

This document is a **plan and contract for a transformation, not the
transformation itself.** It creates no resolved amendment, no resolved
composite, no key, no Stage A, no Stage B, no manifest, no attestation, no
signature and no install record. `T` is `NOT_ACTIVATED`; the programme claim is
`OPEN`.

**v3 REPLACES v2 WHOLLY.** v2 was reviewed by two independent lines against the
v1.8/v1.11 governing bytes. The Y line returned `REVISE_OFFICINA_P1_WB_V2_11`
with three executable Majors, one of them — `M-3` — squarely against this
binding: the "byte-exact" Cell-2 transformation supplied no replacement bytes,
its line actions overlapped physical lines, and `PO-9`'s `D1` and `D2` supplied
no literal pattern arrays. The X line confirmed the pair but logged the same
overlap as `L-X6` and the character-count mislabel as `L-X3`. **v3 is re-issued
against the v1.9 / v1.12 governing bytes with `M-3`, `L-X3` and `L-X6`
repaired.** Every mechanical result of v2 that the X line independently
reproduced — the region split, the marker census, the both-marker line set, the
guard-data retention rule, the `PO-6` / `IR-13` row 47 reasoning, the identity
disposition and the provenance disposition — is carried forward, recomputed
against v1.12, and stated again here.

---

## §0. Position and inputs

### §0.1 What is already signed

Kirill signed, on 2026-08-05, at selection base commit `176d609`:

```text
I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
```

```text
ffcb4116a9171d873be773138cc2c97547f8ff919a1d71f4cbd46e328eb3a7dc  successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md
```

That signature completes **`OR-2` and only `OR-2`**. `OR-3` through `OR-11`
remain unauthorized. **The selection is not reopened by this document.**

### §0.2 The governing bytes this binding reads

The v2.12 generation. Every digest recomputed from disk at authoring time.

```text
a7ec78cca0c7a537c4251a5342d7bb27c63d16de307c2ee2e901d69187d98e17  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9_DRAFT.md
e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_12.md
```

Composite region digests (§P1-14.0 extraction):

```text
H_BODY       d5125d54e312fd87fff7c622cedf8538ef2ea99c9666ec619becfd2e4651a1e6
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  0d3b411e6f92c37f759025d71af6fa59d7b648a0106869829c30c1917b490d66
H_FILE       e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b
```

The two delimited byte-identical regions, extracted and diffed with zero
difference. **THE LENGTHS BELOW ARE ACTUAL UTF-8 BYTE COUNTS**, repairing the
`L-X3` character-count mislabel that v2 carried:

```text
canonical atomic-handoff preamble  a03cb516958052109a860f461e7777916b4185ff1cd1deedeb0d3d955c343a66    4166 UTF-8 bytes
joint install and authorization    6b0e64e0bd4f56c6c2b6a748808944221125ced2d482d8684c7566461584a2f7  223250 UTF-8 bytes
```

The v2.12 author choice packet, hash-read target of `TS-2B` `A16(b)` and member
of nothing:

```text
successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_12_CORRECTION.md
```

Recorded as **external author state, not as a member and not as authority
here**, exactly as `XS-1` records it:

```text
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
```

The two reviews that licensed the v2.12 round and this re-issue:

```text
3964469740fc73a6a4836b64247003c39d5261a6af9c6ddf37a0da76c13f0759  reviews/fable_officina_p1_wb_v2_11_final_x_review.md
ef4508be13d9ef395b2e8d5542d6256e2bd5719e99cbff209d13612dc5dd00c4  reviews/sol_officina_p1_wb_v2_11_final_y_review.md
```

### §0.3 What this document is not

```text
IT IS NOT the resolved amendment and NOT the resolved composite. It creates
  neither, and §2A states the exact boundary against OR-3 and OR-4.
IT IS NOT the LATER COMBINED BINDING named at XS-1(a)..(d). It does not resolve
  the process-claim identity cell, does not bind the identity signature into any
  member class, and does not re-derive any identity field. §3 states this in
  full and it is load-bearing.
IT IS NOT an amendment acceptance. The v1.9 acceptance token is unsigned.
IT IS NOT an implementation, install or activation authorization.
IT IS NOT an X-line or Y-line verdict, and it is normative for nothing. Every
  author closure is an untrusted self-assessment.
IT CONTAINS NO IDENTITY-OBSERVATION CODE AND NO IDENTITY-OBSERVATION CONTRACT.
```

---

## §1. `B1` — the one operative branch

### §1.1 The selected branch, stated once

```text
SELECTED, AND THERE IS NO OTHER:
  option token          I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
  option amendment      P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1

REJECTED, NON-SELECTED. ITS OPERATIVE GRANTS ARE DELETED AT OR-4; ITS TOKENS
REMAIN IN TS-1's CLOSED VALIDATION VOCABULARY AND ARE NOT DELETED (§2.5 PO-6):
  option token          I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
  option amendment      P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
```

The five operative consequences, each traced to its governing locus, with no
addition and no widening:

```text
S1  TOPOLOGY. The watchdog holds TWO SEALED PIPES and no socket: the update
    READ end at descriptor slot 3 and the ack WRITE end at slot 4. SLOT 6 IS
    EXPLICITLY CLOSED BY A FILE ACTION. No freeze-request socket and no
    transport-request capability of any kind.
      composite §P1-13.2 P1-invariant row, [W-B] branch
      composite §P1-15 row 99, [W-B] branch

S2  WATCHDOG ON EOF. Update-pipe EOF is the SINGLE supervisor-death detector.
    On EOF the watchdog WRITES NOTHING, FREEZES NOTHING, SIGNALS NOTHING,
    SENDS NOTHING, settles nothing, and exits.
      composite §P1-9.2 property 12, [W-B] branch
      composite §P1-10.6, [W-B] branch
      amendment §A3.5

S3  PCS AS DETECTOR AND SOLE EXECUTOR FOR THIS ROUTE. Loss of the peer control
    endpoint is detected by the PCS, which runs the §P1-10.7 freeze classifier
    RECORD-FIRST, in the PCS root, and is the sole executor of the resulting
    group stops — under KV-1..KV-6 and SC-1..SC-10, IN TWO EXPLICIT PHASES,
    now DEFINED IN FULL at §P1-10.7 of composite v1.12.
      composite §P1-10.7 TRIGGER, [W-B] branch
      composite §P1-15 row 89, [W-B] branch

S4  NO TRANSPORT FRAME EXISTS ON THIS BRANCH. No t-wd-freeze.v1 record is
    emitted, received, accepted, journalled or witnessed on any path. The W-A
    bounded service window does not exist on this branch.

S5  NO DURABLE OBJECT, NO EVIDENCE, NO SCIENTIFIC INPUT. The watchdog produces
    no durable object of any class and supplies no input to any scientific
    predicate. The classifier's journal state — its terminal, its terminal
    qualifier, its SC-5 tokens and its freeze_ns — is P1-owned process-control
    material and never reaches a peer artifact, an acceptance predicate, a
    qualification, a comparison, a Q or C fact, or any published record.
```

### §1.2 The one peer-layer operation that survives, unchanged by the choice

```text
The watchdog performs EXACTLY ONE peer-layer operation, REQUIRED under BOTH
options and therefore unchanged by this binding: the READ-ONLY verification of
the supervisor identity record of §P1-13.2 row 3, required by §P1-9.2 property 8
and invariant 87, and NEVER by any parent relationship.

A read installs nothing, decides nothing, creates no durable object, and is
invisible to every acceptance predicate and to SW-1..SW-5. IT IS NOT AN
AUTHORITY. "Role-entry only" means no write, no decision and no execution; it
does not mean no read.

THE getppid() PROHIBITION IS UNCHANGED AND IS NOT WEAKENED. Under W-B its
retained rationale is the [W-B] one: the watchdog executes no freeze on any
path, so the prohibition stands because THE INFERENCE IS FALSE.
```

### §1.3 The four common amendments, bound without changing their meaning

Each is bound **by reference to its owning governing locus**. Where this
document and an owning clause could be read to differ, **the owning clause
governs and this document is the defect.**

```text
P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1
  OWNING LOCI  amendment §A6 FB-1..FB-5; §A6.1 TO-1..TO-5
  UNCHANGED BY W-B  FB-5 — the watchdog has no path here, before or after.

P1_PCS_FREEZE_CLASSIFIER_V1
  OWNING LOCI  composite §P1-10.7 including its KG-1, KG-2, KV-1..KV-6 and
    SC-1..SC-10 sub-block; §P1-15 rows 89 and 101
  WHAT W-B FIXES  the TRIGGER, and only the trigger: loss of the peer control
    endpoint, record-first. The W-A trigger is deleted.
  RESOLVED SINCE v2  the definition is now EXECUTABLE. v1.11's KG-1 could not
    return PRESENT_VALID on an ordinary Linux stat line and its
    forbidden-target terminal could be masked by an earlier skip. v1.12 repairs
    both; the fence is lifted for the DEFINITION, not for implementation (§H10
    of the handoff still forbids writing the classifier).
  UNCHANGED  the PCS remains SOLE CALLER of fork, posix_spawn, kill, killpg and
    every wait-family primitive. Two execution SITES are not two CALLERS. S-12
    is retained.

P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1
  OWNING LOCI  composite §P1-1.3; §P1-13.2; §P1-13.9; amendment §A2, §A3.1, §A3.3
  EXPLICITLY  COMMON TO BOTH OPTIONS and NOT itself a choice. Binding W-B
    neither strengthens nor weakens it, and it does not reopen the signed
    selection that retains a dedicated watchdog PROCESS.

P1_FREEZE_PUBLICATION_L6_L9_V1
  OWNING LOCI  amendment §A8.1; §A8.2 PUB-1..PUB-4
  UNCHANGED BY W-B  the watchdog's acknowledgement duty and the ack-absence
    timeout are option-independent. W-B removes no ack and adds none.
```

### §1.4 What this binding does **not** touch

```text
NB-1  IT DOES NOT REOPEN THE OTHER FIVE SIGNED CHOICES of §P1-1.3.
NB-2  IT DOES NOT MOVE THE reachable_closure. 89 rows, CANON length 20534,
      digest aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee,
      its bootstrap subset, its seven unexecuted branches and its 267 false
      effect booleans are untouched.
NB-3  IT ADDS NO MEMBER, NO MEMBER CLASS, NO PRODUCTION ROOT, NO AUTHOR CELL,
      NO SELECTION TOKEN, NO AMENDMENT TOKEN, NO FAILURE CODE AND NO TEST ROW.
NB-4  IT DOES NOT NARROW THE killer ENUM. {WATCHDOG, SUPERVISOR} is RETAINED;
      the WATCHDOG value is unreachable BY CONSTRUCTION, so a stale or forged
      object is REJECTED at conjunct 8 rather than being unparseable.
NB-5  IT CLAIMS NO TEMPORAL, FRESHNESS, MONOTONICITY OR ROLLBACK-RESISTANCE
      PROPERTY. A0.4's honest rollback limitation and TR-2(b) stand unchanged.
NB-6  IT DOES NOT CHANGE THE v2.12 GOVERNING BYTES. Every count, digest and
      rule above is READ from them.
```

---

## §2. The complete option-resolution contract

### §2.1 The mechanical census, recomputed against composite v1.12

```text
MARKER-BEARING LINES, composite v1.12           20
MARKER-BEARING LINES, amendment v1.9             0
  the amendment contains the two marker strings ZERO times; every variant block
  lives in the composite, and OR-4 therefore edits ONE file
"[W-A]" OCCURRENCES, composite                  13
"[W-B]" OCCURRENCES, composite                  13
BOTH-MARKER LINES, WHOLE FILE                    6   83, 2959, 7179, 7207, 7218, 7317
BOTH-MARKER LINES, BODY ONLY                     4   2959, 7179, 7207, 7218
```

Region sentinels in composite v1.12:

```text
OFFICINA-P1-BODY-BEGIN          line  251
OFFICINA-P1-BODY-END            line 7277
OFFICINA-P1-GUARDDATA-BEGIN     line 7279
OFFICINA-P1-GUARDDATA-END       line 7320
OFFICINA-P1-PROVENANCE-BEGIN    line 7322
OFFICINA-P1-PROVENANCE-END      line 7527
```

```text
REGION      LINES  A   B   OBLIGATION AT OR-4
  PREAMBLE      3   2   2   outside G-10's match range. RESOLVED BY §2.2's
    (1..250)                SINGLE-SPAN CELL-2 REPLACEMENT, whose exact bytes
                            are pinned there and which covers the WHOLE Cell-2
                            notice, not only these three lines
  BODY         16  10  10   G-10's exclusive match range. RESOLVE each to the
    (252..7276)             [W-B] branch and DELETE the [W-A] branch
  GUARDDATA     1   1   1   THE PATTERN SOURCE. RETAIN BYTE-IDENTICAL. Never a
    (7280..7319)            match target; deleting it destroys G-10 and changes
                            H_GUARDDATA
  ---------------------------------------------------------------------------
  TOTAL        20  13  13
```

The four both-marker **body** lines must be **edited in place**. A line-deletion
strategy is wrong on its face.

### §2.2 `M-3` / `L-X6` REPAIR — the Cell-2 transformation as ONE canonical literal byte block

**v2's defect, stated so the repair is checkable.** v2 disposed of the Cell-2
span with a table of *semantic line actions*, and those actions **overlapped
physical lines**: line 58 carried both the blocking sentence and a common fact
to retain, line 60 carried both a common fact and "What remains open", and lines
85 and 88 likewise appeared in two rows with different actions. The contract
then supplied only the semantic properties `CT-1`..`CT-6`. **Two implementers
could satisfy every property and emit different bytes.** That contradicted the
"byte-exact" label and handoff `R-2`'s no-design-discretion rule.

**v3 replaces the whole overlapping table with ONE replacement of ONE span, and
pins the bytes.** There is no line-by-line action table, no sentence-role table,
no overlapping range and no prose choice anywhere in `OR-4`'s Cell-2 work.

#### §2.2.1 The exact source span, identified by sentinels rather than by line numbers

```text
SOURCE FILE        successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_12.md
                   H_FILE e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b

FIRST LINE OF THE SPAN — the unique line whose WHOLE content, after stripping a
trailing 0x0A and with no other leading or trailing byte, equals
  ### Cell 2 — `AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM`, new in v1.3

LAST LINE OF THE SPAN — the unique line whose WHOLE content, under the same
rule, equals
  decisions — whichever way they go — land in a document that is otherwise ready.

CARDINALITY  each of those two lines occurs EXACTLY ONCE in composite v1.12
             under whole-line equality. A count of zero, or of two or more,
             FAILS CLOSED and OR-4 does not proceed.
SPAN         the two sentinel lines AND every line between them, each including
             its 0x0A. THE SENTINELS ARE PART OF THE SPAN AND ARE REPLACED WITH
             IT. In composite v1.12 the span is lines 55..95 inclusive; THE LINE
             NUMBERS ARE INFORMATIVE AND THE SENTINELS ARE NORMATIVE, because
             line numbers move with every generation and the sentinels do not.

SPAN LENGTH  41 lines, 2184 UTF-8 bytes
SPAN SHA-256 1623dc45bb5c17c507ca590c3d6ca2a171ed7e40e5c4f287a8a736ee860db2b8
```

#### §2.2.2 The exact replacement bytes

**EXTRACTION RULE FOR THE BLOCK BELOW, STATED SO THE FENCE MARKUP IS EXCLUDED.**
The replacement bytes are the concatenation of the lines lying **strictly
between** the opening fence line and the closing fence line of the single
`REPLACEMENT-BYTES` block below, each line including its `0x0A`. The two fence
lines themselves are markup of this document and are **not** part of the bytes.
No line of the replacement is a fence line, so the closing fence is the first
subsequent line equal to three backtick characters.

```REPLACEMENT-BYTES
### Cell 2 — `AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM`, SIGNED

**The watchdog-freeze mechanism cell carries the author's signature, and this
version is not blocked by it.** The signed token is
`I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS`, signed on
2026-08-05 and recorded at
`successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md`, whose digest
is `ffcb4116a9171d873be773138cc2c97547f8ff919a1d71f4cbd46e328eb3a7dc`.

**The other option was rejected.** Its token was
`I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES` and its paired
amendment token was `P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1`. Both strings
remain in the closed validation vocabulary of §P1-14.4 `TS-1`, where a
conforming authorization must be able to name either in order to refuse the
wrong one. Neither names any capability this document grants.

The watchdog freezer/witness role is reassigned to the supervisor throughout
this version — that reassignment is common to both options and is NOT itself a
choice, and the signature neither strengthens nor weakens it.

The signed mechanism is the one this document carries, and it is stated in the
normative regions rather than here: the watchdog holds two sealed pipes and no
socket, slot 6 is explicitly closed by a file action, and the PCS runs the
freeze classifier of §P1-10.7 record-first on loss of the peer control
endpoint.

Exactly one branch of every author-cell variant block has been retained and the
other deleted, in step `OR-4` of the atomic handoff, whose `H-1`..`H-4` are
stated once in the canonical delimited block at §P1-14.8 of this file and
carried byte-identically at §A9 of the peer amendment; no author closure states
that step or any other. This file carries no variant block, `G-10` (§P1-14.4)
confirms that against `REGION(BODY)`, and a build extracted from a file that
still contained one would not be conforming.

Every other part of the interface repair is complete, and the rest of this
composite is a finished replacement for version 1.11, so that the signed
decisions land in a document that is otherwise ready.
```

```text
REPLACEMENT LENGTH   37 lines, 2120 UTF-8 bytes
REPLACEMENT SHA-256  f2782a63db003dfb370d0c0c5afb9c928a8fc61c8af29285c8a1172657a84fee
ENCODING             UTF-8, no BOM, LF line endings, final byte 0x0A
NON-ASCII CHARACTERS the block contains the U+2014 EM DASH at two loci and no
                     other non-ASCII character
```

#### §2.2.3 The deterministic splice algorithm

```text
SPLICE(composite_bytes) -> resolved_cell2_bytes
  1. L := the lines of composite_bytes, split on 0x0A, each retaining its 0x0A
     except possibly the last.
  2. b := the unique index i with L[i] minus a trailing 0x0A equal to the FIRST
     SENTINEL of §2.2.1. If the count is not exactly 1, FAIL "cell-2 begin
     sentinel cardinality".
  3. e := the unique index i with L[i] minus a trailing 0x0A equal to the LAST
     SENTINEL of §2.2.1. If the count is not exactly 1, FAIL "cell-2 end
     sentinel cardinality".
  4. If not b < e, FAIL "cell-2 sentinel order".
  5. VERIFY: SHA-256 of the concatenation of L[b..e] inclusive equals
     1623dc45bb5c17c507ca590c3d6ca2a171ed7e40e5c4f287a8a736ee860db2b8.
     A mismatch FAILS CLOSED; OR-4 does not proceed against unexpected bytes.
  6. RETURN  concat(L[0..b-1]) || REPLACEMENT || concat(L[e+1..end])
     where REPLACEMENT is the §2.2.2 block, verified to hash to
     f2782a63db003dfb370d0c0c5afb9c928a8fc61c8af29285c8a1172657a84fee.

THERE IS EXACTLY ONE REPLACED RANGE AND IT IS [b, e]. NO OTHER RANGE OF THE
CELL-2 PREAMBLE IS TOUCHED, NO TWO RANGES OVERLAP BECAUSE THERE IS ONLY ONE, AND
NO IMPLEMENTER CHOOSES ANY BOUNDARY, ANY SENTENCE OR ANY WORD.
TWO IMPLEMENTATIONS GIVEN THE SAME SOURCE BYTES EMIT BYTE-IDENTICAL IN-MEMORY
OUTPUT, because every input to the algorithm is a literal fixed here.
```

#### §2.2.4 The properties the replacement satisfies, retained as an audit, not as the contract

`CT-1`..`CT-6` are no longer the acceptance criterion for the Cell-2 bytes —
the digest is. They are retained so a reviewer can check the pinned bytes
against the intent that produced them.

```text
CT-1  IT STATES THAT THE CELL IS SIGNED, names the exact selected token
      I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS, and names
      the signature path and digest ffcb4116…a7dc.                       SATISFIED
CT-2  IT STATES THAT W-A IS REJECTED, by name, as a historical fact about the
      choice — and states NO W-A CAPABILITY. No sentence describes a
      freeze-request socket, a slot-6 endpoint grant to the watchdog, a
      t-wd-freeze.v1 frame or a bounded service window as something the watchdog
      holds, may hold or could hold.                                     SATISFIED
CT-3  IT CONTAINS NO ASSERTION THAT THE CELL, THE MECHANISM OR THE CHOICE IS
      OPEN, UNSIGNED, UNDECIDED, UNPREDICTED OR CARRIED IN BOTH DIRECTIONS.
      MECHANICALLY CONFIRMED: zero of PO-9's eleven D1 literals occur in the
      replacement bytes.                                                 SATISFIED
CT-4  IT CONTAINS NO VARIANT-MARKER STRING, and no notation example that would
      reintroduce one.                                                   SATISFIED
CT-5  IT LEAVES CELL 1 UNTOUCHED. The process-claim identity cell is a separate
      cell, is NOT discharged by this signature, and its blocking notice stands
      unchanged. The splice range begins at the Cell-2 heading, which is after
      every byte of Cell 1, so OR-4 edits no byte of Cell 1.             SATISFIED
CT-6  IT ADDS NO NORMATIVE RULE. The replacement is a status statement. It
      introduces no predicate, no constant, no path, no count and no obligation
      that is not already stated in a normative region.                  SATISFIED

COMMON FACTS RETAINED THAT ARE NEEDED OUTSIDE THE REPLACEMENT, EACH PRESENT IN
THE PINNED BYTES:
  the freezer/witness reassignment is common to both options and is not itself
    a choice;
  H-1..H-4 are stated once in the canonical delimited block at §P1-14.8 and
    carried byte-identically at §A9 of the peer amendment;
  no author closure states OR-4 or any other step;
  G-10 (§P1-14.4) is the guard that confirms no variant block survives, at the
    CORRECTED section reference;
  the rest of the composite is a finished replacement for version 1.11 — the
    stale "replacement for v1.2" wording is gone from the source span itself,
    so no replacement can reintroduce it.
```

**No governing byte is written by this binding.** The transformation is
specified and its output is pinned; `OR-4` performs it, and `OR-4` is not
authorized.

### §2.3 The body locus table

`RESOLVE` = retain the `[W-B]` text inline, without its marker, and delete the
`[W-A]` text. `RETAIN` = leave the bytes untouched.

```text
#   LINE  REGION     OWNING SECTION                   ACTION   NOTE
 1    79  PREAMBLE   Cell 2 notation example          §2.2     inside the single replaced span
 2    80  PREAMBLE   Cell 2 notation example          §2.2     inside the single replaced span
 3    83  PREAMBLE   Cell 2 convention sentence       §2.2     BOTH markers; inside the span
 4   305  BODY       §P1-1.3 six signed choices       RESOLVE  W-A "additionally signals the loss by requesting the freeze" deleted
 5   306  BODY       §P1-1.3 six signed choices       RESOLVE  W-B "The watchdog requests nothing" retained
 6  1656  BODY       §P1-9.2 property 11              RESOLVE  W-B rationale retained
 7  1659  BODY       §P1-9.2 property 11              RESOLVE  W-A G-1/PEER_ENDPOINT_LIVE rationale deleted
 8  1666  BODY       §P1-9.2 property 12              RESOLVE  W-A "sends exactly one t-wd-freeze.v1" deleted
 9  1670  BODY       §P1-9.2 property 12              RESOLVE  W-B "It sends nothing" retained
10  1907  BODY       §P1-10.6 negative surface        RESOLVE  W-A "one further P1-layer operation is permitted" deleted
11  1910  BODY       §P1-10.6 negative surface        RESOLVE  W-B "No further operation of any kind is permitted" retained
12  1932  BODY       §P1-10.7 classifier TRIGGER      RESOLVE  W-B "loss of the peer control endpoint, record-first" retained
13  1933  BODY       §P1-10.7 classifier TRIGGER      RESOLVE  W-A ACCEPTED-record-in-bounded-window trigger deleted
14  2959  BODY       §P1-13.0 residence matrix        RESOLVE  BOTH markers on one line; W-A slot-6 socket clause deleted, W-B "It holds no socket" retained — EDIT IN PLACE
15  3242  BODY       §P1-13.2 P1-invariant row        RESOLVE  W-B TWO SEALED PIPES, "slot 6 is not used and is explicitly closed by a file action", retained
16  3248  BODY       §P1-13.2 P1-invariant row        RESOLVE  W-A THREE SEALED ENDPOINTS block deleted, with its AF_UNIX/SOCK_SEQPACKET socketpair and FD_CLOEXEC clause and its slot-6 request description
17  7179  BODY       §P1-15 test row 61               RESOLVE  BOTH markers; W-B classifier-and-terminal clause retained — EDIT IN PLACE
18  7207  BODY       §P1-15 test row 89               RESOLVE  BOTH markers; site (b) trigger fixed to the endpoint-loss site — EDIT IN PLACE. THE KV/SC CLAUSES, THE TWO-PHASE REQUIREMENT, THE Y COUNTEREXAMPLE AND THE PERMUTATION FIXTURES ARE OPTION-INDEPENDENT AND ARE RETAINED IN FULL
19  7218  BODY       §P1-15 test row 99               RESOLVE  BOTH markers; descriptor set fixed to {0,1,2}+{3,4,5,7,8,9,10}, slot 6 closed — EDIT IN PLACE. The W-A branch's SOCK_SEQPACKET/S_ISSOCK description is deleted with it
20  7317  GUARDDATA  §P1-17 VARIANT_MARKER class      RETAIN   the two pattern strings; NEVER a match target; H_GUARDDATA must not move
```

**Rows 1..3 carry no independent action.** They lie inside the single §2.2 span
and are disposed of by the one splice. They are listed only so the census sums
to twenty.

### §2.4 The mechanical post-`OR-4` invariant

Stated so that each is a total function of the resolved file's bytes.

```text
PO-1  MARKER ELIMINATION, BODY. Extract REGION(BODY) by the §P1-14.0 algorithm,
      apply §P1-14.2 NORMALIZE, count each pattern of the §P1-17
      VARIANT_MARKER class.
        REQUIRED: 0 and 0.
      This is exactly G-10 and it is the only one of these checks the shipped
      verifier performs. G-10 REMAINS BODY-SCOPED and is not widened here.

PO-2  MARKER ELIMINATION, WHOLE FILE OUTSIDE GUARD DATA. Count the same two
      patterns over the whole file MINUS REGION(GUARDDATA).
        REQUIRED: 0 and 0.
      STRICTLY STRONGER than PO-1. It is NOT G-10 and must not be described as
      G-10. IT IS NECESSARY AND IT IS NOT SUFFICIENT — see PO-9.

PO-3  GUARD DATA PRESERVED. Recompute H_GUARDDATA over the extracted region.
        REQUIRED: exactly
        faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
      unchanged from the pre-OR-4 value, with the two VARIANT_MARKER patterns
      still present exactly once each. THE CORRECT ACTION AT LINE 7317 IS TO
      CHANGE NOTHING.

PO-4  THE PERMITTED-OCCURRENCE TABLE. See §2.5. NO WHOLE-FILE "ZERO W-A STRINGS"
      RULE EXISTS IN THIS BINDING.

PO-5  W-B INVARIANTS POSITIVELY PRESENT, derivable from the resolved bytes with
      no variant marker anywhere in the derivation:
        a. the watchdog descriptor set is {0,1,2} + {3,4,5,7,8,9,10}, slot 6
           absent, two sealed pipes                                  (row 99)
        b. §P1-9.2 property 12: writes nothing, freezes nothing, signals
           nothing, sends nothing, exits
        c. §P1-10.6: no further operation of any kind is permitted
        d. §P1-10.7 TRIGGER: loss of the peer control endpoint, record-first
        e. row 89 site (b) is reachable only from the endpoint-loss trigger
        f. §P1-10.7's KG-1, KG-2, KV-1..KV-6 and SC-1..SC-10 are present in full
           and unmodified — they are OPTION-INDEPENDENT and OR-4 does not touch
           them

PO-6  SELECTION-TOKEN BINDING, AND THE CLOSED VOCABULARY THAT MUST SURVIVE.
      The resolved state carries the W-B token as the value bound across the two
      stages at B14, and TS-1's TWO literal option tokens AND BOTH paired
      option-specific amendment tokens MUST REMAIN. Deleting the non-selected
      literals breaks TS-2A A8, TS-2A A9, TS-5 B14 and IR-13 row 47 in one
      stroke, leaving the option-set predicate with no set to validate against.
      TS-1 lives INSIDE the joint install and authorization block, byte-identical
      with the amendment's §A10 block. OR-4 edits the composite only. DELETING A
      TS-1 LITERAL WOULD THEREFORE ALSO DESTROY THE JOINT BLOCK'S BYTE IDENTITY,
      which a reviewer detects by diff.
      NONE OF THE TWENTY MARKER LOCI FALLS INSIDE THE JOINT BLOCK — the highest
      body locus before it is 3248 and the next is 7179, straddling the joint
      block's content lines 3702..6821 without entering it — so a CORRECT OR-4
      never touches TS-1 at all. PO-6
      guards against an over-eager implementer, not against the specified
      procedure.

PO-7  DIGEST CONSEQUENCES, STATED SO THEY ARE NOT DISCOVERED LATE.
        H_GUARDDATA   UNCHANGED   (PO-3)
        H_BODY        CHANGES
        H_NORMATIVE   CHANGES
        H_FILE        CHANGES
      The composite H_FILE changes, therefore the §A0.4 pre-selection anchor
      value in the amendment — which equals the PRE-selection composite H_FILE
      e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b —
      is NOT the post-OR-4 composite digest and MUST NEVER be updated to it.
      IR-11 and MS-12 already state this.

PO-8  AMENDMENT UNCHANGED BY MARKER RESOLUTION. Amendment v1.9 contains zero
      markers, so OR-4's marker work does not touch it. OR-4's separate clause
      "the v1.9 amendment is installed" concerns MS-1's first literal path and
      nothing else.

PO-9  THE WHOLE-FILE-MINUS-GUARDDATA POST-RESOLUTION VERIFIER. See §2.6. Its
      D1 and D2 are now LITERAL ARRAYS, enumerated in full, with canonical
      serializations and hashes.
```

### §2.5 The canonical permitted-occurrence table

```text
CLASS R — RETAINED, AND REQUIRED. Deleting any of these is a defect.

R-1  THE TS-1 OPTION-SET GRAMMAR. Region BODY, inside the joint block.
     fragment  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
     at        composite v1.12 line 5576 (TS-1 selected_option_token grammar)
     required by  TS-1's "EXACTLY ONE of the two EXISTING option tokens";
                  TS-2A A8; TS-5 B14; IR-13 row 47
     EXPECTED COUNT IN THE RESOLVED FILE: 1

R-2  THE TS-1 PAIRING RULE. Region BODY, inside the joint block.
     fragment  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
     at        composite v1.12 line 5582
     required by  TS-1's pairing grammar; TS-2A A9
     EXPECTED COUNT IN THE RESOLVED FILE: 1

R-3  THE CK-14 OPTION-MISMATCH FIXTURE. Region BODY, inside the joint block.
     fragment  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
     at        composite v1.12 line 6490, as the Stage-B value of the fixture
     required by  CK-14's executable conformance fixture, which EXISTS to prove
                  that a twelve-check implementation admits a W-A Stage B
     EXPECTED COUNT IN THE RESOLVED FILE: 1

R-4  THE GUARD DATA MARKER PATTERNS. Region GUARDDATA.
     fragments  "[W-A]"   "[W-B]"      at composite v1.12 line 7317
     required by  §P1-17; §P1-14.3 AD-1; G-10's own text; G-6 against H_GUARDDATA
     EXPECTED COUNT IN THE RESOLVED FILE: 1 each, byte-identical, region digest
                  faf2d709…0426 unchanged

R-5  THE LEGITIMATE SUPERVISOR/PCS SOCKET AND SLOT-6 CLAUSES. Region BODY.
     These are NOT watchdog grants. They are the supervisor's control channel,
     common to BOTH options and untouched by the W-B choice.
       line  395  "T_ROLE_FD_ROLESRC = 5     slot 6 is role-class specific"
       line 1352  the supervisor's AF_UNIX / SOCK_SEQPACKET protocol-0 pair
                  "inherited to slot 6" — a GRANTING clause, for the SUPERVISOR
       line 1354  "SOCK_SEQPACKET is chosen because it is connection-oriented"
       line 7160  row 42: "the peer reaches the supervisor role at slot 6 and
                  nowhere else"
       line  601  "from _socket : _socketpair _CMSG_SPACE _CMSG_LEN"  §P1-3.4
       line  606  "_AF_UNIX _SOCK_SEQPACKET"                          §P1-3.4
       line  847  "_socketpair, whose descriptors CPython creates
                  non-inheritable"                                    §P1-6.x
     EXPECTED COUNT IN THE RESOLVED FILE: all seven present and unchanged
     MECHANICALLY CONFIRMED: none of these seven clauses contains any D1 or D2
     literal, and no D1 or D2 literal contains any of them (§2.6.4).

R-6  WATCHDOG SLOT-6 REFERENCES IN THEIR CLOSED / ABSENT SENSE ONLY.
       line 3242..3246  §P1-13.2 [W-B] branch: "slot 6 is not used and is
                        explicitly closed by a file action; the watchdog holds
                        no socket"
       line 7218        row 99 [W-B] branch: "{0,1,2} together with
                        {3,4,5,7,8,9,10}, slot 6 explicitly closed"
     EXPECTED COUNT IN THE RESOLVED FILE: exactly these two loci, each in its
     CLOSED/ABSENT sense, each with its [W-A] sibling deleted.
     A watchdog slot-6 occurrence in ANY OTHER SENSE IS FORBIDDEN by class F.

R-7  B14 AND IR-13 BINDINGS. Region BODY, inside the joint block.
     TS-5 B14, IR-13 row 35 (CK-14 / STAGE_B_OPTION_MISMATCH) and IR-13 row 47
     (CK-2 / STAGE_A_OPTION_INVALID) are RETAINED VERBATIM. OR-4 does not touch
     the joint block at all, so this is preserved by construction.

CLASS F — FORBIDDEN IN THE RESOLVED FILE. Expected count ZERO for each.

F-1  W-A OPERATIVE GRANTS AT OPERATIVE PREAMBLE OR BODY LOCI, DETECTED BY THE
     LITERAL D2 ARRAY OF §2.6.3 AND BY NOTHING VAGUER.
     LOCI THIS ELIMINATES: the Cell-2 W-A exposition inside §2.2's span, 1659,
     1666, 1907, 1933, the [W-A] clause of 2959, 3248, and the [W-A] clauses of
     7179 and 7218.

F-2  THE W-A REQUEST SOCKET AND FRAME BEHAVIOUR.
     fragment  t-wd-freeze.v1
     EXPECTED COUNT IN THE RESOLVED FILE: 0.
     THIS FRAGMENT IS NOT IN TS-1's VOCABULARY AND IS NOT IN THE GUARD DATA, so
     unlike the two option tokens it CAN be, and must be, eliminated whole. Its
     nine v1.12 occurrences are at 66, 1660, 1666, 1908, 1933, 2959, 3256, 7179
     and 7207, and every one of them is inside a W-A branch or the Cell-2 W-A
     exposition.

F-3  W-A VARIANT BRANCH TEXT.
     Any surviving [W-A]-branch content at any of §2.3's nineteen non-guarddata
     loci, with or without its marker.

F-4  OPEN-CELL ASSERTIONS ABOUT CELL 2, DETECTED BY THE LITERAL D1 ARRAY OF
     §2.6.2 AND BY NOTHING VAGUER.

WHAT CLASS F DOES NOT COVER, STATED SO THE TABLE CANNOT BE MISREAD:
  the W-A OPTION TOKEN and the W-A OPTION-AMENDMENT TOKEN are NOT in class F.
  They are in class R at rows R-1, R-2 and R-3. THERE IS NO RULE IN THIS BINDING
  REQUIRING THEM TO OCCUR ZERO TIMES, AND ANY SUCH RULE WOULD CONTRADICT TS-1,
  IR-13 row 47 AND THE CK-14 FIXTURE.

TOTALS IN THE RESOLVED FILE, AND THE ARITHMETIC THAT PRODUCES THEM
  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
      pre-resolution occurrences in composite v1.12:  3
        line   64  Cell-2 W-A exposition   -> REPLACED by §2.2's single splice
        line 5576  TS-1 option-set grammar -> RETAINED (R-1)
        line 6490  CK-14 fixture Stage-B   -> RETAINED (R-3)
      EXPECTED COUNT IN THE RESOLVED FILE: 2
  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
      pre-resolution occurrences: 1, at line 5582, TS-1's pairing rule
      post-resolution: 2 — the TS-1 pairing rule (R-2) AND ONE HISTORICAL
      MENTION INSIDE THE §2.2 REPLACEMENT, which names the rejected option's
      paired token and describes NO capability (CT-2). BOTH ARE CLASS R.
  t-wd-freeze.v1                  0   (F-2)
  "[W-A]" outside GUARDDATA       0   (PO-2)
  "[W-B]" outside GUARDDATA       0   (PO-2)
  "[W-A]" / "[W-B]" in GUARDDATA  1 each   (R-4)
  watchdog-sense "slot 6"         2 loci, both CLOSED/ABSENT   (R-6)
  supervisor-sense socket/slot-6  7 loci, unchanged            (R-5)
```

### §2.6 `M-3` REPAIR — `PO-9` with literal `D1` and `D2` arrays

**This is the check that closes `Y-M4`, `X-2` and now `M-3`.** It is a
**content** check, not a marker count, and it runs over the whole file **minus**
`REGION(GUARDDATA)`.

#### §2.6.1 Exact normalization, stated before the arrays

```text
PO-9 NORMALIZATION, WRITTEN PN, IS A TWO-STEP FUNCTION AND BOTH STEPS ARE EXACT.

  STRIP_LEAD(bytes)
    Split on 0x0A. From the START of every line delete every leading byte in
    the set { 0x20 SPACE, 0x09 TAB, 0x3E GREATER-THAN }, repeatedly, until the
    first byte of the line is outside that set or the line is empty. Rejoin
    with 0x0A.
    WHY IT EXISTS: markdown blockquote markers and indentation would otherwise
    sit inside a normalized run and let a rewrapped or unquoted restatement of
    a forbidden assertion evade a literal. §P1-14.2 NORMALIZE does not remove
    them.

  PN(bytes) := NORMALIZE( STRIP_LEAD(bytes) )
    where NORMALIZE is composite §P1-14.2 verbatim: decode as UTF-8, apply
    Unicode NFC, map every ASCII uppercase letter to lowercase, delete every
    asterisk, underscore and backtick and every HTML-comment opener and closer,
    replace every maximal run of space/tab/newline/carriage-return with a single
    space, strip leading and trailing spaces.

STRIP_LEAD LIVES IN THE ORACLE AND NOWHERE ELSE. It adds no normative surface to
the governing bytes, adds no guard-pattern class, and changes neither §P1-14.2
nor §P1-17 nor G-10.

BOUNDARY MATCHING, STATED SO IT IS NOT LEFT TO INTUITION. A literal MATCHES the
scope if and only if the literal's bytes occur as a CONTIGUOUS SUBSTRING of
PN(scope_bytes). There is no word-boundary rule, no stemming, no wildcard, no
regular expression, no case folding beyond NORMALIZE's, and no fuzzy match. The
count of a literal is the number of non-overlapping occurrences found by a
left-to-right scan.
```

#### §2.6.2 `D1` — the complete literal array, open-cell assertions about Cell 2

**ELEVEN LITERALS, IN THIS ORDER. THE ORDER IS PART OF THE VALUE.** Each is
`PN` applied to a passage of the pre-resolution Cell-2 span, so every assertion
the transformation discharges has a corresponding detector, and the coverage
claim is checkable rather than asserted.

```text
D1[ 1]  ### cell 2 — authorcellp1watchdogfreezemechanism, new in v1.3
D1[ 2]  this version is not acceptable as an operative object until the watchdog-freeze mechanism cell is signed.
D1[ 3]  what remains open is the mechanism by which a freeze becomes reachable when the peer control endpoint is lost:
D1[ 4]  this document selects neither and predicts neither.
D1[ 5]  where the two differ, the text below carries both variants inside an explicitly delimited block:
D1[ 6]  [w-a] … text operative only if w-a is signed …
D1[ 7]  [w-b] … text operative only if w-b is signed …
D1[ 8]  a [w-a]/[w-b] block is not operative text in either direction until the cell is signed.
D1[ 9]  at signature exactly one branch of every such block is retained and the other is deleted, in step or-4
D1[10]  the resulting file carries no variant block at all.
D1[11]  a build extracted from a file that still contains a variant block is not conforming and the verifier refuses it
```

```text
CANONICAL SERIALIZATION  CANON of the JSON array of those eleven strings in
                         that order, under composite MS-0: keys sorted (there
                         are none), no whitespace outside string literals, every
                         character outside printable ASCII escaped as \uXXXX,
                         followed by exactly one 0x0A. ARRAY ORDER IS PART OF
                         THE VALUE AND IS NEVER SORTED.
LENGTH                   926 bytes
SHA-256                  d5b375c518c935d3a6935a1932bf6bfa237cb9c99c7b81913f4e1433142b6c1e
REQUIRED                 zero matches in PN(resolved file minus REGION(GUARDDATA))
```

**COVERAGE, MECHANICALLY CHECKED RATHER THAN CLAIMED.** Every one of the eleven
literals occurs in `PN` of the pre-resolution Cell-2 span of composite v1.12.
A literal that does not is a defect in this array, and the oracle reports the
array `INCOMPLETE` rather than passing.

#### §2.6.3 `D2` — the complete literal array, rejected W-A operative grants

**THIRTEEN LITERALS, IN THIS ORDER.** `D2[1]` is the whole Cell-2 W-A exposition
with its blockquote markers stripped; `D2[2]`..`D2[5]` are its four capability
clauses taken separately so a partial reintroduction is still caught;
`D2[6]`..`D2[13]` are the `[W-A]` branch texts of the eight other operative
loci, each with its marker removed, because a marker-free reintroduction is
exactly the case `PO-2` cannot see.

```text
D2[ 1]  the watchdog holds one single-opcode, target-free freeze-request socket at slot 6 and may emit exactly one constant t-wd-freeze.v1 transport frame; the pcs opens a bounded service window and runs the freeze classifier only on an accepted request.
D2[ 2]  one single-opcode, target-free freeze-request socket at slot 6
D2[ 3]  may emit exactly one constant t-wd-freeze.v1 transport frame
D2[ 4]  the pcs opens a bounded service window
D2[ 5]  runs the freeze classifier only on an accepted request
D2[ 6]  the watchdog additionally signals the loss by requesting the freeze
D2[ 7]  a watchdog that made that inference would send its one authorized
D2[ 8]  before exiting it sends exactly one constant t-wd-freeze.v1 record
D2[ 9]  one further p1-layer operation is permitted: emitting exactly one constant,
D2[10]  an accepted t-wd-freeze.v1 record inside the bounded service
D2[11]  p1 provides the watchdog role process and its three
D2[12]  loss of the peer control endpoint additionally produces the pcs's bounded service window
D2[13]  with slot 6 sissock, ordwr, sockseqpacket — three sealed endpoints
```

```text
CANONICAL SERIALIZATION  as for D1, CANON of the JSON array in that order
LENGTH                   1044 bytes
SHA-256                  4e2120857dd67124095e5f5479d69cbf7ba703605abb3448a2fe414b3ff8a15c
REQUIRED                 zero matches in PN(resolved file minus REGION(GUARDDATA))

THE SIX FORBIDDEN CAPABILITIES AND THE LITERALS THAT CARRY THEM
  a freeze-request socket                 D2[1] D2[2]
  a watchdog slot-6 endpoint              D2[1] D2[2] D2[13]
  a single-opcode capability              D2[1] D2[2]
  a t-wd-freeze.v1 frame                  D2[1] D2[3] D2[8] D2[10]
  a bounded service window                D2[1] D2[4] D2[10] D2[12]
  an ACCEPTED-request-driven trigger      D2[1] D2[5] D2[10]
  (plus the request-the-freeze grant      D2[6] D2[7] and the three-endpoint
   topology                               D2[11] D2[13])
NO LITERAL IS A BARE WORD. "slot 6", "socket", "window" and "accepted" do not
occur as literals, because each of them occurs legitimately in class R.
```

#### §2.6.4 The false-positive and false-negative demonstrations

```text
FALSE POSITIVES — every retained class, checked against the whole D1+D2 array.
  the §2.2 replacement bytes                     D1 matches 0   D2 matches 0
  Cell 1, byte-unchanged, which legitimately
    still asserts an OPEN cell about a DIFFERENT
    author cell                                  D1 matches 0   D2 matches 0
  the joint install and authorization block,
    where TS-1's grammar, TS-1's pairing rule
    and the CK-14 fixture MUST name the W-A
    token                                        D1 matches 0   D2 matches 0
  REGION(GUARDDATA), which is out of scope
    anyway and is additionally clean             D1 matches 0   D2 matches 0
  each of R-5's seven supervisor-side clauses    contains no literal, and no
                                                 literal contains it
  each of R-6's two closed/absent watchdog
    slot-6 clauses                               contains no literal, and no
                                                 literal contains it

  WHY CELL 1 IS SAFE, AND IT IS THE SHARPEST CASE. Cell 1's blocking notice says
  "This version is not acceptable as an operative object until the author cell
  AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS is signed". D1[2] requires the
  continuation "...until the watchdog-freeze mechanism cell is signed", which
  Cell 1 does not carry. EVERY D1 LITERAL CARRIES A WATCHDOG-FREEZE-SPECIFIC
  DISCRIMINATOR FOR EXACTLY THIS REASON. A detector that fired on Cell 1 would
  demand the deletion of a blocking notice this signature does not discharge,
  which CT-5 forbids.

FALSE NEGATIVES — every forbidden vector, checked.
  each of the eleven D1 literals, placed in a marker-free carrier with
    arbitrary surrounding bytes, arbitrary line wrapping and arbitrary
    blockquote indentation                       DETECTED, 11 of 11
  each of the thirteen D2 literals, likewise     DETECTED, 13 of 13
  the whole Cell-2 W-A exposition restored as
    plain paragraphs with its "> " markers and
    its "[W-A]" marker removed                   DETECTED by D2[1]..D2[5]
  any single capability clause of that
    exposition restored alone                    DETECTED by its own literal
  the pre-resolution Cell-2 heading restored     DETECTED by D1[1]
```

#### §2.6.5 `D3` and `D4`

```text
DETECTOR D3 — CLASS-R PRESENCE. Every row of §2.5's class R is present with its
  expected count. A resolution that satisfies D1 and D2 by DELETING a class-R
  occurrence FAILS D3. This is what makes the D1/D2 pair sound rather than
  merely strict.

DETECTOR D4 — GUARD DATA UNTOUCHED. H_GUARDDATA equals faf2d709…0426.

G-10 REMAINS BODY-SCOPED. PO-9 is not G-10, is not a guard rule, is not added to
§P1-14.3 or §P1-14.4, and is not run by the shipped verifier. It is an ORACLE
check over a candidate transformation, and its failure means the transformation
is wrong — not that the verifier refuses.
```

---

## §2A. `B2` — the dry-run oracle, and its boundary against `OR-3`/`OR-4`

A **test-only, in-memory transformation oracle** may be implemented and
unit-tested **before** the amendment is accepted and before any handoff step is
authorized — **and only after a separate inactive-scaffold authorization, which
does not exist.**

### §2A.1 What the oracle is

```text
O-1  INPUT. Byte copies of amendment v1.9 and composite v1.12, read from their
     literal paths read-only and held in memory. It opens neither for
     behaviour; it hashes and rewrites bytes and interprets no rule.
O-2  IT SELECTS W-B IN MEMORY, from a test-only enum with exactly two members,
     and produces a candidate resolved byte string as a RETURN VALUE.
O-3  IT CHECKS PO-1 THROUGH PO-9 against that in-memory string, and reports each
     as a pass or a fail with the locus that failed.
O-4  IT MAY REPORT DIGESTS, and every reported digest MUST be emitted with the
     literal tag
       test-only/non-installed/non-authoritative
     adjacent to the value, in the same string, so that no transcript, log line
     or test output can be quoted as an install digest.
O-5  IT IS TOTAL AND DETERMINISTIC. Same inputs, same output bytes, on every
     run, on any host. It samples no clock, draws no entropy and reads no
     environment variable. §2.2.3's splice makes this checkable: two independent
     implementations of it must agree byte for byte.
```

### §2A.2 What the oracle may never do

```text
O-6   IT WRITES NO FILE TO ANY GOVERNING OR RUNTIME PATH. Nothing under
      successor/, nothing under successor/officina/, nothing under any INSTALL
      directory, nothing at either MS-1 literal path. If it writes at all it
      writes only under a per-test temporary root it created and removes.
O-7   IT CREATES NO KEY AND NO ENTROPY.
O-8   IT CREATES NO STAGE A AND NO STAGE B, no detached signature, no M4
      manifest, no M7 attestation, no member list, no install record and no
      install_record_id.
O-9   ITS OUTPUT IS NOT PRODUCTION INPUT. The resolved byte string is a return
      value and a test fixture. No function that writes a governing path may
      accept it, and the oracle module must export no writer that could.
O-10  IT IS NOT OR-4 EVIDENCE. A passing oracle run proves nothing about the
      install, satisfies no OR step, and may not be cited in any acceptance,
      authorization, attestation or install record.
O-11  IT RUNS NO PROCESS-CONTROL OPERATION. No fork, exec, posix_spawn, signal,
      wait, killpg, socket, pipe, prctl or /proc read against any live process.
O-12  IT IMPLEMENTS NO RUNTIME BEHAVIOUR. It is not the watchdog EOF route, not
      the PCS classifier, not KG-1, not KG-2, not KV-1..KV-6, not SC-1..SC-10,
      not the descriptor topology and not any process operation. Those are §H3
      of the handoff and they are NOT implementable under any authorization that
      exists.
```

### §2A.3 What later authorized `OR-4` does that the oracle does not

```text
                                        ORACLE      AUTHORIZED OR-4
  produces resolved bytes                in memory   ON DISK at MS-1's second
                                                     literal path
  requires the acceptance token          no          YES — v1.9 accepted first
  requires a completed OR-3              no          YES
  requires an implementation and a       no          YES, both
    one-shot handoff authorization
  installs the amendment (MS-1 path 1)   no          YES
  fixes M1 and its two digests           no          YES
  is a precondition of OR-5..OR-11       no          YES
  its digests may be recorded in M4      NEVER       YES, at OR-6
  is subject to G-10 in the shipped      no          YES
    verifier
  changes H_BODY, H_NORMATIVE, H_FILE    of nothing  of the real composite
    of a real governing file              on disk
  is reversible                          n/a         NO — it lands with
                                                     OR-3..OR-11 or none does

THE SINGLE SENTENCE THAT SEPARATES THEM: the oracle rewrites a copy and returns
it; OR-4 rewrites the governing file and every later step depends on the result.
```

**The resolved-byte files are not created by this task.** Neither this binding,
nor the handoff, nor the oracle produces composite v1.12 in post-selection form
at any path.

---

## §3. `B3` — the gate ledger, and the identity disposition

### §3.1 The total ledger, current state through `T`

```text
#   GATE                                          STATE            AUTHORIZES NEXT?
 0  Composite Cell 1 blocking notice              NOT DISCHARGED   no
      "This version is not acceptable as an operative object until the author
      cell AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS is signed", and the
      Option A signature "does not unblock this cell and does not make this
      version operative."
      NO CHECK IN CK-1..CK-15 EXAMINES CELL 1. G-11 is a final-state integrity
      gate over the closed member set and reads no blocking notice, so the gate
      would pass on an object that declares itself non-operative. THIS ROW IS
      THEREFORE A PRECONDITION OF GATE 3 (acceptance), GATES 9..13
      (OR-3..OR-11) AND GATE 15 (T), AND IT IS CLOSED BY NONE OF THEM.
      §2.2's replacement does not touch it, and PO-9's D1 does not fire on it.

 1  W-B author selection (OR-2)                   COMPLETE         yes — this binding only
      token I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
      signature ffcb4116…a7dc, 2026-08-05, base 176d609

 2  This post-selection binding, v3               DRAFT            no
      awaiting bounded X/Y review against the v2.12 bytes

 3  Watchdog authority amendment v1.9 acceptance  NOT ACCEPTED     no
      token I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9
      unsigned; §4 states exactly what it will and will not do.
      THE v1.8 AND v1.7 TOKENS ARE RETIRED AND MUST NOT BE SIGNED: R1 and R2
      changed the bytes they would have accepted.

 4  Process identity Option A selection           COMPLETE         no
      token I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
      signature 7a8ab2da…3d1f, 2026-08-04
      recorded at XS-1 as external author state, member of no class

 5  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1  NOT ACCEPTED     no
      must be reviewed and accepted SEPARATELY before Option A can become
      operative; §3.2 states the disposition in full

 6  The LATER COMBINED BINDING of XS-1            DOES NOT EXIST   no
      STATE: BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW, by XS-1(b)

 7  Fresh independent X/Y round on the v2.12 pair NOT PERFORMED    no
      the v2.12 governing pair has NOT been independently reviewed. Gate 3
      cannot open before it does.

 8  Inactive SCAFFOLD implementation              CANDIDATE        no
                                                  ELIGIBILITY ONLY
      the handoff v3 is a scope contract for INERT ORACLE AND DECLARATIVE
      SCAFFOLDING ONLY. No code may be written under it until gate 9 exists.

 9  Inactive-scaffold authorization               NOT GRANTED      —
      a separate author act, after gates 3 and 7 and after this binding survives
      X/Y review. IT IS NOT AN AUTHORIZATION TO IMPLEMENT THE RUNTIME.

10  Runtime implementation authorization          NOT GRANTED      —
      a SEPARATE later act, distinct from gate 9. See handoff §H11.

11  OR-3 key generation and Stage A               NOT AUTHORIZED   —
12  OR-4 variant resolution and amendment install NOT AUTHORIZED   —
13  OR-5..OR-9 verifier, tests, M4, M7, member list NOT AUTHORIZED —
14  OR-10 Stage B and detached signature          NOT AUTHORIZED   —
15  OR-11 install record, no-replace, last        NOT AUTHORIZED   —
16  One-shot atomic-handoff authorization         NOT GRANTED      —
      a separate author act; OR-3..OR-11 land together or none does (H-1..H-3)
17  T activation                                  NOT AUTHORIZED   —

T = NOT_ACTIVATED.  PROGRAMME CLAIM = OPEN.
```

Gates 11 through 15 are **not five independent permissions**. `H-1` makes the
amendment and the composite one indivisible acceptance unit; `H-2` and `H-3`
make `OR-1`..`OR-11` a mandatory operator obligation that lands together or not
at all.

### §3.2 The identity-token disposition, resolved from the bytes

**The question:** may the inactive scaffold include observation-only identity
code while `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` is unaccepted?

```text
NO CODE. NOT DISABLED CODE, NOT GATED CODE, NOT DUMMY-TESTED CODE. THE
IDENTITY-OBSERVATION SURFACE IS OUT OF SCOPE FOR THIS IMPLEMENTATION ENTIRELY,
AND THE REASON IS NOT CAUTION — IT IS THAT THE GOVERNING PAIR DOES NOT DEFINE IT.
```

```text
C-1  THE MECHANICAL FACT, RECOMPUTED AGAINST v2.12. The strings attested_pid and
     attested_pgid occur ZERO times in composite v1.12 and ZERO times in
     amendment v1.9. There is no schema, key, type, carrier, consumer or
     destination for an identity observation anywhere in the governing pair.
     Code written now could only be invented.

C-2  composite §P1-13.2 row 2, quoted at Cell 1: "The layer that must write
     those two keys therefore cannot obtain their values." TWO coherent repairs
     exist, choosing between them CHANGES SIGNED MEANING, and — verbatim —
     "This document chooses neither and invents no value." Writing the code
     chooses. THAT IS THE INVENTION THE CELL FORBIDS.

C-3  composite Cell 1 blocking notice stands unchanged, and is gate 0 above.

C-4  amendment XS-1(b): the later combined binding MUST "record the separate
     review and acceptance of P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1, OR
     REFUSE TO PROCEED." That obligation attaches to THE COMBINED BINDING, by
     its own words, and to nothing else.

C-5  amendment N-13 and N-4.
C-6  the identity selection signature's own outstanding-gates section.

C-7  THE NEW R2 CONTENT DOES NOT DISTURB ANY OF THIS. KG-1 observes a process
     GROUP and a start identity from /proc/<pid>/stat for process-control
     purposes; those are not the attested_pid / attested_pgid identity fields of
     §P1-13.2 row 2, which are peer-record fields with no schema in this pair.
     KG-2 P-2 records a pid as a group value inside the PCS's own in-memory
     handle table and writes no durable record of any class. NO IDENTITY FIELD
     IS RE-DERIVED, DEFAULTED OR INVENTED BY EITHER.
```

**This document is NOT the later combined binding `XS-1` names.** `XS-1` defines
that binding by what it must do: (a) record the signature's path and digest;
(b) record separate review and acceptance of the weakening token or refuse to
proceed; (c) state whether the signature becomes a member of its own closed set,
in which class and at what cardinality; (d) re-derive the identity fields of the
process-claim record. **This binding does (a) only**, in the same register
`XS-1` itself uses — external author state, member of no class, authority for
nothing. It performs neither (c) nor (d). **Restating (a) cannot constitute
becoming the combined binding, because `XS-1` already performs (a) in the
governing bytes.**

```text
D-A  THE W-B POST-SELECTION BINDING          not blocked by identity
D-B  THE W-B INACTIVE SCAFFOLD SCOPE         identity-observation code EXCLUDED
                                             — no code, no dummy test, no
                                             disabled path, no enum value, no
                                             schema key
D-C  THE LATER COMBINED BINDING OF XS-1      BLOCKED_PENDING_IDENTITY_
                                             WEAKENING_REVIEW, by C-4
```

`D-C` is a **ledger state of a document that does not exist**, recorded so that
it is auditable rather than silent. **It is not this document's closure token.**

---

## §4. `B6` — the acceptance and authorization boundary

The only watchdog amendment acceptance token available after a fresh bounded X/Y
review round on the v2.12 bytes is:

```text
I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9
```

**The v1.8 and v1.7 tokens are retired.** `R1` and `R2` changed the bytes they
would have accepted, so signing either would accept a pair that no longer exists.

### §4.1 What that future token accepts

```text
A-1  THE TWO GOVERNING FILES AS ONE INDIVISIBLE UNIT — amendment v1.9 and
     composite v1.12, at the exact digests of §0.2, per H-1.
A-2  THE TWO DELIMITED BYTE-IDENTICAL REGIONS at their stated digests, and the
     narrowed identity claim that attaches to those two regions and to nothing
     else.
A-3  THE FIXED ACCOUNTING — MS-2 at 67, MS-3 at 7, MS-8 at 81, TS-3
     member_count 81, member classes 7, closed failure codes 25, pre-production
     checks 15 running CK-1..CK-15, M4 key set 21, IR-13 at 50 rows, MS-13
     element keys 6 with 8 effect booleans each, 32 effect assertions all false,
     4 project-import dependencies, 7 unexecuted module-scope branches, 75
     composite provenance rows, the 16-member generic_harness.py scoped
     allowlist, and the 89-row reachable_closure at CANON length 20534.
A-4  THE KG-1, KG-2, KV-1..KV-6 AND SC-1..SC-10 DEFINITION at §P1-10.7 as
     normative content of the composite, INCLUDING its two explicit phases, its
     closed state-character set and its Part 2 new-rule table.
A-5  THE OBLIGATION SHAPE OF OR-1..OR-11 — the sole conforming construction
     procedure, an operator obligation the final-state gate does not
     reconstruct (FS-1..FS-5).
```

### §4.2 What that future token does **not** authorize

```text
B-1   IT DOES NOT AUTHORIZE ANY CODE EDIT, at any path, of any kind.
B-2   IT DOES NOT START OR-3. No key pair, no entropy draw, no Stage A.
B-3   IT DOES NOT GENERATE OR HOLD ANY KEY.
B-4   IT DOES NOT EXECUTE OR-4. No variant block is resolved by accepting the
      amendment; the composite's bytes do not move, and §2.2's replacement
      bytes are not written anywhere.
B-5   IT DOES NOT INSTALL ANYTHING. No verifier at MS-5's path, no test module
      at either MS-6 path, no edit to any production root.
B-6   IT DOES NOT WRITE M4, M7, THE MEMBER LIST, STAGE B, THE DETACHED
      SIGNATURE OR THE INSTALL RECORD.
B-7   IT DOES NOT RUN THE TEST MATRIX. OR-7 is a separate step.
B-8   IT DOES NOT ACTIVATE T, open a candidate, draw a datum, produce an
      outcome, move a Proof or move the programme claim.
B-9   IT DOES NOT ACCEPT P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1, make it
      signable, or predict it. It does not resolve §P1-13.2 row 2 and it is not
      the combined binding of XS-1. IT DOES NOT DISCHARGE CELL 1.
B-10  IT DOES NOT RETROACTIVELY VALIDATE ANY EXISTING WORKING-TREE CODE.

THREE FURTHER AUTHOR ACTS ARE REQUIRED AFTER IT, AND THEY ARE SEPARATE FROM ONE
ANOTHER:
  (i)   an INACTIVE-SCAFFOLD AUTHORIZATION;
  (ii)  a RUNTIME IMPLEMENTATION AUTHORIZATION — see handoff §H11;
  (iii) a ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION, permitting OR-3..OR-11 to run
        once, together, in order.
NONE IS GRANTED BY THE ACCEPTANCE TOKEN, AND NONE IS GRANTED HERE.
```

---

## §5. `B5` — the provenance disposition, performed again

### §5.1 What changed since v2

v2.11 performed the eight-row catch-up. **v2.12 is another real replacement
generation and owes its own four rows.**

```text
                                       v2.11   v2.12
MS-2                                      63  ->  67
MS-3                                       7      7
MS-8 / TS-3 member_count                  77  ->  81
composite provenance region rows          71  ->  75
member classes                             7      7   only M2 grew
```

The four rows, in `MS-2` order, each digest recomputed from disk:

```text
71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md
3964469740fc73a6a4836b64247003c39d5261a6af9c6ddf37a0da76c13f0759  reviews/fable_officina_p1_wb_v2_11_final_x_review.md
ef4508be13d9ef395b2e8d5542d6256e2bd5719e99cbff209d13612dc5dd00c4  reviews/sol_officina_p1_wb_v2_11_final_y_review.md
```

### §5.2 The disposition rules

```text
PR-1  THE FOUR ROWS ARE IN. This generation's install enumerates 81 members
      from MS-1..MS-7 alone, with MS-2 at its literal 67 and the TS-3
      member_count literal at 81. THE HANDOFF STILL TOUCHES NONE OF IT.
PR-2  OR-4 IS STILL NOT A GENERATIONAL ROUND. It produces the post-selection
      bytes of the SAME generation at MS-1's SAME two literal paths and replaces
      no document, so no row enters at OR-4, OR-6, OR-9 or OR-11.
PR-3  THE NEXT ACTUAL GENERATIONAL ROUND — one that REPLACES v1.9/v1.12 — adds
      its own four rows: the v1.9 amendment, composite v1.12 and that round's
      two independent reviews. It does NOT re-add any of the twelve before them.
PR-4  NEGATIVE TEST OBLIGATION. A fixture that enumerates 63, 69, 73, 77 or 85
      members FAILS against this generation. The handoff states this as a
      required negative test.
PR-5  THE TWO W-B BINDING REVIEWS ARE NOT M2 MEMBERS of any generation and were
      not substituted for any pair-review row.
PR-6  NO HISTORICAL BYTE IS EDITED BY ANY OF THIS. The 63 rows MS-2 already
      carried are byte-unchanged; the four are appended.
```

### §5.3 The governing findings, and their state

```text
F1  MAJOR, FAIL-OPEN.  REPAIRED IN v2.11 and carried. The pre-production range
    is CK-1..CK-15 everywhere; the twelve-check range exists only in sentences
    that negate it or describe the removed defect — THREE per file, recounted
    from the v2.12 bytes, correcting the v2.11 closure's "three in each file"
    which was wrong for the amendment.
F2  MAJOR, NOT IMPLEMENTABLE.  DEFINED IN v2.11, EXECUTABLE IN v2.12. KG-1's
    grammar returns PRESENT_VALID on an ordinary Linux stat line; KG-2's rules
    are stated as new content with an honest source table; SC-9 and SC-10 make
    the forbidden-target terminal dominant before any signal. THE DEFINITION IS
    STILL NOT AN IMPLEMENTATION AUTHORIZATION: the handoff forbids writing the
    classifier and gate 10 does not exist.
F3  MINOR.  REPAIRED. OR-4 reads "the v1.9 amendment is installed", inside the
    joint block and therefore in BOTH files.
F4  MINOR.  REPAIRED in v2.11 and carried: composite's G-10 locator names
    §P1-14.4.
F5  MINOR, NEW AND REPAIRED IN v2.12. H-4 named CK-12 as an owner of
    HISTORICAL_BYTE_MOVED; CK-7 owns it and owns it alone. The canonical block
    now says so, in both files.
F6  MINOR, NEW AND REPAIRED IN v2.12. N-16's MS-8 cardinality 69 -> 81; row
    106's fixture-group header eleven -> ten with every group defined; CK-13's
    "70th entry" -> "82nd entry"; the §A9 line-number locator replaced by a
    section reference; region lengths reported in UTF-8 bytes.
```

---

## §6. Negative space

This draft creates nothing executable. It authorizes no selection, no X/Y
verdict, no amendment acceptance, no identity-token acceptance, no identity
bounded weakening, no implementation, no commit, no verifier or manifest edit,
no key generation, no entropy draw, no selection artifact, no authorization
artifact, no detached signature, no attestation, no install record, no resolved
amendment or composite bytes at any path, no process, socket, pipe, fork, exec,
signal, wait or `prctl` operation, no supervisor, PCS, controller, worker or
watchdog, no capability, world, learner, candidate, trajectory, capacity
artifact, custody disposition, result manifest, spend, datum, outcome, Proof or
claim movement.

**The §2.2 replacement bytes exist here as a specification and nowhere else.**
They are not written to any path, are not composite bytes, and become composite
bytes only at an authorized `OR-4` that does not exist.

No freeze was executed, requested, journalled or witnessed. No `/proc` was read
against any live process. No clock was sampled for any contract purpose. No
Philosophia production or project module was imported, executed or compiled.
**No existing file was modified: no historical or governing document, no code,
no test, no signature, no runtime artifact and no prior review.** The untracked
working-tree `generic_harness.py` was not read, adopted, edited or cited by this
draft; the handoff states the audit obligation that governs it.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 IDENTITY-OBSERVATION IMPLEMENTATION SURFACE = OUT OF SCOPE, NO CODE
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
WATCHDOG AUTHORITY AMENDMENT V1.9 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

The exact selected token and the formal selection signature govern. This draft,
the companion handoff and every author closure are untrusted self-assessments
and are normative for nothing.
