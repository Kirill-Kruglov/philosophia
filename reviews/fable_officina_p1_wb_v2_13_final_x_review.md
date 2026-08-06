# Officina P1 W-B v2.13 — final independent X-line review

**Reviewer:** Claude Code Opus 5, **independent X-line reviewer only**. I did not
author v2.13 or any predecessor generation. Every claim of the author closure was
treated as untrusted testimony and reconstructed from the bytes; where a figure is
reported below it was recomputed here, not copied.

**Repository:** `/home/master/llm_projects/philosophia`. Read-only throughout.
Nothing was modified, staged or committed. Exactly one file was created — this
one. No resolved bytes were written to any repository path; all transform output
was held in memory in a session scratchpad and discarded.

---

## §1. Verdict

```text
OFFICINA_P1_WB_V2_13_X_CONFIRMED_FOR_ACCEPTANCE_REVIEW
```

**No executable Critical or Major defect was demonstrated.** The canonical parser,
the six-phase classifier, the `KG-2` population, the eleven-span `OR-4` transform,
the narrowed quarantine claim and the whole `71 / 85 / 79` accounting all
reproduce independently and exactly. Seven findings are logged below as
non-blocking; the first two are substantive and one of them, `L-X6`, is carried
forward as an **explicit precondition on the next boundary** rather than as a
closed item.

This confirmation authorizes only Kirill's later **consideration** of amendment
v1.10. It authorizes no acceptance, scaffold, code, key, `OR` step, install,
activation or identity weakening. `T` remains `NOT_ACTIVATED`; the programme
claim remains `OPEN`.

---

## §2. Path and digest of this review

```text
path    reviews/fable_officina_p1_wb_v2_13_final_x_review.md
sha256  computed by the operator on the committed bytes; this file cannot carry
        its own digest without breaking the acyclic custody rule of §P1-14.5,
        and it does not attempt to.
```

### §2.1 Pinned-input recomputation — all six MATCH

```text
d50f378ca419f891e79356315d59115b6ec06c38474e812fa01ccb847b15f200  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_13_CORRECTION.md          MATCH
2999e2129de19ff38dee12071453c7156a5432efaf299bc69e79dc7e7b04ac53  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_10_DRAFT.md   MATCH
15e11f0e4c10fe8b85607dc383520d5b009712603084e82a8756211615bd8fb3  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_13.md  MATCH
10207f833a00b0e7e5106ca8a781916f3414d995ab05161fb734078b5ffaef93  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V4_DRAFT.md                             MATCH
080000c478c933bedd91124983c4c9e44cc4b850e52eba17b7628304274cbef9  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V4_DRAFT.md                             MATCH
8245b0f960fa4a349667a0c75213cbe0e39cf83ab4a914be94146d56f93626fd  reviews/opus5_officina_p1_wb_v2_13_closure_repair.md                                    MATCH
```

**One disclosed deviation from the review instruction, which is not a `BLOCKED`
condition.** The instruction pins commit `23a7816`; repository `HEAD` is
`9ed98a7`. I verified that **all six pinned files are byte-identical at
`23a7816` and at `HEAD`** — the only delta between the two commits is the
addition of the two review-request prompts. The review was therefore performed
against exactly the pinned bytes. No mismatch exists and `BLOCKED` is not
returned.

---

## §3. `Q1` — is there exactly one `/proc/<pid>/stat` grammar, and is it exact?

**ANSWER: YES.** I implemented a reference `STAT_PARSE` from the `L0`..`L5`
normative prose of §P1-10.3 alone, without reading any author-supplied
implementation, then drove it with every published vector and with a large
independently constructed adversarial set.

```text
V0 RECONSTRUCTED FROM THE GOVERNING BYTES     144 bytes
   sha256 0ea1e5bcbf609b29f9c3ac91503538b10644e0167a0eb18bafbef1b1727c6c91  MATCH

PUBLISHED VECTOR CHECKS                        50 assertions,  0 mismatches
   V0..V4        PARSE_OK / PRESENT_VALID / PRESENT_VALID, lengths and SHA-256
                 all MATCH (144, 150, 150, 155, 143)
   V5            all NINE state bytes, nine digests, all MATCH
   V6..V10       the Y line's four shifted forms + the fifth: ALL PARSE_REFUSED
                 at L2, measured suffix field counts 51, 51, 49, 51, 49
   V11..V38      all PARSE_REFUSED, no field value returned
   V39           PARSE_OK / PRESENT_VALID / UNPARSABLE, 141 bytes,
                 905feda8…1031a  MATCH — the one consumer-dependent answer
```

```text
INDEPENDENT ADVERSARIAL CASES BEYOND THE PUBLISHED SET      0 failures
   inserted separator at EVERY suffix field boundary        all refuse
   removed separator at EVERY boundary (49 cases)           all refuse
   token shift — suffix rotated by 1..49                    all refuse
   truncation at EVERY byte offset (144 cases)              none PARSE_OK
   every one of the 256 single-byte state substitutions     exactly the nine
                                                            admitted bytes pass
   boundary integers 0, 1, MAX, MAX+1 for ppid/pgrp/sid     exact
   field counts 0..60                                       only 50 parses
   parenthesised/adversarial comm forms                     no field shift
   200,000 random 1-4 byte mutations of V0                  0 wrong-field values
   200,000 randomised consumer-agreement trials             0 disagreements
```

