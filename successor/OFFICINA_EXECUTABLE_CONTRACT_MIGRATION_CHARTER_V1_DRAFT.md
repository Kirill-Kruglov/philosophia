# Officina executable-contract migration charter v1 (draft)

**Status:** draft. Not accepted. Authorizes nothing until the tokens in §8 are
signed after independent X/Y review of these bytes.

**Purpose.** Replace prose-as-executable-authority with a small
machine-checkable contract, preserving every signed scientific and author
choice, and eliminating the manual generation/provenance drift that has
consumed more than one hundred review/repair iterations.

**Scope boundary.** This charter is a route decision. It creates no code, no
contract, no fixture, no manifest and no test. It does not accept, repair or
supersede any current candidate. It does not move `T`, any `OR` step, or the
programme claim.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

---

## §1. Failure diagnosis

### §1.1 The stopping evidence

Two independent lines reviewed byte-identical inputs and diverged. The X line
(`reviews/fable_officina_p1_wb_v2_15_final_x_confirmation.md`) returned
`0 Major` and confirmed for author acceptance. The Y line
(`reviews/sol_officina_p1_wb_v2_15_final_y_confirmation.md`) returned
`REVISE` on three Major findings.

The divergence is not a disagreement about the machine. Both lines reproduced
every mechanical figure they shared. They reviewed **different surfaces of the
same document**: X reviewed the state machine's semantics by executing it; Y
reviewed the document's testimony about its own provenance and generation. The
artifact conflates those surfaces into one 668,002-byte file, so neither line's
verdict covers what the other checked. That is an architecture defect, not a
clause defect, and no further clause repair can close it.

### §1.2 Defect classification

**Class A — genuinely non-obvious concurrency / state-machine issues.**
Questions about route totality, disjointness, gate ordering, write provenance,
tie-break stability under permutation, and the reachability of fail-closed
branches. Representative live instances: the X line's `X15-M1` (the two clauses
of the enumeration rule `(x4)` disagree on 8 self-contradictory tuples and two
conforming builds would publish different route and write counts, both claiming
conformance) and `X15-M2` (a step's sentence order, read strictly, routes 576
watchdog combinations to a substantively different route than three other
clauses of the same document require).

These are real engineering questions, found by *executing* a model of the prose
rather than reading it. Migration does not make them disappear — it makes them
decidable once, instead of re-argued in prose every generation.

**Class B — predictable generation / provenance / hash drift.** Hand-maintained
member cardinalities, digest tables, path lists, cross-references to generation
numbers, and manually repeated statements of what a document is a replacement
for. Representative live instances: all three Y Major findings. `Y15-M1` (the
current composite's normative preamble still names a retired amendment
generation as a live authority surface). `Y15-M2` (the resolved output carries
two incompatible statements about which generation it replaces). `Y15-M3` (a
live proof sentence names one generation as the transform source while the
transform beside it consumes another).

Every one is a human-typed copy of a fact derivable from bytes. None is a
semantic question. This class is the loop's fuel.

**Class C — scientific or author-choice questions.** Which watchdog
architecture; which process-identity model; whether the bounded identity
weakening is acceptable; frame band, split, orientation estimand; the T
envelope. These are settled by signature and are not engineering defects at
all.

**Class D — defects created by the review artifact architecture itself.** The
largest class, and the one least visible from inside a repair round:

- A single 668 KiB normative document containing its own member manifest, its
  own provenance rows and its own cardinality arithmetic, so any change to any
  member obliges hand edits to several places inside the same file.
- A four-surface live authority set — amendment, composite, post-selection
  binding, implementation handoff — with a hand-written precedence rule between
  them, so the same fact appears up to four times and each copy rots
  independently.
- An eleven-span byte-patch transform (`OR-4`) that is *itself* normative prose,
  whose output — the document that would actually govern — exists nowhere on
  disk and must be reconstructed in each reviewer's memory before review.
