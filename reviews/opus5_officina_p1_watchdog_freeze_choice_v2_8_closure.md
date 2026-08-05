# Author closure — Officina P1 watchdog-freeze author choice, v2.8

**Author:** Claude Code Opus 5, **specification author only**. Not an X-line or
Y-line reviewer. **This closure is an untrusted self-assessment and is normative
for nothing.** It adds no step to the handoff, states no rule, and resolves no
cell. Where it and the governing bytes differ, the governing bytes govern.

**Review base commit:** `15357b7` (`Review watchdog v2.7 role import boundary`).
No historical file, code file, test, untracked working-tree file, signature or
runtime artifact was modified. Nothing was committed.

---

## 1. Verdict — exactly one

```text
READY_FOR_OFFICINA_P1_WATCHDOG_V2_8_FINAL_XY_CONFIRMATION
```

`BLOCKED_OFFICINA_P1_WATCHDOG_V2_8` was the required return if the role import
closure violated the watchdog/control invariants and **no scoped-allowlist
reduction was contract-compatible without a new author decision**. The audit did
find a violation — `threading`, reached through `subprocess`, calls
`os.register_at_fork` at module scope, in every role process including the
WATCHDOG. A reduction closing it **is** contract-compatible and required no new
decision: `S-12`, test 8 and the future-edit surface already forbid `subprocess`
on every path of `generic_harness.py`, so removing it from that file's scoped
allowlist reconciles `§P1-3.2` with rules already in these governing bytes.
After the reduction the closure contains no module that starts a task, registers
an at-fork callback or installs a handler at import — verified by measurement,
not assertion. **BLOCKED was therefore not the correct return, and the conflict
was not hidden: `MS-11.2` and `MS-11.5` state it in the governing bytes.**

### 1.1 Inputs, recomputed at `15357b7`, all six MATCH

```text
a03afc3acab5e37d9b27c4f1538887aa5216f6a910546ac2389bede8ede3efb0  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_7_CORRECTION.md
f845b98dcef0edc415420fec1103f7adad4f905c21380a0dddcba0d3b370b794  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_4_DRAFT.md
5301f7e987b768cc3acd9641f6f00400a74b453773299cbd379473c7db569beb  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_7.md
4855020e522228eeb0625fba1efb78941bc547c124da2d1dbb754b548d3057cc  reviews/fable_officina_p1_watchdog_v2_7_independent_x_confirmation.md
0b33108e885fec97ab11e2de5c6ac3ba6ceeb8e98283bb29a09c70ce1c574780  reviews/sol_officina_p1_watchdog_v2_7_final_y_confirmation.md
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
```

All six are byte-unchanged on disk after this round.

### 1.2 Outputs — exactly four files, all new

```text
5666d2bf9cee3c4404cc1f26ac13050a40403af9b4631fa774a1bfacbe481ca8  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_8_CORRECTION.md
28b57c47f89f775199095717111e37a4e588628aa64b2801812f30814711efd4  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md
6b867790707ae7999b31c1ad3dd56a1d4b195efd8f7a8b2bda4c2b065a352176  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md
                                                                  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_8_closure.md  (this file)

COMPOSITE REGION DIGESTS, recomputed by the §P1-14.0 extraction algorithm:
  H_FILE       6b867790707ae7999b31c1ad3dd56a1d4b195efd8f7a8b2bda4c2b065a352176
  H_BODY       c18225d299afde0989eee8d5069aef219f4dcecf266a69de4e6c2d096a19f707
  H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
  H_NORMATIVE  bfd1f339522e5dfb51b571e6b340927843563b8118b18a0689637397530f42d3

JOINT INSTALL AND AUTHORIZATION BLOCK — byte-identical in amendment §A10 and
composite §P1-14.4, 2108 lines each:
  8dd14435128ada01a179da5fa833a065d51768f1cbba0df50456330a5361c2c1

PRE-SELECTION COMPOSITE ANCHOR, amendment §A0.4, token now generation-scoped to
P1_WATCHDOG_V2_8_..., cardinality exactly 1, value equal to the composite's
H_FILE above; zero lines match the retired V2_7 token.

CANON(reachable_closure), MS-11.4:
  length 20534   sha256 aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee

NO FILE CONTAINS ITS OWN DIGEST — verified for all three. Determination order
composite → amendment → packet → closure is acyclic with no back edge.
```

