READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_FINAL_XY_CONFIRMATION

# Author closure — Officina supervisor/control-channel v2.1.10 architectural repair

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only, never an independent reviewer.**

**This closure is an untrusted self-assessment.** It is not an X-line review,
not a Y-line review, and not evidence. The same author line wrote v2.1 through
v2.1.10. `reviews/officina_supervisor_v2_1_authorship_note.md` records that this
line cannot serve as an independent reviewer of its own bytes. **Both v2.1.9
reviews are inputs to this repair, never support for it**; no conditional
authorization from any earlier round survives or transfers.

## Base, bytes, and method

Repository base: commit `e6862baa296a597cd2b37d2d5261e722363529c4`, verified to
descend from the required `ad3d0396f4a6fe9c14168062e0b66a24a8fe0df4`
(`git merge-base --is-ancestor`). The working tree was already dirty at
handover; every pre-existing tracked modification and untracked path was
preserved untouched.

Pinned inputs, independently recomputed and matching exactly:

```text
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
1970986325c75e8f4c2dd72e57e0640ae88b165f3556920e85cae7efc8cc93be  reviews/sol_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
f49dcbf9900c0d3fe2e45abbc28193d8b4b4c20c8640dfab508aff15dcc90984  reviews/opus_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
```

Digest of the artifact this closure accompanies:

```text
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
```

Method: static authoring only. Read-only file and `git` inspection, literal
search, `sha256sum`, and reasoning from pinned Linux/CPython interfaces. **No
repository code, test, probe, smoke command, fork/signal/subprocess experiment,
or Officina process ran. No implementation was written. No existing file,
verifier, manifest, runtime state, activation artifact, entropy, T/Q/C object,
datum, or claim was changed.**

## Verdict, and why it is `READY` rather than either blocked token

`READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_FINAL_XY_CONFIRMATION` states only that
**one** bit-exact, implementable route closes the union of both lines' findings
without a new author choice, and that the two deliverables exist. It is **not** a
confirmation and makes nothing signable.

- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_AUTHOR_CELL` — **not emitted.** Every
  delta is an engineering surface: a fourth executable root, `sys` added to the
  import allowlist, a module-scoped allowlist mechanism, four control-plane
  descriptor indices of exactly the class §Z declared for
  `T_CTRL_FD_LOW`/`T_CTRL_FD_HIGH`, one private argv token, one in-flight wire
  record, and one platform scope. **No resource value, timeout, K1 ceiling,
  E1/E2/E3 value, T band, scientific estimand, or policy cell is reached**; every
  deadline still reuses `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` and
  `T_SUPERVISOR_POLL_INTERVAL_NS`. A3/B1/C1/D1/K1 are untouched. Both v2.1.9
  reviewers independently reached the same author-cell conclusion for the
  repairs they demanded.
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_CONTRACT_CONFLICT` — **not emitted, and
  the test was applied deliberately.** This layer supersedes nine signed
  sentences (§V2110.9 rows 19–27), the sharpest being harness §9's "**No
  additional `scripts/*.py` entry point is introduced** … since adding one would
  require a reviewed amendment to the immutable-control file `verification.py`,
  which this contract does not authorize." That sentence **names its own
  prerequisite**, and this layer is that reviewed amendment, submitted for
  exactly the review it demands — the same governance pattern both lines
  accepted for the `signal` conjunct in v2.1.9. Every supersession is quoted,
  scoped, and paired with what it does **not** touch (the named
  `scripts/officina_t_process.py` counter-example remains forbidden; the
  watchdog keeps no argv surface; §Z3.2's signed role enum and §Z3.3's
  thirteen-element layout are byte-unchanged; `runtime.py`, `ledger.py`,
  `checkpoint.py`, `activation.py`, and the signed events/schemas/constants stay
  byte-unchanged). Reviewers should attack that scoping directly; if either line
  judges a supersession improperly scoped or the root addition unauthorized, the
  correct outcome is `REVISE`.

## What changed architecturally, in one paragraph

