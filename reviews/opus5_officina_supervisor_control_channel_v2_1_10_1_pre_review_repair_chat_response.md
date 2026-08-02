I'll verify the pinned hashes and ancestry, then locate the exact contradictory loci in v2.1.10.

Both hashes verify. Pulling the exact contradictory loci for the replacement index.

All seven blockers confirmed literally in the v2.1.10 bytes. Writing the correction.

Custody verified: exactly two new files; v2.1.10 and its closure unchanged at their pinned digests; `verification.py` unmodified; the specified bootstrap script correctly absent; pre-existing dirty/untracked paths byte-identical.

## Done — v2.1.10.1 pre-review correction

| Deliverable | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md) | `2d4d4b18…759b` |
| [opus5_officina_supervisor_control_channel_v2_1_10_1_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_10_1_closure.md) | `f7a866f9…2008` |

Both pinned hashes verified. Closure line 1: `READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_1_FINAL_XY_CONFIRMATION`. No X/Y review requested.

**B1** — resolved to `{os, sys, _signal, time, fcntl}`. Using the built-in `_signal` deletes `functools`/`enum`/`_thread` from the closure outright, so v2.1.10's `_thread` note is withdrawn rather than mitigated — and it makes the signal primitives genuine built-ins, which is what made the universal identity predicate expressible at all. That predicate would have **rejected the genuine `signal.signal`** (a pure-Python wrapper); it's replaced by a per-primitive table with a `type(len)` object-identity anchor.

**B2** — the "same inode" claim deleted. Source and interpreter stay open on pinned descriptors; the literals `/proc/self/fd/7` and `/proc/self/fd/8` are the exec targets. `sys.executable` is no longer called kernel-supplied and is used for nothing. `readlink` is added to the verifier's forbidden-symbol list so it can't recur.

**B3** — `Popen`/pre-exec-`dup2`/`cwd` deleted as impossible; replaced by `posix_spawn` with a deterministic hoist (all sources ≥ 9) and twelve ordered file actions (six `DUP2` onto 3–8, then six `CLOSE`), collision-free by range disjointness, with `POSIX_SPAWN_DUP2`'s close-on-exec clearing doing the inheritance work. `chdir("/")` moves into the bootstrap.

**B4** — stated as a disjunction: exact isolated process, or no authorized bootstrap. Launcher checks are labelled **diagnostic, not the safety mechanism**.

**B5** — "hostile caller launches an arbitrary supervisor" withdrawn: fd 6 ↔ fd 7 `(st_dev, st_ino)` binding, plus role-side `R-1` re-verification. Byte provenance is explicitly a deploy-time manifest obligation, with the limit stated flatly.

**B6** — route 2 ruled unavailable by inspection; route 1 taken. The bootstrap becomes the Process-Control Server and **the supervisor is given handles, never PIDs** — its wire vocabulary has no pid field, so PID-reuse sensitivity is removed structurally. Bounded by "relocate the primitive, preserve the semantics".

**B7** — eight reconciliations, a `SigBlk == 0` check, a `NO_REPLY` route, and every caller-misbehaviour case routed through `T_PROCESS_INVALID` + the §4c(c)/§4d unknowable route. "Its own user" is withdrawn as a disposition.

The honest flag: **B6 is the largest amendment in the chain** — it touches §W2.1, §W2.4, §W2.5, §W3.3, §Z3.3 and C1's creation path. I've said plainly that a reviewer may judge it needs its own layer, and put that question directly to the X line as X-Q3 so it can be ruled on rather than argued around.

T `NOT_ACTIVATED`; claim `OPEN`; token unavailable.