---

## 2. Disposition of every v2.7 finding

| Finding | Disposition | Where, in governing bytes |
|---|---|---|
| **Y27-B1(a)** `CK-2` ran M4-dependent clauses before M4 was known to exist | **CLOSED** | `TS-2` split into `TS-2A` (A1..A14, reads only Stage A) and `TS-2B` (A15..A17, every clause reads the manifest); `VP-1` names `S1`..`S5` as the prerequisite sub-phase; `CK-9` runs after `CK-7` and `CK-8` |
| **Y27-B1(b)** the non-member install record had no stated structural position | **CLOSED** | literal order `CK-5` locate → `CK-6` structurally validate the record → `CK-7`/`CK-8` members → `CK-9`..`CK-15` semantic; `IR-3` states it too |
| **Y27-B1(c)** two ownership duplications | **CLOSED** | `CK-10` evaluates exactly the eleven `MS-12` rows `TS-2B` does not own; the M2/M3 relation is owned once, at `CK-7`, raising `HISTORICAL_BYTE_MOVED`, and `MEMBER_STALE` is owned once, at `CK-13` |
| **Y27-B2** `MS-11`'s denotation left the role import surface unguarded | **CLOSED, and a real defect found and removed** | `MS-11` redenoted to all three scoped allowlists; `MS-11.1` carries 89 rows; `MS-11.5` removes `subprocess` from one allowlist; `§P1-3.2` and `§P1-3.3` corrected |
| **Y27-B3** the graph omitted the `B14` option edge | **CLOSED** | `IR-4`, `§P1-14.5`, packet §3, row 115; `IR-4` re-derives over option-, id-, key-, count- and assertion-bearing relations, not only digest/path/signature |
| **Y27-R** repository state stated wrongly | **CORRECTED** | two tracked roots, three absent, stated at `MS-11.3`, `MS-11.6`, `§P1-18`'s future-edit surface and packet §4; `MS-11.6` adds that `MS-11.1` is a prospective conformance constraint and not evidence of an implementation |
| **X27** fourteen-row closure reproduced with no difference | **PRESERVED EXACTLY** | those 14 rows in `MS-11.1` carry identical `kind` and identical `transitive_imports`, element for element — verified mechanically |

---

## 3. The new validation topology, and the mandated multi-fault results

```text
VP-4, THE LITERAL TOPOLOGICAL ORDER. Every predicate's prerequisites are
established by an EARLIER check, not merely ordered before it.

  CK-1   when — no predicate
  CK-2   Stage A alone        TS-2A A1..A14        reads only the Stage-A file
  CK-3   Stage B alone        TS-5 B1..B13         reads Stage B, .sig, Stage A
  CK-4   enumerate 65         a constant; reads no file
  CK-5   the record EXISTS and is UNIQUE           INSTALL_RECORD_ABSENT /
                                                   INSTALL_RECORD_REPLAYED
  CK-6   the record is STRUCTURALLY VALID  S1..S8  MEMBER_SUBSTITUTED
  CK-7   members EXIST; digests recomputed; M2/M3  MEMBER_OMITTED /
         against MS-2/MS-3, members in IR-1 order  HISTORICAL_BYTE_MOVED
  CK-8   M4 then M7 STRUCTURALLY VALID     S1..S8  MEMBER_SUBSTITUTED
  CK-9   Stage A against M4  TS-2B A15, A16(a-d), A17
                                                   STAGE_A_PRESELECTION_MISMATCH
                                                   STAGE_A_BINDING_MISMATCH
  CK-10  M4 semantics — the eleven MS-12 rows      MANIFEST_VALUE_MISMATCH
  CK-11  recompute install_record_id
  CK-12  id = filename = record field              INSTALL_RECORD_NAME_MISMATCH
  CK-13  members array vs enumerated set           MEMBER_EXTRA / MEMBER_STALE /
                                                   MEMBER_SUBSTITUTED
  CK-14  Stage B cross-object  TS-5 B14..B18       the STAGE_B_ codes
  CK-15  M7 semantics                              ATTESTATION_MISMATCH

VP-1's S1..S8 name S1..S5 — exists, parses, is an OBJECT, exact key set, exact
types — as THE PREREQUISITE SUB-PHASE, ordered first, because every later
predicate over that object presupposes them. That sub-phase is what version 1.4
lacked.

THE SIX MANDATED MULTI-FAULT STATES, EACH WITH ONE FIRST CODE:

  valid Stage A + absent M4
      CK-7   MEMBER_OMITTED            CK-2 no longer touches M4 at all
  valid Stage A + invalid-JSON M4
      CK-8   MEMBER_SUBSTITUTED        S2; CK-9 is not reached
  malformed sole install record + absent member
      CK-6   MEMBER_SUBSTITUTED        the record is validated before members
  malformed sole install record + stale member
      CK-6   MEMBER_SUBSTITUTED        same reason
  M4 semantic mismatch + Stage-A binding mismatch
      CK-9   STAGE_A_BINDING_MISMATCH  CK-9 precedes CK-10
  changed M2/M3 bytes + coordinated record/member mismatch
      CK-7   HISTORICAL_BYTE_MOVED     CK-7 precedes CK-11..CK-13

All six are pinned as fixtures at rows 105, 106(d) and 109, and each row FAILS a
fixture expecting any other code. Checks 13 → 15; codes unchanged at 26, every
one with exactly one owning check.
```

