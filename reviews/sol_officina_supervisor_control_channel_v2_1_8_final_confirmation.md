REVISE_OFFICINA_SUPERVISOR_V2_1_8

# Independent clean-context Y-line review

Date: 2026-08-02

Reviewer line: Y

## Review base, bytes, and method

Review base: `568f68aeb391ec5292d0446abbae734d9345d981`, verified to
descend from the required commit
`6e158560a8bd452d6780d9e279a079f41f4b78fe`.

I read the supervisor v2 through v2.1.8 replacement chain, the author
selections and signatures, the generic-harness v2 through v2.3.1 composite,
the batch-settlement v1 through v1.1.1 composite, the authorship note, and both
formal v2.1.7 `REVISE` reviews. Claude Code Opus 5 authored v2.1 through
v2.1.8 and its closure. I treated its examples, closure, and chat response as
untrusted self-assessment.

Recomputed SHA-256:

```text
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
```

This exactly matches the expected digest. I also recomputed every digest in
v2.1.8's governing-hash block; all match, including the two v2.1.7 reviews,
the signed harness/batch composites, both author-selection signatures, and the
unamended `verification.py` digest `327b1bb2…`.

This was a static contract review. I used read-only file/Git inspection,
literal search, hashing, and arithmetic. I ran no repository code, tests,
probes, smoke commands, fork/signal experiments, subprocess experiments, or
Officina process. I changed no existing file or runtime state. The pre-existing
dirty tracked and untracked files were preserved.

## Answer

No. v2.1.8 correctly performs the central Linux/CPython disposition repair:
on the pinned CPython interface, `signal.signal(SIGCHLD, SIG_DFL)` reaches
`PyOS_setsig`, whose `sigaction` replacement sets `sa_handler = SIG_DFL`, an
empty mask, and `sa_flags = SA_ONSTACK`; that full replacement clears both an
inherited `SIG_IGN` and inherited `SA_NOCLDWAIT`. Linux auto-reaping is caused
by explicit `SIG_IGN` or `SA_NOCLDWAIT`, and `/proc/self/status` exposes only
the ignored/caught masks, not `SA_NOCLDWAIT`. The layer distinguishes those
facts honestly. Its `ECHILD` and `ESRCH` routes no longer claim death, its
ten-row identity table closes X217-m1, `T3` is removed, and the governing
stage-M causal proof is now the correct `m0`/`rel1`/fork-shared-lock trace.

Four blocking defects remain:

1. The sole-reaper premise is declared, not mechanically established against
   inherited same-process threads or other inherited reapers. On Linux, any
   thread in the parent thread group can wait for a child forked by another
   thread. v2.1.8 permits an in-process entry and checks only that `c3n` runs in
   the main thread; it neither proves that no other thread exists nor prevents
   such a thread from executing a wildcard wait. A competing waiter can reap
   `pid_mid` after `IDENTITY_OBSERVE` and before `SIGNAL_ATTEMPT`; after PID
   reuse, the ownership label is still `OWNED`, and the signal can hit an
   unrelated process before any `ECHILD`, `ESRCH`, or `ppid` detector runs.
2. W-2 through W-5 are enumerated as permitted wait sites but have no total
   result automata. The carried stage-1/stage-2/P3/success prose does not route
   `(0,0)`, `EINTR`, `ECHILD`, arbitrary errors, prior reap, or the success-path
   race where `m8` has been reported but `m9` has not exited. Therefore the
   claimed total reaper/ownership automaton exists only at W-1.
3. The allowlist containment is internally unsatisfiable. The signed harness
   and supervisor chain make `src/philosophia/officina/generic_harness.py` the
   sole module/executable root and place the CLI/bootstrap adapter there.
   v2.1.8 requires `signal` in the module implementing c1–c18 while explicitly
   forbidding `signal` in “the generic harness” and asserting the harness still
   imports no `signal`. A conforming implementation has no permitted importer.
   Moving c1–c18 to an unnamed module would be an undeclared dependency/importer
   expansion.
4. `VERIFY_REAPING_STATE` accepts a short hexadecimal mask as if omitted high
   bits were verified clear. For example, `SigIgn: 0` and `SigCgt: 0` pass V3,
   convert to zero at V4, and pass V5 even though neither string encodes the
   `SIGCHLD` bit position. This violates the required fail-closed treatment of
   malformed/short masks.