- Review effort spent proving that a document's testimony about itself matches
  the document, rather than that a specification matches an implementation.
- A generation-number cascade in which any fix, however local, mints a new
  generation of four documents and invalidates every cross-reference, creating
  fresh Class-B surface at least as fast as repair removes it.

The v2.15 round is the proof: the mechanical figures reproduced exactly, the
transform reproduced byte-exactly, and the round still failed — on three
sentences that testify about generations.

### §1.3 What migration eliminates and what stays real

| Class | After migration |
|---|---|
| **A** | Not eliminated. Converted from prose-interpretation disputes into executable functions with exhaustive enumeration. `X15-M1` and `X15-M2` become impossible *as ambiguities* — a function has one behaviour — but the underlying design decisions must each be made once, deliberately, and are recorded in §3. Residual risk: a wrong decision, correctly implemented. |
| **B** | **Eliminated by construction.** §2 and §6.2 give the argument: the architecture provides no location in which a human may type a derived fact. |
| **C** | Untouched and preserved. Signed choices remain authoritative in their existing signature files. Migration never re-derives, re-opens or re-litigates them. |
| **D** | **Eliminated by construction.** One authoritative representation, one live manifest, no self-reference, no hand-applied transform, no generation cascade for ordinary fixes (§6). |

Migration is justified on Classes B and D — the entire observed content of the
last several rounds — and is honest about Class A, which it makes tractable but
does not solve.

## §2. Authority graph

Acyclic. Edges point from authority to derived. Nothing points back.

```text
  [signed choices]                       existing signature files, unchanged
  successor/*_SIGNATURE.md
         │  (read once, at M1, into the equivalence ledger; never at runtime)
         ▼
  ┌──────────────────────────────────────────────────────────┐
  │ AUTHORITATIVE SOURCE — hand-edited, reviewed             │
  │ successor/officina/contract/                             │
  │   constants.py    typed enums, literals, route names,    │
  │                   token strings, negative boundaries     │
  │   schemas.py      frozen dataclasses + executable        │
  │                   validators, closed key sets            │
  │   machines.py     pure transition functions (KG-2 W0..W8,│
  │                   PCS freeze classifier phases)          │
  │   data/*.json     canonical JSON spec/fixture data       │
  └──────────────────────────────────────────────────────────┘
         │                                    │
         │                                    │
         ▼                                    ▼
  ┌──────────────────────┐          ┌──────────────────────────┐
  │ GENERATOR            │          │ TESTS                    │
  │ tools/officina_      │          │ tests/test_officina_     │
  │   contract/render.py │          │   contract_*.py          │
  └──────────────────────┘          └──────────────────────────┘
         │                                    ▲
         ▼                                    │
  ┌──────────────────────────────────────────────────────────┐
  │ GENERATED — never hand-edited                            │
  │ successor/officina/generated/                            │
  │   CONTRACT.md     human-readable contract                │
  │   MANIFEST.json   the ONE live manifest: path + digest   │
  │                   of each contract/ source file          │
  └──────────────────────────────────────────────────────────┘
         ▲
         │  check-only: regenerate to memory, compare bytes
  ┌──────────────────────────────────────────────────────────┐
  │ VERIFIER  tools/officina_contract/verify.py --check      │
  └──────────────────────────────────────────────────────────┘
```

### §2.1 Structural rules

1. **One authoritative representation per operative fact.** A fact lives in
   exactly one of `constants.py`, `schemas.py`, `machines.py` or `data/`. It
   appears in `CONTRACT.md` only as generator output.
2. **Markdown carries no independent authority.** `CONTRACT.md` is
   documentation. If it disagrees with `contract/`, `contract/` governs and the
   disagreement is a test failure, not a review finding.
3. **Exactly one live manifest.** `MANIFEST.json` covers `contract/**` only. It
   does not cover `generated/**`, does not cover itself, and no second manifest
   is created.
