# Officina P1 watchdog-freeze v2.7 — independent X-line confirmation

**Verdict:** `OFFICINA_P1_WATCHDOG_V2_7_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`

**Reviewer:** Claude Code, model `claude-opus-4-8`, fresh session. Fable 5 was
not available in this environment; the packet §9 fallback (Opus 4.8, an agent
that did not author v2.3–v2.7) applies. I did not author the v2.3, v2.4, v2.5,
v2.6 or v2.7 watchdog documents. The Opus 5 closure
`reviews/opus5_officina_p1_watchdog_freeze_choice_v2_7_closure.md` and the
author packet were treated as **adversarial context only**; every claim below
was recomputed from the governing bytes.

**Reviewed state:** the exact commit `9acc3ea` (`Repair watchdog semantic checks
in v2.7`). No existing file was modified and nothing was committed.

**This confirmation authorizes only Kirill's watchdog option selection.** It
authorizes no key, entropy draw, Stage A/B artifact, detached signature,
manifest, attestation, install record, code, test run, install, activation, T
movement or science.

---

## Hashes recomputed from `9acc3ea` (SHA-256)

```text
a03afc3acab5e37d9b27c4f1538887aa5216f6a910546ac2389bede8ede3efb0  ...PACKET_V2_7_CORRECTION.md                         MATCH
f845b98dcef0edc415420fec1103f7adad4f905c21380a0dddcba0d3b370b794  ...AMENDMENT_V1_4_DRAFT.md                            MATCH
5301f7e987b768cc3acd9641f6f00400a74b453773299cbd379473c7db569beb  ...P1_OPERATIVE_COMPOSITE_V1_7.md                     MATCH
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  ...IDENTITY_SELECTION_V1_SIGNATURE.md (unchanged)     MATCH
```

Supporting recomputations:

```text
d06e7098f0c1b241f607dbab2ff48435ea2db15fa7c34fc70784bdd5ef8d25c7  JOINT INSTALL AND AUTHORIZATION BLOCK — byte-identical in amendment §A10 and composite §P1-14.4 (1713 lines each)
e28c33e3985317a25c333a02674784cb23516b9c50232f8064deed17a8abf287  CANON(reachable_closure), length 2118 — independently reconstructed (see X2)
5301f7e987b768cc3acd9641f6f00400a74b453773299cbd379473c7db569beb  §A0.4 pre-selection composite anchor value = composite v1.7's own on-disk digest (carried by the amendment, not by the composite)
```

---

## X1. Custody and byte structure — PASS

- **Input digests:** all four match the packet's stated values (above).
- **Joint block byte-identity:** the JOINT INSTALL AND AUTHORIZATION BLOCK is
  byte-identical in the amendment (§A10, lines 1136–2848) and the composite
  (§P1-14.4, lines 2955–4667), 1713 lines each, SHA `d06e7098…`.
- **§A0.4 anchor cardinality/value:** exactly **one** line in the amendment
  matches the A16(d) grammar (`P1_WATCHDOG_V2_7_PRE_SELECTION_COMPOSITE_SHA256`
  ` = ` 64 hex, whole line); zero and ≥2 both fail. Its value is
  `5301f7e9…`, which equals the composite v1.7 on-disk digest. The composite's
  current bytes **are** the pre-selection bytes (OR-4 has not run), so this
  anchor is recomputable now and consistent.
- **No self-digest:** the amendment does not contain `f845b98d…`, the composite
  does not contain `5301f7e9…`, the packet does not contain `a03afc3a…`.
- **Determination order acyclic:** the only inter-file digest edge is
  amendment → composite (the A0.4 anchor). Composite → nothing; packet → nothing
  (its pair digests live in the companion closure, not inline). The order
  composite → amendment → (manifest, install-time) is a DAG with no back-edge.
