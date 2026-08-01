READY_FOR_OFFICINA_SUPERVISOR_V2_1_8_FINAL_XY_CONFIRMATION

# Author closure — Officina supervisor/control-channel v2.1.8 bounded repair

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only.**

**This closure is an untrusted self-assessment.** It is not an X-line review, not
a Y-line review, and not evidence of anything. The same author line wrote v2.1
through v2.1.8. `reviews/officina_supervisor_v2_1_authorship_note.md` records
that this line cannot serve as an independent reviewer of its own bytes, and
nothing here may be counted toward the two independent confirmations the
amendment requires. Every claim below is a claim to be *checked*, not a finding.

## Base, bytes, and method

Repository base: commit `d28ae12d8d616c8e9825683dd53ddb137f05b4a3`, verified to
descend from the required `2b25d690acbd122fc94cb58f617bb27e56308e78`
(`git merge-base --is-ancestor`). The working tree was already dirty at handover;
every pre-existing tracked modification and untracked path was preserved
untouched.

Pinned inputs, recomputed and matching exactly:

```text
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
2e4bee2305bafb5825a6ac1cca4d131dcbdf730aa048f29c7023cf679c9936e6  reviews/opus_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
5c82f7c1894d3e76239ee26a611731d102a2891486a9c2d667ce9738956d533b  reviews/sol_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
```

Digest of the artifact this closure accompanies:

```text
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
```

Method: static authoring only. Read-only file and `git` inspection, literal
searches, `sha256sum`, and reasoning over documented bytes and Linux/CPython
process semantics. **No repository code, test, probe, smoke command, or Officina
process ran. No implementation was written. No runtime, capacity, custody, or
scientific artifact was created or changed. No existing file was modified.**

## Verdict and what it does not mean

`READY_FOR_OFFICINA_SUPERVISOR_V2_1_8_FINAL_XY_CONFIRMATION` states only that
the two deliverables exist, that all five governing findings received a
one-to-one repair, that no scientific author cell was reached, and that no
contract conflict was found with the signed harness or batch-settlement
composites. It is **not** a confirmation, and it makes nothing signable.

Neither blocked token applies:

- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_8_AUTHOR_CELL` — **not applicable.** No new
  author-choice token was reached. The repairs are mechanical process-identity,
  reaper, terminal-totality, and causal-proof corrections under the already
  selected A3/B1/C1/D1/K1 policies. Both independent v2.1.7 reviews reached that
  conclusion separately, and this author found nothing that forced a new cell.
  The `signal` allowlist change is an **engineering** artifact, not a scientific
  choice; it is named loudly and submitted for review rather than assumed.
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_8_CONTRACT_CONFLICT` — **not applicable.**
  The one place the delta could have conflicted is §9 of the signed
  `OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md`, which states that the harness
  "uses no `signal`/`threading`/`multiprocessing`/backend import" and that any
  change "requires a reviewed amendment to that allowlist". Both remain true and
  are honoured: the harness still imports no `signal` (§V218.1.2 forbids it in
  every module but the CLI bootstrap), and this layer **is** the reviewed
  amendment that sentence anticipates. Reviewers should test this reading
  adversarially; if either line disagrees, the correct outcome is `REVISE`, not
  a silent reinterpretation.

## The engineering delta, stated as loudly here as in the correction

> **`ALLOWED_ABSOLUTE_IMPORTS` gains exactly one member: `signal`.**
> Every prior layer of this chain claimed a **zero import-allowlist delta**.
> **That claim is superseded and does not survive into v2.1.8.**

- Today's literal set in `src/philosophia/officina/verification.py`
  (digest `327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e`) has
  sixteen members; the future amendment adds the single string `"signal"`, giving
  seventeen. Nothing else in that file changes, and **this correction does not
  edit it.**
