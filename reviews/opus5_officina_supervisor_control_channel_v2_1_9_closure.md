READY_FOR_OFFICINA_SUPERVISOR_V2_1_9_FINAL_XY_CONFIRMATION

# Author closure — Officina supervisor/control-channel v2.1.9 bounded repair

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only.**

**This closure is an untrusted self-assessment.** It is not an X-line review,
not a Y-line review, and not evidence. The same author line wrote v2.1 through
v2.1.9. `reviews/officina_supervisor_v2_1_authorship_note.md` records that this
line cannot serve as an independent reviewer of its own bytes. **Neither v2.1.8
review is author support for these new bytes**: the X confirmation was of
v2.1.8's bytes and was conditional on a Y confirmation of the identical bytes,
which did not occur; the Y `REVISE` is the governing verdict and is the input to
this repair, not an endorsement of it.

## Base, bytes, and method

Repository base: commit `0737f3de8cfa1fde0f75351c6d326f3acd40b3c9`, verified to
descend from the required `64cf100df585db40b347ada3b21a0b692d250d3b`
(`git merge-base --is-ancestor`). The working tree was already dirty at
handover; every pre-existing tracked modification and untracked path was
preserved untouched.

Pinned inputs, independently recomputed and matching exactly:

```text
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
663184378fc6fa48c5d83e96cf659d2d9eb58f67a18fd8c7ba0efcb528caea34  reviews/sol_officina_supervisor_control_channel_v2_1_8_final_confirmation.md
e879b39cf6e22c93bcf309ed4a15a7a1f56e00fbcc17fd8cfc2398b04aec099a  reviews/opus_officina_supervisor_control_channel_v2_1_8_final_confirmation.md
```

Digest of the artifact this closure accompanies:

```text
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
```

Method: static authoring only. Read-only file and `git` inspection, literal
search, `sha256sum`, and reasoning from pinned Linux/CPython interfaces. **No
repository code, test, probe, smoke command, signal/fork/subprocess experiment,
or Officina process ran. No implementation was written. No verifier, runtime
state, activation artifact, entropy, T/Q/C object, datum, or existing document
was changed.**

## Verdict and why it is `READY`, not either blocked token

`READY_FOR_OFFICINA_SUPERVISOR_V2_1_9_FINAL_XY_CONFIRMATION` states only that
one bit-exact, implementable route closes all five governing findings without a
new author choice, and that the two deliverables exist. It is **not** a
confirmation and makes nothing signable.

- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_9_AUTHOR_CELL` — **not emitted, and the
  test for it was applied deliberately.** R2 required a `BLOCKED` verdict if a
  new numeric constant or a scientific/resource choice proved unavoidable. None
  did: every deadline in the shared wait automaton reuses
  `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` paced at `T_SUPERVISOR_POLL_INTERVAL_NS`,
  both already signed; W-5 needs no deadline at all; the topology gate,
  reset pass, and mask rule introduce no numeric value; and `int(signal.SIGCHLD)`
  and the `d == 16` rendering width are pinned platform facts, not chosen
  values. No policy cell A3/B1/C1/D1/K1 is reopened, and both v2.1.8 reviewers
  independently reached the same author-cell conclusion.
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_9_CONTRACT_CONFLICT` — **not emitted,
  because the conflict M218-2 identified is resolved rather than inherited.**
  v2.1.8 genuinely was unimplementable: it required `signal` in the module
  implementing `c1`–`c18` while forbidding it in the generic harness, and
  §V2.10/§Z3.3/harness §9 put `c1`–`c18` in `generic_harness.py`. v2.1.9 adopts
  the smaller Y repair — the sole root **is** the sole importer — and
  explicitly supersedes each conflicting sentence with a stated scope
  (§V219.4.2 rows 15–18). Containment moves from file granularity, which is
  unsatisfiable in a one-module program, to name-and-call-site granularity,
  which is strictly finer and statically checkable. Reviewers should attack that
  resolution directly; if either line judges the supersessions improperly
  scoped, the correct outcome is `REVISE`.

## The X/Y disagreement, resolved explicitly

Recorded at length in §V219.1 and summarized here because the prompt requires it
and because it determined the shape of the repair.

