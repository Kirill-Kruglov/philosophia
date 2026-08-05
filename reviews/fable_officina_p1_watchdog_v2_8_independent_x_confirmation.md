# Officina P1 watchdog-freeze v2.8 — independent X-line confirmation

**Reviewer:** Claude Code, model `claude-opus-4-8`, fresh session. Independent X
line. Did not author v2.3 through v2.8. The Opus 5 closure
(`reviews/opus5_officina_p1_watchdog_freeze_choice_v2_8_closure.md`) was treated
as adversarial context only and was relied on for nothing.

**Reviewed commit:** `dba33e6` ("Repair watchdog role import closure in v2.8").
No historical or untracked file was edited; nothing was committed.

**Pinned build match:** the review host interpreter is byte-identical to the
audited build — `Python 3.12.3 (main, Jun 19 2026, 12:46:00) [GCC 13.3.0]`,
`x86_64` Linux — so `reachable_closure` was reconstructed on the exact
interpreter, not a proxy. All derivations ran under `env -i python3 -I -S -E -P`
(empty environment, the §P1-7.1 launch vector) and imported **no** Philosophia
production module.

---

## VERDICT

```
REVISE_OFFICINA_P1_WATCHDOG_V2_8
```

**One blocking-class finding, and it does not touch the frozen closure value.**
The 89-row `reachable_closure` — every module, every kind, every transitive
edge, every one of the 267 booleans, all three normalizations, the canonical
length and the SHA-256 — was independently reconstructed from the pinned
interpreter with **zero difference** from `MS-11.1`, and the digest was
reproduced exactly. The `subprocess` reduction reproduces exactly, including the
`threading` → `os.register_at_fork` module-scope call. The validation topology
and every recomputed count are confirmed.

The defect is a **factual inaccuracy in the governing bytes**: `MS-11.3` (and
packet §2.5) enumerate the unexecuted module-scope import branches as **"Six"**,
but there are **seven** — `datetime → _pydatetime` is omitted. The value
`M4.reachable_closure` must equal is unaffected (`_pydatetime` is correctly
excluded), so this is a one-line correction, after which re-confirmation should
be immediate. Because the X-line brief specifically directs verification of the
branch enumeration and states that "any wrong … branch is BLOCKING", and because
the false claim lives in the governing bytes reviewers must be able to trust,
`CONFIRMED` is not available this round.

This verdict, had it been `CONFIRMED`, would have permitted only Kirill's
watchdog option choice and would have authorized no keys, artifacts,
implementation, tests, install, activation or science. `T` remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.

---

## Hashes verified at `dba33e6`

| File | SHA-256 | Result |
|---|---|---|
| `…AUTHOR_CHOICE_PACKET_V2_8_CORRECTION.md` | `5666d2bf…b481ca8` | **match** |
| `…WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md` | `28b57c47…4711efd4` | **match** |
| `…P1_OPERATIVE_COMPOSITE_V1_8.md` | `6b867790…65a352176` | **match** |
| `…P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md` | `7a8ab2da…472e3d1f` | **match** |

All four primary bytes match the pinned digests exactly. The four files are
byte-identical between `dba33e6` and `HEAD` (`8f0f5b8`). `M1` document digests
are post-selection (after variant resolution) and are therefore not computable
from the pre-selection on-disk composite; that is by design and is not a defect.

The untrusted Opus 5 closure hashes to
`fd0045041516baa419b9c8fd01054bcf2fab360d7af874203626070454db3585` at this
commit; it was not used as evidence.

---

## X1 — independent reconstruction of the 89-row role closure

Method, all on the pinned interpreter, importing no production module:

1. **Residency (derivation a).** Fresh isolated interpreter (`-I -S -E -P`,
   empty env), import the eighteen-name union of the three scoped direct
   allowlists (PCS `os sys _signal time fcntl _socket`; role `os sys fcntl`;
   generic_harness sixteen `__future__ ast dataclasses datetime enum fcntl
   hashlib hmac json os pathlib re time typing weakref _socket`), record the
   module table.
2. **Normalization, derived not assumed.** The module table after import held
   95 entries. Independently identified: `__main__`; two non-module objects
   (`typing.io`, `typing.re`, both `_DeprecatedType`); three alias keys
   (`os.path`→`posixpath`, `importlib._bootstrap`→`_frozen_importlib`,
   `importlib._bootstrap_external`→`_frozen_importlib_external`). Removing these
   six yields **exactly 89** canonical rows.
