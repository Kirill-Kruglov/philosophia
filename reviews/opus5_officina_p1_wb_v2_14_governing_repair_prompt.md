# Officina P1 W-B v2.14 — final governing repair after divergent v2.13 review

You are Claude Code Opus 5, authoring a bounded governing repair in
`/home/master/llm_projects/philosophia` at commit `12898e7`.

This is not a design round. Signed W-B is fixed. The v2.13 X/Y reviews diverged:
Fable confirmed, but Sol supplied four executable Major counterexamples. The
Majors govern because they reproduce directly from the governing bytes. Repair
them mechanically; preserve every unrelated signed choice and negative boundary.

Do not edit historical inputs, code, tests, signatures, runtime artifacts,
activation state, or unrelated dirty work. Do not commit. Create exactly the six
deliverables named below. No implementation, key, entropy, OR execution, install
or activation is authorized. `T = NOT_ACTIVATED`; programme claim = `OPEN`.

## Pinned inputs

Recompute all hashes before work. A mismatch is `BLOCKED`.

```text
d50f378ca419f891e79356315d59115b6ec06c38474e812fa01ccb847b15f200  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_13_CORRECTION.md
2999e2129de19ff38dee12071453c7156a5432efaf299bc69e79dc7e7b04ac53  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_10_DRAFT.md
15e11f0e4c10fe8b85607dc383520d5b009712603084e82a8756211615bd8fb3  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_13.md
10207f833a00b0e7e5106ca8a781916f3414d995ab05161fb734078b5ffaef93  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V4_DRAFT.md
080000c478c933bedd91124983c4c9e44cc4b850e52eba17b7628304274cbef9  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V4_DRAFT.md
8245b0f960fa4a349667a0c75213cbe0e39cf83ab4a914be94146d56f93626fd  reviews/opus5_officina_p1_wb_v2_13_closure_repair.md
89e210430b617d88a67229df2beeff82c5c844f6de1da1d03b376b758d7cb0c2  reviews/fable_officina_p1_wb_v2_13_final_x_review.md
a4056f477bd631ca7b1b19292371de7afade367ecbfd2b1b090a1f95f79b4036  reviews/sol_officina_p1_wb_v2_13_final_y_review.md
```

Treat both reviews as evidence, not authority. Independently reproduce each
finding. The closure must disposition every item one-to-one.

## Mandatory repairs

### R1 — make every terminal-bearing phase a total reduction

Sol Y-M1 is valid. Phase 4 currently allows table-order-dependent `T1` from
`PRIMITIVE_FAULT` and `T3` from fresh protected membership.

Replace immediate per-entry terminal selection with a closed phase-local scan
and reduction. Pin, in normative bytes:

- the exact set of per-entry observations collected before reduction;
- no signal, ownership mutation or candidate use during that scan;
- the total intra-phase precedence, with structural violation dominating
  forbidden target when both occur in the same phase;
- deterministic terminal, qualifier and per-entry token for every collision;
- permutation invariance over table and fault order;
- discard of all candidates on either terminal;
- the equivalent explicit reduction for every other terminal-bearing phase,
  including Phase 6, or an exhaustive proof that no same-phase collision exists.

Add the exact Y counterexample in both table orders and the full same-phase pair
matrix to the governing conformance rows. Narrow the fresh-observation
cross-product prose to Phase 4's actual prospective domain; retain separate
recorded-form coverage across the full structurally valid table.

### R2 — make KG-2 population single-valued

Sol Y-M2 is valid. Reconcile P-2 and P-10 explicitly:

- group population is attempted only for an `AWAIT_STOP` result whose final
  `outcome == STOPPED`;
- only that path performs the one canonical `PGRP_OBSERVE` and may write;
- `TIMEOUT`, `EXITED`, interruption/deadline failure and retry routes perform no
  population observation and no write, return/retain the named NULL state and
  set any response operand consistently without pretending it was observed;
- retain single writer, at-most-once write, identity equality and `pgrp == pid`;
- pin step ordering so no implementation can observe/write before learning that
  the result is STOPPED.

Update P-2/P-9/P-10, route tables and conformance fixtures together. Include the
ordinary live-leader TIMEOUT counterexample and prove it has one result.

### R3 — repair all current-member literals and recount the generation

Sol Y-M3 is valid. Composite rows 105 and 106 still say 81. Row 105 must use the
current member cardinality; row 106's coherent-rollback fixture must explicitly
use the current generation and its full current member set unless it binds a
complete historical byte generation. Prefer the current-generation repair.

