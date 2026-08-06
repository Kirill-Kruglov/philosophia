# Officina P1 W-B post-selection binding v5 (draft)

**Author:** Claude Code Opus 5, **post-selection binding author only**. Not an
independent X-line or Y-line reviewer. **This draft selects nothing, accepts
nothing, installs nothing and executes nothing.**

This document is a **plan and contract for a transformation, not the
transformation itself.** It creates no resolved amendment, no resolved
composite, no key, no Stage A, no Stage B, no manifest, no attestation, no
signature and no install record. `T` is `NOT_ACTIVATED`; the programme claim is
`OPEN`.

**v5 REPLACES v4 WHOLLY, AND THE REASON IS THAT ITS INPUT MOVED.** v4 was
reviewed by two independent lines against the v1.10/v1.13 governing bytes. The
X line CONFIRMED and reproduced every figure of §2.2 byte-exactly; the Y line
returned four executable Majors against the GOVERNING PAIR, not against this
binding, and those Majors have now been repaired in composite v1.14 and
amendment v1.11. **Because the governing bytes changed, v4's eleven spans and
its full-output hash are RETIRED**: every source digest, the splice line
numbers, the byte arithmetic and the resolved output are functions of the input
file, and the input file is a different file.

**v5 IS A COMPLETE NEW TRANSFORM AND NOT A DELTA ON AN INVISIBLE INTERMEDIATE.**
Every source and replacement span is republished with exact bytes, length and
SHA-256; the splice order and its non-overlap verification are restated; the
expected complete output length and SHA-256 are pinned; every delimited-region
hash and byte-identity check is measured on the pinned output; and the guarddata
region is byte-unchanged.

**THE THREE X-LINE ITEMS THAT LANDED ON THIS BINDING ARE REPAIRED HERE.**

```text
X-L3  THE S7 DELETE-LITERAL TRANSCRIPTION WAS WRONG BY ONE BACKTICK. v4's
      §2.2.4 rendered the literal with a delimiter backtick, a SPACE, then
      "[W-A]" carrying only a CLOSING backtick. Applying v4's own stated
      delimiter rule to that transcription yielded a 276-byte string occurring
      nowhere in the source line. THE TRANSCRIPTION IS CORRECTED HERE SO THAT
      THE WRITTEN LITERAL ITSELF REPRODUCES, and its measured length and digest
      are published beside it. The X line noted the direction was fail-closed;
      it was, and it is now also correct.
X-L4  MP-1's PINNED DIGEST DID NOT REPRODUCE FROM THE PUBLISHED RECIPE. v4 said
      "insert, immediately before the sentence …, the paraphrase followed by one
      blank line", which does not fix the insertion point byte-exactly; the X
      line searched all 8,067 line boundaries under both payload orderings and
      reproduced none. §2.6.5 NOW PINS A UNIQUE WHOLE-LINE INSERTION ANCHOR, THE
      EXACT PAYLOAD BYTES, THEIR ORDER AND THE NEWLINE CONVENTION, and publishes
      the recomputed digest and length. **BOTH THE BEHAVIOUR AND THE BYTES ARE
      REQUIRED, AND NO KNOWN-FALSE DIGEST IS RETAINED AS INFORMATIVE.**
X-L5  L-X6 WAS RECORDED MORE NARROWLY THAN THE BYTES SUPPORTED — only c10, only
      getpgid. It is expanded to c10, c14 AND m3 and to BOTH operations at §2.8,
      and it is marked REPAIRED only because composite v1.14's R4 binds _getsid
      and _getpgid and the bytes now prove the complete surface is reachable.
```

Every mechanical result of v4 that the X line independently reproduced — the
region split, the marker census, the both-marker line set, the guard-data
retention rule, the `PO-6` / `IR-13` row 47 reasoning, the identity disposition
and the provenance disposition — is carried forward, **recomputed against
v1.14**, and stated again here.

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

The v2.14 generation. Every digest recomputed from disk at authoring time.

```text
5f2c74ff371f618039de705f21464454684da122f91e06c251e147bfc61d26be  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11_DRAFT.md
11c8963ac3cbd4c72a90b0a1f0fdc0fe3bfb35be84a974c3a2a953ec699bbdee  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_14.md
```

Composite region digests (§P1-14.0 extraction), **PRE-selection**:

```text
H_BODY       459875d377a5159914f9542ede35b7f7e09bff589d829a3d71e9d45061b165c0
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  090fccba7efc00ac0a086fe8002cc4145d827eaeeb2213188f177ec19f5dfd99
H_FILE       11c8963ac3cbd4c72a90b0a1f0fdc0fe3bfb35be84a974c3a2a953ec699bbdee
```

`H_GUARDDATA` is **byte-unchanged from v1.13 and from every generation that
carried it**. No guard pattern was added, removed or edited by the v2.14 round.

The two delimited byte-identical regions, extracted from both files and diffed
with zero difference. **THE LENGTHS BELOW ARE ACTUAL UTF-8 BYTE COUNTS.**

```text
canonical atomic-handoff preamble  7d5cd45363f197905f4b3d4e6fa1b470b4bb595ec00ea423775412459f340084    4168 UTF-8 bytes
joint install and authorization    5e8a30dde59074c5d91e89429f3aae45a0b6c74f6f83a8f6ac5c7480408eba30  224756 UTF-8 bytes
```

**BOTH REGIONS MOVED IN THIS GENERATION AND BOTH REMAIN BYTE-IDENTICAL ACROSS
THE PAIR.** The joint block carries the whole `MS-1`..`MS-9`, `CK-*`, `IR-*`,
`TS-*`, `OR-*` and `N-*` accounting surface, so R3's recount lands inside it;
the handoff preamble carries `H-1`, whose replacement sentence names the
superseded generation. Each was rebuilt once and copied into both files, so
their byte identity is a construction property here rather than an assertion —
and it is verified on the pinned output at §2.2.6 regardless.

The v2.14 author choice packet, hash-read target of `TS-2B` `A16(b)` and member
of nothing:

```text
successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_14_CORRECTION.md
```

Recorded as **external author state, not as a member and not as authority
here**, exactly as `XS-1` records it:

```text
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
```

The two reviews that licensed the v2.14 round and this re-issue:

```text
89e210430b617d88a67229df2beeff82c5c844f6de1da1d03b376b758d7cb0c2  reviews/fable_officina_p1_wb_v2_13_final_x_review.md
a4056f477bd631ca7b1b19292371de7afade367ecbfd2b1b090a1f95f79b4036  reviews/sol_officina_p1_wb_v2_13_final_y_review.md
```

**THE TWO LINES DIVERGED, AND THE FOUR Y MAJORS GOVERN**, because each of them
reproduces directly from the governing bytes. An X-line confirmation does not
neutralize a Y-line counterexample against the same bytes, and the v2.13 X
review said so in terms.

### §0.3 What this document is not

```text
IT IS NOT the resolved amendment and NOT the resolved composite. It creates
  neither, and §2A states the exact boundary against OR-3 and OR-4.
IT IS NOT the LATER COMBINED BINDING named at XS-1(a)..(d). It does not resolve
  the process-claim identity cell, does not bind the identity signature into any
  member class, and does not re-derive any identity field. §3 states this in
  full and it is load-bearing.
IT IS NOT an amendment acceptance. The v1.11 acceptance token is unsigned.
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
REMAIN IN TS-1's CLOSED VALIDATION VOCABULARY AND ARE NOT DELETED (§2.6 PO-6):
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
    group stops — under KV-1..KV-6 and SC-1..SC-10, IN ONE GLOBAL SIX-PHASE
    ORDER, now DEFINED IN FULL at §P1-10.7 of composite v1.14, over the ONE
    CANONICAL STAT_PARSE of §P1-10.3.
      composite §P1-10.7 TRIGGER, [W-B] branch
      composite §P1-15 row 89, [W-B] branch

S4  NO TRANSPORT FRAME EXISTS ON THIS BRANCH. No t-wd-freeze.v1 record is
    emitted, received, accepted, journalled or witnessed on any path. The W-A
    bounded service window does not exist on this branch.

S5  NO DURABLE OBJECT, NO EVIDENCE, NO SCIENTIFIC INPUT. The watchdog produces
    no durable object of any class and supplies no input to any scientific
    predicate. The classifier's journal state — its three terminals, its two
    terminal qualifiers, its SC-5 tokens and its freeze_ns — is P1-owned
    process-control material and never reaches a peer artifact, an acceptance
    predicate, a qualification, a comparison, a Q or C fact, or any published
    record.
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
  OWNING LOCI  composite §P1-10.3 (STAT_READ, STAT_PARSE, KG_GROUP_ADMISSIBLE)
    and §P1-10.7 including its KG-1, KG-2, KV-1..KV-6 and SC-1..SC-10
    sub-block; §P1-15 rows 89 and 101
  WHAT W-B FIXES  the TRIGGER, and only the trigger: loss of the peer control
    endpoint, record-first. The W-A trigger is deleted.
  RESOLVED SINCE v4  v1.13's PHASE 4 selected its terminal per entry in table
    order while carrying TWO terminal-bearing predicates, so one table returned
    two different terminals under two permutations (Y-M1); and KG-2's P-2 and
    P-10 gave opposite answers on an ordinary AWAIT_STOP/TIMEOUT route (Y-M2).
    v1.14 makes every terminal-bearing phase a CLOSED SCAN FOLLOWED BY A TOTAL
    PHASE-LOCAL REDUCTION under an explicit intra-phase precedence, and makes
    KG-2 population conditional on outcome == STOPPED under a pinned step order.
    v1.14 also BINDS _getsid AND _getpgid at §P1-3.4 (Y-M4), which is the only
    primitive-surface change of this generation. The fence is lifted for the
    DEFINITION, not for implementation (§H10 of the handoff still forbids
    writing the classifier).
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
NB-6  IT DOES NOT CHANGE THE v2.14 GOVERNING BYTES. Every count, digest and
      rule above is READ from them.
NB-7  IT DOES NOT AUTHORIZE THE TWO NEW BOUND PRIMITIVES TO BE CALLED. R4 of the
      governing pair binds _getsid and _getpgid and pins their semantics; this
      binding neither implements nor invokes them, and §2A O-11 already forbids
      every process-control operation in the oracle.
```

