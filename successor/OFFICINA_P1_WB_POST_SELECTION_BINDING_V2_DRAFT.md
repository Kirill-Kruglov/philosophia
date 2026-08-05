# Officina P1 W-B post-selection binding v2 (draft)

**Author:** Claude Code Opus 5, **post-selection binding author only**. Not an
independent X-line or Y-line reviewer. **This draft selects nothing, accepts
nothing, installs nothing and executes nothing.**

This document is a **plan and contract for a transformation, not the
transformation itself.** It creates no resolved amendment, no resolved
composite, no key, no Stage A, no Stage B, no manifest, no attestation, no
signature and no install record. `T` is `NOT_ACTIVATED`; the programme claim is
`OPEN`.

**v2 REPLACES v1 WHOLLY.** v1 was reviewed by two independent lines against the
v1.7/v1.10 governing bytes. Both returned `REVISE_OFFICINA_P1_WB_GOVERNING_PAIR`
and both recorded binding-level blockers. v2 is re-issued against the **v1.8 /
v1.11 governing bytes** with `Y-M3`, `Y-M4`, `Y-M5`, `X-1`, `X-2` and `X-3`
repaired. Every mechanical result of v1 that the X line independently reproduced
and confirmed — the region split, the marker census, the both-marker line set,
the guard-data retention rule, the `PO-6` / `IR-13` row 47 reasoning, the
identity disposition and the provenance disposition — is carried forward,
recomputed against v1.11, and stated again here.

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

The v2.11 generation. Every digest recomputed from disk at authoring time.

```text
71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md
```

Composite region digests (§P1-14.0 extraction):

```text
H_BODY       ce728942d3d1a746960a9fbf0feb4a969b79b9793d2b89f67a5d73c9b31b51cf
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  01ea73918211509a19126e5847234a4b64d6ffbabf8a064d7051b460949743b8
H_FILE       c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6
```

The two delimited byte-identical regions, extracted and diffed with zero
difference:

```text
canonical atomic-handoff preamble  ca2ff30b93818f7945b442de68438ddaa8f71879443595903fddfa950cf4a785   4052 bytes
joint install and authorization    9bf4a831b138889b4ae71d2985820793f10a649311199ec3136d75a6514babe5 222364 bytes
```

The v2.11 author choice packet, hash-read target of `TS-2B` `A16(b)` and member
of nothing:

```text
successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_11_CORRECTION.md
```

Recorded as **external author state, not as a member and not as authority
here**, exactly as `XS-1` records it:

```text
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
```

The two reviews that licensed the v2.11 round and this re-issue:

```text
d8483c185c6f438f4a209353716b7d8aef31529c5f6876381ea03431beb15ba1  reviews/fable_officina_p1_wb_binding_x_review.md
e1bf893a00fc625f97698ddbe9a2f0d4413a8578c65722559f3ddefe7bcd8628  reviews/sol_officina_p1_wb_binding_y_review.md
```

### §0.3 What this document is not

```text
IT IS NOT the resolved amendment and NOT the resolved composite. It creates
  neither, and §2A states the exact boundary against OR-3 and OR-4.
IT IS NOT the LATER COMBINED BINDING named at XS-1(a)..(d). It does not resolve
  the process-claim identity cell, does not bind the identity signature into any
  member class, and does not re-derive any identity field. §3 states this in
  full and it is load-bearing.
IT IS NOT an amendment acceptance. The v1.8 acceptance token is unsigned.
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
REMAIN IN TS-1's CLOSED VALIDATION VOCABULARY AND ARE NOT DELETED (§2.4 PO-6):
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
    group stops — under KV-1..KV-6 and SC-1..SC-8, now DEFINED IN FULL at
    §P1-10.7 of composite v1.11.
      composite §P1-10.7 TRIGGER, [W-B] branch
      composite §P1-15 row 89, [W-B] branch

S4  NO TRANSPORT FRAME EXISTS ON THIS BRANCH. No t-wd-freeze.v1 record is
    emitted, received, accepted, journalled or witnessed on any path. The W-A
    bounded service window does not exist on this branch.

S5  NO DURABLE OBJECT, NO EVIDENCE, NO SCIENTIFIC INPUT. The watchdog produces
    no durable object of any class and supplies no input to any scientific
    predicate. The classifier's journal state — its terminal, its SC-5 tokens
    and its freeze_ns — is P1-owned process-control material and never reaches a
    peer artifact, an acceptance predicate, a qualification, a comparison, a Q
    or C fact, or any published record.
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
    SC-1..SC-8 sub-block; §P1-15 rows 89 and 101
  WHAT W-B FIXES  the TRIGGER, and only the trigger: loss of the peer control
    endpoint, record-first. The W-A trigger is deleted.
  RESOLVED SINCE v1  the scope predicate this amendment names is now DEFINED. v1
    recorded it as finding F2 and fenced it; v1.11 supplies the definition and
    the fence is lifted for the DEFINITION, not for implementation (§H10 of the
    handoff still forbids writing the classifier).
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
NB-6  IT DOES NOT CHANGE THE v2.11 GOVERNING BYTES. Every count, digest and
      rule above is READ from them.
```

---

## §2. The complete option-resolution contract

### §2.1 The mechanical census, recomputed against composite v1.11

