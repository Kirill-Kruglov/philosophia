# Codex closure: Level 1 public-root driver review

Date: 2026-07-13. No entropy was drawn and no file under the real allocation
artifact directory was created.

Inputs:

- `opus_level1_public_root_driver_review.md` —
  `REVISE_LEVEL1_PUBLIC_ROOT_DRIVER`;
- `sol_level1_public_root_allocation_review.md` —
  `LEVEL1_PUBLIC_ROOT_ALLOCATION_ACCEPTED`.

No scientific allocation rule changed. D remains 2 pairs/stratum, roles are
assigned once on the 24 outcome pairs, and R_h remains deferred until N3.

## Opus dispositions

- **M1 closed:** post-draw failure now validates the canonical durable transcript.
  A valid transcript produces `PUBLIC_ROOT_COMMIT_PENDING.json` with its SHA-256
  and the mandatory route "complete a reviewed recovery commit; never redraw".
  `PUBLIC_ROOT_INVALIDITY_REQUIRED.json` is created only when no canonical
  transcript bearing the expected pre-draw HEAD is durably recoverable.
- **M2(a) closed:** the AST entropy scan covers the driver and its reachable
  `public_root`, `allocation`, `serialization`, and `model` modules. The sole
  allowed entropy call is the driver's literal `secrets.token_bytes(32)`.
- **M2(b) closed:** temp-git tests reject expected-HEAD mismatch, reviewed-source
  byte drift, dirty tracked state, non-empty index, and an existing artifact.
- **M2(c) closed:** `_commit_transcript` rechecks the empty index immediately
  before `git add`, stages exactly claim+transcript, verifies the staged name
  list, and only then commits with fixed trailers.
- **M2(d) closed:** failure injection proves durable transcript → commit-pending
  and missing transcript → invalidity, with mutually exclusive artifacts.
- **m1 closed:** `PUBLIC_ROOT_EXECUTION_PROTOCOL.md` names the durable claim as
  the procedural irreversibility boundary. Claim presence forbids deletion and
  rerun; claim-only requires signed invalidity review.
- **m2 closed:** the immediate empty-index recheck and exact staged-path assertion
  are code-enforced and test-pinned.
- **m3 closed:** execution now requires both `--expected-head` and
  `--reviewed-code-head`; preflight mechanically compares driver, public-root,
  allocation, serialization, and model bytes between them. Only docs/review
  changes may separate the two commits.

No recovery command is pre-authorized. If commit-pending occurs, execution stops;
the existing durable root is preserved and a bounded recovery review is required.

## Verification

```text
10 public-root tests passed
132 full-suite tests passed
VALID  inheritance/line12_same_wall/experiment_A/decision.json
VALID  experiments/level_0_grokking/outcomes/decision.json
```

The one-shot driver was not invoked. `--help`, compilation, unit tests, AST
inspection and temp-repository simulations consume no entropy.

## Requested confirmation

Opus should return exactly one:

- `LEVEL1_PUBLIC_ROOT_DRIVER_CONFIRMED`
- `REVISE_LEVEL1_PUBLIC_ROOT_DRIVER`

Even confirmation does not authorize the entropy draw. A later final execution
record must name the reviewed-code HEAD and final expected HEAD, pass byte-identity
and artifact-absence checks, and receive Kirill's explicit one-shot authorization.
