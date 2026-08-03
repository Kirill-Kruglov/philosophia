# Task: bounded X-line confirmation of P1 watchdog-freeze choice packet v2

You are Claude Code Opus acting as independent X-line engineering reviewer. This is a bounded confirmation round, not a new design round. Work read-only except for the one deliverable. Do not implement or execute process-control behavior, activate T, or alter programme state.

## Target

Review committed bytes of:

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`
- `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md`

Compare directly against both v1 reviews and governing contracts:

- `reviews/opus_officina_p1_watchdog_freeze_choice_review.md`
- `reviews/sol_officina_p1_watchdog_freeze_choice_review.md`

Recompute hashes and treat the author closure as untrusted.

Write exactly:

- `reviews/opus_officina_p1_watchdog_freeze_choice_v2_confirmation.md`

Do not modify any existing file.

## Bounded determinations

1. Confirm/refute all X F1-F3 and Y-C1..Y-C3/Y-M1..Y-M3/Y-m1 closures one by one.
2. Mechanically audit the new PCS classifier: `STAT_OBSERVE_G` Linux `/proc/<pid>/stat` field indices, `KV-1..KV-6`, `pgid_or_null` population, deduplication, all signed handle states, the sixteen result tokens, three terminals, and every durable continuation.
3. Prove whether it uses only already-bound primitives/imports/constants plus the disclosed `_MSG_EOR` addition. Identify any missing primitive, module, constant, syscall wrapper, record field, or descriptor.
4. Verify W-B's endpoint-loss classifier distinguishes empty SEQPACKET record from EOF/half-close, journals `ACCEPTED` before action, never retries after an accepted prefix, and never claims supervisor death.
5. Verify repaired W-A is genuinely one-shot, no-target, gated, descriptor-accounted, ordered against endpoint loss, and cannot repeat a freeze or retain the watchdog update-pipe write end.
6. Audit the full composite for every freezer/witness sentence. Confirm that the twelve-site replacement is complete and contains no contradictory old row or invariant.
7. Verify the nullable-identity `ABSENT` amendment is mechanically serializable and that no PCS journal state becomes peer witness evidence.
8. Examine author-disclosed weak points: `setsid()` escape, quiescence interval substitution, `_MSG_EOR` binding, `current_unresolved_member_count`, and any hidden peer reader that assumes a watchdog-written record.

## Verdict

Use exactly one:

- `OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_XLINE_CONFIRMED_FOR_AUTHOR_SELECTION`
- `REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2`
- `BLOCKED_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2`

If confirmed, authorize only Kirill's informed W-A/W-B choice and associated disclosed amendments, not implementation or activation. If `REVISE`, give only concrete residual defects and their smallest exact repairs.

Preserve `T = NOT_ACTIVATED`, programme claim `OPEN`, and identity-cell non-selection.