```text
MARKER-BEARING LINES, composite v1.11           20
MARKER-BEARING LINES, amendment v1.8             0
  the amendment contains the two marker strings ZERO times; every variant block
  lives in the composite, and OR-4 therefore edits ONE file
"[W-A]" OCCURRENCES, composite                  13
"[W-B]" OCCURRENCES, composite                  13
BOTH-MARKER LINES, WHOLE FILE                    6   83, 2531, 6747, 6775, 6786, 6885
BOTH-MARKER LINES, BODY ONLY                     4   2531, 6747, 6775, 6786
```

Region sentinels in composite v1.11:

```text
OFFICINA-P1-BODY-BEGIN          line  251
OFFICINA-P1-BODY-END            line 6845
OFFICINA-P1-GUARDDATA-BEGIN     line 6847
OFFICINA-P1-GUARDDATA-END       line 6888
OFFICINA-P1-PROVENANCE-BEGIN    line 6890
OFFICINA-P1-PROVENANCE-END      line 7094
```

```text
REGION      LINES  A   B   OBLIGATION AT OR-4
  PREAMBLE      3   2   2   outside G-10's match range. RESOLVED BY §2.2's
    (1..250)                CELL-2 TRANSFORMATION, which is byte-exact and
                            covers the WHOLE Cell-2 notice, not only these three
  BODY         16  10  10   G-10's exclusive match range. RESOLVE each to the
    (252..6844)             [W-B] branch and DELETE the [W-A] branch
  GUARDDATA     1   1   1   THE PATTERN SOURCE. RETAIN BYTE-IDENTICAL. Never a
    (6848..6887)            match target; deleting it destroys G-10 and changes
                            H_GUARDDATA
  ---------------------------------------------------------------------------
  TOTAL        20  13  13
```

The four both-marker **body** lines must be **edited in place**. A line-deletion
strategy is wrong on its face.

### §2.2 `Y-M4` / `X-2` REPAIR — the complete Cell-2 transformation, byte-exact

**v1's defect, stated so the repair is checkable.** v1's table disposed of
composite lines 79, 80 and 83 because those are the three marker-bearing
preamble lines, and labelled them "Cell 2 blocking notice". **They are not the
blocking notice.** Lines 79–80 are the notation example, line 83 is the
convention sentence, and the blocking notice itself — together with the option
exposition and the "selects neither" prose — carries **no marker at all**, so no
marker census could reach it and `PO-2` could not see it.

**The transformation is therefore defined over the whole Cell-2 span, line by
line, and it is not limited to marker-bearing lines.**

```text
CELL-2 SPAN, composite v1.11:  lines 55..95 inclusive
LINE(S)  CURRENT CONTENT, BY ROLE                          ACTION AT OR-4
 55      "### Cell 2 — AUTHOR_CELL_P1_WATCHDOG_FREEZE_      REPLACE HEADING
          MECHANISM, new in v1.3"
 56      blank                                             RETAIN
 57-58   "This version is not acceptable as an operative    REPLACE — this is
          object until the watchdog-freeze mechanism cell   THE BLOCKING NOTICE
          is signed."                                       and it is DISCHARGED
 58-60   "The watchdog freezer/witness role is reassigned   RETAIN, marker-free;
          to the supervisor ... common to both options and   it states a fact that
          is NOT itself a choice."                           is TRUE after W-B
 60-62   "What remains open is the mechanism by which a     REPLACE — the
          freeze becomes reachable when the peer control     mechanism is NO
          endpoint is lost:"                                 LONGER OPEN
 63      blank                                             RETAIN
 64-68   the W-A option exposition, as a blockquote:        DELETE ENTIRELY —
          the W-A option token; "one single-opcode,          this is REJECTED W-A
          target-free freeze-request socket at slot 6";      CAPABILITY EXPOSITION.
          "may emit exactly one constant t-wd-freeze.v1      It carries NO marker
          transport frame"; "a bounded service window";      and v1's table did not
          "runs the freeze classifier only on an ACCEPTED    reach it.
          request"
 69      ">" blockquote separator                          DELETE with 64-68
 70-73   the W-B option exposition, as a blockquote         REPLACE — restated as
                                                            THE SIGNED RESULT, not
                                                            as one of two offers
 74      blank                                             RETAIN
 75-76   "This document selects neither and predicts        REPLACE — FALSE after
          neither. Where the two differ, the text below      the signature. NO
          carries BOTH variants inside an explicitly         MARKER; v1 left it.
          delimited block:"
 77      blank                                             RETAIN
 78      "```text"                                         DELETE with 79-81
 79      "    [W-A]   … text operative only if W-A is       DELETE — notation
          signed …"                                          example
 80      "    [W-B]   … text operative only if W-B is       DELETE — notation
          signed …"                                          example
 81      "```"                                              DELETE with 78-80
 82      blank                                             DELETE with 78-81
 83-85   "A [W-A]/[W-B] block is not operative text in      REPLACE — the
          either direction until the cell is signed. At      convention sentence.
          signature exactly one branch of every such block   Carries BOTH markers.
          is retained and the other is deleted, in step
          OR-4 ..."
 85-88   "... of the atomic handoff, whose H-1..H-4 are     RETAIN IN SUBSTANCE
          stated once in the canonical delimited block at    inside the replacement
          §P1-14.8 ... ; no author closure states that
          step or any other."
 88-91   "The resulting file carries no variant block at    REPLACE — restated in
          all. A build extracted from a file that still      the PERFECT tense: no
          contains a variant block is not conforming and     variant block exists,
          the verifier refuses it (G-10, §P1-14.4)."         and G-10 confirms it
 92      blank                                             RETAIN
 93-95   "Every other part of the interface repair is       RETAIN, marker-free
          complete, and the rest of this composite is a      and still true
          finished replacement for v1.2 ..."
