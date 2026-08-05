# Officina P1 W-B v2.11 — final independent X-line review

**Reviewer:** Claude Code Fable 5, acting solely as the independent X line for
this bounded final round. I did not author v2.3 through v2.11, and I authored
none of the six documents under review.

**Base commit reviewed:** `d273765` (`Repair W-B governing pair in v2.11`).

**Mode:** read-only. No governing, historical, code, test, signature or runtime
path was edited. Nothing was committed. Exactly one file was created — this one.

**Standing of the author closure:** treated as untrusted throughout. Every
figure below was recomputed from the bytes on disk. Where my recomputation and
the closure disagree, the recomputation is reported and the closure's claim is
named as the defect.

`T = NOT_ACTIVATED`. Programme claim `OPEN`. W-B is signed and was not reopened
by this review.

---

## §1. Verdict

```text
OFFICINA_P1_WB_V2_11_X_CONFIRMED_FOR_ACCEPTANCE_REVIEW
```

**Why not a revision demand.** The bar this round set is explicit: only a
concrete executable Critical or Major defect may force another governing
generation. I searched for one and did not find one. `R1`..`R6` all land, and
each landed claim was verified mechanically rather than accepted. The seven
findings in §4 are real and three of them sit in governing bytes, but for each I
attempted a minimal executable divergence and each attempt failed against an
explicit, redundant operative rule — in two cases against an *attested*
conformance row that fails any build taking the defective reading.

**Why not blocked.** Nothing in the round required an authorization that does
not exist. The round produced no code, no key, no `OR` step and no artifact, and
I verified that on disk rather than taking the closure's word for it.

**What this token authorizes.** The paired Y review on identical bytes, and
after a passing Y line, an author's separate consideration of amendment v1.8
acceptance. It authorizes no code, no test, no key, no `OR` step, no install and
no activation. §6 states the boundary exactly.

---

## §2. Input integrity

All six task-named inputs recomputed from disk and **matched**:

```text
efe0f908a104060ed01a640fd5c58f5bf9731261dbf07bdc77bf91bc7a9ffdfb  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_11_CORRECTION.md
71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md
d7ccf170b759f89519f24b26bd817d273197dddd0b5208e0d95eecebf59ec91d  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V2_DRAFT.md
a70f6a7774386d7b36084b0e19c5f1e78b11a5e04f2d992d95d93148878c5c6b  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V2_DRAFT.md
e6ef3a8f95b0c9591248db5c9ad996829872a45e5a884754d3e1f56e926e9677  reviews/opus5_officina_p1_wb_v2_11_governing_repair_closure.md
```

Commit `d273765` adds **7 files, 15018 insertions, 0 deletions**. Every path is
new. No governing, historical, code, test, signature or runtime file was
modified, and no unrelated dirty or untracked working-tree file moved. The
closure's §9.4 negative confirmation is accurate.

Composite region digests, recomputed by the `§P1-14.0` extraction algorithm
(sentinel cardinality verified as exactly one line per region per edge):

```text
H_BODY       ce728942d3d1a746960a9fbf0feb4a969b79b9793d2b89f67a5d73c9b31b51cf   MATCH
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426   MATCH
H_NORMATIVE  01ea73918211509a19126e5847234a4b64d6ffbabf8a064d7051b460949743b8   MATCH
H_FILE       c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6   MATCH
```

I extracted `REGION(GUARDDATA)` from composite v1.10 independently and confirmed
`H_GUARDDATA` is **byte-identical across v1.10 and v1.11**. The guard-pattern
region was not touched, so `G-10`'s pattern source and the `VARIANT_MARKER`
class are exactly what the previous generation carried.

---

## §3. Answers to closure §10, `Q1`..`Q10`

### Q1 — `R1`, the canonical block. **YES, with one descriptive defect (L-X3).**

I located the delimiter lines by whole-line equality, extracted the lines
strictly between them each including its `0x0A`, and hashed:

```text
REGION                              AMENDMENT v1.8     COMPOSITE v1.11
canonical atomic-handoff preamble   lines 1210..1270   lines 6615..6675
  SHA-256   ca2ff30b93818f7945b442de68438ddaa8f71879443595903fddfa950cf4a785   MATCH
  cross-file byte equality                                                     TRUE

joint install and authorization     lines 1325..4441   lines 3274..6390
  SHA-256   9bf4a831b138889b4ae71d2985820793f10a649311199ec3136d75a6514babe5   MATCH
  cross-file byte equality                                                     TRUE
```

