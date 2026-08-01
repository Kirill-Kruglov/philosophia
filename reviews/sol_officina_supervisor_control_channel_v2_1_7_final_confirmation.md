REVISE_OFFICINA_SUPERVISOR_V2_1_7

# Independent clean-context Y-line review

Date: 2026-08-01

Reviewer line: Y

## Review base, bytes, and method

Review base: `e965681274989c06d3e3fad3ca35dad990be2614`, proved to
descend from the required commit
`063d29042175e05d35eb3fee2b7403cca300c1a9`.

I read the complete supervisor v2/v2.1/v2.1.1/v2.1.2/v2.1.3/v2.1.4/
v2.1.5/v2.1.6/v2.1.7 replacement chain; the two supervisor author
signatures and authorship note; the signed generic-harness v2 through v2.3.1
composite and its signature; the batch-settlement v1 through v1.1.1
composite; both formal v2.1.6 reviews; and the v2.1.7 author closure/chat
response. Claude Code Opus 5 authored v2.1 through v2.1.7 and its closure.
I treated every author assertion and example as untrusted self-assessment.

Recomputed SHA-256:

```text
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
```

This exactly equals the expected digest. The repository was already dirty;
all pre-existing tracked and untracked changes were preserved. This was a
static contract review only: read-only file/Git inspection, literal searches,
ancestry checking, and SHA-256 were used. No repository code, test, probe,
smoke command, or Officina process ran. No runtime or scientific artifact was
created or changed. This review is the only file created.

## Answer

No. Sol C1 and Opus X216-M1 are closed exactly, and Opus X216-m1's explicit
stat-routing gap is closed. Sol M1 and M2 are not closed exactly.

The blocking defect is inherited process state. Sections V217.2.4,
V217.3.5, V217.5, and test rows 198–200/207 assert that `ECHILD` proves death,
that the CLI's route is the only reaper, and that an unreaped child always
pins its PID until this route proves death. The only premise offered is that
this contract installs no signal disposition and `signal` is outside the
allowlist. That does not constrain the disposition and flags inherited by the
CLI before `c4`, including `SIGCHLD = SIG_IGN` and `SA_NOCLDWAIT`, nor does it
exclude a prior or concurrent reaper. With auto-reaping, the zombie/PID-pin
premise used to make the stat-to-signal interval safe is absent. A child can
exit and be auto-reaped after the identity sample; its PID can then be reused
before `SIGTERM` or `SIGKILL`, so the signal can target an unrelated process.
An unqualified `ECHILD` cannot be attributed to this route as the text does.

Independently, T3 expressly removes `SPAWNING.json`, installs no replacement,
and returns while the middle may still be live. Section V217.3.4 itself calls
that middle “untracked.” The middle retains the fork-shared singleton; if it is
stopped, later acquisition wedges indefinitely and no `s4` record exists.
Calling this fail-closed or an A3 residual does not satisfy the required
no-untracked-live-process and forward-progress conditions. The accompanying
two-supervisor proof also starts at `m5`/`rel2`, whereas every `c5`–`c7`
stage-M abandonment occurs before `c8`: the middle is actually at `m0`, owns
its own `rel1_w`, and exits ordinarily by the `m0` bound. The no-second-
supervisor conclusion survives because that live middle retains the lock and
no `c8` release byte exists, but the stated rel2 proof is not the governing
trace and it does not cure the untracked/stopped case.

The author token remains unavailable.

## One-to-one disposition of the five inherited findings

