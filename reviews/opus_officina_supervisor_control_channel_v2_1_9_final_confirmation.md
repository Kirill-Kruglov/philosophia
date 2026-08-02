REVISE_OFFICINA_SUPERVISOR_V2_1_9

# Opus 4.8 X-line: independent final confirmation of Officina supervisor/control-channel v2.1.9

Date: 2026-08-02
Reviewer line: X (adversarial Linux / CPython / process / signal / crash / hash-construction semantics)
Reviewer: Claude Opus 4.8, clean context.

## Independence and method

v2.1.9 was authored by **Claude Code Opus 5 in the specification-author role**
(Fable 5 unavailable); the same author line wrote v2.1 through v2.1.8. I read its
closure (`reviews/opus5_officina_supervisor_control_channel_v2_1_9_closure.md`),
its repair chat response, and its embedded self-assessment **only as untrusted
author claims** and used none as evidence, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` requires. I rebuilt the
result from the normative bytes: the full v2 → v2.1.9 supervisor chain, the
signed generic-harness v2 → v2.3.1 composite and its signature, the
batch-settlement v1 → v1.1.1 composite, both supervisor author-selection
signatures, the authorship note, and **both** v2.1.8 reviews (Opus X-line
`CONFIRM`, Sol Y-line `REVISE`). **The Y verdict governs**; every Y v2.1.8
finding (C218-1, M218-1, M218-2, M218-3, m218-1) is treated as sound, and no part
of my judgment rests on the v2.1.8 X confirmation.

This was a static contract review. Read-only file/Git inspection, literal search,
`sha256sum`, and arithmetic only. I ran no repository code, test, probe, smoke
command, fork/signal/subprocess experiment, or Officina process, and started no
process of my own. I altered no existing file or runtime state; the pre-existing
dirty tracked and untracked handover paths are preserved. Exactly one file — this
review — was created.

## Recomputed hash and base

Target digest, `sha256`:

```text
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
```

This **matches the expected value exactly**. The file is committed and clean at
`HEAD = 71dffe4a2c03711487f9182e90f3bafd5b40ebc1`, which
`git merge-base --is-ancestor` confirms **descends from the required base**
`8ba4ba9371347326d46f63dce1f4cab2728149bf`.

Every one of the **21 governing hashes** in the v2.1.9 "Governing hashes" block
reproduces byte-for-byte, including the ten prior supervisor layers, both v2.1.7
reviews, both v2.1.8 reviews, the two author-selection signatures, the harness
signature, the harness v2.3.1 and batch v1.1.1 composites, and the unamended
`src/philosophia/officina/verification.py` (`327b1bb2…`). I independently
confirmed `verification.py`'s `ALLOWED_ABSOLUTE_IMPORTS` holds exactly sixteen
members and **does not** contain `signal`, and that the file is a **static AST
walker** over the three-file `PRODUCTION_ROOTS` tuple — a fact load-bearing for
Finding F1 below.

## VERDICT

```text
REVISE_OFFICINA_SUPERVISOR_V2_1_9
```

The layer makes real progress: the wait automaton (M218-1), the importer topology
(M218-2), and the mask-width rule (m218-1) are closed. But the **central repair
does not close C218-1**. §V219.2's executor-set theorem substitutes exactly what
the required question forbids — **clean argv (G-1) and repository-AST/call-graph
constraints (the signed verifier) for clean runtime state**. Its load-bearing
step 4 conflates the *runtime-reachable* code set `C(t₀)` with the *statically
walked source* set, and no gate establishes their equality. Under the layer's own
pinned invocation `python -m philosophia.officina.generic_harness` — which pins
**no** `-S`/`-I`, so `.pth`/`sitecustomize`/`usercustomize` site processing runs,
and which §V219.2.7 explicitly admits to `c4` — a competing reaper or a
substituted reviewed syscall can be introduced after `c3t`/after `c4` invisibly to
`G-1…G-5`, `N-1`, and `V-1…V-10`. Because C218-1 is not closed, **M218-3 is not
closed either**: §V219.5.1 excludes the `ECHILD` contradiction source by *citing
the theorem's own corollary* (the circularity the required question warns of), so
with the theorem unsound, `B-CONTRADICTED` is reachable from **supported** history
and is a permanent `SPAWN.lock`-holding sink. A fail-closed label is not a repair
when supported operation can enter a permanent sink.

The token `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` therefore
remains **unavailable** and is not made signable.

---

## Disposition of all five governing findings

| Finding (v2.1.8 Y-line) | v2.1.9 locus | Independent X-line disposition |
|---|---|---|
| **C218-1** (Critical) — sole-reaper/PID-reservation premise not mechanically established against inherited runtime state | §V219.2 (topology gate `c3t`, executor-set theorem, verifier rule) | **NOT CLOSED (F1).** The theorem is unsound as written: `G-1` proves argv, not the loaded image, and argv is writable in-process and fork-inherited; step 4 equates runtime `C(t₀)` with the static AST the verifier walks. Site-layer contamination + `os.register_at_fork` + `os.*` monkeypatching defeat it while every kernel readback passes. |
| **M218-1** (Major) — four of five wait sites lack a total automaton | §V219.3 (`WAIT_ONE` + five instantiations + product) | **CLOSED at the automaton level.** `WAIT_ONE` is total over `(pid,status)`/`(0,0)`/`ECHILD`/`EINTR`/other-errno with one precondition; the five site tables and the result×site product are exhaustive; only `REAPED_POSITIVE` sets `REAPED`; no site runs after `REAPED`. **Caveat:** its no-wrong-PID safety is contingent on F1 (a monkeypatched `os.waitpid` makes even a targeted call non-total). |
| **M218-2** (Major) — sole-root vs permitted-importer rules contradict | §V219.4 | **CLOSED.** Adopts Y's smaller repair: `generic_harness.py` is sole root **and** sole `signal` importer; the four supersessions (harness §9 `signal` conjunct only; §V2.10 `verification.py` clause only; §V2.10 "delta: none"; the unimplementable file-granularity forbidden-importer row → call-site granularity) are correctly scoped; the seven §S7 obligations make the future `verification.py` delta single-valued (16 → 17). |
| **M218-3** (Major) — `B-CONTRADICTED` has no lawful progress | §V219.5 | **NOT CLOSED (F2), consequential on F1.** The reclassification to an out-of-supported-history sink is the disposition Y pre-authorized — **but only if C218-1 is closed first** (Y Trace 7; §V219.5 concedes this at line 809). §V219.5.1 excludes source (a) by citing §V219.2.2's corollary; that is circular, and with F1 open `ECHILD` is reachable in supported history, so the sink is reachable in supported operation. |
| **m218-1** (Minor) — short `/proc` masks accepted as clear | §V219.6 (`MASK_FIELD`, `W-a`/`W-b`) | **CLOSED.** `SigIgn: 0` / `SigCgt: 0` now fail `W-a` (`4·d ≥ int(SIGCHLD)`) and `W-b` (`d == 16`) before any conversion → `VERIFY_INCONCLUSIVE`, no fork. The Linux `render_sigset_t` fixed 16-hex-digit (`_NSIG = 64`) rendering is correct on every declared arch; both conjuncts are justified and `W-b` is the stricter. |

**Required question — answer: No.** v2.1.9 does not close C218-1 (and hence
M218-3) with an implementable, total contract. The executor set is **not**
genuinely closed from pre-fork through final reap; the layer substitutes clean
argv and repository-AST constraints for clean runtime state, which is exactly the
substitution the question rules out.

---

## The eight required attack traces

### 1. Sole-root identity — G-1 does not prove P-1

`G-1` reads `/proc/self/cmdline`, NUL-splits, and requires
`("-m", "philosophia.officina.generic_harness")` at indices `(1, 2)`. The layer
asserts (lines 347–349, 490) this "is a KERNEL fact … it names the program image
actually loaded." **It does not.** `/proc/self/cmdline` returns the *argv byte
range* (`mm->arg_start … arg_end`), which is (a) **writable in-process**
(`prctl(PR_SET_MM_ARG_START/ARG_END)`, or a direct write to the argv buffer via a
C extension), and (b) **inherited unchanged across `fork`** — the layer concedes
(b) itself. The kernel attestation of the loaded image is `/proc/self/exe`, which
for `-m` module execution names the *interpreter*, never the module. So `G-1`
proves only "the argv currently readable begins with the pinned `-m` pair," which:

- a single-threaded embedding host can forge (spoof argv, then `import` the sole
  root and call the bootstrap in-process), and
- says nothing about whether a fresh `execve` of the sole root actually occurred,
  or whether the running object graph is the reviewed program.

§V219.2.7's inference "if a host is single-tasked *and* its `cmdline` names the
sole root, then **by P-1** the program **is** the sole root" is therefore
**unsound**: it treats a spoofable, inherited argv match as proof of image
identity and of a clean startup. `runpy`, wrapper launchers, and in-process calls
with a matching `cmdline` all pass `G-1`. **G-1 does not prove P-1 as stated.**

### 2. Startup/runtime contamination — the empty-set claim fails

The layer is correct that `execve` erases the prior address space, callbacks,
handlers, hooks, and `sa_flags`. It omits that **Python startup re-populates state
before `__main__`/the bootstrap runs**, and the pinned invocation admits that
startup: the argv rule pins `python -m …` with **no `-S` and no `-I`**, so `site`
processing runs — `.pth` executable lines (any line beginning `import `),
`sitecustomize`, and `usercustomize` all execute in the genuine sole-root process
after `execve` and before `c3t`. §V219.2.7 itself lists a `sitecustomize`/
`faulthandler` process as reaching `c4`.

The layer nets only two contamination classes:

- **new threads** → caught by `G-2`/`G-3` (`/proc/self/task`, `Threads:`);
- **catching handlers** → reset by `N-1`, proved absent by `V-4` (`SigCgt == 0`).

It nets **none** of the following, each of which creates a task, wildcard-wait, or
substituted syscall *after* `c3t` without a `SigCgt` bit and without a task
visible at `G-2`/`G-3`:

1. **`os.register_at_fork(after_in_parent=…)`** registered by a `.pth`/
   `sitecustomize` at startup. The handler runs in **this task** when the
   bootstrap calls `os.fork()` at `c4`, and can start a wildcard-reaping thread
   **in the parent (CLI)** — created *after* `G-2`/`G-3`, precisely when
   `pid_mid` is alive. This is the original C218-1 harm, resurrected: the helper
   reaps `pid_mid`'s zombie, the PID is reused, `OWNERSHIP` is still `OWNED`, and
   `os.kill(pid_mid, …)` hits an unrelated process. Registered at-fork handlers
   have no enumeration API, so no gate can even detect them.
2. **Monkeypatched `os.waitpid`/`os.fork`/`os.kill`** rebound at startup. The
   reviewed source's textual `os.waitpid(pid_mid, WNOHANG)` invokes the rebound
   name; nothing in `G-1…V-10` checks the *identity* of `os.*` callables, and the
   static verifier walks source text, not runtime bindings.
3. **Retained callables** installed at startup and reachable from the program's
   control flow (e.g., a rebound builtin, a patched `os` attribute) — invoked
   "synchronously," so the theorem lumps them into source `(a)`, then step 4
   wrongly equates `(a)` with the walked file set.

Theorem step 4 — "`C(t) ⊆` the reachable production-source set the signed
verifier walks from `PRODUCTION_ROOTS`" — is the false step. `C(t₀)` is a
*runtime* set; the verifier set is *static*. They coincide only if no code outside
the three walked files executes in this task's control flow at a task-creating or
wait/kill point, which P-1 was supposed to guarantee and does not (Attack 1).
**Until a gate establishes `C(t₀) =` the reviewed runtime, C218-1 remains open.**

### 3. Native executor set

`ALLOWED_ABSOLUTE_IMPORTS` includes `os`, `subprocess`, `weakref`, `fcntl`,
`hashlib`, `hmac`. A native/C-extension helper thread spawned **at import time**
would exist before `c3t` and is caught by `G-2`/`G-3` — good. The residual
concern is a permitted dependency that spawns a helper task or waiter **on a call
between the final task readback and the final reap** (not at import); the verifier
sees the Python call site but not the native thread it starts, and `V-7`/`V-8`
(admittedly non-load-bearing) run only once before the first `SIGNAL_ATTEMPT`, not
continuously. `subprocess` is defended in depth (R-c: `Popen` cleanup polls its
own pid), which is correct. This is a narrower channel than Attack 2 and I do not
rest a finding on it, but it is a second reason the "single-task snapshot preserves
single-taskness" claim is a snapshot, not an invariant, once `C(t₀)` may exceed
the walked source.

### 4. Signal reset

The `N-1` derived-mask reset is sound *for handlers*: it iterates the `SigCgt`
bits recorded at `G-4`, resets each to `SIG_DFL`, uses no new `signal` member
(numbers are kernel-derived), routes every exception to `NORMALIZE_INCONCLUSIVE`,
and `SIGKILL`/`SIGSTOP` can never carry a `SigCgt` bit. `V-4` (`SigCgt == 0`),
`V-5`/`V-6` (SIGCHLD ignore bit clear, no other `SigIgn` disturbed), and the
carried unconditional `N-2` (`SA_NOCLDWAIT` clear by the `sigaction` write) are
correct, and the `SIGPIPE = SIG_IGN` preservation is mechanically proved by `V-6`.
`SigCgt == 0` **does** exclude asynchronous callbacks (default actions run no
process code). **But `SigCgt == 0` closes only the asynchronous half of the
executor set.** It says nothing about a synchronous task-creating callback
(`register_at_fork` handler) or a substituted syscall (Attack 2), both of which
enter without any handler. So the signal reset is correct and does **not** by
itself close C218-1.

### 5. `WAIT_ONE` product

Instantiating each result at W-1…W-5:

- `(pid_mid, status)` → `REAPED_POSITIVE`, the sole setter of `REAPED` and the
  sole death proof; targeted positive-pid `waitpid` cannot return any other pid.
- `(0, 0)` → `NOT_YET`; `WNOHANG` without `WUNTRACED` cannot report stop/continue,
  so a SIGSTOPed middle is correctly indistinguishable and never mis-set.
- `ECHILD` → `CONTRADICTED_ECHILD`, never death (carried) — correct.
- repeated `EINTR` → re-issue within deadline; at expiry `INCONCLUSIVE_OTHER`
  (W-1…W-4) or `NOT_YET` after one retry (W-5) — bounded, correct.
- other errno → `INCONCLUSIVE_OTHER`.
- post-`REAPED` → precondition names it a contract violation: no syscall, no
  signal — correct.
- **W-4/`ECHILD`**: P3's death conclusion rests on `/proc` absence/`Z`/identity
  mismatch, not the reap, so `ECHILD`/errno/expiry do not block or reverse the P3
  route; they only forbid a later signal — sound.
- **W-5 race (`m8` before `m9`)**: ≤2 non-blocking `WNOHANG`, no signal, no
  deadline; both `NOT_YET` ⇒ bootstrap still **succeeds** and leaves the carried
  zombie residual (reaped at W-4 or by `init`) — sound. (A SIGSTOPed middle that
  never reaches `m9` lingers as a stopped child that neither W-4's `WNOHANG` nor
  `init` reaps; this is a disclosed A3/host-fault residual, not a new defect.)

Mutual exclusivity (§V219.3.3) is proved, not asserted, and the product table
(§V219.3.4) is complete. **M218-1 is closed at the automaton level.** The only
gap is inherited from F1: "targeted" is a property of the source text, not of the
runtime `os.waitpid` binding.

### 6. Contradiction sink — circular exclusion

§V219.5.1 must show all four `CONTRADICTED` sources are excluded in *supported*
history. Source (a) (`ECHILD`) is excluded by "**§V219.2.2's corollary** …
Another reaper is excluded." This is precisely the circularity the required
question forbids: the sink's out-of-history status is proved **by assuming the
executor-set theorem**. With F1 open, another reaper *can* exist in a supported
execution (a genuine `python -m generic_harness` with a contaminating `.pth`/
`sitecustomize`), so `WAIT_ONE` can return `CONTRADICTED_ECHILD` in supported
history, `OWNERSHIP := CONTRADICTED`, `captured = ⊥`, and the process enters
`B-CONTRADICTED` — the non-returning sink that holds `SPAWN.lock` and
`SPAWNING.json` forever while later CLIs receive only `s5` refusals. `s5` is
correctly **not** called a resolver (§V219.5.4), `B-OWNED` is unchanged in
substance, and the T2-zombie/restart/second-CLI totals are preserved — but that
does not save M218-3, because the sink is reachable from supported operation.
**M218-3 is not closed.** (Its closure follows automatically once F1 is genuinely
closed, exactly as Y stated.)

### 7. Importer/verifier exactness — closed

`generic_harness.py` is the sole executable root (`PRODUCTION_ROOTS`, unchanged)
**and** the sole `signal` importer; the permitted surface is four names
(`signal.signal`, `getsignal`, `SIG_DFL`, `SIGCHLD`) at the two `c3n` functions,
with a callable second argument forbidden everywhere and every other member
enumerated as forbidden. The four supersessions (§V219.4.2 rows 15–18) are each
quoted and scoped: **only** the `signal` conjunct of harness §9, **only** the
`verification.py` entry of §V2.10's frozen list, §V2.10's "delta: none," and the
unsatisfiable file-granularity forbidden-importer row → call-site granularity.
The §S7 obligations 1–7 pin the future `verification.py` delta to a single value
(add the one string `"signal"`, 16 → 17; nothing else changes). The static
verifier's `DYNAMIC_IMPORT_CALLS` set already forbids `__import__`/`eval`/`exec`/
`compile`/`getattr`/`importlib.import_module` in the reviewed source, so aliasing/
rebinding/`from signal import`/dynamic attribute access **within the reviewed
source** are catchable by the proposed AST/call-graph checks. **M218-2 is
implementable and closed.** (This closure is about the *reviewed source*; it does
not — and cannot — bind the site layer, which is the F1 channel.)

### 8. Mask and regression — closed

Linux renders `SigIgn`/`SigCgt` via `render_sigset_t` as a fixed 16-hex-digit
(64-bit, `_NSIG = 64`) value on every declared arch, 32- and 64-bit alike;
`W-b` (`d == 16`) is correct and stricter than the arch-independent `W-a`
(`4·d ≥ int(signal.SIGCHLD)`; `SIGCHLD` = 17 on x86/x86-64/ARM/ARM64, 18 MIPS, 20
Alpha/SPARC). The eleven-row table (empty, `0`, `0000`, 13-digit, 16-digit,
20-digit, `0x` prefix, duplicate, leading zeros, `_NSIG=128` future) each routes
as tabulated; conversion occurs only after both conjuncts pass; duplicates and
absence are `MASK_MALFORMED`; SIGCHLD bit indexing (`(mask >> (n-1)) & 1`,
1-based) is correct. Re-running the carried no-regression surfaces (object-bound
barriers, PID/identity table I-1…I-10, T3 deletion, stage-M `m0`/`rel1` proof,
bound sweep, A3/B1/C1/D1/K1, generic-harness/batch-settlement composites,
E1/E2/E3, nine events, Q/C and T inactivity) shows **no new regression**: the
defect is that the *new* C218-1/M218-3 repair is incomplete, not that a carried
surface was disturbed. **m218-1 is closed; no-regression holds.**

---

## Findings

### F1 (Critical) — C218-1 not closed: the executor-set theorem is unsound; clean argv + repository AST substituted for clean runtime state

**Loci:** §V219.2.1 (P-1), §V219.2.2 (theorem steps 4–5), §V219.2.3 `G-1`,
§V219.2.6 (verifier-as-mechanism), §V219.2.7 (in-process/`sitecustomize` rows),
§V219.5.1 source (a); dependency on the un-pinned `-S`/`-I` in §V2.10's carried
argv rule.

**Failure scenario (concrete, no malicious actor required).** A genuine
`python -m philosophia.officina.generic_harness` process. Site processing runs
(no `-S`/`-I`). A `.pth` executable line or `sitecustomize` — the topology
§V219.2.7 admits to `c4` — executes
`os.register_at_fork(after_in_parent=_start_reaper)`, where `_start_reaper`
launches a thread doing `os.waitpid(-1, os.WNOHANG)` polling. At `c3t`: single
task (`G-2`/`G-3` pass), `SigCgt` reset to 0 (`V-4` passes), `cmdline` matches
(`G-1` passes). At `c4` the bootstrap calls `os.fork()`; the parent-side at-fork
handler runs **in this task** and starts the reaper thread — created *after* the
task readbacks. The reaper reaps `pid_mid`'s zombie; Linux reuses the PID;
`OWNERSHIP` is still `OWNED`; `os.kill(pid_mid, SIGTERM)` succeeds against an
unrelated process. No `ECHILD`/`ESRCH`/`ppid` detector runs in time. The theorem's
step-4 claim `C(t₀) =` walked source is false: the at-fork handler is code
reachable from this task's control flow but not in `PRODUCTION_ROOTS`. A
monkeypatched `os.waitpid`/`os.fork` (Attack 2 case 2) produces the same class of
harm with no thread and no handler at all — invisible to every gate. `G-1` cannot
even establish a fresh sole-root `execve`, since `cmdline` is writable and
fork-inherited (Attack 1).

**Smallest repair.** Stop equating `C(t₀)` with the static source. Establish the
runtime instead: (a) pin `-I` (or at least `-S -E -P`) in the invocation and
verify it at `c3t` via `sys.flags` readback, so `.pth`/`sitecustomize`/
`usercustomize` cannot run; (b) verify `os.fork`/`os.waitpid`/`os.kill` are the
unpatched builtins by identity, and refuse if any is rebound; (c) refuse if any
`os.register_at_fork` handler is registered before `c4` (or fork via a path that
does not run Python-level at-fork dispatch); or (d) adopt a reviewed
`pidfd`-based signalling design so PID reuse cannot mislead a signal regardless of
who reaps. Any of (a)+(b)+(c) or (d) would let the theorem's step 4 be *proved*
rather than assumed. Correspondingly, drop the "kernel fact … names the program
image" language at `G-1`.

### F2 (Major) — M218-3 not closed: `B-CONTRADICTED` is reachable from supported history because its exclusion is circular on F1

**Loci:** §V219.5.1 source (a) exclusion; §V219.5.2 `B-CONTRADICTED`; §V219.5.3;
§V219.7.2 last row.

**Failure scenario.** The F1 competing reaper produces `CONTRADICTED_ECHILD` in a
supported execution before any identity capture. `OWNERSHIP := CONTRADICTED`,
`captured = ⊥` ⇒ `B-CONTRADICTED`: `SPAWN.lock` + `SPAWNING.json` held forever,
`WAIT_ONE` can never return `REAPED_POSITIVE` for the reaped/reused pid, every
later CLI takes `s1→s5` and refuses. The layer classifies this state as "outside
supported history," but that classification is derived solely from §V219.2.2's
corollary — the unsound theorem. The required question is explicit: "A fail-closed
label is not a repair if supported operation can enter a permanent sink."

**Smallest repair.** Close F1; M218-3's disposition (an out-of-history safety
sink) is then exactly what Y pre-authorized and requires no further change.

**No other new finding survives re-derivation.** M218-1, M218-2, and m218-1 are
closed as analysed in Attacks 5, 7, and 8. The author's closure and chat response
were not used as evidence.

---

## No-regression table

| Signed / carried surface | Status under v2.1.9 |
|---|---|
| §V218.2.2 `SIGCHLD := SIG_DFL` full-disposition replacement + `sigaction` + `execve`/`fork` provenance | Carried byte-for-byte; `N-2` is that call, executed unconditionally. Verified. |
| `ECHILD`/`ESRCH` never death | Carried at all five `WAIT_ONE` sites and in `SIGNAL_ATTEMPT`. Verified. |
| Ten-row identity table I-1…I-10 (§V218.3.4) | Carried; ownership × identity × wait product (§V219.7.1) consistent. Verified. |
| Ownership-gated signals + fork-ownership PID-reuse proof (§V218.3.1–.2) | Carried. **The exclusivity premise it needs is supplied by §V219.2.2, which F1 shows unsound**; the carried text is intact but its safety is contingent on F1. |
| `SIGNAL_ATTEMPT` + TERM→KILL schedule (§V218.3.5–.6) | Carried byte-for-byte. |
| Deletion of `T3`; T1/T2/B no-discard invariant (§V218.4.1) | Carried; no route abandons a possibly-live child. Verified. |
| Stage-M causal proof `m0`/`rel1` + fork-shared lock (§V218.5) | Carried byte-for-byte. Verified. |
| §V217.1 object-bound observation + both revalidation barriers | Carried, untouched. Verified. |
| §V217.4 bound-language sweep, row 86, D1 ground | Carried; `B`'s unbounded loop consistent with withdrawn fixed-total-CLI claims. |
| §V216.2 `CLOSE_OWNED`; §V216.1.2/.1.3 `MALFORMED` dominance + `B-P`/`B-QM`/`B-QN` | Carried byte-for-byte (stage-M `B` label distinct). |
| §N2.3 P1–P7 custody, §V214.2.4 reconciliation, K1 constants/one-release | Carried byte-for-byte. |
| Death-before-unlink (§V216.3, §V217.3.1) | Carried; `B` removes nothing. |
| §V216.5 eight-end audit, §V216.4.1 pipe-only, GC order, watchdog, singleton, `s1`–`s5`, §U6.1 P0–P3, §U6.3 | Carried; `s5` behaviour unchanged, description corrected (no longer implied a resolver). |
| §U2.3 `m0`–`m9` incl. `m4`/`m8` EPIPE route + `SIGPIPE = SIG_IGN` | Carried; `V-6` proves `N-1` disturbed no ignored disposition. Verified. |
| §Z3.3 adapter / argv layout / `--officina-bootstrap`; §V2.10 argv rule, six public commands, exit `2` | Carried; `G-1` reuses the existing argv rule and adds no token. **Note:** the argv rule pins no `-S`/`-I` — the F1 site-contamination channel. |
| `PRODUCTION_ROOTS`, sole-root rule, frozen files other than `verification.py` | Unchanged; §V219.4.2 row 16 scopes the one future exception precisely. Verified. |
| A3 / B1 / C1 / D1 / K1 | No scientific cell reopened; A3 residual set consistent (`B-CONTRADICTED` claimed to leave it — but F2 shows it re-enters supported history). |
| Generic harness v2→v2.3.1 / batch settlement v1→v1.1.1 | Referenced unchanged; only change is §V219.4.2 row 15's narrow `signal`-conjunct supersession. Verified. |
| Nine events / E1/E2/E3 / invalidity dominance / Q/C / T | Unchanged; every added fact is control-plane, T-development-only, non-citable. |
| A3 filesystem boundary | Untouched; the topology repair proves nothing about filesystem exclusion. |

No carried surface is broken. The verdict rests solely on the incompleteness of
the **new** C218-1/M218-3 repair.

---

## Author-cell and contract-conflict determination

**No scientific author cell is reopened, weakened, or reinterpreted.** A3/B1/C1/
D1/K1, E1/E2/E3, custody, batch arithmetic, events, schemas, roots, and Q/C
boundaries require no new scientific choice; the intended repairs are
process-control/engineering-surface repairs, and no `BLOCKED_..._AUTHOR_CELL`
verdict is warranted. **The one prior signed-contract conflict (M218-2) is
resolved:** §V219.4.2 correctly and narrowly supersedes the `signal` conjunct of
harness §9 and the `verification.py` clause of §V2.10, with the allowlist delta
still exactly one member (`signal`) and the verifier delta single-valued. No
extra importer, API, durable object, schema, constant, token, operator action,
resource value, or scientific choice becomes implicitly available. The remaining
defect (F1/F2) is **not** a contract conflict but an **unsound safety proof**: the
executor-set theorem's runtime/static conflation and `G-1`'s argv/image
conflation. The bytes therefore still do not state an implementable, total
authorization boundary for the reaper-safety property C218-1 governs.

## Exact authorization boundary

Because this X verdict is **REVISE**, Kirill's token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **unavailable**. It is **not** conditionally authorized on any Y verdict
for these bytes: the v2.1.8 X confirmation was conditional on a Y confirmation of
identical v2.1.8 bytes, the Y line revised those bytes, and that conditional does
not survive or transfer to v2.1.9. A corrected layer must receive fresh
independent X-line **and** Y-line review of its own bytes; had this review
confirmed, authorization would still have been conditional on the Y line
confirming these **identical** v2.1.9 bytes (digest `1468c9ab…`).

This review authorizes **no** implementation, code/test edit, `verification.py`
allowlist change, commit, verifier edit, activation, entropy, runtime
construction (supervisor, controller, worker, watchdog, adapter, middle child,
grandchild, endpoint, pipe, FIFO, journal, spawn record, capability, lease,
operation, output/capacity/custody artifact, result manifest), spend, Q attempt,
Q/C object, scientific work, datum, outcome, Proof, or claim movement, and no
later gate.

## Custody and programme state

No repository code, test, probe, smoke command, or Officina process ran; this
review started no process of its own. The only computations were `sha256sum`,
`git` ancestry/status, directory listing, and read-only text search over
documented bytes, plus literal reasoning about Linux/CPython process semantics.
No existing file or runtime state was altered; nothing was committed or staged;
the pre-existing dirty tracked and untracked handover paths are preserved. Exactly
one new file was created — this review.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
