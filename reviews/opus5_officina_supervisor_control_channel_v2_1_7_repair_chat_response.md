All three pinned hashes match. Reading both v2.1.6 reviews in full.

Both reviews verified. My own semantic sweep found a **sixth** stale locus (v2.1.2 §N11 line 1407) beyond the four Opus named — exactly the false-exhaustiveness failure mode to avoid. Writing the correction.

Custody verified: exactly two new files, all prior artifacts byte-unchanged, pre-existing dirty set untouched.

**[successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md)** — 880 lines, `78973247…`. §V217.0 names 19 superseded clauses and states nothing else moves; §V217.1–§V217.4 map onto R1–R4.

**[reviews/opus5_officina_supervisor_control_channel_v2_1_7_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_7_closure.md)** — line 1 `READY_FOR_OFFICINA_SUPERVISOR_V2_1_7_FINAL_XY_CONFIRMATION`, all 9 proof obligations.

Judgment calls worth surfacing:

- **R4 — my own sweep found a locus neither the X finding nor v2.1.6's "exhaustive" search enumerated.** v2.1.2 §N11's crash-cut cell "every contract-following CLI wait is bounded" is a tenth locus. I declared the eighteen search terms used so a reviewer can reproduce the sweep, listed four *retained* true-but-specific statements to show it was semantic rather than phrase-matching, and scoped the completeness claim explicitly — it asserts what those terms found in those files, not that no equivalent phrasing could exist. Repeating v2.1.6's unqualified "there are no others" would have been the same error twice.
- **R3 — the wedge dissolved once I asked what `SPAWNING.json` actually protects.** Death-before-unlink exists to protect a record that is the *sole durable handle on a process that may still act*. `SPAWNING.json` names only the CLI — it is never a handle on the middle child, group, or grandchild — so removing it can orphan nothing. The abandoning CLI therefore always removes its own record, and the boundary stays intact for the three records it genuinely protects. That needed no new record, schema, path, or tier, and I added the two-supervisor safety proof (`m5` sees EOF once the CLI closes `rel2_w`, so the middle can never fork a grandchild).
- **R2 also fixed R3's root cause.** Making `waitpid` the authoritative, `/proc`-independent death proof means an unreadable `/proc` no longer blocks the proof at all — so the fail-closed path Sol found is now reached only under a host fault. I stated the premise `ECHILD ⇒ PROVED_DEAD` depends on: the contract installs no signal disposition anywhere, so `SIGCHLD` keeps its default, nothing is auto-reaped, and this route is the only reaper.
- **R1 — I did not claim the barriers make the attack impossible.** They bind the observation to inodes and bytes and re-check at two points; a mutation after the final barrier is the signed A3 procedural residual, named and non-citable. `T_RUNTIME.lock` serializes contract actors and is not a same-UID filesystem exclusion mechanism — saying otherwise would have repeated exactly the over-claim Sol C1 penalised.

Zero new constants, durable objects, paths, schemas, keys, tokens, or import delta. T remains `NOT_ACTIVATED`; claim `OPEN`; token unsignable pending fresh X **and** Y reviews of `78973247…`.
