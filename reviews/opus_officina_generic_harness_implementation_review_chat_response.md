Done. I wrote the single required file, `reviews/opus_officina_generic_harness_implementation_review.md`, and changed nothing else.

## Verdict

**`REVISE_OFFICINA_GENERIC_HARNESS_IMPLEMENTATION`** — with one narrow surface flagged `BLOCKED_CONTRACT`.

## What the adversarial trace established

I audited the signed composite (hashes recomputed and matched the signature), then traced actual production calls rather than trusting the 152 green tests — and reproduced the load-bearing failures live in disposable dirs:

- **C1–C4 all CONFIRMED as Critical.** The supervisor/watchdog/isolation boundary is absent (`SubprocessProcessOps` assigned at `:1089`, read nowhere; `run_isolated_operation` runs the callback in-process and returns the hash pre-settlement; `promote_after_settlement` binds nothing). The E1/E3 boundary isn't wired into `heartbeat`, which fabricates a fresh 60 s reservation at a boundary (`:1351`). Archival is skipped — `next_batch_action` returns `RESOLVED` with no `ARCHIVE`, so the registry stops blocking a whole boundary early. The §D1 head-lag repair is unreachable: I reproduced the ledger-ahead-of-head cut and showed both `entries()` and `append()` raise before any repair, and the method's docstring ("head can never lag") is false.
- **M1–M6 CONFIRMED** (M4 narrowed, M6 split). I reproduced M1 end-to-end: recovery → G1 → fresh start → **phase reverts to G5, next heartbeat refused** — the "since last admission" scope is missing. M5 reproduced: the real `python -m` entry point exits 2 (`_argv()` keeps `-m`).

## The three clarifications
1. Pre-review head is **forced** for `ledger_head_sha256` (a cycle otherwise); `ledger_entry_sha256` is under-pinned but the equal binding is the only acyclic reading — confirm + add an acyclicity regression test.
2. The extra `current_ledger_head_sha256` keyword is **faithful and required** by §3b prose — confirm, don't remove.
3. Archival needs **implementation only** — staged set (amendment §3a(2)/§D2c) and trailers (activation §B) are already signed.

## Dispositions
- **Cursor may repair immediately:** C2, C3, C4, M1–M6, and the *determined* bulk of C1.
- **Must wait for a bounded correction:** the persistent watchdog/supervision topology and the confined worker→supervisor result channel under §9's discrete-CLI/no-thread/no-signal constraints — route back as a contract question, don't design inline.
- **No file is eligible to commit** (harness has 4 Criticals; tests encode the facades; `accounting.py` is faithful but gated on X/Y and has no correct consumer yet).

Custody confirmed: no activation, spend, real process, manifest, capability, or outcome created; T remains `NOT_ACTIVATED`; `runtime/` holds only `T_RUNTIME.lock`; unrelated dirty/untracked files (including the concurrent `sol_*` reviews) untouched; nothing committed.
