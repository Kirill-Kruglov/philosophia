REVISE_OFFICINA_WP4_SCOPE

# Review boundary and outcome

I reviewed the signed WP-3 record and the complete WP-4 implementation delta `de8aa1e^..a8cbd91` at the current HEAD. The committed delta `a8cbd91..HEAD` contains only the two WP-4 review prompts; no load-bearing source differs. The deterministic frame/oracle substrate is scientifically inert and matches the selected LOW/C_RICH population. However, two dataflow boundaries are not mechanically true: the test T-contact hook can append to the committed genesis ledger, and the public test factory can issue Q/C-labelled oracle capabilities before the corresponding roots exist and return untagged response bytes. A bounded hardening and focused review are required before any T-activation candidate may be prepared.

# Findings

## Critical

1. **The temporary T-contact hook can write the committed T ledger.** `src/philosophia/officina/world.py:289-327` accepts an arbitrary ordinary `AppendOnlyLedger`, ordinary `TState`, and ordinary `TEnvelope`. Its only authority check is the publicly issued test capability. It never inspects or constrains `ledger.path` or `ledger.head_path`, requires no test-ledger provenance/token, and does not distinguish a temporary accounting state from a future production state. `AppendOnlyLedger.append` at `src/philosophia/officina/ledger.py:179-211` will accept the currently valid genesis ledger/head and durably append the `T_TEST_ONLY_WORLD_CONTACT` event.

   The following counterexample is admitted by the types and checks, but I did **not** execute it because it would mutate the protected artifact:

   ```python
   cap = test_world_capability(
       Surface.T,
       capability=test_only_capability("counterexample"),
       purpose="counterexample",
   )
   ledger = AppendOnlyLedger(
       Path("successor/officina/T_LEDGER.md"),
       head_path=Path("successor/officina/T_LEDGER.md.head.json"),
   )
   state = TState().activate("2026-07-21T00:00:00Z")
   record_test_t_contact(
       capability=cap,
       modulus=10,
       raw_query=canonical_json({"u": "", "v": ""}),
       device_nanoseconds=1,
       timestamp_utc="2026-07-21T00:00:01Z",
       state=state,
       envelope=TEnvelope(),
       ledger=ledger,
   )
   ```

   The committed test at `tests/test_officina_world.py:137-181` demonstrates only the happy path on `tmp_path`; it does not enforce that path in the implementation or test refusal of the committed ledger. This contradicts the implementation claim at `successor/OFFICINA_WP4_IMPLEMENTATION.md:14-16,20-23`, the inactive genesis guarantee at `successor/OFFICINA_WP3_SIGNATURE.md:56-65`, and mandate item 4. A caller could manufacture an apparently valid activated `TState`, charge it, and persist the test event in the real ledger even though no activation decision occurred. The inactive verifier would detect the damage afterward, but detection is not prevention.

## Major

2. **Q/C “test surface” capabilities are publicly issuable and their responses lose the test-only label.** `src/philosophia/officina/interlock.py:33-39` publicly issues the prerequisite `TestOnlyCapability`; `world.py:70-78` then publicly issues `TestWorldCapability` for exact `Surface.Q` and `Surface.C`; `world.py:273-286` returns bare canonical response bytes. The committed tests at `tests/test_officina_world.py:111-120` exercise the actual selected Q modulus 28 and C modulus 26 before either real root exists.

   This code cannot currently create a Q attempt, consume the reserve, emit a competence binary, alter `H_preC`, or execute C: no attempt/journal/root/driver exists, and the real interlock routes at `interlock.py:54-61` always refuse. The responses are test calculations and are not scientific evidence. Nevertheless, the mechanism is not mechanically non-promotable in the form claimed. Any caller can mint the issuer chain, the capability carries the real Q/C surface enum rather than a distinct fixture kind, and the returned bytes carry no test-only provenance. That weakens the signed invariant at `OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md:243-255` that Q/C capability objects and frame/reserve oracle exposure do not exist before their roots. Naming a publicly mintable object “test-only” is not enough once its output is indistinguishable from an oracle answer.

   Q/C membership and refusal tests are legitimate engineering tests, but they do not require a pre-root Q/C oracle capability. The frame mapping can be checked purely, T capability can be tested to refuse all frame/reserve moduli, and oracle semantics can be exercised on a T or separately typed dummy-fixture modulus. Real Q/C capability types must first appear at their signed gates.

