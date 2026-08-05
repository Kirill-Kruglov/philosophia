# Officina P1 W-B v2.11 governing-pair repair — author closure

**Author:** Claude Code Opus 5, **governing-pair repair author only**. Not an
independent X-line or Y-line reviewer, and **not** the reviewer of anything
below. **This closure is an untrusted self-assessment and is normative for
nothing.** Every claim in it is a question put to the independent lines, not an
answer they are bound by.

**Base commit:** `6dda0b3` (`Review W-B binding and governing pair`). Nothing was
committed.

`T = NOT_ACTIVATED`. Programme claim `OPEN`.

---

## §1. Verdict

```text
READY_FOR_OFFICINA_P1_WB_V2_11_FINAL_XY_REVIEW
```

**This token authorizes nothing.** It is not an acceptance, not an
implementation authorization, not an inactive-scaffold authorization, not a key,
not `OR-3`, not `OR-4`, not a one-shot handoff authorization and not an
activation. It states one thing: the bounded round both independent lines
licensed has been performed within its stated scope, and the resulting six
documents are ready to be put to a fresh independent X-line and Y-line round on
identical bytes.

**Why not `REVISE`:** every repair `R1`..`R6` landed, and each was verified
mechanically rather than asserted (§2, §3, §4, §5, §6, §7). **Why not
`BLOCKED`:** nothing in the round required an authorization that does not exist;
the round is documentation-only and produced no key, artifact, code edit or
`OR` step.

---

## §2. Input integrity, and what was created

### §2.1 The seven task-named inputs, recomputed from disk and **matched**

```text
4b7442bd1dafa1ff141212ac8cd59e94983f32633561b6396837ff0767aa48ff  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
86755531f5a7a5f11085802c3e6b5770f4ef5aa90d98ae1a62599348e11f0e8f  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
73d9cfeb4efdfd6a370f369c86162e603ab868acb088455bc9a1873a49b13942  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V1_DRAFT.md
96cda63a70f8498024527323542a762d7d44b353af6781f8091e5b061ee7d440  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V1_DRAFT.md
d8483c185c6f438f4a209353716b7d8aef31529c5f6876381ea03431beb15ba1  reviews/fable_officina_p1_wb_binding_x_review.md
e1bf893a00fc625f97698ddbe9a2f0d4413a8578c65722559f3ddefe7bcd8628  reviews/sol_officina_p1_wb_binding_y_review.md
ffcb4116a9171d873be773138cc2c97547f8ff919a1d71f4cbd46e328eb3a7dc  successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md
```

### §2.2 The six documents created, and nothing else

```text
efe0f908a104060ed01a640fd5c58f5bf9731261dbf07bdc77bf91bc7a9ffdfb  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_11_CORRECTION.md
71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md
d7ccf170b759f89519f24b26bd817d273197dddd0b5208e0d95eecebf59ec91d  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V2_DRAFT.md
a70f6a7774386d7b36084b0e19c5f1e78b11a5e04f2d992d95d93148878c5c6b  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V2_DRAFT.md
                                                                  reviews/opus5_officina_p1_wb_v2_11_governing_repair_closure.md  (this file)
```

Composite v1.11 region digests, by the §P1-14.0 extraction algorithm:

```text
H_BODY       ce728942d3d1a746960a9fbf0feb4a969b79b9793d2b89f67a5d73c9b31b51cf
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426   UNCHANGED FROM v1.10
H_NORMATIVE  01ea73918211509a19126e5847234a4b64d6ffbabf8a064d7051b460949743b8
H_FILE       c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6
```

The independent Y line's guard-data digest `faf2d709…0426`, computed against
v1.10, is **reproduced exactly** against v1.11. The guard-pattern region was not
touched.

---

## §3. Disposition of every finding, one to one

```text
FINDING  LINE   GRADE            DISPOSITION IN v2.11
-------  -----  ---------------  ------------------------------------------
F1       X + Y  MAJOR, EXECUTABLE, FAIL-OPEN
                                 REPAIRED IN GOVERNING BYTES. §4 below.
                                 Every pre-production range is CK-1..CK-15 in
                                 VP-4 order; no CK-1..CK-12 success range exists
                                 in either file; CK-13, CK-14 including B14, and
                                 CK-15 are mandatory before success; H-1..H-4
                                 exist ONCE in one delimited canonical block,
                                 byte-identical in both files at digest
                                 ca2ff30b…a785, with a stated extraction/hash
                                 check; the divergent copies were REPLACED, not
                                 overlaid; the "in full and identically" claim is
                                 narrowed to the two delimited regions and
                                 verified mechanically; the executable
                                 option-mismatch fixture is stated at CK-14
                                 inside the shared block.

F2       X + Y  MAJOR, EXECUTABLE
                                 REPAIRED IN GOVERNING BYTES. §5 below.
                                 KG-1, KG-2, KV-1..KV-6 and SC-1..SC-8 are
                                 defined in full at composite v1.11 §P1-10.7 and
                                 nowhere else; §P1-10.7's SCOPE line and test row
                                 89 resolve only to that definition; the
                                 definition is re-derived from current signed
                                 invariants with a source-trace table; it is
                                 total and fail-closed; the one supporting rule
                                 the pair lacked is defined minimally and tested;
                                 the superseded V2 draft was NOT opened for
                                 behaviour.

Y-M3     Y      MAJOR, BINDING   REPAIRED IN BINDING v2 §2.5 AND §2.6. PO-4's
X-1      X      MAJOR, BINDING   unsatisfiable whole-file token ban is REPLACED
                                 by a canonical permitted-occurrence table with
                                 region, governing rule, literal fragment and
                                 expected count. TS-1's two option tokens and
                                 both paired amendment tokens are RETAINED
                                 (class R rows R-1, R-2), guard-data patterns are
                                 RETAINED byte-identically (R-4), the seven
                                 legitimate supervisor/PCS socket and slot-6 loci
                                 are RETAINED (R-5) — including the three the X
                                 line enumerated — and watchdog slot-6 references
                                 survive ONLY in their closed/absent sense (R-6).
                                 NO WHOLE-FILE "ZERO W-A STRINGS" RULE REMAINS.

Y-M4     Y      MAJOR, BINDING   REPAIRED IN BINDING v2 §2.2 AND §2.6. The
X-2      X      MAJOR, BINDING   transformation is a byte-exact line-by-line
                                 table over the WHOLE Cell-2 span, lines 55..95,
                                 not over the three marker-bearing lines. It
                                 covers the marker-free blocking notice, the
                                 marker-free "selects neither / predicts neither"
                                 assertion, and the marker-free W-A capability
                                 exposition at lines 64..68. The post-selection
                                 result must state that W-B is signed and W-A
                                 rejected (CT-1, CT-2) and must carry no open-cell
                                 assertion (CT-3). PO-9 is a whole-file-minus-
                                 guarddata CONTENT verifier with detectors D1..D4
                                 that see marker-free prose. G-10 remains
                                 body-scoped; guard data remains byte-identical.
                                 X-2's specific correction is adopted: lines 79,
                                 80 and 83 are the notation example and the
                                 convention sentence, NOT the blocking notice,
                                 and v1's labels were wrong.

Y-M5     Y      MAJOR, HANDOFF   REPAIRED IN HANDOFF v2 §H-0. The document is
                                 retitled and re-scoped to INERT ORACLE AND
                                 DECLARATIVE SCAFFOLDING ONLY. It states, in the
                                 first section a reader meets, that it does NOT
                                 implement the runtime W-B EOF route, the PCS
                                 classifier, the descriptor topology or any
                                 process operation, and that those are NOT
                                 implementable under it. Three v1 test paths that
                                 had no implementation under test are REMOVED
                                 from the allowed list. §H11 is the later-stage
                                 authorization table. THE WRITE SCOPE IS NOT
                                 EXPANDED.

X-3      X      MAJOR, BINDING   REPAIRED IN BINDING v2 §3.1 AS GATE 0. Cell 1 is
                                 recorded as a precondition of the composite's
                                 operativeness, with the fact that NO check of
                                 CK-1..CK-15 examines it, and therefore as a
                                 precondition of gate 3, gates 11..15 and gate 17.
                                 THE ROW WAS ADDED TO THE BINDING LEDGER, NOT TO
                                 THE COMPOSITE. The composite's Cell-1 bytes are
                                 unchanged, because X-3 is a binding-level
                                 omission and repairing it in governing bytes
                                 would exceed the licensed scope.

X-4      X      MINOR, LOG       ADOPTED. F3's string is inside the joint block
                                 and lives in BOTH files; v1's amendment-only
                                 framing was wrong and binding v2 PO-8 says so.
                                 The base-commit and capitalization notes are
                                 carried: this closure names the commit that
                                 carries it, and handoff v2 §H12 E-7 no longer
                                 quotes the signature heading.

F3       X + Y  MINOR            REPAIRED. OR-4 reads "the v1.8 amendment is
                                 installed", inside the joint block and therefore
                                 in both files; §A9's audit enumerates FIVE
                                 generation-scoped operative loci and names which
                                 file each lives in.

F4       X + Y  MINOR            REPAIRED. composite line 91 reads §P1-14.4.
                                 §A9's audit is strengthened from "the named
                                 heading exists" to "the named heading is the one
                                 that defines the named rule".

Y log    Y      NON-BLOCKING     ADOPTED. Binding v2 §2A.1 does not duplicate the
                                 O-3 line. Handoff v2 §H12 E-6 and E-7 state that
                                 no key MATERIAL and no signed acceptance
                                 ARTIFACT exists, and that bare string-absence
                                 checks on key_id, public_key_hex and the
                                 acceptance token produce false failures. Handoff
                                 v2 records NO line-number observations of
                                 generic_harness.py at all; §H9 A-2 requires a
                                 fresh reviewed audit as the control.
```

