Both defects confirmed, plus two further affected loci (v2.1 §W2.1's "its parent is `1`", and row 359's supervisor-side pinned-set assertion). Writing the repair.

Custody verified: exactly two new files; v2.1.10.5, its closure, the P1 signature, and `verification.py` unchanged at their pinned digests.

## Done — R1 and R2 closed

| Deliverable | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md) | `8f806e33…143e` |
| [opus5_officina_supervisor_control_channel_v2_1_10_6_pre_xy_repair_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_10_6_pre_xy_repair_closure.md) | `65a32a6e…11cd` |

Closure line 1: `READY_FOR_OFFICINA_SUPERVISOR_P1_PRE_XY_REPAIR_FINAL_CONFIRMATION`.

**R1 — the bounded interpretation is PROVED, so no `BLOCKED` was owed.** I explicitly tested the stop-branch by auditing every consumer of a wait result or exit status in the composite. **Exactly one decision branches on a status word** — `AWAIT_STOP`'s carried `WIFSTOPPED` — and its target is a direct child of the PCS, never an orphan. Everything else uses the returned *pid* of a PCS child, an object-bound `/proc` fact, or a channel EOF; the caller's view of the PCS was already advisory-only. A fifth crash row proves the `killpg` group anchor is `pid_mid`, a PCS child never orphaned while the PCS lives, so subreaper semantics can't reach it. Nothing architectural added — `S-24` enforces that `prctl`/`PR_SET_CHILD_SUBREAPER`/`ctypes` appear in no root.

**R2 — `S-18'` is a three-site whitelist with per-site permission:** `P-f` read-only, `A-5` read-only, `G-5` may close within a pinned keep-set; forbidden in the supervisor's receive path, any remediation, any handle-release, and any phase where live role handles coexist. The `G-5` disjointness proof is temporal — it runs before `G-6`'s `execve`, hence before `A-10`/`A-13`, and role descriptors arrive only by `SCM_RIGHTS` after the first `SPAWN_ROLE`. No "nowhere" sentence survives.

The audit also caught two loci the brief didn't name: carried v2.1 §W2.1's parenthetical "**after the double fork its parent is `1`**" (deleted as false — its actual claim, that `getppid()` isn't used for the supervisor, is retained and is now load-bearing), and row 359's assertion of a supervisor-side "pinned set" that in fact grows with every live handle.

The honest framing: **R1 makes the contract truthful, not stronger.** It now admits a contaminated ancestor may parent and reap the supervisor and every role after PCS death. Safety rests on my own audit being complete, and `S-25` plus row 504 are the only mechanical guard — which is why that's the first weakest point and the first thing both questions ask about. All five F1–F5 closures, the P1 selection, the topology, and A3/B1/C1/D1/K1 are re-confirmed unchanged.

No acceptance token from this round. T `NOT_ACTIVATED`; claim `OPEN`.
