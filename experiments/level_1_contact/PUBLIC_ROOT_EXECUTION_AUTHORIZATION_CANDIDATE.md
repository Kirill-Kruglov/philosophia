# Level 1 public-root execution authorization candidate

Status: `AWAITING_KIRILL_ONE_SHOT_TOKEN`. This record does not itself authorize
or perform an entropy draw.

## Reviewed implementation

```text
REVIEWED_CODE_HEAD=95adcb5011c170fe9076894f6439f1248538600f
XLINE_VERDICT=LEVEL1_PUBLIC_ROOT_DRIVER_CONFIRMED
YLINE_VERDICT=LEVEL1_PUBLIC_ROOT_ALLOCATION_ACCEPTED
```

The six byte-identical execution paths are:

```text
scripts/level1_draw_public_root.py
src/philosophia/level1/public_root.py
src/philosophia/level1/allocation.py
src/philosophia/level1/serialization.py
src/philosophia/level1/model.py
src/philosophia/level1/config.py
```

## Expected-HEAD binding

Kirill's exact token is:

```text
I_AUTHORIZE_LEVEL1_PUBLIC_ROOT_DRAW_FROM_THIS_SIGNATURE_COMMIT
```

After Kirill supplies it, Codex may create exactly one new tracked file,
`experiments/level_1_contact/PUBLIC_ROOT_EXECUTION_SIGNATURE.md`, containing the
token and this authorization-contract commit. The commit adding that file must
contain no source/spec/test changes. **The hash of that signature-only commit is
by definition `EXPECTED_HEAD`.** No tracked commit or modification may occur
between it and the draw.

This construction avoids a self-referential hash: the immutable commit containing
the authorization is the value passed to `--expected-head`, while
`--reviewed-code-head` remains the reviewed implementation commit above.

## Governing lineage hashes

```text
ba2c2d4db9938a19839cb10d5a912f7395c72a1c71a4fa82a2ba5f8a86354e36  SCIENTIFIC_SPEC_V3_DRAFT.md
90b429be96da5fb3be17dd114edc17563c31e964be5f1a1a4ebe00b8cc68fd92  SCIENTIFIC_SPEC_V3_1_ADDENDUM.md
7b2177f9668965bdbf7f826cad54b336b692a33db266b7b900bf13e6f8c76999  SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md
1aba5dcf271a4d3ce4ed8314b6a00e50d00d108f2444866fe6ca475d5a9a0721  SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md
d95739230b74b94e6cd284296fbf6af78e494d7e69de3c43d941a6bdaf24aebf  SCIENTIFIC_SPEC_V3_1_3_CORRECTION.md
f483134926ffff58d2182c23ab71fdd8b86db1c00d08a7441df45b20af46bfce  SCIENTIFIC_SPEC_V3_1_4_PANEL_ADDENDUM.md
6d16930446fbc8f626237120e9515fe9052e34753a56c34b579a27282bac43c0  SCIENTIFIC_SPEC_V3_1_4_1_PANEL_CORRECTION.md
2d76bdb6841c11e46420914721bee12ca7ea9e978ffda947d9ea8ccbec7e0251  SCIENTIFIC_SPEC_SIGNATURES.md
f0956d48b3081f82fa9320e992934fcd0a3c6294c509f86f59941ac2e62693f2  PANEL_CONTRACT_SIGNATURE.md
```

Paths are relative to `experiments/level_1_contact/`.

## Pre-execution predicates

All must pass immediately before the single invocation:

1. `EXPECTED_HEAD == git rev-parse HEAD` and its parent contains this candidate.
2. `git diff --quiet REVIEWED_CODE_HEAD EXPECTED_HEAD -- <six paths>` succeeds.
3. Tracked working tree and index are clean. The sole known untracked path may be
   the user-owned `essay/OUTLINE.md`; any additional untracked path blocks.
4. None of claim, transcript, commit-pending, invalidity, or their temporary files
   exists under `experiments/level_1_contact/allocation/`.
5. All nine lineage hashes equal the table above.
6. Environment is CPython 3.12.3, torch 2.9.1+cpu, CPU/float32, deterministic,
   one intra-op and one inter-op thread after canonical runtime setup.
7. `133` or more full-suite tests pass, public-root tests pass, and inherited/
   Level 0 decisions verify.

## Single command

With the signature-only commit checked out at `HEAD`, the only authorized draw
invocation is:

```bash
.venv/bin/python scripts/level1_draw_public_root.py \
  --reviewed-code-head 95adcb5011c170fe9076894f6439f1248538600f \
  --expected-head "$(git rev-parse HEAD)"
```

Invoke once. If it raises for any reason, stop. Never delete an artifact and
never rerun. Follow `PUBLIC_ROOT_EXECUTION_PROTOCOL.md`:
claim-only/invalidity requires signed invalidity review; a canonical durable
transcript with commit failure requires reviewed commit recovery, never redraw.

## Post-run verification

Before pushing the driver-created commit, verify:

1. claim and canonical transcript exist; commit-pending and invalidity do not;
2. transcript schema is `philosophia.level1.public-root.v1`,
   `scientific_outcome:false`, `root_hex` is 64 hex characters, and
   `os_csprng_calls:1` / `root_bytes:32`;
3. `git_head_before_draw == EXPECTED_HEAD` and
   `reviewed_code_head == REVIEWED_CODE_HEAD`;
4. environment fingerprint and all spec/lineage hashes rederive exactly;
5. D contains 6 pairs (2/stratum), roles contain 24 assignments (8/stratum), and
   `outcome_sample == "deferred-until-N3"`;
6. `forbidden_derivations` still names real panel, raw realizations, ordering,
   salt, and escrow plaintext;
7. the new commit has parent `EXPECTED_HEAD`, contains exactly claim+transcript,
   and carries the four agreed co-author trailers;
8. push that commit to `origin/main`; do not start feasibility, scout, N3, lock,
   escrow, trajectory, or outcome work under this token.

## Authorization boundary

The token authorizes exactly one public-root/allocation draw and its automatic
claim+transcript commit. It does not authorize real evaluator-panel generation,
feasibility, comparative scout, N3 selection, preregistration lock, escrow,
learner trajectory, or outcome.