---

## 4. The complete role-import closure

```text
DENOTATION: the modules resident, by direct or transitive module-scope import,
in a ROLE PROCESS at the instant §P1-7.4 A-10 returns, on the pinned build under
the §P1-7.1 launch. Import-time closure of the union of THREE scoped allowlists —
PCS bootstrap (6), role bootstrap (3), generic_harness.py (16 after MS-11.5) —
union of direct sets: 18 names.

CARDINALITY 89.  BUILTIN 29 · FROZEN 13 · EXTENSION 2 · PURE_PYTHON 45.
76 distinct names occur in some transitive_imports and every one is a row, so
MS-4's self-closure rule holds BY THIS VALUE; 39 rows have an empty array.
ALL 267 BOOLEANS ARE false.
CANON length 20534; sha256 aa974e0c…20ee. The PRIMARY check is a direct
comparison with the MS-11.1 literal; length and digest are corroboration.

THE FOURTEEN CONFIRMED BOOTSTRAP ROWS ARE PRESERVED EXACTLY — verified
mechanically, kind and array element for element, against the values the X line
reproduced from scratch:
  _abc _collections_abc _signal _socket _stat abc fcntl genericpath os posix
  posixpath stat sys time

AUDIT METHOD — three mutually independent derivations that agree, none of which
imports, executes or compiles any Philosophia production module:
  (a) RESIDENCY under the exact production isolation flags with an empty
      environment;
  (b) STATIC CODE-OBJECT PARSE of every module-scope IMPORT_NAME, its
      relative-import level and its fromlist, read from the code object ACTUALLY
      LOADED, not descending into function, method or class bodies;
  (c) RUNTIME DIFFERENTIAL for the booleans — NO SIGNAL DISPOSITION CHANGED,
      THREAD FRAMES 1 BEFORE AND 1 AFTER, NO TRACE OR PROFILE FUNCTION
      INSTALLED; and a module-level effect-name scan across all 89 top-level code
      objects returned ZERO HITS.

SIX UNEXECUTED MODULE-SCOPE BRANCHES, each with its reason: os→nt and os→ntpath
(Windows branch not taken; ntpath is a row only because pathlib imports it
unconditionally); ntpath→nt/_winapi; _frozen_importlib_external→nt/winreg;
abc→_py_abc (the _abc try succeeds); hashlib→logging (an except-ValueError
handler not taken).

THREE NORMALIZATIONS, and only three: three ALIAS entries (os.path is posixpath,
importlib._bootstrap is _frozen_importlib, importlib._bootstrap_external is
_frozen_importlib_external — canonical name is the module's own spec name, which
is why _collections_abc is a row under that name despite its rebound __name__);
two PSEUDO-MODULE entries (typing.io and typing.re are deprecated class objects,
not modules); and the six unexecuted branches above.

__future__ IS ROW 1. A `from __future__ import` statement is BOTH a compiler
directive AND a real runtime import of the ordinary module __future__; the
directive it also carries has no import-time effect.

TWO DISCLOSURES, RECORDED IN THE GOVERNING BYTES:
  1. ABC virtual-subclass registration at module scope in _collections_abc, io,
     collections, encodings, pathlib and weakref is bookkeeping inside those
     modules' own class objects — not at-fork, not atexit, not a handler.
  2. _thread is a row, reached from functools and reprlib, AND is resident in the
     interpreter's own start-up module table before any contract import runs.
     §P1-3.2's rationale sentence for excluding signal ("its import closure pulls
     functools and hence _thread") is FACTUALLY OBSOLETE AS A REASON. THE RULE IS
     UNCHANGED AND NOT WEAKENED — none of the forbidden names is in any
     allowlist. Test row 13 is clarified accordingly: its "absent from the
     closure" is about the PCS root's import-edge closure, not process residency,
     and a fixture asserting _thread is absent from a live PCS process now FAILS
     that row.
```