- **Acyclic ≠ scientifically adequate — distinguished:** the scheme is acyclic
  and internally consistent, but it is **not** a freshness/rollback-resistance
  mechanism. A complete coherent rollback of an entire generation passes every
  clause (TR-2(b)), and the bytes say exactly that (N-12, §A0.4, FS-2, §3.1
  class 5). Confirmed as an integrity binding adequate for its stated purpose
  (anchoring the author's option selection), **not** as anti-rollback custody —
  and it claims only the former.

## X2. Independently derived `reachable_closure` — PASS (BLOCKING-class item cleared)

I did **not** copy the author's fourteen rows. My interpreter is **exactly the
pinned build**: `CPython 3.12.3 (main, Jun 19 2026, 12:46:00) [GCC 13.3.0]`,
x86_64 Linux — the same string §P1-2.1/MS-11.2 pin. I therefore derived the
closure directly on the pinned build.

Method: roots = union of the two §P1-3.2 scoped bootstrap allowlists
(`{os,sys,_signal,time,fcntl,_socket}` ∪ `{os,sys,fcntl}` =
`{os,sys,_signal,time,fcntl,_socket}`). Kinds via the import system. Module-scope
transitive imports via **two independent derivations that agreed on every edge**:
(a) AST parse of each stdlib module's source, descending module-scope
try/except/if but not function/class bodies; (b) `IMPORT_NAME` operands of the
loaded top-level code object. Branch resolutions verified **empirically** by
observing `sys.modules` after import in an isolated `-I -S -E -P` interpreter.

**My independently derived table (identical to MS-11.1):**

| # | module | kind | transitive_imports |
|---|---|---|---|
| 1 | `_abc` | BUILTIN | (empty) |
| 2 | `_collections_abc` | FROZEN | `_abc abc sys` |
| 3 | `_signal` | BUILTIN | (empty) |
| 4 | `_socket` | BUILTIN | (empty) |
| 5 | `_stat` | BUILTIN | (empty) |
| 6 | `abc` | FROZEN | `_abc` |
| 7 | `fcntl` | BUILTIN | (empty) |
| 8 | `genericpath` | FROZEN | `_abc _collections_abc _stat abc os posix posixpath stat sys` |
| 9 | `os` | FROZEN | `_abc _collections_abc _stat abc genericpath posix posixpath stat sys` |
| 10 | `posix` | BUILTIN | (empty) |
| 11 | `posixpath` | FROZEN | `_abc _collections_abc _stat abc genericpath os posix stat sys` |
| 12 | `stat` | FROZEN | `_stat` |
| 13 | `sys` | BUILTIN | (empty) |
| 14 | `time` | BUILTIN | (empty) |

**Differences from the author's value: NONE.** Every module, every kind, every
transitive-import array matched byte for byte.

- **Cardinality:** 14. Kind counts BUILTIN 8, FROZEN 6, EXTENSION 0,
  PURE_PYTHON 0 — matches.
- **Build-sensitive kinds** (the ones X2 flags): on the pinned build, `fcntl`
  and `_socket` are **BUILTIN** (compiled into the interpreter, in
  `sys.builtin_module_names`), not dynamic extensions. Independently confirmed.
- **Branch decisions:** `os`/`nt` — posix branch taken, nt/ntpath excluded
  (`posix` in `builtin_module_names`, `nt` not); `abc`/`_py_abc` — the `_abc`
  try succeeds so the except branch (and `_py_abc`, `_weakrefset`, `_weakref`,
  `types`) never runs; `os.path`/`posixpath` — `os.path` is an alias binding for
  the already-imported `posixpath` (`os.py`: `import posixpath as path`;
  `sys.modules['os.path']=path`), not a distinct row. All three empirically
  confirmed.
- **These are the only three membership-affecting platform-conditional cases.**
  I enumerated every module-scope conditional import block in all six frozen
  sources. `posixpath`'s `try: from posix import _path_normpath` and `stat`'s
  `try: from _stat import *` resolve to already-present builtins and add no
  member; `os`'s other `import subprocess`/`import nt` are function-local (inside
  `popen` and `add_dll_directory`), not at import time. No fourth case exists.
- **Booleans:** all 42 are false. No frozen module's module-level code starts a
  thread/process, calls `os.register_at_fork`, or installs a
  signal/atexit/audit/trace/import/sys hook. The only module-level `*.register`
  calls are `_collections_abc`'s ABC virtual-subclass registrations — exactly
  the author's disclosure; not at-fork/atexit/handler installs. `os` defines but
  does not call `register_at_fork`. Independently confirmed.
- **Self-closure:** the ten distinct names in any transitive_imports
  (`_abc _collections_abc _stat abc genericpath os posix posixpath stat sys`)
  are each a row; the four remaining rows are roots with empty closures. Closed.
- **Canonical length/hash:** I built the value as an array of objects with the
  six keys, serialized under MS-0 (sorted keys, `,`/`:` separators, ASCII, plus
  one trailing `0x0A`). Result: **length 2118 bytes, SHA-256
  `e28c33e3…abf287`** — reproduced independently, matches MS-11.3.

