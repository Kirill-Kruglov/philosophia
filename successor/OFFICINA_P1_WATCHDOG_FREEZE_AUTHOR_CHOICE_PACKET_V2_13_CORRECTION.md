# Officina P1 watchdog-freeze mechanism — author choice packet v2.13 (correction)

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

This packet exists for one reason: the v2.13 generation is a **replacement
governing generation**, and every governing generation of this chain carries an
author-facing packet recording what its two governing files say, at what
digests, with what accounting. It is the pre-selection anchor target named by
`TS-1`'s `governing_pre_selection.packet` and the hash-read target of `TS-2B`
`A16(b)`, and nothing else.

`T` is `NOT_ACTIVATED`; the programme claim is `OPEN`.

---

## §0. Scope — a bounded governing repair after two REVISE verdicts

### §0.1 What licensed this round

Both independent lines reviewed the v1.9/v1.12 governing pair. **Both returned
`REVISE`.**

```text
ca02d4858022fef026fdbbe65dfb07dc7fb1e885563530be27238d7dbcc8a61a  reviews/fable_officina_p1_wb_v2_12_final_x_review.md
    REVISE_OFFICINA_P1_WB_V2_12
    TWO executable Majors, X-M1 and X-M2, plus seven logged items

92a394a3c3e3126b278a9af1d33740db1a08810de940be6b6be2ab062e1f41a3  reviews/sol_officina_p1_wb_v2_12_final_y_review.md
    REVISE_OFFICINA_P1_WB_V2_12
    FIVE demonstrated Majors, M-1 through M-5, plus three log items
```

**THE UNION OF THE TWO SETS GOVERNS.** No finding of either line is traded
against the other, and where the two graded the same clause differently — §P1-10.3,
which the X line deferred to a later round and the Y line graded a this-round
blocker — **the stricter grade governs**. This round is licensed by those seven
Majors, by the accounting they force, and by the maintenance items both lines
logged.

```text
X-M1  KV-5 AND KV-4 MASKED KV-6's FRESH-OBSERVATION CONJUNCT. An entry whose
      recorded group was safe but whose freshly observed pgrp was protected
      failed KV-5 first, was skipped, and a _killpg was issued from that table.
X-M2  A STALE ACCOUNTING LITERAL SURVIVED THE FORCED SWEEP. Composite row 108
      still read "any length other than 77" against an enforced cardinality of
      81, and the v2.12 closure claimed it had moved.
M-1   KG-1's POSITIONAL TOKENISER ACCEPTED SHIFTED MALFORMED FIELDS. Four
      demonstrated forms returned PRESENT_VALID carrying values from the wrong
      fields.
M-2   §P1-10.3 HAD TWO EXECUTABLE RESULTS FOR ONE ORDINARY LINUX LINE.
M-3   MALFORMED / STALE / PROTECTED PRECEDENCE WAS CONTRADICTORY AND
      KV_FORBIDDEN_TARGET WAS NOT SINGLE-VALUED.
M-4   THE POST-SELECTION COMPOSITE BYTES REMAINED UNDER-SPECIFIED OUTSIDE CELL 2,
      AND PO-9's LITERALS DID NOT ESTABLISH THEIR CLAIMED SEMANTIC BOUNDARY.
M-5   THE TWO LIVE AUTHORITY SURFACES IDENTIFIED THEMSELVES AS THEIR
      PREDECESSORS.
```

### §0.2 What this round is, and what it is not

```text
IT IS  a bounded governing repair of R1..R5 in the two governing files, plus a
       regenerated post-selection binding and inert-scaffold handoff, plus this
       packet and one author closure. SIX AUTHORED DELIVERABLES.
IT IS NOT  a design round, a reopening of any signed choice, an acceptance, an
       X/Y verdict, an implementation, an OR step, an install or an activation.
       No author cell is opened and none is closed. No mechanism, evidence
       class, treatment, covariate, endpoint or scientific constant moves.
       W-B REMAINS SIGNED AND IS NOT REOPENED. OR-2 ALONE IS COMPLETE.
```

---

## §1. The v2.13 governing pair

### §1.1 Paths and digests

```text
2999e2129de19ff38dee12071453c7156a5432efaf299bc69e79dc7e7b04ac53  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_10_DRAFT.md
15e11f0e4c10fe8b85607dc383520d5b009712603084e82a8756211615bd8fb3  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_13.md
```

