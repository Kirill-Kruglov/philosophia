LEVEL1_FEASIBILITY_SCOPE_CONFIRMED

## Ordered findings

1. **No load-bearing source drift from reviewed code.** Current HEAD is `e1f235470c0903f50d869c03c9c363252914b301`; the load-bearing feasibility source/test diff from reviewed-code commit `308aa6fcfd165b1742a1ec4988a660d9a6c21333` is empty for `scripts/level1_run_feasibility.py`, `src/philosophia/level1/{feasibility,interlock,train,pool,panel}.py`, and `tests/test_level1_feasibility.py`. Current repository drift consists of review-prompt artifacts only, with unrelated untracked `essay/OUTLINE.md`.

2. **Feasibility output remains scientifically inert.** The signed A8 contract permits only runtime/resource aggregates, artifact sizes, finiteness flags, and one single-arm censoring indicator; no query, loss, or solve series may be recorded. The implementation reports `scientific_outcome: false`, an explicit no-arm-inference interpretation, one RANDOM-STATIC arm, one development world, one replicate, fixed caps, aggregate measurements, `peak_rss_kib`, and contamination guards at `scripts/level1_run_feasibility.py:221`. The allowed measurement payload is aggregate-only at `src/philosophia/level1/feasibility.py:292`.

3. **No comparative or N3 path is reachable.** The driver imports only feasibility/public-root/interlock helpers at `scripts/level1_run_feasibility.py:17` and the tests assert absence of `sample_outcome_pairs`, `estimate_contrast`, and `choose_n3` at `tests/test_level1_feasibility.py:101`. The execution surface is one call to `run_noncomparative_feasibility` after a durable claim at `scripts/level1_run_feasibility.py:211`.

4. **The binary censoring indicator follows the signed persistence logic.** The feasibility trajectory evaluates a dummy panel at step 0 and every checkpoint cadence, then sets `first_complete_window` only after five consecutive qualifying checkpoints at `src/philosophia/level1/feasibility.py:186` and `src/philosophia/level1/feasibility.py:219`. The report exposes only `censored_at_b`, never a solve time or solve series, at `src/philosophia/level1/feasibility.py:225`.

5. **Public-root geometry plus dummy panel is compatible with no escrow.** The current public transcript fixes first development pair `slot=0`, `lower=66` at `experiments/level_1_contact/allocation/PUBLIC_ROOT_TRANSCRIPT.json:1`. The feasibility driver derives the checked world from the public transcript at `scripts/level1_run_feasibility.py:162` and requires the authorization to match it at `scripts/level1_run_feasibility.py:196`. The dummy panel uses actual public-root reservation geometry but a test-only panel key at `src/philosophia/level1/feasibility.py:114`; `DummyPanelBuilder` rejects non-test panel keys at `src/philosophia/level1/panel.py:48`. No real panel, ordering, salt, plaintext, or escrow is generated.

6. **The first allocated lower world is an acceptable fixture, not an inferential sample.** Using `pair_slot=0`, `n=66` is a predeclared endpoint-computability/resource fixture, not a development result and not a sampled Level 1 estimand. It cannot support claims about feasibility across worlds, solve probability, arm ranking, or target difficulty. The public-root allocation itself is already fixed and public; choosing the first allocated lower world for a one-arm feasibility check does not introduce post-outcome interpretation because no comparative datum exists.

7. **Runtime projections are dimensionally honest but narrow.** `projected_random_static_seconds = mean_step_seconds * B` and `projected_active_scorer_seconds = mean_scorer_seconds * B` are explicit component projections at `src/philosophia/level1/feasibility.py:284`. They are honest for the measured components, but they omit initialization overhead, real checkpoint I/O, full multi-arm/multi-replicate scheduling, donor/YOKED paths, real-panel escrow/evaluation overhead, and operator pauses. Those omissions are not blocking because the report is resource-and-binary-feasibility-only, but they must never be narrated as a full Level 1 runtime forecast or sufficiency proof.

8. **One-shot authorization prevents accidental peeking under the procedural threat model.** The driver requires exact HEAD, clean tracked tree, empty index, canonical output directory, tracked authorization, tracked public transcript, fixed token, fixed caps, fixed world, reviewed source bytes, and absence of claim/report files at `scripts/level1_run_feasibility.py:71`. Alternate output directories are rejected at `scripts/level1_run_feasibility.py:80`; untracked authorization or transcript files are rejected at `scripts/level1_run_feasibility.py:86`; repeat claim/report paths are rejected at `scripts/level1_run_feasibility.py:148`. This is a procedural no-peeking mechanism, not a malicious-filesystem security seal; deleting artifacts and rerunning would violate the signed process rather than constitute an allowed software path.