**Nonexistent bootstrap roots — decided.** The two script roots
(`officina_process_control_bootstrap.py`, `officina_role_bootstrap.py`) do not
exist. Their *root-level* import sets are taken from the §P1-3.2 scoped
allowlists (contract literals), not from files; the *transitive* edges and
*kinds* are audited against the standard library and the pinned interpreter,
both of which exist — and I audited them. This is therefore a **valid
contract-level literal closure**, not a factual claim that cannot yet be
audited: I audited every part of it now. Its correspondence to the eventual
bootstrap files is enforced (not assumed) by the §P1-3.2 scoped-allowlist rule
("a file with an entry gets EXACTLY that entry"), by §P1-7.1's pinned argv
guaranteeing frozen modules stay frozen, and by MS-11.4 requiring a new reviewed
generation on any graph change, with G-11/CK-7 re-checking at install. The
denotation deliberately excludes `generic_harness.py` and the two other roots
(covered by S-1..S-24b in the caller context); this bounded scope is coherent
and correctly disclosed.

**A wrong row, edge, kind, boolean or unjustified denotation would have been
BLOCKING. I found none.**

## X3. M4 semantic completeness — PASS

The MS-12 table gives all 20 M4 keys a semantic source, one owner and one code.
The five keys that had no owner/code in v1.3 —
`peer_amendment_sha256`, the three `pre_selection_*_sha256`, and
`reachable_closure` — now each have exactly one.

- `peer_amendment_sha256` is anchored to the SHA-256 of the M1 amendment bytes
  at MS-1's first literal path (CK-7), and B18 additionally requires Stage B's
  `governing_amendment_sha256` to equal it. An arbitrary 64-hex value now fails
  at CK-7 / `MANIFEST_VALUE_MISMATCH`.
- Packet and amendment pre-selection digests recompute from the literal TS-1
  paths (A16(b)/(c)); an absent file fails, no exemption.
- The composite pre-selection digest has **exactly one** unambiguous anchor —
  the single §A0.4 line (A16(d), cardinality-exactly-one), verified in X1.
- Every root and region digest is recomputed (CK-7 over MS-12; G-6/G-7).
- A structurally valid but factually wrong closure is refused (row 111 carries
  six such fixtures, including a kind flip, a true boolean, a spurious 15th row,
  `posix` removed with its references, `os` reduced to the §P1-3.3 six, and a
  wholesale unrelated array). The check is equality against the MS-11.1
  constant, **never** a live-interpreter recomputation — a verifier that
  recomputes and accepts fails row 111.
- No coordinated arbitrary digest triple passes: A16(a) mutual-equality is
  declared insufficient, and A16(b)/(c)/(d) anchor each to bytes/anchor (row
  106(d)).

## X4. Deterministic first failure — PASS

All 59 fields (M4 20, M7 10, record 5, Stage A 11, Stage B 13) appear exactly
once in VP-3 with a single earliest owner and a single code; VP-4 fixes a total
evaluation order (CK-1..CK-13; A1..A17 with A16(a)..(d); B1..B13, B14..B18;
S1..S8; MS-12 order; MS-7 order) and forbids hoisting/deferral.

