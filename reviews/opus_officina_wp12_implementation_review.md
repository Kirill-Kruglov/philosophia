# Opus 4.8 X-line — Officina WP-1/WP-2 implementation review

**`OFFICINA_WP12_XLINE_ACCEPTED`**

Reviewer: Opus 4.8 (X-line, bounded WP-1/WP-2 implementation review). Repository:
`/home/master/llm_projects/philosophia`, reviewed diff `d3be92f..2de1df5`. **I
created no entropy, real world, model run, candidate registration, Q attempt,
lock, escrow secret, or outcome. Nothing committed; no existing file edited.** I
ran non-outcome unit tests and the read-only verifier only. HEAD (`614771b`)
differs from the reviewed commit only by review-prompt files; the load-bearing
source is byte-identical.

This is a faithful, conservatively-scoped, **self-verifying** WP-1/WP-2
implementation: the governance library draws no entropy, imports nothing from the
stopped line, exposes no callable real T/Q/C route, and a committed AST verifier
(run in CI) enforces exactly those properties. No Critical or Major finding. A few
Minor items are genuine **WP-4/WP-6 obligations**, not WP-1/WP-2 defects, and none
blocks WP-3 drafting.

---

## 1. Findings

### Critical / Major
None.

### Minor (WP-4/WP-6 obligations and one boundary note; none blocks WP-3)
- **W-1 (WP-6) — `code_commit` normalization semantics are unspecified.**
  `manifest.py` keys candidate identity on an opaque 40-hex `code_commit`, so
  candidate equivalence is conservative and **never under-charges** (any changed
  manifest field ⇒ new `candidate_id` ⇒ a new E2 slot). But whether the signed
  clause "behavior-inert changes cannot consume a new slot" actually holds depends
  on *what `code_commit` pins* (whole-repo HEAD vs a normalized learner-subtree /
  AST-stripped content hash). The WP-6 candidate-registration contract must define
  that so an inert edit (a comment) does not silently burn a slot. The WP-2
  primitive is sound as-is (conservative, decidable, content-addressed).
- **W-2 (WP-6) — the one-shot journal has no `CLAIMED → TERMINAL` (pre-entropy
  abandonment) transition.** A pre-entropy signed disposition is therefore
  recorded *outside* the journal, leaving a dangling `CLAIMED`. This is correct and
  conservative (a `CLAIMED`-only journal drew no worlds and is uncharged; the only
  forward is `→ DRAW_ARMED`, which commits to charging), but WP-6 must define how a
  signed pre-attempt disposition annotates/resolves a dangling `CLAIMED` for
  unambiguous audit. Not a WP-2 defect.
- **W-3 (WP-4) — device-hour cap is "complete the in-flight quantum, then stop."**
  `TState.charge_device_nanoseconds` checks exhaustion *before* adding, so the
  charge that crosses `E1` completes (final `device_nanoseconds` may exceed the
  cap) and `exhausted()` then fires `T_ENVELOPE_EXHAUSTED`. Correct semantics; WP-4
  must check `exhausted()` before starting each real-T quantum so the overshoot is
  bounded by one quantum.