4. **No self-hashes and no fixpoints.** No generated file contains a digest of
   itself or of any other generated file. Digests flow strictly source →
   manifest. Released artifacts may be bound externally: an author signature
   file, which is *not* generated, may carry the digest of `MANIFEST.json`.
   That edge leaves the graph and does not return.
5. **No hand-maintained cardinality.** Every count is `len(...)` over the
   authoritative collection, evaluated by `render.py`. There is no syntactic
   position in the architecture where a human may write a member count.
6. **Historical generations are Git evidence.** Superseded prose lives in
   `successor/archive/` (or in history alone) and is never a member of the live
   contract, never referenced by `MANIFEST.json`, and never an input to any
   cardinality.
7. **Verification compares generated bytes to source.** `verify.py --check`
   re-runs the generator into memory and diffs against `generated/`. It never
   compares a document to its own testimony about itself.

### §2.2 Dependency policy — recommendation

**Recommended: stdlib only. No new dependency.**

Justification. The repository already has the primitives the contract needs:
`canonical_json` / `sha256_*` / `atomic_replace` in
`src/philosophia/officina/canonical.py`, frozen dataclasses throughout
`src/philosophia/officina/`, and pytest. Exhaustive enumeration is cheap — the X
line enumerated 110,592 combinations twice, in two independent pure-Python
implementations, inside one review. A schema framework would add an unreviewed
third-party semantic layer to the one part of the system that must be auditable
by reading it.

Separation of testing styles (§4) is the only place a dependency is arguable:
generative property testing of the byte parser and canonicalizer is where
Hypothesis earns its keep. A pinned-seed stdlib `random` corpus plus a
checked-in failing-case corpus covers the same ground with reproducible bytes
and no new supply-chain surface. If the author prefers Hypothesis it is
acceptable as **dev-extra only, test-only, never imported by `contract/` or
`tools/`**; the contract must stay importable with zero non-stdlib
dependencies. §8 carries the choice; the default is stdlib.

---

## §3. Semantic extraction boundary

A **closed** inventory. Each item is extracted as *meaning*, from the signed
sources and from the current candidate's operative clauses — never by copying
prose, history, member rows, digest tables or review chronology. Anything not on
this list is out of scope for M1 and requires a charter amendment to add.

