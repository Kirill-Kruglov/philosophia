Now the adversarial re-derivation. The most serious counter-route is `/proc` marker discovery — P1's role argv carries `--officina-spawn-intent <64hex>`:

§Z3.4 retains a `/proc/*/cmdline` discovery predicate for exec'ing children. Reading it and checking its fate under P1:

The watchdog's descriptor set under P1 raises a related question — checking how it freezes:

Confirmed the conflict independently, and found one thing my v1.2 diagnosis stated too strongly. Writing the packet:

Both files delivered. Closure line 1 is `READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_XY_REVIEW`.

## Re-derivation — confirmed, with one correction to my own prior round

I enumerated all nine opcodes' response operands: `handle_id` ×2, `outcome`/`start_identity`/`pgid_is_leader`, two `result` tokens, the six-token classifier, two empties, `pcs_uptime_ticks`. None is a pid or pgid. `pgid_is_leader` decides whether the two are equal while naming neither.

**v1.2 stated the conflict too strongly and I've corrected it.** The chain *does* contain §Z3.4, a `/proc/*/cmdline` discovery predicate for exec'ing children — a route by which a supervisor could get the pid without the PCS. It still isn't live, for two independent reasons: its fixed indices (`cmdline[3] == "--officina-bootstrap"`, marker at 6) don't match P1's argv layout (index 3 is `-E`, marker at 12/13), so it matches **zero** P1 roles; and v2.1.10 deleted argv-as-evidence outright. The correct claim is "no *authorized, non-stale* source exists" — same verdict, different argument, and the argument is what a reviewer checks. That §Z3.4 is stale against P1 is a separate peer-chain defect, recorded not repaired.

## The options

**A** — `AWAIT_STOP` gains `attested_pid`/`attested_pgid` at indices 11–12, on `STOPPED` only, both-or-neither, +16 bytes against a 4096 ceiling. Six ordered PCS proof conjuncts; `attested_pid` is the value the PCS's own `posix_spawn` returned, never read from `/proc`. `pgid_is_leader` retained as a free cross-field invariant. Sole sink: the two claim keys. Request grammar unchanged (`A-R1`–`A-R6`). Escape prevented by `S-25a`–`S-25d` including a taint analysis, plus `A-T5` fault injection. Replay returns recorded bytes and **must not** re-observe — re-running the proof after `REAPED` would violate `WAIT_ONE`'s precondition.

**B** — fully specified (`t-process-claim.v2` + PCS-written binding artifact), then **marked non-selectable**, because it can't be made single-valued without two further cells: does the PCS gain a peer-visible durable-write role, and may a peer validity predicate read a P1-owned artifact (inverting `R-L4`)? The "supervisor writes the binding" variant collapses into A, so it isn't an alternative.

**C** — re-indexing §Z3.4 was examined and **rejected**, not offered for symmetry: same numeric exposure, weaker proof, and it's the argv-as-evidence the chain deleted.

## The A3 answer

**No — observing a PID grants no process authority.** The supervisor is same-UID and already may read every pid from `/proc`; the tuple adds zero OS information, only provenance. P1 removed *authorized addressing*, which A doesn't touch. A contaminated supervisor can already `kill(any_pid)` — v1.2 §P1-12.3 says so affirmatively. **A weakens the English sentence, not the safety property.** The real cost is testability: a lexical invariant becomes a dataflow one. I named it as a bounded weakening with its own token rather than implying equivalence.

**Recommendation: A**, on the three permitted criteria only — it leaves all four signed schemas byte-untouched and reopens zero validity predicates, against B's three superseded schemas and one reopened acceptance predicate.

## One thing worth your attention beyond this round

While re-deriving, I found a second defect of the same root class, recorded at §6 and flagged as orthogonal: **under P1 the watchdog cannot execute a freeze.** The binding requires it to freeze all known groups on update-pipe EOF, but P1 gives all process authority to the PCS, the watchdog's slot map has slot 6 explicitly closed so it holds no PCS socket, and it acts precisely when the supervisor is dead — no relay exists. Neither option here fixes it. It needs its own cell (`AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM`), and I flagged it so it can't be silently absorbed into v1.3.

No choice made, no token accepted, no token signable. v1.1 and v1.2 byte-untouched; only the two new files exist. `T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.