**Can any inserted separator, removed separator, shifted token, extra token or
missing token reach a returned value? NO.** Every such form changes either the
field count (refused at `L2`, an equality) or produces an empty field (refused at
`L1`), and neither survives to `L3`. Across 200,000 mutations no `PARSE_OK`
result ever carried a value taken from a field other than its pinned position.

**Does every refused vector return no field value? YES.** `L5` is honoured: my
reference returns a reason string and no tuple on every refusal, and I asserted
that property on every refusing case.

**Can `STAT_OBSERVE` and `PGRP_OBSERVE` disagree about whether a buffer PARSED?
NO — provably not, and not merely by measurement.** Both consumers call the same
`STAT_READ` and the same `STAT_PARSE`; `PGRP_OBSERVE` differs only by applying
`KG_GROUP_ADMISSIBLE` to an **already-parsed** field. The single divergence is
`pgrp == 0`, which is `PARSE_OK` at both and `PRESENT_VALID` / `UNPARSABLE` at
the two consumers respectively. 200,000 randomised trials found zero violations
of that invariant. The `M-1`/`M-2` repairs hold.

**One anomaly, logged at `X-L1` below:** `V18`'s named refusing rule is
unreachable. It is not an executable defect — the vector's stated *result* holds.

---

## §4. `Q2` — is the phase order total, and is the terminal single-valued?

**ANSWER: YES.** I modelled `SC-9` `P1`..`P6` and `SC-10` as a total function and
drove it adversarially.

```text
THE THREE PUBLISHED COUNTEREXAMPLES                       ALL PASS
  CE-1  recorded protected masked by an earlier skip      T3 / FREEZE_NOT_ATTEMPTED
                                                          0 signals; KV_FORBIDDEN_TARGET
                                                          on the CONTRADICTED entry
  CE-2  the KV-5 form (fresh pgrp = supervisor group)     T3 at PHASE 4, 0 signals,
                                                          a's KV_OK DISCARDED
        the KV-4 form (identity mismatching instead)      T3 at PHASE 4, 0 signals,
                                                          NO OWNERSHIP SET TO
                                                          CONTRADICTED — verified
  CE-3  (i)   malformed + recorded-protected              T1, NO SC-5 token
        (ii)  stale + malformed beside a valid candidate  T1, 0 signals
        (iii) structurally valid stale beside a valid one T2, KV_STALE_HANDLE,
                                                          0 signals
```

```text
SC-10 DOMINANCE TABLE — EVERY PAIR, EVERY ORDER
  6 pairs x 2 orderings                                   12/12 correct
  malformed+stale+recorded-protected, all 6 orderings     T1
  all four fault classes, all 24 orderings                T1
  fresh-protected + identity mismatch, same entry         T3, no CONTRADICTED
  fresh-protected + group mismatch, same entry            T3, KV-5 not evaluated
  fresh-protected on b + KV_OK on a                       T3, a DISCARDED
  identity + group mismatch, no protected group           KV_IDENTITY_CONTRADICTED,
                                                          a PHASE-5 skip
```

```text
EXHAUSTIVE CROSS-PRODUCT SEARCH
  role x state x ownership x pgid{NULL,own,PCS,SUP,WD} x obs{10 PRESENT_VALID
  forms + ABSENT, UNREADABLE, UNPARSABLE, ERROR, PRIMITIVE_FAULT} x generation
  x malformed
    single-entry tables                                   10,800
    two-entry tables, both orderings, against a fully
      valid signalable partner                            21,600
    TOTAL                                                 32,400 tables

  SIGNALS ISSUED TO A PROTECTED GROUP                     0
  SIGNALS ISSUED WHILE A RECORDED **OR** FRESHLY OBSERVED
    PROTECTED GROUP EXISTED ANYWHERE IN THE TABLE         0
  DIVERGENCE OF (terminal, qualifier, signal sequence)
    UNDER TABLE REORDERING                                0
```

**Is any `_killpg` reachable from a table containing a protected group in either
form? NO.** The `X-M1` repair is structural rather than asserted, and I confirmed
the mechanism rather than the claim: `KV-4` and `KV-5` are `PHASE-5` predicates
and `PHASE 5` cannot begin until `PHASE 4` has visited every prospective
candidate without a terminal, so no `PHASE-5` skip can consume an entry before
`KV-6(b)` has run against it. `SC-6` no longer carries a dominance rule; `SC-10`
is the only one.

**The `PHASE-6` recheck was attacked separately and holds.** A table whose
entries are clean at `PHASE 4` but whose `PHASE-6` re-observation reports
migration into a protected group terminates with `T3` and issues zero signals.

**`SC-7`'s partition recounted independently:** `24 + 32 + 4 + 6 + 6 = 72`,
exact, no tuple unclassified and none with two answers; the `PHASE-4`
prospective-candidate set is **12** tuples and the non-`NULL` `pgid_or_null` set
is **36**, both as published.

---

## §5. `Q3` — the four `PHASE-4` exclusions as authority boundaries

**ANSWER: the "no signal can follow" proof is correct for all four exclusions.
One of the two `REQUIRED` proofs rests on a premise the governing bytes
contradict.** Neither affects behaviour; both are logged.

