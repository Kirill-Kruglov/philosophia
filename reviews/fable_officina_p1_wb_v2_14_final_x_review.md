# Officina P1 W-B v2.14 — final bounded X-line review

**Reviewer.** Claude Code Fable 5, independent X line. Read-only, no repository
byte modified outside this one file, nothing committed, no resolved output and
no `MP-1` candidate retained at any path.

---

## VERDICT

```text
OFFICINA_P1_WB_V2_14_X_CONFIRMED_FOR_AUTHOR_ACCEPTANCE
```

`T = NOT_ACTIVATED`; claim = `OPEN`. This confirmation permits only Kirill's
later consideration of amendment `v1.11`. It authorizes no code, no scaffold,
no key, no `OR` step, no install and no activation.

**One Major-class defect of record is reported below (`X-1`) and it is not a
`REVISE` trigger under this review's stated gate.** The gate admits `REVISE`
only for a demonstrated executable Critical/Major **authority, classifier,
quarantine or fail-closed** defect. `X-1` is none of those four: no guard, no
`OR` step, no manifest field and no verifier rule consumes the value, and the
substantive property it witnesses **holds and was verified three ways**. It is
nonetheless a false normative sentence in both governing files and should be
repaired before any `OR` step. If Kirill elects to treat the pair's own clause
*"ANY DIFFERENCE IS A DEFECT IN THIS INDIVISIBLE PAIR"* as binding on its face,
that alone justifies a corrective generation — **that call is his, not mine**,
and I state the finding plainly rather than grading it away.

---

## Path and digest of this file

```text
reviews/fable_officina_p1_wb_v2_14_final_x_review.md
SHA-256  <recomputed by the reader; this file contains none of its own digests>
```

## Pinned bytes — recomputed before any analysis

All six recompute exactly. **No mismatch; not `BLOCKED`.**

```text
3571c1f75283851e4cf1a9b04dfe67c2f35d9c52392e6b97582274195b475cf7  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_14_CORRECTION.md      OK
5f2c74ff371f618039de705f21464454684da122f91e06c251e147bfc61d26be  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11_DRAFT.md OK
11c8963ac3cbd4c72a90b0a1f0fdc0fe3bfb35be84a974c3a2a953ec699bbdee  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_14.md OK
0b08bd3e5e49666dddb475c1e282589a0c1d940221bdebf7ca132a860d4564f1  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V5_DRAFT.md                        OK
9b07b718a6f5de7c27d05bec6a205813329255b8b344adfe0447338357814a77  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V5_DRAFT.md                        OK
b981a88e724c493f2d84d1a92d448394ce21f931e5584fe8f49690b0158b9f92  reviews/opus5_officina_p1_wb_v2_14_governing_repair_closure.md                     OK
```

**Commit note, disclosed rather than silently absorbed.** The prompt names
`cb37808`; repository `HEAD` is `69b69aa`, its child. `git diff cb37808 69b69aa`
touches **only** the two review-request prompts
(`reviews/fable_..._final_x_review_prompt.md`,
`reviews/sol_..._final_y_review_prompt.md`, 143 insertions, no deletions). Every
pinned surface is byte-identical between the two commits, so the review is
against the intended bytes and this is not a `BLOCKED` condition.

The authored closure was treated as untrusted throughout. **No derived table of
`reviews/opus5_officina_p1_wb_v2_14_governing_repair_closure.md` was used as an
input.** `SC-9`/`SC-10` were implemented from the composite prose, and the
`§2.2.5` transform from the binding prose; the closure was opened only at the
end, to compare figures.

---

## X-Q1 — TOTAL CLASSIFIER REDUCTION

`SC-9` `P1`..`P6` and `SC-10` were re-implemented from `§P1-10.7` of composite
`v1.14` alone, with handle tables modelled as **ordered** lists and `KG-1`
observations scripted so the classifier is drivable without a kernel.

### The question, answered

> Report whether `(terminal, qualifier, per-entry token, signal sequence)` is a
> single permutation-invariant function.

**YES. It is a single permutation-invariant function, and no counterexample
exists in anything I could drive.** Across every fixture below — several
thousand executions — the number of distinct
`(terminal, qualifier, per-entry token, signal sequence)` tuples produced by the
permutations of any one table was **exactly one, without exception**.