---

## §4. `R1` — the canonical fifteen-check handoff, shown

### §4.1 The two delimited byte-identical regions, extracted and diffed

```text
REGION                              AMENDMENT v1.8    COMPOSITE v1.11
canonical atomic-handoff preamble   lines 1209..1271  lines 6614..6676
  content bytes                     4052              4052
  SHA-256   ca2ff30b93818f7945b442de68438ddaa8f71879443595903fddfa950cf4a785
  DIFF                              ZERO HUNKS

joint install and authorization     lines 1324..4442  lines 3273..6391
  content bytes                     222364            222364
  SHA-256   9bf4a831b138889b4ae71d2985820793f10a649311199ec3136d75a6514babe5
  DIFF                              ZERO HUNKS
```

Both extractions were performed programmatically by the rule stated in the
documents themselves — locate the unique `BEGIN` line, locate the unique `END`
line, concatenate the lines strictly between them each including its `0x0A`, hash
— and the two strings compared equal byte for byte. **Each of the four delimiter
lines occurs exactly once in its file**; the quoted copies inside the extraction
prose are preceded on their own lines by other bytes and therefore fail the
whole-line equality the rule requires, exactly as `§P1-14.0`'s sentinel
construction and `§A0.4`'s anchor grammar already do.

**The identity claim is now narrowed to exactly these two regions, at every locus
that made it**: `DA-5`, `§A9`'s preamble, composite `§P1-14.8`, composite
preamble line 85–87 and composite preamble line 147–149. Prose outside them is
explicitly not claimed to be identical.

### §4.2 The range, at every locus

```text
LOCUS                                    v1.7/v1.10        v1.8/v1.11
amendment §A9 H-3                        CK-1..CK-12       CK-1..CK-15
composite §P1-14.8 H-3                   "fifteen checks"  CK-1..CK-15
  and the two are now ONE BLOCK, so they cannot disagree again
amendment §A10 / composite §P1-14.4      CK-1..CK-15       unchanged
IR-9                                     CK-2..CK-15       unchanged
CK-15                                    CK-1..CK-15       unchanged
FC-1                                     CK-1..CK-15       unchanged
VP-4                                     fifteen steps     unchanged
packet                                   15 UNCHANGED      15 UNCHANGED
```

`CK-1`..`CK-12` occurs three times in each file. **Every one of them is either a
negation or a description of the removed defect** — "NO CK-1..CK-12 SUCCESS RANGE
EXISTS IN EITHER FILE"; "THERE IS NO `CK-1`..`CK-12` SUCCESS RANGE, AND NO OTHER
PROPER PREFIX"; "VERSION 1.7's §A9 STATED THE RANGE AS `CK-1`..`CK-12` WHILE
COMPOSITE v1.10 STATED FIFTEEN". **No operative clause in either file states a
twelve-check range.**

### §4.3 The option-mismatch refusal, shown

The fixture is inside the joint block at `CK-14`, so both files carry it
byte-identically and no closure is its source.

```text
GIVEN   all 77 members present and byte-correct; M4 and M7 genuine; one
        correctly content-addressed install record; one Ed25519 key pair;
        Stage A and Stage B both CANON at their literal paths; a valid
        128-character detached signature over the exact Stage-B bytes under
        Stage A's pinned key.
DIFFER  Stage A selected_option_token = the signed W-B token, correctly paired
        Stage B selected_option_token = the W-A token

CK-2   PASS   TS-2A A8/A9 read Stage A alone; Stage A is a valid W-B selection
CK-3   PASS   TS-5 B1..B13 are self-contained; B12's Ed25519 verification
              SUCCEEDS because the artifact IS validly signed by the one pinned
              key; NONE of B1..B13 reads selected_option_token
CK-4   PASS   member enumeration is a constant of the governing bytes
CK-5   PASS   exactly one install record
CK-6   PASS   the record is structurally valid
CK-7   PASS   every member exists; every digest recomputes
CK-8   PASS   M4 and M7 structurally valid
CK-9   PASS   Stage A against M4
CK-10  PASS   M4's nine semantic relations
CK-11  PASS   install_record_id recomputes
CK-12  PASS   id equalities
CK-13  PASS   the record's members array equals the enumerated set
CK-14  REFUSE  TS-5 B14 -> STAGE_B_OPTION_MISMATCH        <-- FIRST AND ONLY
CK-15  not reached

CONSEQUENCE, STATED AS A REFUSAL OF A VERIFIER AND NOT ONLY OF A STATE:
  a 12-check implementation ADMITS this state and FAILS CONFORMANCE on this
  fixture. A conformance suite that does not contain it is INCOMPLETE.
  The same range also drops CK-13's total member partition, B15, B16, B17's
  external count binding, B18's two governing digests and the whole of CK-15.
```