3. **Kinds (import-system origin).** BUILTIN 29, FROZEN 13, EXTENSION 2,
   PURE_PYTHON 45. `fcntl` and `_socket` are BUILTIN on this build (compiled in);
   13 rows frozen. **Every one of the 89 kinds matches `MS-11.1`.**
4. **Transitive edges (derivation b).** Static top-level `IMPORT_NAME` parse of
   the code object *actually loaded* for each of the 58 FROZEN/PURE_PYTHON rows
   (BUILTIN/EXTENSION rows have no Python code object and are correctly empty),
   resolving relative levels and fromlists, filtering to resident rows, then
   transitive closure excluding self. The single resident-but-unexecuted branch
   `os → ntpath` was removed after **verifying by execution** that `import os`
   alone does not make `ntpath` resident (`os.path is posixpath`).
5. **Result.** Every one of the 89 `transitive_imports` arrays matches
   `MS-11.1` element for element — **0 rows differ of 89**.
6. **Booleans.** A module-scope scan of all 89 top-level code objects for
   `register_at_fork start_new_thread Thread Popen fork posix_spawn system
   signal setitimer set_wakeup_fd settrace setprofile addaudithook excepthook
   unraisablehook atexit` returned **zero** occurrences → all **267 booleans
   false**, confirmed.
7. **Digest, reproduced from independent data.** Building the canonical value
   from the independently-derived kinds and edges (all booleans false), then
   `CANON` per `MS-0` (sorted object keys, `(",",":")` separators, pure-ASCII,
   single trailing `0x0A`), array sorted ascending by `module`:

   ```
   length  20534           (claim 20534)   MATCH
   sha256  aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee   MATCH
   ```

   The digest was reproduced twice: once from the author's `MS-11.1` table
   (internal consistency) and once from the interpreter's own residency and code
   objects (factual independence). Both give length 20534 and
   `aa974e0c…dc20ee`.

8. **Corroborating counts.** 76 distinct names occur in some
   `transitive_imports` and each is a row (self-closure holds); 39 rows have an
   empty array; the value is closed under itself; written order equals sorted
   order. All confirmed.
9. **Fourteen-row bootstrap subset** (`_abc _collections_abc _signal _socket
   _stat abc fcntl genericpath os posix posixpath stat sys time`) is byte-for-
   byte identical to the v2.7-confirmed subset — verified as a consequence of the
   exact whole-value match.

### X1 blocking finding — the branch enumeration is off by one

The definitive set of **unexecuted module-scope import branches** on the pinned
build (module-scope `IMPORT_NAME` targets that do not execute) is:

| Source module | Branch target(s) | Reason | In author's "six"? |
|---|---|---|---|
| `os` | `nt` | Windows branch; posix taken | yes |
| `os` | `ntpath` | same Windows branch (ntpath resident via `pathlib`) | yes |
| `ntpath` | `nt`, `_winapi` | Windows-only | yes |
| `_frozen_importlib_external` | `nt`, `winreg` | Windows-only | yes |
| `abc` | `_py_abc` | `except ImportError`; `_abc` succeeds | yes |
| `hashlib` | `logging` | `except ValueError` handler; constructors available | yes |
| **`datetime`** | **`_pydatetime`** | **`except ImportError`; `_datetime` is builtin, so the except never runs** | **NO** |

`datetime.py` on this build is `try: from _datetime import * … except
ImportError: from _pydatetime import *`. `_datetime` is in
`sys.builtin_module_names`, so the except branch does not execute and
`_pydatetime` is not resident — the same class of branch as the author's
`abc → _py_abc`, and `datetime` is a direct allowlist seed whose code object was
audited (row 38, `transitive_imports = [_datetime]`, correct). The branch is
therefore a real **seventh** unexecuted module-scope branch that the enumeration
must list.

The false count appears in two places:

- **Governing bytes:** composite `MS-11.3`, "UNEXECUTED MODULE-SCOPE BRANCHES.
  Six, each with its reason" (composite line 3695).
- **Packet:** §2.5, "THE SIX UNEXECUTED MODULE-SCOPE BRANCHES" (packet line 463).

**Severity: BLOCKING (per the X-line brief), but confined.** It does not change
any row, kind, edge, boolean, normalization, or the `CANON` value/length/digest;
`M4.reachable_closure` is unaffected and `CK-10` is unaffected. The repair is:
change "Six" to "Seven" and add the `datetime → _pydatetime` row with its reason
in both loci. No closure recomputation is required.