### What was driven, and the results

**(a) The exact `Y-M1` table, both orders.** Two structurally valid
current-generation prospective candidates, both `CONTROLLER`/`RUNNING`/`OWNED`,
both recorded groups unprotected; `a`'s `PHASE-4` observation `PRIMITIVE_FAULT`,
`b`'s `PRESENT_VALID` with fresh `pgrp` in `G`.

```text
order [a, b]  ->  T1 PCS_FREEZE_CLASSIFIER_STRUCTURAL_VIOLATION
                  FREEZE_NOT_ATTEMPTED, NO SC-5 token, site a, ZERO signals
order [b, a]  ->  T1 PCS_FREEZE_CLASSIFIER_STRUCTURAL_VIOLATION
                  FREEZE_NOT_ATTEMPTED, NO SC-5 token, site a, ZERO signals
```

The `v1.13` split (`T1` for the first order, `T3` for the second) is closed.
`F` non-empty dominates `P` non-empty by `STEP 4B`'s stated intra-phase
precedence, and the precedence never consults order.

**(b) Every permutation of the `PHASE-4` pair matrix.** All seven rows, both
orders, all tuple-invariant:

```text
a:PF b:PF -> T1, token NONE,                signals ()
a:PF b:FP -> T1, token NONE,                signals ()      the Y-M1 row
a:FP b:PF -> T1, token NONE,                signals ()      the same, permuted
a:FP b:FP -> T3, KV_FORBIDDEN_TARGET,       signals ()
a:PF b:OK -> T1, token NONE,                signals ()      b DISCARDED
a:FP b:OK -> T3, KV_FORBIDDEN_TARGET,       signals ()      b DISCARDED
a:OK b:OK -> no PHASE-4 terminal; PHASE 5 begins
```

Both non-`PRIMITIVE_FAULT` sources of `(o4)` were driven separately — a
wrong-shaped `KG-1` return object and a `BaseException` raised while taking or
reading the observation. Both produce `T1` in both orders, confirming `(o4)` is
the union `SC-8` states and not `PRIMITIVE_FAULT` alone.

**(c) Tables with three or more mixed observations, exhaustively.** All 27
three-entry combinations over `{PRIMITIVE_FAULT, fresh-protected, clean}`, then
all **216** three-entry combinations over the six classes
`{PF, FP, OK, ABSENT, ERROR, UNPARSABLE}`, each driven through **all 6
permutations**; plus five four-entry combinations through all 24 permutations.

```text
permutation-variant tables found: 0
```

The non-terminal non-`PRESENT_VALID` classes behave as `SC-9` `P4` states: they
are collected, they raise nothing, and they are carried to `PHASE 5` where
`KV-3` fails for that entry with `KV_OBSERVATION_UNAVAILABLE`.

**(d) The analogous collisions at every `PHASE-6` recheck.** Driven per group
and per signal number, for schedule `(15, 9)`:

- With one handle per group, a collision on the **first** group yields the
  terminal with `FREEZE_NOT_ATTEMPTED` and zero signals; a collision on the
  **second** yields it with `FREEZE_ABANDONED` after exactly the first group's
  two signals. The qualifier depends on whether a signal has issued in the pass
  and not on which terminal was selected, exactly as `P6` states.
- With **two handles sharing one group**, so that both terminal-bearing
  predicates collide inside one re-verification, the reduction returned the same
  answer `PHASE 4` gives for the same multiset, in both orders, for all four
  collision classes.
- Per-signal-number separation holds: a success established for signal 15 is not
  carried to signal 9; a group cleared at 15 whose recheck at 9 observes a
  protected `pgrp` abandons at 9.

**(e) Terminal-bearing predicates in Phases 1, 2, 3 and 5.**

