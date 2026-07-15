# Level 1 feasibility-floor amendment v2 — final Y-line confirmation

`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_FINAL`

Closures 1–6 are confirmed. The v1 scope, learner-class conditional estimand,
temporal weighting, four-learner resource distinction, Level 0 limitation,
validity-first semantics, future ledger/ROADMAP text, pass/censor
interpretations, and prohibition on a v1/v2 effect all match the mandatory
Y-line repairs. Section 9 also makes the author token accept §3's new
learner-class conditional estimand, not merely a resource adjustment.

The sole remaining revision is procedural ambiguity in §6. A Git commit of the
generated claim before step 1 is not scientifically necessary under the signed
procedural threat model; durable atomic claim creation is sufficient. Replace:

> The durable v2 claim is written and committed **before any learner step**; the
> report is written **atomically after valid completion**.

with exactly:

> Before any learner step, the driver durably creates the canonical v2 claim by
> writing canonical JSON to a new same-directory temporary file, `fsync`ing the
> file, atomically installing it at the absent canonical claim path without
> replacement, and `fsync`ing the parent directory; no Git commit of the
> generated claim is required. The valid report is installed atomically only
> after valid completion. Any failure after durable claim installation and
> before valid report installation is
> `LEVEL1_FEASIBILITY_V2_INVALID:PROCESS` (or the more specific frozen
> invalidity cause), leaves `censored_at_b` unset, and authorizes no automatic
> rerun.

A final confirmation remains necessary, bounded solely to verifying that this
exact replacement landed and that nothing else changed. Until then, Kirill's
`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` token is not authorized. No new
scientific review is required.

This confirmation created only this Markdown review. It created no code,
authorization, entropy, probe, trajectory, comparative datum, N3, lock, panel,
escrow, or outcome; it inspected no series and compared no arms.
