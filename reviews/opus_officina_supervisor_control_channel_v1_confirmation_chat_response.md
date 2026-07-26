Done. I wrote the single required file, `reviews/opus_officina_supervisor_control_channel_v1_confirmation.md`, and changed nothing else (the `accounting.py`/tests `M` entries are the pre-existing dirty files, and `sol_*_confirmation.md` is a concurrent reviewer's — both untouched).

## Verdict

**`REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V1`** — the token `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not ready** for Kirill's signature.

The draft picks one topology and correctly closes most of the surface I previously blocked (and its §S6 repair ledger faithfully carries every earlier C1–C4/M1–M6 finding, none weakened). But an adversarial trace against **real Linux semantics** — verified with probes, not prose — found genuine gaps:

**Two Critical (need bounded author choices):**
- **F1** — `CLAIM` is not idempotent under a committed-but-lost reply. Because the replay rule *requires* a strictly-increasing `client_monotonic_ns`, a re-run is a genuinely new request that spawns a **second controller + durable claim**. "Idempotence from durable state" is false for `CLAIM`. Needs a retry-stable idempotency key + reply cache.
- **F2** — Same-UID mode-based confinement (`0700`/`0000`) does **not** satisfy §5b. Probe: a same-UID process `chmod`s the `0000` quarantine back and reads the pre-settlement worker bytes. The "tightened by 0000" claim is affirmatively wrong; fix requires memory-only output custody or an author-acknowledged §5b re-scope.

**Ten Major** (each breaks two-implementer determinacy or a signed invariant): SIGSTOP exec→stop race (F3); pre-claim spawn orphan → "operator/boot" violates single automatic continuation (F4); SPAWN.lock not held-until-live → two supervisors (F5); watchdog "at or before deadline" unbounded under Git-archival/hashing (F6); takeover uses `waitpid` on reparented non-children — probe shows ECHILD and `Z`-zombie `kill(0)` still succeeds (F7); controller log path undefined before `process_id` exists (F8); request `arguments`/reply `detail` not byte-enumerated → `request_sha256` irreproducible (F9); peer role unenforced, controller can write CLI frames to `REQUEST.fifo` (F10); promotion path safety/atomic-rename unpinned (F11); promote-then-`SETTLEMENT.json` gives an ambiguous crash cut (F12).

**Confirmed correct:** the `/proc/stat` field-22 parse, **zero allowlist/frozen-file delta** (checked against `verification.py`), and the §S6 repair mapping.

**Opus Q1:** supervisor-death→§4c mapping is proved, but "at or before the deadline" is not guaranteed under long in-epoch work — route the miss to §4c(b) explicitly. **Opus Q2:** never-reissue and no-double-charge are sound; the one ambiguous cut (F12) must be made atomic.

Custody: no implementation, supervisor, endpoint, capability, spend, or outcome created; T remains `NOT_ACTIVATED` (`runtime/` holds only `T_RUNTIME.lock`); all probes ran in `/tmp`; nothing committed.
