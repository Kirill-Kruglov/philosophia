# Prompt — essay status reconciliation executor (Cursor)

ROLE: mechanical editor working from a closed specification. Do not perform a
fresh scientific review and do not make editorial, statistical or author
choices.

## Preconditions

Read:

1. `successor/dev/ESSAY_STATUS_RECONCILIATION_LAUNCH_PACKET_V1.md`
2. `successor/dev/ESSAY_STATUS_RECONCILIATION_CLAUDE_RESPONSE_V1.md`
3. the four target files named below.

Stop without editing unless all conditions hold:

- the Claude response ends with
  `READY_FOR_CURSOR_ESSAY_STATUS_RECONCILIATION_V1`;
- the human author has explicitly accepted that response in the dispatch
  message;
- all four target hashes still match the launch packet;
- every requested change has the complete `PATCH_ID/TARGET_FILE/ANCHOR_TEXT/
  OPERATION/OLD_TEXT/NEW_TEXT/EVIDENCE/RATIONALE` schema;
- every target is in the allowlist below.

On any failure, write no file and return
`CURSOR_ESSAY_STATUS_RECONCILIATION_PRECONDITION_FAILED_V1` with exact evidence.

## Exact write scope

You may modify only:

```text
README.md
essay/README.md
essay/REVIEW_HANDOFF.md
essay/climbing-the-wall-of-experience.md
```

You may create only:

```text
successor/dev/ESSAY_STATUS_RECONCILIATION_CURSOR_REPORT_V1.md
```

Do not modify `essay/OUTLINE.md`, canonical files, historical reports, any
other successor file, code, JSON, logs or runtime artifacts. Do not clean or
stage unrelated dirty files. Do not commit or push.

## Execution law

1. Apply each Claude `PATCH_ID` literally and once.
2. Do not improve, extend, condense or harmonize prose outside those patches.
3. If an anchor is missing, duplicated ambiguously, or its old text differs,
   stop before making any partial edit.
4. Preserve all existing Markdown links unless the patch explicitly replaces
   one. New external citations must point to the primary sources in the launch
   packet.
5. Do not add a PHASE1_18 Part-B result, B2 Slot closure, successor scientific
   result, root, run or programme verdict.
6. Do not change the programme claim from `OPEN`.

## Verification

After editing:

- show `git diff --` restricted to the five authorized paths;
- run `git diff --check` on the four edited files;
- search the four targets for the forbidden stale/overclaim forms:

```text
four cells in a row died
five cells failing
1.0 at initialisation under length control
trained representation flattens length structure
Stage B is in contract review
159 s vs 181 s as search cost
one theorem is a third
Hamilton-Zero proves
Minimo proves
```

- confirm the diff contains no Part-B outcome or result file reference;
- print raw SHA-256 for all four targets after editing;
- confirm every other pre-existing dirty path is untouched.

## Report

Write `successor/dev/ESSAY_STATUS_RECONCILIATION_CURSOR_REPORT_V1.md` containing:

1. the Claude response hash and terminal token;
2. every applied `PATCH_ID`;
3. old and new hashes of all four targets;
4. exact changed-path list;
5. `git diff --check` result;
6. forbidden-form search result;
7. confirmation that no test, experiment, Part-B process, commit or push ran;
8. any refusal, if applicable.

End successful work with exactly:

`READY_FOR_CODEX_ESSAY_STATUS_RECONCILIATION_DIFF_AUDIT_V1`

No commit or push is authorized.
