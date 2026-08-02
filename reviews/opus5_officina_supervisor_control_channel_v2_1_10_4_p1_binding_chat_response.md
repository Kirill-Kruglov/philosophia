The signature exists. Reading it in full.

Signature verified — P1, with an explicit mandatory-binding section. Hashing the full governing set.

All three signature hashes reproduce exactly. Writing the P1 binding.

The audit surfaced a real name collision: `§U6.1`'s carried preflight steps are literally named `P0`–`P3`. Fixing the test row that would have been ambiguous, and tightening one proof step.

Now the closure.

Custody verified: exactly two new files; the signature, v2.1.10.3, and `verification.py` unchanged at their pinned digests.

## Done — P1 bound

| Deliverable | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md) | `6197d2a4…e84` |
| [opus5_officina_supervisor_control_channel_v2_1_10_4_p1_binding_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_10_4_p1_binding_closure.md) | `5889461b…302` |

Signature read in full; all three of its governing hashes reproduce exactly; its base commit is an ancestor. Closure line 1: `READY_FOR_OFFICINA_SUPERVISOR_P1_COMPOSITE_XY_REVIEW`.

**One operative architecture.** P3/P4 are deleted from the operative contract and survive only in a provenance table with an explicit rule that no operative text may condition behaviour on them. `SPAWN_WATCHDOG` has one uniform meaning — the rename, the `WATCHDOG_REPLACEMENT` handle role and the degradation flag are gone, so there is no first-versus-replacement asymmetry.

**B3 — the capability statement.** "A resource fact, not an authority fact" is deleted; an installed `SCM_RIGHTS` descriptor is a capability. The rule is grounded in `scm_detach_fds()`: Linux installs `min(space, queued)`, reports exactly those, and releases the rest — so an installed-but-unreported descriptor cannot exist at the kernel boundary. The one uncovered interval is an interpreter-side raise inside `_recvmsg`, handled by an immediate `_exit_` with no callback and named as a transient **capability leak**, left inside A3 without upgrading A3.

**B4 — cells bound without softening.** C1 keeps a dedicated freezer watchdog **and** P1 intentionally cuts supervisor-death detection from two mechanisms to update-pipe EOF — stated as the selected trade, with a test row forbidding any text that calls it "unchanged". B1's descriptor non-redelivery means a lost ACK invalidates a generation. D1's availability now rests on an unrecoverable PCS. K1/A3 carried without upgrade.

The audit caught one real defect in my own draft: `§U6.1`'s carried preflight steps are literally named `P0`–`P3`, so a naive "no `P3` anywhere" test would have collided with them. Row 437 now matches option *tokens and phrases*, never bare letters, and exempts the preflight names explicitly. I also tightened the `SPAWN.lock` step of the leak proof, which had a rhetorical feint in the middle of a load-bearing argument.

Eight weakest points are written against the composite, including that the leak proof is now load-bearing for C1 in a way it wasn't under two detectors. Three bounded questions each for X (Opus 4.8) and Y (Sol) on identical bytes. Token unavailable until both confirm digest `6197d2a4…`. T `NOT_ACTIVATED`; claim `OPEN`.
