# Officina P1 W-B v2.15 — final X-line confirmation

**Reviewer:** Claude Code Opus 5, independent X-line reviewer. Read-only. No
governing, history, code, test, signature or runtime artifact was modified; no
commit was made; this is the single review file created.

**Scope.** One bounded executable confirmation of `KG-2` `P-2`/`P-9`/`P-10`
against the normative composite bytes, plus the two named regression questions.
Not a design review. The authored closure
`reviews/opus5_officina_p1_wb_v2_15_final_repair_closure.md` was treated as
untrusted throughout: every number below was derived from the composite bytes
before the closure was opened, and the closure is quoted only where my
measurement and its published measurement differ.

---

## VERDICT

```text
OFFICINA_P1_WB_V2_15_X_CONFIRMED_FOR_AUTHOR_ACCEPTANCE
```

`T = NOT_ACTIVATED`; programme claim = `OPEN`.

This confirmation permits only Kirill's later consideration of amendment
`v1.12`. It authorizes no scaffold, no code, no key, no `OR` step, no install
and no activation, and it is not an acceptance of the amendment.

**Findings: 0 Major, 2 Minor, 3 Observations.** Neither Minor touches a route,
a write site, a write provenance or an authority gate; both are wording
defects with a measured blast radius, stated in §5.

---

## §1. Pinned bytes — recomputed first, all six match

```text
6a00e058e35ab4f81d80b21d5a6680344596231f1299767a076813691723f26a  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_15_CORRECTION.md      OK
e156d66293a608c9090994ae1016c1055a1c9071b71ea0384c58e7ab2595f4a8  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12_DRAFT.md OK
a41c142465c3ab0e3dfc565b6f2c1767f1b43481c28933544d72777d6e76113a  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_15.md OK
c9db32bb8b87af691c71c51a6167883cc953a43700798c9654c39d84ad1c2ff2  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V6_DRAFT.md                        OK
279f59a2de2d3d382a30463b0c72e08108f93ad3ed15473fee145d6361ebc1f1  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V6_DRAFT.md                        OK
59ab82b5d3a7c2f5565d7545a882aad805979aa7d8bf3369fb93cbe1033c2852  reviews/opus5_officina_p1_wb_v2_15_final_repair_closure.md                         OK
```

No mismatch. **Not `BLOCKED`.**

Working tree is at `8d7d14a`, not the instructed `60d92db`. `60d92db` is an
ancestor of `8d7d14a`, and `git diff --name-only 60d92db 8d7d14a` lists exactly
two files — `reviews/fable_officina_p1_wb_v2_15_final_x_confirmation_prompt.md`
and `reviews/sol_officina_p1_wb_v2_15_final_y_confirmation_prompt.md`, the two
confirmation prompts. **None of the six pinned files differs between the two
commits**, so all bytes reviewed here are the bytes `60d92db` carries. Recorded
as Observation X15-O1 rather than treated as a mismatch.

Custody spot check: the composite contains no occurrence of its own digest and
the closure contains none of its own, so `§P1-14.5`'s acyclicity is intact for
this pair.

---

## §2. Method — two implementations, neither derived from the other

**Implementation 1 — `MACHINE`.** `KG-2` `P-2`'s `W0`..`W8` written as straight
control flow from the machine prose alone (composite lines 2549–2716). It walks
`W0` (a),(b),(c1),(c2),(d), then `W1`, `W2`, `W3`, `W4`, `W5` (i),(ii),(iii),
`W6` (L1),(L2), `W7`, `W8`, and returns the route it reaches. It never reads
`P-9`.

**Implementation 2 — `PREDICATES`.** `P-9`'s nine rows transcribed as nine
free-standing booleans from the GUARD column alone (composite lines 2856–2938),
plus `P-9`'s own construction rule applied generically — *"EACH ROW's PREDICATE
IS THE CONJUNCTION OF ITS OWN GUARD WITH THE NEGATION OF EVERY EARLIER ROW's
GUARD"*. It does not import, call, or paraphrase Implementation 1, and it has no
notion of step order beyond that rule.

Both were driven over the complete published twelve-dimension cross-product.
Totality and disjointness are decided on `PREDICATES` alone; `MACHINE` is used
only to test agreement and to trace gate ordering.

Product size recomputed from the published dimension value sets:
`2·2·3·4·2·4·6·2·2·3·2·2 = 110592`, matching `P-10`'s declared count.

---

## §3. Measured results

### 3.1 Totality, disjointness, agreement

```text
COMBINATIONS ENUMERATED                                110592
combinations with NO applicable row                         0
combinations with TWO OR MORE rows                          0
MACHINE / PREDICATES disagreements                          0
```

`P-9` is total and disjoint over the full product, and the ordered machine and
the published predicates select the same route on every one of the 110592
combinations.