```

**THE REQUIRED POST-RESOLUTION RESULT, STATED AS THE PROPERTY AND NOT AS
PROSE.** The replacement text for lines 55, 57–58, 60–62, 64–73, 75–76, 78–83
and 88–91 must, taken together, satisfy all six of:

```text
CT-1  IT STATES THAT THE CELL IS SIGNED, names the exact selected token
      I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS, and names
      the signature path and digest ffcb4116…a7dc.
CT-2  IT STATES THAT W-A IS REJECTED, by name, as a historical fact about the
      choice — and states NO W-A CAPABILITY. No sentence describes a
      freeze-request socket, a slot-6 endpoint grant to the watchdog, a
      t-wd-freeze.v1 frame or a bounded service window as something the watchdog
      holds, may hold or could hold.
CT-3  IT CONTAINS NO ASSERTION THAT THE CELL, THE MECHANISM OR THE CHOICE IS
      OPEN, UNSIGNED, UNDECIDED, UNPREDICTED OR CARRIED IN BOTH DIRECTIONS.
      This is checked by PO-9, which is a CONTENT check and not a marker count.
CT-4  IT CONTAINS NO VARIANT-MARKER STRING, and no notation example that would
      reintroduce one.
CT-5  IT LEAVES CELL 1 UNTOUCHED. The process-claim identity cell is a separate
      cell, is NOT discharged by this signature, and its blocking notice stands
      unchanged. OR-4 edits no byte of Cell 1.
CT-6  IT ADDS NO NORMATIVE RULE. The replacement is a status statement. It
      introduces no predicate, no constant, no path, no count and no obligation
      that is not already stated in a normative region.
```

**No replacement text is written by this binding.** The transformation is
specified; `OR-4` performs it, and `OR-4` is not authorized.

### §2.3 The body locus table

`RESOLVE` = retain the `[W-B]` text inline, without its marker, and delete the
`[W-A]` text. `RETAIN` = leave the bytes untouched.

```text
#   LINE  REGION     OWNING SECTION                   ACTION   NOTE
 1    79  PREAMBLE   Cell 2 notation example          §2.2     deleted
 2    80  PREAMBLE   Cell 2 notation example          §2.2     deleted
 3    83  PREAMBLE   Cell 2 convention sentence       §2.2     BOTH markers; replaced
 4   305  BODY       §P1-1.3 six signed choices       RESOLVE  W-A "additionally signals the loss by requesting the freeze" deleted
 5   306  BODY       §P1-1.3 six signed choices       RESOLVE  W-B "The watchdog requests nothing" retained
 6  1656  BODY       §P1-9.2 property 11              RESOLVE  W-B rationale retained
 7  1659  BODY       §P1-9.2 property 11              RESOLVE  W-A G-1/PEER_ENDPOINT_LIVE rationale deleted
 8  1666  BODY       §P1-9.2 property 12              RESOLVE  W-A "sends exactly one t-wd-freeze.v1 on slot 6" deleted
 9  1670  BODY       §P1-9.2 property 12              RESOLVE  W-B "It sends nothing" retained