```text
role WATCHDOG            NO SIGNAL CAN FOLLOW: CORRECT. KV-2 refuses role
                         WATCHDOG at every state and every ownership (24 of the
                         72 tuples), and §P1-10.6 is absolute on every path.
                         "REQUIRED RATHER THAN CONVENIENT": NOT ESTABLISHED —
                         see X-L2.
state REAPED /           NO SIGNAL CAN FOLLOW: CORRECT. KV-2 refuses both; the
  ownership REAPED        pid-reuse reasoning is sound and the direction is
                         conservative.
pgid_or_null NULL        NO SIGNAL CAN FOLLOW: CORRECT, AND THE LIMIT IS STATED
                         HONESTLY. SC-2 projects pgid_or_null; a NULL handle
                         contributes no member to the scope sequence, so it
                         grants no scope.
```

**Is the `NULL`-recorded-group limit stated honestly, and is any signal reachable
through it? The statement is honest, and no signal is reachable through it.** I
constructed the exact adverse case — a current-generation `CONTROLLER` /
`RUNNING` / `OWNED` handle with `pgid_or_null` `NULL` whose **live process sits
in the recorded supervisor group** — beside a valid unprotected candidate. The
classifier does not detect the `NULL` handle (as the bytes say it does not),
issues `KV_ROLE_OR_STATE_REFUSED` for it at `PHASE 5`, and signals only the
valid candidate's own unprotected group. The undetected handle contributes
nothing to any scope. The author's formulation — *safe because it grants no
scope, not because it was examined* — is exactly right, and it is the correct
way to state a limit of a classifier.

**Is the role-`WATCHDOG` exclusion genuinely required?** The claim is that
*"including watchdog entries here would terminate the classifier on EVERY
conforming table."* That is **not established by these bytes**, because its
premise — *"a conforming watchdog that is its own group leader"* — is contradicted
by §P1-4.1, which spawns the watchdog with `setsid = False`, and by §P1-9.2,
which states the watchdog "is not a session leader". A watchdog that is not its
own group leader never satisfies `KG-2` `P-2(iii)`, so by `P-4` its
`pgid_or_null` **stays `NULL` forever** — and it is therefore already excluded
from `PHASE 4` by the `NULL` exclusion, independently of its role. Logged at
`X-L2`. The exclusion is harmless and conservative; only its proof is wrong.

**A related consequence I checked and cleared.** Because `P3(b)` places both a
watchdog's pid and its recorded group in `G`, and because `PHASE 3` scans *every*
current-generation entry including watchdog rows, a watchdog carrying a non-`NULL`
`pgid_or_null` would terminate the classifier at `PHASE 3` on its own row. I
confirmed this cannot arise on a conforming table — `setsid = False` guarantees
the field stays `NULL` — and that where it does arise (a table no conforming
build can produce) the outcome is a zero-signal terminal, which is the safe
direction. **This is not a defect.**

---

## §6. `Q4` — is `KG-2`'s population total, and is the transition exact?

**ANSWER: YES on both counts.**

**Is the `P-2` decision instant real, single and well-defined?** Yes, and it is
anchored in a clause that already exists rather than invented. §P1-8.3's
`AWAIT_STOP` row has precondition *handle state `SPAWNED`* and response operands
`outcome`, `start_identity` and `pgid_is_leader` in `{0,1}` — so the PCS already
computes, at one instant per evaluation, exactly the predicate `P-2` requires.
§P1-8.4's *"the supervisor issues one outstanding request at a time"* removes all
interleaving, so the instants are totally ordered and the "single instant" is
single-valued. All three conjuncts are decidable there from **one** `KG-1`
observation: `(i)` `PRESENT_VALID`, `(ii)` start-identity equality, `(iii)`
`pgrp == h.pid`.

**Is any path missing from `P-8`..`P-11`? No.** I enumerated the closure:

```text
KG-1's OUTCOME SET IS SIX          ABSENT | PRESENT_VALID | UNREADABLE |
                                   UNPARSABLE | ERROR | PRIMITIVE_FAULT
P-9 COVERS ALL SIX, with PRESENT_VALID split into exactly three by
  (identity match) x (pgrp == pid)                        TOTAL
P-8  creation: 2 failure rows + 3 success rows by role    TOTAL over §P1-8.5's
                                                          three roles
P-10 EINTR retry; deadline expiry; AWAIT_STOP TIMEOUT
     reissue; reissue after a successful write; mid-
     attempt generation invalidation                      TOTAL
P-11 REAP_ROLE (freeze), RELEASE_HANDLE (leaves table,
     no id reuse)                                         TOTAL
```

**Does any route end outside the six named handle states? No.** Every row of
`P-8`..`P-11` names exactly one of `H-ABSENT`, `H-NULL-GROUP`,
`H-GROUP-RECORDED`, `H-CONTRADICTED`, `H-FAULTED`, `H-REAPED`.

**Does any route leave a handle with a group value of unknown provenance? No, and
the argument is closed rather than asserted.** `P-1` initialises `NULL` for every
role with no exception and no default or fallback anywhere; `P-2` is the only
site; `P-3` permits at most one write and makes a second write a `SC-8`
structural violation; `P-5` makes the field immutable; `P-11` freezes rather than
clears it. `GROUP-SIGNALABLE` is defined as exactly the four conjuncts `KV-2`
tests, so there is no intermediate state in which a group value exists but its
provenance is unknown. Retry exhaustion produces `H-NULL-GROUP`, never a default
or sentinel. `RELEASE_HANDLE` requires state `REAPED` (§P1-8.5), which closes the
one route by which a **live** watchdog's group could have left `G`.