---

## 5. The scoped-allowlist reduction, and its proof of scientific inertness

```text
THE CHANGE: §P1-3.2's scoped entry for src/philosophia/officina/generic_harness.py
loses EXACTLY ONE NAME, subprocess. Seventeen becomes sixteen:
    __future__ ast dataclasses datetime enum fcntl hashlib hmac json os
    pathlib re time typing weakref _socket

WHY IT IS NECESSARY. With subprocess present the role closure additionally
contains subprocess, threading, signal, select, selectors, _posixsubprocess,
locale and _locale. FOUR OF THOSE — threading, signal, select, selectors — are
named by §P1-3.2 ITSELF as permitted in no file. AND threading's MODULE-LEVEL
code CALLS os.register_at_fork, so importing it REGISTERS AN AT-FORK CALLBACK in
every role process including the WATCHDOG — the precise property §P1-3.3's audit
column exists to police.

WHY IT IS NOT A NEW AUTHOR DECISION — three operative rules already in these
governing bytes forbid subprocess in that file:
    S-12 of §P1-14.6 CHANGE 3;
    test 8 of §P1-15;
    the future-edit surface row for that path.
An allowlist may not authorize an import no conforming build may perform.

WHAT IT DOES NOT TOUCH: the nineteen-member GLOBAL DEFAULT (unchanged, still
contains subprocess, so activate_t.py and verify_officina_active.py are
unaffected); BOTH bootstrap scoped entries (unchanged); every other allowlist,
root and rule.

PROOF THAT NO SIGNED SCIENTIFIC CELL MOVES:
  NOT IN THE SIGNED CHAIN. §P1-3.2 is a section of the P1 composite, which is NOT
    YET ACCEPTED. The accepted generic-harness chain, the harness signature and
    batch-settlement v1.1.1 — the seven M3 members — contain no import allowlist
    for generic_harness.py and are not edited by one byte. §A0.1's chain list is
    unchanged and every M3 digest is unchanged.
  NOT A SCIENTIFIC CELL. It adds, removes and renames no watchdog option, no
    per-option or common amendment token, no treatment, no evidence class, no
    covariate, no endpoint, no qualification input, no comparison input, no Q
    fact and no C fact. It enters no acceptance predicate. §A5's ten conjuncts,
    §A4's and §A6's schemas and key sets, and §A7's state machine are unchanged.
  OPTION-INDEPENDENT. Identical under W-A and W-B; no variant block mentions it;
    all 20 variant-bearing composite lines are byte-identical to v1.7's.
  OPENS NO AUTHOR CELL. Both open cells are unchanged in number, statement and
    status; no third is created; the reduction was DETERMINED, not chosen.
  REMOVES NO PERMITTED CAPABILITY. §P1-7.1 launches through the bound
    _posix_spawn primitive; S-11 fixes its argument shape; S-12 already forbids
    subprocess on every path of that file.
```

---

## 6. The complete graph, including `B14`