10  1907  BODY       §P1-10.6 negative surface        RESOLVE  W-A "one further P1-layer operation is permitted" deleted
11  1910  BODY       §P1-10.6 negative surface        RESOLVE  W-B "No further operation of any kind is permitted" retained
12  1932  BODY       §P1-10.7 classifier TRIGGER      RESOLVE  W-B "loss of the peer control endpoint, record-first" retained
13  1933  BODY       §P1-10.7 classifier TRIGGER      RESOLVE  W-A ACCEPTED-record-in-bounded-window trigger deleted
14  2531  BODY       §P1-13.0 residence matrix        RESOLVE  BOTH markers on one line; W-A slot-6 socket clause deleted, W-B "It holds no socket" retained — EDIT IN PLACE
15  2814  BODY       §P1-13.2 P1-invariant row        RESOLVE  W-B TWO SEALED PIPES, "Slot 6 is not used and is explicitly closed by a file action", retained
16  2820  BODY       §P1-13.2 P1-invariant row        RESOLVE  W-A THREE SEALED ENDPOINTS block deleted, with its AF_UNIX/SOCK_SEQPACKET socketpair and FD_CLOEXEC clause and its slot-6 request description
17  6747  BODY       §P1-15 test row 61               RESOLVE  BOTH markers; W-B classifier-and-terminal clause retained — EDIT IN PLACE
18  6775  BODY       §P1-15 test row 89               RESOLVE  BOTH markers; site (b) trigger fixed to the endpoint-loss site — EDIT IN PLACE. THE KV/SC CLAUSES AND THE ADVERSARIAL SCOPE FIXTURES ARE OPTION-INDEPENDENT AND ARE RETAINED IN FULL
19  6786  BODY       §P1-15 test row 99               RESOLVE  BOTH markers; descriptor set fixed to {0,1,2}+{3,4,5,7,8,9,10}, slot 6 closed — EDIT IN PLACE. The W-A branch's SOCK_SEQPACKET/S_ISSOCK description is deleted with it
20  6885  GUARDDATA  §P1-17 VARIANT_MARKER class      RETAIN   the two pattern strings; NEVER a match target; H_GUARDDATA must not move
```

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
      still present exactly once each. THE CORRECT ACTION AT LINE 6885 IS TO
      CHANGE NOTHING.

PO-4  THE PERMITTED-OCCURRENCE TABLE. See §2.5. It REPLACES v1's PO-4, which
      both independent lines found UNSATISFIABLE: v1 required zero whole-file
      occurrences of strings that TS-1 and the guard data are REQUIRED to carry.
      NO WHOLE-FILE "ZERO W-A STRINGS" RULE EXISTS IN THIS BINDING.

PO-5  W-B INVARIANTS POSITIVELY PRESENT, derivable from the resolved bytes with
      no variant marker anywhere in the derivation:
        a. the watchdog descriptor set is {0,1,2} + {3,4,5,7,8,9,10}, slot 6
           absent, two sealed pipes                                  (row 99)
        b. §P1-9.2 property 12: writes nothing, freezes nothing, signals
           nothing, sends nothing, exits
        c. §P1-10.6: no further operation of any kind is permitted
        d. §P1-10.7 TRIGGER: loss of the peer control endpoint, record-first
        e. row 89 site (b) is reachable only from the endpoint-loss trigger
        f. §P1-10.7's KG-1, KG-2, KV-1..KV-6 and SC-1..SC-8 are present in full
           and unmodified — they are OPTION-INDEPENDENT and OR-4 does not touch
           them

PO-6  SELECTION-TOKEN BINDING, AND THE CLOSED VOCABULARY THAT MUST SURVIVE.
      The resolved state carries the W-B token as the value bound across the two
      stages at B14, and TS-1's TWO literal option tokens AND BOTH paired
      option-specific amendment tokens MUST REMAIN. Deleting the non-selected
      literals breaks TS-2A A8, TS-2A A9, TS-5 B14 and IR-13 row 47 in one
      stroke, leaving the option-set predicate with no set to validate against.
      A STRUCTURAL REINFORCEMENT THE v1 BINDING DID NOT STATE: TS-1 lives INSIDE
      the joint install and authorization block (composite lines 3273..6391,
      digest 9bf4a831…abe5), which is byte-identical with amendment lines
      1324..4442. OR-4 edits the composite only. DELETING A TS-1 LITERAL WOULD
      THEREFORE ALSO DESTROY THE JOINT BLOCK'S BYTE IDENTITY, which a reviewer
      detects by diff. PO-6 is not a convention; a violation is mechanically
      visible.
      A CAUTION PO-6 SHOULD STATE AND v1 DID NOT: none of the twenty marker loci
      falls inside the joint block — the highest body locus before it is 2820
      and the next is 6747, straddling 3273..6391 without entering it — so a
      CORRECT OR-4 never touches TS-1 at all. PO-6 guards against an over-eager
      implementer, not against the specified procedure.

PO-7  DIGEST CONSEQUENCES, STATED SO THEY ARE NOT DISCOVERED LATE.
        H_GUARDDATA   UNCHANGED   (PO-3)
        H_BODY        CHANGES
        H_NORMATIVE   CHANGES
        H_FILE        CHANGES
      The composite H_FILE changes, therefore the §A0.4 pre-selection anchor
      value in the amendment — which equals the PRE-selection composite H_FILE
      c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6 —
      is NOT the post-OR-4 composite digest and MUST NEVER be updated to it.
      IR-11 and MS-12 already state this.

PO-8  AMENDMENT UNCHANGED BY MARKER RESOLUTION. Amendment v1.8 contains zero
      markers, so OR-4's marker work does not touch it. OR-4's separate clause
      "the v1.8 amendment is installed" concerns MS-1's first literal path and
      nothing else. THE v1.7 "v1.3 amendment" STALE STRING IS REPAIRED IN THE
      v2.11 GOVERNING BYTES; it was inside the joint block and therefore lived
      in BOTH files, which v1 of this binding got wrong.

PO-9  THE WHOLE-FILE-MINUS-GUARDDATA POST-RESOLUTION VERIFIER. See §2.6. This is
      what closes Y-M4 and X-2: it detects MARKER-FREE prose that still asserts
      an open cell or exposes a rejected W-A operative grant, which PO-2 cannot
      see.
```

### §2.5 `Y-M3` / `X-1` REPAIR — the canonical permitted-occurrence table

**Exact mechanical occurrence classes replace v1's semantic prose search.** Each
row names a region, the governing rule that requires or forbids the occurrence,
the literal fragment, and the expected count in the RESOLVED file.