---

## §2. The complete option-resolution contract

### §2.1 The mechanical census, recomputed against composite v1.14

```text
MARKER-BEARING LINES, composite v1.14           20
MARKER-BEARING LINES, amendment v1.11            0
  the amendment contains the two marker strings ZERO times; every variant block
  lives in the composite, and OR-4 therefore edits ONE file
"[W-A]" OCCURRENCES, composite                  13
"[W-B]" OCCURRENCES, composite                  13
BOTH-MARKER LINES, WHOLE FILE                    6   83, 3972, 8205, 8233, 8244, 8343
BOTH-MARKER LINES, BODY ONLY                     4   3972, 8205, 8233, 8244
```

**THE CENSUS IS STRUCTURALLY IDENTICAL TO v1.13's AND EVERY LINE NUMBER MOVED.**
That is the whole reason v4's span table could not be carried forward: the loci
are the same loci, at different offsets, inside a different file.

Region sentinels in composite v1.14:

```text
OFFICINA-P1-BODY-BEGIN          line   252
OFFICINA-P1-BODY-END            line  8303
OFFICINA-P1-GUARDDATA-BEGIN     line  8305
OFFICINA-P1-GUARDDATA-END       line  8346
OFFICINA-P1-PROVENANCE-BEGIN    line  8348
OFFICINA-P1-PROVENANCE-END      line  8561
```

```text
REGION      LINES  A   B   OBLIGATION AT OR-4
  PREAMBLE      3   2   2   outside G-10's match range. RESOLVED BY §2.2's
    (1..251)                SPAN S1, whose exact bytes are pinned there and
                            which covers the WHOLE Cell-2 notice, not only
                            these three lines
  BODY         16  10  10   G-10's exclusive match range. RESOLVED BY §2.2's
    (253..8302)           SPANS S2 THROUGH S11, each of which is pinned by
                            exact source bytes and exact replacement bytes
  GUARDDATA     1   1   1   THE PATTERN SOURCE. RETAIN BYTE-IDENTICAL. Never a
    (8306..8345)           match target; deleting it destroys G-10 and changes
                            H_GUARDDATA
  ---------------------------------------------------------------------------
  TOTAL        20  13  13
```

### §2.2 THE COMPLETE TRANSFORMATION, EVERY SPAN PINNED AGAINST v1.14

**Why the whole table is republished rather than patched.** v4 pinned eleven
spans against composite v1.13 and the X line reproduced every one of them
byte-exactly. R1 through R4 then changed composite bytes at §P1-3.4, §P1-3.5,
§P1-7.5, §P1-10.3, §P1-10.7, the whole `MS`/`CK`/`IR`/`TS`/`OR` accounting
surface and test rows 89 and 103..115. **Nine of the eleven spans carry
byte-identical SOURCE content at NEW LINE NUMBERS; two do not** — `S1`, because
the Cell-2 notice names the superseded version, and `S10`, because test row 89
gains R1's and R2's and R4's conformance clauses. **The full-output length and
digest change for all eleven.** A delta would have described an intermediate
file that exists nowhere, so the complete transform is stated here.

**v5 pins the whole transformation.** There are exactly **ELEVEN SPANS**, they
are pairwise non-overlapping, they are applied in ONE deterministic order, and
the **complete resolved output** carries a pinned byte length and a pinned
SHA-256. Nothing outside the eleven spans is touched.

#### §2.2.1 The span table — exact source identity and exact transformation

Every span is identified by **whole-line sentinels**, never by line numbers; the
line numbers below are informative and move with every generation — and in this
generation every one of them did. `SRCLEN` and `REPLEN` are UTF-8 byte counts
including every `0x0A`.

```text
SPAN  OWNING SECTION                          LINES  SRCLEN  SOURCE SHA-256
      REPLEN  REPLACEMENT SHA-256
---------------------------------------------------------------------------
S1    Cell 2, the whole author-cell notice    55..95    2184
      db66c3ad454a9d4b3cba2e530e54348e02598c87bc824326679969d8a15071e8
      2120  dca85c8dae2e6cc435fee2d3bed981bf95728ad694175af7a60ab83d1e7d3af4
S2    §P1-1.3 the six signed choices         306..307     163
      86d71bcdc7350e977e9f80932bbf155ec535688ac5adbcfda1fecdd58bb92230
        61  fc9dd4e6ac6b5384ecb7bf1cbf6ccee407d41456ff40fbdd7cdcaa7cf9af6901
S3    §P1-9.2 property 11, getppid           1768..1775     598
      2c32d95b7c09dce20b5c6c46dc7071877ed12dfd569a4ed988607e43cee1faf3
       207  839ca35d35a1f3a17de9209721d1cd51a65f110aa7d06d7805f7819263d5723c
S4    §P1-9.2 property 12, the EOF route     1778..1782     298
      563875704d64fb343bbc61c9414e9473ff0a79d87e244c2f2dbd156cd72e410e
        22  7fdc2f4f305adb0895c0b6803f6dd7d43d1bfc9f776484294a549637fa4d878c
S5    §P1-10.6 the negative surface          2266..2269     299
      31a3d866a0dfd3854965f4b064fc8c034f958c6f9f99d794ebeeb74e96c8e1c3
        47  e60732e9219460a1cd9108862be6d29918558cfb12bb46ce3a4e250be7a4b0fa
S6    §P1-10.7 the classifier TRIGGER        2291..2293     218
      fb396762d308a44d0e6dc1e011ced63bcd270a1e1fb5d6f759bf262b9eac9292
        61  78ea5f796aa53acdda9a72d62dd9932d1c3324ef0ddf5881116a3c3f830c801d
S7    §P1-13.0 residence matrix, watchdog       3972     982
      a33c284ebd09f4177ae8aff88409a26d8df27d38f5e440a9a9bdda4593d8fed1
       727  bc68506c9c96db05688bdd76c98d78c21076e1d59e35655b1c2bbe70971ecd6b
S8    §P1-13.2 row 4, the P1 invariant       4255..4272    1329
      dbbf9cbfaacd6edb0dd467a7cff908894768a287cd906cc24f07d297777baa39
       440  bce8b980a104af6fbf186826fa41263667935bf27f17e56031f3209703100650
S9    §P1-15 test row 61                        8205     504
      496d4747775c288bf021b16737857c35e25411319d08781027421d263905849c
       271  55a62571cfce5192b9380a576639102663b1f836a0ac14460fec983dc071315b
S10   §P1-15 test row 89                        8233   14213
      630aa89ad46347371e53baa8fc3a9b727d00dbf8ef77d841ba1e8461138dba6e
      14123  d638ba7d59f5e47ebcbdbcad6aae10e86624857104877c541a4c7be47c3ab882
S11   §P1-15 test row 99                        8244     449
      75ed6f6f747c8b7a8119c985d788f27e5e4b94538c7575ecc85d5913043d47e2
       315  37b63dcd369696ad6046e64e3bb4f32e89dd455809d4395d897559273203a539
---------------------------------------------------------------------------
ELEVEN SPANS. 3 preamble marker loci inside S1, 16 body marker loci across
S2..S11, 1 guarddata locus RETAINED UNCHANGED. 3 + 16 + 1 = 20, which is the
census of §2.1 exactly.
```

**THE SENTINELS, WHOLE-LINE AND EACH OF CARDINALITY EXACTLY ONE.** For a
multi-line span the first and last sentinels bound it inclusively; for a
single-line span (`S7`, `S9`, `S10`, `S11`) the one sentinel is a unique line
PREFIX, stated as such.

```text
S1   FIRST  ### Cell 2 — `AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM`, new in v1.3
     LAST   decisions — whichever way they go — land in a document that is otherwise ready.
S2   FIRST  `[W-A]` The watchdog additionally signals the loss by requesting the freeze the
     LAST   PCS executes. `[W-B]` The watchdog requests nothing. Its complete set of operative
S3   FIRST      `[W-B]` The watchdog executes no freeze on any path, so no misuse of
     LAST       inference is FALSE, not because of what it would trigger;
S4   FIRST      `[W-A]` Before exiting it sends exactly one constant `t-wd-freeze.v1` record
     LAST       `[W-B]` It sends nothing;
S5   FIRST  [W-A] One further P1-layer operation is permitted: emitting exactly one constant,
     LAST   [W-B] No further operation of any kind is permitted.
S6   FIRST  TRIGGER      [W-B] loss of the peer control endpoint, record-first
     LAST                      window; on window end without one, NO freeze occurs
S7   THE UNIQUE LINE BEGINNING  | watchdog role process | PCS `SPAWN_WATCHDOG`
S8   FIRST  P1 invariant         [W-B] P1 provides the watchdog role process and its TWO
     LAST                        artifact.
S9   THE UNIQUE LINE BEGINNING  | 61 | supervisor death produces update-pipe EOF
S10  THE UNIQUE LINE BEGINNING  | 89 | **wrong freeze writer,
S11  THE UNIQUE LINE BEGINNING  | 99 | **endpoint count and type.**
```

