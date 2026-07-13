# Y-line review: Level 1 public-root allocation semantics

Verdict: `LEVEL1_PUBLIC_ROOT_ALLOCATION_ACCEPTED`

## Critical findings

None.

## Major findings

None blocking.

1. The implementation matches the signed one-shot public-root randomization semantics. The public root is a single 32-byte value; all allocation randomness is downstream HMAC/counter/Fisher-Yates sampling, with the relevant public allocation domains separated as `dev/h`, `role/pair_slot`, and deferred `sample/N3/h`. This preserves the signed design-based reading under the procedural threat model in `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md:105` and `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md:111`.

2. The root execution script has the scientifically important order: preflight, durable claim, exactly one CSPRNG root draw, allocation transcript, then commit. The claim-before-draw and no-redraw behavior are encoded in `scripts/level1_draw_public_root.py:54`, `scripts/level1_draw_public_root.py:141`, `scripts/level1_draw_public_root.py:157`, and `scripts/level1_draw_public_root.py:168`. The driver was inspected but not executed.

3. Publishing `root + D + roles` immediately is valid under the signed assignment-conditioned finite-frame estimand. The public root is not a sealed evaluator secret; it is explicitly assigned to public allocation and deterministic runtime surfaces, while real evaluator panel word/order/salt/plaintext remain under a separate escrow secret per `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md:143`.

4. A crash after durable claim creation but before root draw would leave a claim-only state. That state is not a root-selection bias because no entropy has been drawn, and current preflight refuses rerun while the claim exists. Before any real execution, operators should treat any claim-only, transcript-only, or invalidity artifact state as requiring signed invalidity/recovery review rather than rerun-by-convenience.

## Minor findings

1. `scripts/level1_draw_public_root.py:63` and `scripts/level1_draw_public_root.py:65` enforce tracked working-tree and index cleanliness but do not reject unrelated untracked files. This is not verdict-moving for randomization because the transcript binds the expected HEAD and governing spec hashes, and untracked review artifacts cannot alter the tracked driver/code that will be committed with the transcript. If desired, an operational checklist may separately record `git status --porcelain` for process hygiene.

2. The transcript schema binds environment metadata and witness process facts, not scientific choices. The witness statement is limited to process facts and explicitly disclaims cryptographic independence in `src/philosophia/level1/public_root.py:83`.

3. The current tests check fixed-root allocation counts and a golden canonical transcript hash, not a separately printed table of the exact six development pair slots and twenty-four role assignments. That is sufficient for this bounded review because the golden transcript hash plus count assertions pin the serialization output, but a human-facing post-draw verification table would improve audit ergonomics.

## Required questions

### 1. Public root and design-based randomization

Yes. `scripts/level1_draw_public_root.py:157` draws exactly one 32-byte root using `secrets.token_bytes(32)`, and `src/philosophia/level1/public_root.py:59` rejects non-32-byte roots. Downstream allocation uses `DeterministicKey(root, purpose="public-root")` at `src/philosophia/level1/public_root.py:98`, with the HMAC/counter/Fisher-Yates machinery in `src/philosophia/level1/serialization.py:51`, `src/philosophia/level1/serialization.py:71`, `src/philosophia/level1/serialization.py:80`, and `src/philosophia/level1/serialization.py:106`. This restores the signed randomization reading without claiming cryptographic independence beyond the stated procedural threat model.

### 2. Development pairs and role assignments

Yes. `src/philosophia/level1/allocation.py:49` samples exactly two development pairs per stratum using domain `("L1", "alloc", "dev", stratum)`, yielding six development pairs total. `src/philosophia/level1/allocation.py:72` assigns all twenty-four outcome target/donor roles once using domain `("L1", "alloc", "role", pair.slot)`. `src/philosophia/level1/public_root.py:99` materializes the development pairs into the transcript, and `src/philosophia/level1/public_root.py:108` materializes all outcome role assignments.

The unit test re-derives the fixed-root counts: six development pairs, two per stratum, twenty-four roles, and eight roles per stratum in `tests/test_level1_public_root.py:65`. The golden canonical transcript hash is checked in `tests/test_level1_public_root.py:35`, binding the fixed-root serialization.

### 3. Absence and deferral of `R_h`

Yes. The public transcript reports `"outcome_sample": "deferred-until-N3"` at `src/philosophia/level1/public_root.py:120`. The public-root driver imports `derive_public_allocations` but not `sample_outcome_pairs`, and `tests/test_level1_public_root.py:129` regression-checks that `sample_outcome_pairs` is absent from the driver source. The `R_h` sampling function exists separately at `src/philosophia/level1/allocation.py:80`, keyed by `("L1", "alloc", "sample", n3, stratum)` at `src/philosophia/level1/allocation.py:90`, and is therefore mechanically deferred until frozen N3.

No feasibility, censoring, loss, or contrast information can regenerate D/roles through the reviewed path: artifact existence checks reject a second attempt before draw in `scripts/level1_draw_public_root.py:67`, failures after the draw path write invalidity rather than redraw in `scripts/level1_draw_public_root.py:170`, and no-redraw is also bound into the transcript in `src/philosophia/level1/public_root.py:80`.

