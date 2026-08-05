# Final Y-line confirmation — Officina P1 watchdog v2.8

**Reviewer:** GPT-5.6 Sol, independent governance/statistical Y line

**Date:** 2026-08-05

**Review target:** exact commit
`dba33e66f8f999c376eb17ca4587a6714c891a6e`
(`Repair watchdog role import closure in v2.8`)

**Authority used:** the four byte-pinned primary inputs, the governing v2.7 Y
review, and direct reconstruction from the governing bytes and the pinned
CPython build. The v2.7 X review and the Opus 5 v2.8 closure were context only.
The author closure was not treated as authority.

## Verdict

```text
REVISE_OFFICINA_P1_WATCHDOG_V2_8
```

The `TS-2A`/`TS-2B` split and the explicit record-before-members order repair
the six examples named by the packet, but Y27-B1 is not closed globally. The
two governing files retain three conflicts that defeat the claimed unique
first-code partition: `IR-3` assigns the install-record ID equalities to
`CK-8`/`CK-9` while the operative table and checks assign both to `CK-12`; row
111 gives a missing `stage_a_*` or `pre_selection_*` M4 key both the structural
`CK-8` code and a later `STAGE_A_*` code; and `CK-13` has three overlapping
reason-code classes with no within-check order for adversarial combinations.

The new 89-row literal is factually correct for the audited standard-library
allowlist union on the pinned interpreter, and removing `subprocess` is a
legitimate consistency repair within the already stated P1 rules. It still is
not the complete import surface of `A-10`: normal Python package import first
executes `philosophia/__init__.py`, `philosophia/officina/__init__.py`, and the
latter's `canonical.py` and `interlock.py` imports. Those project modules are
neither rows, production roots, members nor digest-bound dependencies. Their
current bytes are benign evidence about the reviewed commit, but the final gate
does not bind them and the prospective contract does not constrain their
import-time effects.

The specific B14 edge is now present everywhere requested. The wider claim
that `IR-4` is complete is nevertheless not established by a derivation that
omits `TS-2` and `TS-5`, where additional cross-object equalities are defined.

This verdict authorizes nothing.

## Custody, bytes and repository topology

The live branch had advanced beyond the target commit and the worktree already
contained unrelated modified and untracked files. I did not check out, edit,
stage, import, execute, or use the untracked `generic_harness.py` as evidence.
The four primary files in the worktree are byte-identical to the target commit
and recompute to:

```text
5666d2bf9cee3c4404cc1f26ac13050a40403af9b4631fa774a1bfacbe481ca8  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_8_CORRECTION.md
28b57c47f89f775199095717111e37a4e588628aa64b2801812f30814711efd4  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md
6b867790707ae7999b31c1ad3dd56a1d4b195efd8f7a8b2bda4c2b065a352176  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
```

The joint install/authorization block is byte-identical in the amendment and
composite, 2,108 lines, SHA-256
`8dd14435128ada01a179da5fa833a065d51768f1cbba0df50456330a5361c2c1` under
the author's stated form that omits the final linefeed. The composite region
digests independently recompute to:

```text
H_FILE       6b867790707ae7999b31c1ad3dd56a1d4b195efd8f7a8b2bda4c2b065a352176
H_BODY       c18225d299afde0989eee8d5069aef219f4dcecf266a69de4e6c2d096a19f707
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  bfd1f339522e5dfb51b571e6b340927843563b8118b18a0689637397530f42d3
```

The amendment has exactly one strict v2.8 A0.4 anchor line, its value equals
`H_FILE`, and no strict retired-v2.7 anchor line exists. The 20 variant-bearing
composite lines are byte-identical to v1.7. The exact commit contains two of the
five roots as tracked files:

```text
scripts/officina_activate_t.py
scripts/verify_officina_active.py
```

Both bootstraps are absent. `generic_harness.py` is also absent as a tracked
file; a same-named unrelated untracked worktree file supplies no evidence.
Thus the precise statement is two tracked roots and three absent tracked roots,
with the three comprising the two bootstraps and `generic_harness.py`.
`MS-11.6` correctly calls its literal a prospective conformance constraint and
not implementation evidence.

## Findings by severity

### Blocking 1 — Y27-B1 is not fully closed

The intended topological order is materially better:

```text
CK-2  Stage A alone
CK-3  Stage B self-contained portion
CK-5  locate the sole record
CK-6  structurally validate the record
CK-7  establish member existence and recompute digests
CK-8  structurally validate M4, then M7
CK-9  compare Stage A with M4
CK-10 M4 semantics
CK-11..CK-13 record/member relations
CK-14 Stage B cross-object relations
CK-15 M7 semantics
```

Accordingly, each of the six mandated examples has the packet's intended first
code: absent M4 at `CK-7`; invalid-JSON M4 at `CK-8`; malformed record plus
absent or stale member at `CK-6`; Stage-A binding mismatch before M4 semantics
at `CK-9`; and changed M2/M3 bytes before a coordinated record mismatch at
`CK-7`.

That does not make the order total for all byte states:

1. In both governing copies, `IR-3` says the record's two ID equalities are
   owned by `CK-8` and `CK-9`. `VP-2`, `VP-3`, `CK-12`, row 105, row 106(e),
   and the local explanation in `CK-6` instead put both at `CK-12`. At `CK-8`
   the `CK-11` recomputation does not yet exist, so the stale assignment is not
   merely a wrong label; a literal implementation has either an undefined
   prerequisite or a different first position.
2. Row 111 first says every missing M4 key is structural and refused at `CK-8`
   with `MEMBER_SUBSTITUTED`. It then says an omitted `stage_a_*` or
   `pre_selection_*` key is additionally refused with
   `STAGE_A_BINDING_MISMATCH` or `STAGE_A_PRESELECTION_MISMATCH`. `TS-2B` and
   `VP-4` correctly prohibit reaching the latter read, but the test matrix
   independently requires it. The same missing-key state therefore has two
   normative answers.
3. `CK-13` assigns `MEMBER_EXTRA`, `MEMBER_STALE`, and `MEMBER_SUBSTITUTED`
   without an internal predicate order. A structurally valid 65-entry record
   can carry an unenumerated path in one entry and a wrong recorded digest in
   another. One implementation may detect the extra/path mismatch first;
   another may detect the stale digest first. Even one replacement path is
   simultaneously an entry outside the enumerated set and a path mismatch,
   while the text maps those descriptions to different codes.
4. `VP-2` says no structural predicate is re-evaluated semantically, but
   `CK-10` says it evaluates all eleven non-Stage-A M4 rows, expressly including
   `schema`, `version`, and `created_utc` already settled structurally. Those
   three cannot become a later first failure after `CK-8`, but their inclusion
   refutes the claimed exactly-once ownership partition.

The intended `CK-7`/`CK-13` split itself is genuine: `CK-7` compares actual
M2/M3 bytes with the immutable digests in `MS-2`/`MS-3`, while `CK-13` compares
the record's recorded member digest with the actual digest already recomputed
at `CK-7`. Unchanged M2/M3 bytes plus a wrong record digest therefore reach
`MEMBER_STALE`; changed M2/M3 bytes fail earlier with
`HISTORICAL_BYTE_MOVED`. The defect is not that these relations are identical;
it is the stale contrary ownership text and the unresolved ordering among the
different mismatches that can coexist inside `CK-13`.

The needed repair is small but normative: correct `IR-3`; delete the second
missing-key answer in row 111; state a disjoint classification and literal
sub-order inside `CK-13`, with adversarial fixtures; and make `CK-10`'s range
the actual semantic relations rather than structurally settled rows.

### Blocking 2 — the denotation still omits part of the actual A-10 import surface

The v2.8 change correctly recognizes that `generic_harness.py` is role code and
correctly includes the standard-library closure of all three scoped import
sets. But this is not everything Python executes for:

```text
import philosophia.officina.generic_harness
```

In a fresh role process, Python first loads the parent packages. At the exact
commit, that executes:

```text
src/philosophia/__init__.py
src/philosophia/officina/__init__.py
src/philosophia/officina/canonical.py
src/philosophia/officina/interlock.py
```

The Officina package initializer imports `canonical` and `interlock`; those are
not hypothetical import mechanics. None of these four paths is one of the five
production roots, an M1..M7 member, a row in the 89-module value, or a path
bound by `root_source_sha256`. `A-11` identity-checks only the imported
`generic_harness` file. The future-edit table's prose that everything else does
not change supplies no path to `CK-4` or `G-11`.

The current four files do not themselves reproduce the `threading` at-fork
effect, but current benign content is not a prospective enforcement argument.
Their unbound bytes can change while all five root digests, the 89-row literal,
the member set, Stage B, and the sole record still agree. They can then perform
role import-time effects before `A-10` returns, precisely where the repair says
such effects matter and where `P-c`, `P-d`, and `P-g` are not repeated.