v2.1.9 tried to **prove** that the process running `generic_harness.py` had a
clean executor set, from `/proc/self/cmdline` plus a repository AST walk. Both
lines rejected that, and the prompt forbids repairing it with another
observation. **v2.1.10 withdraws that theorem entirely and constructs the clean
runtime instead.** A new fourth executable root,
`scripts/officina_process_control_bootstrap.py`, is `execve`'d by a fresh
interpreter with `-I -S -E -P` from an absolute, object-bound path with an empty
environment; it imports five stdlib modules and no project package; it binds the
genuine process primitives at module scope from that clean import state and
identity-validates them; and it contains the entire process-control machine —
lock, records, channels, first fork, stage M, every `wait`/`kill`/`signal`. It
never calls back into `generic_harness.py`, which is now the **contaminated
caller** and is assumed dirty. **The reaping proof becomes a process-boundary
proof**: `pid_mid` is a direct child of the bootstrap and of nothing else, and a
`wait` reaps only direct children, so no helper thread, at-fork handler,
monkeypatch, audit hook, or native extension in the caller can reach it —
regardless of what the caller contains.

## Literal v2.1.9 → v2.1.10 replacement index (summary; §V2110.0 is normative)

Everything not listed carries forward verbatim, including **§V219.3 in full**,
**§V218.2.2**, **§V218.3 in full**, **§V218.4.1–§V218.4.4**, **§V218.5 in
full**, **§V217.1 in full**, and **§V217.4 in full**.

| # | v2.1.9 / carried locus | Action |
|---|---|---|
| 1 | §V219.2.1's topology block, premises P-1/P-3, and its `execve` paragraph | replaced by §V2110.2 — the topology is constructed, not asserted of `generic_harness.py` |
| 2 | §V219.2.2's **executor-set theorem** in full, especially step 4, and its corollary | **deleted and withdrawn.** Replaced by §V2110.3.8 (a closure theorem whose premises follow from the construction) and §V2110.2.3 (the process-boundary proof). Not repaired — removed |
| 3 | §V219.2.3's `G-1` and "this is a KERNEL fact … names the program image actually loaded" | **deleted.** No layer henceforth treats argv as evidence of a clean image, a fresh `execve`, or the executor set |
| 4 | §V219.2.3's `G-2`/`G-3`/`G-4` | retained, re-sited into `P-c`/`P-d`/`P-g`, demoted from proof to corroboration inside a constructed clean process |
| 5 | §V219.2.4 `N-1`/`N-2`, §V219.2.5 `V-1`…`V-10` | retained in substance byte-for-byte, re-sited into the bootstrap |
| 6 | §V219.2.6's verifier-as-mechanism and `R-a`…`R-e` | replaced by §V2110.3.9's exact algorithm; the claim that today's verifier already proves a runtime theorem is **withdrawn as false** |
| 7 | §V219.2.7's entry table, §V219.2.8, §V219.2.9 | replaced by §V2110.3.7, §V2110.2.8, §V2110.7.2 |
| 8 | §V219.4.1's permitted-signal-surface block | replaced by §V2110.3.2/§V2110.3.9 — the bootstrap is the sole `signal` importer; `generic_harness.py` imports it **not at all** |
| 9 | §V219.4.2 rows 15–18 | retained, extended by §V2110.9 rows 19–27 |
| 10 | §V219.4.3's seven prose obligations | replaced by CHANGES 1–5 of §V2110.3.9 |
| 11 | §V219.3.1's result enum | extended by a sixth result, `STRUCTURAL_VIOLATION` |
| 12 | §V219.3.2/§V219.3.4 | retained, bound to the locally held genuine primitives, one column added |
| 13 | §V219.5.1's exclusion of source (a) "by §V219.2.2's corollary" | replaced by §V2110.4.5's non-circular process-boundary argument |
| 14 | §V219.6's `W-b`, its architecture paragraph, and its all-Linux claim | replaced by §V2110.6 — platform pinned to Linux x86_64 / CPython 3.12.3; MIPS explicitly unsupported |
| 15 | §V219.8 rows 241/242/243/249/250/252/253/255/264/265/270/271 | replaced by §V2110.7.4; rows 273–312 added |
| 16 | §V219.10, §V219.11 | replaced by §V2110.10, §V2110.11 |
| 17 | carried §W2.1, §W2.2, §V2.10, harness §9 (five sentences) | superseded by §V2110.9 rows 19–25, each quoted and scoped |

