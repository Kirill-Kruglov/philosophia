READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_1_FINAL_XY_CONFIRMATION

# Author closure — Officina supervisor/control-channel v2.1.10.1 pre-review correction

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only, never an independent reviewer.**

**This closure is an untrusted self-assessment.** It is not an X-line review,
not a Y-line review, and not evidence. The same author line wrote v2.1 through
v2.1.10.1. `reviews/officina_supervisor_v2_1_authorship_note.md` records that
this line cannot serve as an independent reviewer of its own bytes.

**No independent review of v2.1.10 was requested, and none has occurred.** This
layer is a **pre-review author correction**: seven literal and architectural
defects in v2.1.10 that the author found by re-reading its own bytes, corrected
before any reviewer time is spent. v2.1.10 is not edited; it stands as immutable
evidence of what was wrong.

## Base, bytes, and method

Repository base: commit `251c51eae495fed488c13dc2a46b840a4a8df2d2`, verified to
descend from the required `f67256a489ffcecae7caece628529baae0c11c77`
(`git merge-base --is-ancestor`). The working tree was already dirty at
handover; every pre-existing tracked modification and untracked path was
preserved untouched.

Pinned inputs, independently recomputed and matching exactly:

```text
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
4cc19fc914f5908f069cb7b8aa09297dece424943f8a876974105e575d09c47d  reviews/opus5_officina_supervisor_control_channel_v2_1_10_closure.md
```

Digest of the artifact this closure accompanies:

```text
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
```

Method: static authoring only. Read-only file and `git` inspection, literal
search, `sha256sum`, and reasoning from pinned Linux/CPython interfaces. **No
code, test, probe, smoke command, spawn/fork/signal experiment, or Officina
process ran. No implementation was written. No existing file, implementation,
verifier, activation artifact, entropy, T/Q/C object, datum, claim, or prior
document was modified.**

## Verdict, and why it is `READY` rather than either blocked token

`READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_1_FINAL_XY_CONFIRMATION` states only that
all seven blockers are now single-valued and implementable, and that the two
deliverables exist. It is **not** a confirmation and makes nothing signable. The
bytes that must be reviewed are **v2.1.10 as corrected by v2.1.10.1**.

- `BLOCKED_..._AUTHOR_CELL` — **not emitted.** Every delta is an engineering
  surface: an import set, an identity table, two control-plane descriptor
  indices (`T_PCB_FD_SOURCE`, `T_PCB_FD_INTERPRETER`, of exactly the §Z-declared
  `T_CTRL_FD_LOW`/`T_CTRL_FD_HIGH` class), a launch mechanism, two provenance
  checks, a handle-based control protocol, one further private argv token, and
  a blocked-mask check. **No resource value, timeout, K1 ceiling, E1/E2/E3
  value, T band, scientific estimand, or policy cell is reached.** A3/B1/C1/D1/K1
  are untouched.