---

## X2 — the `subprocess` reduction

All independently reproduced on the pinned build:

- The post-reduction sixteen-name generic_harness allowlist (union eighteen)
  yields **exactly 89** resident canonical rows.
- Adding `subprocess` (the pre-reduction seventeen-name allowlist) reaches
  **exactly** the eight extra modules claimed:
  `_locale _posixsubprocess locale select selectors signal subprocess threading`
  — set-equal to the claim, no more, no fewer.
- Four of those eight — `threading signal select selectors` — are named by
  §P1-3.2 as permitted in no file.
- **`threading`'s module-level code calls `os.register_at_fork`.** Its top-level
  code object references `register_at_fork`, and a spy on `os.register_at_fork`
  recorded **exactly one** call triggered by `import threading`. This is the
  decisive finding the reduction rests on, and it is confirmed: under version
  1.4's denotation `registers_at_fork` would have been true for a module
  resident in every role process, including the WATCHDOG.
- **Removing only `subprocess`** eliminates all eight modules and every
  import-time starts-task / registers-at-fork / installs-handler surface: the
  267-boolean scan over the resulting 89 rows returned zero hits. No other direct
  import independently reaches a forbidden or side-effectful surface — the
  post-reduction closure contains none of `subprocess threading signal select
  selectors _posixsubprocess locale _locale socket multiprocessing concurrent
  asyncio ctypes atexit gc`.
- **`__future__`** is a genuine runtime module (PURE_PYTHON, row 1, empty array,
  a real `.py` file); a `from __future__ import …` statement compiles to a real
  `IMPORT_NAME` of it. Confirmed.
- **`_thread` disclosure accurate.** `_thread` is BUILTIN with an empty array,
  is resident in the interpreter's start-up module table before any contract
  import, and is reached by executed module-scope edges from `functools` and
  `reprlib`. It starts no thread (thread-frame count 1 before and after; its
  booleans are false). The §P1-3.3 rule (`signal`, `threading`, `_thread`, … in
  no allowlist) is unweakened; only the obsolete *rationale* about `_thread` is
  corrected. Confirmed.

The reduction's zero-scan-hit claim was checked against the scan definition, not
accepted on faith: the scan is a module-scope name scan over the top-level code
objects, and it is inspecting the right surface. **X2: no defect.**

---

## X3 — validation topology

Audited as executable logic against `VP-1..VP-4`, `TS-2A/TS-2B`, `CK-1..CK-15`.

- **`TS-2A/TS-2B` split is sound.** `TS-2A` A1..A14 reads only the Stage-A file
  and literal constants (evaluated at `CK-2`); `TS-2B` A15, A16(a)..(d), A17
  every clause reads the manifest (evaluated at `CK-9`, after `CK-7`/`CK-8` prove
  M4 present, parseable, an object, exactly keyed, exactly typed). No `TS-2B`
  clause can read an absent/invalid/non-object/missing-key/mistyped M4 — each is
  already fatal earlier with its own single code.
- **`VP-1` prerequisite sub-phase (S1..S5) exists and is ordered first** — the
  precise gap that let a version-1.4 M4-dependent clause be ordered before its
  object existed.
- **Single ownership holds.** `VP-3`'s relation→owner→code table gives every
  record/M4/M7/Stage-A/Stage-B field and every cross-object relation exactly one
  earliest owner and one code. `reachable_closure`: structural `CK-8` S5/S8,
  semantic `CK-10`/`MANIFEST_VALUE_MISMATCH` — one semantic owner. The two
  version-1.4 duplications (CK-7 "every MS-12 relation" vs the nine Stage-A rows;
  CK-13 re-asserting an M2/M3 identity) are both removed. No relation is owned
  twice or zero times.
- **Install-record position is literal:** `CK-5` exists → `CK-6` structural →
  `CK-7` members; "inside CK-6" is gone as an ordering rule.
- **`HISTORICAL_BYTE_MOVED` (CK-7) vs `MEMBER_STALE` (CK-13) are distinct.**
  CK-7 owns an M2/M3 member whose *recomputed* digest differs from the literal
  `MS-2`/`MS-3` value; CK-13 owns the record's *members array* disagreeing with
  the enumerated set. Different objects, different owners, disjoint.