The author token remains unavailable.

## Disposition of the five inherited v2.1.7 findings

| Finding | v2.1.8 disposition | Independent result |
|---|---|---|
| **C217-1 (Critical)** — inherited `SIGCHLD`/reaper state defeats death and PID safety | §V218.1–§V218.3 | **Not closed exactly.** The `SIG_IGN` and `SA_NOCLDWAIT` dispositions are repaired correctly, and `ECHILD` is no longer death. The independently required competing-reaper half remains only a prohibition. A pre-existing same-process thread can reap between observation and signal, defeating the PID pin before a contradiction detector executes. |
| **M217-1 (Major)** — T3 abandons a live untracked middle | §V218.4 | **The returning-T3 defect is closed, but the required forward-progress property is not.** T1/T2/B discard no possibly live child. However B-CONTRADICTED is reachable through the unexcluded reaper schedule and has no possible successful wait or lawful forward resolver; it holds the singleton forever. |
| **m217-1 (Minor)** — stage-M proof uses the wrong gate | §V218.5 | **Closed exactly.** At c5–c7 no c8 byte exists, the middle is at m0 and owns `rel1_w`, m1/m5/m7 are unreachable, and the fork-shared lock serializes a later CLI. `m5`/`rel2` is retained only for post-c8 routes. |
| **X217-M1 (Major)** — inherited `SIGCHLD` defeats the zombie/PID premise | §V218.1–§V218.3 | **Not closed exactly.** The inherited-disposition defect is closed on CPython/Linux, but the replacement proof additionally relies on exclusive wait ownership that is not mechanically established for supported in-process entry. The same recycled-PID signal counterexample survives through a competing thread. |
| **X217-m1 (Minor)** — missing uncaptured `ppid`-mismatch row | §V218.3.4 I-4/I-10 | **Closed exactly.** Mismatch captures nothing, irreversibly sets `CONTRADICTED`, authorizes no signal, and cannot construct T2 from the contradictory observation. |

## Trace 1 — allowlist containment and authority

The intended engineering delta is loudly and exhaustively identified as the
single absolute import `signal`. The only permitted names are `SIGCHLD`,
`SIG_DFL`, `signal`, and `getsignal`; the only permitted call sites are the two
c3n functions. No handler, `SIG_IGN`, mask/wakeup/pidfd function, new constant,
schema, token, event, path, command, operator action, resource choice, or
scientific choice is expressly authorized. Section V218.1.4 supersedes all
fourteen identified zero-delta/`signal`-outside loci, and it correctly invokes
the signed harness §9 rule that an allowlist change needs a reviewed amendment.

Containment nevertheless fails mechanically at the importer boundary:

- v2 §V2.10 pins the sole root to `generic_harness.py`;
- v2.1.1 §Z3.3 makes the fixed bootstrap adapter part of that sole module;
- the signed harness §9 says that `generic_harness.py.__main__` is the CLI and
  that the harness imports no `signal`;
- v2.1.8 §V218.1.2 requires the c1–c18 CLI bootstrap module to import `signal`
  but lists the generic harness among forbidden importers.

Module imports are file-level facts; a function in `generic_harness.py` cannot
import `signal` while the module does not. The text therefore cannot be
implemented without either contradicting §V218.1.2 or adding an unnamed module
and dependency. This is a signed-contract conflict, not a harmless wording
issue. No extra API/importer is implicitly authorized.

## Trace 2 — inherited dispositions and the platform guarantee

The disposition repair itself is sound:

| Initial state | `signal.signal(SIGCHLD, SIG_DFL)` on pinned CPython/Linux | Result |
|---|---|---|
| `SIG_DFL`, flags clear | whole `sigaction` replaced | remains default; no auto-reap |
| explicit `SIG_IGN` inherited through `execve` or `fork` | handler replaced by `SIG_DFL` | ignore bit cleared |
| `SIG_DFL | SA_NOCLDWAIT` inherited through fork without exec | entire `sa_flags` replaced by `SA_ONSTACK` | `SA_NOCLDWAIT` cleared |
| caught handler | handler replaced, mask emptied, flags replaced | no caught SIGCHLD handler remains |