**CARDINALITY IS CHECKED BEFORE ANYTHING IS SPLICED.** Each sentinel, and each
prefix, matches EXACTLY ONE line of composite v1.14 under whole-line equality
(for a sentinel) or whole-line prefix equality (for a prefix). A count of zero,
or of two or more, **FAILS CLOSED and `OR-4` does not proceed.** Each span's
source SHA-256 is then verified against the table above, and a mismatch **FAILS
CLOSED**.

#### §2.2.2 The replacement bytes for `S1`

**EXTRACTION RULE, STATED SO THE FENCE MARKUP IS EXCLUDED.** The replacement
bytes are the concatenation of the lines lying **strictly between** the opening
fence line and the closing fence line of the single `REPLACEMENT-BYTES-S1` block
below, each line including its `0x0A`. The two fence lines themselves are markup
of this document and are **not** part of the bytes. No line of the replacement is
a fence line, so the closing fence is the first subsequent line equal to three
backtick characters.

```REPLACEMENT-BYTES-S1
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
composite is a finished replacement for version 1.13, so that the signed
decisions land in a document that is otherwise ready.
```

```text
REPLACEMENT LENGTH   37 lines, 2120 UTF-8 bytes
REPLACEMENT SHA-256  dca85c8dae2e6cc435fee2d3bed981bf95728ad694175af7a60ab83d1e7d3af4
ENCODING             UTF-8, no BOM, LF line endings, final byte 0x0A
NON-ASCII CHARACTERS the block contains U+2014 EM DASH at TWO loci and U+00A7
                     SECTION SIGN at FIVE loci, and no other non-ASCII
                     character. THE X LINE's L-X1 IS REPAIRED HERE: v3's
                     sentence said "the U+2014 EM DASH at two loci and no other
                     non-ASCII character", which was FALSE against the bytes it
                     described. It was never an executable defect — the SHA-256
                     is the sole verification of the block and it reproduces —
                     but it was a false audit sentence and it is corrected
                     rather than carried.
DIFFERENCE FROM v4's BLOCK, AND IT IS EXACTLY ONE LINE: the final paragraph now
                     reads "a finished replacement for version 1.13" where v4's
                     read "version 1.12", because the generation moved. That is
                     why this block's digest differs from v4's bd725ddd… value.
                     THE SOURCE SPAN ALSO MOVED BY THE SAME ONE LINE, which is
                     why S1's SOURCE digest differs from v4's 83714544… value
                     while its length is unchanged at 2184.
```

#### §2.2.3 The replacement bytes for `S2` through `S6` and `S8`

Same extraction rule as §2.2.2, one fenced block per span.

```REPLACEMENT-BYTES-S2
The watchdog requests nothing. Its complete set of operative
```

```REPLACEMENT-BYTES-S3
    The watchdog executes no freeze on any path, so no misuse of
    `getppid()` can produce a freeze at all; the prohibition stands because the
    inference is FALSE, not because of what it would trigger;
```

```REPLACEMENT-BYTES-S4
    It sends nothing;
```

```REPLACEMENT-BYTES-S5
No further operation of any kind is permitted.
```

```REPLACEMENT-BYTES-S6
TRIGGER      loss of the peer control endpoint, record-first
```

```REPLACEMENT-BYTES-S8
P1 invariant         P1 provides the watchdog role process and its TWO
                     SEALED PIPES — the update read end at slot 3 and the ack
                     write end at slot 4 — for the supervisor-channel-liveness
                     function ONLY, and provides NO input to this record. Slot 6
                     is not used and is explicitly closed by a file action; the
                     watchdog holds no socket.
```

**Trailing-space discipline, stated because it is exactly the class of ambiguity
`M-4` named:** no line of any replacement block above ends in `0x20` or `0x09`,
every line ends in exactly one `0x0A`, and the pinned `REPLEN` and SHA-256 of
each span in §2.2.1 is the acceptance criterion. An implementation whose output
differs from the pinned digest by one space **FAILS CLOSED**.

#### §2.2.4 The four single-line spans, pinned as exact substring replacements

`S7`, `S9`, `S10` and `S11` are single physical lines carrying **both** markers,
which is why v3's "edit in place" prose was not identifiable. Each is pinned here
as ONE exact substring replacement inside ONE uniquely identified line. The
containing line's whole source SHA-256 and whole replacement SHA-256 are in
§2.2.1, so both the edit and its result are byte-pinned.

```text
S7   IN THE UNIQUE LINE BEGINNING "| watchdog role process | PCS `SPAWN_WATCHDOG`"
     DELETE, as one exact contiguous substring, 277 UTF-8 bytes,
       SHA-256 1f8cd74f65b97fa67d58ca9a196ec2388b97eb10e5af00732b1a0cfc10147232
       `` `[W-A]` It additionally holds one single-opcode, target-free freeze-request socket at slot 6 over which it may emit exactly one constant `t-wd-freeze.v1` record; that record is a P1 transport frame, not a peer-owned record, and is never evidence. `[W-B]` It holds no socket. |``
     THE X LINE's X-L3 IS REPAIRED IN THAT LINE. v4 delimited this literal with
     ONE backtick at each end, which is ambiguous for a literal whose own FIRST
     byte after the leading space is a backtick: the rendering collapsed to a
     276-byte string occurring nowhere in the source. THE LITERAL IS NOW
     DELIMITED BY TWO BACKTICKS AT EACH END, so the written literal itself
     reproduces at its stated length and digest and not only its containing
     line's digest does.
     INSERT in its place, 22 UTF-8 bytes,
       SHA-256 523a0dd8e7266f1da09379e8684291b3ec27e87a36e991ac24b031a96e8d9a9c
       ` It holds no socket. |`
     THE DELETED SUBSTRING BEGINS WITH ONE 0x20 AND THE INSERTED ONE BEGINS WITH
     ONE 0x20, so the byte before "[W-A]" and the byte before "It" are the same
     byte and no double space and no lost space can arise.

S9   IN THE UNIQUE LINE BEGINNING "| 61 | supervisor death produces update-pipe EOF"
     DELETE, as one exact contiguous substring, 352 UTF-8 bytes,
       SHA-256 b14fbde31cd1b8d85e7290adbdc8503b4cdf37508812d6c7a695aaff5f7044bd
       ` `[W-B]` Loss of the peer control endpoint additionally produces the PCS's record-first §P1-10.7 classifier and its terminal. `[W-A]` Loss of the peer control endpoint additionally produces the PCS's bounded service window; an `ACCEPTED` `t-wd-freeze.v1` record produces the classifier and its terminal, and window end without one produces no freeze |`
     INSERT in its place, 119 UTF-8 bytes,
       SHA-256 09d3b27d6245f777f49cbdab3ca6904ff31552173f3b27fa3065d48cef7f8699
       ` Loss of the peer control endpoint additionally produces the PCS's record-first §P1-10.7 classifier and its terminal |`

S10  IN THE UNIQUE LINE BEGINNING "| 89 | **wrong freeze writer,"
     DELETE, as one exact contiguous substring, 155 UTF-8 bytes,
       SHA-256 5b23c45a9fdae4607fad494e687252556da134836a931a9ac8f8799260b80007
       `reachable only from its own trigger site (`[W-B]` the endpoint-loss site; `[W-A]` an `ACCEPTED` `t-wd-freeze.v1` record inside the bounded service window).`
     INSERT in its place, 65 UTF-8 bytes,
       SHA-256 68257fda69e7d96d7d965bfd598a3e2a6c7c3fc49977c94867944eb5e6b6c8b6
       `reachable only from its own trigger site, the endpoint-loss site.`
     EVERY OTHER BYTE OF ROW 89 IS UNCHANGED. Its KV/SC clauses, its six-phase
     requirement, its counterexample fixtures, its permutation fixtures, its
     dominance-pair fixtures and its parser-vector fixtures are
     OPTION-INDEPENDENT and are RETAINED IN FULL.

S11  IN THE UNIQUE LINE BEGINNING "| 99 | **endpoint count and type.**"
     DELETE, as one exact contiguous substring, 337 UTF-8 bytes,
       SHA-256 fcdefe4c50970980e9e5b32b33e3112c00259b93aed4a85f8f7b325dd2bf086e
       `**endpoint count and type.** `[W-B]` the watchdog's `/proc/self/fd` is exactly `{0,1,2}` together with `{3,4,5,7,8,9,10}`, slot 6 explicitly closed — two sealed pipes. `[W-A]` exactly `{0,1,2}` together with `{3,4,5,6,7,8,9,10}`, with slot 6 `S_ISSOCK`, `O_RDWR`, `SOCK_SEQPACKET` — three sealed endpoints. In BOTH: no PCS descriptor`
     INSERT in its place, 203 UTF-8 bytes,
       SHA-256 9776e99c68fabc098f4b09e88f317cd3473a4b71a553fe7d4e56afa61921140f
       `**endpoint count and type.** the watchdog's `/proc/self/fd` is exactly `{0,1,2}` together with `{3,4,5,7,8,9,10}`, slot 6 explicitly closed — two sealed pipes. In the resolved branch: no PCS descriptor`
     "In BOTH:" BECOMES "In the resolved branch:" BECAUSE THERE IS NO LONGER A
     "BOTH". That is a required part of the transformation and not an
     implementer's choice; the pinned line digest fixes it.