| # | Invariant | Signed / operative source |
|---|---|---|
| I-1 | Watchdog is sensor-only: holds the two sealed liveness pipes, no freeze-request socket, descriptor slot 6 closed; on update-pipe EOF it sends, writes, freezes and signals nothing and exits. | `OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md` |
| I-2 | Sole process-control authority: one constructed PCS holds every PID and all process-control authority; the contaminated supervisor holds opaque handles only and calls no `fork`/`Popen`/`waitpid`/`kill`/`killpg` on a result-bearing path. | `OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md` |
| I-3 | PCS residency: PCS loss is unrecoverable whole-generation process invalidity; no new PCS adopts a live generation. | same as I-2 |
| I-4 | Process identity Option A, observation-only: the attested pid/pgid pair is an observation returned only in the signed `AWAIT_STOP`/`STOPPED` response; `handle_id` is the only addressable process name; the pair may not select, signal, wait for, route to or allocate for a process. | `OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md` |
| I-5 | The bounded identity weakening `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` is **not accepted** and must be represented as an explicitly unaccepted, non-operative token. | I-4's signature; v2.15 §8.3 |
| I-6 | Freeze classification and group stops are executed by the PCS alone, record-first, under the signed classifier rules. | I-1's signature |
| I-7 | At-most-once group population and at-most-once write: exactly one route performs the one write; no second write in any evaluation; no write of unknown provenance; no write on any other route. | current candidate's `KG-2` machine |
| I-8 | Fail-closed transitions: every structurally violating or undeterminable state has exactly one named continuation and takes no write. | current candidate's `KG-2` machine |
| I-9 | Protected-group safety: a protected/forbidden target masks lower-precedence terminals and emits zero signals; phase precedence dominates within-phase tie-break. | current candidate's classifier phases |
| I-10 | Stable tie-break: within a phase, the selected site is the entry of least `handle_id`; no answer, terminal, qualifier, token or recorded site is permutation-dependent. | current candidate's classifier |
| I-11 | T envelope and accounting: `E1=168` aggregate device hours, `E2=12` canonical candidates, `E3` review at the first of 48 calendar hours or 40 device hours; pause/resume charges through the boundary and resets no clock. | `AUTHOR_SELECTIONS_V1_SIGNATURE.md`; `successor/officina/T_ENVELOPE.json` |
| I-12 | Activation interlocks: `T = NOT_ACTIVATED`; quarantine is a fail-closed realpath-resolved allowlist rooted at `successor/officina`; runtime inheritance forbidden. | `successor/officina/{PATH_POLICY,LINEAGE,T_ENVELOPE}.json` |
| I-13 | Separation of planes: identity fields, their carriers and integrity values are control-plane facts, never scientific data, evidence, endpoints, qualification inputs, Q/C facts, outcomes or Proof. | I-4's signature; `CHARTER_SIGNATURE.md` |
| I-14 | `OR` state: `OR-2` complete; `OR-3`..`OR-11` not authorized. Represented as data, with the authorization boundary as an executable predicate. | v2.15 §10; I-1's signature |
| I-15 | Negative authorization boundaries, as a closed enumerated set: no inactive-scaffold authorization, no runtime implementation authorization, no one-shot atomic-handoff authorization, no key, entropy, seed, Stage A/B, detached signature, attestation, install record, capability, world, learner, candidate, spend, datum, outcome, Proof or claim movement. | v2.15 §10 |

### §3.1 Equivalence ledger — one time only

M1 produces `successor/officina/contract/EQUIVALENCE_LEDGER.md` mapping each of
I-1..I-15 to (a) the signed or operative source by path and section, and (b) the
executable test that pins it. Written once, reviewed at M4, then **archival**:
not a live runtime authority, not a member of `MANIFEST.json`, never
regenerated, never an input to any cardinality. After M5 it moves to
`successor/archive/`. Its purpose is to let one reviewer answer "was anything
lost?" exactly once, rather than to create a sixteenth surface that must stay in
sync forever.

---

## §4. Verification strategy

### §4.1 Exhaustive enumeration and model checking — finite machines

For `machines.py`: enumerate the complete declared cross-product of dimension
value sets (the current product is 110,592) and assert, over every combination:
exactly one route applies; no combination has zero routes; no combination has
two or more; the ordered machine and the row-predicate form agree on every
combination; the write count equals the size of the conjunction that licenses
it; no observation and no write precedes its authority gate.

The two-implementation discipline the X line used is retained and made
structural: the ordered machine and the guard-row predicates are both generated
*from the same source declaration* and cross-checked, so agreement is a test,
not a coincidence of two transcriptions.

Classifier phases: enumerate every fixture under every permutation and assert
the number of distinct answers is 1, per fixture, for terminal, qualifier,
per-entry token and recorded site.

### §4.2 Generative property and mutation testing — byte surfaces

Applied **only** to the parser, the canonicalizer and the framing code — the
surfaces whose input domain is unbounded:

- round-trip: `parse(render(x)) == x` over generated structures;
- canonicalization idempotence and byte-stability: `canon(canon(b)) == canon(b)`;
- rejection: every mutation of a valid frame either parses to a value that
  re-renders identically, or is rejected — never silently accepted as different;
- mutation testing of the validators: a mutant that weakens any closed key set
  or any bound must fail at least one test.

Deterministic by default: pinned seed, checked-in corpus of previously failing
inputs. This is kept strictly separate from §4.1 — finite machines are never
sampled, and byte surfaces are never claimed exhaustive.

