# Prompt for Claude Code Opus 5: pre-review Officina supervisor v2.1.10.1 correction

Act as the **specification author**. Do not request X/Y review yet. v2.1.10 has
several literal and architectural ambiguities discoverable before independent
review. Produce one bounded correction over v2.1.10; do not edit it in place.

Work in `philosophia` at or after commit
`f67256a489ffcecae7caece628529baae0c11c77`. Treat all existing files as
immutable. Recompute:

```text
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
4cc19fc914f5908f069cb7b8aa09297dece424943f8a876974105e575d09c47d  reviews/opus5_officina_supervisor_control_channel_v2_1_10_closure.md
```

Static authoring only. Run no code, tests, probes, spawn/fork/signal experiment,
or Officina process. Modify no implementation, verifier, activation, entropy,
T/Q/C object, datum, claim, or prior document. Create only the two deliverables
named below.

## Bounded blockers to repair

### B1 — contradictory import inventory and invalid identity rule

v2.1.10 says both:

- the bootstrap imports exactly four modules and `fcntl` is excluded; and
- it imports exactly five modules including `fcntl`.

This is not single-valued. Adopt one exact inventory everywhere. Prefer the
smaller built-in surface:

```text
{os, sys, _signal, time, fcntl}
```

using the built-in `_signal` module directly rather than the Python `signal`
wrapper. This removes `signal -> functools -> _thread` from the transitive
closure and makes `_signal.signal`/`_signal.getsignal` genuine built-ins. Name
and supersede every previous `signal`-allowlist/import sentence accordingly.

Do not apply one universal callable identity predicate blindly. Pin an exact
per-primitive table: expected type, `__module__`/`__self__`, name/qualname and
any wrapper-specific rule. The current rule would reject genuine Python-wrapper
`signal.signal` and `signal.getsignal`; the correction must make every genuine
binding pass and every stated substitution fail without trusting mutable
caller state.

### B2 — the script path is not object-bound

`readlink("/proc/self/fd/<n>")` returns a pathname; passing that pathname to the
interpreter re-resolves it and permits replacement after observation. Delete
the claim that this is the same inode.

Specify a real fd-bound launch. The bootstrap source must remain open across
spawn on a pinned descriptor and the interpreter must receive the literal
script argument `/proc/self/fd/<BOOTSTRAP_SOURCE_FD>`, not a readlink result.
The bootstrap must `fstat` that descriptor and prove it is the reviewed regular
file before process authority. State unlink/rename/hardlink/symlink and every
spawn-cut behavior. Bind the source bytes to the reviewed manifest/hash without
silently importing a large hashing stack; if hash verification is outside the
minimal bootstrap, state the exact object-identity + signed-manifest mechanism
that replaces it.

The interpreter executable is also a name today. Either object-bind it through
an inherited executable fd and execute `/proc/self/fd/<INTERPRETER_FD>`, or state
and justify the exact narrower trust premise. Do not call a mutable
`sys.executable` string “kernel supplied”.

### B3 — impossible Popen/pre-exec descriptor mapping

v2.1.10 simultaneously pins `preexec_fn=None` and says the caller `dup2()`s
arbitrary ends onto fd 3…6 “in the pre-exec child”. `subprocess.Popen` has no
general fd-remapping argument; `pass_fds` only preserves existing numbers.

Replace the launch with one exact mechanism. Preferred route:

- bind and identity-validate genuine `os.posix_spawn` in the dirty caller;
- use a closed `file_actions` sequence with `POSIX_SPAWN_DUP2`/`CLOSE` to map
  request, reply, runtime-root, package-root, bootstrap-source and (if chosen)
  interpreter fds to fixed non-overlapping numbers;
- execute the fd-bound interpreter/script paths;
- exact empty environment and exact argv isolation flags;
- no `Popen`, no `fork`, no `preexec_fn`, no shell, and no Python at-fork
  callback in the caller launch route.

Pin the numeric/semantic validation of every `POSIX_SPAWN_*` constant and the
complete file-action ordering, alias collisions, source-fd collisions,
close-on-exec transitions, failure returns/exceptions, and cleanup. Explain from
pinned CPython/libc semantics whether `posix_spawn` invokes user Python at-fork
callbacks; no unsupported assumption may carry the repair.