## Minor

None. The remaining observations below are confirmations or later-gate obligations, not defects in this bounded WP-4 substrate.

# Confirmed scientific/dataflow surfaces

## Signed frame and construct

The constants at `src/philosophia/officina/world.py:22-41` pin exactly the signed choices:

- `CH1_TOKEN=I_SELECT_OFFICINA_FRAME_BAND_LOW`, `N_MIN=26`, `N_MAX=65`, `LAMBDA=140`;
- `CH2_TOKEN=I_SELECT_OFFICINA_SPLIT_C_RICH`, `C_POSITIONS={1,3,5}`, `Q_POSITIONS={2,4}`;
- four strata, five adjacent blocks each, 12 registered C blocks and 16 Q-reserve worlds;
- T-dev bands `[10,25]` and `[166,205]`, disjoint from the registered frame and predecessor band.

`_frame_blocks` and `_validate_frame` at lines 90-156 recompute every `(h,j,p,members,assignment)` from those fixed constants and reject ordering, membership, overlap, cardinality, or stratum-balance drift. `frame_mapping` at lines 159-181 emits the exact signed schema, tokens, contract hash, derived C block positions, and Q worlds. It accepts no band/split argument and contains no alternative selected branch.

This mapping is the public deterministic definition of the registered finite population. Its `assignment="C"` labels identify the 12 blocks eligible for later C sampling; they are not a realized C membership sample. Calling `frame_mapping`, `frame_bytes`, or `frame_sha256` creates no post-lock root, orientation, sample, or result.

## Absent OR-2 and scientific objects

The WP-4 code contains no OR-2 token or implementation, C root, full orientation vector, orientation/sample PRF domain, `C_design_realization_id`, sample draw, learner seed, learner, donor, arm, endpoint, budget, margin, alpha, estimator, inferential method, trajectory, or scientific terminal. `scientific_outcome` is fixed `False` in both the frame mapping (`world.py:175`) and test-contact entry (`world.py:322`). This is the correct absence at this gate.

## No estimator or widened claim

The implementation serializes frame strata and membership only. It does not serialize `W_h`, `pi_h`, FPC, `n_h`, a contrast, a variance, or any estimator; it therefore cannot silently perform finite-frame inference. The code and WP-4 record introduce no exchangeability, superpopulation, construct-wide, learner-class, or expected-success statement. The signed weights and sampling quantities remain future WP-9/WP-10 inputs, not executable WP-4 calculations.

## Q-to-C transport

The signed transport token remains documentary and unexercised. Nothing in WP-4 tests a competence predicate, target-side spendability, donor/yoke behavior, or a C treatment contrast. No pass/fail field exists. After Major 2 is repaired, the code will cleanly preserve the rule that only a future valid Q pass under the separately signed WP-6 contract can supply the routing fact; it still cannot become C evidence.

## Production timer/transaction/run absence

The deliberately absent production timer, activation transaction, state checkpoint, learner loop, and run path at `successor/OFFICINA_WP4_IMPLEMENTATION.md:18-26` are scientifically correct, not an incomplete world substrate. The WP-3 signature at lines 49-61 authorized the pure construct, exact frame, capability-gated T substrate, logging hooks, and tests, while expressly requiring bounded WP-4 review before a separate activation decision. A real timer/transaction/driver would itself be the load-bearing activation candidate and must not be smuggled into this implementation review.

The pure oracle and frame are sufficient as the signed-world substrate. A later candidate must add, under separate review, an exact production T capability, atomic activation/state/ledger transaction, E1 concurrency timer, E2 candidate registry integration, E3 review gates, pause/resume behavior, learner isolation from test/Q/C APIs, and fail-closed hash/path pins. Its preparation is not eligible until the two current blockers are closed.

# Exact mandatory repairs