Composite region digests:

```text
H_BODY       1bb4c5874968884aa61511d7a2ad1bc8d7551099a502a6f14472c453f02f55a5
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  d47076e846029082e26b24b0dda681a409edfc8801d74c5d71bd9b26f31df8aa
H_FILE       15e11f0e4c10fe8b85607dc383520d5b009712603084e82a8756211615bd8fb3
```

`H_GUARDDATA` is **byte-unchanged from v1.12**. No guard pattern was added,
removed or edited by this round.

### §1.2 The two delimited byte-identical regions

Extracted from both files by their own two delimiter lines and diffed with zero
difference. **Lengths are actual UTF-8 byte counts.**

```text
H_HANDOFF  7c5cabe2e48587ad34cd19ae0f4300f78965b27afc93cb719868aae9f5cd44a7    4167 bytes
H_JOINT    7f58b11dfaaa2a59aa3fd9ab48bc350049461d1771cdc609b9d2b81dd5b2c8fa  223866 bytes
```

### §1.3 The pre-selection anchor

Exactly one line of the amendment matches `A16(d)`'s grammar:

```text
P1_WATCHDOG_V2_13_PRE_SELECTION_COMPOSITE_SHA256 = 15e11f0e4c10fe8b85607dc383520d5b009712603084e82a8756211615bd8fb3
```

The complete token occurs **seven** times in the amendment and **once** in the
composite, at `A16(d)`. The retired segments `8`, `9`, `10`, `11` and `12` occur
**zero** times in either file. §A0.4's generation-segment sentence said `11`
while the v1.9 token carried `12`; **neither line logged that**, and it is
repaired here by the author.

---

## §2. `R1` — one canonical exact stat parser for every consumer

### §2.1 What was broken

Two grammars existed. §P1-10.3's prose rule named the state field among the
parsed fields and then called "a non-integer field" a parse failure, which gave
one ordinary Linux line two executable results. §P1-10.7's `KG-1` `G0` split the
suffix on a separator CLASS and required only **at least** twenty tokens, so an
inserted separator, a removed separator, a shifted token, an extra token or a
missing token moved every later position and `PRESENT_VALID` could carry a `pgrp`
that was never the `pgrp` field.

### §2.2 What v2.13 does

```text
ONE PARSER. §P1-10.3 now defines STAT_READ, STAT_PARSE and
KG_GROUP_ADMISSIBLE, and every start-identity consumer and every group consumer
uses them unchanged. §P1-10.7 KG-1 is a five-line CONSUMER with no grammar of
its own. G0..G5 are withdrawn as a separate grammar.

THE AMBIGUOUS SENTENCE IS DELETED and is not replaced by another of its shape.

EXACT FRAMING, NOT POSITIONS:
  L0  the comm frame is the FIRST 0x28 to the LAST 0x29, with an exact UDEC31
      pid prefix, exactly one 0x20 before the comm and exactly one 0x20 after it
  L1  the ONLY separator in the suffix is a single 0x20. Tabs, newlines, VT, FF,
      CR, parentheses, empty fields, leading and trailing spaces all REFUSE
  L2  STAT_LAYOUT_ID LINUX_PROC_PID_STAT_52_FIELD_V1; whole-record field count
      EXACTLY 52; suffix field count EXACTLY 50 — an equality, never "at least";
      state at suffix 1, ppid at 2, pgrp at 3, start_identity at 20
  L3  the state field is EXACTLY ONE BYTE from the closed nine-byte set
  L4  UDEC31 (length 1..10, bound 2147483647) for ppid and pgrp; UDEC64
      (length 1..20, bound 18446744073709551615) for start_identity; NO sign,
      NO underscore, NO radix prefix, NO point, NO exponent, and LEADING ZEROS
      REFUSED
  L5  PARSE_OK only if L0..L4 all hold, and NO field value of any kind is
      returned on a refusal

THE LAYOUT SET IS CLOSED WITH ONE MEMBER AND ITS RELATION TO §P1-2.1 IS PINNED
HONESTLY: the platform predicate admits Linux x86_64 and pins NO kernel release,
so the layout is verified from the observed bytes at EVERY observation and an
unknown kernel/layout combination REFUSES. No future layout is silently
admitted.

pgrp == 0 REFUSES FOR GROUP USE, as the single named admissibility rule
KG_GROUP_ADMISSIBLE, stated once. It is not a second parser.

A WRONG-SHAPED PRIMITIVE RETURN AND A NON-OSError BaseException have one named
closed outcome, PRIMITIVE_FAULT, whose single continuation everywhere is
§P1-10.2's STRUCTURAL_VIOLATION continuation. §P1-10.4 gains row I-11.
```

