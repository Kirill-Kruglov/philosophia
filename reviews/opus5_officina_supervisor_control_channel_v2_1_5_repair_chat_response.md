All three pinned hashes match. Reading both v2.1.4 reviews in full.

All anchors confirmed — Sol m2's provenance finding is exactly right (C2, M2, M3 mismapped, M4 labelled "m2", m1 omitted, "six" for seven). Writing the correction.

Custody verified: exactly two new files, all prior artifacts byte-unchanged, pre-existing dirty set untouched.

**[successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md)** — 707 lines, `7ef8e4d3…`. §V215.0 names 12 superseded clauses and declares no other text moves; §V215.1–§V215.4 map onto R1–R4.

**[reviews/opus5_officina_supervisor_control_channel_v2_1_5_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_5_closure.md)** — line 1 `READY_FOR_OFFICINA_SUPERVISOR_V2_1_5_FINAL_XY_CONFIRMATION`, all 10 proof obligations.

Judgment calls worth surfacing:

- **R1 — I made exclusivity structural, not ordinal.** Rather than relying on "first match wins," each row predicate carries its own negation of the competing terminal (`B-P` requires `¬Q`; `B-QM`/`B-QN` require `¬S`), so the both-terminal layout satisfies row 1 and *nothing else*. Ordering became a presentation aid. I also split row 5 into eight lettered sub-rows so "every other state" isn't a residual bucket — each has its own literal predicate and its own continuation, distinguishing *impossible durable layouts* (record-first invalidity) from *ordinary not-yet-terminal* states (refuse).
- **R2 — the `EINTR` disposition needed a stated reason.** On Linux `close()` releases the descriptor even when it returns `EINTR`, so the routine treats it as closed and **never retries**; retrying could close a descriptor the process has since opened at the same number. `EBADF` is success, every other errno is closed, and the routine never raises — which is what makes it idempotent and leak-free.
- **R2 — kill must precede record removal.** The kill route reads the very identity records step 3 deletes, so `REFUSAL_SEQUENCE` is ordered kill → fd cleanup → record removal → lock release. Getting this backwards would strand an unkillable process.
- **R2 — the `m7` route is faster than the deadline path.** Because no grandchild exists when the second fork fails, the middle child closing `boot_w` removes the *last* boot writer, so `c13` sees EOF immediately rather than waiting out its bound.
- **R3 — I did not manufacture a bound for `c14`/`c15`.** No signed text bounds a `/proc` read or an `fsync`, so inventing one would have been a new resource cell. The bound is restated as policy, expiry is a permitted fail-closed refusal, and I added the two properties the prompt asked for: it creates no citable artifact, and since `REFUSAL_SEQUENCE` removes every record, no state carries between attempts — there is nothing to shop for.
- **The authorization state is recorded rather than softened.** X confirmed v2.1.4 conditionally on Y; Y revised; the token never became signable; and because the bytes change, no earlier confirmation carries across.

Zero new constants, objects, paths, schemas, keys, tokens, or import delta — this layer is predicate and lifecycle text only. T remains `NOT_ACTIVATED`; claim `OPEN`; token unsignable pending fresh X and Y confirmation on `7ef8e4d3…`.
