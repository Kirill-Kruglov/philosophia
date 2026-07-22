OFFICINA_T_INACTIVE_REPAIR_V2_CONFIRMED

# Opus 4.8 X-line — Officina T inactive repair v2 confirmation

Reviewer: Opus 4.8 (X-line, adversarial implementation/provenance). Repository:
`/home/master/llm_projects/philosophia`. Bounded mandate: commit `2277331`
against parent `2d0cc0b`, reconciling the divergence between
`reviews/sol_officina_t_inactive_repair_confirmation.md` (Sol
`REVISE_OFFICINA_T_INACTIVE_REPAIR`, residuals C1–C4) and
`reviews/opus_officina_t_inactive_repair_confirmation.md` (my
`OFFICINA_T_INACTIVE_REPAIR_CONFIRMED`). **I edited nothing, committed nothing,
activated nothing, created no harness, manifest, authorization, world, process,
lease, capability, candidate, entropy, Q/C object, datum, or outcome, and spent
no E1/E2/E3.** Positive constructor/graph probes ran only as read-only, in-memory
values or in disposable temporary directories/mirrors; the real tree was never
mutated. It remains pristine and `NOT_ACTIVATED` after every check:
`T_ENVELOPE.json activated:false`, `runtime/` = `{T_RUNTIME.lock}`, and no
`generic_harness.py`, `runtime_control/PRODUCTION_CALL_GRAPH.json`,
authorization, claim, record, lease, state, or process artifact.

The diff `2d0cc0b..2277331` touches exactly
`src/philosophia/officina/{accounting,activation,runtime,verification}.py`,
`successor/officina/T_ACTIVATION_IMPLEMENTATION.md`, and the three officina test
files — no signed scientific cell, envelope numeric, phase boundary, frame, or
governing/protocol pin changes, and no executable authority is silently
expanded (the real generic harness and production manifest remain absent, so
activation stays mechanically blocked). Sol's C1–C4 are closed one-to-one,
transactionally and within scope.

## Closure of Sol C1–C4

