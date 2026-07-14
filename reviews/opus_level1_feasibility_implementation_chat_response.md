Written to `reviews/opus_level1_feasibility_implementation_review.md`.

## Verdict: `REVISE_LEVEL1_FEASIBILITY_IMPLEMENTATION`

I first verified the source-byte pin: all twelve reviewed paths are byte-identical between `308aa6f` and HEAD. The implementation is faithful to §5/A3/A5/A8/A10 and safely gated — hard caps, one RANDOM-STATIC arm, one replicate, discarded scorer choices, dummy-panel separation, source pin (incl. `config.py`), durable pre-run claim, preflight no-retry, no forbidden derivation. Tests: 6 feasibility + 139 full passed, verifier VALID, no artifacts/authorization present.

**One Major gap (Q7):**
- **FS-1 — the trajectory step and end-to-end loop are untested.** Persistence (`checkpoint_qualifies`/`first_persistent_step`) and the scorer (`select_by_disagreement` no-mutation) *are* component-tested, but `feasibility_committee_step` and `run_noncomparative_feasibility` are never called. So the load-bearing behaviors Q2 asks about — **one trajectory-step spent per oracle step (not four), all four members on the one shared minibatch, the update order, the non-finite break, the step-0 + cadence checkpoints, the scorer state-unchanged guard** — are correct on inspection but unpinned. A trajectory-wrong refactor would pass. Mandatory: a `feasibility_committee_step` unit test + a bounded end-to-end wiring test.

**Minor:** scorer timing excludes per-step candidate realization (FS-2); the RANDOM projection excludes checkpoint-eval cost (FS-3); `public_root.py` (output plumbing) isn't in the pinned set though no-retry is also preflight-guarded (FS-4); `realize_cell` lacks an explicit exhaustion guard (FS-5); the report's contamination guards are declarative, not derived (FS-6, mitigated structurally).

I answered all seven checks in detail. Notably **Q5 (dummy-panel separation)**: `DummyPanelBuilder` now accepts the real public root for genuine reservation geometry but *mandates a test-only panel key*, so it can only build dummy panels and can never touch the real escrow-secret seed — the real-panel boundary is intact. **Q2**: the capability counts **oracle steps, not member updates** — correct.

**May Codex prepare an authorization candidate but not execute it? — Yes.** Codex may draft the authorization JSON with the frozen structural fields (schema, caps, arm, world, output dir, `scientific_outcome:false`, `execution_once:true`, resolved heads), but the `I_AUTHORIZE_...` **token and its commit are Kirill's explicit act** — Codex must not self-authorize, invoke the driver, create the claim/report, draw entropy, build a real panel, or touch any later gate.

The review lists the mandatory edits, the exact execution guards a future authorization must bind, and the preserved negative space. No feasibility execution, authorization, entropy, real panel, N3, lock, escrow, trajectory, or outcome is authorized; nothing was committed or run.
