# Opus 4.8 X-line — Level 1 public-root driver, bounded confirmation

Reviewer: Opus 4.8 (X-line, bounded to the M1/M2/m1–m3 closures). Repository:
`/home/master/llm_projects/philosophia` (not committed; **driver not invoked**;
no entropy). I ran the unit/full tests, `--help`, static inspection, and
in-memory/temp-repo simulations only. No real allocation artifact was created.

---

## Verdict

**`REVISE_LEVEL1_PUBLIC_ROOT_DRIVER`**

M1, M2(a–d), m1, and m2 are genuinely closed and test-pinned. But **m3 is
incomplete in a way I can demonstrate concretely**: the byte-identity set
(`REVIEWED_SOURCE_PATHS`) omits `src/philosophia/level1/config.py`, which is
load-bearing for the recorded allocation. A consistent `config.py` drift between
`--reviewed-code-head` and `--expected-head` passes the byte check *and* the
runtime cardinality guard, yet silently changes D and the role assignments. One
bounded edit closes it.

**Test results:** `pytest tests/test_level1_public_root.py` → 10 passed
(temp-repo preflight sims + failure-route + entropy-scan included); full suite →
132 passed; verifier VALID; `.../allocation/` absent.

---

## The one concrete failure (m3)

`config.py` supplies `DEVELOPMENT_PAIRS_PER_STRATUM`, `OUTCOME_PAIRS_PER_STRATUM`,
and `STRATUM_COUNT`, which drive `development_pairs`/`outcome_pairs`/`assign_roles`
(`allocation.py:52,57,66–67,85,88`). `REVIEWED_SOURCE_PATHS`
(`scripts/level1_draw_public_root.py:44–50`) contains only the driver,
`public_root`, `allocation`, `serialization`, and `model` — **not `config`** — and
the execution-protocol doc names the same five. I verified by in-memory monkeypatch
(no file change): with `DEVELOPMENT_PAIRS_PER_STRATUM = 1` and
`OUTCOME_PAIRS_PER_STRATUM = 9`, `derive_public_allocations` returns **3
development pairs and 27 role assignments** (the signed contract is 6 and 24), and
`outcome_pairs` does **not** raise because its guard checks `9 == 9`. Since the
`git diff --quiet <reviewed> <expected> -- REVIEWED_SOURCE_PATHS` check ignores
`config.py`, such a drift passes preflight and the wrong allocation is recorded
and committed. This violates m3's guarantee that "only docs/review changes may
separate the two commits" — `config.py` is a sixth load-bearing path.

**Exact fix (bounded):** add `"src/philosophia/level1/config.py"` to
`REVIEWED_SOURCE_PATHS` (and the protocol doc's list), and extend
`test_preflight_refuses_...` with a `config.py`-drift case asserting the "source
bytes differ" refusal. (`world.py` need not be added: it is off the draw's output
path and cannot alter the recorded allocation; adding it is optional hardening.)

---

## Confirmation of the other closures

1. **M1 — durable-transcript vs invalidity routing.** `_route_post_draw_failure`
   (`driver:153–160`) validates the transcript via `load_durable_transcript`
   (`public_root.py:135–151`: canonical-JSON round-trip, schema, `git_head_before_draw
   == expected`, 32-byte hex root). A valid durable transcript →
   `PUBLIC_ROOT_COMMIT_PENDING.json` ("never redraw"); a missing/corrupt/HEAD-mismatched
   transcript → `PUBLIC_ROOT_INVALIDITY_REQUIRED.json`. `test_post_draw_failure_...`
   proves the two artifacts are mutually exclusive. Neither route can redraw
   (both raise; preflight blocks reruns on all four artifacts). **Confirmed.**
2. **M2(a) — reachable-module entropy scan.** `test_reachable_modules_contain_exactly_one_entropy_call`
   walks the driver + `public_root` + `allocation` + `serialization` + `model` for a
   fixed entropy-name set and asserts exactly `[(DRIVER, "secrets.token_bytes")]`
   with arg `32`, no keywords. (`config`/`world` are not scanned but are provably
   entropy-free constants/math.) **Confirmed.**