I note one operational coupling that is correct but worth the author's awareness:
because `P-2` is the only population site and it sits inside `AWAIT_STOP`, a
handle for which `AWAIT_STOP` is never issued is never group-signalable. That is
stated by `P-12` and is the conservative direction.

---

## §7. `Q5` — does the complete `OR-4` output reproduce?

**ANSWER: YES, byte-exactly.** I implemented binding §2.2.5 independently — line
splitting, sentinel location under the cardinality rule, source verification,
ascending sort, non-overlap verification, single-pass splice, full-output
verification — and ran it against composite v1.13.

```text
SPAN  LINES        SRCLEN  SOURCE SHA-256   REPLEN  REPLACEMENT SHA-256
S1    55..95        2184   MATCH             2120   MATCH
S2    306..307       163   MATCH               61   MATCH
S3    1657..1664     598   MATCH              207   MATCH
S4    1667..1671     298   MATCH               22   MATCH
S5    2136..2139     299   MATCH               47   MATCH
S6    2161..2163     218   MATCH               61   MATCH
S7    3520           982   MATCH              727   MATCH  (see X-L3)
S8    3803..3820    1329   MATCH              440   MATCH
S9    7745           504   MATCH              271   MATCH
S10   7773          9868   MATCH             9778   MATCH
S11   7784           449   MATCH              315   MATCH

EVERY SENTINEL AND EVERY PREFIX MATCHED EXACTLY ONE LINE.
PAIRWISE NON-OVERLAPPING, e_i < b_{i+1} FOR ALL TEN ADJACENT PAIRS: VERIFIED.

FULL RESOLVED OUTPUT   586426 bytes                                    MATCH
                       3a88798f8f18a5e2f38108c9873e5b36045c7533126685034ad17a28998dc339  MATCH
BYTE ARITHMETIC        589269 − 16892 + 14049 = 586426, and the measured
                       span totals are exactly 16892 and 14049          MATCH

RESOLVED REGION DIGESTS
  H_BODY       f57002460cc94d5f1c220193459ec662f713e0f5e3a1564f76f1732d4e1830df  MATCH
  H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426  MATCH
               AND BYTE-UNCHANGED FROM THE PRE-SELECTION REGION: VERIFIED
  H_NORMATIVE  3bbd378dec0d189d1b4374970a01272b73634c539eb2182773e46ea4cec6811f  MATCH
SOURCE REGION DIGESTS H_BODY 1bb4c587…, H_GUARDDATA faf2d709…,
                      H_NORMATIVE d47076e8…                            ALL MATCH

THE TWO DELIMITED SHARED REGIONS
  canonical atomic-handoff preamble   4167 bytes  7c5cabe2…44a7          MATCH
  joint install and authorization   223866 bytes  7f58b11d…c8fa          MATCH
  extracted from composite v1.13 AND amendment v1.10 by their own two
    delimiter lines: BYTE-IDENTICAL                                      VERIFIED
  survive OR-4 BYTE-IDENTICALLY                                          VERIFIED
```

**`MP-1` reproduces behaviourally and fails `PO-0` as required.** Inserting the Y
line's marker-free paraphrase into the pinned resolved output yields exactly
`586621` bytes (`586426 + 195`, confirming the payload), **`0` `D1` matches, `0`
`D2` matches, `0` and `0` markers outside guarddata, `H_GUARDDATA` unchanged** —
so `PO-1`, `PO-2`, `PO-3` and `D3` all pass — **and `PO-0` fails closed.** The
narrowed claim of §2.6.0 is therefore proved by construction: *the detectors cover
what they list; `PO-0` covers everything else.*

**I could not reproduce `MP-1`'s pinned digest.** Logged at `X-L4`. The length is
exact and every behavioural claim holds; the digest is not reachable from the
published recipe by any line-boundary realisation I tested.

---

## §8. `Q6` — is the quarantine claim now no broader than its detector?

**ANSWER: YES.** I read binding §2.6.0 and searched every live v2.13 surface for
a surviving claim broader than the detector.

```text
NO SENTENCE OF binding v4, handoff v4, the packet OR the closure still claims
that D1 and D2 detect arbitrary semantic paraphrases, forbidden grants as a
class, or anything beyond exact listed literal coverage. §2.6.0 states the claim
as "EXACT LISTED LITERAL COVERAGE AND NOTHING MORE", names v3's "FALSE
NEGATIVES" heading as the withdrawn overclaim, carries the Y line's
counterexample verbatim, and concedes in terms: "THE Y LINE IS RIGHT AND THE
DETECTOR IS SILENT ON IT."

§2.5 additionally states the boundary the other way — that the W-A option token
and its paired amendment token are NOT in class F and that no rule requires them
to occur zero times — which is the correction that keeps TS-1, IR-13 row 47 and
the CK-14 fixture consistent.
```

```text
MEASURED INDEPENDENTLY ON THE PINNED RESOLVED OUTPUT
  D1 matches in PN(resolved minus GUARDDATA)          0 of 11    required 0
  D2 matches in PN(resolved minus GUARDDATA)          0 of 13    required 0
  D1 coverage in PN(pre-resolution Cell-2 span)      11 of 11    claimed 11
  D2 coverage in PN(composite v1.13)                 13 of 13    claimed 13
  D1 CANON   926 bytes  d5b375c5…6c1e                            MATCH
  D2 CANON  1044 bytes  4e212085…a15c                            MATCH
  "[W-A]" / "[W-B]" outside GUARDDATA                 0 and 0    required 0
  "[W-A]" / "[W-B]" inside  GUARDDATA                 1 and 1    required 1
  markers in REGION(BODY)                             0 and 0    required 0
  t-wd-freeze.v1                          pre 9  ->  post 0      MATCH
```

