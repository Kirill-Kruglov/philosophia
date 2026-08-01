I'll start by orienting myself in the repository and locating the normative files for this review.

First, let me verify the hash of the correction file and get oriented.

Hash matches exactly. Now let me locate the v2.1.6 reviews and read the v2.1.7 correction.

The five inherited findings are Sol's C1/M1/M2 and the X-line's X216-M1/X216-m1. Let me read both v2.1.6 REVISE reviews.

Now the X-line v2.1.6 review with findings X216-M1/X216-m1.

I now have the five inherited findings clearly. Let me diff v2.1.6 → v2.1.7 to see exactly what changed.

Let me read the full v2.1.7 correction to examine the actual repair sections.

Now the closing sections and the header of the file.

Now the header/hash-base region (lines 60–139).

I've now read the full v2.1.7 correction. Let me verify the cited governing hashes and the base commit ancestry.

All cited governing hashes verified byte-identical, and 063d290 is confirmed an ancestor of HEAD. Now the substantive work. The sharpest attack the prompt directs (attack 4) is the `ECHILD ⇒ PROVED_DEAD` premise, which rests on default SIGCHLD disposition. Let me verify independently whether that disposition is mechanically pinned, and reproduce the bound-language sweep (attack 7).

Important — the v2 draft mentions installing signal dispositions. Let me examine that and the import allowlist precisely.

Decisive evidence: `signal` is explicitly **outside** the import allowlist (`os`, `fcntl`, `subprocess`, `time`), so the CLI can neither query nor reset SIGCHLD. Let me confirm nothing resets/pins the disposition before fork, and reproduce the bound-language sweep (attack 7) independently.

My independent sweep finds exactly the same stale total-CLI-bound loci the author enumerated (v2.1.2 §N3.5/§N11/row86, v2.1.3 §U2.4/§U2.7), all routed to replacement; v2.1.1:613 ("no unbounded waitpid inside a T_RUNTIME.lock epoch") is a true specific statement, not a total-bound claim. Let me widen the sweep with a few more terms to be certain nothing operative was missed, and confirm the C1/M2 mechanics.

Bound sweep is clean — the ten-locus enumeration is complete and X216-M1 is genuinely closed by total text. Now let me confirm runtime/programme state and that nothing has been altered, before writing the deliverable.

All confirmed: hash matches, base is an ancestor of HEAD, runtime unactivated, tree clean. My verification is complete. Let me record the primary finding as a background chip and write the deliverable.

The five inherited findings (Sol C1/M1/M2, X216-M1/X216-m1) are all genuinely closed. But **attack 4** surfaces a new **Major**: the `ECHILD ⇒ PROVED_DEAD` machinery and its PID-reuse safety rest on "no auto-reaping," inferred only from "this contract installs no signal disposition" — which ignores that `SIGCHLD == SIG_IGN` is **inherited across `execve`** on Linux, and cannot be reset or even queried because `signal` is outside the import allowlist. The premise is not mechanically pinned before fork. Verdict: **REVISE**.

Review complete. Deliverable written to [opus_officina_supervisor_control_channel_v2_1_7_final_confirmation.md](reviews/opus_officina_supervisor_control_channel_v2_1_7_final_confirmation.md).

## Verdict: `REVISE_OFFICINA_SUPERVISOR_V2_1_7`

**Hash/base.** Target digest recomputed = `789732…6871a8` — **matches exactly**. Base `063d290` verified an ancestor of HEAD `e965681`. All governing hashes (both v2.1.6 reviews, inherited harness/batch corrections, signatures) reproduce byte-for-byte.

**All five inherited findings are genuinely closed:**
- **Sol C1** (object-bound TOCTOU) — closed: `OBSERVE` binds enumeration+lstat+O_NOFOLLOW-open+fstat(dev,ino)+pread-through-pinned-fd+hash; two barriers re-observe and require same identity/bytes/paired-absence **and same rule**; residual honestly signed as A3, not "impossible."
- **Sol M2** (SPAWNING-only wedge) — closed: the CLI always removes its own `SPAWNING.json` (it names only the CLI); two-supervisor safety holds via the `m5`-EOF argument.
- **X216-M1** (CLI-total-bound) — closed: I independently reproduced the whole-chain bound sweep; the ten enumerated stale loci are complete, no additional operative total-CLI-bound survives.
- **Sol M1 / X216-m1** (stage-M totality) — closed for the enumerated syscall enums.

**Why REVISE — new Major X217-M1 (attack 4).** The `ECHILD ⇒ PROVED_DEAD` rule *and* its PID-reuse safety ("a terminated child is a zombie whose pid cannot be reassigned") both rest on "children are never auto-reaped," pinned only by "this contract installs no signal disposition." That's a non-sequitur: on Linux `SIGCHLD == SIG_IGN` is **inherited across `execve`** (CPython doesn't reset it), and the contract can neither reset nor query it because `signal` is outside the import allowlist. The premise is **not mechanically pinned before fork**. Under an inherited `SIG_IGN`, a dead child is auto-reaped instantly (no zombie), its pid can be reused before `PROVED_DEAD`, and `SIGNAL_ATTEMPT` can `SIGKILL` an unrelated same-UID process — the "untracked live process" harm the required question forbids. Smallest safety-preserving repair (reset `SIGCHLD` to `SIG_DFL` before the first fork) **touches the signed import allowlist**, so the author's "zero import delta" claim cannot survive it. Plus a subordinate Minor (X217-m1: an unmapped `IDENTITY_SAFE` case).

**Authorization boundary.** Token `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **unavailable/not-signable**. No implementation, activation, entropy, spend, Q/C, or science authorized. Custody clean: no process ran, only this one review file created, target bytes intact. **T `NOT_ACTIVATED`; programme claim `OPEN`.**