### §2.3 The published vectors

`V0` through `V39` are published in the governing bytes at §P1-10.7, each with
its expected `STAT_PARSE`, `STAT_OBSERVE` and `PGRP_OBSERVE` result, and each
positive vector with its SHA-256. They include the Y line's four shifted forms,
the X line's `comm`-containing-`)` case, the inclusive boundary integers, all
nine supported state bytes, and the one consumer-dependent vector. **They are
synthetic byte strings constructed from the documented record layout. No `/proc`
was read against any process to produce them, and the superseded v2 packet was
not opened for behaviour.**

---

## §3. `R2` — one global terminal precedence, and total `KG-2` population

### §3.1 The six-phase order

```text
PHASE 1  TABLE STRUCTURE     every entry, current and stale
PHASE 2  GENERATION          every structurally valid entry
PHASE 3  RECORDED PROTECTED  every current-generation entry's recorded group
PHASE 4  FRESH OBSERVATION   every prospective candidate, with KV-6(b) tested
                             IMMEDIATELY after each PRESENT_VALID observation and
                             BEFORE identity, group equality or any other skip
PHASE 5  CANDIDATE VALIDITY  KV-2, KV-3, KV-4, KV-5 over the whole table
PHASE 6  ACTION              sort, deduplicate, signal, with a fresh protected
                             re-check before every individual signal
```

The overlapping `SC`/`KV` precedence is gone. `SC-6` no longer carries a
dominance rule; `SC-10` carries the one total dominance table. **The terminal set
is closed at exactly three** — structural violation, stale generation, forbidden
target — **with exactly two qualifiers**, `FREEZE_NOT_ATTEMPTED` and
`FREEZE_ABANDONED`. The precedence is the phase order and nothing else, so **no
two applicable predicates choose different terminals** and the answer is stated
for every multi-fault pair.

A stale entry is now a **terminal**, not a skip. That is the stricter answer to
`M-3`'s stale/malformed contradiction. `SC-5` remains **exactly seven tokens**;
`KV_STALE_HANDLE` and `KV_FORBIDDEN_TARGET` become per-entry records of a
terminal rather than skips, and no token is added, removed or renamed.

`PHASE 4`'s prospective-candidate set is defined exactly, with **four named
exclusions each carrying its reason and a proof that no signal can follow from
it** — including the honest statement that a `NULL`-recorded-group handle whose
live process sits in a protected group is not detected, and that it is safe
because it grants no scope, not because it was examined.

### §3.2 The totalized population

`KG-2` `P-2` attaches the single population attempt to **exactly one
process-control transition**: the PCS's own evaluation of the `AWAIT_STOP`
operation of §P1-8.3, at the single instant it computes that operation's
`pgid_is_leader` response operand. Nothing populates the field at any other
opcode, step, site or instant.

`P-7` names **six closed handle states**; `P-8` covers every role and every spawn
success and failure; `P-9` covers every ordinary observation result **and** the
wrong-shaped return **and** the non-`OSError` `BaseException`; `P-10` covers
interruption, deadline expiry, `TIMEOUT` reissue, retry exhaustion and
mid-attempt generation invalidation; `P-11` covers release and reap; `P-12`
states what the legitimate population proves. **Every path ends in one named
state and there is no partially populated usable handle.**

---

## §4. `R3` — the complete `OR-4` output, and an honest quarantine

The defect and its repair are **binding-level** and land in post-selection
binding v4. It enumerates **eleven spans** covering every changed source span
outside guarddata, pins exact source bytes and digest and exact replacement bytes
and digest for each, fixes one deterministic non-overlapping splice order that
verifies non-overlap as part of the algorithm, and pins:

