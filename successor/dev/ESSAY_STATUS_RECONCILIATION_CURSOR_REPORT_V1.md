# Essay status reconciliation — Cursor mechanical execution report V1

Role: mechanical executor report for V2.1 plus executor addendum. No scientific
or editorial review. No commit or push.

---

## 1. Governing inputs

| Object | SHA-256 | Result |
|---|---|---|
| `successor/dev/ESSAY_STATUS_RECONCILIATION_CLAUDE_RESPONSE_V2_1.md` | `1a76eb3864142718ff456d9215244d2014b2ecb56eea2e9faa32fa55c9697b0c` | MATCH |
| `successor/dev/ESSAY_STATUS_RECONCILIATION_V2_1_EXECUTOR_ADDENDUM.md` | `f9aef391bfaa2b6d2ac650b5020a38fb8688f8da5f73a12d3a917188dca3376b` | MATCH |

Claude terminal confirmed present:

```text
READY_FOR_CURSOR_ESSAY_STATUS_RECONCILIATION_V2_1
```

---

## 2. Preconditions and original target hashes

All four allowlisted targets matched their pins before any write:

| Target | Pre-edit SHA-256 | Result |
|---|---|---|
| `README.md` | `d5ae3259fcd4231070fb211559a15d6d02111d222ad4eb7e05878d296ddf4839` | MATCH |
| `essay/README.md` | `9908f5c8405be3a6f49484f62e9884aea134c7d27d33b4709ae2a638f5001346` | MATCH |
| `essay/REVIEW_HANDOFF.md` | `53b0448db45a3ab3727d2dd56a7f2a41dd92444a8962f891b96f3c1206bccbe4` | MATCH |
| `essay/climbing-the-wall-of-experience.md` | `76919e8fe75123293f99bb15cd4dd553f700d53189a7390272c1cd8ba2e55d0f` | MATCH |

Per-patch pre-write checks (all nine):

- target in allowlist: pass
- `OLD_TEXT` byte-exact and unique: pass
- `ANCHOR_TEXT` unique: pass
- no overlapping replacement spans in numerical order: pass

Dirty-worktree baseline captured via `git status --short` before any edit.
Unrelated dirty paths were left untouched.

---

## 3. Patches applied

Patches `1` through `9` applied exactly once each, in numerical order.

| Patch | Target | Operation |
|---|---|---|
| 1 | `README.md` | REPLACE |
| 2 | `README.md` | REPLACE |
| 3 | `essay/climbing-the-wall-of-experience.md` | INSERT_AFTER |
| 4 | `essay/climbing-the-wall-of-experience.md` | INSERT_AFTER |
| 5 | `essay/climbing-the-wall-of-experience.md` | INSERT_AFTER |
| 6 | `essay/climbing-the-wall-of-experience.md` | REPLACE |
| 7 | `essay/README.md` | INSERT_AFTER |
| 8 | `essay/REVIEW_HANDOFF.md` | INSERT_AFTER |
| 9 | `essay/REVIEW_HANDOFF.md` | INSERT_AFTER |

P2 / Slot 4c remains absent. Programme claim remains `OPEN` / open.

---

## 4. Addendum Correction B

Applied to Patch 8 `NEW_TEXT` before insert. Removed the duplicated Stage-R L3
phrase. Resulting Patch 8 passage:

```text
a later MINIMO-based route had Phase-2 Stage-A and
Stage-B L0–L3 engineering surfaces accepted, but the Stage-R route then ended at
its minimum-L4 paper boundary
```

No other Patch 8 byte changed relative to V2.1 plus this substitution.
`essay/REVIEW_HANDOFF.md` new status paragraph names `Stage-B L0–L3` exactly once
and contains all nine authority paths from the executor addendum.

---

## 5. Addendum Correction A — authority attribution (report only)

Correction A changed no target prose. Corrected attribution:

- Accepted Stage-B L0–L2: `successor/recovery/phase2_stage_b_20260815/README.md`
  and its accepted recovery objects.
- Projection-only L3: `successor/stage_r/l3/STAGE_R_L3_PROJECTION_ONLY_CLOSURE_V1.md`.

Target prose form `Stage-B L0–L3 surfaces accepted` / `Stage-B L0–L3 engineering
surfaces accepted` remains as specified in V2.1.