```text
CLASS R — RETAINED, AND REQUIRED. Deleting any of these is a defect.

R-1  THE TS-1 OPTION-SET GRAMMAR. Region BODY, inside the joint block.
     fragment  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
     at        composite v1.11 line 5145 (TS-1 selected_option_token grammar)
     required by  TS-1's "EXACTLY ONE of the two EXISTING option tokens";
                  TS-2A A8; TS-5 B14; IR-13 row 47
     EXPECTED COUNT IN THE RESOLVED FILE: 1

R-2  THE TS-1 PAIRING RULE. Region BODY, inside the joint block.
     fragment  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
     at        composite v1.11 line 5151
     required by  TS-1's pairing grammar; TS-2A A9
     EXPECTED COUNT IN THE RESOLVED FILE: 1

R-3  THE CK-14 OPTION-MISMATCH FIXTURE. Region BODY, inside the joint block.
     fragment  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
     at        composite v1.11 line 6059, as the Stage-B value of the fixture
     required by  CK-14's executable conformance fixture, which EXISTS to prove
                  that a twelve-check implementation admits a W-A Stage B
     EXPECTED COUNT IN THE RESOLVED FILE: 1
     NOTE  THIS ROW IS NEW IN v2.11 AND v1 OF THIS BINDING COULD NOT HAVE HAD
           IT. Any "zero W-A token" rule would now also delete the fixture that
           protects the signed selection.

R-4  THE GUARD DATA MARKER PATTERNS. Region GUARDDATA.
     fragments  "[W-A]"   "[W-B]"      at composite v1.11 line 6885
     required by  §P1-17; §P1-14.3 AD-1; G-10's own text; G-6 against H_GUARDDATA
     EXPECTED COUNT IN THE RESOLVED FILE: 1 each, byte-identical, region digest
                  faf2d709…0426 unchanged

R-5  THE LEGITIMATE SUPERVISOR/PCS SOCKET AND SLOT-6 CLAUSES. Region BODY.
     These are NOT watchdog grants. They are the supervisor's control channel,
     common to BOTH options and untouched by the W-B choice.
       line  395  "T_ROLE_FD_ROLESRC = 5     slot 6 is role-class specific"
                  a general descriptor-table note, option-independent
       line 1352  the supervisor's AF_UNIX / SOCK_SEQPACKET protocol-0 pair
                  "inherited to slot 6" — a GRANTING clause, for the SUPERVISOR
       line 1354  "SOCK_SEQPACKET is chosen because it is connection-oriented"
       line 6728  row 42: "the peer reaches the supervisor role at slot 6 and
                  nowhere else"
       line  601  "from _socket : _socketpair _CMSG_SPACE _CMSG_LEN"  §P1-3.4
       line  606  "_AF_UNIX _SOCK_SEQPACKET"                          §P1-3.4
       line  847  "_socketpair, whose descriptors CPython creates
                  non-inheritable"                                    §P1-6.x
     EXPECTED COUNT IN THE RESOLVED FILE: all seven present and unchanged
     v1's U-5 WOULD HAVE FAILED ON AT LEAST THREE OF THESE. Both independent
     lines said so; the X line enumerated 392 / 1349 / 6344 in v1.10's numbering,
     which are 395 / 1352 / 6728 here.

R-6  WATCHDOG SLOT-6 REFERENCES IN THEIR CLOSED / ABSENT SENSE ONLY.
       line 2814..2817  §P1-13.2 [W-B] branch: "Slot 6 is not used and is
                        explicitly closed by a file action; the watchdog holds
                        no socket"
       line 6786        row 99 [W-B] branch: "{0,1,2} together with
                        {3,4,5,7,8,9,10}, slot 6 explicitly closed"
     EXPECTED COUNT IN THE RESOLVED FILE: exactly these two loci, each in its
     CLOSED/ABSENT sense, each with its [W-A] sibling deleted.
     A watchdog slot-6 occurrence in ANY OTHER SENSE IS FORBIDDEN by class F.

R-7  B14 AND IR-13 BINDINGS. Region BODY, inside the joint block.
     TS-5 B14, IR-13 row 35 (CK-14 / STAGE_B_OPTION_MISMATCH) and IR-13 row 47
     (CK-2 / STAGE_A_OPTION_INVALID) are RETAINED VERBATIM. OR-4 does not touch
     the joint block at all, so this is preserved by construction and is stated
     here because it is what PO-6 protects.

CLASS F — FORBIDDEN IN THE RESOLVED FILE. Expected count ZERO for each.

F-1  W-A OPERATIVE GRANTS AT OPERATIVE PREAMBLE OR BODY LOCI.
     Any sentence, in the Cell-2 preamble or in REGION(BODY) OUTSIDE the joint
     block, that describes the watchdog as holding, being able to hold, or being
     permitted to obtain a freeze-request socket, a slot-6 endpoint, a
     single-opcode capability, or any transport-request capability.
     LOCI THIS ELIMINATES: 64..68 (Cell-2 W-A exposition), 1659, 1666, 1907,
     1933, the [W-A] clause of 2531, 2820..2828, the [W-A] clauses of 6747 and
     6786.

F-2  THE W-A REQUEST SOCKET AND FRAME BEHAVIOUR.
     fragment  t-wd-freeze.v1
     EXPECTED COUNT IN THE RESOLVED FILE: 0.
     THIS FRAGMENT IS NOT IN TS-1's VOCABULARY AND IS NOT IN THE GUARD DATA, so
     unlike the two option tokens it CAN be, and must be, eliminated whole. Its
     nine v1.11 occurrences are at 66, 1660, 1666, 1908, 1933, 2531, 2828, 6747
     and 6775, and every one of them is inside a W-A branch or the Cell-2 W-A
     exposition.

F-3  W-A VARIANT BRANCH TEXT.
     Any surviving [W-A]-branch content at any of §2.3's nineteen non-guarddata
     loci, with or without its marker.

F-4  OPEN-CELL ASSERTIONS ABOUT CELL 2. See PO-9's detector in §2.6.

WHAT CLASS F DOES NOT COVER, STATED SO THE TABLE CANNOT BE MISREAD:
  the W-A OPTION TOKEN and the W-A OPTION-AMENDMENT TOKEN are NOT in class F.
  They are in class R at rows R-1, R-2 and R-3. THERE IS NO RULE IN THIS BINDING
  REQUIRING THEM TO OCCUR ZERO TIMES, AND ANY SUCH RULE WOULD CONTRADICT TS-1,
  IR-13 row 47 AND THE CK-14 FIXTURE.

TOTALS IN THE RESOLVED FILE, AND THE ARITHMETIC THAT PRODUCES THEM
  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
      pre-resolution occurrences in composite v1.11:  3
        line   64  Cell-2 W-A exposition   -> DELETED by §2.2
        line 5145  TS-1 option-set grammar -> RETAINED (R-1)
        line 6059  CK-14 fixture Stage-B   -> RETAINED (R-3)
      EXPECTED COUNT IN THE RESOLVED FILE: 2
  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
      pre-resolution occurrences: 1, at line 5151, TS-1's pairing rule
      EXPECTED COUNT IN THE RESOLVED FILE: 1   (R-2)
  t-wd-freeze.v1                  0   (F-2)
  "[W-A]" outside GUARDDATA       0   (PO-2)
  "[W-B]" outside GUARDDATA       0   (PO-2)
  "[W-A]" / "[W-B]" in GUARDDATA  1 each   (R-4)
  watchdog-sense "slot 6"         2 loci, both CLOSED/ABSENT   (R-6)
  supervisor-sense socket/slot-6  7 loci, unchanged            (R-5)
```

