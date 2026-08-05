# Officina P1 W-B v2.12 executable KV and transformation repair

You are Claude Code Opus 5, governing-pair repair author. Work in:

`/home/master/llm_projects/philosophia`

Base commit: `d4d683a` (`Review W-B governing pair v2.11`). Do not modify
historical inputs, code, tests, untracked work, signatures, runtime artifacts or
prior reviews. Do not commit.

W-B remains signed and is not reopened. `OR-2` alone is complete;
`OR-3..OR-11` remain unauthorized.

## Inputs

```text
71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md
d7ccf170b759f89519f24b26bd817d273197dddd0b5208e0d95eecebf59ec91d  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V2_DRAFT.md
a70f6a7774386d7b36084b0e19c5f1e78b11a5e04f2d992d95d93148878c5c6b  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V2_DRAFT.md
3964469740fc73a6a4836b64247003c39d5261a6af9c6ddf37a0da76c13f0759  reviews/fable_officina_p1_wb_v2_11_final_x_review.md
ef4508be13d9ef395b2e8d5542d6256e2bd5719e99cbff209d13612dc5dd00c4  reviews/sol_officina_p1_wb_v2_11_final_y_review.md
```

Sol returned `REVISE_OFFICINA_P1_WB_V2_11` with three executable Majors. Fable
confirmed the pair but supplied additional maintenance findings. The stricter
executable counterexamples govern. Repair only R1-R5.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_12_CORRECTION.md`
2. `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9_DRAFT.md`
3. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_12.md`
4. `successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V3_DRAFT.md`
5. `successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V3_DRAFT.md`
6. `reviews/opus5_officina_p1_wb_v2_12_governing_repair_closure.md`

## R1 - forbidden-target dominance before any signal

Repair Sol M-1. The classifier must use two explicit phases and must send no
signal until both phases complete successfully.

### Phase P0: global protected-group pre-pass

Before candidate filtering, scope construction, sorting or signalling:

- scan every current-generation handle-table entry, regardless of role,
  ownership or state;
- if any non-null recorded group equals the PCS group, a watchdog leader group
  or the recorded supervisor group, terminate the whole classifier with
  `KV_FORBIDDEN_TARGET` / `FREEZE_NOT_ATTEMPTED`;
- stale-generation entries retain their already-governing structural terminal;
- malformed/null values take their exact closed branch and never grant scope;
- no earlier KV skip may mask this pre-pass.

### Phase P1: verify the complete prospective scope

- evaluate every otherwise eligible candidate through fresh KG/KV checks;
- collect all results before sending any signal;
- a freshly observed protected group terminates the entire classifier, even if
  found after other valid candidates;
- only after the full table has been scanned with no dominant terminal may the
  verified distinct groups be sorted and acted upon;
- re-run the per-handle verification immediately before each individual signal,
  with any protected result terminating all remaining actions.

Pin dominance over every skip/error token. Include the exact Y counterexample:
a current-generation `CONTROLLER/RUNNING/CONTRADICTED` entry whose recorded group
is the supervisor group plus a valid controller. Required outcome: whole
classifier terminates and **zero signals** are sent.

Add permutation tests proving a protected entry yields the same zero-signal
terminal at every table position.

## R2 - executable Linux stat grammar and honest KG-2

Repair Sol M-2.

### KG-1

Using the already-read `/proc/<pid>/stat` buffer:

- locate the final `)` under the current bound parser rule;
- token 1 after it is exactly one permitted ASCII Linux process-state character,
  not an integer;
- token 2 is `ppid`, a base-10 integer under the exact existing numeric grammar;
- token 3 is `pgrp`, a base-10 integer under that grammar;
- reject missing/extra malformed token forms, overflow, signs/whitespace not
  admitted by the current grammar, impossible state character, read/parse/error
  states with a closed token;
- return `PRESENT_VALID` only after all required fields parse.

State the exact closed permitted state-character set and its current-kernel
provenance. If the current governing observer already defines a broader exact
state grammar, use that same grammar and cite it; do not invent a permissive
catch-all.

### KG-2

Stop calling new rules derived when they are new normative content. State
explicitly that v2.12 supplies the missing governing rules licensed by R2:

- initial value of `pgid_or_null` for every handle role;
- exact legitimate population point after successful process creation and
  kernel verification;
- exactly one writer/site per eligible handle;
- watchdog and non-group-leader behavior;
- immutability after the write;
- contradiction behavior on later mismatch;
- total coverage of every creation/failure path.

Provide a source table separating `EXISTING CURRENT CLAUSE` from
`NEW NORMATIVE SUPPORTING RULE IN v2.12`. Do not open or copy the superseded v2
packet for behavior. No `_getpgid` binding or import expansion is permitted.

## R3 - byte-identifiable Cell-2 transformation and PO-9

Repair Sol M-3.