---

## 6. Exact five-path write set

1. `README.md` (modified)
2. `essay/README.md` (modified)
3. `essay/REVIEW_HANDOFF.md` (modified)
4. `essay/climbing-the-wall-of-experience.md` (modified)
5. `successor/dev/ESSAY_STATUS_RECONCILIATION_CURSOR_REPORT_V1.md` (this report; created)

No other path was written by this execution.

---

## 7. SHA-256 (targets)

| Path | Old SHA-256 | New SHA-256 |
|---|---|---|
| `README.md` | `d5ae3259fcd4231070fb211559a15d6d02111d222ad4eb7e05878d296ddf4839` | `4768aff431ad1ada64efdf4fc11a5a585de63fe8a2d0270e64e2ecb646815a19` |
| `essay/README.md` | `9908f5c8405be3a6f49484f62e9884aea134c7d27d33b4709ae2a638f5001346` | `02c583a35147f145668dac16b4142c6c948aca59b91bc87d2d54ce7d82a9d858` |
| `essay/REVIEW_HANDOFF.md` | `53b0448db45a3ab3727d2dd56a7f2a41dd92444a8962f891b96f3c1206bccbe4` | `c10b66ec5422410f7ac671d65271e7ff509f377c9b8d1578dee1098f845d396d` |
| `essay/climbing-the-wall-of-experience.md` | `76919e8fe75123293f99bb15cd4dd553f700d53189a7390272c1cd8ba2e55d0f` | `2f8209e93c90f06799df1cc0872b2164367df12fd3a36fa1b0c6818645d3bf8f` |

Report self-hash omitted: embedding this report's own SHA-256 would mutate the
reported bytes. External caller must compute the hash of this file after write.

---

## 8. Post-edit verification

### `git diff --check`

Restricted to the four edited targets: exit code `0` (no whitespace errors).

### Diff scope

Restricted diff is exactly Patches 1–9 plus addendum Correction B on Patch 8.
All four targets changed. No fifth pre-existing path changed as a consequence of
this execution.

### Required forms (present in resulting targets)

- `CLOSED / SPARSE`
- `SCREEN-VIABLE`
- `Stage-B L0–L3`
- `minimum-L4 paper boundary`
- `NOT_CHEAPLY_AUDITABLE`
- `up to `Aut(M)``
- `roughly 0.5B variational parameters`
- `fixed human-written theorem panel`
- `programme claim remains open`

### Forbidden forms (absent from resulting targets)

- `equational Wall-B cell produced only 2/40`
- `equational Wall-B cell failed its preregistered five-world frame gate`
- `No successor root, learner run`
- `Stage-R and E2 stages stopped before build`
- `Stage-R L3/L4`
- `positive-VICReg alignment probe`
- `BUDGET_MASKED`
- `11 -> 13`
- `one theorem is a third`
- `159 s vs 181 s as search cost`
- `trained representation flattens length structure`
- `Hamilton-Zero proves`
- `Minimo proves`

### Minimo chronology check

Non-contradictory across surfaces: Phase-1 exploratory learner ran (essay Patch
5; REVIEW_HANDOFF Patch 8); later Stage-R route minted no root and executed no
learner or selector (scoped denials on README / essay README / ledger /
REVIEW_HANDOFF).

---

## 9. Dirty-worktree comparison

Before edit: baseline `git status --short` captured (pre-existing dirty
successor/dev artifacts only; the four essay/README targets were clean).

After edit: baseline plus exactly:

- ` M README.md`
- ` M essay/README.md`
- ` M essay/REVIEW_HANDOFF.md`
- ` M essay/climbing-the-wall-of-experience.md`
- `?? successor/dev/ESSAY_STATUS_RECONCILIATION_CURSOR_REPORT_V1.md`

All pre-existing dirty paths remain present and unmodified by this execution.

---

## 10. Process confirmations

- No experiment, test suite, learner, training job, or PHASE1_18 Part-B process ran.
- No external scientific query ran.
- No commit or push ran.
- No staging of paths.
- Markdown-only mechanical edit.

---

```text
READY_FOR_CODEX_ESSAY_STATUS_RECONCILIATION_DIFF_AUDIT_V1
```
