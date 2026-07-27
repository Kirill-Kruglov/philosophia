Done. Exactly two new files; v1 and the uncommitted implementation were not touched.

**Verdict:** `READY_FOR_OFFICINA_SUPERVISOR_AUTHOR_SELECTION`

**Recommended quadruple:** A3 + B1 + C1 + D1

| Choice | Recommendation | Why |
|---|---|---|
| A confinement | **A3** procedural same-UID re-scope | A1 can preflight byte secrecy (`memfd`/`O_TMPFILE` + `ptrace_scope≥1`, no allowlist delta) but this host has no `hidepid`, so Sol C2 metadata channels stay open — recommending A1 would violate the mandate. A2 is the literal-§5b pick if you want a separate supervisor credential/service. |
| B idempotency | **B1** durable journal, all eight commands, redeliver until ack | Fixes double-effect/lost-reply; keeps one-use token *effect* without forcing recovery on every lost STATUS. |
| C watchdog | **C1** dedicated freezer (not a writer) | Only way to keep multi-lease concurrency and still stop behavior at/before deadline during archival. |
| D lifetime | **D1** no idle exit | Smaller state space; no resource reason for D2's drain surface. |

Platform audit (read-only): `ptrace_scope=1`, no `hidepid`, `memfd_create`/`O_TMPFILE`/`pipe2` under allowed `os`, `PC_PIPE_BUF=4096`, `pidfd_getfd` absent. Mechanical F3–F15/Sol repairs are listed as non-choices; a hard output-byte cap is flagged as needing a separate token if you want one (not invented here).

Response template is in the packet — one token per line. No existing amendment token is signable until you select, v2 is drafted, and X/Y re-confirm.

**Question:** Do you want mechanical secrecy against a deliberate same-UID controller (A2), or is A3's honest §5a-aligned residual acceptable for T-dev?