```

**Backtick note, so the literals above are unambiguous.** Each literal is
delimited by one leading and one trailing backtick of this document, EXCEPT
`S7`'s deleted literal, which begins with a space followed by a backtick and is
therefore delimited by TWO backticks at each end — the CommonMark rule for a
code span whose content starts or ends with a backtick. Every backtick INSIDE a
literal is part of the bytes. The authoritative check is not
the transcription: it is the source SHA-256 of the containing line, the
replacement SHA-256 of the containing line, and the full-output SHA-256 of
§2.2.6, all three of which an implementation must reproduce.

#### §2.2.5 The one deterministic splice order

```text
RESOLVE(composite_bytes) -> resolved_bytes
  1. L := the lines of composite_bytes, split on 0x0A, each retaining its 0x0A
     except possibly the last.
  2. For each span S1..S11, locate its sentinel line or lines under §2.2.1's
     cardinality rule. ANY CARDINALITY OTHER THAN EXACTLY ONE FAILS CLOSED.
  3. For each span, form (b_i, e_i), the inclusive line index pair. VERIFY that
     SHA-256 of concat(L[b_i..e_i]) equals the span's pinned source digest. ANY
     MISMATCH FAILS CLOSED; OR-4 does not proceed against unexpected bytes.
  4. SORT the eleven spans by ASCENDING b_i. VERIFY e_i < b_{i+1} for every
     adjacent pair — THE SPANS ARE PAIRWISE NON-OVERLAPPING AND THE VERIFICATION
     IS PART OF THE ALGORITHM, not an assumption.
  5. Emit, in one left-to-right pass: the lines before b_1; replacement 1; the
     lines between e_1 and b_2; replacement 2; … ; replacement 11; the lines
     after e_11.
  6. VERIFY that SHA-256 of the emitted bytes equals §2.2.6's pinned
     FULL RESOLVED OUTPUT digest. A MISMATCH FAILS CLOSED.

THERE ARE EXACTLY ELEVEN REPLACED RANGES. NO OTHER BYTE OF THE COMPOSITE IS
TOUCHED, NO TWO RANGES OVERLAP AND THE ALGORITHM VERIFIES THAT THEY DO NOT, AND
NO IMPLEMENTER CHOOSES ANY BOUNDARY, ANY SENTENCE, ANY WORD OR ANY SPACE.
TWO CONFORMING IMPLEMENTATIONS GIVEN COMPOSITE v1.14 EMIT THE SAME COMPLETE BYTE
SEQUENCE — not merely normalized-equivalent output — because every input to the
algorithm is a literal fixed here and the output is pinned by a whole-file
digest.
```

#### §2.2.6 The complete resolved output, pinned

```text
INPUT     successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_14.md
          627683 UTF-8 bytes
          SHA-256 11c8963ac3cbd4c72a90b0a1f0fdc0fe3bfb35be84a974c3a2a953ec699bbdee

FULL RESOLVED OUTPUT
          624840 UTF-8 bytes
          SHA-256 9904ff3bf73f90329df7ac06fac5dbf4b211713964f610541761018c9bacb5c5

RESOLVED REGION DIGESTS
          H_BODY       731b4d662be269c8a67cb142ebb7fc5c38424bc91934ec40df54b10be18a677b
          H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
                       — UNCHANGED, byte for byte, from the pre-selection value
          H_NORMATIVE  313160d7c1fb240c43ef43bb5432c63a0391f60052648af8115b69aa67f2a268

BYTE ARITHMETIC, CHECKABLE WITHOUT RUNNING ANYTHING
          627683 − (2184+163+598+298+299+218+982+1329+504+14213+449)
                 + (2120+61+207+22+47+61+727+440+271+14123+315)
        = 627683 − 21237 + 18394 = 624840.

THE TWO DELIMITED REGIONS SURVIVE OR-4 BYTE-IDENTICALLY, VERIFIED ON THE PINNED
OUTPUT RATHER THAN ARGUED FOR:
          canonical atomic-handoff preamble  7d5cd453…0084  4168 bytes  UNCHANGED
          joint install and authorization    5e8a30dd…ba30  224756 bytes  UNCHANGED
          EACH WAS EXTRACTED FROM composite v1.14, FROM amendment v1.11 AND FROM
          THE RESOLVED OUTPUT BY ITS OWN TWO DELIMITER LINES AND COMPARED WITH
          ZERO DIFFERENCE, ALL THREE WAYS.
          No span intersects either. The highest body span before the joint
          block ends at line 4272 and the next begins at line 8205, straddling
          the joint block without entering it.

THESE FIGURES WERE COMPUTED IN MEMORY, OVER A COPY, IN A SESSION SCRATCHPAD.
NO RESOLVED BYTES WERE WRITTEN TO ANY REPOSITORY PATH, NO GOVERNING FILE WAS
MODIFIED BY THE COMPUTATION, AND NO OR STEP WAS PERFORMED.
```

### §2.3 What replaced the v3 body-locus table

**v3's §2.3 prose table is WITHDRAWN.** It listed twenty loci with semantic
actions and no bytes; §2.2 replaces it entirely. The mapping from the twenty
census loci to the eleven spans, kept only so a reviewer can confirm the census
still sums:

```text
LOCUS LINES (v1.14)          SPAN     DISPOSITION
79, 80, 83                   S1       inside the single Cell-2 span
306, 307                     S2       W-A clause deleted, W-B retained unmarked
1768, 1771                   S3       W-B rationale retained, W-A deleted
1778, 1782                   S4       W-A send-clause deleted, W-B retained
2266, 2269                   S5       W-A grant deleted, W-B retained
2291, 2292                   S6       W-B trigger retained, W-A trigger deleted
3972                         S7       BOTH markers on one line, substring edit
4255, 4261                   S8       W-B block retained unmarked, W-A deleted
8205                         S9       BOTH markers on one line, substring edit
8233                         S10      BOTH markers on one line, substring edit
8244                         S11      BOTH markers on one line, substring edit
8343                         —        GUARDDATA, RETAINED BYTE-IDENTICAL
```

### §2.4 The mechanical post-`OR-4` invariants

Stated so that each is a total function of the resolved file's bytes.

```text
PO-0  FULL-OUTPUT IDENTITY. THE PRIMARY CHECK, AND THE ONE THAT MAKES
      EVERY OTHER CHECK BELOW A CROSS-CHECK RATHER THAN THE CONTRACT.
        SHA-256 of the complete resolved bytes equals
        9904ff3bf73f90329df7ac06fac5dbf4b211713964f610541761018c9bacb5c5
        and the length equals 624840.
      A CANDIDATE THAT FAILS PO-0 IS WRONG, WHATEVER ELSE IT SATISFIES.

PO-1  MARKER ELIMINATION, BODY. Extract REGION(BODY) by the §P1-14.0 algorithm,
      apply §P1-14.2 NORMALIZE, count each pattern of the §P1-17
      VARIANT_MARKER class.
        REQUIRED: 0 and 0.   MEASURED ON THE PINNED OUTPUT: 0 and 0.
      This is exactly G-10 and it is the only one of these checks the shipped
      verifier performs. G-10 REMAINS BODY-SCOPED and is not widened here.

PO-2  MARKER ELIMINATION, WHOLE FILE OUTSIDE GUARD DATA.
        REQUIRED: 0 and 0.   MEASURED ON THE PINNED OUTPUT: 0 and 0.
      STRICTLY STRONGER than PO-1. It is NOT G-10 and must not be described as
      G-10. IT IS NECESSARY AND IT IS NOT SUFFICIENT — see PO-9.

PO-3  GUARD DATA PRESERVED. Recompute H_GUARDDATA over the extracted region.
        REQUIRED: exactly
        faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
      unchanged from the pre-OR-4 value, with the two VARIANT_MARKER patterns
      still present exactly once each. MEASURED: unchanged, 1 and 1. THE CORRECT
      ACTION AT LINE 7883 IS TO CHANGE NOTHING.

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
        e. row 89 site (b) is reachable only from the endpoint-loss site
        f. §P1-10.3's STAT_READ / STAT_PARSE / KG_GROUP_ADMISSIBLE and
           §P1-10.7's KG-1, KG-2, KV-1..KV-6 and SC-1..SC-10 are present in full
           and unmodified — they are OPTION-INDEPENDENT and NO SPAN TOUCHES THEM
           except S6, which edits only the TRIGGER lines

PO-6  SELECTION-TOKEN BINDING, AND THE CLOSED VOCABULARY THAT MUST SURVIVE.
      The resolved state carries the W-B token as the value bound across the two
      stages at B14, and TS-1's TWO literal option tokens AND BOTH paired
      option-specific amendment tokens MUST REMAIN. Deleting the non-selected
      literals breaks TS-2A A8, TS-2A A9, TS-5 B14 and IR-13 row 47 in one
      stroke, leaving the option-set predicate with no set to validate against.
      TS-1 lives INSIDE the joint install and authorization block, byte-identical
      with the amendment's §A10 block. OR-4 edits the composite only. DELETING A
      TS-1 LITERAL WOULD THEREFORE ALSO DESTROY THE JOINT BLOCK'S BYTE IDENTITY,
      which a reviewer detects by diff — and §2.2.6 VERIFIES that identity on the
      pinned output rather than arguing for it.

PO-7  DIGEST CONSEQUENCES, PINNED RATHER THAN MERELY NAMED.
        H_GUARDDATA   UNCHANGED   faf2d709…0426
        H_BODY        CHANGES to  731b4d66…677b
        H_NORMATIVE   CHANGES to  313160d7…a268
        H_FILE        CHANGES to  9904ff3b…b5c5
      The composite H_FILE changes, therefore the §A0.4 pre-selection anchor
      value in the amendment — which equals the PRE-selection composite H_FILE
      11c8963ac3cbd4c72a90b0a1f0fdc0fe3bfb35be84a974c3a2a953ec699bbdee —
      is NOT the post-OR-4 composite digest and MUST NEVER be updated to it.
      IR-11 and MS-12 already state this.