`IR-13` row 35 remains the sole owner of the `B14` equality; `IR-13` row 47
remains the sole owner of the `A8` option-set relation. **Neither row moved.**
Composite test row 106 carries the same state as fixture group `(k)`, and group
`(i)`'s expected PASS is preserved.

---

## §5. `R2` — `KV`/`SC` in full, with source trace and adversarial fixtures

### §5.1 Where it lives, and the census that made it necessary

```text
"KV" in composite v1.10       2, BOTH references, ZERO definitions
"KV" in amendment v1.7        0
"KV" in packet v2.10          0
"KV" in composite v1.11       11, of which ONE is the definition site at
                              §P1-10.7 and the rest are its own clause names,
                              the SCOPE line and test row 89
"KV" in amendment v1.8        0 — the classifier is a P1-side rule and the
                              amendment does not restate it (DA-3, DA-4)
"SC-1" in composite v1.11     6      "KG-1" in composite v1.11     8
```

### §5.2 The rules, complete

```text
KG-1  PGRP_OBSERVE(pid) -> ABSENT | PRESENT_VALID | UNREADABLE | UNPARSABLE |
      ERROR. ONE full read of /proc/<pid>/stat through the already-bound _open,
      _read and _close. Errno classification EXACTLY §P1-10.3's: ENOENT/ESRCH ->
      ABSENT; EACCES/EPERM -> UNREADABLE; EINTR -> bounded retry at
      T_SUPERVISOR_POLL_INTERVAL_NS to the step deadline, then ERROR; any other
      OSError -> ERROR. From the same buffer: locate the FINAL ")"; the 1st token
      after it is state, the 2nd ppid, THE 3rd THE PROCESS GROUP, the 20th the
      kernel start identity. No final ")", fewer than twenty tokens, or a
      non-integer field -> UNPARSABLE. ONLY PRESENT_VALID CONTRIBUTES.
KG-2  pgid_or_null is NULL at handle creation and is written at EXACTLY ONE
      place, after a kernel verification of §P1-7.5 c10's shape — PRESENT_VALID,
      recorded start identity equal, observed group equal to the pid itself — at
      which instant pgid_or_null := that pid, NEVER WRITTEN AGAIN. The legitimate
      population is exactly the group-leader pids of this PCS's own
      current-generation children; never a request operand, never a record,
      never re-derived, never widened, never repaired.
KV-1  h is in the PCS's own handle table AT THIS INSTANT and h.generation_id is
      the running generation's.
KV-2  h.role in {CONTROLLER, WORKER}; h.ownership exactly OWNED; h.state not
      REAPED; h.pgid_or_null an integer and not NULL.
KV-3  ONE FRESH KG-1 observation of h.pid taken AT THIS INSTANT; PRESENT_VALID
      required; no stored, cached, inherited or earlier observation qualifies.
KV-4  the observed start_identity equals the recorded one exactly. ON MISMATCH:
      FAIL *AND* OWNERSHIP(h.pid) := CONTRADICTED IRREVERSIBLY, per §P1-10.1's
      fourth trigger and §P1-10.4 row I-2. No signal to that pid or its group
      again, ever.
KV-5  the pgrp of THE SAME observation equals h.pgid_or_null exactly.
KV-6  g is NONE of: (a) the PCS's own process group, obtained by one KG-1
      PGRP_OBSERVE(_getpid()) at this instant, and if that observation is not
      PRESENT_VALID KV-6 FAILS CLOSED; (b) for EVERY WATCHDOG handle w, BOTH
      w.pgid_or_null when non-null AND w.pid; (c) the recorded supervisor group
      — SPAWNING_GROUP.json's process_group_id, verified at c10, named as the
      §P1-4.6 group anchor, required by c14 to equal the supervisor's group.
      A HIT IS A STRUCTURAL FAULT, NOT A NON-TARGET, AND IT TERMINATES.
SC-1  candidate set = the PCS's own handle table for the running generation.
      No path, record, operand, peer artifact, directory scan or /proc
      enumeration contributes. No discovery step.
SC-2  project to pgid_or_null; deduplicate by integer equality keeping the
      first; sort ASCENDING. Two conforming implementations produce the same
      sequence, order and length. A shared group is signalled ONCE per signal.
SC-3  KV-1..KV-6 evaluated IN FULL, IN ORDER, IMMEDIATELY BEFORE EVERY _killpg,
      SEPARATELY FOR EVERY SIGNAL NUMBER, against a fresh KV-3 observation.
      NOTHING MEMOIZED; hoisting the predicate out of the loop is nonconforming.
SC-4  no _killpg on any failed predicate; no partial, best-effort, warning,
      retry-on-refusal or override mode.
SC-5  the closed result-token set, EXACTLY SEVEN: KV_OK, KV_STALE_HANDLE,
      KV_ROLE_OR_STATE_REFUSED, KV_OBSERVATION_UNAVAILABLE,
      KV_IDENTITY_CONTRADICTED, KV_GROUP_MISMATCH, KV_FORBIDDEN_TARGET.
      P1-owned journal tokens only; never evidence, never a covariate, never an
      endpoint, never a peer-predicate input. NOT members of FC-1's 25 codes.
SC-6  first-failure evaluation gives every candidate EXACTLY ONE token.
      KV-1..KV-5 failures SKIP the group (KV-4 additionally setting
      CONTRADICTED). KV-6 failure TERMINATES THE WHOLE CLASSIFIER: no further
      signal of any number to any group in this or any later pass, one terminal
      PCS_FREEZE_CLASSIFIER_FORBIDDEN_TARGET, generation routes to §P1-11.6.
      KV_FORBIDDEN_TARGET DOMINATES EVERY OTHER TOKEN.
SC-7  total over 3 x 4 x 3 x 2 = 72 tuples plus the orthogonal stale-generation
      case, by an ORDERED rule list: stale generation -> KV_STALE_HANDLE; role
      WATCHDOG -> refused (24); ownership CONTRADICTED or REAPED -> refused (32);
      state REAPED -> refused (4); pgid NULL -> refused (6); remainder ->
      proceed to KV-3 (6). 24 + 32 + 4 + 6 + 6 = 72, first match wins, no tuple
      unclassified and no tuple with two answers.
SC-8  any value outside §P1-8.5's signed sets, a pgid that is neither NULL nor
      an int under `type(x) is int` so bool is rejected, a handle table that is
      not a mapping, a malformed KG-1 return, or any BaseException, is
      STRUCTURAL_VIOLATION under §P1-10.2: never death, never REAPED, set
      CONTRADICTED irreversibly where a pid is identifiable, no signal ever
      again, no record installed, modified or removed, and terminate the
      classifier as SC-6's KV_FORBIDDEN_TARGET does. NO DEFAULT-ALLOW PATH AND
      NO "UNKNOWN, PROCEED" BRANCH EXISTS.
```

