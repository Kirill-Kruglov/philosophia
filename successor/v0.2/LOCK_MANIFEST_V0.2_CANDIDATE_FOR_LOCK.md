# Lock and artifact manifest v0.2 — candidate for lock

**Status:** CANDIDATE FOR LOCK

This file specifies what must exist and be content-addressed before each irreversible stage.

---

## A. P-1 provenance record — before other lock work

Required:

- exact `MODEL_CONFIG_REF` path;
- SHA256 of config raw bytes;
- provenance link to Level 0 paper-mainline use;
- v0.2 declared-diff file.

If unavailable -> `BLOCKED_CONFIG_PROVENANCE`.

---

## B. Pre-calibration root — before P0

### Scientific documents

- preregistration v0.2;
- implementation contract v0.2;
- calibration/power protocol v0.2;
- analysis plan v0.2;
- conditional SHUFFLED_TAG protocol v0.2;
- kill matrix v0.2;
- lock manifest v0.2;
- review disposition v0.2.

### Provenance/config

- Level 0 config ref/copy/hash;
- declared exception diff;
- environment lock;
- hardware/runtime template.

### Primary code

- world generator;
- p_flip calculator;
- split generator;
- context generator;
- position-layout implementation;
- paired runner;
- history trainer;
- fork probe;
- calibration selector;
- dual-target power calculator;
- primary analysis/heavy-cap sign gate;
- verifier.

### Conditional diagnostic code — required before primary confirmation exists

- SHUFFLED_TAG balanced schedule generator;
- diagnostic runner;
- V/I analysis and 97.5% CI implementation;
- diagnostic sign-gate implementation.

### Tests/reports

- exhaustive world truth report;
- exact p_flip report;
- split size/hash report;
- no trainable per-world context capacity test;
- position/max-position/readout test;
- k1 arm identity unit test;
- optimizer reset test;
- fork nonmutation test;
- SHUFFLED_TAG no-world-code association/balance test;
- D0 duplicated deterministic smoke;
- synthetic primary analysis fixture;
- synthetic heavy-cap fixture;
- synthetic SHUFFLED_TAG decomposition fixture.

### Seed machinery

- seed derivation source;
- first 20 values per namespace;
- seed-vector hash.

### Root record

Record git SHA, timestamp, all file hashes, environment/model hashes, verifier version, `scientific_outcome:false`.

Any scientific/code change after P0 requires a new preregistration version except immutable generated artifacts below.

---

## C. Calibration decision artifact

After P0/P1 write immutable `CALIBRATION_DECISION.json`:

- all attempted scale records;
- selected M/pool;
- all P0 T/cap values;
- median/Q90;
- B_history/tau;
- provenance hashes.

If M96 escalates, preserve failed M96 record; do not overwrite.

---

## D. P1.5 determinism artifact

Before P2 write immutable `DETERMINISM_FULL_REPLAY.json` containing two full-run artifact roots for same dedicated seed:

- init;
- full H1 trajectory;
- H1 final state;
- k1 C probe through criterion/tau;
- equality verdict.

Must PASS.

---

## E. Power decision artifact

After P2/P3 write immutable `POWER_DECISION.json`:

- k1 integrity/headroom gates;
- per-seed d_i hash;
- s_d and sigma_U;
- Delta;
- N_sup;
- N_eq;
- final N;
- `BLOCKED_POWER` if >128;
- code/config/environment hashes.

Observed pilot mean must not enter N calculation.

---

## F. Confirmatory root — before primary confirmation

Commit:

### Final config

- `CONFIRMATORY_CONFIG.json`;
- M/pool/B_history/tau/N;
- exact N seed list;
- competence rule;
- Delta;
- HEAVY_CAP threshold=0.10;
- point-estimate SESOI interpretation;
- conditional SHUFFLED_TAG trigger policy.

### Input/allocation manifests per seed

- C/H1..H6/spare;
- pair split hash;
- context vector hashes;
- batch-order root;
- model init root.

### Code verification

- primary runner/analysis hashes equal pre-calibration root;
- SHUFFLED_TAG runner/analysis hashes equal pre-calibration root;
- no scientific code diff;
- duplicated full deterministic replay passes under final runtime.

### Confirmatory root record

Public/immutable content hash before first primary outcome.

---

## G. Raw primary artifacts

Per seed/arm:

- config snapshot;
- allocation;
- boundary model hashes;
- append-only eval logs;
- fork before/after hashes;
- C k=1,2,4,6 logs;
- H1 reacquisition;
- context/token norm drift records;
- completion/validity;
- runtime fingerprint.

---

## H. Primary outcome artifacts

Only after all primary runs finish or invalidate:

- validity report;
- primary analysis table;
- heavy-cap report;
- sign-gate output if activated;
- decision JSON;
- fixed figures;
- secondary summaries;
- verifier output;
- artifact hash manifest.

Primary decision must be reproducible mechanically from locked analysis + raw logs.

---

## I. Mandatory conditional SHUFFLED_TAG root/execution

Its **code/config semantics are already locked in F**.

If trigger fires, before executing the first SHUFFLED_TAG history write a generated `SHUFFLED_TAG_CONFIG.json` containing:

- reference to primary confirmatory root;
- exact same N seed list;
- same M/pool/B_history/tau/model/environment hashes;
- exact schedule-generator hash;
- locked diagnostic analysis hash;
- trigger primary status/hash.

This generated file contains no tunable value.

Raw diagnostic artifacts per seed:

- schedule hash/code counts per world block;
- history boundary hashes;
- k6 C probe;
- cap flag/runtime.

Outcome artifacts:

- V/I estimates and 97.5% CIs;
- diagnostic sign gates if needed;
- component annotation;
- verifier/hash manifest.

If required diagnostic cannot reach valid N, status=`DIAGNOSTIC_INCOMPLETE`; primary category remains but component attribution is forbidden.

---

## J. Structural/mechanistic follow-ups

Scrambled-family null, LLC/MDL, re-encoding, energetic cell, Experiment B each require a separate future preregistration. They cannot change the v0.2 primary category.