- Permitted surface, statically testable (§V218.1.2): importer = the CLI
  bootstrap module only; members = `signal.SIGCHLD`, `signal.SIG_DFL`,
  `signal.signal`, `signal.getsignal`, and no others; call sites = the two
  functions of step `c3n` and nowhere else. Explicitly forbidden: any handler
  callable, `SIG_IGN`, `pthread_sigmask`, `set_wakeup_fd`, `siginterrupt`,
  `alarm`, `setitimer`, `pidfd_send_signal`, every other member, and every other
  importer.
- Fourteen superseded "zero delta" / "`signal` is outside the allowlist" loci are
  enumerated one by one in §V218.1.4, including the v1-draft §S5 §S7-probe claim,
  §W2.6's parenthetical, §W6.4's parenthetical, and v2.1.7's own two statements.
- Two carried properties keep their substance and lose only their old
  justification: §W2.6 (the controller adapter installs no signal disposition) is
  now a directly asserted, statically tested restriction; §W6.4 (no
  `PR_SET_CHILD_SUBREAPER`) still holds because `prctl(2)` needs `ctypes`, which
  stays outside.
- The integer signal literals `9`/`15`/`18`/`19` and the liveness probe `0` are
  unchanged everywhere. The only symbolic use is `signal.SIGCHLD`, chosen
  because `SIGCHLD`'s number is not uniform across Linux architectures.

## Exact v2.1.7 → v2.1.8 replacement index (summary; §V218.0 is normative)