PO-8  AMENDMENT UNCHANGED BY MARKER RESOLUTION. Amendment v1.11 contains zero
      markers, so OR-4's marker work does not touch it. OR-4's separate clause
      "the v1.11 amendment is installed" concerns MS-1's first literal path and
      nothing else. **THAT CLAUSE IS A LITERAL THIS GENERATION HAD TO REPAIR:**
      v1.10's §A0 asserted it already read "the v1.10 amendment is installed"
      while the bytes of BOTH files read "the v1.9 amendment is installed". The
      author found it, neither independent line reported it, and composite v1.14
      and amendment v1.11 now carry "the v1.11 amendment is installed" inside
      the joint block and therefore in both files. **§2.5's class-R census
      verifies the current value on the pinned output rather than asserting
      it.**

PO-9  THE WHOLE-FILE-MINUS-GUARDDATA POST-RESOLUTION CONTENT DETECTOR. See §2.6.
      ITS CLAIM IS NARROWED IN v4 TO EXACT LISTED LITERAL COVERAGE.

PO-10 SPAN-LEVEL IDENTITY. Every one of the eleven spans, extracted from the
      resolved bytes at the position the splice placed it, hashes to the
      replacement SHA-256 §2.2.1 pins for it. This localizes a PO-0 failure to
      one span rather than reporting only that the file is wrong.
```

### §2.5 The canonical permitted-occurrence table

```text
CLASS R — RETAINED, AND REQUIRED. Deleting any of these is a defect.

R-1  THE TS-1 OPTION-SET GRAMMAR. Region BODY, inside the joint block.
     fragment  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
     at        the TS-1 selected_option_token grammar, inside the joint block
     required by  TS-1's "EXACTLY ONE of the two EXISTING option tokens";
                  TS-2A A8; TS-5 B14; IR-13 row 47

R-2  THE TS-1 PAIRING RULE. Region BODY, inside the joint block.
     fragment  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
     at        the TS-1 pairing rule, inside the joint block
     required by  TS-1's pairing grammar; TS-2A A9

R-3  THE CK-14 OPTION-MISMATCH FIXTURE. Region BODY, inside the joint block.
     fragment  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
     at        the CK-14 fixture, inside the joint block, as its Stage-B value
     required by  CK-14's executable conformance fixture, which EXISTS to prove
                  that a twelve-check implementation admits a W-A Stage B

R-4  THE GUARD DATA MARKER PATTERNS. Region GUARDDATA.
     fragments  "[W-A]"   "[W-B]"      at composite v1.14 line 8343
     required by  §P1-17; §P1-14.3 AD-1; G-10's own text; G-6 against H_GUARDDATA
     EXPECTED COUNT IN THE RESOLVED FILE: 1 each, byte-identical, region digest
                  faf2d709…0426 unchanged.  MEASURED: 1 and 1, digest unchanged.

R-5  THE LEGITIMATE SUPERVISOR/PCS SOCKET AND SLOT-6 CLAUSES. Region BODY.
     These are NOT watchdog grants. They are the supervisor's control channel,
     common to BOTH options and untouched by the W-B choice. Seven clauses:
     §P1-2.4's slot-6 role-class comment; §P1-6's supervisor AF_UNIX /
     SOCK_SEQPACKET protocol-0 pair inherited to slot 6 and its rationale
     sentence; §P1-15 row 42's "the peer reaches the supervisor role at slot 6
     and nowhere else"; §P1-3.4's two `_socket` primitive-binding lines; and
     §P1-6's non-inheritable-descriptor sentence.
     EXPECTED COUNT IN THE RESOLVED FILE: all seven present and unchanged. NO
     SPAN INTERSECTS ANY OF THEM.
     MECHANICALLY CONFIRMED: none of these seven clauses contains any D1 or D2
     literal, and no D1 or D2 literal contains any of them (§2.6.4).

R-6  WATCHDOG SLOT-6 REFERENCES IN THEIR CLOSED / ABSENT SENSE ONLY.
       §P1-13.2 row 4 [W-B] branch: "slot 6 is not used and is explicitly closed
                        by a file action; the watchdog holds no socket"   (S8)
       §P1-15 row 99 [W-B] branch: "{0,1,2} together with {3,4,5,7,8,9,10},
                        slot 6 explicitly closed"                        (S11)
     EXPECTED COUNT IN THE RESOLVED FILE: exactly these two loci, each in its
     CLOSED/ABSENT sense, each with its [W-A] sibling deleted.
     A watchdog slot-6 occurrence in ANY OTHER SENSE IS FORBIDDEN by class F.

R-7  B14 AND IR-13 BINDINGS. Region BODY, inside the joint block.
     TS-5 B14, IR-13 row 35 (CK-14 / STAGE_B_OPTION_MISMATCH) and IR-13 row 47
     (CK-2 / STAGE_A_OPTION_INVALID) are RETAINED VERBATIM. No span touches the
     joint block at all, and §2.2.6 VERIFIES the block is byte-identical after
     the splice.

CLASS F — FORBIDDEN IN THE RESOLVED FILE. Expected count ZERO for each.

F-1  W-A OPERATIVE GRANTS AT PREAMBLE OR BODY LOCI, DETECTED BY THE LITERAL D2
     ARRAY OF §2.6.3 AND BY NOTHING VAGUER, AND ELIMINATED BY CONSTRUCTION
     BECAUSE EVERY ONE OF THEM LIES INSIDE A PINNED SPAN.

F-2  THE W-A REQUEST SOCKET AND FRAME BEHAVIOUR.
     fragment  t-wd-freeze.v1
     EXPECTED COUNT IN THE RESOLVED FILE: 0.   MEASURED: 0.
     THIS FRAGMENT IS NOT IN TS-1's VOCABULARY AND IS NOT IN THE GUARD DATA, so
     unlike the two option tokens it CAN be, and must be, eliminated whole. Its
     NINE occurrences in composite v1.14 are at lines 66, 1772, 1778, 2267, 2292, 3972, 4269, 8205 and 8233,
     and EVERY ONE OF THEM LIES INSIDE A SPAN: S1, S3, S4, S5, S6, S7, S8, S9
     and S10 respectively. MEASURED ON THE PINNED OUTPUT: 0.

F-3  W-A VARIANT BRANCH TEXT. Any surviving [W-A]-branch content at any of the
     nineteen non-guarddata loci, with or without its marker.

F-4  OPEN-CELL ASSERTIONS ABOUT CELL 2, DETECTED BY THE LITERAL D1 ARRAY OF
     §2.6.2 AND BY NOTHING VAGUER.

WHAT CLASS F DOES NOT COVER, STATED SO THE TABLE CANNOT BE MISREAD:
  the W-A OPTION TOKEN and the W-A OPTION-AMENDMENT TOKEN are NOT in class F.
  They are in class R at rows R-1, R-2 and R-3. THERE IS NO RULE IN THIS BINDING
  REQUIRING THEM TO OCCUR ZERO TIMES, AND ANY SUCH RULE WOULD CONTRADICT TS-1,
  IR-13 row 47 AND THE CK-14 FIXTURE.

TOTALS IN THE RESOLVED FILE, RECOUNTED FROM THE PINNED OUTPUT RATHER THAN
ASSERTED — AND ONE OF v3's FIGURES WAS WRONG.
  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
      pre-resolution occurrences in composite v1.14:  3
        the Cell-2 W-A exposition   -> REPLACED, inside span S1
        the TS-1 option-set grammar -> RETAINED (R-1)
        the CK-14 fixture Stage-B   -> RETAINED (R-3)
      POST-RESOLUTION COUNT: 3, NOT 2. v3's §2.5 said 2 and that was
      false against its own pinned replacement bytes, which name the rejected
      option's token once as a historical fact carrying no capability (CT-2).
      The author found it in v4, the X line independently confirmed the figure
      of 3 against the v4 pinned output, and it is RECOUNTED here from the v1.14
      pinned output rather than carried forward. The count is a disclosure, not
      a check, and no PO rule consumes it.
  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
      pre-resolution: 1, TS-1's pairing rule
      POST-RESOLUTION COUNT: 2 — the TS-1 pairing rule (R-2) AND ONE HISTORICAL
      MENTION INSIDE THE S1 REPLACEMENT, which describes NO capability (CT-2).
      BOTH ARE CLASS R.
  I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS   3
  P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1                             2
  t-wd-freeze.v1                  0   (F-2)
  "[W-A]" outside GUARDDATA       0   (PO-2)
  "[W-B]" outside GUARDDATA       0   (PO-2)
  "[W-A]" / "[W-B]" in GUARDDATA  1 each   (R-4)
  "the v1.11 amendment is installed"  1, inside the joint block   (PO-8)
  watchdog-sense "slot 6"         2 loci, both CLOSED/ABSENT   (R-6)
  supervisor-sense socket/slot-6  7 loci, unchanged            (R-5)
```

### §2.6 `PO-9` — the literal detectors, and the HONEST boundary of their claim

**These detectors are DEFENCE IN DEPTH. They are not the primary quarantine.**
The primary quarantine is §2.2: exact source identity, exact transformation, and
the expected full resolved-output hash of §2.2.6. That ordering is the `M-4`
repair, and it is stated first because v3 had it the other way round.

#### §2.6.0 The claim, narrowed, and the claim that is withdrawn

```text
WHAT D1 AND D2 DO CLAIM, AND IT IS EXACTLY THIS:
  For each of the 11 D1 literals and each of the 13 D2 literals, that literal
  occurs ZERO times in PN(resolved file minus REGION(GUARDDATA)); and each of
  the 24 literals is DETECTED when it is present in any carrier, under arbitrary
  line wrapping, arbitrary surrounding bytes and arbitrary blockquote
  indentation. THAT IS EXACT LISTED LITERAL COVERAGE AND NOTHING MORE.