Activation and standalone verification remain properly outside this role
denotation: no process created by this contract imports either script. A
prospective literal is also legitimate despite the three future roots, so long
as it is described as a constraint and later tied to exact root bytes. Neither
point cures the parent-package gap.

The smallest repair is to make every project module necessarily executed by
the A-10 import a digest-bound production dependency with the same applicable
static/effect rules, or to use an import construction that demonstrably avoids
executing unbound parent-package code. The literal's name and prose should then
distinguish project-module coverage from the pinned standard-library closure.

### Major — B14 is added, but whole-graph completeness remains overstated

The narrow Y27-B3 repair is present at all four requested surfaces:

- `IR-4` includes `Stage B --selected_option_token equality (B14)--> Stage A`;
- composite `§P1-14.5` names it;
- packet §3 names it; and
- row 115 positively requires it and rejects a fixture omitting it.

No self-attestation or attester-uniqueness claim is reintroduced.

The wider derivation rule still does not justify “complete.” It says it derives
from `MS-4`, `MS-7`, `IR-1`, `IR-3`, `TS-1`, `TS-3`, and `TS-4`; it does not
include `TS-2` or `TS-5`, even though those sections define cross-object
equalities. For example, `B18` directly requires Stage B's
`governing_amendment_sha256` also to equal M4's
`peer_amendment_sha256`, but the graph lists Stage B's digest edge to the M1
amendment and no Stage-B-to-M4 equality edge. The A15/A16 comparisons between
Stage A and M4 are likewise represented as parallel bindings to common inputs,
not named as the direct equality relations the verifier evaluates. `IR-3` also
defines the record-ID-to-filename relation, while the displayed graph does not
name that ID/path edge.

Those redundancies may be deliberately summarized by common-target edges, but
then the graph must define that quotienting rule and narrow “every relation.”
Under the present rule, B14 is closed as an instance while the completeness
claim is not.

## Allowlist reduction — legitimate consistency repair, with one qualification

### Factual software result

On the exact pinned interpreter
`CPython 3.12.3 (main, Jun 19 2026, 12:46:00) [GCC 13.3.0]`, under
`-I -S -E -P` and an empty environment, independent import measurement gives:

```text
reduced union: 89 normalized resident modules
kinds:         29 BUILTIN, 13 FROZEN, 2 EXTENSION, 45 PURE_PYTHON
with subprocess: 97 normalized resident modules
delta:         _locale, _posixsubprocess, locale, select, selectors,
               signal, subprocess, threading
```

The reduced literal is sorted, distinct and self-closed; it has 76 referenced
names and 39 empty import arrays. Its canonical form is 20,534 bytes and hashes
to `aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee`.
The resident module names and all 89 origin kinds match the literal exactly.

Instrumenting `os.register_at_fork` before the reduced 18-name union produced
zero calls. Importing `subprocess` then produced exactly one call with
`after_in_child`, matching `/usr/lib/python3.12/threading.py`, and the eight
modules above. Thus keeping `subprocess` in the prospective role import surface
would genuinely violate the stated at-fork/forbidden-module invariant. No other
name in the reduced standard-library union recreates that at-fork effect.

This factual result does not cure the separate unbound project-package route.

### Governance judgment

`S-12` is dispositive: before v2.8 it already required `subprocess`, `Popen`,
`fork`, `waitpid`, `kill`, `killpg`, and `system` to appear on no path of
`generic_harness.py`. Test 8 independently forbids the launcher’s fork/Popen/
shell route, and the future-edit surface already requires removal of the
subprocess/fork/wait/kill family. The operative launch route is the bound
`_posix_spawn` primitive. Therefore no implementation conforming to the P1
composite could use the removed name, and its deletion from this one scoped
allowlist changes no P1-admissible implementation, option, acceptance predicate
or scientific cell. I classify the v2.8 reduction itself as a mechanically
required consistency repair, not a new unsigned watchdog choice. `BLOCKED`
would not be the right verdict merely because this reduction was made.