### §5.3 The source trace, and the derivation discipline

Composite v1.11 §P1-10.7 carries a **source-trace table** naming, for each of
`KG-1`, `KG-2`, `KV-1`..`KV-6` and `SC-1`..`SC-8`, the current live clauses it
comes from: §P1-3.4, §P1-3.6, §P1-4.6, §P1-5.1, §P1-7.5 `c10`/`c11`/`c14`,
§P1-8.5, §P1-8.6 `J2`, §P1-10.1, §P1-10.2, §P1-10.3, §P1-10.4 rows `I-2` and
`I-5`..`I-8`, §P1-10.5, §P1-10.6, §P1-11.4, §P1-12.1, §P1-10.7's own `SCOPE`,
`MEDIATION` and publication-boundary lines, `VP-3` and `VP-4`.

**The superseded `…AUTHOR_CHOICE_PACKET_V2_DRAFT.md` was not opened for
behaviour, at any point, in this round.** No clause above depends on its
content, none of it is restated, and the prohibition the X line identified —
`DA-4`'s closure of the behaviour-bearing surfaces to exactly two, reinforced by
`DA-2` and `IR-12` — was the controlling rule.

### §5.4 The one supporting rule, and what it costs

`KG-1`'s process-group field is the **only** thing the live pair did not already
carry. It is the smallest such rule: the same single `/proc/<pid>/stat` read
`§P1-10.3` already performs, through the same three already-bound primitives,
under the same errno classification, taking **one additional already-present
token** from the same buffer — the 3rd after the final `)`, where `§P1-10.3`
already takes the 20th.

```text
§P1-10.3 STAT_OBSERVE                     UNCHANGED; every consumer unchanged
§P1-3.4 primitive binding                 UNCHANGED; no new primitive, and
                                          _getpgid is NOT bound and is NOT used
§P1-3.2 scoped import allowlists          UNCHANGED; no name added
MS-11 reachable_closure                   UNCHANGED; 89 rows, length 20534,
                                          digest aa974e0c…c20ee
MS-13 project-import dependency surface   UNCHANGED
S-12 and the PCS sole-caller rule         RETAINED; KG-1 calls no fork, wait,
                                          kill or killpg primitive
FC-1's 25 closed failure codes            UNCHANGED
```

**Safety was not weakened anywhere to avoid a supporting definition**, and no
reference to an undefined `KV`, `SC`, token or table remains in either file.

### §5.5 The adversarial safety fixtures

Composite test row 89 is extended — the row already owns site (b) — to require a
build to FAIL if any of the following is admitted:

```text
a _killpg authorized by a KV-3 observation taken before an earlier signal of the
  same schedule rather than at that instant                              (SC-3)
a _killpg for signal 9 authorized by an evaluation performed for signal 15 (SC-3)
a WATCHDOG-role handle reaching any _killpg at any state or ownership     (KV-2)
a handle with ownership CONTRADICTED or REAPED, state REAPED, or a NULL
  pgid_or_null reaching any _killpg                              (KV-2, SC-7)
a start-identity mismatch that skips the group WITHOUT setting OWNERSHIP to
  CONTRADICTED irreversibly                                              (KV-4)
a recorded group that differs from the freshly observed pgrp being signalled
  anyway                                                                 (KV-5)
a scope containing the PCS's own process group          -- must TERMINATE (KV-6)
a scope containing a watchdog leader group or watchdog pid -- must TERMINATE
a scope containing the recorded supervisor group        -- must TERMINATE
a KG-1 result other than PRESENT_VALID authorizing any signal            (KV-3)
a role/state/ownership/pgid value outside the signed sets taking any path other
  than SC-8's structural-violation continuation                          (SC-8)
a scope sequence that is not the deduplicated ascending sequence         (SC-2)
any token outside SC-5's closed set of seven                             (SC-5)
```

Composite test row 101 is extended to name `SC-5`'s seven tokens literally and
to require that no eighth exists and that none reaches a peer artifact.

**No test-matrix row was added, renumbered or removed.** `MS-6`'s 92..103 /
104..115 split, `MS-7`'s `rows_attested` 92..115, `row_count` 24 and
`all_rows_passed` true are byte-unchanged.

---

## §6. `R3` — the eight-row accounting, proved

### §6.1 The eight rows, in `MS-2` order, each digest recomputed from disk

```text
1  d5e1d4dbd7731bd6a154c423b36f41e60de771d5ff635423b608bba02d88640f  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_6_DRAFT.md
2  3ce26ba63ca1546ddd7c8422ccf5a4e71e05678e58d1f3deca18e24668e4c1ad  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_9.md
3  588fe8a23fd56a4366f920d4b1463d00ee3e7bd8bbc4cc1cbaca61b89a12f489  reviews/fable_officina_p1_watchdog_v2_9_independent_x_confirmation.md
4  6d83e9b2f082354917b134955d35b8b8f1fdf76761b368c8d34ffae3cd99cf66  reviews/sol_officina_p1_watchdog_v2_9_final_y_confirmation.md
5  4b7442bd1dafa1ff141212ac8cd59e94983f32633561b6396837ff0767aa48ff  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
6  86755531f5a7a5f11085802c3e6b5770f4ef5aa90d98ae1a62599348e11f0e8f  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
7  0998fce3b881e0d0d1947c450b442821047f040a4bdd4a987a1a091ece3a56f7  reviews/fable_officina_p1_watchdog_v2_10_targeted_x_confirmation.md
8  90fb9f9155926df89e9993de1146c05e279639469d7bf2a60c63c6419bc37e52  reviews/sol_officina_p1_watchdog_v2_10_targeted_y_confirmation.md
```

Rows 1–4 are the set `N-14` of the v1.7 amendment named and deferred. Rows 5–8
are this replacement round's own. **The two later W-B binding reviews were not
substituted for rows 7 and 8** and are members of nothing.

### §6.2 The counts, recounted from the produced bytes

```text
                                      v2.10   v2.11   VERIFIED HOW
MS-2 literal rows                        55      63   counted by regex over the
                                                      MS-2 list: 63 rows matched
MS-3                                      7       7   unchanged
MS-8 arithmetic  M1 2 + M2 63 + M3 7 + M4 1 + M5 1 + M6 2 + M7 1 = 77
MS-8 total                               69      77
TS-3 member_count literal                69      77
TS-5 B7 literal                          69      77
TS-5 B17 literal                         69      77
composite provenance digest rows         63      71   counted by regex over the
                                                      region: 71 rows matched
MS-9 P(M2)                               55      63
MS-9 inspected literal strings           64      72
MS-9 union         2+63+7+1+1+2+1 = 77 distinct paths
member classes                            7       7   only M2 grew
```

