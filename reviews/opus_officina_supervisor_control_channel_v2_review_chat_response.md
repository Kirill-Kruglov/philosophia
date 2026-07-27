I'll start by reading the required documents.

Wrote [reviews/opus_officina_supervisor_control_channel_v2_review.md](reviews/opus_officina_supervisor_control_channel_v2_review.md) — one new file, nothing else touched.

**Verdict: `REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2`** — 6 Critical, 11 Major, 7 Minor. A3/B1/C1/D1 not reopened.

The four Criticals that matter most:

- **B1 is inverted (§V2.5).** The journal keys on whole-frame `request_sha256`, which contains `client_pid`, `client_start_identity`, `client_monotonic_ns`, `reply_fifo`, and the generation hash. Every real retry — a re-run CLI is a new process; a cross-generation retry must carry the new generation hash — therefore differs in bytes and hits "same key, different bytes → record-first invalidity", i.e. **G5**. The exact lost-reply case B1 was chosen to fix now ends worse than v1, and any same-UID client can force G5 by reusing a key. The packet's own B1 text said "byte-identical **semantic** request"; v2 dropped the word.
- **F4 is still open (§V2.1.4/§V2.1.6).** `t-spawn-intent.v1`'s exact keys contain no PID, start identity, session, or argv — only `argv_sha256` — so "takeover kills by registry identity" has no referent. The stopped pre-claim child is also not woken or reaped by the kernel after supervisor death (its group was already orphaned at `setsid`), so it persists indefinitely. A durable race-free bridge does exist: embed `spawn_intent_id` in the child's argv and discover via `/proc/*/cmdline`. Separately, `waitpid(WUNTRACED)` on client-supplied argv can wedge the runtime forever, and `¬WIFSTOPPED` has no continuation.
- **The operation surface cannot be entered (§V2.7.1).** No command installs `BOUND.json`; `max_total_output_bytes` is simultaneously a key of the supervisor-owned bound and "controller-supplied after bound install"; `<pending_op_key>` is undefined. `OPERATION_ADMIT` is total-refuse. And the "reservation" is an integer sum against nothing — an arbitrarily large declared bound is unbounded read/hash/copy work, which then starves the watchdog ack path.
- **C1's overrun has no single continuation (§V2.6.5).** Signed `T_PROCESS_RESOURCE_STOP` — designed for exactly "actual overrun recorded in full" — is not excluded; cause is left "`PROCESS` or `CLOCK`"; and since `freeze_ns` is sampled *after* `now ≥ deadline`, the zero-overrun branch is unreachable dead text inviting an unauthorized tolerance. When the freeze event is lost, `freeze_ns` cannot be re-derived, so a signed ending's *validity* depends on a lossy pipe read.

Genuinely closed and not to be reopened: F7, F8, F10 (the inherited-pipe credential is v2's strongest mechanism), F11, F12, F13, F14, F15, Sol M3/M4/M5, A3's Q/C non-inheritance bar, and the whole Codex §S6 carry including the `-m` argv fix.

On the argv question you flagged: **delete the tokens.** `--supervisor-serve` cannot be parentage-checked at all (after a double-fork `getppid()` is 1), and §V2.1.2's "same module image, no new argv" already contradicts §V2.10. In-process post-fork function entry is the smaller safe mechanism for both supervisor and watchdog; only the controller needs `exec`.

Repair is **bounded** and needs **no new author choice** — one conditional: closing the output-byte DoS mechanically (admission-time `statvfs` reservation + chunked ack-servicing hash loop) avoids a cell; a hard signed ceiling instead would be the additional token the packet already flagged. No token becomes eligible from this review.

No code ran, no process/FIFO/journal was created, nothing committed. `runtime/` holds only `T_RUNTIME.lock`, envelope `activated: false`, T remains `NOT_ACTIVATED`. (The untracked `reviews/sol_officina_supervisor_control_channel_v2_review.md` appeared during this pass — that's the parallel Y-line, not mine.)
