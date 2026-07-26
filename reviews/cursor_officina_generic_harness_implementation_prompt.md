# Cursor task: implement the signed Officina batch settlement and generic harness

Work in:

```text
/home/master/llm_projects/philosophia
```

This is a mechanical implementation task against a signed contract. Do not
redesign the protocol, choose scientific values, activate T, or create any real
runtime artifact.

## Authority

Author signature:

```text
successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
sha256 8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a
signature commit 1142e6432748f8065d4a5cb44b74a9d49bcdbcab
```

The two accepted tokens, in their normative order, are:

```text
I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT
I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT
```

Read the signature first. Then treat the following as one ordered composite
contract. Later corrections replace only their named loci:

1. `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md`
2. `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md`
3. `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`
4. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md`
5. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md`
6. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md`
7. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md`
8. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`

The closure and final confirmations are review evidence:

```text
reviews/fable_officina_batch_settlement_v1_1_1_closure.md
reviews/opus_officina_batch_settlement_v1_1_1_final_confirmation.md
reviews/sol_officina_batch_settlement_v1_1_1_final_confirmation.md
```

Do not use chat-response captures as normative sources when a formal artifact
above answers the same question.

## Required implementation

Implement in this order.

### 1. Bounded accounting amendment

Modify `src/philosophia/officina/accounting.py` only as authorized:

- add the frozen `BatchSettlementAuthority` value object;
- add the pure
  `TState.charge_batch_settlement(value, envelope, authority)` path;
- enforce validated-claim binding, expected state/head binding, exact
  process/value/order membership, one-use consumption, and every mismatch,
  substitution, omission, replay, reordering, and value-increase refusal in the
  governing amendment;
- preserve exact integer conservation, including multiple valid charges after
  the first charge crosses E1;
- leave `TState.charge_device_nanoseconds` behavior unchanged.

Add focused accounting tests, including the signed 60/60/60 counterexample,
ordinary post-cap refusal, authority non-reuse, wrong process/value/order,
stale state/head, and prefix reconstruction cases.

Do not change `runtime.py`, `ledger.py`, or `checkpoint.py`.

### 2. Generic harness

Create `src/philosophia/officina/generic_harness.py` and implement the complete
governing contract:

- lifecycle tables and total terminal/dominance routing;
- refusal-first durable transaction ordering and every specified crash cut;
- reservation, per-stream classification, frozen-batch claim construction and
  validation, inline `meter_evidence`, per-process aggregation, unknown-pool
  allocation, settlement automaton, registry, override, and conservation
  checks;
- amendment-authorized head/cache completion only under all six v1.1.1
  preconditions;
- process supervision and isolation/promotion;
- ordinary pause, generational pending-resume checkpoints, overdue review, and
  closed recovery-disposition handling;
- closed non-outcome decision/input schemas;
- CPU meter adapter;
- module `__main__` CLI with exactly the signed commands:
  `claim`, `start`, `heartbeat`, `close`, `pause`, `resume`;
- pre-WP-6 refusals and recursive rejection of scientific/learner/result
  fields.

Use the repository's existing canonical JSON, ledger, runtime, checkpoint,
activation, quarantine, and terminal APIs. Do not duplicate or replace their
signed constructors. The batch path must not call `settle_active_lease` or
`settle_monotonic_delta`.

### 3. Executable acceptance matrix

Create `tests/test_officina_generic_harness.py` plus narrowly scoped test-only
helpers if required. Cover every row of v2 section 10 as corrected by v2.1,
v2.2, v2.3, and v2.3.1, not merely happy paths.

At minimum, mechanically prove:

- every lifecycle transition and every durable crash cut;
- valid close ordering and impossibility of event-before-record;
- live-process and no-process invalidity artifact sets;
- G5 revocation with one through three siblings;
- all recovery-charge classes and the exact unknown-pool quotient/remainder;
- zero, one, and multiple E1 crossings, including 60/60/60;
- exact lease/charge hash chaining and rest-state conservation;
- all dominance pairs and invalid-cause precedence;
- the sole permitted batch head/cache completion and each of its six
  precondition failures;
- inline evidence exact keys, recomputation, timely/late boundary, unknowable
  nullability, recursive scientific-field rejection, and duplicate-field
  rejection;
- isolation escape/fault cases using disposable roots and fake
  clocks/meters/processes only;
- repeated pause/resume generations and all recovery paths;
- pre-WP-6 and Q/C whole-artifact refusals;
- root/import/static-graph invariants that can be tested without creating the
  production call-graph manifest;
- no invalid process or programme ending can be relabelled as valid.

All tests must be test-only and non-production-compatible. They must create no
artifact under the real `successor/officina/runtime/` tree.

## Immutable boundary

These files and surfaces are frozen for this task:

```text
src/philosophia/officina/runtime.py
src/philosophia/officina/ledger.py
src/philosophia/officina/checkpoint.py
src/philosophia/officina/verification.py
scripts/officina_activate_t.py
scripts/verify_officina_active.py
successor/officina/runtime_control/
```

Do not:

- alter signed events, schemas, constants, roots, import allowlists, or phase
  rules;
- add another `scripts/*.py` entry point;
- create
  `successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json`;
- create an activation authorization, capability, real T artifact, world,
  learner, process, entropy, device spend, candidate, Q/C artifact, result, or
  decision;
- modify any scientific contract, review, essay, README, roadmap, ledger, or
  signature file;
- commit or push.

`generic_harness.py` must stay within the currently pinned import allowlists.
No dynamic import, reflection, hidden entropy, backend import, test capability,
predecessor dependency, `signal`, `threading`, or `multiprocessing`.

The only intended production-code changes are:

```text
M src/philosophia/officina/accounting.py
A src/philosophia/officina/generic_harness.py
```

The intended test changes are:

```text
M tests/test_officina_accounting.py
A tests/test_officina_generic_harness.py
```

If the signed behavior cannot be implemented within that surface, stop and
report the exact contradiction with file/section and existing API references.
Do not widen the file set silently.

## Existing dirty work

The worktree contains unrelated user/reviewer edits. Preserve them byte for
byte and do not stage them:

```text
reviews/fable_officina_batch_settlement_v1_1_1_author_choices_prompt.md
reviews/fable_officina_batch_settlement_v1_1_repair_prompt.md
reviews/fable_officina_generic_harness_contract_v2_1_prompt.md
reviews/fable_officina_harness_v2_2_core_amendment_prompt.md
reviews/fable_officina_independent_programme_validation_prompt.md
reviews/opus_officina_wp4_anchor_confirmation_chat_response.md
reviews/sol_officina_batch_settlement_v1_1_1_final_confirmation_chat_response.md
reviews/sol_officina_wp3_v2_1_final_confirmation_chat_response.md
reviews/sol_successor_charter_v1_review_prompt.md
essay/OUTLINE.md
```

If additional unrelated changes appear, leave them untouched and report them.

## Verification

Run:

```bash
.venv/bin/python -m pytest -q tests/test_officina_accounting.py
.venv/bin/python -m pytest -q tests/test_officina_generic_harness.py
.venv/bin/python -m pytest -q
.venv/bin/python scripts/verify_inheritance.py
.venv/bin/python scripts/verify_all.py
.venv/bin/python scripts/verify_officina_wp12.py
.venv/bin/python scripts/verify_officina_active.py
```

The WP-1/WP-2 verifier must remain green. The active verifier is expected to
return nonzero and remain fail-closed solely because no activation authorization
and no production call-graph manifest exist. Report its exact expected
refusals; do not make it green by creating either object.

## Report back

Return:

1. exact files changed;
2. tests added, grouped by contract section;
3. command results and pass counts;
4. confirmation that T is still `NOT_ACTIVATED` and the production manifest is
   absent;
5. any ambiguity or contract/API mismatch, without resolving it by discretion;
6. `git diff --check` result and `git status --short`;
7. no commit.