**A whole-file scan of both governing files for a bare `55` or `69` outside a
hexadecimal digest returns five hits, and every one is legitimate:** the two
`reachable_closure` rows numbered 55 and 69 (preserved byte for byte), the two
test-matrix rows numbered 55 and 69, and one sentence of the composite's own
accounting note that states the transition `63 rows to 71` and `55 to 63`.

### §6.3 Everything the eight rows moved

Enumerated in packet v2.11 §4.3 and re-checked here: `MS-1`, `MS-2`, `MS-8`,
`MS-9` (four sites plus the rewritten `M1`-against-`M2` argument), `MS-13.3`,
`IR-1`, `IR-3`, `IR-4`, `IR-11`, `IR-13` rows 24 and 38 and the `K6`/`K7`
coverage note and the `B7` coverage row, `TS-1`'s three pre-selection paths,
`TS-2B` `A16(d)`, `TS-3`, `TS-5` `B7` and `B17`, `OR-4`, `OR-9`, `CK-4`, `CK-6`,
`CK-7`, `CK-13` (five sites), `CK-14`'s new fixture, `FS-1`, `TR-1`, the
composite's `§P1-18` prose and region list, and composite test rows 103, 104,
105, 106, 107, 108, 114 and 115.

Every generation-scoped path, anchor token, hash and consumer advanced
consistently to **v2.11 / v1.8 / v1.11**:

```text
MS-1 path 1     ..._AMENDMENT_V1_8_DRAFT.md
MS-1 path 2     ..._COMPOSITE_V1_11.md
TS-1 packet     ..._PACKET_V2_11_CORRECTION.md
TS-1 amendment  = MS-1 path 1        TS-1 composite = MS-1 path 2
§A0.4 token     P1_WATCHDOG_V2_11_PRE_SELECTION_COMPOSITE_SHA256
A16(d) token    the same string, inside the joint block, in BOTH files
OR-4            "the v1.8 amendment is installed"          [F3]
acceptance      I_ACCEPT_..._AMENDMENT_V1_8
anchor value    c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6
                = composite v1.11's H_FILE, verified equal
anchor lines matching A16(d)'s grammar in the amendment: EXACTLY ONE
complete anchor-token names carrying segments 8, 9 or 10, in either file: ZERO
```

---

## §7. `R4` — the transformation and the permitted-occurrence census

### §7.1 The marker census, recomputed against composite v1.11

```text
MARKER-BEARING LINES, composite v1.11   20   79 80 83 305 306 1656 1659 1666
                                             1670 1907 1910 1932 1933 2531 2814
                                             2820 6747 6775 6786 6885
MARKER-BEARING LINES, amendment v1.8     0
"[W-A]" OCCURRENCES                     13
"[W-B]" OCCURRENCES                     13

REGION        RANGE          LINES   A    B
  PREAMBLE    1..250            3    2    2
  BODY        252..6844        16   10   10
  GUARDDATA   6848..6887        1    1    1
                              ----  ---  ---
                               20   13   13

BOTH-MARKER LINES, WHOLE FILE   6   83, 2531, 6747, 6775, 6786, 6885
BOTH-MARKER LINES, BODY ONLY    4   2531, 6747, 6775, 6786
```

The X line's independently reproduced 3 / 16 / 1 split, 13 / 13 counts and 6 / 4
both-marker numbers are **reproduced exactly** against the new bytes. The four
both-marker body lines must be edited in place; a line-deletion strategy is wrong
on its face.

### §7.2 The complete Cell-2 transformation

Binding v2 §2.2 gives a **line-by-line, byte-exact table over lines 55..95**,
with an action for every line, not for the three marker-bearing ones. It
disposes of:

```text
LINES 57-58   THE BLOCKING NOTICE ITSELF — marker-free, and v1's table did not
              reach it. REPLACED; the notice is discharged.
LINES 60-62   "What remains open is the mechanism ..." — marker-free. REPLACED.
LINES 64-68   THE W-A CAPABILITY EXPOSITION — marker-free, carrying the W-A
              option token, the slot-6 socket grant, the t-wd-freeze.v1 frame
              and the bounded service window. DELETED ENTIRELY. v1's table did
              not contain these lines at all.
LINE  69      the blockquote separator. DELETED with 64-68.
LINES 70-73   the W-B exposition. REPLACED as the SIGNED RESULT, not as one of
              two offers.
LINES 75-76   "This document selects neither and predicts neither." —
              marker-free, and FALSE after the signature. REPLACED.
LINES 78-82   the notation example and its fence. DELETED.
LINES 83-88   the convention sentence (BOTH markers) and the OR-4 reference.
              REPLACED, retaining the handoff reference in substance.
LINES 88-91   "The resulting file carries no variant block at all ..." REPLACED
              in the perfect tense.
LINES 58-60, 63, 74, 77, 92-95   RETAINED — marker-free and still true.
```

The result must satisfy `CT-1`..`CT-6`: it **states that W-B is signed**, names
the token and the signature digest; it **states that W-A is rejected** while
stating **no W-A capability**; it carries **no open/unsigned/undecided
assertion**; it carries no marker; it leaves **Cell 1 untouched**; and it adds
no normative rule.

### §7.3 The permitted-occurrence census

```text
CLASS R — RETAINED AND REQUIRED
R-1  I_SELECT_..._FREEZE_A_...     BODY, joint block, line 5145   TS-1 grammar
                                   required by TS-1, A8, B14, IR-13 row 47
R-2  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
                                   BODY, joint block, line 5151   TS-1 pairing
                                   required by TS-1, A9
R-3  I_SELECT_..._FREEZE_A_...     BODY, joint block, line 6059   CK-14 fixture
                                   NEW IN v2.11; a zero-token rule would delete
                                   the fixture that protects the signed choice
R-4  "[W-A]" and "[W-B]"           GUARDDATA, line 6885, 1 each, byte-identical
                                   required by §P1-17, AD-1, G-10, G-6
R-5  the seven legitimate supervisor/PCS loci, all BODY, all RETAINED:
       395   descriptor-table note, option-independent
       601   §P1-3.4 _socketpair binding
       606   §P1-3.4 _AF_UNIX _SOCK_SEQPACKET constants
       847   _socketpair descriptor-inheritance note
      1352   the SUPERVISOR's AF_UNIX/SOCK_SEQPACKET pair inherited to slot 6
      1354   why SOCK_SEQPACKET was chosen
      6728   row 42, the same grant as a test row
     v1's U-5 WOULD HAVE FAILED ON AT LEAST THREE OF THESE, as both lines said
R-6  watchdog slot-6 references in CLOSED/ABSENT sense ONLY: lines 2814..2817
     ("Slot 6 is not used and is explicitly closed by a file action") and 6786
     (row 99's [W-B] descriptor set). Two loci, no others.
R-7  B14, IR-13 row 35 and IR-13 row 47 RETAINED VERBATIM — preserved by
     construction, since OR-4 touches no line inside the joint block.

CLASS F — FORBIDDEN, EXPECTED COUNT ZERO
F-1  W-A operative grants at operative preamble or body loci
F-2  t-wd-freeze.v1 — 9 pre-resolution occurrences, ALL inside a W-A branch or
     the Cell-2 W-A exposition; NOT in TS-1's vocabulary and NOT in guard data,
     so unlike the option tokens it can be, and must be, eliminated whole
F-3  surviving [W-A]-branch content at any of the 19 non-guarddata loci
F-4  open-cell assertions about Cell 2, detected by PO-9 D1

ARITHMETIC IN THE RESOLVED FILE
  W-A option token         3 pre-resolution -> 2 retained (5145, 6059);
                           line 64 deleted with the Cell-2 W-A exposition
  W-A amendment token      1 pre-resolution -> 1 retained (5151)
  t-wd-freeze.v1           9 pre-resolution -> 0
  "[W-A]"/"[W-B]" outside GUARDDATA        -> 0 / 0
  "[W-A]"/"[W-B]" inside GUARDDATA         -> 1 / 1, H_GUARDDATA unchanged
  watchdog-sense slot 6    2 loci, both closed/absent
  supervisor-sense loci    7, unchanged
```

