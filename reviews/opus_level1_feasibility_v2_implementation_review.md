# Opus 4.8 X-line — Level 1 feasibility v2 implementation review

Reviewer: Opus 4.8 (X-line, implementation of the **signed** floor amendment).
Repository: `/home/master/llm_projects/philosophia`. **The v2 driver was not
invoked; no v2 authorization, claim, report, invalidity record, probe, entropy,
panel, N3, lock, trajectory, or outcome was created. Nothing was committed.**
Reviewed code commit: `d8c46637adf6f0caab039559c9031b1af65985b4`. I ran the
unit/full suites, `verify_all.py`, independent hash recomputation, and static
inspection.

**Source-byte pin verified.** `git diff d8c46637 HEAD` touches only two
review-only prompt files; the load-bearing set (the v2 driver, `feasibility.py`,
`interlock.py`, `train.py`, `public_root.py`, the ten shared modules, both v2 and
v1 test files, and the v1 driver) is byte-identical between `d8c46637` and HEAD
(`db9b39e…`). The signed amendment is real: `I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_
AMENDMENT` is at line 82 of `SCIENTIFIC_SPEC_SIGNATURES.md`, whose SHA-256 the
driver pins.

---

## Verdict

**`LEVEL1_FEASIBILITY_V2_IMPLEMENTATION_CONFIRMED`**

The implementation is a faithful, single-valued realization of the signed
v2/v2.1/v2.2 amendment and is safely gated. The full-history rule is exactly one
mean-CE AdamW update per answer over all `t` own-history pairs in canonical
contact order as one shared unchunked tensor for all four members — no replay, no
chunking, no accumulation, no extra updates, no post-collection training, no early
success stop. The v2 capability is exactly `2000/0/129600`; v1 code and evidence
are untouched; the durable no-replace claim precedes step 1 and the report is
written only after a valid terminal; the report surface is aggregate/flag/one-bit
only; and the preflight enforces the full lineage. No mandatory edits. Two
optional future guards below are genuinely non-blocking.

**Results:** v2 tests → 9 passed; v1 regression → 10 passed; full suite → 152
passed; `verify_all.py` VALID; all six driver-pinned lineage hashes (signature, 3
amendments, 2 v1-evidence) independently recompute correct; no `feasibility_v2/`,
no `FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json`, no v2 claim/report present.

---

## Findings

### Critical / Major
None.

### Minor
None blocking. See the two future guards.

---

## Point-by-point verification (the eight required checks)

1. **Full-history rule — order, shared four-member update, no replay/chunking/
   accumulation/extra-updates/post-collection/early-stop.**
   `run_noncomparative_feasibility_v2` (`feasibility.py:326`) appends each realized
   pair to `history_tokens`/`history_labels` in schedule order and calls
   `full_history_committee_step` (`train.py:61`), which `torch.stack`s the **entire**
   growing history into one shared `[t, 277]` tensor + one `[t]` label tensor and
   delegates to `feasibility_committee_step`: **one** `spend_trajectory_step`, four
   losses on the **same** tensor, four independent `backward`/`step`/`zero_grad`. It
   **never** calls `replay_batch_indices` (the bounded-wiring test monkeypatches
   replay to raise and passes → never called), there is no chunk loop and no
   `grad`-accumulation, training is inline (no post-loop training), and the loop
   runs the full schedule — `first_complete_window` never breaks it; only a
   non-finite loss breaks. `test_full_history_step_uses_canonical_growing_shared_
   batch` pins the growing shared batch across all four members, `trajectory_steps
   == 2`, and `grad is None` post-step; the wiring test pins `seen == [1,2,3,4]`,
   strictly increasing per-token order, and `steps_completed == 4`. ✓

2. **v1 unchanged; distinct v2 capability `2000/0/129600`; no comparative/outcome
   capability.** The v1 driver `level1_run_feasibility.py`, `run_noncomparative_
   feasibility`, and the v1 evidence are byte-identical (diff empty; both v1 hashes
   recompute to the pinned values); v1 tests pass. `feasibility_v2_capability()`
   (`interlock.py:115`) is `trajectory_cap=2000, scorer_cap=0, wall=129600`, pinned
   by test. `run_level1_trajectory` still raises `ExecutionNotAuthorized`; the v2
   driver imports no `sample_outcome_pairs`/`estimate_contrast`/`choose_n3` (test
   asserts their absence). The `FeasibilityCapability.__init__` wall ceiling was
   raised 12 h→36 h, but `feasibility_capability()` still hard-passes 12 h, so v1
   runtime behavior is unchanged. ✓

