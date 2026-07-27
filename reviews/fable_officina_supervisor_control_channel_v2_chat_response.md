Done. Exactly two new files; nothing else edited or started.

**Verdict:** `READY_FOR_OFFICINA_SUPERVISOR_V2_XY_REVIEW`

v2 is self-contained and embeds **A3 / B1 / C1 / D1** as normative prose. Deleted v1 over-claims: mode-bit secrecy, ephemeral retry, physical serial-loop deadlines, idle exit.

Notable pins:
- **A3** — mechanical roles/grammar vs accidental misuse; deliberate same-UID inspection is procedural residual; not Q/C-citable
- **B1** — durable journal for all eight commands; ADMIT retry without second worker/cursor; token redelivery until ack
- **C1** — dedicated freezer (never a writer); **no** physical non-RT guarantee; `overrun_ns > 0` → already-authorized invalid/recovery only
- **Output bytes** — per-operation `t-operation-output-bound.v1` before spawn (logical + allocated; sparse fail-closed); signed draft-manifest untouched; no universal GiB
- Mechanical ledger 1–15 + §S6 carried; zero allowlist/root delta

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not signable** until both fresh X/Y acceptances.

**Question:** Should the internal `--supervisor-serve` / `--watchdog-serve` tokens stay private double-fork argv (as drafted), or do you want them forbidden entirely so serve can only be entered via an in-process post-fork function call with no argv surface?