`H_HANDOFF` equals `ca2ff30b…a785`. **Delimiter cardinality is exactly one per
line per file** — all four delimiter strings matched exactly once each under
whole-line equality, in each file. The quoted copies inside the extraction prose
(amendment 1143/1145, composite 6592/…) are indented and therefore fail
whole-line equality exactly as the rule requires.

**The narrowing is complete.** I swept every `byte-identical` / `identically` /
`stated in full` sentence in both files. Every surviving identity claim is
scoped to one of the two delimited regions, or has a different subject
(`MS-11.1` member `kind`s; `CANON` byte-equality of parsed values). `DA-5`,
`§A0.2`, composite `§P1-14.8` and both composite preamble loci (85–87, 147–149)
state the narrowing and add the explicit negative — prose outside the two
regions is not claimed identical. **No sentence in either file still asserts a
broader identity than the bytes support.**

**Defect L-X3.** The two regions' lengths are reported as `4052` and `222364`
"content bytes". Those are UTF-8 **character** counts. The true byte lengths are
**4061** and **222736** (the regions carry 7 and 223 non-ASCII characters
respectively). The mislabel appears in packet v2.11 §1.2 lines 126/129, binding
v2 lines 64–65 and closure §4.1. Non-executable: byte-identity is established by
SHA-256, and no operative clause anywhere in the pair consumes a region length —
I grepped both governing files for both literals and found zero occurrences.

### Q2 — `R1`, the range and the fixture. **YES on all four parts.**

**Every operative pre-production range is `CK-1`..`CK-15`.** I enumerated every
`CK-n`..`CK-m` construct in both files. All sub-ranges (`CK-2`..`CK-15` at
`IR-9`, `CK-4`..`CK-13`, `CK-11`..`CK-13`) are ordering or prerequisite claims,
not success ranges, and every one lies inside the joint block at the identical
offset in both files (constant offset 1949), so they cannot diverge.

