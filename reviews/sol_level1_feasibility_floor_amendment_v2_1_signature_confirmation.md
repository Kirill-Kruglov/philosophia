# Level 1 floor amendment v2.1 — Y-line signature confirmation

`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_1`

No. The requested replacement paragraph did not land exactly. The v2.1
paragraph additionally changes the report-installation protocol and adds Git
archival timing, driver archival scope, and pre-run Git-guard language. Those
sentences were not in the exact bounded replacement and move artifact-procedure
text beyond the sole §6 blocker.

Replace the entire v2.1 normative paragraph with exactly:

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

This confirmation created only this Markdown review. It created no code,
authorization, entropy, probe, trajectory, comparative datum, N3, lock, panel,
escrow, or outcome.