```text
FULL RESOLVED OUTPUT   586426 bytes
                       3a88798f8f18a5e2f38108c9873e5b36045c7533126685034ad17a28998dc339
resolved H_BODY        f57002460cc94d5f1c220193459ec662f713e0f5e3a1564f76f1732d4e1830df
resolved H_GUARDDATA   faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426  UNCHANGED
resolved H_NORMATIVE   3bbd378dec0d189d1b4374970a01272b73634c539eb2182773e46ea4cec6811f
```

`D1` and `D2` remain as defence in depth and **their claim is narrowed to exact
listed literal coverage**. The claim that finite literals detect arbitrary
semantic paraphrases is **withdrawn**. The Y line's marker-free paraphrase is
carried in the binding as fixture `MP-1`: it yields zero `D1` and zero `D2`
matches, passes every marker check and the guard-data check, **and fails the
full-output identity check**, which is the proof of the boundary.

**No resolved bytes exist at any path.** The figures above were computed in
memory over a copy and nothing was retained.

---

## §5. `R4` — the accounting, the identities, and the sweep

### §5.1 The four new `M2` rows, in `MS-2` order

```text
a7ec78cca0c7a537c4251a5342d7bb27c63d16de307c2ee2e901d69187d98e17  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9_DRAFT.md
e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_12.md
ca02d4858022fef026fdbbe65dfb07dc7fb1e885563530be27238d7dbcc8a61a  reviews/fable_officina_p1_wb_v2_12_final_x_review.md
92a394a3c3e3126b278a9af1d33740db1a08810de940be6b6be2ab062e1f41a3  reviews/sol_officina_p1_wb_v2_12_final_y_review.md
```

### §5.2 The atomic update

```text
MS-2                              67 -> 71
MS-3                               7      7   unchanged
MS-8 / TS-3 member_count          81 -> 85
composite provenance region       75 -> 79
recorded M2+M3 digests            74 -> 78
member classes                     7      7   only M2 grew
M1 2 + M2 71 + M3 7 + M4 1 + M5 1 + M6 2 + M7 1 = 85
```

Recounted from the produced bytes: `MS-2` carries **71 rows with 71 distinct
paths**, `MS-3` carries **7 with 7 distinct**, their intersection is **empty**,
and the provenance region carries **79 rows with 79 distinct paths**.

### §5.3 Every dependent literal that moved

`MS-9`'s union arithmetic and its `M1`/`M2` disjointness argument; `G-11`'s
input-set sentence, which said **fifty-seven** literal repository paths and now
says eighty-five — **neither line logged it**; `IR-1`, `IR-3` and `IR-4`;
`IR-13` row 38; `CK-4`, `CK-6`, `CK-7` and `CK-13`; `TS-3`, `B7` and `B17`;
`OR-9`; `N-14` and `N-16`; and composite test rows 103, 104, 105, 107, 108 and
115. **Row 108's stale `77` is repaired to `85`** and its 82-entry setup moves to
86; both lines named that literal and both were right that the v2.12 closure
claimed it had moved when it had not.

### §5.4 The live identities

```text
amendment title                 version 1.10
amendment opening               wholly replaces version 1.9, and ALL TEN
                                predecessors — versions 1 through 1.9, counted
                                exactly — become provenance
composite title                 version 1.13
composite opening               a full replacement for version 1.12
composite Cell-1 identity       Version 1.13
DA-1 historical lists           carry composite 1.12 and amendment 1.9
DA-4 live surfaces              amendment v1.10, composite v1.13
MS-1 literal member paths       _AMENDMENT_V1_10_DRAFT.md, _COMPOSITE_V1_13.md
TS-1 pre-selection paths        packet v2.13, amendment v1.10, composite v1.13
A16(d) consuming token          P1_WATCHDOG_V2_13_..._SHA256
OR-4's installed amendment      "the v1.10 amendment is installed"
IR-11 and row 114               name the actual new/current pair and refuse the
                                actual wrong combinations
```

**No live authority surface identifies itself as a predecessor.**

### §5.5 The maintenance sweep

