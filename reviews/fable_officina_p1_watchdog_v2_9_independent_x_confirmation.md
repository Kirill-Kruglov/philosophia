# Officina P1 watchdog-freeze v2.9 — independent X-line confirmation

**Reviewer:** Claude Code, model `claude-opus-4-8`, fresh session, independent X
line. Did not author v2.3 through v2.9. The Opus 5 v2.9 closure
(`reviews/opus5_officina_p1_watchdog_freeze_choice_v2_9_closure.md`) was treated
as an untrusted self-assessment and relied on for nothing; every claim below was
recomputed.

**Reviewed commit:** `1731811` ("Consolidate watchdog authority contract in
v2.9"). HEAD is `1c6bc56`; all recomputation was performed against the committed
blobs at `1731811`, which are byte-identical on disk for the three governing
files. No governing, historical, code, test, signature or runtime file was
modified; nothing was committed. Exactly this one review file was created.

**Pinned build match:** the review host interpreter is byte-identical to the
audited build — `Python 3.12.3 (main, Jun 19 2026, 12:46:00) [GCC 13.3.0]`,
`x86_64` Linux — so `reachable_closure` residency was reconstructed on the exact
interpreter. All interpreter derivations ran under `env -i python3 -I -S -E -P`
(empty environment, the §P1-7.1 launch vector) and imported **no** Philosophia
production module. The four project dependencies were audited by AST parse of
their source only — never imported, executed or compiled.

---

## VERDICT

```text
REVISE_OFFICINA_P1_WATCHDOG_V2_9
```

**One blocking-class finding, and it does not touch the frozen closure value or
any authority boundary.** Everything the v2.8 X line demanded is repaired: the
unexecuted-branch inventory is now correct at seven, MS-11.1 is carried forward
byte-for-byte and recomputes to length `20534` and digest `aa974e0c…dc20ee`, and
MS-13 factually binds the four project modules the role import executes. The
89-row closure, its kinds, its 267 booleans, the joint block, the seven-name
stdlib-seed union and the negative-authorization space are all confirmed.

The defect is a **stale generation token in an operative validation clause,
present in both governing files, and it is an incomplete re-scope of the very
anchor v2.9 claims to have re-scoped.** `TS-2B A16(d)` — the
pre-selection-composite **anchor extraction rule**, stated "extracted by this
exact rule and no other" — still binds the retired token
`P1_WATCHDOG_V2_8_PRE_SELECTION_COMPOSITE_SHA256`, at amendment line 2838 and
composite line 4689. But the only §A0.4 anchor line, and §A0.4's own description
of `A16(d)`, use `P1_WATCHDOG_V2_9_…`. As literally written, `A16(d)` splits the
M1 amendment on `0x0A`, finds **zero** lines matching the V2_8 grammar,
and fails `STAGE_A_PRESELECTION_MISMATCH` — the pre-selection composite anchor
is not extractable by its own governing rule. This is a **Major
identifiability/consistency defect in the governing bytes**, which is
REVISE-eligible under the round's gate. It fails **closed** (over-refusal, never
fail-open, no authority weakening, no improper acceptance), so it is Major and
not Critical.

The three literal §A0.4 sub-claims of question 1 are nonetheless all true (one
V2_9 anchor line, value equal to the composite `H_FILE`, zero retired-token
*anchor lines*); the defect is in the **consumer** of that anchor, which
question 1 also asks me to assess.

Had this been `CONFIRMED`, it would have authorized only Kirill's watchdog option
choice and no key, artifact, implementation, test, install, activation or
science. `T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`; the
watchdog cell remains `NOT SELECTED`.

---

## Hashes verified at `1731811`

| File | Claimed SHA-256 | Recomputed |
|---|---|---|
| `…AUTHOR_CHOICE_PACKET_V2_9_CORRECTION.md` | `22f2e3dc…4efb6c66` | **match** |
| `…WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_6_DRAFT.md` | `d5e1d4db…d88640f` | **match** |
| `…P1_OPERATIVE_COMPOSITE_V1_9.md` | `3ce26ba6…68e4c1ad` | **match** |
| `reviews/opus5_…_v2_9_closure.md` | `991c7389…15e3d0fab` | **match** |
| `reviews/fable_…_v2_8_independent_x_confirmation.md` (prior X) | `ddd6d63a…95d8e8e9` | **match** |

Four project dependencies (MS-13), recomputed from committed blobs:

| Path | Recomputed SHA-256 | MS-13 |
|---|---|---|
| `src/philosophia/__init__.py` | `96833596…785ddf684` | **match** |
| `src/philosophia/officina/__init__.py` | `2bb45ebf…73ca831e1f` | **match** |
| `src/philosophia/officina/canonical.py` | `a95cad3e…17978a54` | **match** |
| `src/philosophia/officina/interlock.py` | `8b464f52…1159d24ecc8` | **match** |