3. **v1-faithful schedule/world/model/optimizer/init, step-0/every-50 panel, five
   checkpoints spanning 200, non-finite route, checkpoint-size surface.** Same
   `("L1","feas")` without-replacement `B`-schedule, same `_committee` (init/
   optimizer), world `{0,66}` from the transcript; step-0 `_panel_qualifies` seed +
   `step % CHECKPOINT_CADENCE == 0` evaluation; the qualifying window is five
   consecutive qualifying checkpoints (`len(recent_qualifying) >= 5 and
   all(recent_qualifying[-5:])`, a 200-step span at cadence 50); a non-finite loss
   sets `all_losses_finite=False` and breaks (A6 scientific censoring, never a
   process fault); `_checkpoint_size` measures an in-memory `torch.save` payload
   (not persisted), with a v2 purpose string. All identical to v1 except the update
   rule. ✓

4. **Schemas/paths/token/hashes/source-pins/tracked-lineage/clean-tree/index/HEAD/
   existing-artifact + later-gate refusals.** `_preflight` (`:155`) enforces
   `HEAD==expected_head`, clean tracked tree, empty index, frozen output dir,
   git-tracked lineage (authorization, transcript, signatures, 3 amendments, 2
   v1-evidence), `_verify_lineage_hashes` (verify-and-refuse-on-mutation over all
   six pinned SHA-256), the full authorization contract (schema `.v2`, token,
   `scientific_outcome:false`, `execution_once:true`, arm, caps `{1,2000,0,129600}`,
   world `{0,66}`, output dir, the three lineage-hash maps, 40-hex `reviewed_code_
   head`), the reviewed-source byte diff over the 13 pinned paths, the transcript
   contract, existing claim/report refusal (`FileExistsError`), and later-gate
   refusal (`comparative_scout`, `N3_SELECTION.json`, `PREREG.lock`,
   `escrow/REAL_PANEL.enc`, `outcomes/decision.json`). Preflight tests exercise
   lineage-accept, source-drift reject, mutated-v1-evidence reject, and
   existing-claim reject. ✓

5. **Transcript fingerprint consistency + canonical runtime match before claim
   creation.** Preflight checks the transcript's internal fingerprint consistency
   (`environment_fingerprint(transcript.environment) == transcript.environment_
   fingerprint`, `:243`); `main` calls `configure_canonical_runtime()` then
   `_verify_current_environment(transcript)` (`:300–301`), which requires the live
   environment dict **and** its fingerprint to equal the transcript's — **before**
   the claim is created (`:328`). `test_v2_driver_environment_must_match_public_
   root` pins the drift rejection. ✓