### §4.3 Golden fixtures generated from source

`generated/**` is the golden fixture. `verify.py --check` regenerates into
memory and refuses on any byte difference. A test invokes it. Consequence: a
hand edit to `CONTRACT.md` or `MANIFEST.json` fails the suite, and a source
change that the author forgot to render fails the suite. There is no third
outcome.

### §4.4 Import and call-surface checks

Retained where the invariant is genuinely about *absence* of a capability:
AST assertions that `contract/` imports nothing outside the stdlib allowlist,
and that modules bound to the contaminated-supervisor role contain no call to
the forbidden process primitives (I-2) — the only mechanical enforcement of a
negative.

### §4.5 Crash-cut and atomicity — at real persistence boundaries only

Where the contract asserts durability (ledger append, checkpoint, manifest
write), test at the actual boundary: write, interrupt between the rename and the
directory fsync, reopen, assert the invariant. The repository's existing
`atomic_create`/`atomic_replace`/`fsync_directory` are the units under test.
No simulated filesystem stands in for this.

### §4.6 Minimal disposable integration smoke

One test that constructs the contract objects, renders, verifies and tears down
in a temporary directory, touching no real T world, drawing no entropy, spending
no E1/E2/E3 and creating no runtime artifact. It catches wiring breakage, not
behaviour.

### §4.7 What tests cannot prove, and how it stays bounded

- **That the extracted invariants are the right ones** (Class C, and the
  faithfulness of §3). Bounded by: the one-time equivalence ledger, the M4
  independent review, and the M5 author acceptance. Not by tests, ever.
- **That the Linux kernel behaves as the pinned semantics assert** — signal
  delivery, `SCM_RIGHTS`, `/proc` races, process-group reaping. Bounded by:
  these remain declared pinned assumptions in `constants.py` with the citation
  attached, tested only against a model, and re-examined once at activation
  review. A model check of a wrong model proves nothing, and the charter says so
  rather than implying coverage.
- **Real concurrency under real scheduling.** Enumeration covers the declared
  interleavings, not the machine's. Bounded by: fail-closed defaults, and the
  fact that `T` activation is separately authorized and out of scope here.
- **Absence of an unimagined state.** Bounded by: totality is asserted over the
  declared product, so an undeclared dimension is invisible. The declared
  dimension set is itself an M4 review object.

---

## §5. Migration work packages and gates

Each package: inputs → outputs, allowed edits, tests, reviewer, terminal
failure, authorization boundary. No package may begin before its predecessor's
gate closes.

### M0 — signed halt and archive decision

- **Inputs:** this charter; the §8 tokens.
- **Outputs:** an author signature file recording the halt and the route.
- **Allowed edits:** create one signature file; move superseded prose to
  `successor/archive/` **only** if the author's token so directs.
- **Tests:** none.
- **Reviewer:** independent X/Y on this charter's bytes, before signature.
- **Terminal failure:** author declines the route. The prose line resumes under
  its existing rules, or the programme returns to science with the P1 cell
  unresolved. Both are acceptable; neither is this charter's to choose.
- **Authorization boundary:** records a decision. Authorizes no code.

### M1 — invariant inventory and source-of-truth skeleton

- **Inputs:** M0 signature; the §3 inventory; signed signature files.
- **Outputs:** `contract/` skeleton with `constants.py` and `data/` populated;
  `EQUIVALENCE_LEDGER.md` covering I-1..I-15; empty `machines.py`/`schemas.py`
  with signatures only.
- **Allowed edits:** create `successor/officina/contract/**` only. No edit to
  `src/`, `tests/`, existing successor documents, runtime artifacts, or dirty
  work.
- **Tests:** ledger completeness (every I-n present, each with a source path
  that exists); no duplicated literal across `contract/` modules.