**Why the X confirmation was reasonable.** It independently re-derived every
*disposition-reset* fact — `PyOS_setsig`'s single `sigaction` with
`sa_handler = SIG_DFL`, an empty mask and `SA_ONSTACK`; the `execve`/`fork`
provenance asymmetry; the `SigIgn`/`SigCgt` readback and its `SA_NOCLDWAIT`
blind spot; the pre-fork placement; the per-attempt reset — and those facts do
close the two inherited v2.1.7 findings, which were about dispositions. The Y
line agreed with every one of them. On the reaper half the X line applied the
criterion "does the contract forbid every wildcard reaper in the CLI, and is
that statically testable?", answered yes, and stopped.

**Why it was insufficient.** The correct criterion is "can a wildcard reaper
**exist in this process** at the instant of the fork, whatever the contract says
about our source?" §V218.2.6 was a rule about what Officina source may contain;
it never constrained inherited host state, and v2.1.8 permitted an in-process
entry whose only pinned property was main-thread eligibility — which implies
neither single-taskness nor exclusive wait ownership. The same unestablished
premise propagated into M218-3, because the acceptability of the
`B-CONTRADICTED` sink was argued *from* it. Independently, the X line judged
W-2…W-5 sound because each is a targeted `waitpid`, but targeting is not
totality; and it read the importer rule as governing two components when
§V2.10, §Z3.3 and harness §9 place them in the same file.

**Consequence for this layer.** The repair starts at C218-1 and lets M218-3
follow from it. **Nothing in v2.1.9 is defended by appeal to the X verdict**,
and every Y counterexample is closed mechanically rather than argued away.

## Literal v2.1.8 → v2.1.9 replacement index (summary; §V219.0 is normative)

Everything not listed carries forward verbatim, including **§V218.2.2** (the
`SIGCHLD` full-disposition replacement and its whole analysis), **§V218.3 in
full**, **§V218.4.1–§V218.4.4**, **§V218.5 in full**, **§V217.1 in full**, and
**§V217.4 in full**.

| # | v2.1.8 / carried locus | Action |
|---|---|---|
| 1 | §V218.2.1's `c3n` placement block | extended by §V219.2.3 — new step `c3t` immediately precedes `c3n` |
| 2 | §V218.2.2's `NORMALIZE_REAPING_STATE` | extended by §V219.2.4 — reset pass `N-1` runs first; the `SIGCHLD` call `N-2` and its analysis are unchanged |
| 3 | §V218.2.3's `V1`–`V7`, in particular `V3`'s "non-empty string of hexadecimal digits" and `V4`'s conversion | replaced by §V219.6 (grammar + width before conversion) and §V219.2.5 (`V-1`…`V-10` post-write re-verification) |
| 4 | §V218.2.4's main-thread sentence | replaced by §V219.2.1–§V219.2.3; main-thread eligibility is retained but is no longer offered as evidence of single-taskness or exclusive wait ownership |
| 5 | §V218.2.6's SOLE-REAPER CONTRACT paragraph | replaced by §V219.2.2 (executor-set theorem) and §V219.2.6 (verifier-enforced source/call-graph rule) |
| 6 | §V218.2.6's five-row wait table and its mutual-exclusivity assertion | replaced by §V219.3 — one classifier, five instantiation tables, and a *proof* of mutual exclusivity |
| 7 | §V218.1.2's PERMITTED SIGNAL SURFACE block | replaced by §V219.4.1 — sole root is the sole importer |
| 8 | §V218.1.3's §S7 obligation | replaced by §V219.4.3 — seven single-valued verifier obligations |
| 9 | §V218.1.4's row 1 and third carried consequence | extended by §V219.4.2 rows 15–18 |
| 10 | §V218.4.2's `B` block | replaced by §V219.5.2 — `B-OWNED` unchanged in substance, `B-CONTRADICTED` reclassified |
| 11 | §V218.4.5's residual 3 | replaced by §V219.5.3 |
| 12 | §V218.4.4's `B` row | extended by §V219.5.4 — `s5` named as a consequence, explicitly not a resolver |
| 13 | §V218.6's `c3n` and `B` rows | replaced/extended by §V219.7.3 |
| 14 | §V218.7 rows 219, 220, 223, 224, 233, 234 | replaced; rows 241–272 added |
| 15 | §V218.9's determinacy and compatibility paragraphs | replaced by §V219.11 |
| 16 | carried §V2.10's "Frozen files (byte-unchanged): … `verification.py` …" and "Allowlist delta: **none**." | replaced by §V219.4.2 and §V219.10 |
| 17 | carried signed harness §9's "uses no `signal`/`threading`/`multiprocessing`/backend import" | **only the `signal` conjunct** superseded by §V219.4.2 row 15 |

## One-to-one disposition of the five governing findings