**The twelve-check mentions.** Here I correct the closure. `CK-1`..`CK-12`
occurs **three** times in the composite (6577, 6647, 6653) but **five** times in
the amendment (135, 149, 1130, 1242, 1248) — the amendment carries two extra in
`§A0.3`, a section the composite does not have. The closure's "three times in
each file" is wrong for the amendment (finding L-X5). **The substantive claim
survives intact:** I read all eight in context and every one is a negation ("NO
CK-1..CK-12 SUCCESS RANGE EXISTS IN EITHER FILE"; "THERE IS NO `CK-1`..`CK-12`
SUCCESS RANGE") or a description of the removed defect. **No operative clause in
either file states a twelve-check range.**

**The `CK-14` fixture traces exactly as stated.** I executed it independently
against `TS-5` `B1`..`B18` rather than reading the trace:

```text
B1  .json and .sig both exist at TS-3's literal paths            PASS
B2  parses as JSON, byte-identical to CANON                      PASS
B3  key set is exactly TS-3's thirteen keys                      PASS  (key SET only)
B4  schema literal                                               PASS
B5  version integer 1                                            PASS
B6  created_utc grammar + MS-10 semantics                        PASS
B7  member_count integer 77                                      PASS
B8  five 64-lowercase-hex strings                                PASS
B9  install_record_path concatenation                            PASS
B10 signature_algorithm "Ed25519"                                PASS
B11 .sig exactly 128 hex characters                              PASS
B12 Ed25519 verify over exact .json bytes under Stage A's key     PASS  (validly signed)
B13 stage_a_path, stage_a_sha256, key_id                         PASS  (Stage A genuine)
B14 selected_option_token equals Stage A's        --> REFUSE  STAGE_B_OPTION_MISMATCH
```

I verified the load-bearing claim by inspection rather than assertion: **none of
`B1`..`B13` reads the *value* of `selected_option_token`.** `B3` is the only
clause that touches the field at all, and it tests the key *set*, not the value.
`B14` is therefore the first and only refusal, and a success range stopping at
`CK-12` admits the state. The fixture is executable and the fail-open it
documents was real.

**Placement in the joint block is correct.** Stating the fixture at `CK-14`
inside the joint block puts it in bytes both files carry identically, with no
closure as its source. Adding a test-matrix row instead would have perturbed
`MS-6`'s membership rule and `MS-7`'s `rows_attested`. I confirmed the
alternative was avoided: **the test matrix has 123 rows with maximum row 115 in
both v1.10 and v1.11**, and `rows_attested` remains the 24 integers 92..115 with
`row_count` 24 and `all_rows_passed` true. Nothing moved.

### Q3 — `R2`, `KV`/`SC` totality and fail-closed. **YES. Source trace honest.**

I brute-forced `SC-7`'s partition over the full signed value space rather than
checking the arithmetic:

```text
value space  role(3) x state(4) x ownership(3) x pgid_or_null(2) = 72
ordered rules, first match wins:
  role WATCHDOG                      24   claimed 24   OK
  ownership CONTRADICTED or REAPED   32   claimed 32   OK
  state REAPED                        4   claimed  4   OK
  pgid_or_null NULL                   6   claimed  6   OK
  remainder -> KV-3                   6   claimed  6   OK
                                     --                 
                                     72 = 72, every tuple classified exactly once
```

**Total, no residue, no double answer.** The ordering makes first-match
single-valued, and I confirmed independently that the 6-tuple remainder is
*exactly* the set satisfying `KV-2`'s four conjuncts — the first four rules are
precisely the negations of those conjuncts, so `SC-7` and `KV-2` cannot
disagree.

**`SC-8` leaves no default-allow path.** Every out-of-signed-set value, the
`type(x) is int` bool rejection, a non-mapping handle table, a malformed `KG-1`
return and any `BaseException` all route to `§P1-10.2`'s single
`STRUCTURAL_VIOLATION` continuation and terminate the classifier as `SC-6` does.
The section states in terms that no predicate has an "UNKNOWN, PROCEED" branch,
and I found no path that contradicts it.

**`KV-6`'s dominance is sound, and I verified the one case that could have
broken it.** `KV_FORBIDDEN_TARGET` terminates rather than skips, silences every
later signal of the generation, and is pinned by test row 89, which requires
each of the three forbidden classes to *terminate the whole classifier rather
than skip one group*. I then checked the masking case the dominance claim
depends on: a handle carrying a forbidden `pgid_or_null` that fails an *earlier*
predicate yields a skip, not a termination. That is safe, and provably so —
`SC-2` builds the scope sequence only from `KV-1`/`KV-2` survivors, so such a
handle contributes no group and no signal can reach the forbidden target; and if
any handle that *does* survive carries that same pgid, `KV-6` fires on it and
terminates. `KV-6(b)` separately scans **all** watchdog handles regardless of
`KV-1`/`KV-2`, closing the one case where the pgid would not otherwise recur.
The dominance holds over every outcome that could produce a signal, which is the
property that matters. (Observation L-X7: this argument is not written down; one
sentence would save an implementer the derivation.)

**The source trace is honest.** I checked each cited clause against the current
bytes. `pgid_or_null` is not invented — it pre-exists in `§P1-8.5`'s handle
schema at composite line 1445. `§P1-10.3`'s "20th token after the final `)`"
rule, `§P1-3.4`'s bound primitives, `§P1-7.5` `c10`/`c11`, `§P1-8.6` `J2`,
`§P1-10.1`'s CONTRADICTED triggers, `§P1-10.2`, `§P1-10.5`, `§P1-10.6`,
`§P1-4.6` and `§P1-5.1` all say what the table claims. Nothing is imported from
a superseded document.

`SC-5`'s seven tokens are closed and are excluded from `FC-1`'s 25-code set;
row 101 now pins the seven and forbids an eighth.

### Q4 — `R2`, the supporting rule. **YES, `KG-1` is the smallest.**

**It adds no import.** `KG-1` reads `/proc/<pid>/stat` once, in full, through
`_open`, `_read`, `_close` — all three already bound at `§P1-3.4` — and takes
the 3rd whitespace-separated token after the final `)` from **the same buffer**
`§P1-10.3` already parses for the 20th token. `KV-6(a)` obtains the PCS's own
group via `PGRP_OBSERVE(_getpid())`, and I confirmed `_getpid` is already in
`§P1-3.4`'s `from os` binding list (composite line 594) while **`_getpgid` is
not bound anywhere in either file**. Reusing the existing buffer is therefore
strictly smaller than binding `_getpgid`, which would have required widening the
primitive surface.

**It perturbs nothing.** I diffed v1.10 against v1.11 in full. `§P1-3.2`'s
allowlists, `MS-11`'s 89 rows, `MS-13` and `S-12` are untouched — the only
`§P1-3.2` movement anywhere in this generation is `N-15`'s pre-existing
`subprocess` reduction carried forward from v1.7, not a widening. The 89-row
`reachable_closure`, its canonical length 20534 and its digest `aa974e0c…c20ee`
appear identically in both versions. `KG-1` adds no caller of any fork, wait,
kill or killpg primitive, so the PCS remains the sole caller and `S-12` holds.

**`KG-2` is sound.** Its population rule — write once, at a `§P1-7.5`
`c10`-shaped kernel verification, when the process is `PRESENT_VALID`, its start
identity matches, and its observed group equals its own pid — makes the
legitimate population exactly the group-leader pids of this PCS's own
current-generation children. It is never taken from a request operand, a durable
record or a peer artifact, and never re-derived, widened or repaired. That is
the "kernel-verified group" `§P1-8.5` and `§P1-10.5` already require; `KG-2`
states it literally so the predicates are decidable rather than assumed. A NULL
field is not group-signalable and `KV-2` refuses it.

### Q5 — `R3`, the accounting. **Digests and structure YES. One dependent literal WAS missed (L-X2).**

All eight provenance digests recomputed from the files on disk — **eight of
eight MATCH**, at the exact paths stated (v1.6 amendment, composite v1.9, the
two v2.9 confirmations, v1.7 amendment, composite v1.10, the two v2.10 targeted
confirmations).

Counts recounted from the produced bytes, not read from prose:

```text
MS-2 literal (digest, path) rows          63   distinct 63   claimed 63   OK
MS-3 literal rows                          7                 claimed  7   OK
MS-8  2 + 63 + 7 + 1 + 1 + 2 + 1 =        77                 claimed 77   OK
composite provenance region rows          71   distinct 71   claimed 71   OK
```

I then swept every dependent literal in both files. The cascade is thorough —
`MS-9`'s inspected-string count `64 -> 72`, its union `2+63+7+1+1+2+1 = 77`, the
`TS-3` `member_count`, `B7`, `B17`, `OR-9`, `CK-4`, `CK-6`, `CK-13`, `IR-1`,
`IR-13` row 38, and test rows 103 (`62 -> 70`), 104, 105, 106, 107 (`69 -> 77`
and `68 -> 76`), 108 (`70 -> 78`, `62 -> 70`, `55 -> 63`) and 115 were all
updated correctly.

**One was missed.** Amendment `N-16`, line 4497:

> ``…unchanged; `MS-8`'s member cardinality is 69 and none of the four is in it;…``

`MS-8` is 77. The literal was **correct in v1.7**, where `MS-8` was 69, and was
carried verbatim into v1.8 without the cascade. `N-14`, twenty-nine lines below
it at line 4526, states "`MS-8` is 77, up from 69" — so the same document
contradicts itself. The composite is clean; this is amendment-only prose outside
both delimited regions.

Not executable, and I tried to make it so. `N-16` is a negative-claims clause
whose operative content is that the four `MS-13` dependencies are not members;
the cardinality is a supporting parenthetical. Eight operative loci fix the
count at 77, five of them inside the byte-identical joint block, and an
enumeration of 69 is refused at `CK-4`/`CK-6` structurally and at `B7`/`B17`.
The handoff's own `D-6` even names 69 as a required *failing* enumeration.

**Both other structural judgements are correct.** Entering all eight rows in one
update is right: splitting them would require an intermediate generation whose
only content is provenance growth, which would itself need superseding and add
four more rows — a round that does not terminate. And refusing to substitute the
two W-B binding reviews for the v2.10 pair-confirmation rows is right; they
attest a different round and are not this generation's supersession set.

### Q6 — `R4`, the transformation and the census. **YES on all three parts.**

I recomputed the census from the composite bytes:

```text
marker-bearing lines, composite v1.11    20    claimed 20   OK
marker-bearing lines, amendment v1.8      0    claimed  0   OK
[W-A] occurrences / [W-B] occurrences  13/13   claimed 13/13 OK
both-marker lines, whole file   83, 2531, 6747, 6775, 6786, 6885    exact match
both-marker lines, body only    2531, 6747, 6775, 6786              exact match
region sentinels at 251 / 6845 / 6847 / 6888 / 6890 / 7094          exact match
region distribution  PREAMBLE 3 (2/2)  BODY 16 (10/10)  GUARDDATA 1 (1/1)   OK
```

The §2.3 body locus table lists twenty line numbers. I compared them
element-by-element against my computed census: **identical, in order.**

**The Cell-2 transformation reaches every marker-free assertion.** I read
composite lines 55–95 directly. Markers occur only at 79, 80 and 83; the four
assertions the signature discharges — the blocking notice at 57–58, "what
remains open" at 60–62, the W-A exposition at 64–68 and "selects neither" at
75–76 — are all **marker-free**, which is exactly why v1's marker census could
not reach them and `PO-2` could not see them. All four are covered by the v2
table with the right action (REPLACE, REPLACE, DELETE ENTIRELY, REPLACE). That
is a genuine repair of `Y-M4`/`X-2`.

Observation L-X6: the table's spans are *sentence* spans, not a line partition —
lines 58, 60, 85 and 88 each appear in two rows with different actions, because
sentences straddle line boundaries. The prose calls the table "line by line" and
"byte-exact", which overstates it. Non-executable: no replacement text is
written by this binding, `OR-4` is not authorized, and the acceptance criterion
is `CT-1`..`CT-6` plus `PO-9`, which are content properties over the resolved
file and are indifferent to reflow.

**The §2.5 permitted-occurrence table is exact and mechanical**, and I found no
rule in it that contradicts `TS-1`, `IR-13` row 47, the `CK-14` fixture or the
guard data. `IR-13` row 35 remains sole owner of the `B14` equality and row 47
sole owner of the `A8` option-set relation; neither moved.

**`PO-9` is sufficient.** `D1` catches marker-free open-cell prose because it is
a normalized *content* check whose pattern list is required to be derived from
the pre-resolution Cell-2 span line by line and to cover every REPLACE row —
which is precisely the gap that let v1 miss lines 57–58, 60–62 and 75–76. `D2`
catches marker-free W-A grants by enumerating the six capabilities rather than
the token. The class-R exclusions are correctly drawn: the joint block (where
`TS-1`'s grammar, its pairing rule and the `CK-14` fixture *must* name the W-A
token), the Cell-2 replacement's single historical sentence (which `CT-2`
confines to naming the token with no capability), and `R-5`'s seven
supervisor-side loci. `D3` is what makes the pair sound — it blocks the
degenerate resolution that satisfies `D1` and `D2` by deleting class-R
occurrences. `D4` pins `H_GUARDDATA`. Holding the pattern list in the oracle
rather than the composite correctly adds no normative surface and leaves
`§P1-17` and `G-10` unchanged.