```text
PHASE 1  role / state / ownership outside §P1-8.5's literals; pgid_or_null a
         bool; pgid_or_null a str; generation_id absent, 63 hex, uppercase;
         table not a mapping        -> T1, token NONE, ZERO signals, order-invariant
         stale entry + malformed role beside a valid candidate   -> T1  (CE-3(ii))
         recorded supervisor group + malformed state             -> T1  (CE-3(i))
PHASE 2  stale generation is a TERMINAL, not a skip -> T2, KV_STALE_HANDLE, zero signals
         stale + recorded-protected -> T2 ;  stale + fresh-protected -> T2
PHASE 3  KV-6(a) scanned regardless of role, state and ownership: every one of
         role WATCHDOG / WORKER, ownership CONTRADICTED / REAPED, state REAPED,
         against each of the PCS's own group, a watchdog pid, a watchdog leader
         group and the recorded supervisor group -> T3, KV_FORBIDDEN_TARGET,
         ZERO signals, order-invariant
PHASE 5  raises NO terminal: all five SC-6 outcomes are skips or KV_OK
```

The `row 89 (2)` permutation fixtures were run as a single family — the
protected entry at position 1, at every interior position, at the last position
and as the only entry; and separately carrying **each** of the 3 roles × 4
states × 3 ownerships; and with the protected value being in turn the PCS's own
group, a watchdog leader group, a watchdog pid and the recorded supervisor
group. **Distinct answers across that entire family: 1**, namely
`(T3, FREEZE_NOT_ATTEMPTED, KV_FORBIDDEN_TARGET, no signals)`.

`SC-7`'s partition was recomputed independently and is exact:
`role WATCHDOG 24`, `ownership CONTRADICTED|REAPED 32`, `state REAPED 4`,
`pgid_or_null NULL 6`, `proceed 6` — `24+32+4+6+6 = 72`, no tuple unclassified
and none with two answers.

**(f) Candidate discard, ownership non-mutation, per-entry token, qualifier.**

- `CE-1` reproduces: `PHASE 3` scans the `CONTRADICTED` handle regardless of its
  ownership, terminates `T3`, and sends **zero** signals including none to the
  valid handle's group. The dominant answer is **not**
  `KV_ROLE_OR_STATE_REFUSED`.
- `CE-2` / `X-M1` reproduces in both forms. Fresh-protected on `b` with a clean
  `KV_OK` on `a`: `T3`, `a`'s collected candidate **discarded**, zero signals.
  The `KV-4` form — `b`'s start identity mismatching instead of its group —
  gives the same zero-signal terminal and **sets no ownership to
  `CONTRADICTED`**, because `KV-4` is never evaluated. I checked the mutation
  list explicitly on every such run and it was empty.
- Identity mismatch **plus** group mismatch on one entry with no protected group
  anywhere gives `KV_IDENTITY_CONTRADICTED`, a `PHASE-5` skip, and ownership
  `CONTRADICTED` — `KV-4` precedes `KV-5` in `SC-6`, as stated.

**(g) All paths to `_killpg`.** An exhaustive sweep over
`role × state × ownership × pgid_or_null × 11 observation classes`, each beside
a clean candidate, in both table orders:

```text
tables driven                        1584
tables emitting at least one signal  1224
violations of SC-9 P6's six conjuncts   0
```

No signal precedes completion of Phases 1..5: every emitting run had no
terminal, and every emitted `(group, signal)` satisfied ownership `OWNED`, role
`CONTROLLER|WORKER`, state not `REAPED`, a `PRESENT_VALID` observation with
matching identity, `pgrp == pgid_or_null`, and `pgrp ∉ G`. No further signal
follows a `PHASE-6` terminal: driven for 2-, 3- and 4-group schedules with the
fault placed at every group position, the signal count was always exactly
`2 × (groups cleared before the fault)` and never one more. `SC-2`'s scope
sequence is deduplicated and ascending and permutation-stable — a group shared
by two handles is signalled once per signal number.

### X-Q1 verdict

**No counterexample.** `(terminal, qualifier, per-entry token, signal sequence)`
is a single permutation-invariant function of the handle table.

---

## X-Q2 — FULL TRANSFORM AND QUARANTINE FIXTURE

`§2.2.5` `RESOLVE` was implemented independently against composite `v1.14`.
Sentinels were re-derived from the binding's own `§2.2.1` sentinel block rather
than hand-transcribed, after a hand transcription of `S6`'s LAST sentinel proved
wrong by two spaces — **my error, not the document's**; the document's bytes are
correct and unique.

**Every span, both directions.**