- **All six mandated multi-fault fixtures resolve to one first code**, each
  consistent with the literal `VP-4` order: absent M4 → `CK-7 MEMBER_OMITTED`;
  invalid-JSON M4 → `CK-8 MEMBER_SUBSTITUTED`; malformed record ± absent/stale
  member → `CK-6 MEMBER_SUBSTITUTED`; M4-semantic + Stage-A-binding →
  `CK-9 STAGE_A_BINDING_MISMATCH`; changed M2/M3 + coordinated mismatch →
  `CK-7 HISTORICAL_BYTE_MOVED`. Because the checks are totally ordered and each
  relation has a single earliest owner, I could not construct a multi-fault state
  that permits two conforming implementations to return divergent first codes.

**X3: no defect.**

---

## X4 — integrity, counts and regressions

- **Graph completeness.** The `Stage B --selected_option_token equality
  (B14)--> Stage A` edge is present in `IR-4`, §P1-14.5, packet §3, and test row
  115. `A9`'s intra-object pairing is correctly named as *not* an edge. Re-deriving
  edges over every path/digest/id/signature/option-token/key/count/assertion
  relation surfaced no further omission.
- **Member set:** classes `M1..M7` = `2 / 51 / 7 / 1 / 1 / 2 / 1` = **65**;
  digest distribution `2/51/7/1/1/2/1` sums to 65. `MS-2` cardinality 51, `MS-3`
  cardinality 7 as stated.
- **Governing loci:** file 1 = 82 + 70 + 10 + 6 + 2 + 12 = **182**; file 2 =
  23 + 4 + 3 + 24 = **54**; total **236** (delta +3 from 233: CK 13→15, N 14→15).
  Arithmetic checks.
- **Failure codes:** exactly **26** distinct closed codes. **Checks:** 15.
  **Test rows** 92..115 = **24**. `reachable_closure` rows **89**;
  generic_harness allowlist **16**. All confirmed.
- **Preservation:** `§A0.4` anchor is one line, generation-scoped to
  `V2_8`, extraction rule `TS-2B A16(d)`, TR-2(b) unchanged; FS-1..FS-5 and
  TR-2(a)/(b) carried; row 106(i) expected PASS
  (`OUTSIDE_GUARANTEE_COHERENT_ROLLBACK`); W-A/W-B symmetry and non-selection;
  identity Option A boundaries with
  `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` not accepted;
  `T = NOT_ACTIVATED`; programme claim `OPEN`; negative authorization space
  intact across all three files. No live overclaim found.

**X4: no defect.**

---

## Findings by severity

**BLOCKING (1) — accuracy of the governing bytes:**

- **B-1.** The unexecuted module-scope branch enumeration is **seven, stated as
  six** — `datetime → _pydatetime` is omitted. Loci: composite `MS-11.3` (line
  3695) and packet §2.5 (line 463). Verified: `_datetime` is a builtin so the
  `except ImportError` branch never runs; `_pydatetime` is a genuine top-level
  `IMPORT_NAME` in `datetime.py`'s loaded code object and is correctly absent
  from the closure. **The frozen `MS-11.1` value, its length, and its digest are
  unaffected.** Repair: "Six" → "Seven" plus one row in both loci; no closure
  recomputation.

**MAJOR:** none.

**INFO:**

- **I-1.** The `MS-11.3` audit-provenance section is otherwise exact: the three
  normalizations (3 aliases, 2 pseudo-modules) and the two disclosures (ABC
  bookkeeping; `_thread` residency/rationale correction) are all independently
  reproduced.
- **I-2.** `os → ntpath` is correctly excluded even though `ntpath` is resident
  (imported unconditionally by `pathlib`); verified by execution, not assumed.

---

## Next boundary

If B-1 is repaired (correct the branch count to seven and add the
`datetime → _pydatetime` row in `MS-11.3` and packet §2.5) with **no** change to
`MS-11.1`, its `CANON` value, length `20534` or digest `aa974e0c…dc20ee`, and no
change to any other row/kind/edge/boolean/normalization/count, the closure and
the entire remainder of v2.8 are independently confirmed and re-confirmation is a
targeted re-read of the two edited loci plus a digest re-check. A fresh
independent X reviewer (Fable 5 or Opus 4.8, not an author of v2.3–v2.8) and the
bounded Sol Y line should perform that pass; the author closure remains an
untrusted self-assessment normative for nothing. No key, artifact,
implementation, test, install, activation, selection or science is authorized by
this document.
```
T = NOT_ACTIVATED    programme claim = OPEN    no option selected    no token minted
```