No file contains its own digest: the composite `H_FILE` `3ce26ba6…` occurs
**once** in the amendment (the §A0.4 anchor line) and **zero** times in the
composite; the amendment's own digest `d5e1d4db…` occurs zero times in the
amendment.

---

## The eight answers

### 1 — outputs, joint block, §A0.4 anchor — **YES on all three literal sub-claims; but the anchor's extraction rule is broken (see finding B-1)**

- The three governing outputs recompute to the pinned hashes exactly (table
  above).
- The **joint install-and-authorization block is byte-identical** in the
  amendment (§A10, lines 1167–3792) and the composite (§P1-14.4, lines
  3018–5643): 2626 lines each, SHA-256
  `d89995ea70f02a2245f49ebd442fb3857bfea44daa635fa25967ac6ca2b47fec`, equal to
  the closure's claim.
- The **§A0.4 anchor occurs exactly once** (amendment line 268), generation-
  scoped to `P1_WATCHDOG_V2_9_…`, value
  `3ce26ba63ca1546ddd7c8422ccf5a4e71e05678e58d1f3deca18e24668e4c1ad` = the
  composite `H_FILE`. **Zero lines match the retired V2_8 anchor grammar**
  (`P1_WATCHDOG_V2_8_… = <64 hex>`) in either file.

All three literal sub-claims hold. **However**, question 1 asks me to assess the
anchor, and the operative rule that extracts it is stale — see **B-1** below.
This is the blocking finding.

### 2 — MS-11.1 bit-for-bit and recomputes — **YES**

- The MS-11.1 table (rows 1–89) is **byte-identical** between composite v1.8
  (`8f0f5b8`) and v1.9 (`1731811`): both 188 lines, SHA-256
  `8c97e086775f117e24931e84f95858679fdd25be81e5fb549ffa4967f4e301a7`. The value
  the independent v2.8 X line confirmed is carried forward untouched.
- Parsing the literal table and building the canonical value per MS-0
  (`sort_keys`, `(",",":")`, pure-ASCII, single trailing `0x0A`, array sorted by
  `module`) reproduces: **89 rows**; kinds **BUILTIN 29 / FROZEN 13 / EXTENSION 2
  / PURE_PYTHON 45**; **76** distinct transitive-import names, each a row; **39**
  empty arrays; **267 booleans all `false`**; **canonical length 20534**; SHA-256
  **`aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee`**.
- Factual independence on the pinned interpreter: importing the eighteen-name
  union of the three scoped allowlists and normalizing (drop `__main__`; two
  pseudo-modules `typing.io`/`typing.re`; three alias keys `os.path`→`posixpath`,
  `importlib._bootstrap`→`_frozen_importlib`,
  `importlib._bootstrap_external`→`_frozen_importlib_external`, keyed by
  `__spec__.name` so `_collections_abc` correctly survives) yields **exactly 89**
  resident modules whose **names are identical** to the literal and whose
  **kinds match with zero mismatches**.

### 3 — seven unexecuted branches, `datetime → _pydatetime` the sole v2.8 omission — **YES**

MS-11.3 now reads **SEVEN** (composite line 3744) and names the seventh with its
reason. Enumerating module-scope `IMPORT_NAME` targets across the loaded code
objects on the pinned build reproduces exactly the seven branch groups:
`os → nt`; `os → ntpath` (ntpath resident via `pathlib`, but the os edge is the
untaken Windows branch — `os.path is posixpath`); `ntpath → nt, _winapi`;
`_frozen_importlib_external → nt, winreg` (confirmed by fetching the frozen code
object via `_imp.get_frozen_object`; module-scope `IMPORT_NAME` = `_imp _io sys
_warnings marshal nt winreg posix`, with `nt`/`winreg` unexecuted); `abc →
_py_abc`; `hashlib → logging`; `datetime → _pydatetime`. `_datetime` is in
`sys.builtin_module_names`, so `datetime.py`'s `try: from _datetime import *`
succeeds and the `except ImportError` never runs — `_pydatetime` is correctly
absent and `datetime.transitive_imports = [_datetime]` is unchanged. The prior X
table listed the first six as already present at v2.8; `datetime → _pydatetime`
was the sole omission. No row, kind, edge, boolean, length or digest of MS-11.1
is affected.

### 4 — MS-13 factually correct for all four dependencies — **YES** (one prose count is off; log-only, B-2)

Derived by AST parse of source only (no import/execute/compile):