Everything not listed carries forward verbatim — **including §V217.1 in full**
(object-bound observation, `OBSERVE` O1–O9, both revalidation barriers, the A3
residual, the mutation-cut table) and **§V217.4 in full** (the ten-locus
bound-language replacement, the eighteen declared search terms, the
retained-statement table, revised row 86, D1's true ground).

| # | v2.1.7 / carried locus | Action |
|---|---|---|
| 1 | v2.1.7 Engineering-Constants "Zero import-allowlist delta" and its "`signal` … remain outside" clause | replaced by §V218.1 |
| 2 | v2.1.7 §V217.7 "The import-allowlist delta remains **none**." | replaced by §V218.1.1 |
| 3 | the same zero-delta wording carried in v2.1.6, v2.1.5, v2.1.4, v2.1.3, v2.1.2, v2.1.1, v2.1, and the v1 draft §S5/§S0 | replaced by §V218.1.1 / §V218.1.3, enumerated in §V218.1.4 |
| 4 | v2.1 §W2.6 and §W6.4 parentheticals justifying properties by `signal`'s exclusion | replaced by §V218.1.2 (claims retained, justification replaced) |
| 5 | §U2.2's step list `c1`–`c8` | **extended** by step `c3n` (§V218.2.1) |
| 6 | §U2.5 / §U6.1 wait sites | **extended** by the sole-reaper contract and the closed five-site wait table (§V218.2.6); no route's behaviour changes |
| 7 | §V217.2.2's `IDENTITY_SAFE` block | replaced by §V218.3.4's total ten-row table |
| 8 | §V217.2.3's `ESRCH ⇒ GONE` clause | replaced by §V218.3.5 (`ESRCH` under an owned unreaped child is a premise contradiction) |
| 9 | §V217.2.3's SIGTERM→SIGKILL schedule | replaced by §V218.3.6 (ownership-gated; `D/2`, `D`, and the `≥` edge rule preserved verbatim) |
| 10 | §V217.2.4's `ECHILD ⇒ PROVED_DEAD` line | replaced by §V218.3.3 (`INCONCLUSIVE_ECHILD`) |
| 11 | §V217.2.4's "Why these two outcomes prove death" bullets | replaced by §V218.3.3; the false universal "children are never auto-reaped" and its non-sequitur premise are **deleted** |
| 12 | §V217.2.4's "PID reuse" paragraph | replaced by §V218.3.2's fork-ownership proof |
| 13 | §V217.2.5's `c5`/`c6`/`c7` mapping | replaced by §V218.3.7 |
| 14 | §V217.3.1's "Two-supervisor safety, proved" (`m5`/`rel2`) paragraph | replaced by §V218.5.1 (`m0`/`rel1`/fork-shared lock) |
| 15 | §V217.3.1's "the abandoning CLI … on every route" sentence | replaced by §V218.4.3 (scoped to **returning** terminals) |
| 16 | §V217.3.2's `T1`/`T2`/`T3` block | replaced by §V218.4.2; **`T3` deleted**, including its "install NOTHING … remove ONLY `SPAWNING.json` … return" body and its "or `DENIED` signals" membership |
| 17 | §V217.3.3's forward-progress table | replaced by §V218.4.4 plus the §U6.1/§U2.5 totality proof |
| 18 | §V217.3.4's residual paragraph | replaced by §V218.4.5's three named residuals |
| 19 | §V217.3.5 and §V217.5 rows for `ECHILD`, `ESRCH`, `EPERM`, unreadable/unparsable `/proc`, PID reuse, and every `T3` row | replaced by §V218.6 |
| 20 | §V217.6 test rows 198, 199, 200, 203, 205, 207, 208 | replaced; rows 213–240 added (§V218.7) |
| 21 | §V217.7's determinacy and compatibility paragraphs | replaced by §V218.9 |

## One-to-one disposition of all five governing findings

| Finding | Repair | Where |
|---|---|---|
| **Sol C217-1 (Critical)** — inherited `SIGCHLD`/reaper state defeats the death and PID-reuse premise | Step `c3n` executes `signal.signal(signal.SIGCHLD, signal.SIG_DFL)` before the first `os.fork` of **every** attempt, in the main thread, under the held lock. One `sigaction` replaces the whole disposition record, clearing an inherited `SIG_IGN` **and** an inherited `SA_NOCLDWAIT` regardless of whether the CLI was exec'd or forked into. Verification reads the kernel's own `SigIgn`/`SigCgt` masks from `/proc/self/status`. No fork occurs unless the result is `NORMALIZED`. A sole-reaper contract forbids wildcard waits, `subprocess` objects, threads, and handlers in the CLI, and enumerates the five permitted wait sites. `ECHILD` maps to `INCONCLUSIVE`, never `PROVED_DEAD`. | §V218.2, §V218.3.3 |
| **Opus X217-M1 (Major)** — the `ECHILD`/no-auto-reap premise is not mechanically pinned before fork | Same repair; additionally the allowlist delta is named loudly instead of being denied, and the PID reservation is re-derived as a proof from the *performed* normalization (§V218.3.2) rather than asserted from an assumed default. Three independent detectors — `ECHILD`, `ESRCH` on an owned unreaped child, and a `ppid` mismatch — irreversibly forbid every further signal if the premise fails anyway. | §V218.1, §V218.2, §V218.3.1–§V218.3.3 |
| **Opus X217-m1 (Minor)** — `IDENTITY_SAFE` omits `PRESENT_VALID ∧ uncaptured ∧ ppid ≠ getpid()` | `IDENTITY_SAFE` is rebuilt as a total ten-row decision table over stat result × capture state × `ppid` comparison × ownership. The missing case is row **I-4** and is resolved in the safe direction: no signal, no capture, no durable record, contradiction set — it becomes the last line of defence against a failed normalization rather than a gap. | §V218.3.4 |
| **Sol M217-1 (Major)** — `T3` abandons a live untracked middle and has contradictory terminal membership | `T3` is **deleted**. Stage M becomes `T1` (authoritative reap only), `T2` (truthful durable handoff), and `B` (an explicit non-returning blocked reaper). The three predicates are pairwise disjoint and exhaustive. Because ownership — not `/proc` — authorizes the signal, a stopped child is SIGKILLed and reaped even with `/proc` entirely unreadable. No route returns, releases the lock, removes `SPAWNING.json`, or discards every handle while the child may be live and unreaped. The "or `DENIED` signals" clause is gone. | §V218.4 |
| **Sol m217-1 (Minor)** — the written second-supervisor proof names the wrong gate | Replaced by the actual `c5`–`c7` trace: no `c8` byte was ever written; the middle is at `m0`; it owns its own `rel1_w`, so EOF at `m0` is impossible; `m1`/`m2`/`m4`/`m5`/`m7` are unreachable, so no grandchild is forked and no `SUPERVISOR_IDENTITY.json` is installed; the fork-shared `SPAWN.lock` reference is what serializes the next CLI. `m5`/`rel2` is retained **only** for cuts at or after `c8`. | §V218.5 |

## Proof obligation 3 — the complete `waitpid` table

| `os.waitpid(pid_mid, WNOHANG)` | Result | Ownership | Continuation |
|---|---|---|---|
| returns `(pid_mid, status)` | `PROVED_DEAD` | → `REAPED` | the **only** entry to `T1`; the route never touches the pid again |
| returns `(0, 0)` | `NOT_YET` | unchanged | continue polling; a stopped child appears here and is SIGKILLed |
| `ECHILD` | `INCONCLUSIVE_ECHILD` | → **`CONTRADICTED`** | leave the deadline loop; **never** `PROVED_DEAD`, **never** `T1`; `T2` if an identity was captured, else `B-CONTRADICTED` |
| `EINTR` | bounded retry at `T_SUPERVISOR_POLL_INTERVAL_NS` within the existing signed deadline; on expiry `INCONCLUSIVE_OTHER` | unchanged | continue |
| any other `OSError` | `INCONCLUSIVE_OTHER` | unchanged | continue polling to `t0 + D`, then terminal selection |
| evaluated after `REAPED` | contract violation, not a route | — | — |
| `WIFSTOPPED` report | impossible: `WNOHANG` without `WUNTRACED` never reports a stop | — | — |

Every prose row, table cell, and test row asserting `ECHILD ⇒ PROVED_DEAD`, or a
zombie pin without §V218.3.2's mechanically established scope, is deleted:
§V217.2.4's bullet and PID-reuse paragraph, §V217.3.5's and §V217.5's `ECHILD`
rows, and test rows 198/199/200.

**Fork-ownership / PID-reuse proof (§V218.3.2), in one paragraph.** A pid is
reassignable only when no task holds it. `c4`'s child holds `pid_mid` from the
instant `fork` returns. On termination the kernel auto-reaps only if the
parent's `SIGCHLD` action is `SIG_IGN` or carries `SA_NOCLDWAIT`; `c3n`, executed
**before** the fork, made it `SIG_DFL` with neither, and verified the
`SIG_IGN`/handler half against the kernel's own bitmasks. The task therefore
becomes and stays `EXIT_ZOMBIE`, still holding the pid, until a targeted
`os.waitpid(pid_mid, …)` from one of the five enumerated sites returns it — at
which instant `OWNERSHIP := REAPED` forbids every further use. The
capture-to-signal window is thus closed by a property established before the
child existed, not by a `/proc` read.

## Proof obligation 4 — the total `IDENTITY_SAFE` table

Ten rows over stat result × capture state × `ppid` × ownership; every cell is
pinned in §V218.3.4. In summary: `PRESENT_VALID` with a matching capture and
`PRESENT_VALID` with `ppid == getpid()` confirm identity (the latter captures);
`PRESENT_VALID` with a mismatching capture and `PRESENT_VALID` with
`ppid ≠ getpid()` are **premise contradictions** that forbid every further
signal, the second also forbidding capture; `ABSENT` is never death;
`UNREADABLE`/`UNPARSABLE`/`ERROR` withhold the durable identity but no longer
block termination, because ownership carries the kill; and the `REAPED` and
`CONTRADICTED` entry states are explicit rows rather than omissions.

**`os.kill(pid_mid, …)` executes if and only if `OWNERSHIP == OWNED`** — one
statically checkable precondition that discharges "no branch may signal a PID
after authoritative reap or under an inconclusive ownership premise" without
per-branch reasoning.

## Proof obligation 5 — the terminal automaton

```text
M5 terminal selection (pairwise disjoint, exhaustive):
   OWNERSHIP == REAPED                     ⇒ T1   (returns)
   OWNERSHIP != REAPED ∧ captured != ⊥     ⇒ T2   (returns)
   OWNERSHIP != REAPED ∧ captured == ⊥     ⇒ B    (DOES NOT RETURN)
```

- **`T1`** — entered only on `waitpid == pid_mid`. Ordered removal of all four
  records in the §U6.3 order under the held lock, then release, then a retryable
  refusal.
- **`T2`** — entered when the child was not reaped but a start identity was
  captured while ownership held, so every `SPAWNING_MIDDLE.json` field is an
  observed value. Installs that already-signed record, removes only
  `SPAWNING.json`, retains `pid_mid` in memory for wait site W-4, releases the
  lock, returns retryably. §V218.4.4 proves the **existing** §U6.1
  P0/P1/P2a/P2b/P3 and §U2.5 `s4`/`s5` resolver total for it, with no new tier,
  record, schema, or operator step, and states two honest limits (a resolver
  that also cannot read `/proc` refuses retryably rather than acting; `s4`
  proves death by `/proc` absence or state `Z`, which the new zombie satisfies
  precisely).
- **`B`** — no truthful record is constructible, so nothing is installed and
  nothing is returned. It **retains** `SPAWN.lock`, `SPAWNING.json`, the
  in-process `pid_mid` handle, and its bootstrap ends, and loops on
  `WAIT_PROVE` + ownership-gated `SIGKILL` + re-observation. Its only exits are
  `PROVED_DEAD` ⇒ `T1` and a valid capture ⇒ `T2`. It introduces no object, no
  constant, no deadline, no blocking syscall, and no operator step, and it
  reintroduces no bound-language contradiction, because §V217.4.3 already
  withdrew every fixed-total-CLI claim.
- **Stopped child and long-lived CLI.** Ownership authorizes `SIGKILL` with no
  `/proc` read, so a stopped middle is killed and reaped even under a total
  `/proc` fault. Every returning terminal removes the CLI's own `SPAWNING.json`,
  so no live returned CLI can trigger a later P2b. Crash/restart traces for
  `T1`, `T2`, and `B` are tabulated in §V218.6.
- **No handle is discarded while the child may act** — the invariant is stated
  as §V218.4.1 and each terminal is checked against it individually.

**Three residuals, named rather than concealed** (§V218.4.5): the **new**
unreaped-zombie residual this repair itself creates (one zombie per `T2`, no
descriptors, no lock reference, resolved by W-4 or CLI exit, and positively
useful as a state-`Z` death proof for other processes); `B-OWNED`
non-termination, which requires a deliberately stopped child **and** a
persistent signal fault, since a normally executing middle exits at its own `m0`
bound and is reaped; and `B-CONTRADICTED` non-termination under a violated
sole-reaper contract, which holds the singleton, emits nothing citable, and is
explicitly process control rather than scientific or resource evidence.

## Proof obligation 6 — the corrected causal trace

At `c5`, `c6`, or `c7`: no `c8` release byte exists on `rel1` (the pipe is fresh
from `c3` and `c8` never executed); the middle is at `m0`, its literal first
instruction; it still owns its inherited `rel1_w`, so EOF at `m0` is impossible
in principle; its exit is controlled by its own `m0` bound or by the parent's
ownership-authorized `SIGTERM`/`SIGKILL` and reap; it can never reach `m1`,
hence never `m2`, `m4`, `m5`, or `m7`, so **no grandchild is forked and no
`SUPERVISOR_IDENTITY.json` is installed**; and the fork-shared `SPAWN.lock`
reference — not any `rel2` event — is what prevents a new CLI from acquiring
until the middle exits. The five schedules (stopped/resumed, queued byte,
writer copy, timeout, immediate new CLI) are re-run in §V218.5.2. **No stage-M
sentence, table, test, or claim in the correction or in this closure cites
`m5`, `rel2`, or a `rel2` EOF**; §V218.5.3 lists the cuts at or after `c8` where
that argument remains correct and is retained.

## Proof obligation 7 — no regression

§V217.1 (object-bound observation, `OBSERVE`, both barriers, the A3 residual,
the mutation-cut table) and §V217.4 (the complete bound-language replacement,
the search terms, the retained-statement table, revised row 86, D1's ground) are
carried **byte-for-byte**; both were confirmed closed by both v2.1.7 reviewers.
Also carried unchanged: `CLOSE_OWNED` at every site including both lock closes;
`MALFORMED` physical-presence dominance and the rule ordering; the cross-product
and sub-routing; the three branch bodies; §N2.3's P1–P7 custody proof and
§V214.2.4's reconciliation; K1's constants and one-release accounting;
death-before-unlink for the three records naming other processes; §V216.5's
eight-end audit; §V216.4.1's narrowed pipe-only invariant; bootstrap, forks,
gates, GC, the watchdog partition, and the singleton preflight; A3/B1/C1/D1/K1;
the generic-harness v2→v2.3.1 and batch-settlement v1→v1.1.1 composites; the
nine signed events; E1/E2/E3; the Q/C boundary; and T's inactivity. **The reaper
repair is nowhere presented as a proof of filesystem exclusion**: `T_RUNTIME.lock`
still serializes contract actors only, the A3 same-UID procedural residual is
untouched, and no security boundary is invented.

## Proof obligation 8 — future implementation and tests, none performed

Rows 198, 199, 200, 203, 205, 207, 208 are replaced and rows **213–240** are
added (§V218.7), including the two fixtures the finding demanded: an **inherited
`SIG_IGN`** fixture (parent sets `SIG_IGN`, then `execve`s the CLI) and an
**inherited `SA_NOCLDWAIT`** fixture (parent installs the flag and **forks
without exec** into the CLI entry, so both the disposition and the flags are
inherited — the fixture may use `ctypes`, which the runtime allowlist forbids
but which does not govern test fixtures). Also added: a negative control with
normalization disabled; allowlist-containment and `signal`-surface assertions;
§W2.6 and §W6.4 survival tests; totality tests for both new functions; the
no-fork-on-failure test; the single-kill-precondition and sole-reaper static
assertions; the wait-site enumeration; the per-attempt reset; the total
`IDENTITY_SAFE` product; the PID-reuse window at every instruction boundary;
`/proc`-fully-unreadable live and stopped children; the `B`-state properties and
both of its non-termination cases; `T2` truthfulness and resolver totality; the
zombie residual; long-lived-CLI crash/restart traces; the corrected causal trace
and its five schedules; and a whole-chain no-regression diff.

**No implementation exists and none is authorized.** No code, test, or fixture
was written. The one-string amendment to
`src/philosophia/officina/verification.py` is *specified*, not applied; that
file is unmodified and its digest is recorded in the correction's hash block.

## Proof obligation 9 — the two fresh confirmation questions

§V218.10 carries one bounded question for each line, each requiring SHA-256
recomputation of the v2.1.8 bytes and of every governing hash, each treating this
closure as untrusted, and each demanding adversarial review of the reaper repair
and of the eliminated `T3`:

- **X line (Claude Opus 4.8)** — eight numbered attacks covering the exact
  `sigaction` semantics on the pinned CPython, the sufficiency of the
  `/proc/self/status` readback given the honestly stated `SA_NOCLDWAIT` gap and
  its three backup detectors, the fork-ownership proof at every instruction
  boundary, the totality of the rebuilt `IDENTITY_SAFE` and the safe direction of
  X217-m1's case, whether `T3` is truly gone and `B` is total and honest, the
  containment of the allowlist delta and the survival of §W2.6/§W6.4, the scope
  of the new zombie residual, and regression of every v2.1.7 closure. Verdict
  line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_X` or
  `REVISE_OFFICINA_SUPERVISOR_V2_1_8`.
- **Y line (GPT-5.6 Sol)** — seven numbered attacks covering the C217-1
  counterexample end to end through a fork-without-exec launcher inheriting both
  `SIG_IGN` and `SA_NOCLDWAIT`, universal application of `ECHILD ⇒ INCONCLUSIVE`,
  the M217-1 stopped-middle/unreadable-`/proc` case against R3's two permitted
  continuations, terminal disjointness and `T2` truthfulness with the existing
  resolver's totality, the m217-1 causal trace and any surviving `m5`/`rel2`
  citation, the delta's containment against the signed harness's own import
  clause plus the zombie residual's scope, and regression of §V217.1/§V217.4 and
  of the filesystem-exclusion boundary. Verdict line 1 exactly
  `CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_Y` or `REVISE_OFFICINA_SUPERVISOR_V2_1_8`.

## Weakest points of this layer, stated by its own author

Recorded so that reviewers attack them first rather than having to find them:

1. **`SA_NOCLDWAIT` is written but not read back.** Linux exposes no
   `SA_NOCLDWAIT` bit through `/proc`, and `ctypes` stays outside the allowlist,
   so that half of the normalization rests on the semantics of the `sigaction`
   the correction pins rather than on an observation. §V218.2.3 states this
   explicitly, marks the two underlying platform facts as reviewer-verifiable
   rather than author-asserted, and backs the gap with three independent
   contradiction detectors. If a reviewer judges that insufficient, the finding
   is real.
2. **`B-CONTRADICTED` does not terminate** under a violated sole-reaper contract
   and holds `SPAWN.lock` while it lasts. That is a deliberate fail-closed
   choice — the alternatives are signalling a possibly recycled pid or declaring
   a possibly live child dead — but it is a stall, and reviewers should test
   whether a safe terminating alternative exists that this author missed.
3. **The zombie residual is new cost created by this repair.** Normalizing
   `SIGCHLD` means a long-lived CLI that takes `T2` retains one zombie per such
   attempt until its next attempt or its exit.
4. **The sole-reaper contract is a restriction on the implementation**, verified
   statically (rows 223/224) rather than by construction. A future implementer
   who adds a thread, a `Popen`, or a wildcard wait to the CLI breaks the
   premise; the correction calls that a contract violation rather than a route.
5. **The `T2` resolver's `/proc` dependence.** If the *later* process also cannot
   read `/proc`, `s4` refuses retryably instead of acting. That is correct
   fail-closed behaviour, but it is a liveness limit and is stated as one.

## Custody, authorization boundary, and programme state

Exactly **two** files were created by this work, and nothing else in the
repository was touched:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_8_closure.md` (this file)

No prior artifact, contract, signature, review, prompt, code file, test file,
runtime tree, Cursor-dirty file, or unrelated change was edited, staged, or
committed. Nothing ran; no process, probe, smoke command, or Officina component
was started; no runtime or scientific data was created.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not authorized and
remains unavailable**. It becomes available only if a fresh independent X-line
review and a fresh independent Y-line review both confirm the **exact v2.1.8
bytes** whose digest is `33b0b916…`; no earlier confirmation of any version
carries across, and the `signal` allowlist delta makes independent review of
these bytes strictly mandatory. This closure authorizes **no** implementation,
no code or test change, no commit, no host change, no T activation, no entropy,
no E1/E2/E3 spend, no Q/C work, no capability, lease, operation, capacity
artifact, custody disposition, result manifest, world, learner, candidate, Q
attempt, datum, outcome, Proof, or claim movement, and no later gate.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`.
**T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`; no artifact was
produced.**