### Q7 — the `H-4` log item. **MINOR. It does not reopen W-B.**

The misattribution is real: `H-4` says "`OR-11` and `CK-12` verify this and
refuse on any difference with `HISTORICAL_BYTE_MOVED`", and `CK-7` owns that
code.

I attempted the executable divergence and it fails. An implementation that
placed the `MS-2`/`MS-3` literal-digest comparison at `CK-12` would contradict
**five** operative statements, all in the byte-identical joint block:

```text
CK-7   "HISTORICAL_BYTE_MOVED IS OWNED HERE AND NOWHERE ELSE"
FC-1   "EVERY ONE OF THE 25 HAS EXACTLY ONE OWNING CHECK: HISTORICAL_BYTE_MOVED
        only at CK-7"   — and INSTALL_RECORD_NAME_MISMATCH only at CK-12
CK-13  "a member whose bytes differ from an MS-2 or MS-3 literal is already
        fatal at CK-7 with HISTORICAL_BYTE_MOVED"
IR-13  precedence table: "CK-7  HISTORICAL_BYTE_MOVED  (CK-7 precedes CK-11..CK-13)"
MS-2/MS-3 relation table: "the literal digest at MS-2 or MS-3 -> CK-7"
```

and it is **caught by an attested conformance row**. Row 109 — inside
`rows_attested` 92..115 — states that for `M2` and `M3` "the refusal fires
earlier and with a different code — `HISTORICAL_BYTE_MOVED` at `CK-7`", and
fails any fixture that places it elsewhere. `CK-15` requires
`all_rows_passed = true` over exactly those 24 rows, so the defective reading
cannot reach a conforming install.