**C1 — pre-WP-6 E2 no longer representable or interpretable (CLOSED).**
`TState.__post_init__` now rejects any nonempty `candidate_ids`
(`accounting.py:74-77`: "candidate registrations require the absent signed WP-6
authority"), so `from_mapping` (which constructs through `__post_init__`) is
covered too; `exhausted()` now depends **solely** on the E1 device-hour cap
(`accounting.py:137-139`), the `candidate_cap` term removed. Independently
reproduced: a direct active `TState` with 12 candidate IDs is rejected;
`from_mapping` with a candidate list is rejected; `exhausted()` is `True` exactly
at the 168 h cap and `False` one nanosecond under. No callable pre-WP-6 path can
create or interpret E2 consumption. (`register_candidate` still raises, and the
active verifier still fails on a persisted candidate list — defense in depth.)

**C2 — final-record composition is coupled to the settlement event and requires
activation-control validation (CLOSED).** `build_active_lease` and
`build_process_record` now invoke `validate_process_claim_against_activation`
**internally and mandatorily** (new required `activation_record_sha256` +
`immutable_control_sha256` params), so an arbitrary/nonmatching immutable-control
map is refused (reproduced: `build_active_lease` with `{"totally.py":…}`
refuses). The settlement `final_charge_event` must be `T_DEVICE_TIME_CHARGED`
(not "either kind"), so Sol's first cross-kind probe (a `T_RUNTIME_INVALID` event
yielding a `VALID` close) is refused ("process settlement requires a device-time
charge event"). A `ProcessDisposition.INVALID` close now **requires** a matching
`T_RUNTIME_INVALID` terminal event **and** a typed invalidity record, bound
together by event ancestry (`previous_sha256 == charge.entry_sha256`,
`sequence == charge.sequence + 1`), identical post-state, coupled
`invalid_cause` across event and record, matched `outstanding_liability_ns`, a
hash-bound `invalidity_record_sha256`, and `observed_utc == terminal timestamp`;
a `VALID` disposition that carries either artifact is refused. Sol's second
cross-kind probe (an ordinary charge silently producing an `INVALID` close) is
therefore refused. The invalidity record cannot be an activation invalidity
(`transaction_kind == "T_ACTIVATION"` refused for a process close), and
`validate_invalidity_record` now pins `transaction_kind`, `affected_path_sha256`,
`observed_utc`, and clock/boot identity (a process invalidity must carry
`CLOCK_MONOTONIC` + a boot id; an activation invalidity must not). I verified the
activation-written invalidity payload satisfies this expanded schema exactly
(`transaction_kind:"T_ACTIVATION"`, `clock_kind:null`, `boot_identity:null`),
so the record-before-event post-anchor path stays consistent.

**C3 — reviewed-commit presence over the full pinned union (CLOSED).**
`_preflight_git` now applies the `git cat-file -e {reviewed}:{path}` presence
check to the deduped union of `reviewed_source_paths ∪ GOVERNING_PATHS ∪
PROTOCOL_PATHS` (`activation.py:333-352`), not reviewed source alone. Sol's
remove-at-reviewed-HEAD/restore-at-authorization attack is refused ("pinned path
is absent at reviewed HEAD"). The committed test
`test_every_pinned_path_must_exist_at_reviewed_head` is parametrized over **both**
a governing and a protocol path on disposable `tmp_path` mirrors, matching Sol's
reproduction.

**C4 — closed repository-local call graph with root reachability (CLOSED).**
`verify_production_boundary` now resolves **every** import against the canonical
`repo` and `repo/src` search roots (`resolve_module`/`imported_modules`,
`verification.py:213-276`), handling absolute, relative-level, and package
imports; a repository-local resolution that is omitted from the reviewed set
trips the existing "omitted local dependencies" failure, and any test-world
symbol on the now-included helper is caught. Ambiguous resolution (a name that is
both a module and a package) is rejected; executable **reachability** is computed
by BFS from the declared `PRODUCTION_ROOTS` — missing roots ("executable roots
are unreviewed") and reviewed-but-unreachable sources ("unreachable from roots")
both fail — and the manifest is bound to `sorted(reachable)` and the reachable
edge map, not to "all reviewed Python." The `FORBIDDEN_IMPORT_PREFIXES`
quarantine, dynamic-resolution, and entropy checks apply across the reachable
closure. Independently reproduced Sol's exact case: a reviewed `external_behavior`
importing an omitted repo-local `local_helper` that pulls `evaluate_test_query`
is refused for the omitted dependency, and refused for the test-world symbol once
the helper is included.

## Required-check results

1. **Candidate placeholder empty; E1 alone drives exhaustion — CONFIRMED**
   (constructor/`from_mapping`/`exhausted`/reservation/event-verifier paths;
   C1 reproduced).
2. **Valid/invalid closure hand-traced — CONFIRMED.** Activation-validated claim
   is mandatory at lease creation and record composition; the invalid branch
   requires a process-specific `T_DEVICE_TIME_CHARGED` charge immediately
   followed by a matching hash-bound `T_RUNTIME_INVALID` event and invalidity
   record with coupled cause/state/liability/time; both cross-kind probes and the
   arbitrary-control-map probe refuse. The signed process-record schema and key
   set remain v1 (`PROCESS_RECORD_SCHEMA`; `validate_process_record` unchanged
   key set, with the added type/range/time checks).
3. **Missing-at-reviewed-commit governing and protocol paths refuse — CONFIRMED**
   (parametrized disposable-mirror test; C3 code path).
4. **Module resolution + manifest reachability from all three roots — CONFIRMED.**
   External-module/omitted-helper, ambiguity, missing root, and unreachable
   reviewed-source cases refuse without importing/executing those sources;
   dynamic resolution, entropy, quarantined imports, and test-world symbols are
   rejected on the reachable closure (C4 reproduced).
5. **Tests/verifiers/real-tree — CONFIRMED.** Focused
   `tests/test_officina_{accounting,activation,runtime}.py` → **45 passed**; full
   `pytest` → **267 passed** (was 260; +7 C1–C4 tests, no regression);
   `verify_officina_wp12.py` → OK quarantined/inactive; `verify_inheritance.py` →
   OK 71 files; `verify_officina_active.py` → **exit 1**, failing closed on the
   absent authorization. No authorization, harness, manifest, state, claim,
   record, lease, spend, or runtime output exists; `runtime/` holds only
   `T_RUNTIME.lock`; HEAD `ad0ea10` unchanged.

## New issues

None gating. The bounded repair introduces no concrete, reproducible defect. One
non-gating hygiene note, consistent with Sol's: `tests/test_officina_activation.py`
retains a few harmless trailing no-op expressions; removing them is optional test
cleanup and must not reopen the gate. (Observation, not a repair demand: the
untracked `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V1_DRAFT.md` present in the
worktree is a pre-existing governance-prompt draft, not created by me and not a
harness, manifest, authorization, or runtime artifact; it is outside this diff
and does not bear on the inactive substrate.)

## Scope opened by this verdict

A positive verdict authorizes **only** entry into a separately specified and
reviewed generic metered-harness **design** gate. It authorizes **no** harness
code, production manifest, activation candidate, authorization, activation,
process, lease, capability, world, learner, breathing check, candidate
registration, E1/E2/E3 spend, entropy, Q/C object, datum, outcome, or claim
movement, and no implementation or execution by implication. Activation still
additionally requires the reviewed-and-pinned generic harness and its real
`PRODUCTION_CALL_GRAPH.json`, an exact author-signed authorization committed at
HEAD, and Kirill's explicit `I_AUTHORIZE_OFFICINA_T_ACTIVATION`, before the driver
runs exactly once.

## Negative space

The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its records are non-citable and chose no value here. Officina's T and Q are
permanently non-citable for C1–C6; activation, leases, streams, tuning
observations, breathing checks, draft manifests, E3 reviews, non-finiteness, and
every T ending are non-scientific and move no claim; a future Q pass is a
spendability-gate fact only; S is unavailable; only a valid, independently locked
C execution may ever move an Officina claim, within its selection-conditional,
selected-frame, orientation, device, and learner-seed scope. Censored/`UNKNOWN`/
every invalid state is never success, equivalence, a boundary, or learner
impossibility. `PROOF_CORE`/`PROOF_STRONG` remain earned by nothing; the
programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this review), authorized
nothing, activated no T state, implemented no harness, created no manifest, and
committed nothing. `essay/OUTLINE.md` untouched. My actions were reading the
bounded diff, the Sol/Opus repair confirmations, and the governing/protocol
chain, and running the read-only probes, disposable reproductions, suites,
verifiers, and pristine-tree checks above. The real repository remains
`NOT_ACTIVATED`.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