**No whole-file "zero W-A strings" rule exists anywhere in binding v2.** The
contradiction both lines found is removed by construction, not by an exception.

### §7.4 `PO-9`, the whole-file-minus-guarddata content verifier

Detectors `D1` (open-cell assertions, including marker-free prose), `D2`
(rejected W-A operative grants, including marker-free prose, scoped to exclude
class R), `D3` (class-R presence, so a resolution cannot satisfy `D1`/`D2` by
deleting a required occurrence) and `D4` (`H_GUARDDATA` = `faf2d709…0426`).

`D1`'s pattern list must be **derived line by line from the pre-resolution
Cell-2 span**, so that every assertion the transformation discharges has a
detector; a list that does not cover every `REPLACE` row is reported
**INCOMPLETE**. The list lives **in the oracle**, not in the composite: this
round adds **no** normative surface to the governing bytes and **no** new
guard-pattern class. **`G-10` remains body-scoped and `§P1-17` is unchanged.**

---

## §8. `R5` and `R6` — the scaffold, and identity

### §8.1 The honestly narrowed scaffold

Handoff v2's first section, before any path list, states that the document
scopes **inert oracle and declarative scaffolding only**, and that it does **not**
implement and **cannot** implement the runtime W-B EOF route, the PCS classifier,
the descriptor topology, the supervisor freeze routes or any process operation.

```text
ALLOWED, AND ONLY AFTER AN INACTIVE-SCAFFOLD AUTHORIZATION THAT DOES NOT EXIST
  src/philosophia/officina/p1_wb_oracle.py       pure, in-memory, no I/O
  src/philosophia/officina/p1_wb_contract.py     pure data, no I/O
  tests/test_officina_p1_wb_oracle.py            dummy tests
  tests/test_officina_p1_wb_contract.py          dummy tests
  tests/fixtures/p1_wb/                          deterministic, test-only
  a per-test temporary root

REMOVED FROM v1's ALLOWED LIST, AND THE REMOVAL IS THE REPAIR
  tests/test_officina_p1_wb_classifier_ordering.py
  tests/test_officina_p1_wb_negative_surface.py
  tests/test_officina_p1_wb_disposable_integration.py
  each had no implementation under test; the third additionally implied
  process-control smoke, which §H1 R-5 now forbids outright and everywhere

FROZEN, UNCHANGED FROM v1 AND RE-VERIFIED
  the two governing files; the five §P1-3.1 production roots; MS-5's baseline
  verifier; both MS-6 modules; every TS-1/TS-3/M4/M7/install path; the four
  MS-13 project modules; every M2 and M3 path; every prior review and signature;
  and all unrelated dirty and untracked working-tree files

ABSOLUTE
  NO test_p1_row_NNN_ FUNCTION MAY BE CREATED, anywhere, before OR-5 and OR-7
  NEITHER MS-6 MODULE MAY BE CREATED before OR-5
  NO real process-control smoke, syscall, key, artifact or shared runtime tree
  THE UNTRACKED generic_harness.py REMAINS NON-EVIDENCE, is not adopted, is not
    edited, and was NOT READ BY THIS ROUND. Handoff v2 records no line-number
    observation of it and requires a FRESH, RECORDED, SEPARATELY REVIEWED AUDIT
    against the v1.8/v1.11 bytes before any P1 reuse.
```

Handoff v2 §H11 is the **later-stage authorization table**, naming for each
excluded surface exactly what separate authorization it needs after governing
acceptance: an inactive-scaffold authorization, a **distinct** runtime
implementation authorization, a reviewed `generic_harness.py` audit disposition,
the one-shot atomic-handoff authorization, and finally a separate `T` activation
act. **None exists, and the write scope was not expanded by this round.**

### §8.2 The identity disposition, preserved exactly as ruled

```text
THIS W-B-ONLY BINDING CONTAINS NO IDENTITY OBSERVATION CODE. Recomputed against
  the new bytes: attested_pid and attested_pgid occur ZERO times in composite
  v1.11 and ZERO times in amendment v1.8.
IT IS NOT THE LATER XS-1 COMBINED BINDING. XS-1 defines that binding by (a)..(d);
  this one does (a) only, in XS-1's own register, and performs neither (c) nor
  (d).
P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 REMAINS UNACCEPTED. This round does
  not accept it, make it signable or predict it.
THE LATER COMBINED IDENTITY BINDING REMAINS BLOCKED_PENDING_IDENTITY_WEAKENING_
  REVIEW, pending its own review.
CELL 1 IS RECORDED AS GATE 0 of the binding ledger, as a precondition of the
  composite's operativeness that NO check of CK-1..CK-15 examines. THE ROW WAS
  ADDED TO THE LEDGER, NOT TO THE COMPOSITE.
```

### §8.3 The acceptance token, version-bumped

```text
I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8
```

**The v1.7 token is retired and must not be signed**: `R1` and `R2` changed the
bytes it would have accepted. **Even a future signature of the v1.8 token
authorizes neither code edits nor `OR-3`, keys, `OR-4`, install or activation.**
A separate inactive-scaffold authorization and a separate later atomic-handoff
authorization remain required, and they are separate from each other.

---

## §9. Hashes, regions, stale-string sweep and preserved boundaries

### §9.1 Hashes and regions

