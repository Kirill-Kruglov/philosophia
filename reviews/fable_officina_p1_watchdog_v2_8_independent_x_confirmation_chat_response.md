Internal consistency is **exact**: the author's MS-11.1 table canonicalizes to length 20534 and SHA-256 `aa974e0c…`, with 76 distinct transitive names, 39 empty arrays, closed under itself, written order = sorted order. Now the factual-independence part. First let me measure the interpreter's startup module set and resident set after importing the 18 seeds.

My `import json` polluted the startup snapshot. Let me fix the ordering and get a clean residency picture, including the normalization candidates (aliases, non-modules, `__main__`).

Independent residency confirms the **exact 89-row set**, the **2 pseudo-modules** (typing.io/re) and **3 aliases** — no difference either direction. Now let me verify every `kind`, then derive the transitive-import edges by execution tracing.

All 89 kinds match exactly (counts 29/13/2/45; fcntl/_socket BUILTIN; 13 frozen). Now the transitive-import edges. Let me first inspect the startup module list, then decide the tracing method.

Confirmed: `os` alone does **not** pull `ntpath` (os.path is posixpath) — the `os→ntpath` unexecuted-branch claim is independently verified. All BUILTIN/EXTENSION rows are correctly empty. Now let me build the execution-faithful edge tracer (evict + re-import under an `__import__` hook) and compute transitive closures.

Only 11 rows differ, and **every** difference is an edge *missing from mine*, never extra — concentrated in the codec/import-machinery modules (encodings, encodings.utf_8, zipimport, codecs) and their transitive dependents, plus `hmac`→`_operator`. This is a signature of my eviction+hook method missing edges imported via CPython's C-level import path (which bypasses `builtins.__import__`). Let me switch to a static top-level code-object parse (the spec's own derivation-b method), which reads the actually-loaded code objects directly.