### 4. Scientific validity of publishing root, D, and roles

Yes. Immediate publication of root, development allocation, and target/donor roles is scientifically valid under the signed procedural threat model because the estimand conditions on the fixed finite frame and assigned seed schedule, not on hidden allocation. The signed public/secret split says the public root may derive allocation, initialization, replay, controls, and feasibility surfaces, while evaluator panel realization remains escrow-secret sealed in `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md:143`.

This is timing transparency, not a new inferential degree of freedom. It does not authorize changing architecture, endpoint, margins, estimator, N3, or panel construction after seeing the public root.

### 5. Provenance, inclusion probabilities, and FPC auditability

Yes. The transcript binds `root_hex`, `git_head_before_draw`, timestamp, environment, environment fingerprint, required spec hashes, governing lineage hashes, allocations, process attestation, witness attestation, and forbidden derivations in `src/philosophia/level1/public_root.py:61`. The required v3/v3.1 spec hashes are computed in `scripts/level1_draw_public_root.py:135`, and the governing lineage through v3.1.4.1 plus signatures is hashed in `scripts/level1_draw_public_root.py:138`.

The allocation frame is auditable because `registry_pairs()` defines eight adjacent pairs per stratum at `src/philosophia/level1/allocation.py:41`, `outcome_pairs()` excludes development pairs and asserts eight outcome pairs per stratum at `src/philosophia/level1/allocation.py:63`, and the eventual FPC denominator remains the signed stratum size of eight. From the fixed test root `bytes(range(32))`, tests re-derive the six development pairs and twenty-four roles, then compare the canonical transcript hash `cecd64d27b9a053e54ba690ed16354c11efeb3caae9b6ada90b8c2cd5c3dfbb6` at `tests/test_level1_public_root.py:60`.

### 6. Evaluator-panel secrecy

The public root and transcript do not reveal the real evaluator-panel word set, order, salt, or plaintext. `src/philosophia/level1/public_root.py:87` explicitly lists forbidden derivations including real evaluator panel, raw panel realizations, panel ordering, encryption salt, and escrow plaintext. This matches the public-root/escrow-secret boundary in `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md:143`.

### 7. Failure, invalidity, and selection among roots

The reviewed path does not permit selection among roots. Before entropy, `_preflight()` refuses an existing transcript, claim, invalidity artifact, or temporary artifact in `scripts/level1_draw_public_root.py:67`. The claim is durably created before entropy at `scripts/level1_draw_public_root.py:147`, and any failure after entropy routes to an invalidity artifact with `required_action: signed invalidity decision; never redraw` in `scripts/level1_draw_public_root.py:93` and `scripts/level1_draw_public_root.py:170`.

Failure before any entropy draw is not root selection. Failure after durable claim creation is procedurally locked against casual rerun by the same preflight checks. The only acceptable path after an ambiguous artifact state is signed invalidity/recovery review, not another draw.

### 8. Environment and witness fields

Environment and witness fields are scientific metadata, not new scientific degrees of freedom. `scripts/level1_draw_public_root.py:78` records runtime environment facts; `src/philosophia/level1/public_root.py:32` hashes the environment dictionary; and `src/philosophia/level1/public_root.py:83` limits witness attestation to process facts about signature visibility, durable transcript write, and follow-up commit. These fields help audit provenance and do not affect allocation probabilities.

### 9. Remaining pre-execution and post-execution checks

Before a single real root execution may be authorized, the operator must verify:

1. The expected HEAD is the reviewed HEAD to be supplied with `--expected-head`.
2. No claim, transcript, invalidity, or temporary allocation artifact exists at the paths checked in `scripts/level1_draw_public_root.py:25`.
3. The tracked working tree and index are clean, as required by `scripts/level1_draw_public_root.py:63` and `scripts/level1_draw_public_root.py:65`.
4. The governing lineage files through v3.1.4.1 and both signature records exist and hash successfully, as required by `scripts/level1_draw_public_root.py:32` and `scripts/level1_draw_public_root.py:72`.
5. The reviewed public-root unit test and full suite still pass immediately before execution.

After the single execution, the operator must verify:

1. The transcript has schema `level1.public_root_transcript.v1`, `scientific_outcome: false`, exactly one 32-byte `root_hex`, and `os_csprng_calls: 1`.
2. The transcript contains exactly six development pairs, two per stratum, and exactly twenty-four outcome role assignments, eight per stratum.
3. `outcome_sample` remains deferred until N3.
4. The transcript hashes match the signed spec lineage and the committed HEAD.
5. No real evaluator-panel derivation, feasibility/scout run, N3 selection, lock, escrow, trajectory, or outcome artifact is produced by this step.

## Tests run

- `.venv/bin/python -m pytest tests/test_level1_public_root.py` — 7 passed.
- `.venv/bin/python -m pytest` — 129 passed.

## Mandatory edits

None.

## Gate boundary

This review accepts the reviewed public-root allocation semantics and permits only committing the reviewed code/review artifacts. A single public-root execution may be authorized later only after the pre-execution checks above are satisfied and the responsible signatory explicitly invokes that gate. This review does not authorize entropy execution, feasibility, comparative scout, N3 selection, lock, escrow, learner trajectory, or outcome.