```text
SPAN  SRCLEN   src digest   REPLEN   rep digest   sentinel cardinality
S1     2184 OK      OK       2120 OK      OK              1 / 1
S2      163 OK      OK         61 OK      OK              1 / 1
S3      598 OK      OK        207 OK      OK              1 / 1
S4      298 OK      OK         22 OK      OK              1 / 1
S5      299 OK      OK         47 OK      OK              1 / 1
S6      218 OK      OK         61 OK      OK              1 / 1
S7      982 OK      OK        727 OK      OK              1 (prefix)
S8     1329 OK      OK        440 OK      OK              1 / 1
S9      504 OK      OK        271 OK      OK              1 (prefix)
S10   14213 OK      OK      14123 OK      OK              1 (prefix)
S11     449 OK      OK        315 OK      OK              1 (prefix)
```

Every informative line number in `§2.2.1` is also correct against `v1.14`
(`55..95`, `306..307`, `1768..1775`, `1778..1782`, `2266..2269`, `2291..2293`,
`3972`, `4255..4272`, `8205`, `8233`, `8244`).

**Non-overlap and order.** Sorting by ascending `b_i` gives `S1..S11` in name
order, and `e_i < b_{i+1}` holds for all ten adjacent pairs. Verified as part of
the algorithm, not assumed.

**The four single-line substring replacements**, each rendered from the
document's own delimiter rule before comparison:

```text
S7   DEL 277 bytes  1f8cd74f…7232 OK   INS  22 bytes  523a0dd8…d9a9c OK   1 occurrence
S9   DEL 352 bytes  b14fbde3…44bd OK   INS 119 bytes  09d3b27d…8699  OK   1 occurrence
S10  DEL 155 bytes  5b23c45a…0007 OK   INS  65 bytes  68257fda…c8b6  OK   1 occurrence
S11  DEL 337 bytes  fcdefe4c…f086 OK   INS 203 bytes  9776e99c…1140f OK   1 occurrence
```

**`S7` renders at exactly 277 bytes and its pinned hash**, from the two-backtick
delimiting the document now specifies. `X-L3`, which I logged against `v4`, is
repaired: the literal reproduces at its stated length and digest on its own, and
not only through its containing line. Each deleted literal occurs exactly once
in its uniquely identified line, so the substring replacement is unambiguous.

**Full output.**

```text
FULL RESOLVED OUTPUT   624840 bytes            pinned 624840            OK
SHA-256   9904ff3bf73f90329df7ac06fac5dbf4b211713964f610541761018c9bacb5c5   OK
byte arithmetic   627683 − 21237 + 18394 = 624840                        OK
```

**Three region digests, recomputed on my own resolved bytes.**

```text
H_BODY       731b4d662be269c8a67cb142ebb7fc5c38424bc91934ec40df54b10be18a677b  OK
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426  OK
H_NORMATIVE  313160d7c1fb240c43ef43bb5432c63a0391f60052648af8115b69aa67f2a268  OK
```

`REGION(GUARDDATA)` is **byte-unchanged**, 1816 bytes, compared directly against
composite `v1.14`'s own extracted region — not inferred from the digest match.

**Both delimited-region identities**, extracted by their own two delimiter lines
from **composite `v1.14`, amendment `v1.11` and my resolved output**, and
compared all three ways with zero difference:

```text
canonical atomic-handoff preamble   4168 bytes  7d5cd45363f1…f340084   identical x3
joint install and authorization   224756 bytes  5e8a30dde590…08eba30   identical x3
```

No span intersects either block: the handoff block occupies lines 8071..8134 and
the joint block 4714..7848, and the intersecting-span set is empty for both. The
highest body span before the joint block ends at 4272 and the next begins at
8205, straddling it without entering — as `§2.2.6` states.

**`MP-1`, constructed solely from its published anchor, payload, order and
newline rules before any digest was compared.**

```text
anchor cardinality in the resolved output   1        (exactly one; not FAILS CLOSED)
payload                                     4 lines, last empty, ends with two 0x0A
PAYLOAD LENGTH                            195        pinned 195               OK
PAYLOAD SHA-256   ee8a830d46f709ff2ffd95238600437e885c32d84bf268a1658950cd5ed63d2f  OK
FULL LENGTH                            625035        pinned 625035 = 624840+195  OK
FULL SHA-256      ba513ff06338eef1228d4c640617a08d1ab0da1869110cac2b4d99ee42cedb39  OK
```