- **Reviewer:** X line — extraction faithfulness against signed sources.
- **Terminal failure:** an invariant in §3 has no single authoritative home, or
  two invariants contradict. Stop; amend the charter; do not improvise.
- **Authorization boundary:** creates declarations. No machine, no generator,
  no runtime.

### M2 — executable machines and schemas

- **Inputs:** reviewed M1.
- **Outputs:** `machines.py` (pure transition functions), `schemas.py` (frozen
  dataclasses + validators).
- **Allowed edits:** `contract/**` only.
- **Tests:** §4.1 in full; §4.2 for any byte surface introduced.
- **Reviewer:** X line — semantics; the Class-A decisions of §1.2 are settled
  here, explicitly and once.
- **Terminal failure:** enumeration finds a state with zero or two routes that
  cannot be resolved without a new author choice. Stop; raise the choice; do not
  pick a reading.
- **Authorization boundary:** pure functions with no I/O, no process, socket,
  pipe, signal, `/proc` read or filesystem write.

### M3 — generator, verifier, tests

- **Inputs:** reviewed M1 and M2.
- **Outputs:** `tools/officina_contract/{render,verify}.py`;
  `generated/{CONTRACT.md,MANIFEST.json}`; `tests/test_officina_contract_*.py`.
- **Allowed edits:** `tools/officina_contract/**`,
  `successor/officina/generated/**`, new `tests/test_officina_contract_*.py`.
  No edit to any existing test file.
- **Tests:** §4.3 through §4.6; check-mode drift refusal proven by a test that
  perturbs a copy and asserts failure.
- **Reviewer:** X line — generator determinism and verifier completeness.
- **Terminal failure:** the generator is not deterministic (two runs differ), or
  the verifier passes a perturbed copy.
- **Authorization boundary:** writes only under `generated/` and the test
  tree. No runtime artifact, no `successor/officina/runtime/**` touch.

### M4 — independent equivalence review

- **Inputs:** M1–M3 outputs; the equivalence ledger; signed sources.
- **Outputs:** one X memo and one Y memo on identical bytes.
- **Allowed edits:** reviewers create exactly one review file each. Nothing
  else.
- **Tests:** reviewers re-run the suite and independently re-derive at least the
  enumeration totals and the manifest digests.
- **Reviewer:** X and Y, neither of whom authored M1–M3.
- **Terminal failure:** X and Y diverge on a *semantic* question. Under this
  architecture they cannot diverge on a provenance question — §6.2 — so a
  semantic divergence is a genuine open design question and goes to the author,
  not to a repair round.
- **Authorization boundary:** review only.

### M5 — author acceptance of the replacement inactive contract

- **Inputs:** M4 memos.
- **Outputs:** an author signature accepting the executable contract as the
  inactive operative contract, superseding the prose line.
- **Allowed edits:** one signature file; archive move of the prose line.
- **Reviewer:** the author.
- **Terminal failure:** acceptance withheld. The contract remains a reviewed,
  unaccepted draft; nothing regresses.
- **Authorization boundary:** accepts an **inactive** contract. Not activation.

### M6 — implementation integration review

- **Inputs:** accepted contract; the salvage candidates of §7.
- **Outputs:** a bounded plan reconciling `src/philosophia/officina/` with the
  accepted contract.
- **Authorization boundary:** planning and review only; integration is a
  separate authorization. **Activation remains separately authorized and is not
  reachable from any token in this charter.**

### §5.1 Cursor's boundary

Cursor may implement **bounded routine packages only, and only after the M1 and
M2 specifications have been independently reviewed** — M3's generator, verifier
and test scaffolding, and mechanical M1 data entry against a reviewed
specification. Cursor may not author `machines.py` semantics, resolve a Class-A
question, decide an extraction boundary, or create or modify any signature,
review, runtime or activation artifact.

---

## §6. Complexity and exit budgets

### §6.1 Enforceable limits

