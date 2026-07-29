I'll start by reading the governing artifacts in full.

Now I have the complete picture. Writing the correction.

Done. Two new files, nothing else touched.

**[successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md)** (1893 lines, `ee317172…`) — a replacement layer with a 68-row §Z0 index naming every superseded v2.1 clause/sentence/table row, then §Z1–§Z9 keyed one-to-one to R1–R9, plus §Z10 envelopes/schemas/authority table, §Z11 crash cuts, §Z12 disposition + test delta, §Z13 governance.

**[reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md)** — verdict line 1 `READY_FOR_OFFICINA_SUPERVISOR_V2_1_1_FINAL_XY_CONFIRMATION`, with the one-to-one disposition of X21-C1..C5, X21-M1..M8, all seven Opus Minors, Sol C1..C5/M1..M3, Sol's eight B1 traces, the authority table, ten worked counterexample traces, the A3/B1/C1/D1/K1 + signed-surface no-regression table, obligations without authorization, and the two bounded yes/no prompts.

Load-bearing repair decisions worth flagging:

- **R1** — allocation moved off the client entirely: `occurrence_mode ∈ {NEW, RETRY}` in the frame, and `NEW(i)` is a compare-and-swap against the tombstone's `next_occurrence_index` under `T_RUNTIME.lock`. That makes concurrent NEWs structurally distinct, makes client files freely deletable, and — because the reply envelope now carries `next_occurrence_index` — closes X21-C5's wedge without touching §W5.2's closed `REFUSED` detail set. Tombstone keys become two monotone integers; `last_effect_reply_sha256` is deleted, so post-GC classification needs no unavailable hash.
- **R3** — `spawn_intent_id` now hashes a placeholder-bearing argv **template**; `complete_argv_sha256` is separate. The grandchild is identified by a sealed bootstrap pipe plus an immediate `SPAWNING_CHILD.json`, never by `cmdline`, with three bounded timeouts and an identity-proved stuck-holder route so D1 can't wedge. A pinned thirteen-index adapter argv reintroduces exactly one refusal-first entry token (`--officina-bootstrap`) — required by Sol C3.4, and it explicitly replaces §W2.1's "no private argv entry surface" sentence.
- **R4** — beyond restoring the publication trigger, the watchdog must **drain its update pipe and re-read `LEASES.json` before freezing**. Without that, a legitimately renewed lease is still frozen at the superseded deadline (Opus's Q2 symmetric gap), and every freeze is invalidity by §W3.4's single route.
- **R7** — zero-frame `COMPLETED` is decided as a **canonical empty result** (`result_sha256 = SHA-256(b"[]")`), because routing it to failure would derive invalidity from an output property; capacity is unaffected since K1 now retains `bytes_reserved` regardless.
- **R8** — I did both options: a bounded pre-settlement re-hash through inode-verified descriptors (closing equal-size substitution mechanically) **and** an explicit naming of the residual it cannot close — same-name substitution of the `out/` directory between verification and `os.replace`, since the kernel has no rename-by-descriptor.

No author cell was reopened and no new author-choice token proved unavoidable, hence `READY` rather than `BLOCKED_…_AUTHOR_CELL`. Two new control refusal tokens (`OCCURRENCE_INDEX`, `SUPERSEDED_PLAN`), several control-plane constants, and the tightened argv bounds (32 elements / 768 bytes, printable ASCII) are the only enum/constant movement; the five signed K1 values and the import allowlist are untouched.