## One-to-one disposition of both lines' findings

| Finding | Line(s) | Disposition |
|---|---|---|
| **C219-1 / F1 (Critical)** — argv is not clean-exec or runtime-executor evidence; `.pth`, site/user customization, at-fork/audit/import/trace hooks, monkeypatching, retained callables and native extensions survive every v2.1.9 gate | Y + X | `G-1` deleted; the theorem withdrawn. The clean runtime is **constructed**: `-I -S -E -P` makes `site`, `.pth`, `sitecustomize`, `usercustomize`, `PYTHON*` env and path injection unable to run **at all**, and the flags are read back from `sys.flags`, not from argv. Five audited stdlib imports, no project package, primitives bound at module scope and identity-validated, and an eight-step preflight. **Independently**, the reaping proof is now a process boundary: `pid_mid` is a direct child of the bootstrap alone, so a `wait` in the caller can never reach it. Both counterexamples are replayed step-by-step in §V2110.7.2 and fail at their load-bearing step, **without any premise about the caller** |
| **M219-1 (Major)** — the current/future verifier does not establish a closed runtime executor or call-target theorem | Y | The claim is **withdrawn as false** (§V2110.9 row 27). §V2110.3.9 gives CHANGES 1–5: the fourth root; a module-scoped import allowlist (the bootstrap gets exactly `{os, sys, signal, time, fcntl}`, not a union); a closed ten-predicate AST grammar S-1…S-10 covering imports, prohibited syntax, the binding block, single-assignment, module-attribute escape, indirect call targets, forbidden symbols, wait forms, signal arguments, and finalizers; `generic_harness.py` losing `signal`; and a manifest gaining `root_source_sha256`. §V2110.3.8 states which premises are runtime readbacks, which are enumerations, which are statically decided **over one small file**, and which are constructions — and what is **not** claimed |
| **M219-2 / F2 (Major)** — `WAIT_ONE` totality and `B-CONTRADICTED` unreachability depend on the failed premise; unexpected callable results/exceptions are not total | Y + X | A sixth result, `STRUCTURAL_VIOLATION`, is evaluated **before** any errno mapping and covers wrong arity/type (`bool` rejected), negative or wrong positive pid, `(0, nonzero)`, out-of-range status, and **every** `BaseException` including `SystemExit`, `KeyboardInterrupt`, `GeneratorExit`, `MemoryError` and `RecursionError` — with **one** safe continuation at all five sites: never death, `CONTRADICTED` set irreversibly, no signal ever again, no record touched, the site's carried `CONTRADICTED_ECHILD` continuation. The same classifier covers `_kill` and `_fork`. `B-CONTRADICTED` unreachability is re-proved from direct-child ownership and the bootstrap's own two task readbacks, **citing no executor theorem and no property of the caller** |
| **m219-1 (Minor)** — 16 hex digits are false over the stated Linux scope; MIPS `_NSIG = 128` renders 32 digits | Y (stricter; X had judged it closed) | **Y governs.** The all-Linux claim is withdrawn. The bootstrap is pinned to `Linux x86_64, CPython 3.12.3`, checked at `P-a`/`P-b` via `os.uname()`, `sys.implementation`, `sys.version_info`. `d == 16` is justified **only inside that scope**, and `W-b` is evaluated only after `P-a`/`P-b` pass — so the false MIPS rejection cannot arise, because MIPS is refused **before any mask is parsed**. `signal.NSIG` is not added and no architecture is silently included |

## The ten required evidence items

1. **Literal replacement index** — §V2110.0, twenty-three rows; summarized above.
2. **One-to-one disposition of both lines' findings** — the table above; the
   union is closed and the stricter disposition is taken where the lines differ
   (m219-1).
3. **Exact process tree with direct-child/reaper ownership at every edge** —
   §V2110.2.2's diagram and its three-row edge table: caller → bootstrap →
   middle (`pid_mid`) → grandchild → exec'd supervisor role, with creator,
   direct-child relation, permitted waiter, and permitted signaller per edge.