WHAT IS WITHDRAWN, EXPLICITLY:
  v3's §2.6.4 heading "FALSE NEGATIVES — every forbidden vector, checked" and
  the sentence structure around it implied that D1 and D2 detect the CLASS of
  forbidden W-A grants. THEY DO NOT. A FINITE ARRAY OF EXACT LITERALS CANNOT
  DETECT ARBITRARY SEMANTIC PARAPHRASES, AND THIS BINDING NO LONGER CLAIMS THAT
  IT CAN.

THE Y LINE's COUNTEREXAMPLE, ACCEPTED AND CARRIED HERE RATHER THAN ARGUED WITH:

    The watchdog is permitted a socket in descriptor slot 6 and may send one
    fixed freeze command; acceptance causes the PCS to invoke its group-freeze
    routine during a time-limited service period.

  That paragraph restores the W-A slot-6 socket, the request frame, the
  acceptance-driven trigger and the bounded service window in different words,
  and it normalizes to ZERO D1 matches and ZERO D2 matches. THE Y LINE IS RIGHT
  AND THE DETECTOR IS SILENT ON IT.

WHY THAT IS NEVERTHELESS NOT A HOLE IN THE TRANSFORMATION, STATED AS A PROOF
RATHER THAN AS REASSURANCE:
  SUCH A PARAGRAPH CANNOT ENTER A BYTE-IDENTICAL RESOLVED OUTPUT. The resolved
  output is a total function of composite v1.13's bytes and the eleven pinned
  spans; any inserted byte anywhere changes the full-output SHA-256 and PO-0
  FAILS CLOSED. §2.6.5 publishes that fixture with its measured numbers.
  THE DETECTORS THEREFORE COVER WHAT THEY LIST; PO-0 COVERS EVERYTHING ELSE.
```

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
`PN` applied to a passage of the pre-resolution Cell-2 span.

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
MEASURED ON THE PINNED OUTPUT: 0 of 11.
COVERAGE, MECHANICALLY CHECKED: 11 of 11 occur in PN of the pre-resolution
                         Cell-2 span of composite v1.14. A literal that does not
                         is a defect in this array, and the oracle reports the
                         array INCOMPLETE rather than passing.
```

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
MEASURED ON THE PINNED OUTPUT: 0 of 13.
COVERAGE, MECHANICALLY CHECKED: 13 of 13 occur in PN(composite v1.14).

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

#### §2.6.4 False positives — measured, not argued

```text
  the S1 replacement bytes                       D1 matches 0   D2 matches 0
  Cell 1, byte-unchanged, which legitimately
    still asserts an OPEN cell about a DIFFERENT
    author cell                                  D1 matches 0   D2 matches 0
  the joint install and authorization block,
    where TS-1's grammar, TS-1's pairing rule
    and the CK-14 fixture MUST name the W-A
    token                                        D1 matches 0   D2 matches 0
  REGION(GUARDDATA), out of scope anyway and
    additionally clean                           D1 matches 0   D2 matches 0
  each of R-5's seven supervisor-side clauses    contains no literal, and no
                                                 literal contains it
  each of R-6's two closed/absent watchdog
    slot-6 clauses                               contains no literal, and no
                                                 literal contains it
  THE WHOLE PINNED RESOLVED OUTPUT MINUS
    GUARDDATA                                    D1 matches 0   D2 matches 0

  WHY CELL 1 IS SAFE, AND IT IS THE SHARPEST CASE. Cell 1's blocking notice says
  "This version is not acceptable as an operative object until the author cell
  AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS is signed". D1[2] requires the
  continuation "...until the watchdog-freeze mechanism cell is signed", which
  Cell 1 does not carry. EVERY D1 LITERAL CARRIES A WATCHDOG-FREEZE-SPECIFIC
  DISCRIMINATOR FOR EXACTLY THIS REASON. A detector that fired on Cell 1 would
  demand the deletion of a blocking notice this signature does not discharge,
  which CT-5 forbids.
```

#### §2.6.5 The mutated-paraphrase fixture — REQUIRED, and it fails on `PO-0`

```text
FIXTURE MP-1, BYTE-EXACT. THE X LINE's X-L4 IS REPAIRED HERE: v4's recipe did not
fix the insertion point byte-exactly, so its pinned digest was not reachable from
its own published text and the X line could not reproduce it at any of the
8,067 line boundaries it searched. THE INSERTION IS NOW PINNED BY A UNIQUE
WHOLE-LINE ANCHOR, AN EXACT PAYLOAD, AN EXACT ORDER AND AN EXACT NEWLINE
CONVENTION, AND BOTH THE BEHAVIOUR AND THE BYTES ARE REQUIRED. NO KNOWN-FALSE
DIGEST IS RETAINED AS INFORMATIVE.

CONSTRUCTION, TOTAL AND DETERMINISTIC:
  1. Take the pinned resolved output of §2.2.6 and split it on 0x0A into lines,
     each retaining its 0x0A except possibly the last.
  2. THE ANCHOR is the UNIQUE line whose whole content, with no leading or
     trailing byte, equals exactly:
       THE WATCHDOG PRODUCES NO DURABLE OBJECT OF ANY CLASS. It is therefore not a
     ITS CARDINALITY IN THE RESOLVED OUTPUT IS EXACTLY ONE. Zero, or two or
     more, FAILS CLOSED and MP-1 is not constructed.
  3. INSERT THE PAYLOAD IMMEDIATELY BEFORE THE ANCHOR LINE — that is, the
     payload's first byte becomes the first byte of the anchor line's former
     offset — and emit every other byte unchanged.
  4. THE PAYLOAD IS EXACTLY THESE FOUR LINES, IN THIS ORDER, each terminated by
     exactly one 0x0A, the fourth being empty so that the payload ends with two
     consecutive 0x0A:
       The watchdog is permitted a socket in descriptor slot 6 and may send one
       fixed freeze command; acceptance causes the PCS to invoke its group-freeze
       routine during a time-limited service period.
       <empty line>
     PAYLOAD LENGTH   195 UTF-8 bytes
     PAYLOAD SHA-256  ee8a830d46f709ff2ffd95238600437e885c32d84bf268a1658950cd5ed63d2f
     THE BLANK LINE FOLLOWS THE PARAGRAPH AND NEVER PRECEDES IT. That ordering
     is part of the value, and it is the ambiguity v4 left open.

MEASURED ON THAT CANDIDATE:
  D1 matches                       0
  D2 matches                       0
  markers outside REGION(GUARDDATA) 0 and 0      -> PO-1 PASSES, PO-2 PASSES
  H_GUARDDATA                      faf2d709…0426 -> PO-3 PASSES
  class-R rows                     all present   -> D3 PASSES
  FULL OUTPUT LENGTH               625035 bytes, which is 624840 + 195
  FULL OUTPUT SHA-256              ba513ff06338eef1228d4c640617a08d1ab0da1869110cac2b4d99ee42cedb39
  PO-0                             ***FAILS***, because that digest is not
                                   9904ff3bf73f90329df7ac06fac5dbf4b211713964f610541761018c9bacb5c5

BOTH THE BEHAVIOUR AND THE BYTES ARE ACCEPTANCE CRITERIA. A build whose MP-1
reproduces the behaviour but not the length and digest above has not constructed
MP-1, and a build that reports MP-1 as CONFORMING fails outright.

THIS FIXTURE IS THE PROOF OF THE §2.6.0 BOUNDARY, STATED AS A RUNNABLE THING
RATHER THAN AS A CLAIM: a candidate that reintroduces a W-A capability in words
the detectors do not list PASSES EVERY DETECTOR AND STILL FAILS, because the
complete output is byte-pinned. A build that reports MP-1 as conforming FAILS.
```

#### §2.6.6 `D3` and `D4`

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

### §2.7 The properties the `S1` replacement satisfies — an audit, not the contract

`CT-1`..`CT-6` are not the acceptance criterion for the Cell-2 bytes — the digest
is, and now the full-output digest is. They are retained so a reviewer can check
the pinned bytes against the intent that produced them.

```text
CT-1  IT STATES THAT THE CELL IS SIGNED, names the exact selected token and the
      signature path and digest ffcb4116…a7dc.                         SATISFIED
CT-2  IT STATES THAT W-A IS REJECTED, by name, as a historical fact about the
      choice — and states NO W-A CAPABILITY.                           SATISFIED
CT-3  IT CONTAINS NO ASSERTION THAT THE CELL, THE MECHANISM OR THE CHOICE IS
      OPEN, UNSIGNED, UNDECIDED OR CARRIED IN BOTH DIRECTIONS. MECHANICALLY
      CONFIRMED: zero of the eleven D1 literals occur in the block. SATISFIED
CT-4  IT CONTAINS NO VARIANT-MARKER STRING.                            SATISFIED
CT-5  IT LEAVES CELL 1 UNTOUCHED. The splice range begins at the Cell-2 heading,
      which is after every byte of Cell 1, so OR-4 edits no byte of Cell 1.
                                                                       SATISFIED
CT-6  IT ADDS NO NORMATIVE RULE. The replacement is a status statement.  SATISFIED
```

**No governing byte is written by this binding.** The transformation is
specified, its complete output is pinned, and `OR-4` performs it — and `OR-4` is
not authorized.

### §2.8 `L-X6` — expanded to the surface the bytes actually carried, then
### closed by `R4` and by nothing else