`X-L4`, which I logged against `v4`, is repaired: the digest now reproduces from
the published recipe. The ordering constraint is real and load-bearing — placing
the blank line **before** the paragraph instead of after yields a different
digest, so the stated order is part of the value.

**Detector and `PO-0` behaviour on `MP-1`.** `PO-0` **FAILS**, as required,
because `ba513ff0…` is not `9904ff3b…`. `H_GUARDDATA` is unchanged, so `PO-3`
passes. The payload contains no `[W-A]`, `[W-B]`, `t-wd-freeze.v1` or
`SOCK_SEQPACKET` literal, so `D1`/`D2` see nothing and `PO-1`/`PO-2` pass. The
fixture therefore demonstrates exactly the `§2.6.0` boundary it claims: a
candidate that reintroduces a W-A capability in words the detectors do not list
passes every detector and still fails, because the complete output is
byte-pinned. **No claim exceeds its detector here.**

**No resolved output and no `MP-1` candidate was written to any path.** Both
existed in memory in a session scratchpad and were discarded.

### X-Q2 verdict

**Every figure of `§2.2` and `§2.6.5` reproduces byte-exactly.** No defect.

---

## REGRESSION BOUNDARY

The `v2.13` repairs survive intact within the changed `R1`/transform surfaces:

```text
F8   PO-9's quarantine claim narrowed to exact listed literal coverage;
     the semantic-paraphrase claim withdrawn; MP-1 demonstrates the boundary.   HELD
F9   §2.5 W-A option token recount                                              HELD, 3 measured
F10  §2.2.2 encoding sentence: U+2014 at TWO loci and U+00A7 at FIVE, and no
     other non-ASCII. Independently censused on the S1 block: exactly {—:2, §:5}.
     37 lines, 2120 bytes.                                                      HELD
F15  S7 literal now delimited so it reproduces at 277 bytes (my X-L3)           REPAIRED
F16  MP-1 digest now reachable from its own recipe (my X-L4)                    REPAIRED
```

Trailing-space discipline verified mechanically on all seven fenced replacement
blocks: no line ends in `0x20` or `0x09`, every line ends in exactly one `0x0A`.

Every `§2.5` census figure was recounted on **my** resolved output, not read
from the closure:

```text
t-wd-freeze.v1                       pre 9 (lines 66,1772,1778,2267,2292,3972,4269,8205,8233)  post 0   OK
I_SELECT_..._A_WATCHDOG_REQUESTS_PCS_EXECUTES        pre 3  post 3   OK  (class R, not F)
P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1              pre 1  post 2   OK  (R-2 + one historical mention)
I_SELECT_..._B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS            post 3   OK
P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1                       post 2   OK
"[W-A]" / "[W-B]" outside GUARDDATA                         post 0   OK
"[W-A]" / "[W-B]" inside  GUARDDATA                         post 1 each  OK
"the v1.11 amendment is installed"                          post 1   OK
```

Every claimed pre-resolution `t-wd-freeze.v1` line number is correct, and every
one lies inside a pinned span.

No unrelated signed science was reopened and no stylistic change is demanded.
The duplicated explanatory paragraph in closure `§12` is treated as the known
non-normative editorial note it is and is not counted as a finding.

---

## FINDINGS BY SEVERITY

### CRITICAL — none

### MAJOR — one, and it is not a `REVISE` trigger under this gate

**`X-1` — the pinned `H_HANDOFF` value in BOTH governing files is the stale
`v1.13` digest and is false against the `v1.14` bytes.**

Composite `v1.14` at lines 8060–8061, and amendment `v1.11` at lines 1315–1316,
each state:

```text
REQUIRED, AND ANY DIFFERENCE IS A DEFECT IN THIS INDIVISIBLE PAIR:
  HANDOFF(amendment v1.11) is BYTE-IDENTICAL to HANDOFF(composite v1.14), and
  H_HANDOFF equals, in both,
    7c5cabe2e48587ad34cd19ae0f4300f78965b27afc93cb719868aae9f5cd44a7
```