### 3.2 Route counts

```text
  R-A0   103680      R-A1     2304      R-B      1152
  R-C      2304      R-D       576      R-E       552
  R-F        12      R-G         6      R-H         6      TOTAL 110592
```

### 3.3 Writes, and where they occur

```text
combinations that perform the one write                     6   all via R-H
writes on any route other than R-H                          0
writes of unknown provenance                                0
second writes in any evaluation                             0
combinations that take the one observation                576   R-E 552, R-F 12,
                                                                 R-G 6, R-H 6
combinations that take no observation                  110016
```

Every writing combination has the full `W7` conjunction true — `W0`
(a),(b),(c1),(c2), `outcome == STOPPED`, `WROTE` false, (i),(ii),(iii), (L1),
(L2) — and the count 6 is exactly `2 roles × 3 EINTR values`, satisfying `(x2)`
as written. No observation is taken on `R-A0`, `R-A1`, `R-B`, `R-C` or `R-D`.

### 3.4 Gate ordering — does any observation or write precede its authority gate?

Traced per combination, recording each gate evaluation, the observation and the
write as ordered events.

```text
observations preceding any of W0(a),(b),(c1),(c2),(d), W1 or W3        0
writes preceding any of the above plus W5(i)(ii)(iii), W6 L1, W6 L2    0
```

**No observation and no write precedes its authority gate on any of the 110592
combinations.** In particular the `W0` (d) prior-write read is of the PCS's own
table, takes no primitive and reads no `/proc`, and it is pinned before `W4` on
every route that reaches `W4`.

### 3.5 The named results

| Question | Measured result |
|---|---|
| **WATCHDOG role** | 36864 combinations. Routes: `R-A0` 34560, `R-A1` 2304. **Zero observations, zero writes, no other route.** Where the handle exists and the generation is valid, the route is `R-A0` when `h.state != SPAWNED` and `R-A1` otherwise, matching `P-10`'s watchdog fixture and `§P1-15` (6B)(iv) with **0 deviations** across every state, ownership, outcome and available observation. |
| **prior-write true** | `outcome == STOPPED` ∧ `WROTE` → `R-D`, 576 combinations. No observation taken, no second write, `pgid_is_leader := 1` derived only from the recorded fact. Reissue after a successful write: `R-A0` if `h.state` moved out of `SPAWNED`, `R-D` otherwise — both confirmed, no third answer. |
| **non-NULL at L** | `(i)(ii)(iii)(L1)` hold ∧ `(L2)` fails → `R-G`, 6 combinations. Observation taken, **no write**, `SC-8` structural violation, `§P1-10.2`'s single continuation. Unreachable on every conforming route by (s1)..(s4); retained fail-closed. |
| **invalidation at each boundary** | Before `W0`: `(b)` fails → `R-A0`, no observation, no write. Between `W4` and the write: `(L1)` fails → `R-F`, 12 combinations, observation taken, **no write lands**, field stays NULL, generation routes to `§P1-11.6`. The two boundaries are distinguished by `L` and never collapse into `R-H`. |
| **EINTR / deadline** | `retried then resolved` produces the same route as a clean read of the same result on all 110592 combinations. Deadline exhaustion arrives as `ERROR` **inside** the one observation and takes `R-E`'s `ERROR` sub-row; it is not a route. Combinations whose route depends on the EINTR dimension: **0**. Second observations produced by retry: **0**. |
| **reissue after success** | 144 reissue pairs driven with the post-state of a writing evaluation as the pre-state of the next, over every second-evaluation outcome and KG-1 class. Pairs producing a second write: **0**. Pairs producing an off-fixture answer: **0**. |

### 3.6 `R-E`'s sub-row partition

All seven distinct results are reached and each `R-E` state selects exactly one:
`PRESENT_VALID`/identity matches/`pgrp != h.pid`; `PRESENT_VALID`/identity
mismatches; `ABSENT`; `UNREADABLE`; `UNPARSABLE`; `ERROR`; `PRIMITIVE_FAULT`.
The eighth row — wrong-shaped primitive return or non-`OSError`
`BaseException` — is stated to arrive **as** `PRIMITIVE_FAULT` and correctly
shares its result rather than forming a ninth class. No `R-E` state is
uncovered and none is double-valued.

---

## §4. The two regression questions

### 4.1 `PHASE 3` reduction (`SC-9` `P3` `STEP 3A`/`3B`/`3C`)

Modelled and driven over every permutation of each fixture.

- All five terminal-bearing predicates reduce as enumerated: `(p1)` → `T1`,
  `(p2)` → `T3`, `(p3)` → `T1`, `(p4)` → `T3`, `(p5)` → `T3` with
  `KV_FORBIDDEN_TARGET` against the entry of least `handle_id` and no other.