| Finding | Repair | Where |
|---|---|---|
| **C218-1 (Critical)** — inherited same-process thread can wildcard-reap between identity observation and signal; the stale `OWNED` label can then signal a reused PID | One supported production topology is pinned: sole-root program image, single task, no catching disposition, normalized `SIGCHLD`. New step `c3t` verifies the first three from the kernel (`/proc/self/cmdline`, `/proc/self/task`, `Threads:`), `c3n` gains a reset pass that clears every caught signal using numbers **derived from the kernel's own `SigCgt` mask** (no new `signal` member), and `V-4` re-reads `SigCgt == 0`. The executor-set theorem then proves that the task set is a singleton and stays one: a task joins a thread group only by `clone(CLONE_THREAD)` from a task already in it; the only such task is ours; the only asynchronous entry into a task is a signal handler, and none exists; every other callback class is synchronous and therefore inside the reachable set the **signed verifier** already walks, where `threading`/`_thread`/`multiprocessing`/`concurrent`/`asyncio`/`ctypes`/`sys`/`atexit` are rejected imports. The prohibition becomes a theorem. | §V219.2 |
| **M218-1 (Major)** — W-2…W-5 lack total result automata | One shared classifier `WAIT_ONE` over `pid_mid` / `(0,0)` / `EINTR` before and at the deadline / `ECHILD` / every other `OSError` / invocation after `REAPED` / the impossibility of a stop-or-continue status under `WNOHANG` without `WUNTRACED`, instantiated for all five sites with exact entry condition, existing-constant deadline, signal policy, transition, record cleanup or handoff, lock behaviour, and continuation — plus a full result × site product table and a *proof* of per-attempt mutual exclusivity. Only a positive targeted return sets `REAPED`; no site runs after `REAPED`; no `ECHILD` means death. | §V219.3 |
| **M218-2 (Major)** — sole-root and permitted-importer rules simultaneously require and forbid `signal` in `generic_harness.py` | The smaller Y repair is adopted: `generic_harness.py` is the sole executable root **and** the exact permitted importer. Containment moves to name-and-call-site granularity — four permitted names, two permitted call sites, `SIG_DFL`-only arguments — which is satisfiable inside a one-module program. Four sentences are superseded with stated scope: harness §9's `signal` conjunct only; §V2.10's frozen list, `verification.py` only, by one added string; §V2.10's "Allowlist delta: none"; and v2.1.8's unimplementable forbidden-importer row. No second module, dynamic import, handler, extra API, importer, dependency, executable root, or call-graph edge. | §V219.4 |
| **M218-3 (Major)** — reachable `B-CONTRADICTED` has no lawful progress action | With C218-1 closed, each of the four contradiction sources is shown to require one of exactly three stated failures: a platform contradiction (the pinned `PyOS_setsig` or Linux auto-reap semantics not holding), a kernel contradiction (`/proc` reporting a parentage or start identity inconsistent with our own `fork` return), or an implementation-contract contradiction (a build violating the verifier-enforced allowlist or call-graph rules). `B-CONTRADICTED` is therefore **unreachable in every supported execution** and is reclassified as a non-returning safety sink outside supported history, with a proof that it is not a liveness route. `s5` is named as a *consequence* and explicitly **not** a resolver; no operator notice or indefinite retry is offered as one; no handle is deleted and no signal is authorized. `B-OWNED` is unchanged in substance and remains the named A3/host-fault residual the Y line accepted. | §V219.5 |
| **m218-1 (Minor)** — short `/proc` signal masks pass as verified | `MASK_FIELD` fixes the grammar (single occurrence, mandatory whitespace, maximal hex run to end-of-line, no `0x` prefix, no sign, no internal whitespace, no trailing byte) and imposes a two-conjunct width rule **before** any conversion: `4 * d >= int(signal.SIGCHLD)` (architecture-independent, mandatory) **and** `d == 16` (the pinned Linux `render_sigset_t` width). Empty, one-digit, four-digit, thirteen-digit, and twenty-digit masks all route to `VERIFY_INCONCLUSIVE`; no fork. An eleven-row decision table and rows 220/270 pin every case. | §V219.6 |

## The ten totality and regression obligations

1. **Literal replacement index** — §V219.0, seventeen rows plus the two carried
   supersession rows; summarized above.
2. **One-to-one disposition** — the table immediately above; §V219.1 records the
   X/Y disagreement separately so no finding is answered by appeal to a verdict.