- `BLOCKED_..._CONTRACT_CONFLICT` — **not emitted.** Nine further signed
  sentences are superseded (§V21101.10 rows 28–36), each quoted, each scoped,
  and each paired with the property it does **not** touch. The largest, row 36
  (the watchdog's in-process fork), is a *strengthening* of C1's own argument:
  an `execve`'d watchdog has no capability in its address space **by
  construction** rather than by an ordering argument. Reviewers should attack
  that scoping; if either line judges a supersession improperly scoped — in
  particular B6's — the correct outcome is `REVISE`.

## One-to-one disposition of the seven blockers

| Blocker | Resolution | Where |
|---|---|---|
| **B1** — contradictory import inventory and an invalid identity rule | v2.1.10 said both "four modules, `fcntl` excluded" and "five modules including `fcntl`". **Resolved to exactly `{os, sys, _signal, time, fcntl}`**, using the **built-in `_signal`** rather than the Python `signal` wrapper. This deletes `functools`, `enum`, `_thread`, `reprlib`, `collections`, `operator` and `types` from the transitive closure entirely — v2.1.10's `_thread` note and its accompanying weakest-point are **withdrawn, not mitigated** — and it makes the signal primitives genuine built-ins. v2.1.10's single universal predicate `type(f).__name__ == "builtin_function_or_method"` **would have rejected the genuine `signal.signal`**, which is a pure-Python wrapper function; it is replaced by an exact per-primitive table with three kinds (built-in callable, integer constant, string constant), a `type(len)` object-identity anchor, and a per-row `__self__`/`__qualname__`/value requirement. Every genuine binding passes; every stated substitution — Python function, `partial`, bound method, callable instance, foreign-module builtin, wrong qualname, wrong constant — fails | §V21101.1 |
| **B2** — the script path is not object-bound | The claim "so the exec target is the SAME inode the caller opened" is **deleted as false**: `readlink` returns a pathname and the interpreter re-walks it. Replaced by a real fd-bound launch — the source stays open on `T_PCB_FD_SOURCE` and the interpreter receives the **literal** `"/proc/self/fd/7"`; the interpreter binary likewise stays open on `T_PCB_FD_INTERPRETER` and the spawn target is the literal `"/proc/self/fd/8"`. `sys.executable` is **no longer called "kernel supplied"** and is used for nothing. New preflight `P-s1`–`P-s6` `fstat`s both descriptors and proves regular-file, non-group/other-writable, read-only status, recording `SOURCE_IDENTITY` and `INTERPRETER_IDENTITY`. A twelve-row table covers unlink, rename, replace-at-name, truncate, hardlink, symlink and every spawn cut. `readlink` is added to the verifier's forbidden-symbol list so the defect cannot recur | §V21101.2 |
| **B3** — impossible `Popen`/pre-exec descriptor mapping | `subprocess.Popen` has no general fd-remapping argument, and `cwd` is not expressible by `os.posix_spawn`, so v2.1.10's launch block was unimplementable. Replaced by `os.posix_spawn` with a two-phase mapping: a deterministic **hoist** moving all six logical descriptors above 8 (postcondition: pairwise distinct, all `>= 9`), then **twelve ordered file actions** — six `DUP2` onto 3…8, then six `CLOSE`. Collision-freedom follows from the disjointness of the source range `>= 9` and the destination range `3…8`; `POSIX_SPAWN_DUP2` clears close-on-exec on the destination, which is why no `set_inheritable` is needed. Constants are validated by set-equality and pairwise distinctness against the review record. `cwd="/"` is deleted and replaced by a bootstrap-side `_chdir("/")`, with the reason the inherited cwd was already irrelevant: every operation is `dir_fd`-relative, on an open descriptor, or an absolute `/proc` name | §V21101.3 |
| **B4** — dirty-caller launcher authority | The claim is narrowed to a **disjunction**: either the caller constructs exactly the isolated process through genuine primitives, **or no authorized bootstrap comes into existence**. A seven-row table shows which caller behaviour lands in which disjunct. Launcher primitives are bound and identity-checked with the same table, and any mismatch refuses **before** the spawn; no `subprocess`, `shutil`, `pathlib` or `tempfile` is used on the launch path. **These checks are explicitly stated to be diagnostic, not the safety mechanism** — a fully hostile caller can defeat them, which is precisely why the property is a disjunction — and all load-bearing safety is the bootstrap's own preflight, executed where the caller cannot reach. The three counterexamples (`.pth`/`sitecustomize`, `register_at_fork`, monkeypatched `os.fork`/`os.waitpid`) are replayed and each fails at a named step | §V21101.4 |
| **B5** — package/role provenance | "A hostile caller can make the bootstrap launch a supervisor of the caller's choosing" is **withdrawn as an accepted route.** `P-p1`–`P-p3` open the canonical bootstrap path under fd 6 with `O_NOFOLLOW` and require its `(st_dev, st_ino)` to equal the executing source's, so fd 6 and fd 7 must be the same tree. `P-p4`–`P-p6` resolve the role image object-bound, and role-side `R-1` re-verifies `(st_dev, st_ino)` against its own loaded module before any behaviour — closing the window between the bootstrap's check and the interpreter's `-m` resolution. The byte-provenance division is stated exactly: **object identity at run time, byte provenance by the signed manifest's `root_source_sha256` at deploy time**, with the limit stated without softening ("a deployment that ships unverified bytes gets no run-time rescue"), and with the reason `hashlib` was excluded and an in-root SHA-256 rejected. Path components *below* an object-bound directory fd are handed explicitly to the **signed A3 same-UID residual**, unchanged and not claimed closed | §V21101.5 |
| **B6** — the supervisor retains the same defect class | Route 2 is ruled **unavailable by inspection**: a four-row table shows the supervisor issues `Popen`, `waitpid`, `fork`, `kill` and `killpg` on result-bearing paths (§W2.5 claims and leases, §W2.1's watchdog, §W2.4/§U2.5 death proofs, §W3.3 freeze). **Route 1 is taken.** The reviewed bootstrap does not exit; it becomes the **Process-Control Server**, performing every child creation, signal, wait, and the watchdog creation for the whole generation. **The supervisor is given opaque handles and is never told a PID** — its wire vocabulary contains no pid field, so it *cannot express* a signal to a numeric pid, and PID-reuse sensitivity is removed **structurally**. Nine operations, five handle-table invariants that each carry a signed rule forward, a role-side descriptor table, and a complete call/ownership table. The amendment is bounded by the principle **"relocate the primitive, preserve the semantics"**: §W2.5's self-stop handshake, §Z3.3's argv layout, §W2.4's discovery predicate, §W3.3's freeze, §U2.5's tier rules and C1's watchdog role all keep their exact meaning; only the issuing process and the supervisor's naming power change | §V21101.6 |
| **B7** — totality in the corrected topology | Eight reconciliations plus a `SigBlk == 0` check (`P-g0`) and a `NO_REPLY` route. Every "caller may kill or misreport" case is routed through the **signed** invalidity semantics — `T_PROCESS_INVALID` plus the §4c(c)/§4d unknowable route with invalidity dominance — and the phrase "its own user" is **withdrawn from the chain** as a disposition. `init` adoption after PCS death, W-5's stopped middle, `P-e`'s inherited-child side effect, `STRUCTURAL_VIOLATION` at every site including the new handle sites, and locks/records/fds across every exec and failure are each tabulated | §V21101.7 |

## Required contents of the correction

| Required | Where |
|---|---|
| literal v2.1.10 → v2.1.10.1 replacement index | §V21101.0, twenty rows, each quoting the superseded text |
| exact imports | §V21101.1.1 — `{os, sys, _signal, time, fcntl}`, with the closure table in §V21101.1.2 |
| exact launcher / file actions | §V21101.3.1–§V21101.3.6 — hoist, twelve ordered actions, the full spawn call, constant validation, failure and cleanup, `chdir` |
| fd table | §V21101.3.2 (six bootstrap descriptors) and §V21101.6.4 (seven role descriptors) |
| primitive identity table | §V21101.1.4 — three kinds, per-row requirements, `type(len)` anchor |
| process / ownership tree | §V2110.2.2 carried, extended by §V21101.6.6's five-row call/ownership table |
| package provenance | §V21101.5.2–§V21101.5.4 |
| supervisor-authority disposition | §V21101.6 in full |
| crash matrix | §V21101.7.4 plus the carried §V2110.7.1 rows |
| future verifier algorithm and tests | §V21101.8.1 (CHANGES 2 and 3 amended; S-3b, S-11, S-12, S-13 added) and §V21101.8.2 (six rows replaced, rows 313–352 added) |
| no-regression table | §V21101.9.1–§V21101.9.2 |
| weakest points against myself | §V21101.11, eight items plus 2b |

## Weakest remaining points, stated by the author against the author

Carried verbatim from §V21101.11 so they are visible in both deliverables.

1. **The interpreter is object-bound but not attested.** `/proc/self/fd/8` binds
   *which object* runs, not that it is a reviewed CPython. `P-b` checks a pinned
   identity a patched build could satisfy. Unchanged from v2.1.10 and still the
   sharpest boundary in the design.
2. **Byte provenance is a deploy-time obligation.** The bootstrap proves object
   identity and consistency; it hashes nothing. `hashlib` was excluded to keep
   the five-module closure exact, and an in-root SHA-256 was rejected as too
   large for a file whose value is being statically decidable. A reviewer may
   reject that trade.
2b. **`/proc` must be mounted and unfaked.** Every object-bound path, the flag
   and mask readbacks, and the task-count checks route through `/proc`. A host
   with a substituted `/proc` defeats them and nothing here detects it.
3. **B6 is the largest amendment in this chain.** It relocates every process
   primitive in the system and re-points the watchdog through an `execve`'d
   role, touching §W2.1, §W2.4, §W2.5, §W3.3, §Z3.3 and C1's creation path. I
   bounded it by "relocate the primitive, preserve the semantics" and by the
   handle model, **but a reviewer may reasonably judge that it needs its own
   layer rather than a subsection of a pre-review correction.** I have put that
   judgment explicitly in X-Q3 so a line can rule on it directly.
4. **The handle model removes PID authority, not bookkeeping corruption.** A
   contaminated supervisor can still mis-order its own requests or mis-record
   its journal; that is governed by the signed B1 rules and the invalidity
   semantics, which this layer does not strengthen and does not claim to.
5. **`P-e`'s single wildcard wait remains a real exception**, with a stated
   reaping side effect in the case where it returns.
6. **The launcher checks are defeatable by a fully hostile caller.** Accepted,
   and the reason §V21101.4.1 is a disjunction — but it means the *loudness* of
   a mis-launch is not guaranteed, only its harmlessness.
7. **The `posix_spawn` at-fork fact is reviewer-verifiable, not author-proved.**
   I made it non-load-bearing and rely instead on the process boundary; the two
   are independent.
8. **`_signal` is a private CPython module.** Its API is stable in practice and
   is what `signal` itself wraps, but depending on an underscore module trades
   convention for a smaller auditable closure.

## Final questions

§V21101.12 carries **three** bounded questions per line. X-Q1 attacks the
construction, the `_signal` closure, the identity table and the object-binding;
X-Q2 the `posix_spawn` launcher, its collision argument, the at-fork fact and
the disjunction; X-Q3 provenance and B6, **including an explicit invitation to
rule that B6 is too large for this layer**. Y-Q1 attacks single-valuedness and
the identity rule; Y-Q2 launcher authority, provenance and whether B6's route 1
is a genuine resolution; Y-Q3 the eight totality reconciliations and whether
§V21101.7.5 uses the **signed** invalidity semantics rather than inventing a
disposition. Both lines must recompute the digests of v2.1.10 and v2.1.10.1 and
of every governing hash, and must treat both author closures as untrusted.
Verdict line 1 is exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_10_1_X` / `..._Y`
or `REVISE_OFFICINA_SUPERVISOR_V2_1_10_1`.

## Custody, authorization boundary, and programme state

Exactly **two** files were created by this work, and nothing else in the
repository was touched:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_1_closure.md` (this file)

`scripts/officina_process_control_bootstrap.py` is **specified, not created**;
it does not exist. `src/philosophia/officina/verification.py` is unmodified —
digest `327b1bb2…` — and the production call-graph manifest does not exist.
v2.1.10 and its closure are **not edited**; their digests are recorded above and
match. No prior artifact, contract, signature, review, prompt, code file,
verifier, test file, or runtime tree was edited, staged, or committed; the
untracked `src/philosophia/officina/generic_harness.py`,
`tests/test_officina_generic_harness.py`, `essay/OUTLINE.md`, and the modified
`accounting.py`, `test_officina_accounting.py`, and review/prompt files are
preserved byte-for-byte.

Confirmed explicitly, as required: **no code, no test, no run of any kind — no
implementation, probe, smoke command, spawn/fork/signal experiment, or Officina
process — and no activation, entropy, T/Q/C work, datum, outcome, or claim
movement.** T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`; no
artifact was produced.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not authorized and
remains unavailable**. No independent review of v2.1.10 was requested and none
of v2.1.10.1 has occurred; no conditional authorization from any earlier round
survives or transfers. The token becomes available only if a fresh independent
X-line review **and** a fresh independent Y-line review both confirm **v2.1.10
as corrected by these bytes**, digests `2b4f9cad…` and `2d4d4b18…`. This closure
authorizes no implementation, no code, test, verifier, manifest, or allowlist
change, no commit, no host change, no T activation, no entropy, no E1/E2/E3
spend, no Q/C work, no capability, lease, operation, capacity artifact, custody
disposition, result manifest, world, learner, candidate, Q attempt, datum,
outcome, Proof, or claim movement, and no later gate.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`.
