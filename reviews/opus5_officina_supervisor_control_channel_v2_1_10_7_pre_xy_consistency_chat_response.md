All four loci confirmed at exact lines. Writing the correction.

Custody verified: exactly two new files; v2.1.10.6, its closure, the P1 signature, and `verification.py` unchanged at their pinned digests.

## Done — the consistency defect is closed

| Deliverable | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md) | `66dc6fdc…d51a` |
| [opus5_officina_supervisor_control_channel_v2_1_10_7_pre_xy_consistency_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_10_7_pre_xy_consistency_closure.md) | `02d13b9d…32a9` |

Closure line 1: `READY_FOR_OFFICINA_SUPERVISOR_P1_FINAL_XY_REVIEW`. No topology change, no new syscall/import/process, no new author choice — so no `BLOCKED` was owed.

**The table is now temporal.** A wait-set isn't a static property: it grows whenever a descendant is orphaned and that process is the nearest living subreaper. The caller's "the PCS only" becomes "the PCS **plus** every process it has adopted", with an arbitrary higher ancestor `A*` as its own row. Wildcard waits are stated affirmatively as ranging over adopted children. `AWAIT_STOP` non-interception is proved in both halves — target is a non-orphan while custody is live; no decision is taken once it isn't.

**Three withdrawals to earned strength.** The closed status set is false and gone — a status is an untrusted OS fact that may reflect A3 interference; the surviving half is re-grounded on "no route reads it", not on the set being small. "Forge or block" splits: **no false-positive** proof survives; **indefinite denial** of proof and channel EOF via `SIGSTOP` is admitted, and each lands in a *carried* fail-closed route. "Cannot gain process authority" becomes an authorization statement — kernel parent/reaper power admitted, no descriptor/handle/opcode/journal authority conferred, no interference accepted as a decision.

One precision the brief didn't ask for but the analysis produced: **adoption adds exactly two powers** — reaper status and `getppid()` visibility. Signalling was already available to any same-UID actor under A3, so adoption grants no new interference; and `getppid()` confers nothing because no Officina route reads it.

§P1T.5 draws the boundary explicitly: S1–S4 guaranteed, **L1–L5 explicitly not** — including that no generation is guaranteed to complete and that a stall may never terminate. That makes the composite honestly weaker, and I've put the consequence to Y directly: if a control plane with no liveness guarantee under its own threat model is unacceptable, that's a **new author cell**, not a defect in these bytes.

Four consecutive layers have each found defects in the previous one, all mine — the reason `S-26`/`S-27`/`S-28` are wording guards against exactly the phrasings that went wrong, and the reason this closure asks to be weighted low. No acceptance token from this round. T `NOT_ACTIVATED`; claim `OPEN`.
