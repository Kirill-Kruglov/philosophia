# Opus review prompt: Level 1 feasibility v2 terminal-route audit

Review the immutable evidence and terminal decision draft at commit
`ae18a3efec802ab206a58e4c8db3e8aa955ce501`:

- `experiments/level_1_contact/feasibility_v2/LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2_CLAIM.json`
- `experiments/level_1_contact/feasibility_v2/LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2.json`
- `experiments/level_1_contact/FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json`
- `experiments/level_1_contact/FEASIBILITY_V2_GATE_DECISION_DRAFT.md`

The evidence-only commit is
`756648ae427f9738e22bbcc58e1669702c62fb1e`; the authorization commit is
`e3967a64fcaefeb605713d2e337d888919392541`; reviewed code is
`f025cf7fe981c8ae41f502d2e7608e6e9273fc25`.

Mechanically audit:

1. Recompute claim/report hashes and verify every lineage hash against the
   authorization, governing amendments/signature, immutable v1 evidence, and
   public-root transcript.
2. Confirm canonical JSON, schemas, `scientific_outcome:false`, execution
   token, frozen arm/world/replicate/caps, reviewed code HEAD, and
   `validity:valid-scientific-terminal`.
3. Confirm `B=2000` was completed, losses and parameters are finite, the
   dummy panel is computable, `censored_at_b:true`, and all contamination
   guards are false.
4. Confirm no comparative scout, N3 selection, preregistration lock, real
   panel, escrow, Level 1 outcome, retry artifact, or uncommitted temporary
   artifact exists.
5. Apply §7 of
   `FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md` plus v2.1/v2.2 literally.
   Is route 2, `BLOCKED_LEVEL1_FEASIBILITY`, the single valid route?
6. Recompute or reject the resource aggregates in the draft. Confirm they are
   resource-only and never a v1/v2 efficacy contrast.
7. Attack every sentence that might silently turn feasibility censoring into a
   C1 result, a programme boundary/falsification, a learner-capacity claim, a
   retry authorization, or permission for a later gate.
8. State exact corrections, if any, before canonical admission.

Do not modify evidence, run a learner, create a retry, or create any later-gate
artifact. Read-only tests and verification are allowed. Do not commit.

Write `reviews/opus_level1_feasibility_v2_terminal_review.md`.
Lead with exactly one verdict:

- `LEVEL1_FEASIBILITY_V2_TERMINAL_XLINE_CONFIRMED`
- `REVISE_LEVEL1_FEASIBILITY_V2_TERMINAL_DECISION`
- `LEVEL1_FEASIBILITY_V2_TERMINAL_INVALID`

If confirmed, state whether Codex may admit the decision into README, ROADMAP,
CLAIM_LEDGER, KILL_MATRIX, RESULTS_CANONICAL, and the essay without another
author signature, while leaving C1 unrun/untested and Level 2 blocked under the
signed total contact-mode rule.