```text
  install record  --digest-->  each of the 65 members (2/51/7/1/1/2/1)
  M4 manifest     --digest-->  the M1 composite, by p1_composite_sha256
                  --digest-->  the M1 amendment, by peer_amendment_sha256
                  --digest-->  the five production roots
                  --digest-->  the three composite region digests and H_FILE
                  --path+digest-->  the three pre-selection inputs
                  --path+digest+key id-->  Stage A
  Stage A         --path+digest-->  the pre-selection packet
                  --path+digest-->  the pre-selection amendment
                  --path+digest-->  the pre-selection composite
                  --key pin-->  the one key under which Stage B verifies
  M1 amendment    --anchor line digest-->  the pre-selection composite bytes
  M7 attestation  --digest-->  M5
                  --digest-->  each of the two M6 modules
                  --digest-->  the M6 canonical bundle digest
                  --assertion-->  that the matrix ran and rows 92..115 passed
  Stage B         --path+digest+key id-->  Stage A
                  --selected_option_token equality (B14)-->  Stage A   ← ADDED
                  --id+path+count-->  the record and the member set
                  --digest-->  the two M1 members
  detached sig    --Ed25519-->  the exact canonical Stage-B bytes

RE-DERIVED over every relation bearing a PATH, DIGEST, ID, SIGNATURE, OPTION
TOKEN, KEY or KEY ID, MEMBER COUNT or ASSERTION. Version 1.4 derived over
digest-, path- and signature-bearing fields only, which is exactly how an
option-bearing relation escaped it; widening the derivation closes the CLASS of
error, not only the instance. NO FURTHER OMISSION FOUND.
A9's intra-object option pairing inside Stage A is named as deliberately NOT an
edge, so its absence cannot be mistaken for a second omission.
PRESERVED: no object attests itself; redundant inbound edges are intentional;
NO UNIQUENESS OF ATTESTER AND NO UNIQUENESS OF EXTERNAL ATTESTER IS CLAIMED, and
row 115 still fails any fixture asserting either.
```

---

## 7. Residuals, and proof that nothing moved

```text
RESIDUAL 1 — UNCHANGED AND ACCEPTED. TR-2(a) full-chain substitution at or
  before Stage-A creation, and TR-2(b) complete coherent rollback at any later
  time. NEITHER IS NARROWED BY v2.8.
RESIDUAL 2 — CARRIED FORWARD AND ACCEPTED BY THE Y LINE. The pre-selection
  composite digest cannot be recomputed after OR-4 and is anchored to the §A0.4
  line of the M1 amendment. Honest, acyclic, and not freshness.
RESIDUAL 3 — DISCLOSED AND ENLARGED. MS-11.1 is now an EIGHTY-NINE-ROW factual
  claim about a software artifact, six times the size of the value the X line
  reproduced. It is the single most falsifiable thing in this pair.
RESIDUAL 4 — NEW, AND STATED. _thread is resident in every process of this
  contract before any contract import runs, and no allowlist choice can change
  that. Its booleans are false and the thread-frame count is measured at 1
  before and 1 after, but the RESIDENCY is a fact the bytes now record rather
  than a property the bytes control.
RESIDUAL 5 — CARRIED FORWARD. The A3 same-UID procedural residual and the
  doubly-detached-descendant residual.
RESIDUAL 6 — CARRIED FORWARD. XS-1's later combined binding.

NOTHING MOVED:
  W-A/W-B — all 20 variant-bearing composite lines BYTE-IDENTICAL to v1.7
    (extracted-line SHA-256 ce1463c0ab88952b88d996be4e8f2c64d800a07722e53cb4bb26e2c125507302
    for both files); markers 13/13 whole-file and 10/10 body; neither selected;
    W-B still only recommended on the same five criteria.
  BEHAVIOURAL SURFACE — the amendment's §A1 through §A8 differ from v1.4 by
    EXACTLY ONE LINE, the composite cross-reference v1.7 → v1.8.
  NO KEY, ENTROPY OR ARTIFACT — successor/officina/runtime_control and
    successor/officina/authorization do not exist; no Stage A, Stage B,
    signature, M4, M7 or install record exists.
  NO CODE, TEST OR UNTRACKED FILE TOUCHED — verification.py byte-unchanged;
    the two M6 test modules do not exist; no test was run; the untracked
    generic_harness.py was neither read for behaviour, adopted nor edited.
  NO PRODUCTION MODULE IMPORTED, EXECUTED OR COMPILED by the audit; three of the
    five production roots do not exist as tracked files.
  ROLLBACK SWEEP — across all three new files, every occurrence of "undetected",
    "unnoticed" and "without detection" is an explicit WITHDRAWAL; zero surviving
    positive detection, rollback-resistance, freshness, monotonicity, recency or
    external-custody claims.
  SCIENTIFIC STATE — T = NOT_ACTIVATED; programme claim OPEN; watchdog-freeze
    cell NOT SELECTED; identity cell SELECTED as external author state only;
    P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 NOT ACCEPTED under that or any
    other name.
  HISTORY — all six inputs recompute to their recorded digests. The only files
    this round added are the three governing outputs and this closure. NOTHING
    WAS COMMITTED.

RECOMPUTED NUMERICS, none copied from v2.7:
  236 governing loci = 182 (file 1) + 54 (file 2); 152 tagged rules
  (82 amendment families + 70 joint families); 65 members = 2+51+7+1+1+2+1;
  21 disjoint class pairs; 58 matching M2+M3 digests; 59 provenance rows;
  26 failure codes; 15 checks; 24 test rows 92..115; 89 closure rows;
  16-name generic_harness scoped allowlist. Delta from 233 is +3 (CK +2, N +1).
```