Running that section's own extraction — which it explicitly publishes *"so that
a reviewer re-runs it mechanically"* — gives:

```text
HANDOFF(composite v1.14)   4168 bytes  7d5cd45363f197905f4b3d4e6fa1b470b4bb595ec00ea423775412459f340084
HANDOFF(amendment v1.11)   4168 bytes  7d5cd45363f197905f4b3d4e6fa1b470b4bb595ec00ea423775412459f340084
HANDOFF(composite v1.13)   4167 bytes  7c5cabe2e48587ad34cd19ae0f4300f78965b27afc93cb719868aae9f5cd44a7
```

The pinned literal is `v1.13`'s value. The block moved this generation — the
binding says so itself (*"BOTH REGIONS MOVED IN THIS GENERATION"*; the handoff
preamble carries `H-1`, whose replacement sentence names the superseded
generation) and it gained one byte. The **first** conjunct of the required
equality holds and I verified it. The **second** fails, in both files.

*Why this is not scored as a `REVISE` trigger, stated so the reasoning can be
checked rather than trusted.* Grepping both governing files for `H_HANDOFF`
returns exactly two occurrences per file — the definition and this assertion.
**No `G-*` guard, no `OR` step, no manifest field, no `MS`/`CK`/`IR`/`TS` rule
and no verifier input consumes it.** The joint block carries no pinned digest at
all, only a byte-identity requirement, which holds. So the defect widens no
authority, admits no signal, authorizes no install and cannot fail open; the
pair-indivisibility property the assertion witnesses is intact and independently
confirmed. It is a defect **of record**, not of authority — the witness is
stale, the fact is true.

Also worth recording plainly: the author closure at
`reviews/opus5_officina_p1_wb_v2_14_governing_repair_closure.md` lines 76–77
reports the **correct** recomputed values (`7d5cd453…`, 4168 bytes; `H_JOINT`
`5e8a30dd…`, 224756 bytes). The closure did the arithmetic and the repair simply
was not propagated into the two governing files.

**Recommended repair:** update the literal at composite `v1.14` line 8061 and
amendment `v1.11` line 1316 to
`7d5cd45363f197905f4b3d4e6fa1b470b4bb595ec00ea423775412459f340084`. Note that
doing so changes both files' bytes and therefore every downstream digest,
including all eleven `§2.2.1` span figures that straddle nothing but whose file
offsets shift, `H_FILE`, `H_BODY`, `H_NORMATIVE` and `§2.2.6`'s full-output
digest. That is a governing-byte change and is the author's to make.

### MINOR — three

**`X-L7` — `PHASE 3` carries three terminal-bearing predicates, not one, and
`SC-10` says otherwise.** `SC-10` asserts *"PHASE 1, PHASE 2 AND PHASE 3 CARRY
EXACTLY ONE TERMINAL-BEARING PREDICATE EACH … SO NO SAME-PHASE COLLISION EXISTS
IN THEM."* `SC-9` `P3` in fact carries three: `KV-6(a)`; `P3(a)`'s fail-closed
route on a self-observation that is not `PRESENT_VALID`; and `P3(c)`'s
fail-closed route on an absent, unreadable or non-conforming
`SPAWNING_GROUP.json` `process_group_id`. The collision is concrete: if
`P3(a)`'s `PGRP_OBSERVE(_getpid())` returns `PRIMITIVE_FAULT` — or a
wrong-shaped object, or raises a non-`OSError` `BaseException` — then `P3(a)`'s
sentence names `T3` `FORBIDDEN_TARGET` literally, while `§P1-10.3`'s
*"single continuation at EVERY consumer"*, `SC-8` and `SC-10`'s
*"`T1` … wherever `SC-8` arises"* name `T1`. `SC-10`'s Level-2 rule does resolve
it to `T1`, but `SC-10` simultaneously tells the implementer that Phase 3 needs
no such resolution. Separately, `P3(c)` names **no** terminal at all — it says
only *"the classifier terminates"*, leaving the member of the closed set of
three unspecified. **Consequence is confined to the journal terminal name:**
both routes are zero-signal and `FREEZE_NOT_ATTEMPTED`, and the `SC-8`
continuation's ownership clause has no identifiable pid here (the observation is
of the PCS itself, which holds no handle), so no state mutation diverges either.
Same class as `Y-M3`, but strictly inside the zero-signal fail-closed region.
**Pre-existing, not a `v2.14` regression:** the identical text is in `v1.13` at
lines 2811 and 2827.