### §2.6 `PO-9` — the whole-file-minus-guarddata post-resolution verifier

**This is the check that closes `Y-M4` and `X-2`.** It is a **content** check,
not a marker count, and it runs over the whole file **minus** `REGION(GUARDDATA)`.

```text
INPUT   the resolved composite bytes
SCOPE   the whole file MINUS REGION(GUARDDATA), extracted by §P1-14.0
NORMALIZATION  §P1-14.2 NORMALIZE, so that case and whitespace cannot evade it

DETECTOR D1 — OPEN-CELL ASSERTIONS ABOUT THE WATCHDOG-FREEZE CELL.
  The resolved file must contain NO sentence asserting any of:
    that the watchdog-freeze mechanism cell is unsigned, open, unresolved or
      undecided;
    that this version is not acceptable as an operative object BECAUSE OF the
      watchdog-freeze cell;
    that the document selects neither watchdog option, predicts neither, or
      carries both variants;
    that a [W-A]/[W-B] block exists, is not operative, or awaits a signature;
    that "what remains open" is the freeze mechanism.
  IMPLEMENTED AS a closed list of normalized phrase patterns held in the ORACLE,
  not in the composite — this binding adds NO normative surface to the governing
  bytes and NO new guard-pattern class. §P1-17 is unchanged and G-10 is
  unchanged.
  REQUIRED: zero matches.
  THE PATTERN LIST MUST BE DERIVED FROM THE PRE-RESOLUTION CELL-2 SPAN ITSELF,
  line by line over lines 55..95, so that every assertion the transformation is
  supposed to discharge has a corresponding detector. A pattern list that does
  not cover every REPLACE row of §2.2 is INCOMPLETE and the oracle must say so.

DETECTOR D2 — REJECTED W-A OPERATIVE GRANTS, INCLUDING MARKER-FREE PROSE.
  The resolved file must contain NO sentence granting or describing as available
  to the watchdog: a freeze-request socket; a slot-6 endpoint; a single-opcode
  capability; a t-wd-freeze.v1 frame; a bounded service window; or an
  ACCEPTED-request-driven classifier trigger.
  REQUIRED: zero matches.
  D2 MUST NOT FIRE ON class R. It is scoped to exclude:
    the joint install and authorization block, extracted by its own delimiters
      — TS-1's grammar, TS-1's pairing rule and CK-14's fixture live there and
      are REQUIRED;
    the Cell-2 REPLACEMENT's single historical sentence recording that W-A was
      the rejected option, which names the token and describes NO capability
      (CT-2);
    the seven supervisor-side loci of R-5.

DETECTOR D3 — CLASS-R PRESENCE. Every row of §2.5's class R is present with its
  expected count. A resolution that satisfies D1 and D2 by deleting a class-R
  occurrence FAILS D3.

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
does not exist.** It lets §2.2's transformation, §2.3's table, §2.4's invariants,
§2.5's census and §2.6's detectors be checked mechanically without touching a
governing or runtime path.

### §2A.1 What the oracle is

```text
O-1  INPUT. Byte copies of amendment v1.8 and composite v1.11, read from their
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
     environment variable.
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
      the PCS classifier, not KG-1, not KV-1..KV-6, not SC-1..SC-8, not the
      descriptor topology and not any process operation. Those are §H3 of the
      handoff and they are NOT implementable under any authorization that exists.
```

### §2A.3 What later authorized `OR-4` does that the oracle does not

```text
                                        ORACLE      AUTHORIZED OR-4
  produces resolved bytes                in memory   ON DISK at MS-1's second
                                                     literal path
  requires the acceptance token          no          YES — v1.8 accepted first
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
nor the handoff, nor the oracle produces composite v1.11 in post-selection form
at any path.

---

## §3. `B3` — the gate ledger, and the identity disposition

### §3.1 The total ledger, current state through `T`