| Finding | v2.1.7 repair | Independent disposition |
|---|---|---|
| **Sol C1 (Critical)** — selector facts not object-bound/finally revalidated | §V217.1 binds enumeration, `lstat`, `O_NOFOLLOW` open, `fstat`, bytes, hash, and decode; barriers precede branch and disposition | **Closed exactly.** The old descriptor pins the old inode; unchanged `(dev, ino)` against the fresh canonical-name `lstat` cannot validate a replacement because the pinned old inode cannot be reused. Both barriers re-observe all three names and require the same rule and relations. The only remaining mutation window is after the last observation, explicitly A3 procedural and non-citable. |
| **Sol M1 (Major)** — stage-M syscall/result table not total | §V217.2 introduces closed stat/signal/wait enums | **Not closed.** The individual errno/result rows are syntactically enumerated, but the `ECHILD` and PID-reuse conclusions depend on an unestablished default-`SIGCHLD`/sole-reaper premise. The table can authorize an unsafe signal or false route without the exact inherited-process-state premise. |
| **Sol M2 (Major)** — fail-closed stage M can wedge later launch | §V217.3 removes the CLI's `SPAWNING.json`; T2 reuses `SPAWNING_MIDDLE`; T3 installs nothing | **Not closed.** T1 can rest on the unsound M1 premise. T2 is constructible when a valid identity was observed, but T3 deliberately leaves a possibly live middle untracked and can leave the singleton wedged forever when that process is stopped. The T3 parenthetical also mentions `DENIED` signals although any signal attempt follows `PRESENT_VALID`, which selects T2; that text gives two terminal readings. |
| **Opus X216-M1 (Major)** — stale fixed-total CLI assertions and false exhaustive search | §V217.4 replaces §N3.5, §N11, §N12 row 86, §U2.4, §U2.7 and prior false completeness statements | **Closed exactly.** Independent declared-term and semantic-equivalent searches found no surviving operative fixed-total CLI lifetime/lock-hold assertion. D1 now rests only on no supervisor waiting for `SPAWN.lock`. |
| **Opus X216-m1 (Minor)** — unreadable/unparsable c6 stat unmapped | `UNREADABLE`/`UNPARSABLE`/`ERROR` explicitly route no-kill/no-unlink | **Closed as the narrow finding.** Those results no longer escape. The broader M1 death/reaper premise remains open. |

## Trace 1 — object-bound C1 and every mutation cut

One epoch enumerates once and constructs one closed record for each of
`SETTLEMENT.json`, `QUARANTINE.json`, and `RESULT_MANIFEST.json`.
Presence is negated paired absence, so enumeration membership or successful
`lstat` makes a symlink, directory, device, FIFO, socket, multiply-linked,
zero-byte, truncated, partial, or malformed object present and invalid rather
than absent. `O_NOFOLLOW` rejects a new symlink; `(lstat_dev,lstat_ino)` must
equal the opened descriptor's `fstat`; the complete bytes, SHA-256, and decode
come from that descriptor only.

The object-name replacement attack fails mechanically:

1. The initial descriptor pins inode A and records A's `(dev,ino)`, bytes, and
   hash.
2. A same-UID actor renames canonical name A away and installs inode B.
3. A barrier's fresh `lstat` of the canonical name observes B. Its identity
   differs from A. A cannot be recycled to the same inode number while the
   retained descriptor pins it.
4. R-b fails; no branch or disposition is authorized. A rewrite in place is
   caught by the fresh descriptor bytes/hash comparison. A remove/create is
   caught by paired absence or identity change.

The complete cut result is: mutation before O1 is the observed state; listed
then removed is inconclusive; created after enumeration is present; symlink
replacement is invalid; removal or regular replacement between `lstat` and
open is inconclusive; descriptor-read/decode facts remain bound; any change
before barrier 1 prevents branch entry; any change after barrier 1 but before
barrier 2 prevents `.disposed.json` and release. Both barriers re-run the same
algorithm over all three names and require unchanged B/HS/HQ and the same
§V216.1.2 rule. The descriptor-pinned old inode cannot validate a newly
replaced canonical name.

## Trace 2 — A3 residual boundary

Changes before the branch barrier release nothing. Changes after that barrier
but before the disposition barrier release nothing. A change after one name's
last observation in the final barrier is necessarily within the final
observation-to-install window and is not prevented; §V217.1.5 and the cut
table label it as a deliberate same-UID A3 procedural residual, permanently
non-citable and not impossible. `T_RUNTIME.lock` is not represented as a
same-UID filesystem security boundary. The selector repair therefore meets
the required honest residual boundary.

That conclusion does not excuse §V217.3.4's different stopped-middle state:
the task's required boundary forbids using fail-closed/A3 language to accept a
live untracked process or a silent singleton wedge.

## Trace 3 — M1 stat, signal, wait, EINTR, exit, and PID reuse

The literal table covers these surface results:

| Operation/result | Written route | Independent result |
|---|---|---|
| stat `ENOENT`/`ESRCH` | `ABSENT`; no signal; `WAIT_PROVE` | Safe: absence alone is not death. |
| stat valid + matching/captured identity | signal route | Safe only while the own-child PID remains pinned. That premise is not established under inherited auto-reaping/external reaping. |
| stat `EACCES`/`EPERM`, parse failure, other error | no kill/unlink/death; terminal selection | Explicit and fail-closed. |
| stat `EINTR` | retry to the existing deadline, then `ERROR` | Closed if the referenced step deadline governs the call. |
| signal success | poll `WAIT_PROVE` | No death inferred merely from success. |
| signal `ESRCH` | `GONE`; `WAIT_PROVE` | No death inferred merely from `ESRCH`. |
| signal `EINTR` | retry same signal to deadline, then `ERROR` | Explicit. |
| signal `EPERM`/other | no further signal/unlink; T2/T3 | Explicit, subject to the contradictory T3 parenthetical. |
| wait returns `pid_mid` | `PROVED_DEAD` | Sound; this call reaped the terminated own child. |
| wait returns `0` | `NOT_YET`; continue to deadline | Sound for running or stopped child. |
| wait `EINTR` | retry to deadline, then inconclusive | Explicit. |
| wait other error | inconclusive; T2/T3 | Explicit but inherits the terminal defect. |
| wait `ECHILD` | `PROVED_DEAD` | **Rejected as specified.** No mechanical pre-fork reset/check or sole-reaper invariant exists. The stated reason is false as a contract premise. |

The decisive signal counterexample is independent of whether a particular
`ECHILD` happens before or after the child terminates: inherit
`SIGCHLD=SIG_IGN` or `SA_NOCLDWAIT`; obtain `PRESENT_VALID`; let the child exit
and auto-reap before the next signal; reuse the PID; then `os.kill(pid_mid,
SIGTERM|SIGKILL)` can target the reused process because the claimed zombie pin
never existed. Prior/concurrent `waitpid` similarly falsifies “this route is
the only reaper.” Ordinary exits are total only after that premise is made
mechanical.

## Trace 4 — `ECHILD` premise

The contract contains no pre-`c4` operation that reads and rejects inherited
`SIGCHLD` state, sets `SIGCHLD` to default, clears `SA_NOCLDWAIT`, or excludes
another thread/reaper. Saying that this contract itself installs no signal
disposition establishes none of those facts. Test row 199 can only prove the
absence of an installation in these files; it cannot prove the process state
that the death and PID-reuse rules require.

Smallest mechanical repair: before `c4`, normalize and verify default
`SIGCHLD`, clear `SA_NOCLDWAIT`, and establish the CLI route as the sole
reaper for `pid_mid` (with the required reviewed import/allowlist change), or
use a mechanically pinned child handle such as a reviewed pidfd design. Until
then, treat `ECHILD` as inconclusive and never use the unreaped-zombie premise
to authorize a signal. Merely changing the `ECHILD` row is insufficient unless
the stat-to-signal PID-reuse window is also repaired.

## Trace 5 — M2 terminals and crash continuations

T1 is safe only when `waitpid` actually returns `pid_mid`; it is unsafe when
reached through the unestablished `ECHILD` premise. T2's existing
`SPAWNING_MIDDLE.json` schema is truthfully constructible after any
`PRESENT_VALID` observation: pid, start identity, ppid, CLI identity,
`spawning_id`, boot identity, and creation time are available. The existing
`s4` route can validate and kill that recorded middle after the age bound,
then P3 removes the record. Wait timeout/error and signal denial select T2
when that valid observation exists.

T3 is not an acceptable total continuation. At c5/c6 it can have only
`pid_mid`; unreadable/unparsable/error results and an inconclusive wait leave a
possibly live child. The route installs nothing, removes the only attempt
marker, releases the CLI's reference, and returns. A normally scheduled child
remains inert at `m0` and exits at its bound; a stopped child remains live,
unrecorded, and retains the singleton indefinitely. The next CLI times out on
the lock but has neither a middle identity nor an s4 record. This is precisely
an untracked-live-process/later-progress wedge, not a complete terminal.

The phrase “or DENIED signals” in T3 also conflicts with its formal condition
“no `PRESENT_VALID` stat was ever obtained”: a signal attempt is reachable
only after an identity-safe `PRESENT_VALID` result, which formally selects T2.
One implementation installs the middle record; another following the
parenthetical installs nothing.