**`X-L8` — a watchdog handle with a non-`NULL` `pgid_or_null` self-collides at
`PHASE 3` and permanently disables the classifier.** `P3(b)` puts every
watchdog's `pid` **and** its `pgid_or_null` (when not `NULL`) into `G`; the
`P3` scan then tests every current-generation entry's recorded group against `G`
*"REGARDLESS OF ANYTHING ABOUT IT … Role WATCHDOG is scanned."* A watchdog whose
field was written under `KG-2` `P-2` therefore matches `G` **through its own
contribution**, and the whole classifier terminates `T3` /
`KV_FORBIDDEN_TARGET` / `FREEZE_NOT_ATTEMPTED` with zero signals *"in this pass
and in every later pass of this generation."* I reproduced this directly. This
defeats `KG-2` `P-4`'s stated rationale — that the watchdog's field is written
*"deliberately"* and is *"load-bearing"* precisely so the group form of the
exclusion is decidable — since the moment it is written nothing can ever be
frozen. **Latent and fail-closed:** `v1.14` itself argues the field never gets
written on a conforming lifecycle (`§P1-4.1` spawns the watchdog `setsid =
False`, `§P1-9.2` says it is not a session leader, so `P-2(iii)` never holds and
`P-4` keeps it `NULL` forever), so on conforming bytes the collision is
unreachable; and the direction is zero signals, never a spurious one. Logged
because the two sentences pull opposite ways and a future lifecycle change would
make it live.

**`X-L9` — the permutation-invariance justification overclaims about the
recorded site.** `SC-9` `P4` states: *"Permuting the table permutes the indices
consistently, so the least-index member of a non-empty class is the same ENTRY
under every permutation."* That is false whenever a class has two or more
members. Smallest counterexample: three entries whose `PHASE-4` observations are
all `PRIMITIVE_FAULT` — the recorded site is entry `600`, `601` or `602`
depending on the permutation. Same for three fresh-protected entries under `T3`.
**No executable consequence, and the normative surface is intact:** `SC-9` `P4`
defines *"the answer of PHASE 4"* as its terminal, its qualifier and its
per-entry token, which excludes the site; row 89 lists the same three; and the
pair-matrix rows say *"site = the least-index entry"* rather than naming a fixed
entry. My exhaustive sweep confirms the answer so defined is invariant. Only the
supporting sentence is wrong, and it is wrong in a way that would mislead an
implementer into thinking the recorded site is stable when it is not.

### Observations, not findings

- The `S6` LAST sentinel is unique and correct; my initial hand transcription of
  it was wrong by two spaces. Recorded so the correction is attributable to me
  and not read as a document defect.
- `SC-7`'s `24 + 32 + 4 + 6 + 6 = 72` partition is exact, independently
  recomputed.
- `PHASE 4` exclusion 1's withdrawal of the `v1.13` necessity claim (my `X-L2`)
  is honest and correct against these bytes, and the exclusion is properly
  retained as conservative rather than required.
- `P4` exclusion 4 names honestly the one thing the classifier does not detect —
  a `NULL`-group handle whose live process sits in a protected group — and the
  safety argument given (it grants no scope) is sound, since `SC-2` projects
  `pgid_or_null` and there is none.

---

## EXACT NEXT BOUNDARY

Confirmation permits **only** Kirill's later consideration of amendment
`v1.11`. It authorizes:

```text
no code, no scaffold, no key, no entropy draw
no OR step of any number — in particular no OR-4
no install, no activation, no manifest or verifier edit
no selection, authorization or attestation artifact
no detached signature, no install record
no resolved amendment or composite bytes at any path
no process, socket, pipe, fork, exec, signal, wait or prctl operation
```

`T = NOT_ACTIVATED`. Claim = `OPEN`. Nothing in this review moves either.

The one thing the author should do before any `OR` step is repair `X-1` in both
governing files. I do not force a generation for it, for the reasons stated
under the verdict; whether to spend one is Kirill's call.