```text
amendment v1.8   H_FILE  71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c
                 4575 lines; joint block 1324..4442; handoff block 1209..1271;
                 §A0.4 anchor line: exactly one match of A16(d)'s grammar
composite v1.11  H_FILE  c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6
                 7095 lines
                 BODY-BEGIN 251        BODY-END 6845
                 GUARDDATA-BEGIN 6847  GUARDDATA-END 6888
                 PROVENANCE-BEGIN 6890 PROVENANCE-END 7094
                 sentinel cardinality: exactly one each; order valid
                 H_BODY       ce728942d3d1a746960a9fbf0feb4a969b79b9793d2b89f67a5d73c9b31b51cf
                 H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
                 H_NORMATIVE  01ea73918211509a19126e5847234a4b64d6ffbabf8a064d7051b460949743b8
handoff block    ca2ff30b93818f7945b442de68438ddaa8f71879443595903fddfa950cf4a785    4052 bytes
joint block      9bf4a831b138889b4ae71d2985820793f10a649311199ec3136d75a6514babe5  222364 bytes
```

### §9.2 The stale-string sweep

```text
SWEPT AND ZERO IN BOTH FILES
  P1_WATCHDOG_V2_8_PRE_SELECTION_COMPOSITE_SHA256          0
  P1_WATCHDOG_V2_9_PRE_SELECTION_COMPOSITE_SHA256          0
  P1_WATCHDOG_V2_10_PRE_SELECTION_COMPOSITE_SHA256         0
  "(`G-10`, §P1-14.3)"                                     0
  any operative CK-1..CK-12 range                          0
  "the v1.3 amendment" INSIDE EITHER JOINT BLOCK           0
    and "the v1.8 amendment is installed" occurs once per file, inside it
  __ANCHOR__, __TOKCOUNT__, __H_HANDOFF__ placeholders     0

SWEPT AND REPAIRED
  composite "full replacement for version 1.8"       -> version 1.10
  composite "Version 1.9 does not accept ..."        -> Version 1.11
  composite authority level 3 predecessor lists      -> through composite 1.10
                                                        and amendment 1.7
  amendment DA-1's two version lists                 -> the same
  amendment replacement chain "all seven"            -> version 1.7, all eight
  amendment DA-4's two surface names                 -> v1.8 / v1.11
  acceptance token and reviewer-independence range   -> V1_8, v2.3 through v2.11

DELIBERATELY RETAINED, AND WHY
  AMENDMENT_V1_7 occurs once in the amendment and twice in the composite: as an
    MS-2 provenance row, as MS-9's disjointness argument, and as the composite's
    provenance-region row. All three are correct.
  CK-1..CK-12 occurs three times per file, every one a negation or a description
    of the removed defect. §4.2 lists them.
  "the v1.3 amendment" survives TWICE in the amendment, both inside §A0.3's R4
    narrative and §A9's five-locus audit, each quoting the repaired string in
    order to name what was wrong. Neither is inside a joint block and neither is
    operative.
  the retired anchor-token generation segments survive only inside ellipsised
    narrative sentences of §A0.4 that describe what version 1.6 did; none is a
    token name and none can match A16(d)'s grammar.
```

### §9.3 Preserved boundaries — verified, not asserted

```text
the signed W-B selection and its sensor-only semantics       NOT REOPENED
the 89-row reachable_closure VALUE, CANON length 20534,
  digest aa974e0c…c20ee, the 14-row bootstrap subset and
  the seven unexecuted branches                              BYTE-UNCHANGED
the project-import dependency surface MS-13                  BYTE-UNCHANGED
CK-13's D1/D2 partition, FC-1's 25 codes, B14's semantics
  and IR-13's K1..K5 relation-class boundary                 UNCHANGED
A0.4's honest rollback limitation, FS-1..FS-5, TR-2(a),
  TR-2(b) and row 106(i)'s expected PASS                     UNCHANGED
identity Option A selection and its unaccepted weakening     UNCHANGED
scientific contracts, the T envelope, programme claims       UNTOUCHED
T = NOT_ACTIVATED, programme claim OPEN                      UNCHANGED
MS-6's two modules and the 92..103 / 104..115 split          UNCHANGED
MS-7's rows_attested 92..115, row_count 24, all_rows_passed  UNCHANGED
the seven member classes                                     UNCHANGED
H_GUARDDATA and the VARIANT_MARKER class                     BYTE-UNCHANGED
```

### §9.4 Negative confirmation for this round

```text
EXACTLY SIX FILES WERE CREATED — the five successor documents of §2.2 and this
closure. NO existing file was modified, staged, reverted or deleted: no
governing document, no historical document, no code, no test, no signature, no
runtime artifact, no prior review and no unrelated dirty or untracked
working-tree file. NOTHING WAS COMMITTED. `git status` shows the five new
successor paths as untracked and every pre-existing modification and untracked
file exactly as it stood at the base commit.

No key, entropy, seed, Stage A, Stage B, manifest, attestation, member list,
install record or detached signature was created, requested or predicted. NO OR
STEP RAN; OR-4 DID NOT RUN, and no resolved amendment or composite bytes exist
at any path. No amendment was accepted. No identity token was accepted and no
bounded weakening was authorized under any name. No implementation, install or
activation was authorized.

No test was run. No Philosophia production or project module was imported,
executed or compiled. No process, socket, pipe, fork, exec, signal, wait or
prctl operation was performed. No /proc was read against any live process. No
clock was sampled for any contract purpose.

The untracked src/philosophia/officina/generic_harness.py WAS NOT READ, not
adopted, not edited and not cited by any document of this round.

The superseded OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md WAS
NOT OPENED FOR BEHAVIOUR. No clause of the KV/SC definition depends on it and no
part of it is restated anywhere.

Scratch files used for extraction, diffing and digest recomputation were written
only under the session scratchpad, never under the repository.
```

### §9.5 Log items — not repaired, and why

```text
L-1  H-4 of the canonical handoff block says "`OR-11` and `CK-12` verify this
     and refuse on any difference with HISTORICAL_BYTE_MOVED". HISTORICAL_BYTE_
     MOVED is owned by CK-7, not CK-12. THIS TEXT IS CARRIED VERBATIM FROM BOTH
     v1.7 AND v1.10, WHERE IT WAS ALREADY BYTE-IDENTICAL, AND NEITHER
     INDEPENDENT LINE RAISED IT. It is not one of R1..R6. Repairing it silently
     inside a block whose whole point is that it now has one canonical copy
     would be an unlicensed substantive edit, so it is REPORTED HERE and put to
     the reviewers as Q7 rather than changed.
L-2  Composite line 94's "a finished replacement for v1.2" inside the Cell-2
     paragraph is stale by many generations. It sits inside the span that the
     OR-4 Cell-2 transformation of binding v2 §2.2 leaves RETAINED, so a
     reviewer may reasonably ask whether the transformation should replace it.
     It is REPORTED, not changed, because it is not a generation-scoped
     OPERATIVE string of the §A9 audit's five classes.
```

---

## §10. Bounded X/Y questions

These are the **only** questions this closure puts, and they are bounded to the
`R1`..`R6` repairs and to implementation-scaffold eligibility. **A reviewer is
bound by none of the answers this closure implies.**