| Budget | Limit | Justification |
|---|---|---|
| Authoritative source, total | **2,500 LOC** and **120 KiB** across `contract/**` | `src/philosophia/officina/` is 7,349 LOC of working code; the contract is a specification of one subsystem and must be smaller than the subsystem. 120 KiB is 5.5× smaller than the single current composite. |
| Any one source module | **600 LOC** | A module a reviewer cannot hold in one sitting is where Class-A defects hide. |
| Canonical JSON data | **64 KiB** across `data/**` | Data that outgrows this is a fixture generator, not a declaration. |
| Generated `CONTRACT.md` | **3,000 lines** and **200 KiB** | Generated text cannot drift, but it must stay readable; beyond this nobody reads it and its documentation value is fictional. |
| Live files under `contract/` | **12** | Forces one home per fact rather than a taxonomy. |
| Live manifests | **1** | §2.1(3). |
| Duplicated string literals across live surfaces | **0**, enforced by a test | This is the Class-B kill switch, not a style rule. |
| Review rounds per work package | **2**. A third round is prohibited. | The prose line took >100. Two rounds is enough to catch a real defect and not enough to sustain a loop. |
| Generation numbers | **None for ordinary fixes.** A fix edits source in place; Git carries history. Version identifiers exist only on author-signed artifacts. | The generation cascade *is* Class D. |
| Time to M5 | **21 calendar days** from the M0 signature. | Long enough for six gates at the observed pace; short enough that overrun is a signal rather than a habit. |

### §6.2 The mandatory redesign threshold

If any package reaches a **third** review round, or the 21-day clock expires
before M5, work **stops**. It does not continue under a new generation. The
outcome is one short memo stating what converged, what did not, and which of
three routes the author is asked to choose: (a) accept a reduced contract
covering only the converged invariants; (b) return to scientific development
with the P1 cell explicitly unresolved and the harness left inactive; (c) a new
signed route decision.

This threshold is the charter's own stopping condition. A charter that proposes
to end a repair loop and does not bind itself to a stopping condition has
learned nothing from the loop.

### §6.3 Override

Every limit above may be exceeded **only** by a new author-signed route decision
naming the limit, the new value and the reason. Silent expansion is prohibited.
A budget overrun discovered in review is a §6.2 event, not a finding to repair.

---

## §7. Disposition of current artifacts

| Artifact | Disposition |
|---|---|
| Composite `v1.15`, amendment `v1.12`, binding `v6`, handoff `v6`, and **all** prior prose generations | Halted as **unaccepted**. Retained as Git and archive evidence. Never members of the live contract, never inputs to any cardinality, never cited as authority. On the M0 token they move to `successor/archive/`. |
| `I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12` | **Not accepted, and retired unsigned.** It does not become signable by this charter, by the X line's confirmation, or by any token in §8. It is superseded as a route by the M5 acceptance. |
| `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` | **Remains not accepted.** Extracted as I-5, represented explicitly as an unaccepted non-operative token. Migration does not accept it by implication or by omission. |
| Uncommitted `src/philosophia/officina/generic_harness.py`, the accounting edits, `tests/test_officina_generic_harness.py`, `tests/test_officina_accounting.py` | **Salvage candidates only, untouched.** Not authority, not evidence, not a member of anything. They remain exactly as they are on disk until M6 evaluates them against the accepted contract. This charter authorizes no edit, no commit, no revert and no deletion. |
| Signed author and scientific choices — charter `v2.1`, author selections `v1`, WP-3, the four P1/supervisor selection signatures | **Preserved unchanged and remain authoritative.** Migration reads them once at M1 and never modifies, restates or supersedes them. Their existing files stay the authority for Class-C facts. |
| `successor/officina/{LINEAGE,PATH_POLICY,T_ENVELOPE}.json`, `T_LEDGER.md`, `runtime/` | Untouched. Extracted as I-11/I-12 by reference, not by copy. |
| `T = NOT_ACTIVATED` | Unchanged. No token in this charter can change it. |
| `OR-2 COMPLETE`, `OR-3..OR-11 NOT AUTHORIZED` | Unchanged, and extracted as I-14. |