If `cwd="/"` cannot be expressed by the chosen spawn API, remove the false
launcher claim and have the isolated bootstrap call a locally bound genuine
`chdir("/")` before opening any name; show why object-bound descriptors make the
pre-chdir cwd irrelevant.

### B4 — dirty-caller launcher authority

The caller is declared to have “ANY runtime state”, so its `sys.executable`,
`os.posix_spawn`, `os.open`, constants and fd setup may be rebound. Narrow and
mechanize the claim:

- bind/identity-check every launcher primitive and immutable value before use;
- refuse before spawn on any mismatch;
- use no mutable high-level wrapper;
- specify which caller contamination is made harmless by `execve` and which
  causes a no-spawn refusal.

Do not claim a hostile or arbitrarily monkeypatched caller must successfully
launch the bootstrap. The required property is: it either constructs the exact
isolated process through genuine primitives or creates no authorized bootstrap.
Replay the `.pth`/at-fork/monkeypatch counterexamples against this launcher.

### B5 — package/role provenance

The bootstrap currently admits that a dirty caller can pass an arbitrary
package-root fd and make it exec an arbitrary supervisor. That is not merely a
cosmetic limit once the reply affects the harness and later scientific work.
Bind fd 6 to the reviewed repository/manifest at least by:

1. opening the canonical bootstrap source relative to fd 6 with
   `O_NOFOLLOW` and proving its `(st_dev, st_ino)` equals the inherited
   bootstrap-source fd;
2. reusing the signed production-manifest/root-source-hash mechanism with exact
   object-bound reads for the supervisor role and every load-bearing root;
3. refusing before fork/exec on any mismatch or unsupported hardlink/replacement
   pattern.

If full role provenance is intentionally assigned to an inherited verifier,
state the exact previously signed mechanism and demonstrate that the caller
cannot substitute its inputs. Do not leave “hostile caller can launch arbitrary
supervisor” as an accepted supported route.

### B6 — the supervisor retains the same defect class

The closure admits that the supervisor's `Popen`/wait handshake and watchdog
fork remain in a contaminated interpreter and calls that outside scope. That is
not sufficient for an amendment named **supervisor/control-channel**.

Provide one of exactly two resolved outcomes:

1. extend isolated process authority so every supervisor-owned child creation,
   numeric signal, wait and watchdog fork is performed by the clean bootstrap
   or an identically constructed clean process-control instance; or
2. prove with a complete call/ownership table that the supervisor holds no
   PID-reuse-sensitive authority and that contamination cannot affect any
   process, ledger, capacity, custody or scientific result.

The second route is unavailable if the supervisor calls `Popen`, `fork`,
`waitpid`, `kill` or `killpg` on a result-bearing path without the same
construction. Do not defer a known same-class safety defect merely because the
v2.1.9 finding used `pid_mid` as its first counterexample.

### B7 — totality details carried into the corrected topology

Reconcile the new launch/process tree with:

- caller helper reaping the bootstrap;
- pipe reply when the caller dies, lies, stops reading or closes early;
- bootstrap/operator SIGINT at every cut;
- `P-e` wildcard wait and inherited-child side effect;
- W-5 stopped middle after m8;
- `STRUCTURAL_VIOLATION` at every W site;
- direct-child ownership if bootstrap dies and init adopts descendants;
- locks/records/fds across every exec and failure.

Any claim that the caller may kill or misreport while science stays valid must
be routed through the existing invalidity/fail-closed semantics, not merely
described as “its own user”.

## Required deliverables

Create exactly:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_1_closure.md`

The correction must contain a literal v2.1.10 → v2.1.10.1 replacement index,
exact imports, exact launcher/file actions, fd table, primitive identity table,
process/ownership tree, package provenance, supervisor-authority disposition,
crash matrix, future verifier algorithm/tests and no-regression table. State the
weakest remaining points against yourself.

Closure line 1 exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_1_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_1_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_1_CONTRACT_CONFLICT`

Use `READY` only if all seven blockers are single-valued and implementable. Ask
each line at most three bounded final questions. Confirm: no code/test/run,
implementation, activation, entropy, T/Q/C, datum, outcome or claim movement;
T `NOT_ACTIVATED`, claim `OPEN`, amendment token unavailable.
