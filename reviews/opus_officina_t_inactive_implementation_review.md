# Opus 4.8 X-line — Officina T inactive implementation review

**`OFFICINA_T_INACTIVE_IMPLEMENTATION_ACCEPTED`**

Reviewer: Opus 4.8 (X-line, adversarial transaction/runtime). Repository:
`/home/master/llm_projects/philosophia`, implementation commit `77c5a63` (HEAD
`d853dbc` differs only by review prompts). **I edited/committed/activated nothing,
created no authorization, real world, process, or lease, and spent no E1/E2/E3;
positive activation tests ran only as written, in disposable temp git mirrors.**
The real tree is pristine: `T_ENVELOPE.json activated:false`, ledger at genesis,
`runtime/` contains only the reviewed immutable lock (`OFFICINA_T_RUNTIME_LOCK_V1`).
`git diff --check` clean.

The implementation is a faithful, fail-closed, **inactive** realization of the
v1+v2+v2.1 protocol: exact schemas/key-sets, hash-pinned authorization, exact-stage
activation commit with claim-before-mutation failure routing, a held-descriptor
runtime lock, the closed nine-event vocabulary with state-bearing t_state, the
`min()` E1/E3 reservation arithmetic, validity-first records with recursive
scientific-field rejection, a mechanical production/test boundary, and — decisively
— **no real-T capability and activation blocked until the generic metered harness
is reviewed**. No Critical or Major finding; two Minor items, non-blocking.

---

## Findings

### Critical / Major
None.

### Minor