This generation adds as historical M2 inputs at least amendment v1.10,
composite v1.13, and the two v2.13 final reviews. Recompute, never copy, every
member/provenance/accounting value and dependent literal. The expected starting
arithmetic is `MS-2 71 -> 75`, total members `85 -> 89`, provenance `79 -> 83`,
but measured bytes govern. Recalculate every index, prose number, row 103..115,
install schema, rollback fixture, `N-16`, `G-11`, overlap/disjointness value,
maintenance matrix and content hash. Search all retired cardinals and classify
every surviving occurrence.

### R4 — close the primitive surface, not merely the prose

Sol Y-M4 governs over Fable's non-blocking Q8 classification. Mandatory c10,
c14 and m3 require both `getsid` and `getpgid`; no conforming implementation can
currently supply them.

Add exact local bindings `_getsid` and `_getpgid` from `os` to the closed
primitive surface and every corresponding identity, import, attribute, call,
allowlist and verifier rule. Keep all later calls through the bound local names.
Pin argument/result/error semantics for pid 0 and positive pids, and route
unexpected results/faults fail-closed. Do not weaken S-3/S-5/S-6/S-7.

Regenerate all affected reachable-closure rows, canonical bytes, digests,
counts, test fixtures, binding spans, resolved-output identity and handoff
surfaces. Explicitly cover c10, c14 and m3. The v2.13 `L-X6` exception is
withdrawn only after the bytes prove the complete surface is reachable.

## Required non-Major cleanup

Disposition all Fable X-L1..X-L7 and Sol Y-L1 rather than dropping them:

1. Remove the dead/circular L1 `0x29` rationale, place the last-`)` guarantee at
   L0, and reattribute V18 to the rule that actually refuses it while preserving
   its published refusal result.
2. Withdraw the false claim that the role-WATCHDOG exclusion is required because
   every conforming watchdog is a group leader. Describe it as conservative and
   redundant under the normal `setsid=False` lifecycle; keep its no-signal rule.
3. Correct the S7 delete-literal transcription so the written literal itself,
   not only its digest, reproduces.
4. Make MP-1 byte-exact: pin a unique insertion anchor/order/newline convention,
   recompute its digest and length, and require both behaviour and bytes. Do not
   retain a known false digest as informative.
5. Expand the old `L-X6` narrative to c10/c14/m3 and both operations, then mark it
   repaired only through R4.
6. Present four exclusions as four rows or state explicitly that one row carries
   two exclusions.
7. Reconcile the dependent-literal list involving row 106 with what actually
   changed in this generation.
8. Narrow the fresh protected cross-product to the prospective set and state
   separately what full-table recorded-protection coverage proves.

## Complete resolved-output and quarantine obligation

Because R1-R4 change governing bytes, v2.13's eleven spans and full-output hash
are retired. Publish a complete new transform, not a delta on an invisible
intermediate:

- every source/replacement span with exact bytes, length and SHA-256;
- deterministic non-overlapping splice order;
- expected complete output length and SHA-256;
- all delimited-region hashes and byte-identity checks;
- byte-unchanged guarddata, or a loud scoped reason and renewed review if that is
  impossible;
- corrected MP-1 fixture;
- primary full-output quarantine plus honestly narrow literal defense.

Independently construct the resolved bytes in memory, verify every figure, then
discard them. Do not create a resolved production file or execute OR-4.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_14_CORRECTION.md`
2. `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11_DRAFT.md`
3. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_14.md`
4. `successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V5_DRAFT.md`
5. `successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V5_DRAFT.md`
6. `reviews/opus5_officina_p1_wb_v2_14_governing_repair_closure.md`

The new amendment wholly replaces v1.10; the new composite wholly replaces
v1.13. Retire the v1.10 acceptance token. The only possible future token is:

```text
I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11
```

It is not signable from this authorship round.

## Closure requirements

The closure must contain:

- verdict `READY_FOR_OFFICINA_P1_WB_V2_14_FINAL_XY_REVIEW`,
  `REVISE_OFFICINA_P1_WB_V2_14`, or `BLOCKED_OFFICINA_P1_WB_V2_14`;
- recomputed input/output hashes and byte lengths;
- one-to-one disposition of Sol Y-M1..Y-M4/Y-L1 and Fable X-L1..X-L7;
- executable counterexample tables before/after R1 and R2;
- exact primitive-surface diff and proof for c10/c14/m3;
- measured generation accounting and stale-cardinal sweep;
- full transform reproduction and MP-1 reproduction;
- confirmation that identity Option A and its unaccepted bounded weakening remain
  untouched and that XS-1 remains blocked;
- confirmation that no scaffold/code/test/key/artifact/OR step/install/activation
  was created or authorized;
- exactly two bounded final-review questions for independent Fable X and two for
  independent Sol Y, focused on executable correctness rather than prose style.

Only after both independent lines confirm the same v2.14 bytes may Kirill
consider the v1.11 token. Even later acceptance authorizes no implementation.
Do not predict science or move the programme claim.