**Is the §2.5 W-A option-token count of 3 correct against the pinned output? YES.**
`I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES` occurs **3** times
pre-resolution and **3** times post-resolution — the `TS-1` grammar, the `CK-14`
fixture and one historical mention inside the `S1` replacement. The author's
self-reported correction of v3's false "2" is itself correct. The three companion
counts also verify: the paired amendment token `1 -> 2`, the W-B option token `3`,
and `P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1` `2`.

---

## §9. `Q7` — do `71 / 85 / 79` recount, and are the live identities right?

**ANSWER: YES to both, with no stale figure surviving anywhere.** Recounted from
the bytes without reading any table's own total.

```text
MS-2 literal rows                71   COUNTED 71; 71 distinct paths; 71 distinct
                                      digests
MS-3 literal rows                 7   COUNTED  7; 7 distinct paths
MS-2 ∩ MS-3                       ∅   EMPTY — no class overlap
MS-8 / TS-3 member_count         85   2 + 71 + 7 + 1 + 1 + 2 + 1 = 85, recomputed
composite provenance rows        79   COUNTED 79; 79 distinct paths; = 71 + 7 + 1
recorded M2+M3 digests           78   71 + 7

THE FOUR NEW M2 ROWS — DIGESTS VERIFIED AGAINST THE FILES ON DISK, NOT MERELY
AGAINST THE TABLE:
  a7ec78cc…  …_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9_DRAFT.md      VERIFIED
  e796d9e8…  …_P1_OPERATIVE_COMPOSITE_V1_12.md                        VERIFIED
  ca02d485…  reviews/fable_officina_p1_wb_v2_12_final_x_review.md     VERIFIED
  92a394a3…  reviews/sol_officina_p1_wb_v2_12_final_y_review.md       VERIFIED
```

**`X-M2` is repaired in the bytes.** Composite row 108 now reads *"a members array
of any length other than **85** is a STRUCTURAL failure"*, its setup reads **86**
entries against **85** enumerated from the constants, and its provenance-overlap
figures read **78** and **71**. The v2.12 closure's claim that the literal had
moved was false; this generation moved it and states the recount.

**Is any stale figure left anywhere? NO.** I swept the composite for every retired
cardinality (`57`, `67`, `74`, `75`, `77`, `81`). Every surviving occurrence is a
legitimate `MS-11` module-closure row index, a test-matrix row number, or the
**non-normative** `PROVENANCE` region's own historical narrative recording the
move ("the region moves from 75 rows to 79 and `MS-2` from 67 to 71"), which is
correct in that position. Row 103 reads 78; rows 104/107 read 85 and 85→84; row
106 declares exactly ten groups `(a)`..`(j)`; `G-11`'s input-set sentence now
reads **"eighty-five literal repository paths in seven pairwise-disjoint
classes"**, repairing the author-found `fifty-seven`.

**Does any live authority surface still identify itself as a predecessor? NO.**

```text
amendment title            "version 1.10 (draft)"                        OK
amendment opening          "WHOLLY REPLACES version 1.9 (a7ec78cc…)"     OK
amendment predecessors     ten, listed 1, 1.1 … 1.9 and counted exactly  OK
composite title            "version 1.13"                                OK
composite opening          "a full replacement for version 1.12"         OK
DA-1 historical lists      composites 1..1.12; amendments 1..1.9         OK
DA-4 live surfaces         amendment v1.10 / composite v1.13, exactly two OK
row 114                    refuses v1.9+v1.13 and v1.10+v1.12            OK
```

**The §A0.4 anchor.** Exactly **one** line of the amendment matches `A16(d)`'s
grammar, and its value equals composite v1.13's `H_FILE` — verified by
recomputing the composite's digest and comparing. The complete token occurs
**7** times in the amendment and **1** time in the composite, as documented.
Retired generation segments `8`, `9`, `10`, `11` and `12` occur **0** times in
either file, so the author-found `§A0.4` defect (`A-1`) is genuinely repaired.

**Do the two delimited regions extract byte-identically from both files? YES** —
see §7; both regions were extracted from composite v1.13 and amendment v1.10 by
their own two delimiter lines and compared with zero difference, at the pinned
lengths 4167 and 223866 and the pinned digests.

---

## §10. `Q8` — the known unresolved `L-X6`

### §10.1 What the bytes actually say

```text
§P1-3.4 BINDS, from os:
  _fork _waitpid _kill _killpg _getpid _getppid _open _read _write _close
  _fstat _stat _listdir _unlink _fsync _rename _pipe2 _dup2 _dup _execve
  _setsid _exit_ _uname _chdir _get_inheritable _posix_spawn
  -> NO _getpgid.  AND NO _getsid.

§P1-7.5 REQUIRES:
  c10  "getsid and getpgid of that pid both equal middle_child_pid"
  c14  "getpgid of it equals process_group_id"
  m3   "verify getsid(0) == getpgid(0) == getpid()"

§P1-10.3 STAT_PARSE RETURNS (STAT_LAYOUT_ID, state, ppid, pgrp, start_identity)
  and states "NO OTHER SUFFIX FIELD IS PARSED, READ, INTERPRETED OR CONSTRAINED"
  -> pgrp IS obtainable from the canonical parser.
  -> THE SESSION ID IS NOT OBTAINABLE BY ANY BOUND ROUTE AT ALL.
```