There is also no precedence rule that would let the preamble win. `H-2`
establishes the opposite pattern in terms: the ordered steps are "STATED THERE
IN FULL, AND THEY ARE NOT RESTATED IN A SECOND FORM ANYWHERE" — the canonical
block is a summary layer over the joint block, not an authority above it.

**Classification: Minor.** It is a defect in governing bytes and it should be
repaired, but it is not one this round must reopen for. It sits inside the
canonical delimited block, so repairing it costs a full generation (both region
digests, `H_FILE`, the `§A0.4` anchor, the `TS-1` digests, the packet and the
binding all cascade). **The round that should carry it is the next authoring
round that opens the governing pair for any other reason** — not a round of its
own, and not this one. Logged as L-X4; I agree with the closure's decision to
report rather than silently repair it, and for the reason the closure gives.

### Q8 — implementation-scaffold eligibility. **YES on all four parts.**

**The narrowing is honest and complete.** `§H-0` states without hedging that no
path on the allowed list can implement the runtime behaviour v1 described, and
`§H3` is retitled to modelling-only. I read every one of `D-1`..`D-7` looking
for a sentence that still implies runtime implementation and found none — each
is explicitly a constant, a frozen set, an enum or a pure function over
synthetic data, each with an explicit negative ("NO DESCRIPTOR IS OPENED…", "NO
EOF IS OBSERVED…", "NO MEMBER IS ENUMERATED FROM DISK"). The exclusion list
names the freeze classifier — including `KG-1`, `KG-2`, `KV-1`..`KV-6`,
`SC-1`..`SC-8` — as not implementable here, with the right reason: **a
definition is not an authorization.**

**The three removed v1 test paths were correctly removed**, and none of them was
implementable. A classifier-ordering test has no implementation under test; a
negative-surface test over a surface that does not exist is not a test; and
`R-5` forbids process-control smoke outright, so the disposable integration test
had nothing to run. Removing them narrows the claim rather than the capability.

**`D-4` is a legitimate declarative check, not a classifier.** `SC-7` is a pure
function of four enum fields and has no I/O component whatever — I evaluated it
myself over 72 invented tuples in this review without touching a process. The
classifier's executable content lives in `KV-3`'s fresh kernel observation,
`KV-6(a)`'s `PGRP_OBSERVE`, `KG-1`'s `/proc` read and `_killpg`, and `D-4`
touches none of them. It reads no handle table, no pid and no `/proc`, and emits
tokens rather than signals. It proves the partition is total and proves nothing
about a running system, which is what it says.

**`§H11` is complete and the split is the right boundary.** It is in fact a
five-stage graded table, and every excluded surface is placed in it: acceptance
→ inactive-scaffold authorization → runtime implementation authorization →
one-shot atomic-handoff authorization (`OR-3`..`OR-11`, which owns the `M5`
verifier and the two `M6` modules because those are member paths) → a separate
`T` activation act. Separating the inactive scaffold from runtime implementation
is correct precisely because the two allowed modules are pure and the runtime
routes are not; collapsing them would let a pure-module authorization carry a
syscall surface.

**I verified the scaffold claims no runtime implementation by checking the
working tree**, not by reading the document:

```text
src/philosophia/officina/p1_wb_oracle.py         absent
src/philosophia/officina/p1_wb_contract.py       absent
tests/test_officina_p1_wb_oracle.py              absent
tests/test_officina_p1_wb_contract.py            absent
tests/fixtures/p1_wb/                            absent
tests/test_officina_p1_freeze_authority.py       absent   (MS-6 module 1)
tests/test_officina_p1_install_integrity.py      absent   (MS-6 module 2)
successor/officina/authorization/                absent
successor/officina/runtime_control/              absent
scripts/officina_process_control_bootstrap.py    absent
scripts/officina_role_bootstrap.py               absent
src/philosophia/officina/verification.py         exists — the non-enforced
                                                 pre-install baseline, NOT M5
test_p1_row_NNN_ functions, whole repository     0
```

No scaffold code exists. `OR-5`'s and `OR-7`'s paths are all absent. The
handoff's frozen-path list correctly identifies the untracked
`generic_harness.py` and `accounting.py` as not to be touched.

### Q9 — identity and acceptance. **YES. Preserved exactly.**

I verified `C-1`'s mechanical claim rather than accepting it: **`attested_pid`
and `attested_pgid` occur zero times in composite v1.11 and zero times in
amendment v1.8.** There is no schema, key, type, carrier, consumer or
destination for an identity observation anywhere in the pair, so code written
now could only be invented — which is the invention `§P1-13.2` row 2 forbids in
the words "This document chooses neither and invents no value."

I diffed composite lines 13–54 across v1.10 and v1.11. **The Cell-1 blocking
notice is byte-unchanged except for one repair** — "Version 1.9 does not accept"
became "Version 1.11 does not accept", correcting a self-reference that was
already stale in v1.10. The substance stands unchanged.

No identity-observation code, not the `XS-1` combined binding, the weakening
unaccepted, the combined binding still blocked. The binding performs `XS-1`(a)
only — recording path and digest in the same register `XS-1` itself uses — and
performs neither (c) nor (d); restating (a) cannot constitute becoming the
combined binding, because `XS-1` already performs (a) in the governing bytes.
That reasoning is sound.

**Recording Cell 1 as gate 0 of the BINDING ledger is the correct scope boundary
for `X-3`.** The alternative — adding a paragraph to the composite — would edit
a governing document to record a fact about a *different* cell that this
signature does not discharge, which is exactly what `CT-5`, `N-4`, `N-13` and
`XS-1` are at pains to keep separate. A ledger entry in a draft binding is
auditable without touching governing bytes.

The acceptance token is version-bumped correctly: `…AMENDMENT_V1_8` appears, and
the `V1_7` token occurs **zero** times in either file. The retired anchor tokens
`P1_WATCHDOG_V2_8/V2_9/V2_10_PRE_SELECTION_COMPOSITE_SHA256` occur **zero**
times in either file. The live token `P1_WATCHDOG_V2_11_PRE_SELECTION_COMPOSITE_SHA256`
matches `A16(d)`'s grammar on **exactly one** line (amendment 327), and its
value equals composite v1.11's `H_FILE` — so the anchor is extractable by its
own rule, which is the defect class v1.7's `R1` existed to close.

### Q10 — scope discipline. **One locus moved outside the stated list (L-X1). Nothing else.**

I diffed both governing files against their predecessors in full and classified
every hunk. The composite diff is 510 added / 112 removed lines; the amendment
464 / 290. Every change falls into: `R1` (canonical block, range, fixture),
`R2` (the `KG`/`KV`/`SC` definition, 255 new lines at `§P1-10.7`), `R3` (the
accounting cascade), `R4`/`R5`/`R6`, or generation-scoped version strings.

I word-diffed all ten changed test rows to check for substantive movement:

```text
row  89   R2 — SC-1..SC-8 named, per-signal re-evaluation, adversarial scope fixtures
row 101   R2 — SC-5's closed seven-token set pinned, no eighth
row 103   count 62 -> 70
row 104   count 69 -> 77
row 105   count 69 -> 77
row 106   R1 — "ten" -> "eleven" groups, group (k) enumerated; count 69 -> 77
row 107   counts 69 -> 77, 68 -> 76, 55 -> 63
row 108   counts 70 -> 78, 69 -> 77, 62 -> 70, 55 -> 63
row 114   generation strings v1.6/v1.10/v1.7/v1.9/v2.9/v2.10 -> one generation forward
row 115   count 69 -> 77
```

**No author cell, authority, option, token, mechanism, treatment, scientific
constant, member class or count outside the stated list moved.** The 89-row
`reachable_closure`, its length 20534 and its digest are byte-unchanged;
`MS-13`, `MS-11`, `S-12`, `FC-1`'s 25 codes, `CK-13`'s D1/D2 partition,
`IR-13`'s `K1`..`K5` boundary, `MS-6`'s two modules, `MS-7`'s attestation
triple, the seven member classes, `H_GUARDDATA`, `FS-1`..`FS-5`, `TR-2` and row
106 group (i)'s expected PASS are all unchanged. `T` and the programme claim did
not move.

**The one locus that moved incorrectly is inside `R1` itself** — row 106's group
count. See L-X1 below.

---

## §4. Findings

None meets the executable Critical/Major bar. Ordered by materiality.

### L-X1 — row 106 declares eleven fixture groups and defines ten. **Major-descriptive. NEW this round. Governing bytes.**

Composite v1.11 test row 106 opens:

> "**two-stage author authorization — eleven fixture groups. Groups (a)
> through (g), (j) and (k) are refused with the named codes;…**"

The row defines groups **(a) through (j)** — ten — each introduced by a bold
`**(x)**` marker. **Group (k) is never defined**, in row 106 or anywhere else in
either governing file. The string `(k)` occurs exactly once in the row: in the
header enumeration above.

```text
v1.10  header "ten fixture groups"      bodies defined: a b c d e f g h i j  (10)   consistent
v1.11  header "eleven fixture groups"   bodies defined: a b c d e f g h i j  (10)   INCONSISTENT
```

This was introduced by this round, in the `R1` repair, in an **attested** row
(106 ∈ `rows_attested` 92..115). The intended referent is inferable — the
closure's §4.3 says row 106 "carries the same state as fixture group (k)", and
the only candidate is the `CK-14` first-and-only-refusal fixture, which group
(f) does *not* already cover (f asserts the code; the `CK-14` fixture asserts
the full `CK-2`..`CK-13` pass trace). But the row does not say so.

**Why it is not executable.** `CK-15` verifies `M7`'s `rows_attested`,
`row_count` and `all_rows_passed`; it does not re-run the suite or verify any
row's fixture content. A build implementing ten groups and one implementing
eleven both produce a valid `M7` and both pass the gate — no state's accept or
refuse answer differs. The obligation to carry the mismatch fixture is anyway
held independently by the joint block, where `CK-14` states it in full and `H-3`
declares that a suite lacking it is INCOMPLETE. So the dangling label costs no
safety; it is a governing enumeration that does not match its own content.

**Disposition.** Next authoring round that opens the pair. Either define group
(k) as the `CK-14` fixture, or revert the header to "ten" and rely on the joint
block. It should be repaired together with L-X4 and L-X2 in one generation.

### L-X2 — amendment `N-16` states `MS-8` = 69. **Minor. NEW this round. Governing bytes.**

Amendment line 4497. Correct in v1.7, stale in v1.8, contradicted by `N-14`
twenty-nine lines below and by `MS-8` in the joint block. Full analysis at Q5.
Not executable: refused at `CK-4`/`CK-6`/`B7`/`B17`. Same disposition as L-X1.

### L-X3 — "content bytes" are character counts. **Minor.**

`4052` / `222364` are UTF-8 character counts; the byte lengths are `4061` /
`222736`. Packet §1.2 lines 126/129, binding v2 lines 64–65, closure §4.1. Full
analysis at Q1. Not executable — no operative clause reads a region length. The
two governing files are unaffected; only the packet and the binding carry it, so
this one can be fixed without a governing generation.

### L-X4 — `H-4` attributes `HISTORICAL_BYTE_MOVED` to `CK-12`. **Minor.**

Full analysis at Q7. I concur with closure L-1. Carry in the next round that
opens the pair for another reason.

### L-X5 — closure §4.2 miscounts the twelve-check mentions. **Closure-only.**

"Three times in each file" is right for the composite and wrong for the
amendment, which carries five. The substantive claim — that none is operative —
holds; I verified all eight. The closure is normative for nothing, so this
corrects the record only.

### L-X6 — binding §2.2's Cell-2 spans overlap. **Observation.**

Lines 58, 60, 85 and 88 each appear in two rows with different actions, so the
table is a sentence-role table rather than the line partition its prose claims.
Non-executable; acceptance runs through `CT-1`..`CT-6` and `PO-9`, which are
content checks. Worth a wording fix when the binding is next revised.

### L-X7 — `KV-6` masking argument is unstated. **Observation.**

The dominance is sound (proof at Q3), but the reason a forbidden target masked
by an earlier-failing predicate is harmless — `SC-2` excludes it from scope, and
`KV-6(b)` scans all watchdog handles regardless — is left to the reader. One
sentence in `SC-6` would close it.

### Closure L-2 — composite line 94's "a finished replacement for v1.2".

I agree it is stale by many generations, and note it sits in the 93–95 span that
§2.2 marks RETAIN. Not a generation-scoped operative string; log only.

---

## §5. What I checked and found clean

Stated so the Y line can see the negative space of this review. Both delimited
regions and their cross-file byte equality; delimiter cardinality; every
operative `CK` range; the `B1`..`B18` trace; `SC-7`'s 72 tuples by brute force;
`KV-2`/`SC-7` agreement; `SC-5`'s closed token set; `SC-8`'s structural
continuation; `KG-1`'s primitive and import surface; `_getpid` bound and
`_getpgid` unbound; `pgid_or_null`'s pre-existence in `§P1-8.5`; the eight
provenance digests; `MS-2`/`MS-3`/`MS-8`/provenance counts recounted from bytes;
all four region digests; `H_GUARDDATA` unchanged across v1.10/v1.11; the full
marker census and region distribution; the twenty body loci; the Cell-2 span
read directly; `PO-9`'s four detectors; `attested_pid`/`attested_pgid` absence;
Cell 1 byte-comparison; the acceptance and anchor tokens; anchor-line
cardinality and value; the test matrix row count and `rows_attested`; every
changed test row word-diffed; the working tree against the scaffold's claims;
and the commit's file-level scope.

---

## §6. Exact next boundary

```text
THIS REVIEW AUTHORIZES: the paired independent Y-line review on identical bytes,
and — only after that Y line passes — an author's SEPARATE consideration of
amendment v1.8 acceptance. Nothing else.

EXPLICITLY NOT AUTHORIZED BY THIS REVIEW
  no acceptance of I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_
    AMENDMENT_V1_8; the v1.7 token is retired and must not be signed
  no inactive-scaffold authorization; no code at any allowed path, including the
    oracle and the contract module
  no runtime implementation authorization
  no key, entropy, seed, Stage A or Stage B
  no OR-3, no OR-4, no OR-5..OR-11, no one-shot atomic-handoff authorization
  no identity-token acceptance and no bounded weakening under any name
  no T activation and no programme-claim movement
  no edit to any governing, historical, code, test, signature or runtime path

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
XS-1 COMBINED IDENTITY BINDING = BLOCKED ON SEPARATELY REVIEWED AND ACCEPTED
  BOUNDED WEAKENING
```

```text
OFFICINA_P1_WB_V2_11_X_CONFIRMED_FOR_ACCEPTANCE_REVIEW
```

The exact selected token and the formal selection signature govern. This review
is an independent X-line assessment of the six named inputs at commit `d273765`
and is normative for nothing beyond the boundary stated above.