3. **M2(b) — temp-repo preflight refusals.** `test_preflight_refuses_...` exercises
   HEAD mismatch, reviewed-source byte drift, dirty tracked tree, staged index, and
   pre-existing artifact — all before entropy. **Confirmed** (with the m3 addition
   above).
4. **M2(c)/m2 — commit staging.** `_commit_transcript` (`driver:163–184`) rechecks
   `git diff --cached --quiet` immediately before `git add`, stages exactly
   `CLAIM`+`TRANSCRIPT`, verifies the staged name list equals those two, and commits
   with the four fixed co-author trailers; `test_commit_stages_only_...` pins the
   call sequence. **Confirmed.** (Minor, non-blocking: the staged-set check uses
   ordered tuple equality, which relies on git's alphabetical order matching the
   `paths` order — true today, since `..._DRAW_CLAIM` < `..._TRANSCRIPT`; a
   set/sorted comparison would be more robust.)
5. **M2(d) — failure injection.** Covered by the M1 test. **Confirmed.**
6. **m1 — claim irreversibility + recovery documented; no silent recovery command.**
   The claim carries `operator_rule: "claim presence forbids rerun or deletion"`;
   `PUBLIC_ROOT_EXECUTION_PROTOCOL.md` names the claim as the procedural
   irreversibility boundary, routes each state honestly, and states "No recovery
   command is authorized by this candidate." **Confirmed.**
7. **D/roles/R_h unchanged.** `derive_public_allocations` still yields D = 2/stratum
   (6), roles on the 24 outcome pairs, and `outcome_sample: "deferred-until-N3"`;
   `sample_outcome_pairs` is absent from the driver. Byte/scientifically unchanged
   from Sol's acceptance. **Confirmed.**
8. **No forbidden production.** No entropy drawn; no real panel, feasibility/scout,
   N3, lock, escrow, trajectory, or outcome exists or is newly authorized; the
   driver was not invoked. **Confirmed.**

---

## What a later execution-authorization record must bind

Because this is a `REVISE`, the draw is not authorizable until the m3 fix lands and
a bounded re-confirmation passes. The eventual execution-authorization record must
bind:

- `REVIEWED_CODE_HEAD` and the final docs-only `EXPECTED_HEAD`, with
  `git diff --quiet REVIEWED_CODE_HEAD EXPECTED_HEAD --` **empty over the corrected
  path set including `config.py`** (six paths);
- `EXPECTED_HEAD == git rev-parse HEAD` and a clean tracked tree with an empty
  index at draw time;
- absence of all four one-shot artifacts (claim, transcript, commit-pending,
  invalidity) before the draw;
- the presence and hashes of the nine governing-lineage files;
- the transcript's `git_head_before_draw`, `reviewed_code_head`,
  `environment_fingerprint`, `required_spec_hashes`, `governing_lineage_hashes`,
  `os_csprng_calls: 1`, and `forbidden_derivations`;
- Kirill's explicit one-shot authorization and the post-run checklist (single
  invocation, `os_csprng_calls == 1` in the committed transcript, D=6/roles=24/R_h
  deferred, commit contains exactly claim+transcript, then push).

## Negative space (preserved, unweakened)

Adjacent-only detector scope; the operational-modulus certificate and its sole S4
tooth; the public-root / escrow-secret-panel separation and `R_h`-deferred; the
public-reservation / secret-realization boundary; `PROOF_CORE`/`PROOF_STRONG` and
C6-as-annotation; `UNKNOWN`/censored never success; donor transcripts encode
`n_donor`, never `n_target`; development contrasts non-citable forever; Level 1
never evidence for `PROOF_CORE`.

**No entropy, real panel, feasibility/scout, N3, lock, escrow, trajectory, or
outcome is authorized by this confirmation.**

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
