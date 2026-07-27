Now writing the v2.1 correction.

`READY_FOR_OFFICINA_SUPERVISOR_V2_1_FINAL_XY_CONFIRMATION`

Two files created, nothing else touched:

- [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md)
- [fable_officina_supervisor_control_channel_v2_1_closure.md](reviews/fable_officina_supervisor_control_channel_v2_1_closure.md)

## The five load-bearing surfaces

**B1 (§W1).** Identity is two-level: `intent_scope_sha256` over `{activation record, command, arguments}` plus an `occurrence_index`, with `idempotency_key = SHA-256(scope, occurrence)` — both **recomputed and checked by the supervisor**, so nothing about the key is trusted. A durable client intent slot separates intent from retry mechanically: an occurrence without its `.done.json` mark is unfinished, so the next invocation resends it; otherwise a new occurrence is allocated. Successive heartbeats get distinct occurrences; a retry reuses one. No PID, clock, generation, or entropy in the key. Journal is four immutable predecessor-bound phase files with per-command `effect_plan` locators covering the multi-artifact `CLOSE`/`PAUSE`/`RESUME`/`ADMIT` automata. Key reuse with changed semantics is a plain `INVALID`, never G5. Ordinary effect-acks are implicit (successor occurrence or process terminal); only the one-use token needs an explicit ack; status observation is unjournaled so polling grows nothing; GC bounded by a permanent per-**scope** tombstone holding one integer.

**Spawn/singleton/takeover (§W2).** argv-embedded `spawn_intent_id` + `/proc/*/cmdline` discovery; grandchild **retains** the `SPAWN.lock` fd through identity install (safe because the argv serve tokens are deleted and both supervisor and watchdog use in-process post-fork entry, so there's no `exec`); bounded self-stop wait with one `BOOTSTRAP` route; takeover split into client control-plane and supervisor runtime phases.

**Watchdog (§W3).** Table published and acked before first `SIGCONT`; unacked renewal leaves the old deadline authoritative. `freeze_ns` is the instant whole-tree quiescence is *proved*, written by the watchdog itself into archival-excluded `WATCHDOG/**` — consistent with C1, which forbids only `runtime/` and ledger writes. Lost evidence → `freeze_ns = null` → unknowable route; no timestamp is ever synthesized. Zero-overrun branch deleted (unreachable), not replaced by a tolerance. Cause `PROCESS`; `T_PROCESS_RESOURCE_STOP` named as forbidden. Ack liveness on the watchdog's own sample.

**K1 (§W4).** `OPERATION_ADMIT` is the sole bound installer, circularity removed, nine ordered crash-reducible steps. Worker gets no writable output path; supervisor writes and hashes every byte in **one pass**, servicing watchdog + control between 4 MiB chunks, closing the read end at the ceiling. Custody spans reservations, pending settlement, quarantine, retained `T_PROMOTED`; only a disposition proving `custody_absent` releases. `FAILED` becomes a closed artifact with eight classes, each mapped to one signed route.

**Observation/promotion (§W5–W7).** One fixed `PENDING` shape; group descendants rejected on the CLI endpoint with the deliberate-escape residual stated as A3 procedural; offset-resume deleted; held-descriptor revalidation with the TOCTOU residual named; `st_dev` preflight so `EXDEV` cannot arise.

## Two things worth your attention

One signed sentence is superseded, named explicitly rather than by silence: harness §5a's "executes the v2.1 §1 sequence **at or before it**" (§W6.5). Its replacement is strictly weaker and fail-closed. That is the single compatibility item I flagged for both reviewers to attack.

Zero import-allowlist delta and `verification.py` byte-unchanged were preserved throughout — which is why the serve loop is a `time`-paced poll and no `prctl` subreaper containment is claimed.

All 31 findings (6 X-Critical, 11 X-Major, 7 X-Minor, 5 Sol Critical, 2 Sol Major with seven sub-items) are dispositioned to named loci in §W9; the 50-row test matrix covers every Critical and Major in rows 1–35. The dirty implementation is unchanged and still has zero occurrences of supervisor/FIFO/journal/watchdog/pipe2 — it neither cures nor creates any of these defects. T `NOT_ACTIVATED`, claim `OPEN`, runtime dir still just `T_RUNTIME.lock`.
