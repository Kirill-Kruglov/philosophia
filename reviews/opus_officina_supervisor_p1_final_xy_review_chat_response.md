I'll begin by orienting myself in the repository and recomputing the required hashes.

Both hashes match exactly. Now let me map the full carried chain.

The chain is large. The 10.7 composite is the operative document. Let me read it in full, plus its closure.

The 10.7 layer is a bounded delta. The substance lives in the carried chain. Let me verify the governing hash block for integrity, then read the closure and the key carried layers (10.6, 10.5, 10.4 binding, P1 selection).

All 23 governing hashes match — the chain is byte-intact. Now the closure (second review target), then the carried layers.

Now the carried layers. Let me read 10.6, 10.5, and the P1 selection signature.

Now the foundational P1 binding (10.4) and the P1 selection signature.

Let me read the rest of the 10.4 binding.

I have the full composite now. Let me examine the actual verifier surface (`verification.py`) to ground claims about implementability of the prose rules S-23/S-26/S-27/S-28, and check how superseded text is handled.

The verifier is pure Python-AST over `PRODUCTION_ROOTS` (3 code files today; 5 under CHANGE 1). Yet the composite adds *prose* rules (S-23, S-26/27/28) quantifying over "operative sentence[s]... in the reviewed source **or contract**." Let me test whether the forbidden phrasings literally persist in committed files, and whether any layer materializes an "operative composite" or defines "operative" mechanically.

Finding confirmed. Critically, the P1 selection signature (line 50) *mandated* "The selected P1 architecture must be emitted as **one operative composite** before independent review" — yet the forbidden phrasings the new guards target literally persist in committed predecessor layers (10.4/10.5/10.6), and the only place "operative composite" is referenced as an existing object is a rhetorical question. Let me confirm no consolidated composite artifact exists and check the frozen implementation surface.

I have enough to complete the review. Key confirmations: the process-control core is byte-intact (23/23 governing hashes + both target hashes match), but the P1 selection's explicit precondition — "emit as **one operative composite** before independent review" — was never met, no consolidated artifact exists, and the new prose guards fire on superseded committed text. Let me write the review.

Let me verify I created exactly one file and modified nothing else in the tracked tree.

Review complete. I created exactly one new file and touched nothing else; the pre-existing dirty set (11 tracked modifications, all from before this session) is unchanged, and both review-target bytes still hash to their expected values.

## Verdict

**`REVISE_OFFICINA_SUPERVISOR_P1_COMPOSITE`**

Written to [reviews/opus_officina_supervisor_p1_final_xy_review.md](reviews/opus_officina_supervisor_p1_final_xy_review.md).

## What I did

- **Recomputed both target hashes** — match exactly (`66dc6fdc…`, `02d13b9d…`), plus **all 23 governing hashes** in the 10.7 block, plus the predecessor blocks. The carried chain is byte-intact.
- **Read the whole operative chain**: 10.7, its closure, 10.6, 10.4 P1 binding (both pages), the P1 process-authority signature, and the pinned `verification.py`, tracing the traces the prompt named — caller→PCS→`pid_mid`→supervisor, the `DUP2`/`CLOEXEC` leak proof, the `SCM_RIGHTS`/`scm_detach_fds()` path, subreaper adoption + `AWAIT_STOP` non-interception, PID reuse, the watchdog no-signal route, `SPAWN.lock` survival, and `S-18'`.

## Why REVISE (no Critical, one Major)

The **process-control core is sound and single-valued** — I could not construct a wrong-PID action, false death proof, fd escape, two-owner handle, replay-becomes-valid, watchdog signal, or `SPAWN.lock` leak. The three 10.7 withdrawals are correct on their own terms, and F1–F5 are preserved.

But the **verifier/contract surface is not mechanically single-valued** (Major):

- The P1 signature *mandated* "emit as **one operative composite** before independent review." That was never done — the contract is fragmented across 10.4/10.5/10.6/10.7 + the carried chain, superseded only by prose replacement-index tables. No consolidated artifact exists.
- The new prose guards `S-23`/`S-26`/`S-27`/`S-28` (10.7's *only* new mechanical deliverable) quantify over "operative sentences of the contract," but "operative" is not computable from the committed bytes, and applied to those bytes the guards **fire on the correct composite** — I confirmed the forbidden phrasings ("the PCS only", "closed, small set…", "forge or block a death proof", "gain Officina process authority", bare "re-parented to init") literally persist in committed 10.4/10.5/10.6.

Repair is a **specification-author** action (materialize the composite; re-scope the rules to a named artifact) — hence `REVISE`, not `BLOCKED`. Two Minor findings (S-25's "direct PCS child" clause isn't statically decidable; 10.7's hash block isn't self-sufficient) are noted but not verdict-driving.

No implementation, activation, or claim movement is authorized. T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.
