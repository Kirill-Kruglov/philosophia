Written to `reviews/opus_level1_feasibility_v2_terminal_review.md`.

## Verdict: `LEVEL1_FEASIBILITY_V2_TERMINAL_XLINE_CONFIRMED`

The v2 gate was executed once (Kirill-authorized) and produced a valid censored terminal. Every mechanical check passes; the decision draft applies the pre-signed route 2 faithfully; **no corrections needed**.

**Mechanical integrity (independently recomputed):**
- Claim SHA `366029b7…`, report SHA `9d9942c8…`, auth SHA `54b70ead…` — all match the draft's recorded values; all three artifacts canonical; `report.authorization_sha256 == sha(auth)`.
- All seven lineage hashes (signature, 3 amendments, 2 immutable v1, transcript) recompute correct; the committed authorization is **byte-identical to the reviewed candidate**; `reviewed_code_head = f025cf7`.
- Commit chain clean: authorization commit `e3967a6` adds **only** the JSON (and is the run's `git_head`/EXPECTED_HEAD); evidence commit adds **only** claim+report; source byte-identical `f025cf7 ↔ e3967a6`.

**Terminal predicates:** 2000/2000 steps, losses **and** parameters finite, panel computable, `censored_at_b:true`, `validity:valid-scientific-terminal`, all 12 contamination guards false, no series persisted. No scout/N3/lock/panel/escrow/outcome/retry/temp artifact; single `feasibility_v2/` dir.

**§7 route:** Route 2 is the **single** valid route — not 1 (censored true), not 3 (A6: both finiteness flags true), not 4 (valid terminal, wall 35.82h < 36h, no fault), not 5 (hashes verify). → `BLOCKED_LEVEL1_FEASIBILITY`.

**Resource aggregates recompute** (mean 64.476 × 2000 = 128,951.863s = 35.820h; max 135.467; RSS 49.782 GiB; checkpoint 24.575 MiB) and are resource-only with no v1/v2 contrast. Notable: the run completed with only ~11 min of headroom under the 36h wall (realized step cost ~37× v1's), vindicating AM-4 — a 30h cap would have `RESOURCE_CAP`-invalidated it; but it *did* complete, so it's a valid terminal.

**Sentence-level attack — no leakage:** the draft keeps the Level 1 terminal as `BLOCKED_LEVEL1_FEASIBILITY` (never relabeled INSUFFICIENT or "learner lacks n"); C1 stays unrun/untested; not a boundary; no arm ordering; no programme falsification (claim stays OPEN); v1/v2 never contrasted. The Level 2 cascade is **precise, not a conflation** — Level 1 is feasibility-blocked, while the *separate* never-run C1 comparison is an "unresolved required comparison" that the signed CLAIM_LEDGER rule routes to INSUFFICIENT for the total selector. The two status lines match the amendment's pre-signed §7 lines verbatim.

**Admission answer: Yes** — route 2 was signed before execution (via `I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`), so selecting the terminal needs **no new author signature**; this bounded review confirms application, not a design reopening. Codex may admit the decision into README, ROADMAP, CLAIM_LEDGER, KILL_MATRIX, RESULTS_CANONICAL, and the essay, provided it uses the signed status lines verbatim, records Level 1 = `BLOCKED_LEVEL1_FEASIBILITY` / C1 unrun-untested / Level 2 blocked (INSUFFICIENT-for-selector, **no** programme kill), asserts no C1/capacity/efficacy/falsification claim, and authorizes no retry or later gate — the programme claim stays OPEN and Level 2 stays blocked under the signed total contact-mode rule. The ledger commits remain Kirill's as custodian, but no new scientific signature gates them.

**Confirmed:** no evidence modified, no learner run, no retry or later-gate artifact created, nothing committed. My actions were read-only inspection, hash/canonical recomputation, and commit-scope verification.