```text
WHAT v2.13 RECORDED, AND WHY IT WAS TOO NARROW. Amendment v1.10 §A0.3 and the
v2.13 closure both recorded exactly one clause: "§P1-7.5 c10 requires a getpgid
answer while §P1-3.4 binds no _getpgid". THE BYTES CARRIED MORE THAN THAT, AND
THE X LINE SAID SO AT X-L5:

  CLAUSES AFFECTED, ALL THREE, NOT ONE
    c10  requires getsid(pid_mid) == pid_mid AND getpgid(pid_mid) == pid_mid
         before c11 may install SPAWNING_GROUP.json
    c14  requires getpgid(supervisor_pid) == process_group_id
    m3   requires getsid(0) == getpgid(0) == getpid() in the middle

  OPERATIONS AFFECTED, BOTH, NOT ONE
    getpgid   HAD a substitute route in principle — §P1-10.3's STAT_PARSE
              returns the pgrp field — though c10/c14 name the literal
              operation and not the parser
    getsid    HAD NO ROUTE AT ALL. STAT_PARSE returns no session id and states
              in terms that NO OTHER SUFFIX FIELD IS PARSED, READ, INTERPRETED
              OR CONSTRAINED. THIS IS THE HARDER HALF AND v2.13 DID NOT NAME IT.

  BOTH OPERATIONS, IN BOTH ARGUMENT FORMS
    positive pid   c10, c14
    pid 0          m3

WHY IT COULD NOT BE CARRIED AS A FENCED EXCEPTION. §P1-3.6 requires every later
primitive use through a bound local name; §P1-14.6 S-3, S-5, S-6 and S-7 refuse
an added binding, a module attribute call, an Attribute call target and every
indirection route STATICALLY. A build attempting c10 as written produced no
certified artifact — the direction was fail-closed — but the clause was an
implementation dead end rather than a gate, and §H11 can later authorize writes
and execution only and grants no authority to alter an accepted primitive
surface. ACCEPTANCE WOULD HAVE BOUND AN OPERATION A LATER AUTHORIZED
IMPLEMENTATION STILL COULD NOT SUPPLY. The Y line graded that a Major, Y-M4, and
the stricter grade governs.

THE EXCEPTION IS WITHDRAWN, AND ONLY BECAUSE THE BYTES NOW PROVE THE COMPLETE
SURFACE IS REACHABLE. Composite v1.14 §P1-3.4 binds _getsid and _getpgid from os,
in the binding block, in order; §P1-3.5 states their four identity tests
explicitly; their argument, result and error semantics are pinned for pid 0 and
for positive pids with every unexpected result and every fault routed
fail-closed; and c10, c14 and m3 call them through the bound local names.
S-3, S-5, S-6 and S-7 ARE NOT WEAKENED — S-3 reads §P1-3.4's list by reference
and therefore accepts exactly the new list and nothing wider. MS-11's
eighty-nine-row closure, its canonical length 20534 and its digest are
UNCHANGED, because both names are attributes of a module already in every
relevant allowlist. THE EXCEPTION IS CLOSED BY R4 AND BY NOTHING ELSE, and
composite test row 89 clause (6C) exercises c10, c14 and m3 explicitly.
```

---

## §2A. `B2` — the dry-run oracle, and its boundary against `OR-3`/`OR-4`

A **test-only, in-memory transformation oracle** may be implemented and
unit-tested **before** the amendment is accepted and before any handoff step is
authorized — **and only after a separate inactive-scaffold authorization, which
does not exist.**

### §2A.1 What the oracle is

```text
O-1  INPUT. Byte copies of amendment v1.11 and composite v1.14, read from their
     literal paths read-only and held in memory. It opens neither for
     behaviour; it hashes and rewrites bytes and interprets no rule.
O-2  IT SELECTS W-B IN MEMORY, from a test-only enum with exactly two members,
     and produces a candidate resolved byte string as a RETURN VALUE.
O-3  IT CHECKS PO-0 THROUGH PO-10 against that in-memory string, and reports
     each as a pass or a fail with the locus that failed.
O-4  IT MAY REPORT DIGESTS, and every reported digest MUST be emitted with the
     literal tag
       test-only/non-installed/non-authoritative
     adjacent to the value, in the same string, so that no transcript, log line
     or test output can be quoted as an install digest.
O-5  IT IS TOTAL AND DETERMINISTIC. Same inputs, same output bytes, on every
     run, on any host. It samples no clock, draws no entropy and reads no
     environment variable. §2.2.5's splice makes this checkable: two independent
     implementations of it must agree byte for byte and both must reproduce
     §2.2.6's full-output digest.
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
      the PCS classifier, not STAT_PARSE, not KG-1, not KG-2, not KV-1..KV-6,
      not SC-1..SC-10, not the descriptor topology and not any process
      operation. Those are §H3 of the handoff and they are NOT implementable
      under any authorization that exists.
```

### §2A.3 What later authorized `OR-4` does that the oracle does not

```text
                                        ORACLE      AUTHORIZED OR-4
  produces resolved bytes                in memory   ON DISK at MS-1's second
                                                     literal path
  requires the acceptance token          no          YES — v1.11 accepted first
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
nor the handoff, nor the oracle produces composite v1.13 in post-selection form
at any path. **The figures of §2.2.6 were computed in memory over a copy in a
session scratchpad and no resolved bytes were retained anywhere.**

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
      Span S1 does not touch it, and PO-9's D1 does not fire on it.

 1  W-B author selection (OR-2)                   COMPLETE         yes — this binding only
      token I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
      signature ffcb4116…a7dc, 2026-08-05, base 176d609

 2  This post-selection binding, v5               DRAFT            no
      awaiting bounded X/Y review against the v2.14 bytes

 3  Watchdog authority amendment v1.11 acceptance NOT ACCEPTED     no
      token I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11
      unsigned; §4 states exactly what it will and will not do.
      THE v1.10, v1.9, v1.8 AND v1.7 TOKENS ARE RETIRED AND MUST NOT BE SIGNED:
      R1 through R4 changed the bytes they would have accepted.

 4  Process identity Option A selection           COMPLETE         no
      token I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
      signature 7a8ab2da…3d1f, 2026-08-04
      recorded at XS-1 as external author state, member of no class

 5  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1  NOT ACCEPTED     no
      must be reviewed and accepted SEPARATELY before Option A can become
      operative; §3.2 states the disposition in full

 6  The LATER COMBINED BINDING of XS-1            DOES NOT EXIST   no
      STATE: BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW, by XS-1(b)

 7  Fresh independent X/Y round on the v2.14 pair NOT PERFORMED    no
      the v2.14 governing pair has NOT been independently reviewed. The v2.13
      round WAS performed and DIVERGED — X confirmed, Y returned four executable
      Majors — and this generation exists because the Majors governed. Gate 3
      cannot open before BOTH lines confirm the SAME v2.14 bytes.

 8  Inactive SCAFFOLD implementation              CANDIDATE        no
                                                  ELIGIBILITY ONLY
      the handoff v5 is a scope contract for INERT ORACLE AND DECLARATIVE
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
C-1  THE MECHANICAL FACT, RECOMPUTED AGAINST v2.14. The strings attested_pid and
     attested_pgid occur 0 times in composite v1.14 and 0 times in
     amendment v1.11. There is no schema, key, type, carrier, consumer or
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

C-8  R4's TWO NEW BOUND PRIMITIVES DO NOT DISTURB ANY OF THIS EITHER. _getsid
     and _getpgid answer questions about SESSION and PROCESS-GROUP membership of
     a pid for the bootstrap's own kernel verification at §P1-7.5 c10, c14 and
     m3. They are not the attested_pid / attested_pgid peer-record fields, they
     write no durable record of any class, and no identity field is re-derived,
     defaulted or invented by binding them.

C-7  THE R1 PARSER CONTENT DOES NOT DISTURB ANY OF THIS. §P1-10.3's STAT_PARSE
     observes a process GROUP, a ppid, a state character and a start identity
     from /proc/<pid>/stat for process-control purposes; those are not the
     attested_pid / attested_pgid identity fields of §P1-13.2 row 2, which are
     peer-record fields with no schema in this pair. KG-2 P-2 records a pid as a
     group value inside the PCS's own in-memory handle table and writes no
     durable record of any class. NO IDENTITY FIELD IS RE-DERIVED, DEFAULTED OR
     INVENTED BY EITHER.
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
review round on the v2.14 bytes is:

```text
I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11
```

**The v1.10, v1.9, v1.8 and v1.7 tokens are retired.** `R1` through `R4` changed
the bytes they would have accepted, so signing any of them would accept a pair
that no longer exists.

### §4.1 What that future token accepts

```text
A-1  THE TWO GOVERNING FILES AS ONE INDIVISIBLE UNIT — amendment v1.11 and
     composite v1.14, at the exact digests of §0.2, per H-1.
A-2  THE TWO DELIMITED BYTE-IDENTICAL REGIONS at their stated digests, and the
     narrowed identity claim that attaches to those two regions and to nothing
     else.
A-3  THE FIXED ACCOUNTING — MS-2 at 75, MS-3 at 7, MS-8 at 89, TS-3
     member_count 89, member classes 7, closed failure codes 25, pre-production
     checks 15 running CK-1..CK-15, M4 key set 21, IR-13 at 50 rows, MS-13
     element keys 6 with 8 effect booleans each, 32 effect assertions all false,
     4 project-import dependencies, 7 unexecuted module-scope branches, 83
     composite provenance rows, the 16-member generic_harness.py scoped
     allowlist, and the 89-row reachable_closure at CANON length 20534 — WHICH
     R4 DOES NOT PERTURB, BECAUSE BINDING TWO MORE ATTRIBUTES OF AN
     ALREADY-IMPORTED MODULE ADDS NO MODULE.
A-4  THE ONE CANONICAL PARSER at §P1-10.3 — STAT_READ, STAT_PARSE with its
     STAT_LAYOUT_ID pin, its exact suffix framing, its closed state set, its two
     integer grammars and its PRIMITIVE_FAULT outcome, and KG_GROUP_ADMISSIBLE
     — together with §P1-10.4 row I-11.