**The author's record of `L-X6` understates it in three respects,** and I record
that as part of the finding rather than as a separate item: it names only `c10`
(not `c14`, not `m3`), only `getpgid` (not `getsid`), and does not observe that
the `getpgid` half has a substitute route through `STAT_PARSE`'s `pgrp` field
while the `getsid` half has none.

### §10.2 The decision

**`L-X6` is outside the authority accepted by amendment v1.10 and may remain a
separately blocked later surface. It is NOT a current Critical/Major defect, and
I did not reach that conclusion because it was previously logged.** The reasons
are reachability and the gate, and I set them out so they can be checked:

**1. Nothing that confirmation or acceptance authorizes consumes `c10`.** The
amendment's own status clause is explicit: *"EVEN A FUTURE SIGNATURE OF THAT
TOKEN AUTHORIZES NO CODE EDIT, NO `OR-3`, NO KEY OR ENTROPY, NO `OR-4`, NO
INSTALL AND NO `T` ACTIVATION. Acceptance of this indivisible pair and
authorization to construct anything are separate acts, and the second one does
not follow from the first."* §P1-10.7 closes with *"no code may be written at any
production root under this pair, and `OR-5` remains the step at which the
verifier and the test bundle are installed."*

**2. The W-B mechanism this generation exists to fix does not depend on it.** I
verified the whole reachability chain. The §P1-10.7 classifier never calls
`getpgid`: `SC-9` `P3(a)` obtains the PCS's own group by *"exactly one `KG-1`
`PGRP_OBSERVE(_getpid())`"* — using the **bound** `_getpid` and the canonical
`STAT_PARSE` over `_open`/`_read`/`_close`, all bound — and `P3(c)` **reads**
`process_group_id` from the `SPAWNING_GROUP.json` record rather than recomputing
it. `KV-5` and `P3(c)` *cite* `c10` as the provenance of that recorded value, but
they consume the record, not the syscall. **The classifier, the parser and
`KG-2` are implementable in full under the existing bound primitive set.**

**3. The failure direction is closed, not open.** `P3(c)` states that if the
record *"IS ABSENT OR UNREADABLE, OR ITS `process_group_id` IS NOT A CONFORMING
INTEGER, PHASE 3 FAILS CLOSED and the classifier terminates; THE SUPERVISOR
GROUP IS NEVER TREATED AS UNKNOWN-AND-PROCEED."* No route exists on which a
weakened `c10` yields a permissive classifier answer.

### §10.3 The mechanical gate, named exactly

Implementation cannot consume `c10` before a separately reviewed binding exists.
**Four independent static rules of §P1-14.6 `CHANGE 3` refuse it, and they refuse
it at the verifier rather than at review time:**

```text
S-3   "the binding block is exactly the list of §P1-3.4, IN THAT ORDER, at
      module scope, each target a plain Name and each value an Attribute of one
      of the permitted modules"
      -> adding _getpgid = os.getpgid (or _getsid) to the binding block is a
         STATIC VIOLATION. The list is an equality, not a minimum.

S-5   "the six module names appear as an Attribute value ONLY INSIDE the
      binding block"
      -> calling os.getpgid(pid) at c10, c14 or m3 is a STATIC VIOLATION.

S-6   "every Call func is a plain Name, a bound name, or a builtin from the
      closed set"
      -> an Attribute call such as os.getpgid(...) is refused outright.

S-7   forbids getattr, setattr, vars, globals, locals, eval, exec, compile,
      __import__ and importlib anywhere in the PCS and role roots
      -> every indirection route to an unbound primitive is closed.

REINFORCED BY, AND NOT DEPENDENT ON, THESE FOUR:
  §P1-3.6's no-rebinding / no-indirection rule;
  §P1-14.6 CHANGE 2, which pins the allowlists with the scoped map exact and
    never a union with the default;
  MS-11's eighty-nine-row reachable_closure, canonical length 20534, digest
    aa974e0c…c20ee, unchanged by this round;
  MS-13, unchanged;
  and, above all, the authorization state itself: INACTIVE-SCAFFOLD
    AUTHORIZATION = NOT GRANTED and RUNTIME IMPLEMENTATION AUTHORIZATION =
    NOT GRANTED. There is no authorized artifact in which c10 could be written.
```

**Consequence, stated as a binding precondition rather than as a closed item.**
Any build that attempts `c10`, `c14` or `m3` as written **fails the verifier
statically and produces no certified artifact** — the direction is fail-closed.
But the defect is real and it is now the *only* known clause of the live pair
that cannot be implemented to conformance. **It must be repaired before any
scaffold or runtime implementation authorization is granted**, and it cannot be
carried silently into an `OR-5` bundle. The smallest bounded repair boundary is
recorded in §12.

---

## §11. Findings, ordered by severity

**No Critical. No Major.** Seven non-blocking items follow, most substantive
first.

