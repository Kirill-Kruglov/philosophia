# Opus 4.8 X-line — Level 1 public-root driver, final bounded confirmation (m3)

Reviewer: Opus 4.8 (X-line, bounded to the m3 closure). Repository:
`/home/master/llm_projects/philosophia` (not committed; **driver not invoked**;
no entropy). Inputs: my prior confirmation,
`codex_level1_public_root_m3_correction.md`, and the four named source/doc files.
I ran the public-root and full suites and static/in-memory checks only.

---

## Verdict

**`LEVEL1_PUBLIC_ROOT_DRIVER_CONFIRMED`**

The single concrete m3 failure is closed — and closed with defense in depth: the
git byte-identity pin now includes `config.py`, **and** `derive_public_allocations`
independently asserts the signed D=6 / roles=24 cardinalities regardless of git
history. My exact DEV=1/OUTCOME=9 counterexample now raises. No other contract,
allocation output, recovery route, or gate changed; no entropy or artifact was
produced.

**Tests:** `pytest tests/test_level1_public_root.py` → 11 passed;
full suite → 133 passed (one new cardinality-guard test); verifier VALID;
`.../allocation/` absent.

---

## Confirmation of the five points

1. **`config.py` is the sixth reviewed byte path and entropy-scan path.** It is
   the sixth entry of `REVIEWED_SOURCE_PATHS`
   (`scripts/level1_draw_public_root.py`), the sixth `REACHABLE_SOURCES` entry in
   `tests/test_level1_public_root.py`, and is named in
   `PUBLIC_ROOT_EXECUTION_PROTOCOL.md`'s byte-identity list. **Confirmed.**

2. **A docs-only final HEAD with `config.py` drift is mechanically refused.**
   `test_preflight_refuses_...` now includes a `config` case: a commit changing
   only `src/philosophia/level1/config.py` makes `_preflight(changed, reviewed)`
   raise `RuntimeError: ... source bytes differ ...` (the
   `git diff --quiet REVIEWED_CODE_HEAD EXPECTED_HEAD -- REVIEWED_SOURCE_PATHS`
   check now covers `config.py`). **Confirmed.**

3. **The literal D=6/roles=24 runtime guard catches DEV=1/OUTCOME=9 independently
   of git.** `derive_public_allocations` (`public_root.py`) asserts
   `len(development) == 6` with per-stratum `[2,2,2]` and `len(roles) == 24` with
   `[8,8,8]`, raising `"signed development allocation cardinality changed"` /
   `"signed outcome role cardinality changed"` otherwise. This runs on the derived
   allocation at draw time and consults no git state, so it fires even if the byte
   check were bypassed. `test_runtime_cardinality_guard_rejects_config_drift`
   monkeypatches `DEVELOPMENT_PAIRS_PER_STRATUM = 1`, `OUTCOME_PAIRS_PER_STRATUM = 9`
   — my exact counterexample (which previously yielded dev=3/roles=27 undetected)
   — and now asserts the guard raises. **Confirmed.**

4. **The staged-path check is exact but order-independent.** `_commit_transcript`
   now tests `len(staged) != len(paths) or set(staged) != set(paths)` instead of
   ordered tuple equality; `test_commit_stages_only_claim_and_transcript` supplies
   the staged names in **reversed** order (`TRANSCRIPT`, then `CLAIM`) and still
   passes, while `git add` and the accept set remain exactly claim+transcript with
   the empty-index recheck and fixed trailers. **Confirmed.**

5. **No other contract/allocation/recovery/gate changed; no entropy/artifact.**
   The allocation output is unchanged (D=6, roles on the 24 outcome pairs, R_h
   `deferred-until-N3`, `sample_outcome_pairs` absent); the guard only *enforces*
   the existing law. The commit-pending vs invalidity routing, the durable-claim
   irreversibility protocol, and the gate order are unchanged. The driver was not
   invoked; no real one-shot artifact exists. **Confirmed.**

---

## The six reviewed source paths (byte-identity + entropy scan)

1. `scripts/level1_draw_public_root.py`
2. `src/philosophia/level1/public_root.py`
3. `src/philosophia/level1/allocation.py`
4. `src/philosophia/level1/serialization.py`
5. `src/philosophia/level1/model.py`
6. `src/philosophia/level1/config.py`

## Next step (not the draw)

Confirmation authorizes only the preparation of a **final execution-authorization
record** plus **Kirill's explicit one-shot token** — never the draw itself. That
record must bind: `REVIEWED_CODE_HEAD` and the final docs-only `EXPECTED_HEAD` with
an empty `git diff` over the six paths above; `EXPECTED_HEAD == HEAD` with a clean
tracked tree and empty index; absence of all four one-shot artifacts (claim,
transcript, commit-pending, invalidity); the nine governing-lineage files and their
hashes; the transcript fields (`git_head_before_draw`, `reviewed_code_head`,
`environment_fingerprint`, `required_spec_hashes`, `governing_lineage_hashes`,
`os_csprng_calls: 1`, `forbidden_derivations`); and the post-run checklist (single
invocation, `os_csprng_calls == 1`, D=6/roles=24/R_h deferred, commit contains
exactly claim+transcript, then push).

## Negative space (preserved, unweakened)

Adjacent-only detector scope; the operational-modulus certificate and its sole S4
tooth; the public-root / escrow-secret-panel separation and R_h-deferred; the
public-reservation / secret-realization boundary; `PROOF_CORE`/`PROOF_STRONG` and
C6-as-annotation; `UNKNOWN`/censored never success; donor transcripts encode
`n_donor`, never `n_target`; development contrasts non-citable forever; Level 1
never evidence for `PROOF_CORE`.

**No entropy, real panel, feasibility/scout, N3, lock, escrow, trajectory, or
outcome is authorized by this confirmation.**

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