4. **Byte-exact invocation, argv/environment policy, canonical request schema** —
   §V2110.2.1 (seven argv elements, `env={}`, `cwd="/"`, `close_fds=True`,
   `preexec_fn=None`, `shell=False`, object-bound exec target) and §V2110.2.5
   (six-field request, five-field reply, closed enums, no field able to carry a
   path, module, symbol, callable, primitive, fd, or timeout).
5. **Import / native-operation / callback / at-fork inventory before child
   creation** — §V2110.3.2's five-module table with native-vs-pure and
   transitive closure, including the disclosed `signal` → `functools` →
   `_thread` edge, and §V2110.3.3's eleven-row exhaustive operation list with
   an at-fork column and a task-creation column.
6. **Genuine-primitive binding and total return/exception tables** —
   §V2110.3.4 (the binding block, the positive identity test, the three-part
   no-rebinding rule) and §V2110.4.1–§V2110.4.2 (the six-result classifier and
   the full result × site product).
7. **Exact future verifier and manifest changes** — §V2110.3.9 CHANGES 1–5 plus
   the explicit runtime-preflight list, with a named fail-closed result per
   violation.
8. **Crash/cut matrix and replay of both counterexamples** — §V2110.7.1
   (nineteen added rows) and §V2110.7.2/§V2110.7.3 (the `.pth`/`os.fork`
   wrapper, the monkeypatched `os.waitpid`, and Y's Trace 6 wedge, each replayed
   step by step).
9. **Platform/mask table including x86_64 and the explicitly unsupported MIPS
   route** — §V2110.6.2's six-row table, with MIPS refused at `P-a` before any
   mask parse, and §V2110.6.3 on why this narrows only an engineering surface.
10. **No-regression and exact future edit surface** — §V2110.8 (twenty-two
    rows) and §V2110.10, which names the new bootstrap file and preserves the
    current untracked Cursor work byte-for-byte.

## Why the caller's contamination is now harmless — the load-bearing paragraph

`wait`, `waitpid`, `wait3`, `wait4`, and `waitid`, in **every** form including
the wildcard forms, reap only a direct child of the calling process's thread
group. `pid_mid` is created by the bootstrap's own `_fork` and is therefore a
direct child of the bootstrap and of nothing else. A wildcard wait issued by any
task of the caller ranges over the caller's children — which contains the
bootstrap and never `pid_mid`. Therefore no helper thread, at-fork handler,
monkeypatched `os.waitpid`, audit hook, or native extension in the caller can
reap `pid_mid`, **and this argument cites no property of the caller whatsoever**.
That is the exact structural difference from v2.1.9, whose theorem needed the
*same* process to be clean. The residual reaper set is the bootstrap's own task
set, which is a singleton by `execve` plus two independent kernel readbacks, in
a process where no user code could run and no callback can be dispatched.

## Weakest points, stated by the author against the author

Reviewers should attack these first rather than having to find them; they are
also carried verbatim in §V2110.11.

1. **The CPython 3.12.3 build is a pinned identity, not a hashed artifact.**
   `P-b` checks `implementation.name` and `version_info`, which a patched
   interpreter could satisfy while behaving differently. The bootstrap cannot
   hash its own interpreter without `hashlib`, which was deliberately excluded
   to keep OpenSSL and its native surface out of the import closure. This is the
   sharpest remaining boundary between "verified at run time" and "reviewed
   once", and it is a real limit on what the construction proves.
2. **The five-module closure includes `_thread`,** via
   `signal` → `functools` → `from _thread import RLock`. No task is created and
   every task-creating symbol is syntactically unreachable under S-7, but the
   closure is not free of threading machinery and the argument is about calls,
   not imports.
3. **The bootstrap cannot attest the reviewed-ness of the role image it
   `execve`s.** The package root arrives as a caller-opened directory
   descriptor. The bootstrap guarantees process-control custody, not the code
   provenance of the supervisor. A hostile caller can make it launch a
   supervisor of the caller's choosing — while still being unable to corrupt
   `pid_mid`'s custody, force a false death proof, or cause a wrong-PID signal.