**`X-3` REPAIR: gate 0 is new.** The v1 ledger recorded Cell 1's blocking notice
only as a reason to exclude identity code. It had no row for Cell 1 as a
precondition of the composite's operativeness, so a reader following gates
3 → 8 → 14 → OR-3 would not learn that Cell 1 blocks the destination.

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
      It costs nothing to record — every downstream gate is already NOT
      AUTHORIZED — and it makes the ledger total.

 1  W-B author selection (OR-2)                   COMPLETE         yes — this binding only
      token I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
      signature ffcb4116…a7dc, 2026-08-05, base 176d609

 2  This post-selection binding, v2               DRAFT            no
      awaiting bounded X/Y review against the v2.11 bytes

 3  Watchdog authority amendment v1.8 acceptance  NOT ACCEPTED     no
      token I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8
      unsigned; §4 states exactly what it will and will not do.
      THE v1.7 TOKEN IS RETIRED AND MUST NOT BE SIGNED: R1 and R2 changed the
      bytes it would have accepted.

 4  Process identity Option A selection           COMPLETE         no
      token I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
      signature 7a8ab2da…3d1f, 2026-08-04
      recorded at XS-1 as external author state, member of no class

 5  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1  NOT ACCEPTED     no
      must be reviewed and accepted SEPARATELY before Option A can become
      operative; §3.2 states the disposition in full

 6  The LATER COMBINED BINDING of XS-1            DOES NOT EXIST   no
      STATE: BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW, by XS-1(b)

 7  Fresh independent X/Y round on the v2.11 pair NOT PERFORMED    no
      the v2.11 governing pair has NOT been independently reviewed. Gate 3
      cannot open before it does.

 8  Inactive SCAFFOLD implementation              CANDIDATE        no
                                                  ELIGIBILITY ONLY
      the handoff v2 is a scope contract for INERT ORACLE AND DECLARATIVE
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
at all. They are enumerated separately only so a reader can see that none of
them is open.

### §3.2 The identity-token disposition, resolved from the bytes

**The question:** may the inactive scaffold include observation-only identity
code while `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` is unaccepted?

**The answer, and it is stricter than the fail-closed minimum:**

```text
NO CODE. NOT DISABLED CODE, NOT GATED CODE, NOT DUMMY-TESTED CODE. THE
IDENTITY-OBSERVATION SURFACE IS OUT OF SCOPE FOR THIS IMPLEMENTATION ENTIRELY,
AND THE REASON IS NOT CAUTION — IT IS THAT THE GOVERNING PAIR DOES NOT DEFINE IT.
```

```text
C-1  THE MECHANICAL FACT, RECOMPUTED AGAINST v2.11. The strings attested_pid and
     attested_pgid occur ZERO times in composite v1.11 and ZERO times in
     amendment v1.8. There is no schema, key, type, carrier, consumer or
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

**Why this does not block the W-B binding.** `§P1-10.7` computes the classifier's
scope **from the PCS's own handle table**, `SC-1` closes that candidate set, and
row 89 confirms it. The opaque `handle_id` remains the only addressable process
name under the signed Option A contract. **The W-B surface is identity-free by
construction**, so exclusion costs the W-B work nothing and invents nothing —
whereas blocking would conflate two cells that `N-4`, `N-13` and `XS-1` are at
pains to keep separate. **Exclusion is strictly stronger than the fail-closed
minimum: absence admits no gate to be flipped.**

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

**What no future step may do without a separate accepted token.** No install
path, no activation path, no verifier configuration, no manifest field and no
test fixture may make an identity observation operative, may set or default an
`attested_pid` or `attested_pgid`, or may treat the Option A signature as having
accepted the bounded weakening. The verifier's obligation if such a surface is
ever added is stated in the handoff: **refuse, before any production action.**

---

## §4. `B6` — the acceptance and authorization boundary

The only watchdog amendment acceptance token available after a fresh bounded X/Y
review round on the v2.11 bytes is:

```text
I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8
```

**The v1.7 token is retired.** `R1` and `R2` changed the bytes it would have
accepted, so signing it would accept a pair that no longer exists.

### §4.1 What that future token accepts

```text
A-1  THE TWO GOVERNING FILES AS ONE INDIVISIBLE UNIT — amendment v1.8 and
     composite v1.11, at the exact digests of §0.2, per H-1.
A-2  THE TWO DELIMITED BYTE-IDENTICAL REGIONS at their stated digests, and the
     narrowed identity claim that attaches to those two regions and to nothing
     else.
A-3  THE FIXED ACCOUNTING — MS-2 at 63, MS-3 at 7, MS-8 at 77, TS-3
     member_count 77, member classes 7, closed failure codes 25, pre-production
     checks 15 running CK-1..CK-15, M4 key set 21, IR-13 at 50 rows, MS-13
     element keys 6 with 8 effect booleans each, 32 effect assertions all false,
     4 project-import dependencies, 7 unexecuted module-scope branches, 71
     composite provenance rows, the 16-member generic_harness.py scoped
     allowlist, and the 89-row reachable_closure at CANON length 20534.
A-4  THE KG-1, KG-2, KV-1..KV-6 AND SC-1..SC-8 DEFINITION at §P1-10.7 as
     normative content of the composite.
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
      amendment; the composite's bytes do not move.
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
  (i)   an INACTIVE-SCAFFOLD AUTHORIZATION, permitting the inert oracle and the
        declarative contract module and their dummy tests to be written at the
        handoff's allowed paths;
  (ii)  a RUNTIME IMPLEMENTATION AUTHORIZATION, permitting the watchdog EOF
        route, the PCS classifier, the descriptor topology and the process
        operations to be written at all — see handoff §H11;
  (iii) a ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION, permitting OR-3..OR-11 to run
        once, together, in order.