```text
X-L1  §P1-10.3 L1's REFUSAL OF 0x29 IN THE SUFFIX IS UNREACHABLE, AND V18's
      NAMED RULE IS THEREFORE WRONG.
      L0 defines S := B[j+2 .. end] where j is the index of the LAST 0x29, so S
      can never contain 0x29 by construction. L1's "S contains 0x29 => REFUSE"
      disjunct is dead. V18 is published as refusing at L1; every concrete
      realisation I could build refuses at L2 or L0 instead.
      The L0 justification is additionally circular: it says the last-")" rule
      "is safe because NOTHING AFTER THE COMM MAY CONTAIN 0x29 — L1 refuses a
      suffix containing one", but L1 cannot refuse what L0 already excludes.
      NOT EXECUTABLE. The safety property is TRUE — it comes from L0's
      last-0x29 framing, which 200,000 mutation trials confirmed never yields a
      wrong-field value — and V18's published RESULT (PARSE_REFUSED /
      UNPARSABLE) holds, so no build fails row 89 on it. The 0x28 half of the
      same L1 rule IS live and is correctly placed.
      SUGGESTED: state the guarantee against L0 where it actually lives, and
      re-attribute V18 to the rule that refuses it.

X-L2  THE role-WATCHDOG EXCLUSION'S "REQUIRED RATHER THAN CONVENIENT" PROOF
      RESTS ON A PREMISE THE PAIR CONTRADICTS.
      SC-9 P4 argues that "a conforming watchdog THAT IS ITS OWN GROUP LEADER
      therefore has a freshly observed pgrp IN G by construction, so including
      watchdog entries here would terminate the classifier on EVERY conforming
      table". But §P1-4.1 spawns the watchdog with setsid = False and §P1-9.2
      says it "is not a session leader", so a conforming watchdog is NEVER its
      own group leader; by KG-2 P-4 its pgid_or_null stays NULL forever, and it
      is already excluded by the NULL exclusion regardless of its role.
      KG-2 P-4's companion claim is affected in the same way: "a recorded value
      is what makes the group form of that exclusion decidable" is vacuous on
      every conforming build, and KV-6's "every watchdog leader group" is an
      always-empty contribution to G.
      NOT EXECUTABLE. The exclusion is harmless, conservative and redundant
      rather than wrong, and the "NO SIGNAL CAN FOLLOW" half of the proof —
      which is the load-bearing half — is correct.

X-L3  BINDING §2.2.4's TRANSCRIPTION OF THE S7 DELETE LITERAL IS WRONG BY ONE
      BACKTICK.
      The transcription reads "` [W-A]` It additionally holds …" — delimiter
      backtick, SPACE, then [W-A] with only a CLOSING backtick. The actual
      bytes are " `[W-A]` It additionally holds …". Applying the binding's own
      stated rule ("Each literal is delimited by one leading and one trailing
      backtick") to the transcribed line yields a 276-byte string that occurs
      nowhere in the source line and matches no pinned digest.
      NOT EXECUTABLE, AND FAIL-CLOSED. The binding anticipates exactly this:
      "The authoritative check is not the transcription: it is the source
      SHA-256 of the containing line, the replacement SHA-256 of the containing
      line, and the full-output SHA-256 of §2.2.6." I recovered the true
      277-byte literal from the source line by its pinned length and digest,
      found it UNIQUE (exactly one occurrence), and the span's replacement
      digest and the full-output digest then both reproduced. An implementer who
      transcribed literally would fail §2.2.5 step 6 and stop — the safe
      direction. Every other span, including S9, S10 and S11, transcribes
      correctly and was recovered from the binding bytes directly.

X-L4  MP-1's PINNED FULL-OUTPUT DIGEST DOES NOT REPRODUCE FROM THE PUBLISHED
      RECIPE.
      §2.6.5 pins 586621 bytes and afbdb075…5ccf. The LENGTH reproduces exactly
      (586426 + 195, which confirms the 3-line payload and the one blank line),
      and every behavioural claim reproduces — D1 0, D2 0, markers 0 and 0,
      H_GUARDDATA unchanged, PO-0 FAILS CLOSED. The DIGEST does not. I searched
      ALL 8,067 line boundaries of the pinned resolved output under both
      orderings of the payload (paragraph-then-blank and blank-then-paragraph);
      NONE reproduces afbdb075…5ccf. The recipe — "insert, immediately before
      the sentence … the paraphrase followed by one blank line" — does not fix
      the insertion point byte-exactly.
      GRADED NON-BLOCKING, AND I CONSIDERED AND REJECTED GRADING IT MAJOR. The
      fixture's REQUIRED behaviour is "passes every detector and still fails
      PO-0", and that reproduces independently; handoff T-10's pass criterion is
      that a build must not report MP-1 as conforming, which is satisfied. No
      rule of the binding, the handoff or the governing pair CONSUMES the
      digest as a gate. The quarantine boundary MP-1 exists to prove is
      established independently by §7 above: any inserted byte changes the
      full-output hash and PO-0 fails closed. It is a disclosure figure of the
      same class as the W-A option-token count the author themself corrected.
      SUGGESTED: either make §2.6.5's insertion point byte-exact and republish
      the measured digest, or state the digest as informative.

X-L5  L-X6 IS RECORDED MORE NARROWLY THAN THE BYTES SUPPORT.
      The amendment §A0.3 R4 and the closure both record only "§P1-7.5 c10
      requires a getpgid answer while §P1-3.4 binds no _getpgid". The pair also
      requires getpgid at c14 and at m3, and requires GETSID at c10 and m3.
      getsid is the harder half: STAT_PARSE returns no session id and states
      that no other suffix field is parsed, so there is no substitute route for
      it, whereas pgrp IS available from the canonical parser.
      NOT EXECUTABLE for the reasons of §10. Recorded so the later bounded
      repair is scoped to the actual surface rather than to one clause.

X-L6  THE "FOUR EXCLUSIONS" OF SC-9 P4 ARE PRESENTED IN THREE ROWS.
      The prospective-candidate set carries four conditions and the prose says
      "THE FOUR EXCLUSIONS", but the table lists three rows, the second of which
      ("state REAPED, ownership REAPED") carries two. The count is defensible;
      the presentation invites a miscount. Presentational only.

X-L7  ONE DEPENDENT-LITERAL LIST DISAGREES WITH THE OTHER TWO.
      Amendment §A0.3 R4 lists "composite test rows 103, 104, 105, 106, 107,
      108 and 115" among the literals that MOVED; the packet §5.3 and the
      closure §5.4 both list 103, 104, 105, 107, 108 and 115 without 106. Row
      106 did NOT move — it continues to declare exactly ten groups (a)..(j),
      which I verified, and the amendment says so itself a few lines later.
      Bookkeeping only; the bytes are right and only one narrative sentence is
      loose.
```