6. **Race-safe durable no-replace claim; claim before step 1; report only after
   valid terminal; no auto-rerun.** `atomic_create_no_replace` (`public_root.py:189`)
   writes a same-directory temp via `O_EXCL`, `flush`+`fsync`s the file, installs
   with `os.link` (**no-replace**: raises `FileExistsError` if the target exists,
   closing the replace race that `os.replace` would open), unlinks the temp, and
   `fsync`s the parent directory; on any failure it cleans the temp. The claim is
   installed at `:328` **before** the capability/run (`:330–331`); the report at
   `:383` **after** the run and a final `check_wall`. `test_v2_driver_surface…`
   pins `claim < run < report`; `test_atomic_create_no_replace_preserves_racing_
   destination` pins that a racing writer's bytes are preserved and the temp is
   cleaned. A wall-hit or crash between claim and report raises before the report
   is written — `censored_at_b` is never set, the claim's `status:
   started-no-delete-no-rerun` stands, and the existence refusals block any
   automatic rerun. ✓

7. **Report surface: only allowed aggregates/size/flags/one bit.** `report_payload_
   v2` emits only `trajectory` (latency count/mean/median/min/max, `steps_completed`,
   `all_losses_finite`, `panel_computable`, `censored_at_b`, `checkpoint_artifact_
   bytes`) and a `projection_scope` string — **no scorer, no series, no projected
   contrast**. The report adds `scientific_outcome:false`, the caps, `peak_rss_kib`,
   and `contamination_guards` all-false (including `v1_v2_contrast` and
   `scorer_repeated`). Tests assert `scorer`/`loss_series`/`query_series` never
   appear and the payload keys are exactly `{trajectory, projection_scope}`. Only a
   **valid scientific terminal** is ever written (`validity: valid-scientific-
   terminal`); routes 4/5 raise before any report. ✓

8. **Tests detect policy/replay/scorer/source/evidence/environment/output/repeat
   drift and replacement races.** Covered respectively by the growing-full-history
   assertions, the replay-raises monkeypatch, the `scorer_cap != 0` refusal + the
   `scorer_steps: 0` cap, the source-drift preflight test, the mutated-v1-evidence
   preflight test, the environment-fingerprint drift test, the frozen output dir +
   existing-claim refusal, and the `atomic_create_no_replace` collision test. ✓

**A6 route fidelity (adversarial check).** No resource/process fault can
masquerade as a censoring: `capability.check_wall()` raises `ExecutionNotAuthorized`
(propagates, no report), OOM crashes (no report), and only a *completed or
cleanly non-finite* run returns a `FeasibilityV2Run` that yields a valid-terminal
report. A non-finite trajectory is recorded as scientific censoring with
`all_losses_finite:false` (route 3), and a window completed **before** the first
non-finite state still stands (`censored_at_b:false` with the non-finite
diagnostic), exactly as A6/§7 require — never relabeled a process fault. ✓

---

## Future guards (optional, non-blocking)

- **G-1 — `allocation.py` is transitively imported but not pinned.** The pinned
  `public_root.py` imports `allocation.py`, so it loads during a v2 run, but
  **none** of its functions (`development_pairs`, `assign_roles`, `sample_outcome_
  pairs`, `derive_public_allocations`) is called on the v2 execution path — the
  development world is read from the committed transcript JSON, not re-derived —
  and `allocation.py` has no module-level side effects. A byte-drift in it
  therefore cannot alter the v2 measurement or route, so it is **not** a mandatory
  pin (unlike the FS-4 case, where `public_root.py`'s *executed* output plumbing
  justified pinning). Adding it to `REVIEWED_SOURCE_PATHS` would be belt-and-
  suspenders import-closure completeness; the reviewed-implementation gate may
  choose to include the full transitive import set.

- **G-2 — the public-root transcript content hash is recorded, not pinned as a
  frozen constant.** Unlike the amendment/signature/v1-evidence hashes, the
  transcript's SHA-256 is written into the claim/report but not compared to a
  hard-coded value. This is consistent with the v1 driver and the signed §6
  contract (the transcript is the public-root gate's own attested output), and a
  silent world/env swap is already blocked by the clean-tree + `HEAD==expected_head`
  binding, the exact `development_world {0,66}` and `forbidden_derivations` checks,
  and the live-environment fingerprint match. Pinning the transcript SHA-256 as a
  constant (symmetric with the other lineage pins) would be a reasonable optional
  hardening; it is not required for v2 integrity.

Neither guard changes any signed scientific constant, schema, cap, route, or gate.

---

## May Codex prepare a v2 authorization candidate for separate review, but not
execute it?

**Yes — prepare, not execute, not self-authorize.** With the amendment signed and
the implementation confirmed, Codex may draft the
`FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json` **candidate** carrying the frozen
structural fields the preflight validates: `schema =
philosophia.level1.feasibility-authorization.v2`, `token = I_AUTHORIZE_LEVEL1_
NONCOMPARATIVE_FEASIBILITY_V2` (as the **field Kirill must sign**, not asserted on
his behalf), `scientific_outcome:false`, `execution_once:true`, `arm:"RANDOM-
STATIC"`, `caps={development_worlds:1, trajectory_steps:2000, scorer_steps:0,
wall_seconds:129600}`, `development_world={pair_slot:0, modulus:66}`,
`output_directory = experiments/level_1_contact/feasibility_v2`, the three lineage
maps (`governing_signature_sha256`, `governing_amendment_sha256`, `v1_evidence_
sha256`) exactly as pinned, and `reviewed_code_head = d8c46637…`. That candidate
goes to **separate review**. Codex must **not** create the actual authorization
with Kirill's token, commit it, invoke `scripts/level1_run_feasibility_v2.py`,
create the claim/report/invalidity record, draw entropy, build a real panel, or
touch any later gate. Execution is a distinct, Kirill-authorized one-shot.

## Negative space (preserved, unweakened)

`censored_at_b` exists only after a valid terminal; a resource/process/hash/seal
fault sets no bit and authorizes no automatic rerun; a valid second censoring →
`BLOCKED_LEVEL1_FEASIBILITY` (C1 untested), no third learner-policy intervention;
no v1/v2 contrast may ever be formed; feasibility is `scientific_outcome:false`,
single-arm (RANDOM-STATIC), one replicate, dummy-panel-only — never a contrast,
N3, lock, escrow, or decision; the operational-modulus certificate and its sole S4
tooth, the public-root/escrow-secret-panel separation, and R_h-deferred all stand;
censored/`UNKNOWN` never success, equivalence, or a narrated boundary; development
artifacts non-citable forever; Level 1 is a detector, never evidence for
`PROOF_CORE`. The immutable v1 evidence is untouched.

**No v2 execution, authorization, entropy, probe, real panel, N3, lock, escrow,
trajectory, or outcome is authorized by this review.**

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