- **The multi-fault fixture is correct in both directions.** Own-group
  observation `ABSENT` together with a `SPAWNING_GROUP.json` read that raises
  `SC-8` answers `T1`, and so does its mirror. `STEP 3A` collects both fallible
  sources before `STEP 3B` selects, so structural violation dominates forbidden
  target inside the phase. This is the state v1.14 would have answered `T3` for.
- The fixed source order `(a)` then `(c)` is a property of the clause, not of
  any table, so the site is invariant under every table permutation.
- `STEP 3C` reaches the table scan only when `G` exists, scans every
  current-generation entry regardless of role, ownership and state, and selects
  no terminal while it runs.
- CE-1 masking counterexample: `T3` / `KV_FORBIDDEN_TARGET` /
  `FREEZE_NOT_ATTEMPTED`, **zero signals**, including none to the valid
  handle's group. Confirmed with the protected entry as the only entry, at
  every position among five (120 permutations), and across the full
  role × state × ownership sweep (36 fixtures) — one answer throughout.

**No regression.** Every previously confirmed classifier answer is reproduced,
and the only behaviour that changed is the pair of states v1.14 answered wrongly
(`(p1)` routed to `T3`, `(p4)` left with no named terminal).

### 4.2 Stable-handle tie-break (least `handle_id`)

- Three prospective candidates all `PRIMITIVE_FAULT`, all six permutations:
  `T1`, token `NONE`, **site = the same entry — the one of least `handle_id` —
  in all six**. The same fixture with all three fresh-protected: `T3`,
  `KV_FORBIDDEN_TARGET` against the same single entry in all six. This is the
  positional defect logged as `X-L9`, and it is closed rather than re-argued.
- `SC-10`'s same-phase pair matrix, all seven rows, both table orders: one
  answer per row, terminal, qualifier, per-entry token **and recorded site**
  identical across orders. The exact `Y-M1` table answers `T1` / site `a` /
  zero signals in order `[a,b]` and in order `[b,a]` alike.
- CE-2 in both its group and identity forms: same zero-signal `T3`, the clean
  candidate's `KV_OK` discarded, **no ownership set to `CONTRADICTED`**.
- CE-3 (i),(ii),(iii): `T1`, `T1`, `T2` respectively — phase precedence still
  dominates the within-phase rule.
- `PHASE 6`'s re-verification reduces a same-phase collision identically to
  `PHASE 4`, differing only in the qualifier.

**No regression, and no permutation-dependent authority anywhere.** Across every
fixture and every permutation driven, the number of distinct answers was 1.

`X-L8` self-collision: the machine confirms **0** watchdog combinations reach
the write across all 110592, so `STEP 3A` source (b)'s second clause is provably
vacuous, exactly as the composite claims. The watchdog-pid clause still
populates `G` unconditionally and correctly protects a child that records a
watchdog pid.

---

## §5. Findings by severity

### Major — none

No uncovered route, no double-valued route, no second write, no
unknown-provenance write, no non-`R-H` write, and no permutation-dependent
authority was found.

### Minor X15-M1 — `(x4)`'s two clauses disagree, and the closure's published counts follow the clause that `(x4)` itself excludes

`P-10` `(x4)` reads: *"The three EINTR values must not change the route for any
combination; `retried through the deadline` must change only the KG-1 result to
ERROR inside W4."* Clause 2, read as a forcing rule that rewrites the KG-1
dimension, contradicts clause 1 on exactly **8** of the 110592 combinations —
those with `eintr = retried through the deadline`, `KG-1 = PRESENT_VALID`,
identity matching and `pgrp == h.pid`.

Measured both ways:

```text
                       R-E   R-F  R-G  R-H   writes   obs
this review (clause 1) 552    12    6    6        6   576
forcing (clause 2)     560     8    4    4        4   576
authored closure       560     8    4    4        4   576
```

The authored closure's numbers are the forcing reading; I reproduce them
exactly. The closure also reports `(x4)` as *"EINTR route changes **outside the
R-E relabelling** 0"* — a weakened criterion. `(x4)` clause 1 as written admits
no such exemption, and under the forcing reading 8 combinations change route
across the EINTR dimension, so the composite's own `(x4)` clause 1 is not
satisfied by the closure's enumeration.

Two further clauses of the composite settle the reading against forcing:
`P-10`'s preamble — *"NO COMBINATION IS EXCLUDED IN ADVANCE, AND A COMBINATION
WHOSE LATER DIMENSIONS THE MACHINE NEVER CONSULTS IS REQUIRED TO PRODUCE THE
SAME ANSWER FOR EVERY VALUE OF THEM"* — and `(x2)`, which fixes the write count
as *"the number whose full conjunction holds"*; the `W7` conjunction does not
name EINTR, so that number is 6, not 4. The counter-textual pull is `W4`'s own
sentence that deadline expiry makes the observation's result `ERROR`, which is
what makes clause 2 readable as forcing. The 8 affected tuples are physically
unrealizable — they assert both that the observation timed out and that it
returned `PRESENT_VALID` — which is why the composite is safe either way.