### §11.1 Author claims I checked and found TRUE

Recorded because the discipline of this line is to verify testimony rather than
to report only its failures:

```text
X-M1 repaired, and STRUCTURALLY rather than by assertion   VERIFIED (§4)
X-M2 row 108's stale 77 -> 85, with 86 / 78 / 71           VERIFIED (§9)
M-1  shifted-field acceptance closed by exact framing      VERIFIED (§3)
M-2  one line, one result; G0..G5 withdrawn                VERIFIED (§3)
M-3  one total precedence, closed terminal set of three    VERIFIED (§4)
M-4  eleven spans pinned; full output byte-pinned          VERIFIED (§7)
M-5  no live surface identifies itself as a predecessor    VERIFIED (§9)
L-X1 U+2014 twice AND U+00A7 five times                    VERIFIED
L-X5 KV-3's one carriage rule                              VERIFIED (§4, §6)
L-X7 four named exclusions, honest NULL limit              VERIFIED (§5)
A-1  §A0.4 segment 13; retired segments 8..12 occur 0      VERIFIED (§9)
A-2  G-11's input set 57 -> eighty-five                    VERIFIED (§9)
A-3  the W-A option token occurs 3 times, not 2            VERIFIED (§8)
SC-5 remains exactly seven tokens, none added or renamed   VERIFIED
row 89 clause (2A), both the group and the identity form   VERIFIED
the negative boundaries of closure §6 (scaffold absent,
  identity unmoved, acceptance token unsigned)             VERIFIED on disk
```

---

## §12. The exact next boundary

```text
THIS REVIEW AUTHORIZES: the X-line half of a bounded acceptance-review record on
the six v2.13 deliverables, for KIRILL'S LATER CONSIDERATION of amendment v1.10.
NOTHING ELSE. An X-line confirmation does not neutralize a Y-line counterexample
against the same bytes; the Y line's verdict is independent and is not predicted
here.

BEFORE ANY SCAFFOLD OR RUNTIME IMPLEMENTATION AUTHORIZATION IS CONSIDERED, ONE
BOUNDED REPAIR IS REQUIRED — AND IT IS REQUIRED THEN, NOT NOW:
  SCOPE: §P1-7.5 c10, c14 and m3, and §P1-3.4's binding list, and nothing else.
  Either (a) restate c10/c14/m3 against values the bound primitive set can
  actually produce — pgrp via §P1-10.3's STAT_PARSE, and a session-id route that
  does not exist today — or (b) open a SEPARATELY REVIEWED import-surface
  binding that adds _getpgid and _getsid, with MS-11's closure, MS-13, S-3, S-5,
  S-6, S-7 and the manifest digests all recomputed in the same round.
  THAT REPAIR IS AN IMPORT-SURFACE OR BOOTSTRAP CHANGE. IT IS OUTSIDE THIS
  GENERATION'S LICENCE, AND ATTEMPTING IT HERE WOULD HAVE BEEN THE UNAUTHORIZED
  EXPANSION THE ROUND CORRECTLY DISCLAIMED.

EXPLICITLY NOT AUTHORIZED BY THIS REVIEW
  no acceptance of I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_
    AMENDMENT_V1_10; the V1_9, V1_8 and V1_7 tokens are retired and must not be
    signed
  no inactive-scaffold authorization; no code at any allowed path
  no runtime implementation; no classifier, no parser, no /proc read, no process
    operation
  no key, entropy, seed, Stage A or Stage B
  no OR-3, no OR-4, no OR-5..OR-11, no one-shot atomic-handoff authorization
  no identity-token acceptance and no bounded weakening under any name
  no T activation and no programme-claim movement
  no edit to any governing, historical, code, test, signature or runtime path

T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
WATCHDOG AUTHORITY AMENDMENT V1.10 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
XS-1 COMBINED IDENTITY BINDING = BLOCKED ON SEPARATELY REVIEWED AND ACCEPTED
  BOUNDED WEAKENING
```

```text
OFFICINA_P1_WB_V2_13_X_CONFIRMED_FOR_ACCEPTANCE_REVIEW
```

The exact selected token and the formal selection signature govern. This review
is an independent X-line verdict only. It confirms no acceptance and authorizes
no scaffold, code, key, `OR` step, install or activation.