### Exact replacement bytes

Replace binding v2's overlapping semantic line actions with one canonical
literal byte block for the complete post-selection Cell-2 preamble. Pin:

- exact UTF-8 bytes in a fenced literal whose extraction rules exclude fence
  markup;
- canonical byte length and SHA-256;
- exact source span/sentinels replaced as one unit;
- exact post-selection W-B text, with W-A rejected and no stale “open”,
  “unsigned”, “selects neither” or “replacement for v1.2” assertion;
- all common retained facts needed outside the replacement;
- deterministic splice algorithm with no overlapping ranges or prose choice.

Two implementations given the same source bytes must emit byte-identical
in-memory output.

### Literal D1/D2 detector tables

Enumerate the complete normalized literal arrays consumed by PO-9 D1 and D2,
including exact normalization and boundary matching. Pin canonical serialization,
length and hash of each array. Provide positive and negative vectors for every
literal and every class-R allowed occurrence. No “derived from”, semantic
category, substring intuition or implementer-chosen phrase boundary remains.

Retain exactly:

- both option tokens and paired amendment tokens in TS-1;
- the CK-14 mismatch fixture vocabulary;
- guarddata bytes;
- legitimate supervisor/PCS socket language;
- watchdog slot-6 only in closed/absent W-B sense.

Remove only operative W-A grant/request behavior and discharged Cell-2 open
state. Demonstrate no false positive against all retained classes and no false
negative for every forbidden vector.

## R4 - generational accounting and maintenance sweep

v2.12 is another real replacement generation. Add exactly four new M2 rows:

1. amendment v1.8;
2. composite v1.11;
3. Fable v2.11 final X review;
4. Sol v2.11 final Y review.

Update atomically:

```text
MS-2: 63 -> 67
MS-8 / install member_count: 77 -> 81
composite provenance rows: 71 -> 75
```

Update all dependent schemas, B7/B17, CK/member fixtures, counts, hashes and
install-id examples. Seven member classes remain.

Because the pair is already regenerating, also repair every logged item:

- H-4 owner `CK-12` -> `CK-7` for `HISTORICAL_BYTE_MOVED`;
- amendment N-16 stale 69 -> current 81;
- region labels use actual UTF-8 byte lengths, not character counts;
- remove stale “finished replacement for v1.2”;
- row 106: restore a consistent fixture-group count and define every named
  group; prefer ten `(a)..(j)` unless an actual eleventh fixture is fully given;
- correct closure-derived counts of historical/negated `CK-1..CK-12` mentions;
- remove overlapping Cell-2 spans through the single replacement block;
- fix the declared file count so chat provenance is not confused with the six
  authored deliverables.

Advance all packet/amendment/composite paths, anchor tokens and consumers to
v2.12/v1.9/v1.12 consistently. Recompute every region/joint/file hash.

## R5 - binding, scaffold and acceptance state

Regenerate binding v3 and handoff v3 around the exact transformation and
detectors above. Handoff remains inert oracle/declarative scaffolding only:

- no runtime EOF/classifier/process-control implementation;
- no production-root, MS-5/MS-6, test-row or shared-runtime edit;
- no identity-observation code; not the XS-1 combined binding;
- existing dirty/untracked `generic_harness.py` remains non-evidence and
  untouched;
- no real process-control smoke.

Version-bump the future acceptance token:

```text
I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9
```

Even future acceptance authorizes no code, test, key, OR-3/OR-4, install or
activation. Separate inactive-scaffold authorization and later runtime/atomic
authorizations remain required.

## Preserve

Do not reopen/change signed W-B, the 89-row closure, project-import surface,
CK-13/25 codes/B14/IR-13 boundary, rollback residuals, identity Option A or its
unaccepted weakening, scientific contracts, T envelope or programme claim.

Create no code, test, key, artifact, OR step, process operation, install or
activation. `T=NOT_ACTIVATED`; programme claim `OPEN`.

## Closure

Emit exactly one:

- `READY_FOR_OFFICINA_P1_WB_V2_12_FINAL_XY_REVIEW`
- `REVISE_OFFICINA_P1_WB_V2_12`
- `BLOCKED_OFFICINA_P1_WB_V2_12`

The closure must:

1. disposition Sol M-1..M-3 and every X/Y log item;
2. show the two-phase forbidden-target proof and permutation fixtures;
3. give executable KG-1 grammar and honest KG-2 provenance/new-rule table;
4. publish exact Cell-2 replacement bytes and literal PO-9 arrays with hashes;
5. prove 67/81/75 accounting and maintenance sweep;
6. show scaffold/identity/acceptance negative boundaries;
7. ask only bounded final X/Y questions on executable totality and byte
   identifiability.

In chat report verdict, output paths/hashes, M-1/M-2/M-3 repairs, accounting,
maintenance sweep, negative space and exact next boundary.