**Why Minor, not Major.** I ran the full check under both readings. Both give
zero combinations with no route, zero with two, and zero `MACHINE`/`PREDICATES`
disagreements; under both, the only writing route is `R-H`, no write has unknown
provenance, and no answer is permutation-dependent. The ambiguity moves 8
self-contradictory enumeration tuples between `R-E` and `R-F`/`R-G`/`R-H` and
changes no real state, no route, no write site and no authority gate. It does
not fail `§P1-15` (6B)(vi), whose required result is the zero/zero criterion,
which both readings meet.

**Recommended before any `OR` step:** reconcile `(x4)`'s two clauses — either
restate clause 2 as a realizability remark about which tuples can arise, or
exclude the 8 tuples explicitly and drop the "no combination is excluded in
advance" sentence. As it stands, two conforming builds will publish different
route counts and different write counts and both will claim `(x1)`.

### Minor X15-M2 — `W1`'s sentence order would route 576 watchdog combinations to `R-B`

`W1` states the `R-B` sentence before the `R-A1` sentence. Read as strict step
order, a `WATCHDOG` handle that is `SPAWNED` in a valid generation and whose
`W1` cannot determine an outcome takes `R-B` rather than `R-A1` — **576**
combinations. The two routes differ substantively: `R-A1` returns the operation
normally and is `H-NULL-GROUP` permanently, `R-B` completes with no success
status and leaves the recorded-group state unchanged.

The composite settles this to `R-A1` three times over: `P-9`'s row order with
its prefix-exclusion rule places `R-A1` before `R-B`; `R-B`'s own guard says
*"W0 admits"*, and `W0`'s admissibility includes `(c2)`; and both `P-10`'s
watchdog fixture (*"with any outcome"*) and `§P1-15` (6B)(iv) (*"every
outcome"*) require `R-A1`. `R-A1`'s own sentence also presupposes an outcome
`W1` determined, which does not hold in this state. Both my implementations
select `R-A1` and agree. Recorded as Minor because the resolution is normative
and redundant, and the only defect is `W1`'s prose order.

**Recommended:** add *"and `(c2)` held at `W0`"* to `R-B`'s guard, or swap the
two sentences in `W1`.

### Observation X15-O1 — commit

Working tree at `8d7d14a`, instructed `60d92db`. `60d92db` is an ancestor and
the diff is confined to the two confirmation prompts; all six pinned files are
byte-identical at both commits. Not a mismatch.

### Observation X15-O2 — `P-9`'s rows are not disjoint as free-standing booleans

Read without `P-9`'s construction rule, the nine own-guards overlap on **80760**
of 110592 combinations (largest classes: `R-A0`+`R-C` 49680, `R-A0`+`R-E` 12420,
`R-A0`+`R-D` 12420). This is not a defect — `P-9` states the prefix-exclusion
rule explicitly and the rows are disjoint by construction under it — but an
implementer who transcribes the GUARD column into nine independent booleans and
omits the rule gets a table that describes most states more than once. Worth a
sentence in the handoff, since `§P1-15` (6B) fails a build in which any state is
described by two routes.

### Observation X15-O3 — `R-D`'s derivation is total

`R-D` derives `pgid_is_leader := 1` from the recorded fact alone, with no
observation and no comparison. This is sound only because `R-H` is the sole
write and assigns exactly `h.pid`. I confirmed across all 110592 combinations
that `R-H` is the only writing route and that its assigned value is `h.pid`
unconditionally, so the derivation cannot be reached with any other recorded
integer. Noted because the property is load-bearing and is established by `P-3`
and `P-5` rather than by anything local to `R-D`.

---

## §6. This file

```text
path    reviews/fable_officina_p1_wb_v2_15_final_x_confirmation.md
sha256  recomputed by the reader over the committed bytes
```

This file contains none of its own digests, so custody stays acyclic.

---

## §7. Next boundary

The next boundary is **Kirill's consideration of amendment `v1.12`**, and
nothing else. This confirmation is the X line's input to that consideration.

- `T = NOT_ACTIVATED`
- programme claim = `OPEN`
- `WATCHDOG AUTHORITY AMENDMENT V1.12 = NOT ACCEPTED`
- W-B remains signed and is not reopened

No scaffold, code, key, `OR` step, install or activation is authorized by this
confirmation. The two Minors are recommended for repair before any `OR` step;
neither blocks the author acceptance this verdict confirms.