9. **Later gates remain blocked.** The driver refuses later-gate artifacts before execution at `scripts/level1_run_feasibility.py:152`, and the contamination guards explicitly record no second arm, no contrast, no real panel, no escrow, no N3 selection, no lock, and no outcome at `scripts/level1_run_feasibility.py:240`. This matches the gate order in `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md:247` and A8’s no-contrast feasibility scope in `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md:313`.

## Mandatory edits

None.

## Question-by-question audit

1. **Allowed fields and tuning risk:** No allowed field, projection, dummy-panel result, or timing aggregate permits an arm comparison. The only learner-performance field is the one-arm `censored_at_b` indicator; timing and artifact fields are resource diagnostics. They cannot tune thresholds, margins, architecture, B, target solve rate, N3, or estimator rules without a signed amendment and re-review.

2. **Censoring semantics:** `censored_at_b` is computed as failure to complete any five-checkpoint qualifying window by B under the signed cadence/persistence rule. It is reported inside a `scientific_outcome: false` feasibility report and cannot be narrated as a Level 1 result.

3. **No-escrow compatibility:** The use of actual public-root reservation geometry is procedural-resource faithful; the panel seed is `dummy_key("level1-feasibility", purpose="panel")`, test-only, and domain-separated. This creates no real panel and no escrow secret.

4. **First world fixture:** The first allocated development pair, lower world `n=66`, is acceptable as a predeclared feasibility fixture. It is not an inferential world sample and provides no evidence about world-level variance or adjacent-pair effects.

5. **Projection honesty:** The projections are component-level `mean * B` estimates for the measured RANDOM-STATIC trajectory and ACTIVE scorer-only path. They are not a full-run wall-clock forecast and omit components large enough to matter for operations; the report’s interpretation boundary prevents that omission from becoming a scientific claim.

6. **Repeated peeking:** The claim/authorization mechanism blocks reviewed-path repeated peeking, alternate output directories, and untracked authorization files. It is adequate for the signed procedural threat model, while malicious deletion or filesystem tampering remains outside the claim and would require invalidity/recovery review rather than rerun.

7. **Forbidden statements:** See the table below; both successful and censored feasibility checks remain non-citable resource diagnostics, not Level 1 evidence.

## Allowed / forbidden interpretation table

| Feasibility artifact field or state | Allowed interpretation | Forbidden interpretation |
|---|---|---|
| `censored_at_b = false` | The single predeclared RANDOM-STATIC development fixture completed at least one persistent dummy-panel solve window within B. | Level 1 solved; RANDOM-STATIC is good; ACTIVE/YOKED/RANDOM comparisons; threshold, B, margin, architecture, or N3 tuning. |
| `censored_at_b = true` | The single fixture did not complete such a window within B, or no completed window preceded a non-finite stop. | The learner lacks `n`; Level 1 fails; RANDOM-STATIC is inferior; increasing B or changing endpoint without signed amendment. |
| Latency aggregates | Component timing diagnostics for this machine/path. | Full outcome runtime guarantee; arm efficiency comparison; resource sufficiency proof for all arms/blocks/replicates. |
| Artifact-size estimate and `peak_rss_kib` | Local resource-sizing diagnostics. | Final storage/memory budget for outcome, escrow, or checkpoint archive. |
| Dummy-panel computability/finiteness flags | Implementation/resource sanity for the fixture. | Evidence about real panel behavior, calibration, leakage absence, or scientific validity beyond the gate. |
| Authorization/claim/report existence | Procedural one-shot record for a non-outcome feasibility gate. | A preregistration lock, escrow, outcome, or citable result. |

## Authorization-candidate boundary

Codex may prepare an authorization candidate, but not execute it. The candidate may be a canonical JSON artifact for Kirill review/signature containing the fixed token, reviewed code head `308aa6fcfd165b1742a1ec4988a660d9a6c21333`, fixed caps, fixed world `{pair_slot: 0, modulus: 66}`, canonical output directory, and `scientific_outcome: false`. Codex must not run `scripts/level1_run_feasibility.py`, create a claim/report, inspect any feasibility outcome, select N3, create a lock, create escrow, or execute learner trajectories beyond unit tests.

## Tests and verifiers run

- `git diff --exit-code 308aa6fcfd165b1742a1ec4988a660d9a6c21333..HEAD -- scripts/level1_run_feasibility.py src/philosophia/level1/feasibility.py src/philosophia/level1/interlock.py src/philosophia/level1/train.py src/philosophia/level1/pool.py src/philosophia/level1/panel.py tests/test_level1_feasibility.py` — no diff.
- `.venv/bin/python -m pytest tests/test_level1_feasibility.py` — 6 passed.
- `.venv/bin/python -m pytest` — 139 passed.
- `.venv/bin/python scripts/verify_all.py` — existing admitted decisions valid; no new Level 1 gate executed.