3. **Supported-entry topology table and complete pre-fork state machine** —
   §V219.2.1 (P-1…P-4), §V219.2.3 (`TOPOLOGY_GATE` `G-1`…`G-5`), §V219.2.4
   (`N-1`, `N-2`), §V219.2.5 (`V-1`…`V-10`), §V219.2.7 (seven entry points, each
   with its reach-`c4` verdict). Every non-`OK` result takes the carried
   `PRE_FORK_FAIL_CLOSED` body; **no fork occurs on any of them**.
4. **Shared wait classifier plus five site instantiations** — §V219.3.1,
   §V219.3.2 (five tables), §V219.3.3 (exclusivity proof), §V219.3.4 (the full
   result × site product).
5. **Signal/import/call-graph allowlist table** — §V219.4.1's permitted-surface
   block, §V219.2.6's vector table and rules `R-a`…`R-e`, §V219.4.3's seven
   verifier obligations.
6. **Ownership × identity × wait × terminal product check** — §V219.7.1, five
   rows over the three ownership states × capture state, each listing the
   reachable identity rows, reachable wait results, authorized signals, and
   terminal.
7. **Schedules** — §V219.7.2: inherited thread with a wildcard wait; the
   enumeration-to-fork window; W-2 `EINTR`-then-`(0,0)`; W-3 arbitrary errno;
   W-4 `ECHILD` against P3; the W-5 `m8`-before-`m9` race; PID reuse; short
   mask; `T2` zombie; `B-CONTRADICTED`.
8. **Static future tests distinguishing the repair from v2.1.8** — §V219.8 rows
   241–272, with row **271** dedicated to exactly that discrimination: the
   C218-1 replay, the W-5 race, the short-mask case, and the sole-root importer
   check must **fail** against a v2.1.8-conforming implementation and **pass**
   against a v2.1.9-conforming one.
9. **No-regression over every carried signed surface** — §V219.9, twenty-two
   rows, including all repairs both lines accepted and the explicit statement
   that the topology repair proves nothing about filesystem exclusion.
10. **Exact code and control files a later implementation review may change** —
    §V219.10: `generic_harness.py`, `verification.py` (one added string plus the
    containment probe), and `tests/test_officina_generic_harness.py`. Everything
    else stays byte-unchanged, and the current untracked Cursor work and the
    frozen runtime surfaces are explicitly preserved.

## The counterexample replay, in full

The Y line's six-step schedule, under the chosen topology (§V219.2.9):

1. *An in-process host with a pre-existing helper thread doing
   `waitpid(-1, WNOHANG)` invokes the CLI on the main thread.* — cannot reach
   `c4`. `G-2` lists ≥2 entries in `/proc/self/task` and `G-3` reads
   `Threads: ≥2`; either alone refuses. If the host is single-tasked but is not
   the sole-root image, `G-1` refuses on a kernel-established `cmdline`.
2. *`c3n` normalizes; `c4` establishes `OWNED`.* — reached only under P-1…P-4.
3. *`M2` reads a matching identity.* — unchanged.
4. *The child exits and the helper reaps it.* — **impossible**: the executor set
   is a singleton and no wildcard wait exists anywhere in the reachable program,
   so no entity but this task can reap `pid_mid`; the child becomes and stays
   `EXIT_ZOMBIE`.
5. *The PID is reused.* — **impossible**: Linux cannot reassign a pid held by a
   task in any state, and the zombie holds it until this route's own targeted
   `waitpid` returns it.
6. *`M3` signals the reused process.* — **unreachable.**

**The proof depends on no detector.** Steps 4–6 are excluded before any signal
is sent, not by `ECHILD`, `ESRCH`, or a `ppid` mismatch observed afterwards.
Those three detectors are retained unchanged as a second line against the one
unverifiable platform premise, and §V219.5 states exactly what their firing now
means: not a route, but evidence that the process is executing outside its own
premises.

## Weakest points of this layer, stated by its own author

Recorded so reviewers attack them first rather than having to find them.

1. **`SA_NOCLDWAIT` remains written but not read back.** Linux exposes the flag
   nowhere readable from `os`, and `ctypes` stays outside the allowlist. This is
   carried unchanged from v2.1.8, where both lines examined and accepted it, but
   it is still the one premise resting on the semantics of a write. It is now
   the *only* stated route into `B-CONTRADICTED` that is not a kernel or build
   contradiction, so its weight has, if anything, increased.