Smallest repair after fixing the child-state premise: because an own child
with default `SIGCHLD` and a sole reaper retains a non-reusable PID until
waited, stage M may safely terminate that own child even when `/proc` identity
is unreadable, and must obtain a real wait result before removing the attempt
handle. Delete T3 as a returning live-child terminal, or add a truthful durable
handle and a total later resolver that cannot wedge. No route may return after
discarding every durable handle on a child that may remain live.

## Trace 6 — T3 and second-supervisor schedules

For the actual c5/c6/c7 cuts, execution order is
`c4 → c5 → c6 → c7 → c8`; therefore no `rel1` release byte has been written.
The middle is at `m0`, retains its own `rel1_w` and the fork-shared
`SPAWN.lock` description, and cannot reach `m1`, `m5`, or `m7`. Closing the
CLI's `rel2_w` is not the causal protection on these cuts. An ordinary middle
exits when the m0 bound expires; until then, its retained lock prevents a new
CLI from acquiring immediately. If hypothetically at m5, the middle has
closed its own rel2 writer, the abandoned CLI has queued no c12 byte and closes
the last writer, so EOF/bound also prevents m7. No schedule queues c12 before
these stage-M routes.

Thus no valid c5–c7 history yields two supervisors. But safety against a
second supervisor does not make the T3 state acceptable: a stopped untracked
middle can hold the singleton forever, and the false `ECHILD`/auto-reap premise
can also remove records on an unsafe process-state inference.

## Trace 7 — X216-M1 whole-chain fixed-total sweep

I repeated the declared eighteen-term search across every operative
supervisor layer and separately searched semantic equivalents involving CLI,
client, `SPAWN.lock`, maximum/finite duration, lifetime, lock hold, deadlines,
and release. The stale class is fully replaced:

- v2.1.2 §N3.5 and §N11 now carry §V217.4.3;
- v2.1.2 §N12 row 86 is replaced by §V217.4.4;
- v2.1.3 §U2.4 and §U2.7 now carry §V217.4.3;
- v2.1.4 §V214.1.1/§V214.1.5 and rows 121/126 remain replaced by v2.1.6;
- the v2.1.4 grandchild sufficiency claim remains replaced by v2.1.5;
- §V216.4.1's and §V216.4.2's false universal/exhaustiveness wording is
  replaced by scoped, reproducible language.

The retained statements are specific rather than total: v2.1 §W2.2 bounds one
identity poll; v2.1.1 §Z3.5 bounds a bootstrap-pipe read; v2.1.6 bounds only
pipe helpers; v2.1.5 defines a grandchild anti-wedge policy while naming
unbounded `/proc`/install/`fsync`. No operative statement supplies a fixed
arithmetic bound for the CLI's total lifetime or total lock hold. Rows 86,
121, 126, 159, 160, 161, and 162 are jointly satisfiable. D1 rests solely on
the fact that no supervisor waits for `SPAWN.lock`, not on a client total.

## Trace 8 — no regression

| Surface | Independent result under v2.1.7 |
|---|---|
| `CLOSE_OWNED` | Preserved verbatim, including both lock closes, ownership removal before routing, no fd-number retry, and Linux non-`EBADF` release semantics. |
| Malformed-first selector / cross-product | Rule 0 physical-presence dominance and the §V216.1.3 cross-product are preserved; §V217.1 strengthens only observation and revalidation. |
| Branch/custody release | B-P/B-QM/B-QN, P1–P7, capacity disposition, no-replenishment, and one-release K1 accounting are preserved; barriers narrow release. |
| Bootstrap/fork/GC/watchdog/singleton | Four bounded nonblocking channels, adapter and fork gates, accepted-last GC with D6, watchdog single-authority partition, and the normal singleton order carry. The new stage-M reaper/T3 rules are the exceptions identified above. |
| A3/B1/C1/D1/K1 | No selected policy cell is reopened. A3's selector residual is honestly scoped; B1 journal semantics, C1 freezer/witness role, D1 no-idle-exit, and K1 constants/custody are unchanged. |
| Generic harness / batch settlement | v2.3.1 §J1–§J3 and batch v1.1.1 §D1/§D2, including inline meter evidence, fixed process order, prefix settlement, head/cache authority, and archival boundaries, are untouched. |
| Events / E1/E2/E3 | Nine signed events, phase/resource constants, invalidity dominance, and no scientific relabelling are unchanged. |
| Q/C and T | Every added fact remains control-plane, T-development-only, and non-citable; no Q/C authority moves. T remains inactive. |

## New findings

