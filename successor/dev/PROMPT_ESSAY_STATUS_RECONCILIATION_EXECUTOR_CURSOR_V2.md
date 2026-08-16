# Prompt — essay status reconciliation mechanical executor (Cursor V2)

ROLE: mechanical editor. Apply the closed V2.1 patch specification plus its
two-item executor addendum. Do not perform another scientific or editorial
review, choose alternative wording, move a passage, or make an author decision.

Do not run an experiment, test suite, learner, training job, PHASE1_18 Part-B
process or external scientific query. Do not clean the dirty worktree, stage,
commit or push.

## Preconditions — verify before any write

Read and SHA-256 verify:

```text
successor/dev/ESSAY_STATUS_RECONCILIATION_CLAUDE_RESPONSE_V2_1.md
1a76eb3864142718ff456d9215244d2014b2ecb56eea2e9faa32fa55c9697b0c

successor/dev/ESSAY_STATUS_RECONCILIATION_V2_1_EXECUTOR_ADDENDUM.md
f9aef391bfaa2b6d2ac650b5020a38fb8688f8da5f73a12d3a917188dca3376b
```

Confirm that the Claude response ends with:

```text
READY_FOR_CURSOR_ESSAY_STATUS_RECONCILIATION_V2_1
```

Confirm that the four targets still match:

```text
README.md
d5ae3259fcd4231070fb211559a15d6d02111d222ad4eb7e05878d296ddf4839

essay/README.md
9908f5c8405be3a6f49484f62e9884aea134c7d27d33b4709ae2a638f5001346

essay/REVIEW_HANDOFF.md
53b0448db45a3ab3727d2dd56a7f2a41dd92444a8962f891b96f3c1206bccbe4

essay/climbing-the-wall-of-experience.md
76919e8fe75123293f99bb15cd4dd553f700d53189a7390272c1cd8ba2e55d0f
```

Before editing, capture the complete `git status --short` as the dirty-worktree
baseline. Do not alter, delete, stage or normalize any pre-existing dirty path.

For each of the nine V2.1 patches, verify before the first write that:

- its target is in the allowlist below;
- its full `OLD_TEXT` is byte-exact in that target;
- its `ANCHOR_TEXT` resolves exactly once;
- applying all patches in numerical order creates no overlapping replacement.

On any failed precondition, make no edit and create no report. Return exactly:

`CURSOR_ESSAY_STATUS_RECONCILIATION_PRECONDITION_FAILED_V2`

with the concrete mismatch in the chat response.

## Exact write scope

Modify exactly these four existing files:

```text
README.md
essay/README.md
essay/REVIEW_HANDOFF.md
essay/climbing-the-wall-of-experience.md
```

Create exactly this one report:

```text
successor/dev/ESSAY_STATUS_RECONCILIATION_CURSOR_REPORT_V1.md
```

No other path may change. In particular, do not modify the Claude response,
executor addendum, `essay/OUTLINE.md`, canonical files, historical reports,
successor evidence, code, JSON, logs or runtime artifacts.

## Execution law

1. Apply V2.1 Patches 1 through 9 once each and in numerical order.
2. Apply `ESSAY_STATUS_RECONCILIATION_V2_1_EXECUTOR_ADDENDUM.md` Correction B
   to Patch 8's `NEW_TEXT` before inserting it. This removes the duplicated
   Stage-R L3 phrase and changes no other Patch 8 byte.
3. Correction A changes no target prose. Use its correct L0–L2 versus L3
   authority attribution in the report.
4. Apart from Correction B, use every V2.1 `NEW_TEXT` literally. Do not improve
   style, rewrap unrelated text, reorder sections or alter an existing link.
5. Preserve the original shared prohibitions in `essay/REVIEW_HANDOFF.md`
   verbatim and append only V2.1 Patch 9.
6. Keep P2/Slot 4c absent. Keep the programme claim `OPEN`.
7. Do not restructure `Proof`, `Falsification`, `Boundary`, or replace existing
   `What this does not show` prose.

## Post-edit verification

Before writing the report:

1. Run `git diff --check` restricted to the four edited targets.
2. Inspect the complete diff restricted to the four targets and confirm it is
   exactly the nine patches plus addendum Correction B.
3. Confirm all four targets changed and no fifth pre-existing path changed as a
   consequence of this execution. Compare the full post-edit
   `git status --short` with the captured baseline, allowing only the four
   target modifications and the new report.
4. Confirm these required forms occur in the resulting targets:

```text
CLOSED / SPARSE
SCREEN-VIABLE
Stage-B L0–L3
minimum-L4 paper boundary
NOT_CHEAPLY_AUDITABLE
up to `Aut(M)`
roughly 0.5B variational parameters
fixed human-written theorem panel
programme claim remains open
```

5. Confirm these stale, false or forbidden forms do not occur in the resulting
   targets:

```text
equational Wall-B cell produced only 2/40
equational Wall-B cell failed its preregistered five-world frame gate
No successor root, learner run
Stage-R and E2 stages stopped before build
Stage-R L3/L4
positive-VICReg alignment probe
BUDGET_MASKED
11 -> 13
one theorem is a third
159 s vs 181 s as search cost
trained representation flattens length structure
Hamilton-Zero proves
Minimo proves
```

6. Specifically inspect the two Minimo passages together and confirm they are
   non-contradictory: a Phase-1 exploratory learner ran; the later Stage-R route
   minted no root and executed no learner or selector.
7. Specifically confirm that `essay/REVIEW_HANDOFF.md` names Stage-B L0–L3 only
   once in its new status paragraph and contains all nine authority paths from
   the executor addendum.
8. Compute raw SHA-256 for all four edited targets and the report.

Do not run a test suite: this is a Markdown-only mechanical edit.

## Report

Write
`successor/dev/ESSAY_STATUS_RECONCILIATION_CURSOR_REPORT_V1.md` with:

1. both governing input hashes and the Claude terminal;
2. precondition results and original target hashes;
3. Patches `1..9` applied exactly once;
4. explicit application of addendum Correction B;
5. corrected authority attribution: recovery checkpoint supports accepted
   L0–L2; the Stage-R L3 closure supports projection-only L3;
6. the exact five-path write set (four modified targets plus this report);
7. old/new SHA-256 for every target and the report's SHA-256 if self-hashing is
   feasible without mutating the reported bytes; otherwise state that the
   external caller must compute the report hash;
8. `git diff --check`, required-form and forbidden-form results;
9. before/after dirty-worktree comparison and confirmation that unrelated dirty
   paths were untouched;
10. confirmation that no experiment, test, Part-B process, external query,
    commit or push ran.

End successful work with exactly:

`READY_FOR_CODEX_ESSAY_STATUS_RECONCILIATION_DIFF_AUDIT_V1`

No commit or push is authorized.