```text
H-4 owner                       CK-7, sole owner of HISTORICAL_BYTE_MOVED
row 106                         exactly ten defined groups (a)..(j)
row 108                         85
CK-13 extra-entry examples      86th
N-16                            85
region lengths                  actual UTF-8 byte counts
state-set provenance            phrased against the STAT_LAYOUT_ID pin, because
                                §P1-2.1 pins no kernel release. The v1.12
                                "5.x and 6.x series" sentence is WITHDRAWN
X-line L-X1                     the encoding sentence is corrected in binding
                                v4: U+2014 twice AND U+00A7 five times
X-line L-X5                     KV-3 now states the ONE carriage rule exactly
X-line L-X7                     answered by named exclusions with proofs, not by
                                a sentence broader than the test
X-line L-X6                     UNRESOLVED AND SAID SO: §P1-7.5 c10 requires a
                                getpgid answer while §P1-3.4 binds no _getpgid.
                                It predates R1..R5, no import surface moves here
author-found, unreported        binding v3's §2.5 said the W-A option token
                                would occur twice in the resolved file; it
                                occurs three times
```

### §5.6 Exact-file accounting

```text
THIS ROUND AUTHORS EXACTLY SIX DELIVERABLES:
  1  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_13_CORRECTION.md
  2  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_10_DRAFT.md
  3  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_13.md
  4  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V4_DRAFT.md
  5  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V4_DRAFT.md
  6  reviews/opus5_officina_p1_wb_v2_13_closure_repair.md

A SEPARATELY ARCHIVED CHAT TRANSCRIPT IS PROVENANCE CREATED BY THE OPERATOR AND
IS NOT A SEVENTH AUTHORED DELIVERABLE. THIS ROUND DOES NOT CLAIM THAT NO SEVENTH
REPOSITORY FILE CAN LATER EXIST. Both lines graded the v2.12 closure's "there is
no seventh" FALSE because the commit carried such a transcript; the claim is not
repeated, and it is replaced by this one, which is about AUTHORSHIP rather than
about the commit's file set.
```

---

## §6. Tokens and invariants

### §6.1 There is no recommendation, because the cell is signed

`W-B` is selected. This packet recommends nothing, compares nothing and predicts
nothing.

### §6.2 The closed validation vocabulary is retained in full

`TS-1` must be able to name **either** option token and **either** paired
amendment token in order to refuse the wrong one. `OR-4` deletes W-A's operative
GRANTS and deletes **no** `TS-1` literal. Deleting one would break `TS-2A` `A8`,
`TS-2A` `A9`, `TS-5` `B14` and `IR-13` row 47 in one stroke, and would also
destroy the joint block's byte identity, which binding §2.2.6 verifies on the
pinned output rather than argues for.

### §6.3 Tokens

```text
SIGNED, NOT REOPENED
  I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
  I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY

RETIRED, MUST NOT BE SIGNED
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7

THE ONE FUTURE ACCEPTANCE TOKEN, NOT SIGNABLE YET
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_10
  It becomes signable only after a bounded independent X-line and Y-line round
  on the v2.13 bytes, and only jointly with composite v1.13 under §A9's single
  atomic handoff. EVEN THEN IT AUTHORIZES NO CODE, NO TEST, NO KEY, NO OR-3, NO
  OR-4, NO INSTALL AND NO ACTIVATION.

NOT ACCEPTED, AND NOT MADE SIGNABLE HERE
  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
```

---

## §7. Independence

The next act is a bounded independent X-line and Y-line review of the **same new
bytes**, performed by reviewers that did not author this round. Neither line's
verdict is predicted here. An X-line confirmation does not neutralize a Y-line
counterexample against the same bytes, and the reverse holds equally; **this
round exists because both lines returned `REVISE` on the previous pair and the
union of their findings governed.**

---

## §8. Negative space

This packet creates nothing executable and authorizes no selection, X/Y verdict,
acceptance, implementation, commit, verifier or manifest edit, key, entropy,
seed, Stage A, Stage B, detached signature, attestation, member list, install
record, `OR` step, process, socket, pipe, fork, exec, signal, wait or `prctl`
operation, capability, world, learner, candidate, trajectory, capacity artifact,
custody disposition, result manifest, spend, datum, outcome, Proof or claim
movement.

No freeze was executed, requested, journalled or witnessed. No `/proc` was read
against any live process. No clock was sampled for any contract purpose. No
Philosophia production or project module was imported, executed or compiled. No
existing file was modified: no historical or governing document, no code, no
test, no signature, no runtime artifact and no prior review.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
WATCHDOG AUTHORITY AMENDMENT V1.10 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

The exact selected token and the formal selection signature govern. This packet
and every author closure are untrusted self-assessments and are normative for
nothing.