NONE IS GRANTED BY THE ACCEPTANCE TOKEN, AND NONE IS GRANTED HERE.
```

---

## §5. `B5` — the provenance disposition, now performed

### §5.1 What changed since v1

v1 recorded the four `v2.9` rows as a **declared, auditable deferral** and
stated at `PR-2` and `PR-3` where they would enter. Both independent lines
confirmed `PR-2` and `PR-3` exactly, and the Y line added the operative
consequence: *because a v2.11 governing repair is required, that repair is the
first such actual next generation and must perform the accounting once.*

**v2.11 performed it.** The disposition is no longer a residual.

```text
                                       v2.10   v2.11
MS-2                                      55  ->  63
MS-3                                       7      7
MS-8 / TS-3 member_count                  69  ->  77
composite provenance region rows          63  ->  71
member classes                             7      7   only M2 grew
```

The eight rows, in `MS-2` order, each digest recomputed from disk:

```text
d5e1d4dbd7731bd6a154c423b36f41e60de771d5ff635423b608bba02d88640f  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_6_DRAFT.md
3ce26ba63ca1546ddd7c8422ccf5a4e71e05678e58d1f3deca18e24668e4c1ad  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_9.md
588fe8a23fd56a4366f920d4b1463d00ee3e7bd8bbc4cc1cbaca61b89a12f489  reviews/fable_officina_p1_watchdog_v2_9_independent_x_confirmation.md
6d83e9b2f082354917b134955d35b8b8f1fdf76761b368c8d34ffae3cd99cf66  reviews/sol_officina_p1_watchdog_v2_9_final_y_confirmation.md
4b7442bd1dafa1ff141212ac8cd59e94983f32633561b6396837ff0767aa48ff  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
86755531f5a7a5f11085802c3e6b5770f4ef5aa90d98ae1a62599348e11f0e8f  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
0998fce3b881e0d0d1947c450b442821047f040a4bdd4a987a1a091ece3a56f7  reviews/fable_officina_p1_watchdog_v2_10_targeted_x_confirmation.md
90fb9f9155926df89e9993de1146c05e279639469d7bf2a60c63c6419bc37e52  reviews/sol_officina_p1_watchdog_v2_10_targeted_y_confirmation.md
```

### §5.2 The disposition rules, carried and re-scoped

```text
PR-1  THE EIGHT ROWS ARE ALREADY IN. This generation's install enumerates 77
      members from MS-1..MS-7 alone, with MS-2 at its literal 63 and the TS-3
      member_count literal at 77. THE HANDOFF STILL TOUCHES NONE OF IT: no
      fixture, no test row, no manifest field and no member enumeration in the
      inactive scaffold may add, remove or reorder a row.
PR-2  OR-4 IS STILL NOT A GENERATIONAL ROUND. It produces the post-selection
      bytes of the SAME generation at MS-1's SAME two literal paths and replaces
      no document, so no row enters at OR-4, OR-6, OR-9 or OR-11.
PR-3  THE NEXT ACTUAL GENERATIONAL ROUND — one that REPLACES v1.8/v1.11 — adds
      its own four rows: the v1.8 amendment, composite v1.11 and that round's
      two independent confirmations. It does NOT re-add any of the eight.
PR-4  NEGATIVE TEST OBLIGATION. A fixture that enumerates 59, 69 or 73 members
      FAILS against this generation. So does one that enumerates 81. The
      handoff states this as a required negative test.
PR-5  THE TWO W-B BINDING REVIEWS ARE NOT M2 MEMBERS of this generation and were
      not substituted for the v2.10 pair-confirmation rows.
PR-6  NO HISTORICAL BYTE IS EDITED BY ANY OF THIS. The 55 rows MS-2 already
      carried are byte-unchanged; the eight are appended.
```

### §5.3 The two governing findings, and their state

```text
F1  MAJOR, FAIL-OPEN.  REPAIRED IN v2.11. See §2 of the packet and H-3 of the
    canonical block. The pre-production range is CK-1..CK-15 everywhere; the
    twelve-check range exists only in sentences that negate it; H-1..H-4 exist
    once, delimited, byte-identical, at digest ca2ff30b…a785; the identity claim
    is narrowed to two verified regions; and the option-mismatch fixture is
    stated executably at CK-14 in the joint block.
F2  MAJOR, NOT IMPLEMENTABLE.  REPAIRED IN v2.11. KG-1, KG-2, KV-1..KV-6 and
    SC-1..SC-8 are defined in full at composite §P1-10.7, re-derived from the
    current signed invariants with a source-trace table, total and fail-closed.
    §P1-10.7's SCOPE line and row 89 resolve to that definition and to nothing
    else. THE DEFINITION IS NOT AN IMPLEMENTATION AUTHORIZATION: the handoff
    still forbids writing the classifier, and gate 10 does not exist.
F3  MINOR.  REPAIRED. OR-4 now reads "the v1.8 amendment is installed", inside
    the joint block and therefore in BOTH files, and §A9's audit enumerates FIVE
    generation-scoped operative loci.
F4  MINOR.  REPAIRED. composite line 91 now reads §P1-14.4.
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
WATCHDOG AUTHORITY AMENDMENT V1.8 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

The exact selected token and the formal selection signature govern. This draft,
the companion handoff and every author closure are untrusted self-assessments
and are normative for nothing.
