§W3.3 requires `killpg` plus numeric pgid. Checking what the lease table carries and the watchdog's exact slot map under P1:

The blocker is provable four independent ways. Writing the packet:

Both files delivered. Closure line 1: `READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_XY_REVIEW`.

## Blocker: proved, and stronger than I reported last round

I treated the reporting author as untrusted and re-derived. The report gave two mechanisms; there are **four**, and the two strongest weren't among them:

1. **`S-12` of the selected composite itself** — "subprocess, Popen, fork, waitpid, kill, killpg and system appear on no path of `generic_harness.py`". The watchdog's role entry *is* in that file (`A-10` imports it as the only import; `A-13` calls one pinned entry from it). **The verifier of the selected architecture forbids the watchdog from freezing.** Dispositive on its own.
2. **The signed sole-caller sentence** — the PCS "is the sole caller of `fork`, `posix_spawn`, `kill`, `killpg` and every wait-family primitive". Dispositive on its own.
3. No endpoint — slot 6 explicitly closed, no runtime-root descriptor. *(as reported)*
4. No relay at the only moment it matters. *(as reported)*

**One corollary constrains the whole option space**, and it wasn't in my prior report: the PCS must never retain a write end on the watchdog update pipe. If it did, the pipe would never reach EOF on supervisor death — and that EOF is the **single remaining supervisor-death detector** under P1. This rules out the most obvious naive repair.

## The two options

Both are specified so **neither depends on the identity cell**: each routes the absent witness through §N5's already-signed `ABSENT` sentinel, so no numeric witness is needed anywhere.

**W-A** — watchdog requests, PCS executes. `SOCK_SEQPACKET` at reopened slot 6; the request carries **no target field of any kind** and one opcode from a one-element set, so a wholly compromised watchdog can request exactly "freeze the set the PCS already knows" — it cannot name, narrow, widen or redirect it. Amends "holds no capability".

**W-B** — PCS freezes on its own `PEER_EOF`. **Adds no descriptor, no opcode, no capability**; the §P1-6.4 leak proof stands byte-unchanged and the watchdog holds strictly less than before. The two EOFs are the same kernel event on two descriptors, so no ordering between them is needed and no race exists.

**Recommendation: W-B** on the three stated criteria. It amends zero P1 sentences and introduces **no new liveness dependency** — where W-A makes the freeze contingent on a live watchdog, i.e. on a process whose death is itself one of the conditions C1 exists to handle. W-B's honest costs: the PCS acts without a request for the first time in this architecture (named as new initiative, bounded by a kernel-fact trigger, pre-existing scope, once per generation), and the watchdog is demoted from freezer/witness to liveness sensor — a real C1 change carrying its own token.

I also rejected six route families with reasons, including terminate-instead-of-freeze, which deletes signed C1 rather than implementing it.

## Separation from the identity cell

All four combinations — (W-A or W-B) × (identity A or B) — are compatible with no interaction at any step, and the identity outcome doesn't change which watchdog option is better on any criterion. Neither choice is conditioned on the other.

Two things worth your attention in §9: the slot-6/EOF corollary is my reasoning, not any signed document's, and if it's wrong the option space is larger; and the `ABSENT`-route reuse is load-bearing in both options — I verified §N5 admits and routes a null rejected-witness path, but did not audit every consumer for an assumption that it's rare.

No choice accepted, no token accepted, none signable. v1.2 and the identity packet are byte-untouched; only the two new files exist. `T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.