- **W-4 (boundary note, procedural threat model) — quarantine TOCTOU.**
  `PathPolicy.authorize` realpath-resolves and re-hashes fixtures, but a symlink
  swap between authorize and the subsequent read is outside the guarantee. This
  matches the charter's and `interlock.py`'s stated model ("accidental-execution
  guard, not a security sandbox"); acceptable, and worth stating so no one reads
  the allowlist as a malicious-filesystem seal.

---

## 2. Answers to the six required attacks

### Attack 1 — quarantine positive/negative paths: SOUND.
`PathPolicy` (`quarantine.py`) resolves `realpath` **before** the decision
(`resolve(strict=False)` normalizes `..`/symlinks), returns `native` for
`successor/officina/**`, else consults hash-pinned fixture grants, else **denies
by default**. Engineering fixtures are **read-only**, **T-context-only**, and
**hash-verified** at authorize time; `ArtifactLabel.derived` propagates
non-promotability (`all(parent.promotable)`), and `require_promotable` raises when
a non-promotable artifact enters Q or C — the fixture→Q/C dataflow block.
Warm-start is doubly prevented: the stopped-line checkpoint paths are
deny-by-default, **and** `manifest.py` mandates `initialization ==
{"checkpoint": null, "kind": "from-scratch"}`. **Source-import quarantine** is
mechanically enforced: `verification.py` AST-walks every officina module and fails
on any `philosophia.level0/level1`/`gate_harness` import or any entropy call, and
the CI runs it. Same-repo **audit ancestry works without runtime predecessor
reads**: `LINEAGE.json` pins the predecessor by 40-hex commit and the two
signature files by SHA-256 (git ancestry is audit metadata; `runtime_inheritance:
forbidden`). `PATH_POLICY.json` has `default: deny`, empty fixtures,
`realpath_before_decision: true`. Tests cover native-allow/predecessor-deny,
fixture read-only/T-only/non-promotable/hash-pinned, and symlink-escape blocking.

### Attack 2 — bootstrap integrity: SOUND.
Canonical manifests (`LINEAGE`, `PATH_POLICY`, `T_ENVELOPE`, all
`scientific_outcome:false`); `LINEAGE` pins the authorization and charter
signatures by content hash and the predecessor by commit; the verifier asserts the
**exact** six-file set, deny-by-default policy, `activated:false` envelope, and a
`T_LEDGER.md` that is both an empty `NOT_ACTIVATED` skeleton **and** parseable by
`parse_ledger` (header-pinned, no `- {` entry line). The committed ledger holds no
real entry.

### Attack 3 — one-shot positive path: SOUND, draws zero entropy.
`OneShotJournal` is a hash-chained, append-only, phase-monotonic event log:
`CLAIMED → DRAW_ARMED → {LAUNCHED, TERMINAL}` and `LAUNCHED → TERMINAL`, with no
backward transition. The launch boundary is precise and safe: `arm_draw`
(`DRAW_ARMED`) is durable **before** the caller's entropy invocation, so **any**
`DRAW_ARMED → TERMINAL` recovery is *forced* to `charged: true, competence: null`
("ambiguous draw recovery must be charged with competence unset"), and
`recovery_requires_charge()` returns true for `DRAW_ARMED`/`LAUNCHED`. There is
therefore **no path to entropy without a durable charge** (entropy ⟹ durable
`DRAW_ARMED` ⟹ forced charge), **no redraw** (`LAUNCHED` admits only `TERMINAL`),
**no fallback**, and **no silent within-journal retry** (monotonic). `LAUNCHED`
records only a 64-hex **root commitment**, never the root — **the package itself
draws zero entropy** (confirmed by grep and by the CI AST verifier; the
`ENTROPY_CALLS` set in `verification.py` is the denylist, not a call site). Tests
pin monotonicity, tamper detection, and the ambiguous-`DRAW_ARMED`→charged-invalid
recovery. (Cross-attempt "no silent retry" from a fresh `CLAIMED` journal is the
WP-6 signed-disposition gate — W-2.)

### Attack 4 — durability: SOUND.
`canonical.py` provides `atomic_create` (O_EXCL temp → write+flush+**fsync file**
→ `os.link` **no-replace** → unlink temp → **fsync parent dir**) and
`atomic_replace` (O_EXCL temp → `os.replace` → fsync dir), with temp cleanup on
any exception. `ledger.py` is append-only, hash-chained (`previous_sha256`,
`entry_sha256`, contiguous `sequence`), header-pinned, canonical-JSON-per-line,
`flock(LOCK_EX)`-serialized for concurrent append (each appender re-reads the tail
under the lock), fsync file+dir; `parse_ledger` detects non-ASCII, header drift,
non-canonical/non-JSON lines, sequence gaps, chain breaks, and hash mismatches.
`checkpoint.py` orders the pause correctly: the pause checkpoint (binding
`ledger_head_before` = the head **before** the pause entry) is written durably,
**then** the `T_OPERATIONAL_PAUSE` entry is appended; `verify_resume` requires the
ledger to end in that pause, the checkpoint hash to match, the path to match, and
`ledger_head_before == entries[-2].entry_sha256` (**prior-ledger-head binding**) —
so a crash after the checkpoint but before the entry fails closed (no pause
terminal), and checkpoint mutation is rejected. `resets_e3: false`; a
never-activated maintenance records the fact and **creates no fictitious
checkpoint**. Tests pin tamper-evidence, pause round-trip counter preservation,
resume-refuses-mutation, and no-checkpoint-when-inactive.

### Attack 5 — candidate identity / interlocks: SOUND.
`manifest.py` requires the **exact** field set `{schema, code_commit, stack_id,
initialization, optimizer, policy, interface, config}` — **unknown fields raise**
(missing or extra), mandatory `from-scratch` initialization, 40-hex `code_commit`,
non-empty `stack_id`, object-typed sub-configs — and content-addresses the
candidate. Re-registering the same `candidate_id` is **idempotent** (no new slot);
a different id consumes one. `interlock.py` exposes **only** a `test-only`
capability (purpose must start `test-only:`); every real route
(`generate_real_world`, `run_real_t`, `launch_q`, `execute_c`) is a **raising
stub** (`ExecutionNotAuthorized`), and `__init__.py` exports only safe primitives.
**No callable real T/Q/C route exists.** `terminal.py` types the exclusive/total
taxonomy so invalidity can never carry a scientific field (`QTerminal`/`CTerminal`
invariants). Tests pin conservative/content-addressed manifests, invalidity-can't-
become-science, and real-entry-points-fail.

### Attack 6 — scope: FAITHFUL WP-1/WP-2; no downstream cell smuggled in.
No module implements or selects a WP-3/WP-6/WP-9 cell: no population frame /
support / strata / weights (WP-3); no Q caps / `δ_Q` / spending / competence
numerics (WP-6 — the journal and terminals are numeric-free primitives); no
endpoint / margin / N / arms (WP-9 — escrow is caller-supplied building blocks);
no entropy-mechanism instantiation (the launch records a caller commitment, draws
nothing); no breathing-check run; `stack_id` is an opaque string. `T_ENVELOPE.json`
carries only the signed caps and `activated:false`. The package is **primitives +
inactive bootstrap** exactly.

---

## 3. Tests and verifiers run (read-only)

- `pytest tests/test_officina_accounting.py tests/test_officina_bootstrap.py
  tests/test_officina_governance.py` → **22 passed** (7 accounting, 6 bootstrap,
  9 governance).
- `pytest` (full suite) → **189 passed** (no regression to the stopped line).
- `scripts/verify_officina_wp12.py` → **OK: Officina WP-1/WP-2 bootstrap is
  quarantined and inactive** (exact file set, authorization/charter hash pins,
  deny-by-default, inactive envelope, empty ledger skeleton, AST source
  quarantine).
- `grep` for entropy calls in officina source → none (the only matches are the
  denylist literals in `verification.py`).
- `grep` for `philosophia.level0/level1`/`experiments/level` imports in officina →
  none.
- CI (`.github/workflows/ci.yml`) runs `verify_officina_wp12.py`, so the
  no-entropy / no-predecessor-import / inactive-bootstrap properties are enforced
  on every push.

---

## 4. Blockers before WP-3 vs later WP obligations

**Blockers before WP-3 drafting: none.** The implementation faithfully matches the
signed WP-1/WP-2 authorization; no repair is required to begin drafting the WP-3
population/construct contract.

**Later obligations (not now):** W-1 (`code_commit` normalization) and W-2
(pre-entropy signed-disposition journal annotation) are **WP-6** cells; W-3
(exhaustion check before each real-T quantum) is a **WP-4** cell; W-4 (TOCTOU) is
an accepted procedural-threat-model boundary. WP-3 itself must, per the charter,
pin the eight population objects, the `P_Q`↔`P_C` relation, and the finite-frame
sample interpretation (A2) with its inclusion probabilities/weights/FPC — none of
which this WP-1/WP-2 work has touched or constrained.

## 5. May Codex close WP-1/WP-2 and begin only WP-3 drafting?

**Yes.** With this X-line acceptance (and Sol's parallel Y-line review), Codex may
**close WP-1/WP-2** and begin **only the drafting** of the WP-3
population/construct contract — a reviewable document, not code that generates
worlds. Codex must **not**: generate any real T world or dev-root entropy;
activate the T envelope or run any real T training; register a candidate; run a
breathing check; launch a Q attempt; or touch any Q/C/lock/escrow surface. WP-3 is
itself independently drafted, X/Y-reviewed, and **author-signed before any real T
world exists**; WP-4 (T infrastructure) and every later gate keep their own review
and signature. The `interlock.py` stubs and the CI quarantine verifier remain the
fail-closed floor throughout.

## 6. Negative space and confirmation

The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its C1 unrun and untested; v1/v2 non-comparable, non-citable, and choosing nothing
here. Officina's T and Q can never earn, kill, or boundary-label C1–C6; S is
unavailable; only a valid, independently locked C execution may ever move a
successor claim, within its selection-conditional scope. "No qualifier," censored,
`UNKNOWN`, and every invalid state are never success, equivalence, a boundary, or
learner impossibility. This implementation moves no scientific claim and creates no
world, entropy, candidate, run, Q, lock, escrow, or outcome;
`PROOF_CORE`/`PROOF_STRONG` remain earned by nothing and the programme claim stays
`OPEN`.

I edited no existing file, created exactly one new file (this review), selected no
open cell, and committed nothing. `essay/OUTLINE.md` untouched. My only actions
were reading the reviewed diff and running the read-only unit tests and verifier
above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