**No current candidate becomes accepted by implication.** The X line's
`OFFICINA_P1_WB_V2_15_X_CONFIRMED_FOR_AUTHOR_ACCEPTANCE` verdict is an input to
a consideration that the author is not being asked to complete. Halting the line
is not accepting its last generation, and the M0 token says so explicitly.

---

## §8. Bounded author choices and tokens

Four tokens. Three are recommended as stated; one is a genuine choice with a
recommended default.

### T-1 — Halt the prose-generation line

```text
I_HALT_OFFICINA_PROSE_CONTRACT_LINE_V1
```

Halts the amendment/composite/binding/handoff line at its current generation,
archives it as **unaccepted** evidence, and retires
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12`
unsigned. **Recommended.** Declining leaves the line live under the divergent
X/Y verdicts with no defined next act.

### T-2 — Accept the migration route

```text
I_ACCEPT_OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1
```

Accepts §1–§7 as the route: the authority graph, the §3 extraction boundary,
the §4 verification strategy, the §5 gates, and the §6 budgets **including the
mandatory redesign threshold**. **Recommended.** It accepts a plan, not a
contract; the replacement is accepted separately at M5.

### T-3 — Dependency policy

Mutually exclusive. Recommended default first.

```text
I_SELECT_OFFICINA_CONTRACT_DEPENDENCY_STDLIB_ONLY          (recommended)
I_SELECT_OFFICINA_CONTRACT_DEPENDENCY_STDLIB_PLUS_HYPOTHESIS_DEV_ONLY
```

The first keeps `contract/` and `tools/` importable with zero non-stdlib
dependencies and uses seeded deterministic corpora for §4.2. The second adds
Hypothesis as a **dev extra, test-only**, never imported by `contract/` or
`tools/`, for the byte-surface property tests only. Both satisfy §4; the first
minimizes unreviewed surface, which is the whole point of the migration.

### T-4 — Authorize M1 and M2 implementation only

```text
I_AUTHORIZE_OFFICINA_CONTRACT_M1_M2_IMPLEMENTATION
```

Signable **only after** independent X-line and Y-line review of this charter's
bytes, in which both lines review the same bytes. Authorizes creation of
`successor/officina/contract/**` under §5's M1 and M2 boundaries and nothing
else.

### §8.1 What no token here authorizes

No token in this charter authorizes, and none may be read as authorizing:
`T` activation; any `OR-3`..`OR-11` step; any scientific specification,
preregistration, entropy, seed, key, world, learner, candidate, Q or C object,
datum, outcome, Proof or claim movement; any E1/E2/E3 spend; any install,
attestation, detached signature, Stage A or Stage B, or install record; any
process, socket, pipe, FIFO, fork, exec, signal, wait or `prctl` operation; any
edit to `src/`, to existing tests, to runtime artifacts, or to the uncommitted
salvage work; any acceptance of amendment `v1.12` or of
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`; and any commit.

---

## §9. Negative space of this document

This charter creates no code, contract module, schema, fixture, generator,
verifier, manifest, test or runtime artifact. It executed no machine,
enumerated no cross-product against any live process, read no `/proc`, opened
no socket, pipe or descriptor, and sampled no clock for any contract purpose.
It modified no existing file: no governing or historical document, no code, no
test, no signature, no runtime artifact, no prior review, and none of the dirty
or untracked working-tree work. It made no commit. It predicts no X or Y
verdict and no scientific outcome.

The seven pinned inputs were recomputed and all seven reproduced exactly.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
WATCHDOG AUTHORITY AMENDMENT V1.12 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

The exact signed tokens and the formal signature files govern. This charter and
every author closure are untrusted self-assessments and are normative for
nothing until §8's tokens are signed.