R1. **Make the test contact ledger/state mechanically test-only.** `record_test_t_contact` must not accept a raw `AppendOnlyLedger`, `TState`, and `TEnvelope` that are type-identical to future production objects. Require an exact internally issued test-contact harness (or equivalent unforgeable wrapper) that owns its ledger and test accounting state. Its factory must:

- require the existing test-only capability;
- create a fresh ledger/head under an explicitly temporary root outside the repository and outside `successor/officina`;
- resolve paths before use and reject symlink aliases, hard-link/inode aliases, the committed ledger/head, and any repository-native ledger;
- ensure the test ledger is newly initialized and cannot be substituted after issuance;
- keep the fake activated state internal and return it only as test state, never as a production checkpoint.

The hook must validate that wrapper and protected-path separation **before** evaluating a query, charging state, or writing. Add regression tests that (a) an ordinary caller-supplied `AppendOnlyLedger` is rejected, (b) direct, relative, symlink, and hard-link aliases of the committed ledger/head are rejected without byte/hash change, (c) a temporary issued harness still logs `T_TEST_ONLY_WORLD_CONTACT`, and (d) the committed envelope, ledger, and external head remain byte-identical genesis before and after the suite.

R2. **Remove pre-root Q/C-labelled oracle capabilities from the production module.** Before WP-6/WP-10, `test_world_capability` must not issue exact `Surface.Q` or `Surface.C`, and no source callable may accept such a test capability to return an oracle answer. Replace those tests with:

- pure checks of the registered Q/C modulus sets and frame assignments;
- T-capability refusal checks for every frame/reserve modulus; and
- oracle/classifier tests on the authorized T test surface or a separate test-fixture kind that is not `Surface.Q`/`Surface.C`, carries explicit non-promotable provenance through its result type, and cannot be admitted by any production/Q/C API.

Add tests that Q/C issuance is refused before roots, no selected Q/C modulus can be evaluated through a test/T capability, the real `launch_q`/`execute_c` refusals remain, and no test result can enter `ArtifactStore.admit` for Q/C. This repair changes no frame member, construct answer, transport premise, or future root design.

# Checks run

I ran only permitted non-outcome checks:

```text
.venv/bin/python -m pytest -q \
  tests/test_officina_world.py \
  tests/test_officina_bootstrap.py \
  tests/test_officina_governance.py \
  tests/test_officina_accounting.py
63 passed in 2.27s

.venv/bin/python scripts/verify_officina_wp12.py
OK: Officina WP-1/WP-2 bootstrap is quarantined and inactive.

git diff --check de8aa1e^..a8cbd91
passed
```

Static import/search inspection found no stopped-line import or path in the WP-4 source. The verifier checked every `src/philosophia/officina/*.py` file for forbidden predecessor imports, entropy references, dynamic imports, and random-device paths. The signed contract/signature hash test passed. No comparative or feasibility outcome supplies a WP-4 constant. After the suite, `successor/officina/T_ENVELOPE.json` remains `activated:false`; `T_LEDGER.md` remains the exact `NOT_ACTIVATED` header with no entry; and `T_LEDGER.md.head.json` remains at genesis count 0/hash zero.

# Next-step boundary and negative space

This review authorizes only bounded repairs R1-R2 and a focused WP-4 confirmation. It does **not** authorize preparation of a T-activation candidate yet. If both repairs receive bounded confirmation, the eligible next step may be only preparation of a separately reviewed T-activation candidate implementing the production transaction/timer/driver boundaries named above. Neither that preparation nor this review authorizes activation.

I created no real world, entropy, frame realization, sample, panel, candidate, manifest, committed ledger event, Q/C root, orientation vector, `C_design_realization_id`, lock, escrow, T/Q/C execution, scientific datum, outcome, Proof, or claim movement. Temporary pytest fixtures and ledgers were confined to pytest temporary storage and are non-citable. T remains `NOT_ACTIVATED` at genesis. The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; no stopped-line artifact was read by WP-4 and its outcomes selected nothing. Officina T/Q test activity is never C1-C6 evidence. No qualification, contrast direction, learner capability, or programme success is predicted.