### C217-1 (Critical) — inherited `SIGCHLD`/reaper state defeats the death and PID-reuse premise

**Loci:** §V217.2.4 paragraphs “Why these two outcomes prove death” and “PID
reuse”; §V217.3.5 `ECHILD` row; §V217.5 `ECHILD` row; tests 198–200 and the
T1/death-before-unlink obligations.

**Counterexample:** inherit `SIGCHLD=SIG_IGN` or `SA_NOCLDWAIT`; capture a
valid child identity; let the child exit and auto-reap before a later signal;
let the PID be reused; then signal the reused PID under the false zombie-pin
claim. The contract can kill an unrelated process. A prior/concurrent reaper
also refutes the claimed sole provenance of `ECHILD`.

**Smallest repair:** mechanically normalize/check `SIGCHLD` and
`SA_NOCLDWAIT` before fork and exclude every competing reaper for this child,
or adopt a reviewed pinned-handle design. Map `ECHILD` to inconclusive unless
its exact safe premise has been mechanically established. Repair the entire
stat-to-signal PID-reuse interval, not only the prose explanation.

### M217-1 (Major) — T3 abandons a live untracked middle and has contradictory terminal membership

**Loci:** §V217.3.2 T2/T3, §V217.3.3 “nothing” continuation, §V217.3.4,
§V217.3.5 long-lived/unreadable rows, §V217.5 T3/stopped-middle rows, tests
203–208.

**Counterexample:** every `/proc` observation fails, `waitpid` is
inconclusive, and the middle is stopped at m0. T3 installs nothing, removes
`SPAWNING.json`, and returns. The live middle retains the fork-shared lock;
the next CLI cannot acquire it and has no identity-bearing record for s4.
Progress is silently wedged. Separately, a denied signal presupposes
`PRESENT_VALID`, making both the T2 condition and T3's parenthetical apply.

**Smallest repair:** no returning terminal may discard every handle while the
middle may live. With the corrected sole-reaper/zombie-pin premise, terminate
and genuinely reap the own child even when `/proc` is unreadable, eliminating
the live T3 case. Otherwise introduce a truthful durable handle plus a total,
identity-safe later resolver; make terminal predicates disjoint.

### m217-1 (Minor) — the written second-supervisor proof names the wrong gate for stage M

**Loci:** §V217.3.1 “Two-supervisor safety,” §V217.5 test row 207, and the
author closure §5 (non-governing but evidentiary of the same reasoning).

**Counterexample:** at c5–c7 the middle has not received c8, remains at m0,
and still owns rel1_w; it cannot be analyzed as an m5 rel2 reader. The claimed
rel2 EOF is not the causal continuation of those cuts.

**Smallest repair:** state the actual c5–c7 trace: no c8 byte, m0 bound, and
the middle's fork-shared lock prevents acquisition until exit. Retain the rel2
argument only for routes that can actually reach m5. This does not cure
M217-1 by itself.

## Author-cell determination

No new author-choice cell is required. The repairs are mechanical process-
identity, reaper, terminal-totality, and causal-proof corrections under the
already selected A3/B1/C1/D1/K1 policies. Any required `signal`/pidfd import or
allowlist change must be named and reviewed as a control-surface delta; it is
not silently available in the current zero-delta contract.

Claude Code Opus 5 is the specification author and cannot serve as the
independent X line for its own bytes. This Y verdict is `REVISE`; no X verdict,
past or future, can make these exact bytes signable without a corrected layer
and fresh review of that layer.

## Exact authorization boundary and custody

Because the verdict is **REVISE**, Kirill's token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains
**unavailable**. This review does not authorize implementation, code/test
changes, activation, entropy, runtime construction, any supervisor/controller/
worker/watchdog/adapter/middle child, endpoint, pipe, FIFO, journal, spawn
record, capability, lease, operation, capacity or custody artifact, result
manifest, E1/E2/E3 spend, world, learner, candidate, Q attempt, Q/C object,
science, datum, outcome, Proof, or claim movement. Conditional authorization
on X confirming these bytes is not granted because Y does not confirm them.

No project execution or runtime change occurred; no implementation, test,
probe, smoke command, or Officina process ran; no contract, signature, prior
review, code, test, or pre-existing dirty artifact was modified. Exactly this
one review file was created. T remains `NOT_ACTIVATED`; the programme claim
remains `OPEN`.