**Zero differences** — the static top-level code-object parse (the spec's own derivation-b) reproduces all 89 transitive_imports arrays exactly, with the single `os→ntpath` unexecuted-branch removal that I verified by execution. Now the decisive test: build the full canonical value from my **independently-derived** kinds + edges + booleans and compute the CANON digest. Also enumerate the unexecuted branches to check the "six" claim.

**The independent CANON digest matches exactly: length 20534, SHA-256 `aa974e0c…`** — reproduced from the interpreter's own residency and code objects, not from the author's table. X1 items 1–6 confirmed. Now let me enumerate the unexecuted branches (the "six" claim) and audit the 267 booleans (module-level side-effect calls).

The boolean scan found **zero** module-level occurrences of any side-effect term across all 89 top-level code objects — confirming all 267 booleans false (X1.4). The real non-resident *module* branches match the author's six — **except** I also see `datetime → _pydatetime`, which is a genuine unexecuted module-scope branch not in the author's list of six. Let me examine `datetime.py` to determine whether this is a real 7th branch.

`datetime.py` is `try: from _datetime import * … except ImportError: from _pydatetime import *`. On this build `_datetime` (builtin) is available, so `_pydatetime` is a genuine **unexecuted module-scope import branch** — the same class as the author's `abc → _py_abc`. Let me enumerate the definitive set of module-scope IMPORT_NAME base targets that don't execute, to get the exact branch count.

Definitive branch enumeration: the distinct unexecuted module-scope import branches are `os→{nt,ntpath}`, `ntpath→{nt,_winapi}`, `_frozen_importlib_external→{nt,winreg}`, `abc→_py_abc`, `hashlib→logging`, **and `datetime→_pydatetime`** — that is **seven** source-module branches, not the six the author enumerates in MS-11.3 (governing bytes) and §2.5. The closure value itself remains exact; this is an accuracy defect in the enumeration. 

Now X2 — the subprocess experiment.

X2 fully confirmed: post-reduction union → exactly 89 rows; adding `subprocess` reaches **exactly** the 8 claimed modules (`_locale _posixsubprocess locale select selectors signal subprocess threading`); `threading` module-level code **actually calls `os.register_at_fork` once** at import (n=1); post-reduction closure has zero side-effect hits. Now let me audit the topology (X3) and integrity/counts (X4) in the composite. Let me read the CK/VP/TS and graph sections.

Let me read the VP-3/VP-4 ownership tables and the CK check sequence to audit single-ownership and prerequisite ordering (X3).

The topology (VP-1..VP-4, CK-1..CK-15, TS-2A/2B, VP-3 single-ownership) is internally coherent, and all six multi-fault fixtures' first-codes are consistent with the literal CK order. Let me quickly verify the remaining integrity counts (member classes, failure codes, MS-2/MS-3 cardinalities), then write the review.

All X4 integrity counts confirmed: 65 members (2/51/7/1/1/2/1), 182/54/236 loci, 24 test rows, exactly 26 closed failure codes, MS-2=51, MS-3=7. My independent computation is complete. Let me record the finding to memory context and write the review file.

Confirmed: `_datetime` is builtin, so `datetime.py`'s `except ImportError: from _pydatetime import *` never executes — `datetime→_pydatetime` is a genuine unexecuted module-scope branch, omitted from **both** the composite MS-11.3 (governing bytes, line 3695) and packet §2.5 (line 463). Now writing the review file.

Let me compute the review file's digest for the record and confirm it's a new untracked file (nothing existing modified, nothing committed).

Independent X-line review complete. The new review file is written and untracked; nothing existing was modified and nothing was committed.

## Verdict

```
REVISE_OFFICINA_P1_WATCHDOG_V2_8
```

One blocking-class finding — and it does **not** touch the frozen closure value, which I reproduced exactly. Written to [reviews/fable_officina_p1_watchdog_v2_8_independent_x_confirmation.md](reviews/fable_officina_p1_watchdog_v2_8_independent_x_confirmation.md) (sha256 `ddd6d63a…95d8e8e9`).

## Hashes
All four primary bytes match the pinned digests at `dba33e6` (`5666d2bf…`, `28b57c47…`, `6b867790…`, `7a8ab2da…`); files are identical at HEAD. Untrusted Opus 5 closure = `fd004504…`, relied on for nothing. The review host interpreter is byte-identical to the audited build (`Python 3.12.3 (main, Jun 19 2026, 12:46:00) [GCC 13.3.0]`, x86_64), so the closure was reconstructed on the exact pinned interpreter.

## Independent closure result / differences
Reconstructed all 89 rows from residency + static code-object parse, importing no production module:
- **Row set, kinds, normalizations: 0 differences.** 89 canonical rows (95 module-table entries − `__main__` − 2 pseudo-modules `typing.io/re` − 3 aliases). Kinds 29/13/2/45; `fcntl`/`_socket` BUILTIN; 13 frozen — all match.
- **Transitive edges: 0 of 89 rows differ**, element for element.
- **267 booleans all false** (module-scope scan → zero side-effect hits).
- **Digest reproduced from independently-derived data:** length **20534**, sha256 **`aa974e0c…dc20ee`** — exact. 76 distinct ti-names, 39 empty arrays, self-closed. Fourteen-row bootstrap subset byte-identical.

**The one difference (BLOCKING B-1):** the governing bytes enumerate the unexecuted module-scope branches as **"Six"** (composite `MS-11.3` line 3695; packet §2.5 line 463), but there are **seven** — `datetime → _pydatetime` is omitted (a `try:from _datetime import * except ImportError:from _pydatetime import *` branch; `_datetime` is builtin so the except never runs, same class as the listed `abc→_py_abc`). Verified by execution. It changes no row/kind/edge/boolean/digest — a one-line correction (six→seven + the row), no closure recomputation.

## Subprocess experiment (X2)
Fully confirmed. Post-reduction union → exactly 89 rows. Adding `subprocess` reaches **exactly** the 8 claimed modules (`_locale _posixsubprocess locale select selectors signal subprocess threading`). **`import threading` calls `os.register_at_fork` exactly once** at module scope (spy-confirmed) — the decisive finding holds. Post-reduction closure has zero forbidden/side-effectful surface. `__future__` is a real runtime `IMPORT_NAME`; `_thread` residency/edge disclosure accurate. No defect.

## Topology result (X3/X4)
No defect. TS-2A/2B prerequisite split sound; VP-1 S1–S5 sub-phase present; VP-3 single-ownership holds (no relation owned twice or zero times); install-record position literal (CK-5→CK-6→CK-7); `HISTORICAL_BYTE_MOVED`@CK-7 vs `MEMBER_STALE`@CK-13 distinct; all six multi-fault fixtures resolve to one first code and I could not construct a divergent state. B14 edge present; members 65 = 2/51/7/1/1/2/1; loci 182/54/236; 26 codes; 15 checks; 24 test rows; A0.4/FS/TR-2/row 106(i)/`T=NOT_ACTIVATED`/programme `OPEN` all preserved.

## Findings by severity
- **BLOCKING (1):** B-1 branch enumeration off by one (seven vs six).
- **MAJOR:** none.
- **INFO:** MS-11.3 otherwise exact (3 aliases, 2 pseudo-modules, 2 disclosures reproduced); `os→ntpath` correctly excluded though `ntpath` is resident (verified by execution).

## Next boundary
Repair B-1 in the two loci with **no** change to `MS-11.1`/its CANON value/length `20534`/digest `aa974e0c…`, then a fresh independent X (Fable 5 or Opus 4.8, non-author of v2.3–v2.8) plus bounded Sol Y re-confirm via a targeted re-read of the two edited loci and a digest re-check. This document authorizes no keys, artifacts, implementation, tests, install, activation, selection or science; `T` stays `NOT_ACTIVATED`, programme claim `OPEN`.