- **T-m1 — the reservation terminal-routing rule (§4) is not an encoded/tested
  primitive (`runtime.py:210-211`).** `reservation_for` returns `None` when
  `per_unit ≤ 0` without distinguishing **E1-exhausted** (→ `T_ENVELOPE_EXHAUSTED`)
  from **E3-due** (→ the nonterminal E3 gate) from **both-zero** (→ "exhaustion
  first, E3 preserved"), which protocol v2.1 §4 fixes exactly. The arithmetic and
  boundary-shortening are correct and tested
  (`test_reservation_shortens_at_e1_and_e3_boundaries_without_stranding`), but the
  which-terminal routing is left implicit for the (deferred) orchestration.
  **Bounded repair:** add a small testable helper (e.g. returning
  `RESERVE | E1_EXHAUSTED | E3_DUE`) that encodes the §4 both-zero-→-exhaustion-first
  rule, or state explicitly that the deferred harness owns it with the §4 rule
  pinned and a mirror test. Either way the both-zero precedence should be enforced,
  not left to harness discretion.

- **T-m2 — the activation re-derive verify and commit run just outside the
  `RuntimeLock` (`activation.py:408, 411, 415`).** The `with RuntimeLock` block ends
  after step 5; the pre-commit `verify_active_repository`, `_commit_activation`, and
  post-commit verify then run unlocked, whereas protocol §B states the post-verify
  is under the lock. For **one-shot** activation (`execution_once:true`, no
  concurrent writer) this is benign, but it deviates from the stated lock scope.
  **Bounded repair (or explicit rationale):** extend the lock to cover the
  re-derive/commit/post-verify, or note that activation's single-shot exclusivity
  makes the post-lock verify safe while the **runtime** metering path (deferred)
  must keep the whole read-verify-append-commit-verify under the lock.

---

## Item-by-item audit

1. **Schemas / paths / pins / staged commit / claim-before-mutation — CONFIRMED.**
   `_AUTHORIZATION_KEYS`/`_CLAIM_KEYS`/`_RECORD_KEYS` and the runtime schemas match
   protocol §C/§D exactly; `canonical_paths` includes the v2.1 `runtime_lock` plus
   the seven logical names, resolved-absolute. `validate_authorization` enforces the
   exact key set, schema, `scientific_outcome:false`/`execution_once:true`, token,
   40-hex reviewed HEAD, unique reviewed paths ↔ hash map, the **12 immutable
   control paths ⊆ reviewed**, the **generic-harness-in-reviewed** gate, canonical
   paths, and the exact command. `_commit_activation` stages **exactly**
   `ACTIVATION_STAGE_PATHS` (order-independent set-equality, empty-index precheck)
   with the three exact trailers. Claim-before-mutation: under the lock,
   `atomic_create` CLAIM → STATE → ledger `T_ACTIVATED` (state-bearing) → `atomic_
   replace` ENVELOPE → RECORD; `except BaseException: if step ≥ 1:
   _record_activation_invalidity(step); raise` — a failure after the durable claim
   writes `T_ACTIVATION` `INVALID_PROCESS_RECORD` (`required_action=SIGNED_BOUNDED_
   RECOVERY_NO_AUTOMATIC_RETRY`), a pre-claim failure leaves pristine T. No
   field/type mismatch or ambiguous carry-forward found.

2. **Authorization newer than `reviewed_code_head`, empty diff, no unreviewed
   source — CONFIRMED.** `_preflight_git` checks the reviewed commit exists, then
   `git diff --quiet reviewed HEAD -- <reviewed paths>` (bytes unchanged) with a
   clean worktree and empty index and a tracked authorization — so the authorization
   commit may be newer than the reviewed HEAD while the reviewed source diff stays
   empty. Unreviewed source cannot reach activation: the 12 byte-pinned control
   modules + generic harness are the whole production graph (their fixed bytes
   cannot import an unreviewed module), and `verify_hash_map` re-checks every
   reviewed byte.

3. **Runtime lock / derivation / atomic ordering / substitution / partial txn /
   verifier split — CONFIRMED.** `RuntimeLock` opens `O_RDWR|O_CLOEXEC|O_NOFOLLOW`,
   `samestat`-anchors, verifies the exact lock bytes, `flock(LOCK_EX)`, and
   re-anchors after locking; `verify_runtime_lock` rejects a symlink/wrong-bytes/
   identity-drift lock. `AppendOnlyLedger.append` carries its `expected_file_
   descriptor` anchor. The active/inactive split is real: `verify_bootstrap` now
   **returns `["ACTIVE_TREE_REQUIRES_ACTIVE_VERIFIER"]`** once the envelope is
   `activated:true`, and `verify_officina_active.py` governs thereafter (confirmed:
   the inactive verifier passes on the committed tree, the active verifier refuses
   it for the absent authorization). Partial-transaction handling is tested
   (`test_partial_activation_is_durable_invalidity_and_cannot_rerun`).

4. **Nine-event vocabulary + state-bearing post-state; checkpoint change —
   CONFIRMED.** `POST_ACTIVATION_EVENTS` is the closed nine; `STATE_BEARING_EVENTS`
   the eight (minus `T_PROCESS_STARTED`). `verify_active_repository` rejects any
   ledger event outside the vocabulary, requires every state-bearing event to carry
   `t_state`, and requires the state cache to equal the **last** state-bearing
   event's `t_state`. The checkpoint change adds `t_state` to `T_OPERATIONAL_PAUSE`
   (making it state-bearing) and `verify_resume` now requires the pause ledger
   `t_state` to equal the checkpoint's — extending, not breaking, the confirmed
   pause/resume/`ResumeGate` semantics (full suite green).

5. **E1/E3 reservation arithmetic — CONFIRMED (see T-m1).** `reservation_for`
   computes `per_unit = min(60 s, e1_remaining//units, e3_remaining//units)` with
   `e1_remaining = 168 h − (charged + live liabilities)` and `e3_remaining = 40 h −
   (device-since-review + live liabilities)`; caps concurrency at 4 and aggregate
   liability at 240 device-seconds; one behavior-capable **stream** = one unit.
   Hand-checked at ordinary/concurrent/shortened/overshoot boundaries;
   `settle_monotonic_delta` requires a strictly increasing cursor and retains the
   crossing charge (tested). Only the terminal-routing distinction is deferred
   (T-m1).

6. **Process-id / claim → lease → settlement → final record — CONFIRMED.**
   `process_id_for` = SHA-256 over the exact identity core (activation-record hash,
   sequence, four behavior hashes, argv, device identity, boot identity), re-derived
   and checked in `validate_process_claim`; `bool` is excluded everywhere via
   `type(x) is int`; `clock_kind` pinned to `CLOCK_MONOTONIC`; `boot_identity`
   validated; duplicate id/sequence and cursor rollback are rejected; and
   `reject_scientific_fields` recursively bars the forbidden public keys **and**
   `c1`–`c6` from every claim/lease/record/invalidity artifact (tested). Invalid
   causes are exactly `PROCESS/RESOURCE/HASH/CLOCK/FILESYSTEM` — `NONFINITE_
   DEVELOPMENT` is absent (v2.1 §3), with learner non-finiteness routed to a public
   `T_PROCESS_VOLUNTARY_STOP`.

7. **Production/test boundary — CONFIRMED.** `verify_production_boundary` AST-rejects
   the six test-world symbols (`test_world_capability`, `issue_test_t_contact_
   harness`, `evaluate_test_query`, `record_test_t_contact`, `TestWorldCapability`,
   `TestTContactHarness`) in every reviewed `.py` **except `world.py`**, catching
   `from`-imports (alias name), dotted attribute access, and bare names; reflection
   via `getattr`/`eval`/`exec` is separately banned by `verify_source_quarantine`;
   omitted paths cannot enter the byte-pinned production graph. A test-only world
   route cannot reach production (`test_production_boundary_detects_test_world_
   imports`).

8. **Deferred supervisor/quiescence/harness — CORRECTLY AND MECHANICALLY
   DEFERRED.** The inactive core provides only schemas, the lock, reservation
   arithmetic, and record builders/validators; it **claims no runtime contract it
   cannot enforce**: `RealTCapability.__init__` and `issue_real_t_capability`
   **raise**, and `validate_authorization` **refuses activation** unless
   `src/philosophia/officina/generic_harness.py` (absent) is in the reviewed source
   paths (`ActivationRefused: generic metered harness has not received review`). The
   supervisor, watchdog, backend-quiescence adapter, and real oracle/learner
   metering are thus deferred to the separately required harness review, with the
   v2.1 rules pinned and the accounting substrate available for that harness to
   consume.

9. **Suites / verifiers / pristine tree — CONFIRMED.**
   `pytest tests/test_officina_activation.py tests/test_officina_runtime.py` → **15
   passed**; officina suite → **84 passed**; full `pytest` → **251 passed** (no
   regression); `verify_officina_wp12.py` → **OK: quarantined and inactive**;
   `verify_officina_active.py` correctly **refuses** the inactive tree (absent
   authorization); the real tree holds only the reviewed immutable lock in
   `runtime/` and remains `NOT_ACTIVATED`; the committed `T_LEDGER.md`/head are at
   genesis. No load-bearing path is untested except the T-m1 terminal-routing
   distinction (deferred/implicit).

## Next gate

A positive verdict authorizes **only the next generic metered harness
design/implementation gate** (protocol v2.1 §7) — the supervisor, process-tree,
backend-quiescence/synchronization adapter, watchdog, oracle/update/checkpoint
metering, and test-surface call graphs — subject to its own bounded X/Y review. It
authorizes **no** activation candidate, activation, entropy, real T world, learner
execution, lease, E1/E2/E3 spend, breathing check, Q/C activity, or scientific
interpretation. Activation additionally requires `generic_harness.py` reviewed and
pinned, an exact authorization candidate, and Kirill's explicit
`I_AUTHORIZE_OFFICINA_T_ACTIVATION`, before the driver runs exactly once.

## Negative space

The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its records are non-citable and chose no value here. Officina's T and Q are
permanently non-citable for C1–C6; activation, leases, streams, tuning observations,
breathing checks, draft manifests, E3 reviews, non-finiteness, and every T ending
are non-scientific and move no claim; a future Q pass is a spendability gate fact
only; S is unavailable; only a valid, independently locked C execution may ever move
an Officina claim, within its selection-conditional, selected-frame, orientation,
device, and learner-seed scope. Censored/`UNKNOWN`/every invalid state are never
success, equivalence, a boundary, or learner impossibility. `PROOF_CORE`/`PROOF_
STRONG` remain earned by nothing; the programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this review), authorized
nothing, activated no T state, and committed nothing. `essay/OUTLINE.md` untouched.
My actions were reading the implementation/tests/protocol and running the read-only
suites, verifiers, and pristine-tree checks above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