4. **The supervisor process is not isolated.** §W2.5's own `Popen` +
   `waitpid(WUNTRACED)` handshake and the in-process watchdog fork run in a
   contaminated interpreter. No finding raised it and it is outside C219-1's
   scope, but it is the **same class** of defect, and this layer explicitly does
   not claim to have repaired it. If either line judges that the scope note is
   an evasion rather than an honest boundary, that is a legitimate `REVISE`.
5. **`P-e`'s single wildcard wait is a real exception** to the no-wildcard rule.
   It is pre-fork, its only accepted outcome is `ECHILD`, and it refuses on
   anything else — but in the case where it returns it has already reaped an
   inherited child, and that side effect is stated rather than avoided.
6. **`start_new_session=False`** keeps the bootstrap interruptible by an
   operator's terminal `SIGINT`, which also means the caller's process group can
   be signalled as a unit by a third party. Both directions are stated.
7. **The platform pin is narrow to the point of inconvenience** — one
   architecture, one CPython patch version. Any other host refuses before fork.
   That is the intended fail-closed behaviour and a real operational constraint.
8. **The amendment surface is the largest of any layer in this chain**: a fourth
   executable root, a second allowlist member, a new verifier mechanism, four
   descriptor constants, a re-introduced private argv surface, a new wire
   record, and a platform scope. Each is named and scoped in §V2110.9, but the
   aggregate is a fair thing to challenge on governance grounds alone.

## Confirmation questions

§V2110.12 carries **three** bounded questions per line, focused as required:
X-Q1/Y-Q1 on clean construction and runtime closure (the isolation flags, the
import closure, the operation inventory, the primitive binding, and above all
the process-boundary argument); X-Q2/Y-Q2 on primitive, wait, and `B` totality
(the structural classifier over returned objects and raised objects, its single
continuation, W-5 with a middle stopped between `m8` and `m9`, and the
non-circular `B-CONTRADICTED` exclusion); X-Q3/Y-Q3 on root, verifier, and
platform containment (the nine supersessions, the exactness of CHANGES 1–5 and
S-1…S-10, and the MIPS/x86_64 platform table). Both lines must recompute the
digest of the v2.1.10 bytes and of every governing hash, and must treat this
closure and both v2.1.9 reviews as untrusted inputs. Verdict line 1 is exactly
`CONFIRM_OFFICINA_SUPERVISOR_V2_1_10_X` / `..._Y` or
`REVISE_OFFICINA_SUPERVISOR_V2_1_10`.

## Custody, authorization boundary, and programme state

Exactly **two** files were created by this work, and nothing else in the
repository was touched:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_closure.md` (this file)

`scripts/officina_process_control_bootstrap.py` is **specified, not created**;
it does not exist. `src/philosophia/officina/verification.py` is unmodified —
digest `327b1bb2…`, recorded in the correction's hash block — and the production
call-graph manifest does not exist. No prior artifact, contract, signature,
review, prompt, code file, verifier, test file, runtime tree, Cursor-dirty file,
or unrelated change was edited, staged, or committed; the untracked
`src/philosophia/officina/generic_harness.py`,
`tests/test_officina_generic_harness.py`, `essay/OUTLINE.md`, and the modified
`accounting.py`, `test_officina_accounting.py`, and review/prompt files are
preserved byte-for-byte.

Confirmed explicitly, as required: **no execution of any kind — no
implementation, test run, probe, smoke command, fork/signal/subprocess
experiment, or Officina process — and no entropy, activation, T process, spend,
Q/C work, datum, outcome, or claim movement.** T remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`; no artifact was produced.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not authorized and
remains unavailable**. Both independent lines revised v2.1.9, so no conditional
authorization survives or transfers. The token becomes available only if a fresh
independent X-line review **and** a fresh independent Y-line review both confirm
the **identical v2.1.10 bytes** whose digest is `2b4f9cad…`. This closure
authorizes no implementation, no code, test, verifier, manifest, or allowlist
change, no commit, no host change, no T activation, no entropy, no E1/E2/E3
spend, no Q/C work, no capability, lease, operation, capacity artifact, custody
disposition, result manifest, world, learner, candidate, Q attempt, datum,
outcome, Proof, or claim movement, and no later gate.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`.