A-5  THE KG-1, KG-2, KV-1..KV-6 AND SC-1..SC-10 DEFINITION at §P1-10.7,
     INCLUDING its six global phases, its closed three-terminal set with two
     qualifiers, its TWO-LEVEL dominance rule with the intra-phase precedence
     and least-index tie-break, the explicit PHASE-4 and PHASE-6 reductions, its
     KG-2 population conditioned on outcome == STOPPED under the pinned K1..K6
     step order, and its published parser vectors V0..V39.
A-7  THE CLOSED PRIMITIVE SURFACE OF §P1-3.4 INCLUDING _getsid AND _getpgid,
     their four identity tests at §P1-3.5, their pinned argument, result and
     error semantics for pid 0 and for positive pids, and their three call sites
     at §P1-7.5 c10, c14 and m3 and nowhere else.
A-6  THE OBLIGATION SHAPE OF OR-1..OR-11 — the sole conforming construction
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
B-4a  IT DOES NOT AUTHORIZE CALLING _getsid OR _getpgid, or any other bound
      primitive. Binding a name in a specification is not permission to run it;
      gates 9 and 10 remain ungranted and §H11 of the handoff is unchanged.
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

### §5.1 What changed since v3

v2.13 performed its own four-row catch-up. **v2.14 is another real replacement
generation and owes its own four rows.**

```text
                                       v2.13   v2.14
MS-2                                      71  ->  75
MS-3                                       7      7
MS-8 / TS-3 member_count                  85  ->  89
composite provenance region rows          79  ->  83
recorded M2+M3 digests                    78  ->  82
member classes                             7      7   only M2 grew
```

The four rows, in `MS-2` order, each digest recomputed from disk:

```text
2999e2129de19ff38dee12071453c7156a5432efaf299bc69e79dc7e7b04ac53  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_10_DRAFT.md
15e11f0e4c10fe8b85607dc383520d5b009712603084e82a8756211615bd8fb3  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_13.md
89e210430b617d88a67229df2beeff82c5c844f6de1da1d03b376b758d7cb0c2  reviews/fable_officina_p1_wb_v2_13_final_x_review.md
a4056f477bd631ca7b1b19292371de7afade367ecbfd2b1b090a1f95f79b4036  reviews/sol_officina_p1_wb_v2_13_final_y_review.md
```

**BOTH v2.13 REVIEWS ENTER, INCLUDING THE CONFIRMING ONE.** What makes a review
an `M2` row is that the generation it reviewed is no longer live, not the verdict
it returned.

### §5.2 The disposition rules

```text
PR-1  THE FOUR ROWS ARE IN. This generation's install enumerates 89 members
      from MS-1..MS-7 alone, with MS-2 at its literal 75 and the TS-3
      member_count literal at 89. THE HANDOFF STILL TOUCHES NONE OF IT.
PR-2  OR-4 IS STILL NOT A GENERATIONAL ROUND. It produces the post-selection
      bytes of the SAME generation at MS-1's SAME two literal paths and replaces
      no document, so no row enters at OR-4, OR-6, OR-9 or OR-11.
PR-3  THE NEXT ACTUAL GENERATIONAL ROUND — one that REPLACES v1.11/v1.14 — adds
      its own four rows: the v1.11 amendment, composite v1.14 and that round's
      two independent reviews. It does NOT re-add any of the twenty before them.
PR-4  NEGATIVE TEST OBLIGATION. A fixture that enumerates 63, 69, 73, 77, 81, 85
      or 93 members FAILS against this generation. The handoff states this as a
      required negative test.
PR-5  THE TWO W-B BINDING REVIEWS ARE NOT M2 MEMBERS of any generation and were
      not substituted for any pair-review row.
PR-6  NO HISTORICAL BYTE IS EDITED BY ANY OF THIS. The 71 rows MS-2 already
      carried are byte-unchanged; the four are appended. EVERY ONE OF THE 82
      RECORDED M2 AND M3 DIGESTS WAS RECOMPUTED FROM THE FILE ON DISK AND ALL 82
      MATCH.
```

### §5.3 The governing findings, and their state

```text
F1  MAJOR, FAIL-OPEN.  REPAIRED IN v2.11 and carried. The pre-production range
    is CK-1..CK-15 everywhere.
F2  MAJOR, NOT IMPLEMENTABLE.  DEFINED IN v2.11, EXECUTABLE IN v2.12, CANONICAL
    IN v2.13. One parser governs every consumer; the field framing is exact; the
    dominance is a phase order rather than an assertion; the population is total.
    THE DEFINITION IS STILL NOT AN IMPLEMENTATION AUTHORIZATION: the handoff
    forbids writing the classifier and gate 10 does not exist.
F3  MINOR.  **NOT ACTUALLY REPAIRED IN v2.13, AND REPAIRED HERE.** v2.13
    asserted that OR-4 read "the v1.10 amendment is installed"; the bytes of
    both files read "the v1.9 amendment is installed". Amendment v1.10's own
    §A0 carried the same false completeness claim over all five
    generation-scoped strings. NEITHER INDEPENDENT LINE REPORTED IT. OR-4 now
    reads "the v1.11 amendment is installed", inside the joint block and
    therefore in BOTH files, and PO-8 verifies the current value on the pinned
    output.
F4  MINOR.  REPAIRED in v2.11 and carried: composite's G-10 locator names
    §P1-14.4.
F5  MINOR.  REPAIRED in v2.12 and carried: H-4 names CK-7 as sole owner of
    HISTORICAL_BYTE_MOVED.
F6  MINOR.  REPAIRED in v2.12 and carried: N-16, row 106's ten groups, CK-13's
    entry-count literal, the §A9 section locator, UTF-8 byte counts.
F11 MAJOR, ORDER-DEPENDENT TERMINAL.  NEW IN v2.13, REPAIRED IN v2.14. PHASE 4
    carried two terminal-bearing predicates and selected per entry in table
    order, so one table returned T1 or T3 depending on permutation (Y-M1). Every
    terminal-bearing phase is now a closed scan plus a total reduction under an
    explicit intra-phase precedence.
F12 MAJOR, DOUBLE-VALUED POPULATION.  NEW IN v2.13, REPAIRED IN v2.14. KG-2 P-2
    and P-10 gave opposite answers on an ordinary AWAIT_STOP/TIMEOUT route
    (Y-M2). Population is now conditioned on outcome == STOPPED under a pinned
    step order.
F13 MAJOR, STALE EXECUTABLE LITERAL.  NEW IN v2.13, REPAIRED IN v2.14. Composite
    test rows 105 and 106 retained 81-member literals against an enforced 85
    (Y-M3), and the v2.13 closure's claim that every dependent literal had moved
    was false. The whole generation is recounted at 89 and swept.
F14 MAJOR, UNREACHABLE MANDATORY SURFACE.  LOGGED SINCE v2.11 AS L-X6, GRADED
    MAJOR BY THE Y LINE IN v2.13 AS Y-M4, REPAIRED IN v2.14. §P1-3.4 now binds
    _getsid and _getpgid and pins their semantics; c10, c14 and m3 call them
    through the bound local names.
F7  MAJOR, IDENTIFIABILITY.  NEW AND REPAIRED IN v2.13, AND ITS OUTPUT IS
    REPLACED HERE BECAUSE ITS INPUT MOVED. The complete OR-4 output
    is pinned: eleven spans, exact source and replacement bytes and digests, one
    deterministic splice order, and a full resolved-output length and SHA-256.
F8  MAJOR, OVERBROAD CLAIM.  NEW AND REPAIRED IN v2.13. PO-9's quarantine claim
    is narrowed to exact listed literal coverage, the semantic-paraphrase claim
    is withdrawn, and MP-1 demonstrates the boundary.
F9  MINOR, NEW AND AUTHOR-FOUND IN v2.13. v3's §2.5 said the W-A option token
    would occur twice in the resolved file. It occurs three times, because the
    pinned replacement names it once. Neither line reported it. §2.5 is
    corrected and the figure is recounted from the pinned output.
F10 MINOR, NEW AND REPAIRED IN v2.13. v3's §2.2.2 encoding sentence claimed the
    replacement carried U+2014 at two loci "and no other non-ASCII character";
    it also carries U+00A7 at five. The X line logged it as L-X1.
F15 MINOR, NEW IN v2.13, REPAIRED IN v2.14. v4's §2.2.4 transcription of the S7
    delete literal was wrong by one backtick and rendered a 276-byte string
    occurring nowhere. The X line logged it as X-L3 and noted the direction was
    fail-closed. The literal is now delimited so that it reproduces.
F16 MINOR, NEW IN v2.13, REPAIRED IN v2.14. v4's MP-1 digest did not reproduce
    from its own recipe, because the insertion point was not byte-exact. The X
    line logged it as X-L4 and graded it non-blocking. §2.6.5 now pins a unique
    whole-line anchor and republishes the measured length and digest, and both
    the behaviour and the bytes are required.
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
The resolved bytes and the `MP-1` candidate were constructed IN MEMORY, every
figure above was measured on them, and both were then DISCARDED. **No resolved
production file was created at any path and `OR-4` was not executed.**
They are not written to any path, are not composite bytes, and become composite
bytes only at an authorized `OR-4` that does not exist. **The full resolved
output of §2.2.6 exists as a LENGTH AND A DIGEST and as nothing else: it was
computed in memory over a copy and no resolved byte sequence was retained at any
path, inside or outside the repository.**

No freeze was executed, requested, journalled or witnessed. No `/proc` was read
against any live process, and the parser vectors of §P1-10.7 are synthetic byte
strings constructed from the documented record layout rather than samples of any
running process. No clock was sampled for any contract purpose. No Philosophia
production or project module was imported, executed or compiled.
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
WATCHDOG AUTHORITY AMENDMENT V1.11 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

The exact selected token and the formal selection signature govern. This draft,
the companion handoff and every author closure are untrusted self-assessments
and are normative for nothing.