```text
Q1   R1, THE CANONICAL BLOCK. Extract the canonical atomic-handoff preamble
     block from both files by the stated rule and diff them. Is the result
     byte-identical, and does H_HANDOFF equal ca2ff30b…a785? Is the delimiter
     cardinality exactly one per line per file, and do the quoted copies inside
     the extraction prose correctly fail whole-line equality? Is the narrowing
     of the "in full and identically" claim to exactly two delimited regions
     complete — that is, does any sentence in either file still assert a broader
     identity than the bytes support?

Q2   R1, THE RANGE AND THE FIXTURE. Is every operative pre-production range
     CK-1..CK-15? Are the three surviving CK-1..CK-12 mentions per file all
     negations or historical descriptions, with none operative? Does the CK-14
     fixture, as stated in the joint block, correctly trace CK-2..CK-13 as
     passing and B14 as the first and only refusal? Is stating the fixture
     inside the joint block — rather than as a new test-matrix row — the right
     placement, given that adding a row would perturb MS-6's membership rule and
     MS-7's rows_attested?

Q3   R2, THE KV/SC DEFINITION. Is KG-1 + KG-2 + KV-1..KV-6 + SC-1..SC-8 TOTAL
     and FAIL-CLOSED? Specifically: does SC-7's ordered rule list partition all
     72 tuples with no residue and no double answer; does SC-8 leave no
     default-allow path; and does KV-6's whole-classifier termination correctly
     dominate every skip? Is the source-trace table honest — does every rule
     follow from the current clauses it names, with nothing imported from a
     superseded document?

Q4   R2, THE SUPPORTING RULE. Is KG-1 the SMALLEST supporting rule that makes
     the predicate decidable? In particular: is reading the 3rd token after the
     final ")" from the SAME /proc/<pid>/stat buffer §P1-10.3 already reads a
     smaller change than binding _getpgid, which §P1-3.4 does not bind? Does
     KG-1 perturb §P1-3.2's scoped allowlists, MS-11's 89 rows, MS-13 or S-12 in
     any way? Is KG-2's population and immutability rule sound against §P1-7.5
     c10/c11 and §P1-8.5's "kernel-verified group"?

Q5   R3, THE ACCOUNTING. Recompute the eight digests and confirm the exact
     paths. Are MS-2 63, MS-8 77, TS-3/B7/B17 77 and the provenance region 71
     internally consistent across every dependent literal, with none missed? Is
     the decision to enter both four-row sets in ONE update correct, and is the
     refusal to substitute the two W-B binding reviews for the v2.10
     pair-confirmation rows correct?

Q6   R4, THE TRANSFORMATION AND THE CENSUS. Does binding v2 §2.2's line-by-line
     Cell-2 table reach every marker-free assertion the signature discharges —
     the blocking notice at 57-58, "what remains open" at 60-62, the W-A
     exposition at 64-68 and "selects neither" at 75-76? Is the permitted-
     occurrence table of §2.5 exact and mechanical, and does it contain no rule
     that contradicts TS-1, IR-13 row 47, the CK-14 fixture or the guard data?
     Is PO-9's D1/D2/D3/D4 construction sufficient to detect marker-free
     open-cell prose and marker-free W-A grants WITHOUT firing on class R?

Q7   THE H-4 LOG ITEM, L-1. H-4 attributes HISTORICAL_BYTE_MOVED to CK-12 where
     CK-7 owns it. The text is carried verbatim from both v1.7 and v1.10, was
     already byte-identical there, and was raised by neither line. WAS IT RIGHT
     TO REPORT IT RATHER THAN REPAIR IT, given that it now sits inside the one
     canonical copy? If a reviewer judges it a Major, it is a governing defect
     and this round should be revised; if Minor, name the round that should
     carry it.

Q8   IMPLEMENTATION-SCAFFOLD ELIGIBILITY. Is handoff v2's narrowing honest and
     complete — does any sentence still imply that the allowed paths implement
     §H3's runtime behaviour? Is the removal of the three v1 test paths correct,
     or does it remove something that WAS implementable? Is D-4's synthetic-tuple
     totality test over SC-7 a legitimate declarative check, or does it come too
     close to implementing the classifier? Is the §H11 later-stage authorization
     table complete, and is the two-way split between an inactive-scaffold
     authorization and a distinct runtime implementation authorization the right
     boundary?

Q9   IDENTITY AND ACCEPTANCE. Is the identity disposition preserved exactly — no
     identity observation code, not the XS-1 combined binding, the weakening
     unaccepted, the combined binding still blocked? Is recording Cell 1 as
     gate 0 of the BINDING ledger, rather than adding a paragraph to the
     composite, the correct scope boundary for X-3?

Q10  SCOPE DISCIPLINE. Did this round change anything outside R1..R6 and the
     accounting they force? In particular: did any author cell, authority,
     option, token, mechanism, treatment, scientific constant, member class or
     count outside the stated list move? If the answer is yes anywhere, name the
     locus.
```

---

## §11. Exact next boundary

```text
THE VERDICT AUTHORIZES: nothing to be built, written, installed, accepted or
activated. It licenses ONE thing — submitting the v2.11 generation to a FRESH
BOUNDED INDEPENDENT X-LINE AND Y-LINE ROUND on identical bytes, performed by
reviewers that did not author v2.3 through v2.11.

THE NEXT ACT IS A REVIEW ACT, NOT AN AUTHORING ACT AND NOT AN IMPLEMENTATION
ACT.

EXPLICITLY NOT AUTHORIZED BY THIS CLOSURE
  no acceptance of I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_
    AMENDMENT_V1_8, and the v1.7 token is retired and must not be signed
  no inactive-scaffold authorization; no code at any allowed path, including the
    oracle and the contract module
  no runtime implementation authorization
  no key, entropy, seed, Stage A or Stage B
  no OR-3, no OR-4, no OR-5..OR-11, no one-shot atomic-handoff authorization
  no identity-token acceptance and no bounded weakening under any name
  no T activation and no programme-claim movement
  no edit to any governing, historical, code, test, signature or runtime path

ONLY AFTER A PASSING INDEPENDENT ROUND may an author separately consider
amendment acceptance; and only after that, separately again, a narrowly scoped
inactive-scaffold authorization; and only after that, separately again, a runtime
implementation authorization; and only after that, separately again, the one-shot
atomic-handoff authorization. THE XS-1 COMBINED IDENTITY BINDING REMAINS BLOCKED
ON SEPARATELY REVIEWED AND ACCEPTED BOUNDED WEAKENING.

T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 IDENTITY-OBSERVATION IMPLEMENTATION SURFACE = OUT OF SCOPE, NO CODE
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
WATCHDOG AUTHORITY AMENDMENT V1.8 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

```text
READY_FOR_OFFICINA_P1_WB_V2_11_FINAL_XY_REVIEW
```

The exact selected token and the formal selection signature govern. This closure
and the five documents it reports on are untrusted self-assessments and drafts;
they are normative for nothing.
