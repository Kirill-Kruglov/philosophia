All three pinned hashes match. Reading both v2.1.3 reviews in full.

Sol m1 confirmed exactly: line 8 is 43 bytes with LF; the 504-byte total is unaffected. Writing the correction.

Custody verified: exactly two new files, all prior artifacts byte-unchanged, pre-existing dirty set untouched.

**[successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md)** — 1159 lines, `cc5af143…`. §V214.0 names 30 superseded clauses; §V214.1–§V214.7 map onto R1–R7.

**[reviews/opus5_officina_supervisor_control_channel_v2_1_4_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_4_closure.md)** — line 1 `READY_FOR_OFFICINA_SUPERVISOR_V2_1_4_FINAL_XY_CONFIRMATION`, all 11 proof obligations.

Judgment calls worth surfacing:

- **The authorization state needed care.** X *confirmed* v2.1.3 and made the token conditional on Y also confirming; Y returned REVISE, so the condition never fired and the token never became signable. X also said patched bytes take a fresh confirmation. The closure records this exactly rather than implying X's confirmation carries forward.
- **R1 — I made all four channels nonblocking, not just `boot`.** Sol only required the report channel, but leaving `rel3` blocking would violate "no blocking syscall may prevent deadline evaluation." The grandchild gate gets a derived bound of `2 × T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` — the factor two is forced: between `m7` and `c16` the CLI does a full 10 s-bounded `boot` read plus a verify and an install, so a 1× bound would kill healthy bootstraps.
- **R1 — I declined the early-close option.** The prompt allowed closing the grandchild's inherited `boot` write end before its gate, but that would break the independently confirmed "literal first instruction is the gate read" property. Instead I showed the nonblocking deadline alone makes every cut total, and I state per-cut whether termination comes from EOF or the bound — Opus X213-m2's exact complaint. EOF is now asserted only where a sole-writer argument supports it.
- **R2 — I took the stronger of the two suggested repairs.** Rather than only widening V6's exemption, the orphan manifest is *bound* in `QUARANTINE.json` and gets its own verified branch, so the disposition is anchored to the quarantine record rather than merely permitted.
- **R3 — deleting `ack.json` before `accepted.json` needed an argument, not just an order.** It is sound because the tombstone's `acknowledged_prefix_occurrence` is permanent and, by the contiguous-prefix construction, `i ≤ prefix` *is* the durable proof of acknowledgement; `ack.json` is a per-key witness of the same fact. That is what lets the finalization rule work with only `accepted` plus the tombstone.
- **R5 — the diagnostic set is required, not optional.** Recording all true conditions is safe because every I-condition routes identically and nothing reads `invalid_condition`; making it required removes the "which one did you record" ambiguity rather than leaving it to the implementer.

Sol m1 verified independently: the line is 43 bytes with LF (10+1+1+30+1), and the eight lines still sum to 504, so no digest in the chain moves.

Zero new constants, objects, paths, tokens, or import delta; two schemas gain one key each. T remains `NOT_ACTIVATED`; claim `OPEN`; token unsignable pending fresh X and Y confirmation on `cc5af143…`.