- **Digests**: all four match MS-13 (table above).
- **Import edges / order**: `philosophia` → `project_imports []`;
  `philosophia.officina` → `["philosophia.officina.canonical",
  "philosophia.officina.interlock"]` in that execution order;
  `canonical`/`interlock` → `[]`. `execution_order = [philosophia,
  philosophia.officina, philosophia.officina.canonical,
  philosophia.officina.interlock]`.
- **Seven-name stdlib-seed union**: the union of the four modules' `stdlib_seeds`
  is exactly `{__future__, dataclasses, hashlib, json, os, pathlib, typing}` —
  seven names, each one of the sixteen scoped seeds of `generic_harness.py`. No
  standard-library module enters that MS-11.1 does not already carry.
- **32 effect assertions all `false`**: the only module-scope `Call` among the
  four is `interlock`'s `object()` sentinel; `canonical` has eight function
  definitions (four of which *define* filesystem writers) and **no** module-scope
  call; both initializers have none. None of the eight effects occurs at import
  in any of the four → all 32 assertions are correctly `false`.

### 5 — can any byte state make two conforming implementations return different first codes — **NO**

`VP-4` is a literal, totally ordered check sequence (`CK-1`…`CK-15`, each
prerequisite established by an earlier check), and `IR-13`/`VP-3` assign every
relation **exactly one earliest owner and exactly one code**. The first code any
conforming implementation emits is therefore the code of the earliest failing
check in the fixed order — identical across implementations. I could construct no
multi-fault state that diverges; the twelve decisive multi-fault results all
resolve to one first code (e.g. absent M4 → `CK-7 MEMBER_OMITTED`; invalid-JSON
M4 → `CK-8 MEMBER_SUBSTITUTED`; M4-semantic + Stage-A-binding → `CK-9
STAGE_A_BINDING_MISMATCH`; a project dependency differing from MS-13 → `CK-10
MANIFEST_VALUE_MISMATCH`). The B-1 token defect does **not** create divergence:
both implementations find zero V2_8 anchor lines and both fail
`STAGE_A_PRESELECTION_MISMATCH` — deterministically, if wrongly.

### 6 — is IR-13 exhaustive over its stated sections; any omitted relation — **EXHAUSTIVE: YES within its range; OMISSION FOUND: NO** (label nit, log-only, B-3)

The 47-row `IR-13` covers every record / M4 / M7 / Stage-A / Stage-B /
project-dependency relation between distinct objects (or object-to-literal),
each with exactly one owner and one code, with intra-object constraints
(`A9` pairing, `S1..S8`, `MS-8`/`MS-9`) correctly listed separately at the foot.
I found **no** relation a check can refuse on that the table omits. Note: the
stated derivation range enumerates **fifteen** section labels — MS-4, MS-6,
MS-7, MS-11, MS-12, MS-13, IR-1, IR-2, IR-3, TS-1, TS-2A, TS-2B, TS-3, TS-4,
TS-5 — while the prose (amendment line 2471, and closure §3) calls it "sixteen
sections." This is a descriptive counting mismatch, not a missing relation.

### 7 — do the §7 constants recompute — **YES** (with the label nit of B-3)

Independently confirmed: 89-row closure with length 20534 and digest
`aa974e0c…dc20ee`; 7 unexecuted branches; IR family →13 (IR-13 new); MS family
→14 (MS-13 new); IR-13 = 47 relations; 4 project dependencies with 32 effect
assertions; seven-name stdlib-seed union; install-record members **69** (`M1 2 +
M2 55 + M3 7 + M4 1 + M5 1 + M6 2 + M7 1`); `MEMBER_EXTRA` retired (absent from
the code enumeration); joint block 2626 lines; §A0.4 re-anchored to the V2_9
value. The failure-code family reduction 26→25 is consistent with `MEMBER_EXTRA`
retirement. The "sixteen sections" descriptor is the one non-recomputing label
(B-3).

### 8 — does v2.9 create or authorize any key/artifact/impl/install/activation/claim movement/author cell — **NO**

Commit `1731811` adds five documents only — the composite v1.9, amendment v1.6,
packet v2.9, the closure and a repair chat-response — 11 582 insertions, **0
deletions**, no code, test, key, signature, manifest or install-record file. The
governing bytes preserve `T = NOT_ACTIVATED`, programme claim `OPEN`, watchdog
cell `NOT SELECTED`, process-identity Option A as external author state only, the
bounded-weakening token `NOT ACCEPTED`, and the full negative-authorization
space.

---

## Blocking finding

### B-1 (Major, identifiability/consistency; REVISE-eligible) — `A16(d)` binds the retired V2_8 token in both governing files

**What it is.** The pre-selection-composite anchor was re-scoped from V2_8 to
V2_9 in `§A0.4` (amendment line 255 prose and line 268 anchor line — the
amendment-only region, *before* the joint block). The **consuming rule
`TS-2B A16(d)`**, which lives **inside the joint block** (amendment line 2838,
composite line 4689, byte-identical in both), was **not** re-scoped and still
reads:

> "…consists of the literal token
> `P1_WATCHDOG_V2_8_PRE_SELECTION_COMPOSITE_SHA256` followed by exactly one 0x20,
> one 0x3D, one 0x20, and then exactly 64 characters…"

**Demonstration.** In v1.5 all three loci were consistently `V2_8` (amendment
lines 242, 255, 2411). In v1.6 the re-scope reached `§A0.4` (lines 255, 268 →
V2_9) but not the joint-block `A16(d)` (line 2838 → still V2_8), and likewise the
composite `A16(d)` (line 4689 → still V2_8). §A0.4 itself states `A16(d)` uses
`P1_WATCHDOG_V2_9_…` (line 255), directly contradicting the actual `A16(d)` text.
A conforming implementation of `A16(d)` — "extracted by this exact rule and no
other" — splits the M1 amendment on `0x0A`, matches lines against the **V2_8**
grammar, finds **zero** (the sole anchor line is V2_9), and fails
`STAGE_A_PRESELECTION_MISMATCH` on the anchor-cardinality rule. The
pre-selection composite anchor is therefore **not extractable by its own
governing rule**, defeating the entire purpose of §A0.4.

**Severity.** Major, not Critical: the failure is **fail-closed**
(over-refusal); no byte state makes `A16(d)` accept a wrong value on the
legitimate amendment, so there is no fail-open, no authority weakening and no
claim movement. But `A16(d)` is an **operative** validation clause, not wording,
and the contradiction lives in the governing bytes reviewers must be able to
trust — precisely the incomplete-re-scope error class this bounded round exists
to catch, and stronger than the v2.8 branch-count inaccuracy that was itself
ruled blocking.

**Why it is not implementation-log-only.** `A16(d)` is inside the joint block,
which must stay byte-identical in both files and whose bytes feed `H_BODY`,
`H_NORMATIVE` and `H_FILE`. Correcting the two loci changes the joint block hash
and the composite `H_FILE`, which forces §A0.4 to be **re-anchored** to the new
`H_FILE`. That is a specification regeneration, not a note.

**Repair (surgical).** In the joint block, change
`P1_WATCHDOG_V2_8_PRE_SELECTION_COMPOSITE_SHA256` → `…_V2_9_…` in `A16(d)` (both
files, byte-identically); recompute the joint block hash, `H_BODY`,
`H_NORMATIVE`, `H_FILE` and the two file digests; re-anchor §A0.4 to the new
composite `H_FILE`. No change to MS-11.1, MS-13, the 47-row IR-13, any owner,
code, count or authority boundary is required. After that, re-confirmation is a
targeted re-read of the two `A16(d)` loci, the §A0.4 anchor and the region
digests.

---

## Implementation-log-only notes (do not, by themselves, trigger regeneration)

- **B-2 (Minor, prose count).** `MS-13.1` describes `canonical.py`'s module scope
  as "one `__future__` statement, four import statements and eight function
  definitions." It is **five** non-`__future__` import statements (`hashlib`,
  `json`, `os`, `pathlib`, `typing`), not four. The bound value —
  `stdlib_seeds` = the six names — and the operative conclusion (no module-scope
  call) are correct; only the illustrative count is off by one.
- **B-3 (Minor, label count).** The IR-13 derivation range is called "sixteen
  sections" (amendment line 2471; closure §3) but enumerates fifteen distinct
  section labels. No relation is thereby omitted.

Since B-1 already requires a joint-block regeneration, B-2 and B-3 should be
folded into that same repair rather than deferred.

---

## What a future confirmation would authorize

A `CONFIRMED` verdict on corrected bytes authorizes **only Kirill's watchdog
author option selection**. It authorizes no key generation or entropy draw, no
Stage A or Stage B, no detached signature, no M4 manifest, no M7 attestation, no
install record, no implementation/verifier/manifest edit, no test run, no
install, no production entry, no `T` activation and no candidate, trajectory,
datum, Proof or claim movement. The selected process-identity Option A, the
unselected watchdog choice and the accepted scientific cells are not reopened.

`T = NOT_ACTIVATED`   programme claim = `OPEN`   watchdog cell = `NOT SELECTED`
process-identity cell = Option A, external author state only   bounded-weakening
token = `NOT ACCEPTED`

## Next boundary

Repair B-1 (and fold in B-2, B-3) in the joint block of both governing files,
re-anchor §A0.4, recompute the region and file digests, and re-issue for a
bounded independent X-line and Y-line re-confirmation on the corrected bytes by
reviewers that did not author v2.3–v2.9. This document authorizes nothing.