2. **The executor-set theorem's step 2 is a claim about CPython's execution
   model**, not a kernel fact: that finalizers, weakref callbacks, trace and
   profile functions, audit hooks, import hooks, and `atexit` handlers are all
   invoked synchronously from the program's own control flow, so that signal
   handlers are the only asynchronous entry. If a reviewer can name an
   asynchronous entry I have missed, the theorem's conclusion does not follow
   and the finding is real.
3. **`G-1` treats `/proc/self/cmdline` as evidence of the loaded program
   image.** It is established by `execve` and inherited unchanged by `fork`, so
   a process that exec'd the sole root and then forked into the bootstrap would
   pass `G-1`. I argue this is harmless because the program in that child *is*
   the sole root and therefore governed by the verifier and by the call-graph
   rules, and because the child of a single-tasked process is single-tasked.
   Reviewers should test that argument rather than accept it.
4. **Resetting every caught signal removes `KeyboardInterrupt` from the CLI
   process.** A delivered `SIGINT` now takes its default action and terminates
   the bootstrap. I judge that safer for a lock-holding process — death releases
   the descriptors and the lock reference by kernel action and removes no
   record — but it is a real behavioural change, it is not undone afterwards,
   and it is only acceptable because P-1 makes the process *be* the CLI rather
   than a host.
5. **`W-b`'s `d == 16` is a pinned-platform rendering claim.** It is the
   stricter conjunct and it fails closed on any kernel that renders sigsets
   differently, but it is a fact about `render_sigset_t` that reviewers must
   verify rather than take from this document.
6. **The containment rule is now finer than file granularity**, which makes it
   more expressive but also harder to enforce: obligations 4–7 of §V219.4.3 are
   AST-level assertions over a single large module rather than a per-file import
   check. If a reviewer judges them not mechanically single-valued, M218-2 is
   not closed.

## Confirmation questions

§V219.12 carries **three** bounded questions per line, no more, concentrated as
required on R1, R2/R4, and R3/R5: X-Q1/Y-Q1 attack the executor-set theorem and
the counterexample replay premise by premise; X-Q2/Y-Q2 attack `WAIT_ONE`'s
totality at all five sites — including the `m8`-before-`m9` race and W-4's
`ECHILD` against P3 — and then the sink classification and the explicit
non-resolver status of `s5`; X-Q3/Y-Q3 attack the sole-root importer topology,
the scope of the four supersessions, the seven verifier obligations, and the
mask width rule. Both lines must recompute the digest of the v2.1.9 bytes and of
every governing hash, and must treat this closure and both v2.1.8 reviews as
untrusted inputs. Verdict line 1 is exactly
`CONFIRM_OFFICINA_SUPERVISOR_V2_1_9_X` / `..._Y` or
`REVISE_OFFICINA_SUPERVISOR_V2_1_9`.

## Custody, authorization boundary, and programme state

Exactly **two** files were created by this work, and nothing else in the
repository was touched:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_9_closure.md` (this file)

No prior artifact, contract, signature, review, prompt, code file, verifier,
test file, runtime tree, Cursor-dirty file, or unrelated change was edited,
staged, or committed. In particular `src/philosophia/officina/verification.py`
is unmodified — its digest `327b1bb2…` is recorded in the correction's hash
block — and the untracked `src/philosophia/officina/generic_harness.py`,
`tests/test_officina_generic_harness.py`, `essay/OUTLINE.md`, and the modified
`accounting.py`, `test_officina_accounting.py`, and review/prompt files are
preserved byte-for-byte.

Confirmed explicitly, as required: **no implementation, no test execution, no
signal/fork/subprocess experiment, no probe, no smoke command, no Officina
process, no entropy, no activation, no T process, no spend, no Q/C work, no
datum, no outcome, and no claim movement.** T remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`; no artifact was produced.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not authorized and
remains unavailable**. The v2.1.8 X confirmation was conditional on a Y
confirmation of the identical v2.1.8 bytes; that condition failed, so no
conditional authorization survives and none transfers to v2.1.9. The token
becomes available only if a fresh independent X-line review **and** a fresh
independent Y-line review both confirm the **identical v2.1.9 bytes** whose
digest is `1468c9ab…`. This closure authorizes no implementation, no code, test,
or verifier change, no allowlist edit, no commit, no host change, no T
activation, no entropy, no E1/E2/E3 spend, no Q/C work, no capability, lease,
operation, capacity artifact, custody disposition, result manifest, world,
learner, candidate, Q attempt, datum, outcome, Proof, or claim movement, and no
later gate.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`.
