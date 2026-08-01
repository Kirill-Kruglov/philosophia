All three pinned hashes match. Reading the Y-line review and the X chat trace.

All five Sol findings verified against the bytes — including that at `m0` the middle owns its own `rel1_w` copy, so EOF there is impossible in principle. Writing the correction.

Custody verified: exactly two new files, all prior artifacts byte-unchanged, pre-existing dirty set untouched.

**[successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md)** — 820 lines, `e4aa9ef4…`. §V216.0 names 17 superseded clauses and states nothing else moves; §V216.1–§V216.5 map onto R1–R5.

**[reviews/opus5_officina_supervisor_control_channel_v2_1_6_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_6_closure.md)** — line 1 `READY_FOR_OFFICINA_SUPERVISOR_V2_1_6_FINAL_XY_CONFIRMATION`, all 10 proof obligations.

Judgment calls worth surfacing:

- **R1 — I blocked each counterexample twice, not once.** `MALFORMED` dominates as Rule 0 *and* every releasing rule carries physical absence of the opposite terminal (`¬PQ` for B-P, `¬PS` for B-QM/B-QN). Either conjunct alone would close Sol C1; both together mean a single editing slip can't reopen it. I also made presence explicitly decode-free — a symlink, directory, zero-byte or truncated file at a canonical name is *present* — since that is exactly where "malformed reads as absent" crept in.
- **R1 — Sol's fourth counterexample needed a different fix from the other four.** It wasn't a release path but two *differently named* invalidity routes for one state. Making Rule 0 dominant means only Rule 0 fires; I also recorded that Rules 0 and 1 share one continuation class, so their order can't change an outcome.
- **R2 — the per-site `CLOSED_ERROR` routing came out uniformly CONTINUE, with a reason.** On Linux the descriptor is released in every outcome except `EBADF` (nothing open) and `NOT_OWNED` (nothing attempted), so the observable pipe state after a close error is identical to success. No site's correctness depends on a close's return value. Stating that once removes the discretion rather than leaving a per-site judgment call. The `NOT_OWNED` short-circuit — no syscall at all — is what actually makes a reused number unclosable.
- **R3 — I proved Sol's point is stronger than stated.** At `m0` the middle owns its own `rel1_w` copy, and EOF requires *every* writer closed, so EOF there is impossible **in principle**, not merely unlikely. And the fail-closed continuation now says plainly that the singleton is *not* free while the middle lives — replacing a false "released" cell rather than papering over it.
- **R4 — replaced, not extended, at five audited loci.** The exhaustive phrase search found exactly five; one was already superseded, so four needed action. Row 126 now tests the deterministic slow-valid refusal, which makes row 159 satisfiable for the first time.

On the X line: the saved trace ends mid-sentence before the review file was created, so there is **no X verdict for v2.1.5** — I recorded that as fact, and noted (without relying on it) that the trace's provisional "selector holds" claim is what Sol C1 refutes.

Zero new constants, objects, paths, schemas, keys, tokens, or import delta. T remains `NOT_ACTIVATED`; claim `OPEN`; token unsignable pending fresh X **and** Y reviews of `e4aa9ef4…`.