One qualification must remain explicit. The accepted generic-harness v2 chain
does grant a CPU launcher capability using `subprocess` with
`start_new_session=True` and `os.killpg`; it is not accurate to suggest that
the accepted chain never mentions or grants that capability. The capability is
not silently revoked by v2.8: the later P1 architecture had already expressly
replaced that launch route through `S-11`, `S-12`, and `_posix_spawn`. The
documentation should state that sequence directly. The v2.8 allowlist edit is
the bookkeeping consequence of the earlier P1 rescope, not the original source
of the rescope.

## The 89-row value and its limits

Direct value equality plus the length and hash checks honestly prevents M4
from substituting a different standard-library closure while the current M1
bytes remain fixed. It is not a runtime monitor, a proof that future root bytes
exist, or a complete model of every effect of importing Python code.

The three booleans cover the control-relevant effects selected by the contract:
new concurrent execution, at-fork registration, and handler/hook installation.
They do not denote arbitrary module-global mutation, cache or registry changes,
filesystem reads, or later effects when imported callables run. The document
discloses ABC virtual-subclass registration, and other runtime behavior is
intended to be controlled separately by the root AST, primitive and preflight
rules. That division can be coherent only after every project module executed
at A-10 is inside one of those enforced surfaces; currently it is not.

The `_thread` disclosure is accurate. `_thread` is both reached by allowed
imports and resident in the interpreter before contract import; importing it
does not itself start a thread. Row 13 now honestly tests absence from the PCS
root's import-edge closure, not absence from a live process. The rule excluding
the pure-Python `signal` wrapper is preserved. However §P1-3.2 still prints the
old `_thread`-absence rationale and `MS-11.3` later calls that rationale
factually obsolete. That is candid disclosure, but a final repair should
replace the obsolete sentence at its owning locus instead of leaving the
normative explanation contradicted later.

## Preserved boundaries and residuals

Subject to the blockers above, the following v2.7 boundaries are carried
without expansion:

- A0.4 remains an acyclic cross-file integrity commitment, not freshness or
  rollback resistance. Its cardinality and value are correct.
- The fourteen previously confirmed bootstrap rows retain the same kinds and
  transitive-import arrays.
- The manifest's peer-amendment, root, region, pre-selection and Stage-A
  anchors remain present.
- The preamble, G-6 and G-7 retain current-generation, fixed-chain,
  proper-subset qualifiers and point to coherent rollback.
- `FS-1` remains a one-instant final-byte statement. `FS-2` denies historical
  reconstruction and external freshness. `FS-3`..`FS-5` preserve the operator
  obligation, contemporaneous refusal and undiscovered-procedure residual.
- Both `TR-2(a)` full-chain substitution and `TR-2(b)` complete coherent
  rollback remain open. Row 106(i) still expects `PASS` for a fully restored
  generation and fails a fixture that expects refusal.
- No external witness, timestamp authority, monotonic generation counter,
  notary, transparency log, or rollback-resistant custody is introduced.

W-A and W-B remain byte-symmetric and unselected. W-B remains a recommendation
only. Identity Option A remains external author state and is not a member,
install record fact, or scientific fact. The separately required
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` token remains unaccepted, with no
bounded weakening accepted under another name.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = NOT SELECTED
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, external author state only
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
```

No authority or science moved. Nothing in v2.8 creates a key, entropy draw,
Stage A, Stage B, detached signature, M4, M7, install record, implementation,
test execution, install, activation, candidate, trajectory, datum, outcome,
Proof, or programme-claim movement.

## Smallest bounded repair and next boundary

1. Reconcile `IR-3`, row 111, `CK-10`, and `CK-13` with `VP-2`..`VP-4`; add
   missing-key M4 and adversarial multi-fault record fixtures that require one
   literal sub-order and one code.
2. Bind or avoid every parent-package/project module necessarily executed by
   A-10, then redenote and re-audit the role import surface. Do not use the
   unrelated untracked `generic_harness.py` as evidence.
3. Re-derive `IR-4` over the actual verification relations of `TS-2` and
   `TS-5`, or define and consistently apply a narrower graph equivalence rule.
4. Replace the obsolete `signal` rationale at §P1-3.2 and explicitly acknowledge
   that the accepted generic-harness chain had a subprocess launcher which the
   later P1 architecture already superseded.
5. Repeat bounded independent X/Y review on the identical repaired bytes.

The next permissible action is a documentation-only v2.9 (or equivalent)
repair. Kirill's watchdog option choice is not authorized by this review.

No key, Stage A/B artifact, detached signature, manifest, attestation, install
record, code, test, install, activation, or scientific action is authorized.