CPython 3.12.3's `signal_signal_impl` calls `PyOS_setsig`; `PyOS_setsig` uses
`sigaction` with an empty mask and `SA_ONSTACK`. Neither `SA_NOCLDWAIT` nor
`SA_NOCLDSTOP` survives. Linux documents that explicit `SIG_IGN` or
`SA_NOCLDWAIT` prevents zombies; fork inherits dispositions, while exec resets
caught dispositions but preserves ignored ones. `/proc`'s `SigIgn`/`SigCgt`
readback is correctly described as limited: it cannot read `SA_NOCLDWAIT`.

The repair is placed under `SPAWN.lock`, after c3's pipe construction and
immediately before c4. A normalization/verification failure takes a no-fork
cleanup route. Repeated attempts repeat c3n. These properties defeat both the
fork-inherited and exec-inherited disposition counterexamples.

They do not defeat a competing waiter already present in an in-process host.
Main-thread eligibility for `signal.signal` proves neither single-threadedness
nor exclusive child-wait ownership.

Platform references used for this static check:

- [CPython 3.12.3 `signal_signal_impl`](https://github.com/python/cpython/blob/v3.12.3/Modules/signalmodule.c)
- [CPython 3.12.3 `PyOS_setsig` implementation](https://github.com/python/cpython/blob/v3.12.3/Python/pylifecycle.c)
- [Linux `sigaction(2)`](https://www.man7.org/linux/man-pages/man2/rt_sigaction.2.html)
- [Linux `wait(2)`](https://www.man7.org/linux/man-pages/man2/waitpid.2.html)
- [Linux `signal(7)`](https://man7.org/linux/man-pages/man7/signal.7.html)

## Trace 3 — c3n state machine

`NORMALIZE_REAPING_STATE` routes normal return to `NORMALIZE_OK` and catches
`ValueError`, `RuntimeError`, `OSError`, and every other exception as
inconclusive. The prior handler return is diagnostic only. Wrong thread and
subinterpreter therefore cause no fork. `VERIFY_REAPING_STATE` routes missing,
unreadable, duplicate, non-hex, or disagreeing `SigIgn`/`SigCgt`, and a
`getsignal` disagreement, to failure/inconclusive; all three non-normalized
results use the same no-fork cleanup. The lock, record, and eight fd ends have
one owner and cleanup route. No partial process authorization exists before
c4.

The state machine is not total for short masks. Its grammar accepts any
nonempty hex string, so the bit shift manufactures zero for a bit position the
text never encoded. The smallest correct rule is to require each mask to
encode at least `int(SIGCHLD)` bits (or the exact pinned kernel width) before
V5. A short mask must be `VERIFY_INCONCLUSIVE`, and test row 220 must include
empty, one-digit, and just-below-required-width cases.

## Trace 4 — reaper and wait table

The five allowed sites are named, positive-pid targeted, and intended to be
mutually exclusive per attempt:

| Site | Purpose | Total result table? |
|---|---|---|
| W-1 | stage-M WAIT_PROVE | **Yes**: pid, zero, `ECHILD`, `EINTR`, other error |
| W-2 | stage-1 c9/c10 failure | **No** |
| W-3 | stage-2 c13/c14/c17 failure | **No** |
| W-4 | same-process later-attempt P3 reap | **No** |
| W-5 | success-path middle reap after m8 report | **No** |

At W-1, only `(pid_mid,status)` proves death and sets `REAPED`; `(0,0)` is
running/stopped; `ECHILD` is inconclusive and contradictory; `EINTR` retries
to the existing deadline; arbitrary errors remain inconclusive. WNOHANG without
WUNTRACED cannot return a stop/continue status. Those rows are sound.

The other four sites merely say `waitpid(pid_mid, WNOHANG)` or “reap if own”.
For example, after c13 observes m8's bootstrap line, the middle can still be
between m8 and m9, so W-5 can return `(0,0)`. No continuation, deadline, retry,
or ownership transition is specified. At W-2/W-3/W-4, `EINTR`, `ECHILD`, and
arbitrary errors are likewise unmapped. Section V218.2.6's statement that no
route behavior changes preserves these gaps rather than closing them.

The external-reaper attack is load-bearing. Linux permits any thread in a
thread group to wait on another thread's child. Schedule:

1. an in-process host invokes the CLI on the main interpreter thread while a
   pre-existing helper thread executes `waitpid(-1, WNOHANG)`;
2. c3n normalizes successfully and c4 establishes `OWNED`;
3. M2 reads a matching identity;
4. the child exits and the helper reaps it;
5. the PID is reused;
6. M3 sees `OWNED` and `os.kill(pid_mid, SIGTERM)` succeeds against the reused
   process.

No detector runs between steps 4 and 6. A later `ECHILD`, `ESRCH`, or ppid
mismatch is too late. Thus the normative sentence “no external component may
reap” is not a mechanical premise and does not establish the PID pin.

## Trace 5 — identity and signals

The ten rows I-1 through I-10 are disjoint and exhaustive over the stated
product once ownership is supplied. In particular:

- I-4 (uncaptured, `ppid != getpid`) captures nothing, contradicts ownership,
  and signals nothing;
- I-2 preserves only an earlier truthful capture and makes T2 available;
- I-5 treats absence as non-death;
- I-6/I-7/I-8 withhold capture while ownership, not observation, gates a
  signal;
- I-9 forbids all post-reap PID use;
- I-10 makes contradiction irreversible.

`SIGNAL_ATTEMPT` enumerates success, `ESRCH`, `EINTR`, `EPERM`, and other
errors. Success is not death. `ESRCH` becomes contradiction, never death.
`EPERM`/other errors stop that schedule's signals without changing identity.
The TERM/KILL schedule reaches a stopped owned child through uncatchable
SIGKILL, independent of `/proc`. After `REAPED` or `CONTRADICTED`, no signal is
authorized.

This table is safe only if `OWNED` is true. Because the competing-reaper
premise is not established, an `OWNED` label can outlive the actual child and
authorize the successful wrong-PID signal above. Ownership cannot replace
observation until its exclusivity premise is mechanical.

## Trace 6 — T1/T2/B, no T3

`T3` has no surviving operative body, membership clause, test, or prose
implication. References in v2.1.8 are deletions, historical descriptions, and
negative tests. The stage-M successor predicates are mechanically disjoint and
exhaustive:

```text
REAPED                              -> T1
not REAPED and captured identity    -> T2
not REAPED and no captured identity -> B
```

T1 returns only after targeted positive reap. T2's record uses only an
identity captured while ownership was not contradicted; it removes only the
self-naming CLI record, retains the middle record, and leaves P2b/P3/s4 as the
existing resolver. B returns nothing, retains the lock, record, and pid, and
therefore does not orphan or untrack a possibly live middle. No returning route
abandons a live child.

The corrected c5–c7 trace is sound: no c8 byte exists; the middle remains at
m0 with its own `rel1_w`; EOF cannot occur; m1, setsid, m5, and m7 are
unreachable; the middle's own m0 bound or an ownership-authorized kill ends it;
the fork-shared lock blocks a second CLI until exit. Long-lived, stopped,
no-capture, later-capture, unreadable `/proc`, wait-error, crash/restart, and
second-CLI schedules all preserve a handle. The exceptions are the unmechanical
ownership premise and the missing W-2…W-5 result tables already identified.

## Trace 7 — residual judgment

| Residual | Judgment |
|---|---|
| **T2 unreaped zombie** | **Acceptable in policy, but its W-4 implementation contract is incomplete.** A zombie is dead, holds no fd or fork-shared lock, and cannot act or cause PID reuse. It is reaped by a later same-process attempt or CLI exit. One zombie per T2 attempt is a truthful, non-citable process-resource residual. W-4 still needs the common total wait table. |
| **B-OWNED nontermination** | **Acceptable as a named A3/host-fault residual.** With sound ownership, SIGKILL or m0's own bound ordinarily leads to a positive reap. Persistent nontermination requires stopped-child interference plus persistent signal failure; B keeps every handle and s5 exposes retryable refusal without unsafe mutation. |
| **B-CONTRADICTED nontermination** | **Blocking under the present contract.** After `ECHILD`, a targeted wait can never return `pid_mid`; B's only stated exit is therefore impossible. It holds the lock and self-record forever, while every later CLI can only take s5 and retry the same refusal. There is no lawful progress action, durable contradiction handoff, or resolver; “an operator will notice” is expressly not a step. Because the competing reaper is not mechanically excluded, this is not confined to a mechanically impossible history. Naming the wedge makes it visible, not acceptable under the requested forward-progress criterion. |

The smallest resolution is first to establish exclusive reaping mechanically.
If contradiction is then limited to an implementation/host contract violation,
B-CONTRADICTED can remain an explicit non-returning safety sink. If the contract
continues to support environments where another waiter can exist, it instead
needs a reviewed pinned-handle design or a durable contradiction state with a
total safe resolver; s5 alone is not such a resolver.

## Trace 8 — full regression

| Surface | Independent result under v2.1.8 |
|---|---|
| Stage-M serialization | Correct `m0`/`rel1`/fork-shared-lock proof; post-c8 `m5`/`rel2` routes remain correctly scoped. |
| Object-bound observation and barriers | §V217.1 O1–O9, pinned-descriptor bytes/hash, paired absence, same-rule revalidation at branch and disposition, and all mutation cuts carry unchanged. |
| A3 residual | Final observation-to-install filesystem window remains procedural/non-citable; the reaper repair is nowhere a filesystem-exclusion proof. |
| Bound-language sweep | §V217.4's stale loci and revised rows carry. B's unbounded duration is consistent with the withdrawn fixed-total-CLI claim; no false finite total is reintroduced. |
| `CLOSE_OWNED` | Ownership removal before close, no fd-number retry, both lock closes, errno outcomes, and all named sites carry. |
| Malformed-first selector | Physical presence, Rule 0 dominance, full cross-product, and opposite-terminal exclusion carry. |
| Branch/custody release | B-P/B-QM/B-QN, P1–P7, custody absence, one-release K1 accounting, and no replenishment carry. |
| A3/B1/C1/D1/K1 | Policy cells and K1 constants do not move. The new process findings are mechanical; no scientific cell is reopened. |
| GC/watchdog/singleton | Accepted-last GC/D6, watchdog sole-writer/freezer partition, lock-first preflight, four-record ordering, P0–P3, and s1–s5 carry. The B-CONTRADICTED use of s5 is a liveness defect, not a mutation of s5. |
| Generic harness/batch settlement | v2.3.1 §J1–§J3 and batch v1.1.1 §D1/§D2, fixed process order, prefix settlement, head/cache authority, inline meter evidence, and archival boundaries are unchanged. The `signal` importer contradiction is the one contract conflict. |
| Events/E1/E2/E3 | Nine events, resource constants, invalidity dominance, and no relabelling are unchanged. |
| Q/C and T | New facts remain control-plane, T-development-only, and non-citable. No Q/C authority or science moves; T remains inactive. |

## New findings

### C218-1 (Critical) — the sole-reaper/PID-reservation premise is not mechanically established

**Loci:** §V218.2.4, §V218.2.6, §V218.3.1–§V218.3.2,
§V218.3.5–§V218.3.6, tests 222–224 and 230.

**Counterexample:** an in-process host has a pre-existing helper thread doing a
wildcard wait. The main interpreter thread passes c3n and forks. After a valid
identity observation, the child exits and the helper reaps it; the PID is
reused before M3; `OWNERSHIP` is still `OWNED`; `os.kill` succeeds against the
new process. Contradiction detectors run only afterward.

**Smallest repair:** mechanically establish a single-thread/no-competing-waiter
process before c4 and keep that property stable through the final reap. At
minimum, pin the permitted entry topology, verify a single task in
`/proc/self/task`, and close the signal-callback/thread-creation race between
that verification and c4; otherwise use a reviewed pidfd-based signalling
design. A prose prohibition and static search of Officina source are not
sufficient for inherited host state.

### M218-1 (Major) — four of five permitted wait sites have no total result automaton

**Loci:** §V218.2.6 W-2…W-5; carried §U2.5 stage-1/stage-2 routes; §U6.1 P3;
carried §W2.1 success reap; tests 223–224.

**Counterexample:** c13 receives the m8 bootstrap report, W-5 immediately calls
`waitpid(pid_mid, WNOHANG)`, and the child has not yet executed m9. The call
returns `(0,0)`; no retry/deadline/terminal is specified. Equivalent gaps exist
for `ECHILD`, `EINTR`, and arbitrary errors at W-2/W-3/W-4.

**Smallest repair:** define one shared targeted-positive-pid wait automaton for
all five sites, with explicit per-site deadlines and continuations for pid,
zero, `EINTR`, `ECHILD`, and every other error. Only pid sets `REAPED`; every
`ECHILD` is inconclusive/contradicted; no site executes after `REAPED`.

### M218-2 (Major) — the sole-root and permitted-importer rules contradict

**Loci:** §V218.1.2–§V218.1.4; v2 §V2.10; v2.1.1 §Z3.3; signed generic-harness
§9 and signature boundary.

**Counterexample:** implement c1–c18 in the signed sole CLI module
`generic_harness.py`. Importing `signal` satisfies c3n but violates the explicit
forbidden-importer row and the claimed unchanged harness rule. Moving the code
to another module creates an undeclared importer/dependency outside the exact
surface.

**Smallest repair:** choose and state one implementable topology. The smaller
one is to permit the tightly contained `signal` import in
`generic_harness.py`, explicitly replace the harness §9 no-`signal` sentence
and the affected implementation-boundary text, and retain the four-member/two-
function restriction. If a separate module is chosen instead, its exact path,
owner, imports, call-graph role, and edit authorization must be reviewed.

### M218-3 (Major) — B-CONTRADICTED has no lawful progress action

**Loci:** §V218.4.2 B, §V218.4.4 s5 row, §V218.4.5 residual 3, test 234.

**Counterexample:** a competing reaper produces `ECHILD` before any identity
capture. B-CONTRADICTED waits for a positive return that can never occur,
retains `SPAWN.lock` and `SPAWNING.json` forever, and later CLIs can only repeat
s5 refusals. No record or resolver can lawfully change the state.

**Smallest repair:** close C218-1 so this is mechanically unreachable under the
supported entry contract, or introduce a reviewed durable handoff/pinned-handle
resolver. Do not call s5 a resolver and do not rely on manual repair.

### m218-1 (Minor) — short `/proc` signal masks are accepted as verified clear

**Loci:** §V218.2.3 V3–V5 and test 220.

**Counterexample:** `SigIgn: 0` and `SigCgt: 0` satisfy the written grammar and
bit tests even though they do not encode the SIGCHLD bit position.

**Smallest repair:** require an exact pinned mask width or at least
`4 * hexadecimal_digit_count >= int(SIGCHLD)` before converting; otherwise
return `VERIFY_INCONCLUSIVE` and fork nothing. Add short-mask cases to row 220.

## Author-cell and contract-conflict determination

No scientific author cell is reopened. A3/B1/C1/D1/K1, E1/E2/E3, custody,
batch arithmetic, events, schemas, roots, and Q/C boundaries do not require a
new scientific choice. The required repairs are process-control and
engineering-surface repairs.

There is, however, a concrete signed-contract conflict: v2.1.8 cannot both
keep the signed harness's no-`signal` import property and place its required
`signal` call in the sole generic-harness CLI module. The supervisor amendment
token may review an engineering allowlist amendment, but these bytes do not
state an implementable authorization boundary. A corrected layer must name the
actual importer and explicitly supersede every conflicting harness/supervisor
sentence. No extra importer, API, durable object, schema, constant, token,
operator action, resource value, or scientific choice is implicitly available.

## Exact authorization boundary

Because the verdict is **REVISE**, Kirill's token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains
**unavailable**. It is not conditionally authorized on any X verdict for these
bytes. A corrected layer must receive fresh independent X/Y review.

This review authorizes no implementation, code/test edit, verifier allowlist
change, commit, activation, entropy, runtime construction, supervisor,
controller, worker, watchdog, adapter, middle child, endpoint, pipe, FIFO,
journal, spawn record, capability, lease, operation, output/capacity/custody
artifact, result manifest, E1/E2/E3 spend, Q attempt, Q/C object, scientific
work, datum, outcome, Proof, or claim movement.

No repository execution or runtime change occurred. No existing file was
modified; exactly this review file was created. T remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`.