---

## 8. The bounded confirmation questions

### 8.1 For the independent X line — yes/no

The reviewer must not have authored v2.3 through v2.8. Recompute every claim
from the governing bytes; treat this closure as adversarial context only.

```text
X1.  Do the three outputs and six inputs recompute to §1.1/§1.2, is the joint
     block byte-identical in both governing files at 8dd14435…, and does the
     §A0.4 anchor have cardinality exactly one with a value equal to the
     composite's H_FILE, with zero lines matching the retired V2_7 token?
                                                                     YES / NO
X2.  Is MS-11.1's eighty-nine-row value FACTUALLY CORRECT — every module, every
     kind, every transitive_imports array and all 267 booleans — for the
     at-import closure of the eighteen union allowlist names on CPython 3.12.3
     x86_64 Linux under -I -S -E -P with no -X option, derived WITHOUT importing
     or executing any Philosophia production module?                 YES / NO
X3.  Are the fourteen bootstrap rows you reproduced against v2.7 preserved
     BYTE-IDENTICALLY in kind and transitive_imports?                YES / NO
X4.  Does CANON of the value have length 20534 and SHA-256 aa974e0c…20ee, and
     does the value satisfy MS-4's sort, distinctness and self-closure rules?
                                                                     YES / NO
X5.  Are MS-11.3's six unexecuted branches, three alias normalizations and two
     pseudo-module exclusions each correct and collectively exhaustive?
                                                                     YES / NO
X6.  Is the MS-11.5 finding correct — that `threading`, reached only through
     `subprocess`, CALLS `os.register_at_fork` at module scope, and that after
     the reduction NO row starts a task, registers at fork or installs a handler?
                                                                     YES / NO
X7.  Is VP-4 a genuine TOPOLOGICAL order — is there any check whose predicate
     reads an object that no earlier check has proved to exist, parse, be an
     object, and carry a value of the stated type?  TOPOLOGICAL YES / NO ;
                                                    COUNTEREXAMPLE FOUND YES / NO
X8.  Can you construct ANY byte state, single- or multi-fault, for which two
     conforming implementations following VP-3 and VP-4 return different first
     codes?                                                          YES / NO
                                                  (a YES here is a BLOCKING find)
X9.  Is IR-4's graph complete under its own widened derivation rule, and can you
     find any further omitted directed relation?    COMPLETE YES / NO ;
                                                    FURTHER OMISSION FOUND YES / NO
X10. Do the recomputed counts hold: 236 = 182 + 54; 152 tagged rules; 65 members;
     58 M2+M3 digests; 59 provenance rows; 26 codes; 15 checks; 24 test rows;
     89 closure rows; 16-name scoped allowlist?                      YES / NO
X11. Is every item you confirmed in v2.7 still present and unweakened — TS-2A
     plus TS-2B with no clause removed, TS-5 B1..B18, MS-10, CK-4's enumeration
     from MS-1..MS-7 alone, TS-4's wire format, TR-1's non-circularity, the
     §A0.4 scheme, and the three rollback qualifiers?                YES / NO
X12. Does anything in v2.8 create or authorize a key, entropy draw, artifact,
     implementation, test run, install, activation or claim movement, or open a
     new author cell?                                                YES / NO
                                                  (a YES here is a BLOCKING find)
```

