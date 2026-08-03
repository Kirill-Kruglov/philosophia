# Task: independent X-line review of P1 watchdog-freeze choice packet v1

You are Claude Code Opus acting as the independent **X-line engineering/mechanical reviewer**. You did not author the packet. Work read-only except for the single review deliverable. Do not implement code, run process-control probes, activate T, or alter programme state.

## Review target

Review the committed bytes of:

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
- `reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md`

Recompute their SHA-256 hashes. Treat the author closure as untrusted. Inspect the governing P1 composite, authority selection, C1/watchdog, generic-harness, and activation contracts directly.

Write exactly:

- `reviews/opus_officina_p1_watchdog_freeze_choice_review.md`

Do not modify any existing file.

## Required determinations

1. Independently prove or refute the blocker: selected P1 forbids the watchdog's `killpg`, makes PCS the sole signal caller, closes watchdog slot 6, and leaves no relay when supervisor death triggers update-pipe EOF. Verify the corollary that PCS retaining the update-pipe write end would suppress EOF.
2. Attack W-A mechanically: descriptor topology and leak proof, one-opcode/no-target grammar, generation/table binding, replay/idempotency, ack timeout, first/replacement symmetry, crash cuts, and the new dependency on a live watchdog.
3. Attack W-B mechanically: whether `PEER_EOF` is a unique and sufficient kernel-fact trigger; whether ordering between control-socket EOF and watchdog update-pipe EOF creates any race that matters; once-per-generation journaling; exact handle scope; idempotent freeze procedure; PCS crash/restart cuts; and whether this is genuinely bounded autonomous initiative rather than an unreviewed general authority.
4. Verify that supervisor death, PCS death, watchdog death, half-close, inherited descriptor leak, stale generation, replacement watchdog, and simultaneous failures each have one deterministic route.
5. Verify that neither option requires the unresolved PID/PGID identity choice and that `ABSENT` is a legitimate signed witness route rather than fabricated evidence.
6. Verify the packet's blast-radius and recommendation comparison. In particular, determine whether W-B truly changes zero P1 sentences while amending C1, and whether all contract sentences that made the watchdog the freezer/witness are enumerated.
7. Verify that PCS does not accidentally retain the watchdog update-pipe write end under either option.

## Verdicts

Use exactly one:

- `OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_XLINE_CONFIRMED_FOR_AUTHOR_SELECTION`
- `REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_PACKET`
- `BLOCKED_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE`

Lead with findings ordered by severity. If `REVISE`, give the smallest exact repairs and say whether W-B remains mechanically preferable after them. If confirmed, explicitly state that confirmation authorizes only Kirill's informed A/B selection, not implementation or activation.

The review must preserve: `T = NOT_ACTIVATED`, programme claim `OPEN`, no selection, no process control, no spend/data/outcome, and no implementation authority.
