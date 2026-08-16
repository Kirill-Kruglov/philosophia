# Prompt — essay status reconciliation analyst (Claude)

ROLE: independent factual, scientific and structural analyst. Evidence review
is read-only. You may create exactly the response file named under `Output`; do
not edit any existing file, run an experiment, resume PHASE1_18 Part B,
generate data, choose an author decision, commit or push.

Your job is to turn a stale reconciliation proposal into a closed, numbered
patch specification for a separate mechanical executor. You are not the
executor and must not rewrite the essay wholesale.

## Read first

1. `successor/dev/ESSAY_STATUS_RECONCILIATION_LAUNCH_PACKET_V1.md`
2. `essay/climbing-the-wall-of-experience.md`
3. `README.md`
4. `essay/README.md`
5. `essay/OUTLINE.md`
6. `essay/REVIEW_HANDOFF.md`
7. `canonical/CLAIM_LEDGER.md`
8. `canonical/RESULTS_CANONICAL.md`
9. `canonical/KILL_MATRIX.md`

Read the following evidence objects, not conversational summaries:

- `successor/dev/WALLB_EQUATIONAL_CELL_CLOSURE.md`
- `successor/dev/WALLB_POLICY_CHANNEL_AUDIT_14B.md`
- `successor/dev/PHASE1_EXTRINSIC_16B.md`
- `successor/dev/PHASE1_EXTRINSIC_16D.md`
- `successor/dev/PHASE1_TERMINAL_18.md`
- `successor/dev/PHASE1_18_PART_A.md`
- `successor/dev/PHASE1_18_PART_B_AMENDMENT_1.md`
- `successor/dev/PHASE1_18_PART_B_AMENDMENT_5.md`
- `successor/dev/B2_09_PRE_FIX_RESULTS_AND_ESCALATION.md`
- `successor/dev/B2_09_AUDIT_SOL_STATIC.md`
- `successor/dev/B2_09_STATIC_AUDIT_DISPOSITION.md`
- `successor/dev/STANDING_RULES.md`
- `successor/dev/TWOPRES_LINE_CLOSURE.md`
- `successor/dev/PHASE2_STAGE_A_DRIVER_CLOSURE_19.md`
- `successor/recovery/phase2_stage_b_20260815/README.md`
- `successor/stage_r/l3/STAGE_R_L3_PROJECTION_ONLY_CLOSURE_V1.md`
- `successor/stage_r/l4/STAGE_R_L4_MINIMUM_ANNEX_V1_1_DRIVER_BOUNDED_CONFIRMATION.md`
- `successor/stage_r/README.md`
- `successor/stage_r/idea_gate/STAGE_R_E2_IDEA_GATE_DRIVER_SYNTHESIS_V1.md`

For external claims use primary sources:

- Minimo: `https://arxiv.org/abs/2407.00695`
- Hamilton-Zero paper: `https://arxiv.org/abs/2608.11911`
- Hamilton-Zero code: `https://github.com/simulacra-research/HamiltonZero`
- Hamilton-Zero checkpoint: `https://huggingface.co/simulacra-research/HamiltonZero`

## Required analysis

### A. Reconcile every proposed status change

Return an evidence matrix with one row per proposed change and exactly one
classification: `APPLY`, `REWORD`, `DEFER`, or `REJECT`.

Cover at least:

1. the mistaken narrative of repeated feasibility deaths;
2. the distinct Wall-B library and policy outcomes;
3. the B2 Slot 4c diagnostic and absence of a formal closure;
4. the invalid length-stratum causal explanation;
5. wall seconds versus host-independent search work;
6. 16D seed-independence versus run invariance;
7. `BUDGET_MASKED`, the `11 -> 13` arithmetic and incomplete Part B;
8. TWOPRES closure and its retained findings;
9. exact current Phase-2/Stage-R/E2 chronology;
10. the bounded Minimo reproduction statement;
11. Hamilton-Zero as a contemporary neighbouring system;
12. whether the ledger now reads as discipline or taxonomy substituting for a
    conclusion, and whether the three endings retain real negative space.

### B. Preserve evidential classes

- Do not turn a development diagnostic, screen, engineering closure or
  IDEA_GATE stop into a scientific result.
- Do not state that Slot 4c is closed. The maximum admissible status is
  `DIAGNOSTIC NON-IDENTIFICATION; NO SLOT OUTCOME` unless you find a later
  explicit author closure in a durable file and quote it exactly.
- Do not use `1.0` for exact displacement. `1.0` belongs to `sign_d`.
- Do not call the one-theorem discrepancy a measured noise floor or assign it
  solely to threading/binary changes.
- Treat the current PHASE1_18 Part-B directory and logs as incomplete runtime
  state, never as evidence.
- Do not use "external transfer" for the local Minimo reproduction without
  explaining that it means evaluation on a fixed human-written theorem panel,
  not the programme's cross-world/presentation transfer.
- Do not claim Hamilton-Zero tests self-selected contact, path independence or
  the Philosophia causal contrast.

### C. Produce a mechanical patch specification

For each approved edit emit:

```text
PATCH_ID:
TARGET_FILE:
ANCHOR_TEXT:
OPERATION: INSERT_AFTER | INSERT_BEFORE | REPLACE
OLD_TEXT:   # exact, for REPLACE
NEW_TEXT:   # final prose, not advice
EVIDENCE:
RATIONALE:
```

The specification may target only:

```text
README.md
essay/README.md
essay/REVIEW_HANDOFF.md
essay/climbing-the-wall-of-experience.md
```

Keep edits local. Preserve the walk-world void row, both Wall-B rows, H4,
24/12/0, `REPRODUCED, PLATFORM ONLY`, and the entire existing "What this does
not show" argument except for strictly necessary status additions. Preserve the
shared prohibitions in `REVIEW_HANDOFF.md`, while updating its status and read
list if required.

Do not target `essay/OUTLINE.md`, canonical files, historical reports or any
successor evidence object.

## Output

Write exactly one new file:

`successor/dev/ESSAY_STATUS_RECONCILIATION_CLAUDE_RESPONSE_V1.md`

It must contain:

1. findings ordered Critical/Major/Minor;
2. the evidence matrix;
3. the complete numbered patch specification;
4. a scope table listing the four allowed targets and whether each changes;
5. explicit confirmation that no Part-B outcome was used;
6. exact primary-source links for Minimo and Hamilton-Zero;
7. one terminal token.

Use `READY_FOR_CURSOR_ESSAY_STATUS_RECONCILIATION_V1` only if every proposed
edit is mechanically closed and evidence-bounded. Otherwise end with
`BLOCKED_ESSAY_STATUS_RECONCILIATION_ANALYSIS_V1` and list the minimum author
decisions still required.

No modification beyond that response file is authorized.