- I attempted to construct a byte state yielding two defensible first codes and
  could not. The one genuine subtlety — the six `pre_selection_*` and three
  `stage_a_*` M4 fields are owned by **CK-2** (Stage A), which runs *before*
  CK-6 (M4's own structural phase) — is resolved: A15/A16/A17 read the manifest
  fail-closed and each raises exactly one code, and because VP-4 makes CK-2
  strictly precede CK-6, both conforming verifiers refuse at CK-2 with
  `STAGE_A_PRESELECTION_MISMATCH`/`STAGE_A_BINDING_MISMATCH` even when the
  manifest field is malformed or the manifest is unparseable. Coherent by
  design, not a defect.
- CK-1..CK-13, FC-1 and rows 105/111/113 reconcile: IR-3 and MS-7 value
  grammars lose their cross-object equalities (re-owned by CK-9 /
  `INSTALL_RECORD_NAME_MISMATCH` and CK-12 / `ATTESTATION_MISMATCH`); the
  undefined phrase "when the schema itself is violated" is withdrawn; row 105 and
  row 113 each carry explicit structural and semantic lists and fail a fixture
  that crosses them. CK-5 (multiplicity) now precedes any predicate over the
  record's bytes.
- **`MANIFEST_VALUE_MISMATCH` placement confirmed:** it is new in v1.4, the sole
  code of CK-7, listed once in FC-1's closed 26-code set, and appears as the M4
  semantic code throughout VP-3.

## X5. Integrity graph and regression — PASS

- **Graph:** IR-4 now carries the three Stage-A pre-selection edges
  (Stage A → packet / amendment / composite) and the M1-amendment → composite
  anchor edge, and these are asserted positively in composite §P1-14.5, packet
  §4 and **row 115** (which fails a build missing any edge and a Stage A whose
  `governing_pre_selection` omits the packet entry). No further omission found.
  No object attests itself; no uniqueness of attester (internal or external) is
  claimed.
- **Counts, all recomputed:** `233 = 179 + 54`; 149 tagged rules
  (81 amendment-side families `DA5 WA6 TIMING4 QC5 FD4 F8 KW3 FB5 TO5 RF3 NS4
  AK7 PUB4 H4 N14` + 68 joint families `IR12 MS13 TS6 OR11 CK13 FC1 TR2 FS5 VP4
  XS1`); 61 members `2+47+7+1+1+2+1` (MS-1..MS-7 cardinalities verified); 21
  disjoint class pairs `C(7,2)`; 54 matching M2+M3 digests (47+7); 55 provenance
  rows (54 + 1 baseline); 26 codes; 13 checks (CK-1..CK-13); 24 test rows
  (92..115). Delta from v2.6's 225 is +8 (MS+2, CK+1, VP+4, N+1), all in file 1.
- **Regression:** TR-2(a)/(b) carried forward, closed proper-subset list widened
  by four to fifteen (row 106(g)), residual narrowed by nothing; row 106(i)
  coherent-rollback expected **PASS** (fails a fixture asserting refusal); option
  symmetry preserved — all 20 variant-bearing composite lines byte-identical to
  v1.6, markers 13/13 whole-file, neither option selected; Stage-B wire format
  and validity predicate unchanged (X26-LOW-1's loose "verbatim" wording
  correctly withdrawn); identity Option A recorded at XS-1 and bound into
  nothing, `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` **not accepted**;
  `T = NOT_ACTIVATED`, programme claim `OPEN`; negative-authorization space
  intact. Part C: the three absolute digest sentences (composite preamble, G-6,
  G-7) are qualified to proper-subset current-generation checking, conditional on
  the manifest/authorization chain, cross-referencing TR-2(b); a lexical sweep of
  all three files found every occurrence of the swept terms to be a withdrawal, a
  prohibition, in-generation clock/liveness vocabulary, or a disambiguated
  document-authority word — **zero surviving positive detection/rollback/freshness
  claims**.

---

## Findings by severity

- **BLOCKING:** none.
- **MAJOR:** none.
- **MINOR / INFO:**
  1. *(INFO)* The `reachable_closure` literal is a valid contract-level constant,
     fully auditable now and matched byte-for-byte on the exact pinned build. Its
     correspondence to the two **nonexistent** bootstrap files is enforced by the
     §P1-3.2 scoped allowlists + §P1-7.1 argv pin + MS-11.4 + install-time G-11,
     not provable at authoring time. Correctly disclosed; downstream of and
     independent of the author choice; non-blocking.
  2. *(INFO)* The A0.4 anchor / determination scheme is acyclic and internally
     consistent but provides no freshness or rollback resistance; a coherent
     full-generation rollback passes (TR-2(b)). Correctly and repeatedly
     disclosed; no surviving overclaim.
  3. *(INFO)* The M4 `pre_selection_*`/`stage_a_*` fields are owned by CK-2,
     which precedes M4's own CK-6 structural phase. Deterministic via VP-4's
     total order and fail-closed self-reading A15/A16/A17; coherent by design.

None of these prevents Kirill from making the watchdog author choice.

---

## Independently derived closure table — differences

**None.** My from-scratch derivation on the pinned interpreter reproduced all 14
rows, all kinds, all transitive-import arrays, all 42 booleans (false), the
self-closure, the 2118-byte canonical length and the SHA-256
`e28c33e3…abf287` exactly.

## Status of the nonexistent bootstrap roots

`scripts/officina_process_control_bootstrap.py` and
`scripts/officina_role_bootstrap.py` do **not** exist. Their root import sets are
contract literals (§P1-3.2), their transitive edges/kinds are audited against the
extant standard library and pinned interpreter, and their eventual conformance is
enforced by the scoped-allowlist rule and re-checked at install. Valid
contract-level literal closure; no factual claim is left un-auditable.

## Exact next authorization boundary

Confirmation means **only** that Kirill may emit exactly one of the two existing
option tokens
(`…_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES` or
`…_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS`).

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A (recorded at XS-1, bound into nothing)
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 WATCHDOG-FREEZE CELL = NOT SELECTED → now selectable by author choice
```

It authorizes **no** key generation or entropy draw, **no** Stage A/B artifact,
**no** detached signature, **no** manifest / attestation / install record, **no**
implementation, verifier or manifest edit, **no** test run or install, **no** T
activation, and **no** scientific execution. Before this pair can become
operative, a later independently reviewed combined binding must record the
identity signature's path/digest, separately accept or refuse
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, state that signature's membership
status, and re-derive the process-claim identity fields.

---

**VERDICT:** `OFFICINA_P1_WATCHDOG_V2_7_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`