### 8.2 For the independent Y line — yes/no

```text
Y1.  Is Y27-B1(a) closed — does the TS-2A/TS-2B split, together with VP-1's
     S1..S5 prerequisite sub-phase and VP-4's topological order, mean that no
     clause can read an absent, invalid-JSON, non-object, missing-key or wrongly
     typed M4, and that each of those five states has one earlier owner and one
     code?                                                           YES / NO
Y2.  Is Y27-B1(b) closed — is the install record's structural position now
     literal (locate at CK-5, structurally validate at CK-6, members at CK-7 and
     CK-8, semantic from CK-9), and does a malformed sole record with an absent
     or stale member have exactly one first code?                    YES / NO
Y3.  Is Y27-B1(c) closed — does every field AND every cross-object relation have
     exactly one earliest owner, with CK-10 no longer claiming TS-2B's relations
     and the M2/M3 relation evaluated once?                          YES / NO
Y4.  Is Y27-B2 closed, AND IS THE MS-11.5 REDUCTION LEGITIMATE? Specifically: is
     the removal of `subprocess` from generic_harness.py's scoped allowlist
     DETERMINED by S-12, test 8 and the future-edit surface rather than a new
     author decision; does it move no signed scientific cell (§5); and was
     emitting BLOCKED instead the better call? **THIS IS THE ROUND'S LARGEST
     JUDGMENT CALL AND IS PUT TO YOU AS A QUESTION, NOT PRESENTED AS SETTLED.**
                                        CLOSED YES / NO ; REDUCTION LEGITIMATE
                                        YES / NO ; BLOCKED WAS BETTER YES / NO
Y5.  Is the denotation now accurate — role closure covering all three scoped
     allowlists, with activate_t.py and verify_officina_active.py excluded on
     the stated ground that no process this contract creates ever imports them?
                                                                     YES / NO
Y6.  Is Y27-B3 closed — is the B14 edge present at IR-4, §P1-14.5, packet §3 and
     row 115, and is the widened derivation rule adequate to prevent another
     relation class from escaping?                                   YES / NO
Y7.  Is Y27-R corrected everywhere — two tracked roots, three absent, the
     untracked file not adopted, and MS-11.1 described as a PROSPECTIVE
     CONFORMANCE CONSTRAINT and not as evidence of an implementation?
                                                                     YES / NO
Y8.  Is the _thread disclosure honest and adequate — the rule preserved, the
     rationale corrected, test row 13 clarified rather than weakened — or does
     it conceal a residual you consider blocking?    ADEQUATE YES / NO
Y9.  Are the accepted boundaries preserved WITHOUT NARROWING — §A0.4, the
     fourteen confirmed rows, the M4 anchors, the three rollback qualifiers,
     FS-1..FS-5, TR-2(a)/(b), row 106(i)'s expected PASS, W-A/W-B symmetry and
     the identity boundary?                                          YES / NO
Y10. Does anything in v2.8 move the watchdog cell, the identity cell, the
     recommendation, T, the programme claim, or any scientific or authorization
     boundary?                                                       YES / NO
                                                  (a YES here is a BLOCKING find)
```

---

## 9. The next boundary

```text
THE NEXT PERMISSIBLE ACTION IS A BOUNDED INDEPENDENT X-LINE AND Y-LINE
CONFIRMATION ROUND ON THESE EXACT BYTES, BY REVIEWERS THAT DID NOT AUTHOR v2.3
THROUGH v2.8. Nothing else.

NOT AUTHORIZED BY THIS ROUND OR BY THIS CLOSURE: the author's watchdog option
selection; any key generation or entropy draw; Stage A or Stage B; the detached
signature; the M4 manifest; the M7 attestation; the install record; any
implementation, code edit, verifier edit or manifest edit; any test run; any
install; any production entry; any T activation; any candidate, trajectory,
datum, outcome, Proof or claim movement.

T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = NOT SELECTED
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, external author state only
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
```
