# Lock and artifact manifest v0.1

**Status:** DRAFT FOR EXTERNAL REVIEW

This file specifies what must exist and be content-addressed before each irreversible stage.

---

## A. Pre-calibration root

Must be committed before P0 produces an outcome-bearing trajectory.

### Scientific documents

- `PREREGISTRATION_V0.1.md`
- `IMPLEMENTATION_CONTRACT_V0.1.md`
- `CALIBRATION_AND_POWER_PROTOCOL_V0.1.md`
- `ANALYSIS_PLAN_V0.1.md`
- `KILL_MATRIX_V0.1.md`
- `LOCK_MANIFEST_V0.1.md`

### Provenance/config

- exact Level 0 model config copy/reference;
- `MODEL_CONFIG_REF` path;
- SHA256 of the referenced config bytes;
- declared exception/diff file showing only authorized v0.1 deviations;
- Python/package environment lock;
- hardware/runtime declaration template.

### Code

- world generator;
- p_flip calculator;
- deterministic split generator;
- context-code generator;
- paired runner;
- history block trainer;
- fork-probe implementation;
- calibration runner;
- power-N calculator;
- confirmatory analysis code;
- verifier scripts.

### Tests/reports

- exhaustive generator truth report;
- exact p_flip report;
- split-size/hash report;
- context-code non-trainability test;
- k=1 arm-identity test;
- optimizer-reset test;
- fork-nonmutation test;
- deterministic prefix replay report;
- synthetic analysis fixture report.

### Seed machinery

- seed derivation source;
- first 20 derived seeds for each namespace;
- hash of seed test vectors.

### Pre-calibration root record

Machine-readable record should include:

- git SHA;
- timestamp;
- all file SHA256s;
- environment hash;
- model config hash;
- verifier version;
- `scientific_outcome:false`.

Any code/scientific-document change after this point requires a new preregistration version, except generated decision/config artifacts explicitly permitted below.

---

## B. Calibration decision artifact

After P0/P1, write immutable `CALIBRATION_DECISION.json` using the provided template, filled with:

- selected M;
- selected module pool;
- all P0 T/censor values;
- median and Q90;
- B_history;
- tau;
- gate status;
- provenance hashes.

If M=96 escalates, record both the failed M96 decision and the fresh M128 P0 record. Never overwrite the first record.

---

## C. Power-pilot decision artifact

After the six-seed P2/P3 pilot, write immutable `POWER_DECISION.json` containing:

- k1 integrity result;
- headroom metrics;
- per-seed d_i values or their immutable hash;
- sample variance s_d^2;
- one-sided 80% sigma upper bound;
- signed SESOI;
- N_raw;
- final N or `BLOCKED_POWER`;
- code/config/environment hashes.

The script used to create this artifact was already locked in A.

No observed pilot mean may enter any field used by the N formula.

---

## D. Confirmatory lock root

Before any confirmatory model trains, commit:

### Final machine config

- `CONFIRMATORY_CONFIG.json`;
- selected M/pool;
- B_history;
- tau;
- locked N;
- exact list of N confirmatory replicate seeds;
- competence definition;
- SESOI;
- model/config/environment hashes.

### Input/allocation manifests

For every confirmatory seed, pre-generate and hash:

- C modulus;
- H1..H6 order;
- spare modulus;
- train/held-out pair split hash;
- context-code hashes;
- batch-order manifest hashes or deterministic generator root.

The model does not receive these manifests; they are audit artifacts.

### Code re-verification

- runner hash equals pre-calibration locked runner hash;
- analysis hash equals pre-calibration analysis hash;
- no scientific code diff since A;
- deterministic prefix replay passes under final runtime.

### Confirmatory root record

Record all hashes and a public/immutable commitment according to repository governance before the first confirmatory outcome exists.

---

## E. Raw confirmatory artifacts

Per seed/arm:

- config snapshot;
- world allocation;
- boundary checkpoint hashes;
- append-only eval log;
- fork before/after hashes;
- C probe logs k=1,2,4,6;
- H1 reacquisition log;
- completion/validity status;
- runtime/environment fingerprint.

Do not rewrite raw logs after aggregation.

---

## F. Outcome artifacts

Generated only after all locked confirmatory runs finish or terminal invalidation occurs:

- validity report;
- primary analysis table;
- decision JSON;
- fixed figures;
- secondary summaries;
- verifier output;
- final artifact SHA manifest.

The outcome decision must be mechanically reproducible from raw logs + locked analysis code.

---

## G. Conditional diagnostics

`SHUFFLED-TAG`, scrambled-family nulls, LLC/MDL, re-encoding, energetic cells, or Experiment B are **not allowed to modify the confirmatory decision**.

If executed after a licensing outcome, each must have its own preregistered config/analysis lock before its data are generated. The primary v0.1 artifact remains immutable.

---

## H. Review checklist before declaring v0.1 lockable

External reviewer should explicitly answer:

1. Is the scientific manipulation stated as aliased/unlabeled vs separable, rather than contradiction-only?
2. Is `delta_SESOI=ln(1.20)` operationally unambiguous?
3. Is k=1 exact identity actually guaranteed by context-code construction?
4. Does any trainable parameter scale with the number of world IDs?
5. Are history blocks sequential and fixed-budget, never interleaved/early-stopped?
6. Can any C probe mutate main history?
7. Are M/B/tau/N selected only by the signed mechanical gates?
8. Is the independent N the paired-seed count?
9. Does restricted cost clearly disclose saturation?
10. Can a positive result be reported without claiming mechanism/full experience?
11. Is every implementation-relevant Level 0 constant resolved from repository provenance rather than guessed?
12. Is there any unregistered degree of freedom that can be changed after pilot mean is visible?
