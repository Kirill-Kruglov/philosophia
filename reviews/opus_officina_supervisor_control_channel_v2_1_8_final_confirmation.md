CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_X

# Opus 4.8 X-line: independent final confirmation of Officina supervisor/control-channel v2.1.8

Date: 2026-08-02
Reviewer line: X (adversarial Linux / CPython / process / signal / crash / hash-construction semantics)
Review base: commit `568f68aeb391ec5292d0446abbae734d9345d981` (HEAD), whose
ancestry includes the required `6e158560a8bd452d6780d9e279a079f41f4b78fe`
(verified with `git merge-base --is-ancestor`). The working tree was dirty
exactly as handed over; **nothing was modified by this review** other than the
creation of this one file.

**Independence.** I am Claude Opus 4.8 on a clean context. v2.1.8 was authored by
**Claude Code Opus 5 in the specification-author role** (Fable 5 unavailable). I
read the v2.1.8 closure and its repair chat response **only as untrusted author
claims** and used none as evidence. I rebuilt the result from the normative bytes:
the full v2 → v2.1.8 chain, both signed supervisor author-selection signatures,
the signed generic-harness v2→v2.3.1 composite and its signature, the
batch-settlement v1.1.1 composite, the authorship note, and **both** v2.1.7 REVISE
reviews (Opus X-line and Sol Y-line). Both independent lines revised v2.1.7; there
is no v2.1.7 confirmation of any kind and no earlier confirmation carries across.

## Recomputed hash and base

Target digest, `sha256`:

```text
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
```

This **matches the expected value exactly.** Every governing hash printed in the
v2.1.8 "Governing hashes" block reproduces byte-for-byte, including the two
inherited v2.1.7 reviews it must answer and the new `verification.py` line:

```text
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
2e4bee2305bafb5825a6ac1cca4d131dcbdf730aa048f29c7023cf679c9936e6  reviews/opus_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
5c82f7c1894d3e76239ee26a611731d102a2891486a9c2d667ce9738956d533b  reviews/sol_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

I independently confirmed that `src/philosophia/officina/verification.py` holds
exactly the sixteen pinned `ALLOWED_ABSOLUTE_IMPORTS` members and **does not**
contain `signal`; its digest `327b1bb2…` matches, and this correction does not
edit it.

**Method.** Static, read-only. No repository code, test, probe, smoke command,
supervisor, controller, worker, watchdog, adapter, middle child, endpoint, pipe,
FIFO, journal, or other Officina process ran. The only computations were
`sha256sum`, `git` ancestry/status, directory listing, and text search over
documented bytes, plus literal reasoning about Linux/CPython process semantics. No
existing file or runtime state was altered.

## VERDICT

```text
CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_X
```

v2.1.8 **closes all five inherited findings** — Sol C217-1 (Critical), M217-1
(Major), m217-1 (Minor) and Opus X217-M1 (Major), X217-m1 (Minor) — at their
root, and it does so by mechanically **establishing** before every first fork the
exact process state the stage-M kill/reap machinery depends on, rather than
assuming it. The single required engineering delta — adding **exactly** the module
`signal` to `ALLOWED_ABSOLUTE_IMPORTS`, used only by the CLI bootstrap at four
members (`SIGCHLD`, `SIG_DFL`, `signal`, `getsignal`) at `c3n`'s two functions — is
named loudly, contained by a statically testable surface, and is the very reviewed
amendment the signed harness §9 clause anticipates. No false death proof, orphaned
child, PID-reuse signal, hidden operator step, or contract conflict survived
re-derivation. The two admitted residuals (the new unreaped-zombie residual and
`B-CONTRADICTED` non-termination) are **honest fail-closed** states, named rather
than concealed, and neither misclassifies valid history, abandons a live own
child, nor produces a citable artifact.

Because this X verdict is CONFIRM, the token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` becomes signable **only**
if the independent Y line also confirms the **identical bytes** (digest
`33b0b916…`). Until then it remains unavailable.

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT   — signable by Kirill ONLY on the identical-bytes Y confirmation
```

---

## Disposition of all five inherited findings

| Inherited finding (v2.1.7) | v2.1.8 locus | Independent disposition | Basis (re-derived) |
|---|---|---|---|
| **Sol C217-1** (Critical) — inherited `SIGCHLD`/reaper state defeats the death & PID-reuse premise | §V218.2, §V218.3 | **CLOSED at root** | `c3n` performs one `signal.signal(SIGCHLD, SIG_DFL)` before **every** attempt's first fork, in the main thread, under the held lock. Because `PyOS_setsig` issues one `sigaction` that replaces the entire disposition record, it clears an inherited `SIG_IGN` **and** an inherited `SA_NOCLDWAIT` regardless of exec/fork provenance. `VERIFY_REAPING_STATE` reads the kernel's own `SigIgn`/`SigCgt` bits from `/proc/self/status`; **no fork** occurs unless the result is `NORMALIZED`. The one component `/proc` cannot expose (`SA_NOCLDWAIT`) rests on the pinned write and is backed by three irreversible `CONTRADICTED` detectors. `ECHILD ⇒ INCONCLUSIVE`, never `PROVED_DEAD`. The premise is now *performed and verified*, not assumed. |
| **Opus X217-M1** (Major) — premise not mechanically pinned before fork; safety-preserving repair touches the signed allowlist | §V218.1, §V218.2, §V218.3.1–§V218.3.2 | **CLOSED** | The allowlist delta this finding demanded is taken and named loudly (`signal`, one member); v2.1.7's "zero delta" claim is superseded and every superseding locus enumerated (§V218.1.4). The PID reservation is re-derived as the fork-ownership **proof** of §V218.3.2 from the *performed* normalization, not asserted from an assumed default. `os.kill(pid_mid, …)` executes iff `OWNERSHIP == OWNED`. |
| **Opus X217-m1** (Minor) — `IDENTITY_SAFE` omits `PRESENT_VALID ∧ uncaptured ∧ ppid ≠ getpid()` | §V218.3.4 (row I-4) | **CLOSED, safe direction** | The missing case is row I-4: an owned, unreaped child necessarily has `ppid == getpid()`, so this observation is a **premise contradiction** → `CONTRADICTED`, no signal, no capture (capturing would fabricate another process's identity), route to `B`. It becomes the last-line detector of a failed normalization rather than a gap. |
| **Sol M217-1** (Major) — `T3` abandons a live untracked middle; contradictory terminal membership | §V218.4 | **CLOSED** | `T3` is **deleted** — verified: no route installs nothing, removes `SPAWNING.json`, releases the lock, and returns while `pid_mid` may be live. Stage M is now `T1`/`T2`/non-returning `B`, pairwise disjoint and exhaustive. Because **ownership** (not `/proc`) authorizes the kill, a stopped child is SIGKILLed and reaped even with `/proc` entirely unreadable. The "or `DENIED` signals" clause is gone. The no-discard invariant (§V218.4.1) is checked against each terminal. |
| **Sol m217-1** (Minor) — the second-supervisor proof names the wrong gate (`m5`/`rel2`) | §V218.5 | **CLOSED** | Replaced by the actual `c5`–`c7` trace: no `c8` byte on `rel1`; the middle is at `m0`; it still owns its inherited `rel1_w`, so EOF at `m0` is impossible in principle; `m1`/`m2`/`m4`/`m5`/`m7` are unreachable, so no grandchild and no `SUPERVISOR_IDENTITY.json`; the fork-shared `SPAWN.lock` serializes the next CLI. I verified by exhaustive search that **no operative stage-M sentence, table, test, or claim cites `m5`, `rel2`, or a `rel2` EOF**; every such occurrence is a deletion record, an unreachability assertion, or the §V218.5.3 retention scoped to cuts at or after `c8`. |

All five are answered by exact, independently re-derived text. No inherited finding
survives, and no earlier finding is reopened.

---

## The eight required attack traces

### 1. Reviewed allowlist amendment

The delta is **exactly** the string `signal`. Independent enumeration of every
`signal.<member>` reference in the correction shows the only *used* members are
`signal.SIGCHLD`, `signal.SIG_DFL`, `signal.signal`, and `signal.getsignal`; every
other member (`SIG_IGN`, `pidfd_send_signal`, `pthread_sigmask`, `pthread_kill`,
`set_wakeup_fd`, `siginterrupt`, `alarm`, `setitimer`, `raise_signal`, `sigwait`,
`strsignal`, `valid_signals`) appears **only** inside the §V218.1.2 "Forbidden,
explicitly" prohibition list — named as forbidden, never invoked. The importer is
restricted to the CLI bootstrap module, and the call sites to
`NORMALIZE_REAPING_STATE`/`VERIFY_REAPING_STATE` at `c3n` and nowhere else
(statically testable, row 216). No other importer, handler, signal API, event,
path, schema, constant, token, or scientific cell is introduced (Engineering
constants: "Zero new constants … Exactly one import-allowlist delta").

Every superseded zero-delta assertion is enumerated (§V218.1.4, fourteen loci,
including the v1-draft §S5/§S0 claims, v2.1 §W2.6/§W6.4 parentheticals, and
v2.1.7's Engineering-Constants and §V217.7 statements). I found no operative
zero-delta claim left un-superseded.

**Can this supervisor-layer review validly satisfy the signed harness's
reviewed-amendment clause?** Yes. The signed §9 of
`OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md` (lines 534–541) states the harness
"uses no `signal`/`threading`/`multiprocessing`/backend import" and that any such
change "requires a reviewed amendment to that allowlist." Both remain literally
true: the *harness* still imports no `signal` (§V218.1.2 forbids it in the harness,
batch-settlement, supervisor-serve, watchdog, controller, and worker modules), and
the `signal` import is confined to the supervisor CLI bootstrap. The clause
demands **a reviewed amendment** for the allowlist change; the two-line
independent X/Y review of these exact bytes, followed by Kirill's
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` token, **is** that
reviewed amendment, submitted for exactly the review the clause requires. This is
governance-consistent, not a silent reinterpretation: the correction states the
delta as an amendment, enumerates the `verification.py` mutation it will one day
require (16 → 17 members), and does not itself perform that edit. **No contract
conflict** with the signed harness or batch-settlement composites. (I note that
§V218.9's compatibility classification also carries — from a prior layer, not
introduced here — §W6.5's supersession of harness §5a's deadline sentence; that is
pre-existing and outside this layer's five findings, and it is disclosed rather
than concealed.)

### 2. Kernel disposition normalization

I independently checked the pinned semantics of
`signal.signal(signal.SIGCHLD, signal.SIG_DFL)` on the main thread:

- CPython routes it through `PyOS_setsig`, which on any `sigaction(2)` platform
  (Linux always) issues **one** `sigaction(SIGCHLD, &act, &oldact)` with a fully
  initialized `act`: `sa_handler = SIG_DFL`, `sigemptyset(sa_mask)`, and an
  `sa_flags` that on the pinned CPython (`requires-python >= 3.11`, confirmed in
  `pyproject.toml`) is `SA_ONSTACK` — which contains **neither** `SA_NOCLDWAIT`
  **nor** `SA_NOCLDSTOP`.
- Because `sigaction` replaces the **entire** disposition record (handler, mask,
  and flags together), this single call clears, atomically, both Linux auto-reap
  mechanisms: an inherited `SIGCHLD == SIG_IGN` (replaced by `SIG_DFL`) **and** an
  inherited `SA_NOCLDWAIT` (the fresh `sa_flags` omits it). The kernel's auto-reap
  condition in `do_notify_parent()` is exactly `SIG_IGN ∨ SA_NOCLDWAIT`, so after
  the call a terminating own child becomes and remains `EXIT_ZOMBIE`.
- The provenance analysis is correct: `execve`'s `flush_signal_handlers()`
  preserves `SIG_IGN` but clears `sa_flags` to `0`, so an exec'd CLI can inherit
  `SIG_IGN` but not `SA_NOCLDWAIT`; a fork-without-exec launcher inherits **both**.
  Clearing both is therefore mechanically required, and the single write does it.

**Clearing `SA_NOCLDWAIT` is mechanically warranted by the pinned call** — it is a
property of the `sigaction` *write*, not an unverified assumption about inherited
state (the v2.1.7 defect). The correction separates cleanly what
`/proc/self/status` can prove (`SigIgn`/`SigCgt` bits ⇒ not-ignored and
not-caught ⇒ `SIG_DFL`) from what it cannot (`SA_NOCLDWAIT`, which Linux exposes
nowhere readable from `os`), marks the two underlying platform facts as
reviewer-verifiable, and backs the unobservable half with three independent
`CONTRADICTED` detectors. **No rejection.** (One non-load-bearing imprecision: the
parenthetical "earlier CPython sets 0" understates that `SA_ONSTACK` has been set
since CPython 3.7, not only 3.11; this is immaterial because only `>= 3.11`
governs and *both* `SA_ONSTACK` and `0` exclude the two `NOCLD` flags. Not a
finding.)

### 3. Pre-fork placement and failure closure

`c3n` is inserted between `c3` and `c4` (§V218.2.1). I traced every attempt from
lock entry (`c1`) through `SPAWNING.json` install (`c2`), the four channels (`c3`),
`c3n`, and the first fork (`c4`):

- `c3n` runs **in the CLI main thread of the main interpreter** immediately before
  `c4` — the only fork the CLI performs — so the disposition governing `pid_mid`
  is normalized from the child's first instant. Off the main thread `signal.signal`
  raises `ValueError` ⇒ `NORMALIZE_INCONCLUSIVE` ⇒ no fork (a premise enforced by
  its own failure, not assumed).
- **Every attempt re-executes `c3n` in full**; no cached "already normalized" flag
  may be consulted (§V218.2.1, test 225). A single long-lived CLI making a second
  attempt normalizes and re-verifies again.
- On **any** non-`NORMALIZED` result (`NORMALIZE_INCONCLUSIVE`, `VERIFY_FAILED`,
  `VERIFY_INCONCLUSIVE`) `PRE_FORK_FAIL_CLOSED` executes: **no `os.fork`**, no
  lease, no process record, no ownership — it cleans the eight bootstrap ends via
  `CLOSE_OWNED`, removes only its own `SPAWNING.json` while holding the lock, and
  returns a non-retryable named refusal. A `c4` fork that raises `OSError` never
  establishes ownership and falls into the same body. **No fork, lease, record, or
  later action occurs on any exception, unexpected disposition, `/proc`
  read/parse failure, wrong `SigIgn`/`SigCgt` mask, or non-`NORMALIZED` result.**
  Confirmed.

### 4. Sole reaper and complete wait surface

The sole-reaper contract (§V218.2.6) forbids, in the CLI, every wildcard/external
reaper: `os.wait()`, `os.wait3()`, `os.waitpid(-1|0, …)`, `os.waitid(P_ALL, …)`,
negative-pgid forms, any `subprocess`/`Popen` object, any helper thread, any
`atexit`/finalizer reaper, and any signal handler — each a **contract violation,
not a route** (statically asserted, rows 223/224). The five permitted sites W-1…W-5
are all targeted `os.waitpid(pid_mid, WNOHANG)`, mutually exclusive per attempt,
and none may run after `OWNERSHIP == REAPED`. Client-takeover phase 1 reaps nothing
(it runs pre-fork). For the result space: `(pid_mid, status) ⇒ PROVED_DEAD` (the
**only** entry to `T1`); `(0,0) ⇒ NOT_YET` (running or stopped); `EINTR ⇒` bounded
retry within the existing signed deadline; `ECHILD ⇒ INCONCLUSIVE_ECHILD +
CONTRADICTED`; other errno `⇒ INCONCLUSIVE_OTHER`; `WIFSTOPPED` impossible under
`WNOHANG` without `WUNTRACED`. **Only `waitpid == pid_mid` proves death.** Both
`ECHILD` and `ESRCH` (the latter in `SIGNAL_ATTEMPT`) under an owned, unreaped
child are treated as contradictions/inconclusive — **never** proof of death.
Confirmed.

### 5. Ownership, identity, and PID reuse

`OWNERSHIP ∈ {OWNED, CONTRADICTED, REAPED}` with exactly two transitions, each set
at one place; `os.kill(pid_mid, …)` executes **iff `OWNERSHIP == OWNED`** (§V218.3.1,
row 222). I reproduced the full ten-row `IDENTITY_OBSERVE` table (§V218.3.4):
I-1 matching capture (confirm); I-2 mismatching capture ⇒ contradiction (d), no
kill, earlier truthful capture stands ⇒ `T2`; I-3 uncaptured `ppid == getpid()` ⇒
capture; **I-4 uncaptured `ppid ≠ getpid()` ⇒ contradiction (c), no kill, no
capture ⇒ `B`** (X217-m1's exact case, safe direction); I-5 `ABSENT` (absence is
**never** death); I-6/I-7/I-8 `UNREADABLE`/`UNPARSABLE`/`ERROR` withhold durable
identity but ownership still carries the kill; I-9 `REAPED`-on-entry and I-10
`CONTRADICTED`-on-entry are explicit rows. The fork-ownership proof (§V218.3.2)
holds at every instruction boundary between `STAT_OBSERVE` and `os.kill`: the child
holds `pid_mid` from the instant `fork` returns and, under the normalized
disposition, becomes a zombie that keeps the pid until this route's own targeted
`waitpid` returns it — so no reuse can occur before the reap, including for a
stopped child (still a task holding the pid) and an unreaped zombie. **Every signal
is gated solely by `OWNERSHIP == OWNED`; none after reap or contradiction; no
PID-reuse inference is drawn from `/proc` absence** (`ABSENT` routes to
`WAIT_PROVE`, never to a kill or a death conclusion). Confirmed.

### 6. Terminal totality

`T3` is **absent** — verified by search and by re-derivation of §V218.4.2. Terminal
selection is `REAPED ⇒ T1`; `¬REAPED ∧ captured ≠ ⊥ ⇒ T2`; `¬REAPED ∧ captured =
⊥ ⇒ B`. These are **pairwise disjoint and exhaustive** over the product
(`OWNERSHIP` reaped/not) × (`captured` ⊥/non-⊥): `REAPED` covers both capture
values, the other two partition `¬REAPED`. Traces: a **stopped child** →
ownership-authorized `SIGKILL` (uncatchable) → zombie → `WAIT_PROVE` → `T1`, even
with `/proc` entirely unreadable; **completely unreadable `/proc`** → I-6/I-7/I-8
withhold identity but ownership carries the kill → `T1`, or (if no identity ever
captured) → `B`; **inherited auto-reap contradiction** → `ECHILD`/`ESRCH`/`ppid`
mismatch → `CONTRADICTED` → `T2` (if earlier capture) or `B-CONTRADICTED`;
**long-lived CLI** → every *returning* terminal removes the CLI's own
`SPAWNING.json`, so no future P2b is triggered by a live-CLI record; **crash/restart**
and a **new CLI** are tabulated in §V218.6 with a single continuation each and no
record naming a possibly-live process removed without an authoritative reap or a
signed §U6.1 P3 death proof.

**`B-CONTRADICTED`'s non-return is an honest fail-closed terminal, not an unbounded
silent wedge.** It arises only when the pinned premise is *violated* (a
`SA_NOCLDWAIT` the readback cannot see, a sole-reaper-contract breach, or a hostile
same-UID `ppid` mismatch) **and** no truthful identity was ever captured. In that
state the route holds `SPAWN.lock` + `SPAWNING.json` + the in-process handle and
loops on `WAIT_PROVE`; it emits **no** refusal, event, ledger entry, capacity or
custody artifact, or scientific/resource statement. It does not misclassify valid
history (no false `PROVED_DEAD`, no false `INVALID`), does not abandon a live own
child (the child that produced the contradiction was reaped by something else, so
`pid_mid` denotes nothing of ours to abandon), and does not signal an innocent
recycled pid (kill is gated off). The only alternatives to the visible stall —
returning while signalling a possibly-recycled pid, or declaring a possibly-live
child dead — are exactly the harms the required question forbids. The wedge is
**named** (residual 3), visible (a held lock, not a false result), and reachable
only under a contract violation; it is not the prohibited silent wedge the v2.1.6
lineage removed (which struck under *normal* operation). Judgment below.

### 7. T2 residual

I confirmed `T2`'s route is total and free of a competing reaper. `T2` installs the
already-signed `SPAWNING_MIDDLE.json` with the signed `c7` key set, every field an
**observed** value captured while `OWNERSHIP == OWNED` (nothing fabricated),
removes only `SPAWNING.json`, and **retains `pid_mid` in memory** so a later attempt
in the same process reaps it at W-4 (§U6.1 P3). The surviving record is resolved by
the **existing** §U6.1 P0/P1/P2a/P2b/P3 and §U2.5 `s4`/`s5` routes — I checked each
case maps to a pinned continuation with **no new tier, record, schema, resolver, or
operator step** (§V218.4.4). No competing reaper exists: the middle's zombie is
released only by its parent's `waitpid` (W-4) or the parent's exit; a *different*
CLI never `waitpid`s it, but proves death by `/proc` absence or state `Z` with
matching identity — which the zombie satisfies **precisely**, so the record does
not block progress. The zombie holds **no descriptors and no `SPAWN.lock`
reference**, so it never wedges the singleton; it is bounded (at most one
outstanding per process between attempts, since the next attempt's P3/W-4 clears
the prior). A zombie can persist for the CLI's lifetime only for a long-lived CLI
that never retries — which the contract states exactly and which blocks nothing.
The two honestly-stated liveness limits (a resolver that also cannot read `/proc`
refuses retryably via `s5`; `s4` proves death by `/proc`, not `waitpid`) are
correct fail-closed behaviour, not misclassification. Confirmed total and
non-competing.

### 8. Causal and TOCTOU regression

The corrected stage-M proof rests at **`m0`/`rel1`/fork-shared lock**, never
`m5`/`rel2` (§V218.5.1): no `c8` byte on the fresh `rel1`; the middle is at `m0`,
still owns its inherited `rel1_w`, so EOF at `m0` is impossible; `m1`/`m2`/`m4`/`m5`/`m7`
unreachable; the fork-shared lock serializes the next CLI. Every `m5`/`rel2`
occurrence is a deletion record, an unreachability assertion, a test row, or the
§V218.5.3 retention scoped to cuts at or after `c8` — no operative `c5`–`c7`
continuation cites them.

I re-ran the v2.1.7 no-regression surface. **§V217.1 in full** (object-bound
`OBSERVE` O1–O9, both revalidation barriers `BRANCH_ENTRY`/`DISPOSITION`, the
`R-a`/`R-b` same-rule requirement, `bytes_sha256` binding, the A3 residual honesty,
the mutation-cut table) and **§V217.4 in full** (the ten-locus bound-language
replacement, eighteen search terms, retained-statement table, revised row 86, D1's
true ground) are carried byte-for-byte, and both were confirmed closed by *both*
v2.1.7 lines. `CLOSE_OWNED` at every site including both lock closes; `MALFORMED`
physical-presence dominance and the §V216.1.2 rule ordering; §V216.1.3 sub-routing
and cross-product; the three branch bodies `B-P`/`B-QM`/`B-QN` (unrelated to this
layer's stage-M `B` label); §N2.3 P1–P7 custody and §V214.2.4 reconciliation; K1's
five constants and one-release accounting; death-before-unlink for the three
records naming other processes; §V216.5's eight-end audit and `boot_w` provenance;
§V216.4.1's pipe-only invariant; GC order with `accepted.json` last; the watchdog
partition; the singleton preflight; the generic-harness and batch-settlement
composites; the nine events; E1/E2/E3; the Q/C boundary; and T inactivity — all
carry. `B`'s unbounded loop is *consistent with* §V217.4's already-withdrawn
fixed-total-CLI bounds and reintroduces no contradiction (revised row 86 remains
satisfiable). No selector, custody, capacity, or filesystem rule is disturbed.
Confirmed no regression.

---

## Findings

**No Critical, Major, or Minor finding survived re-derivation.** All five inherited
findings are closed by exact text; the eight attacks each pass. One non-blocking
observation is recorded for completeness — the §V218.2.2 parenthetical "earlier
CPython sets 0" understates that `SA_ONSTACK` has been set since CPython 3.7 — but
it is immaterial to the pinned `>= 3.11` target and to the load-bearing claim
(neither `NOCLD` flag is set), so it does not affect the verdict.

---

## No-regression table

| Signed / inherited surface | Status under v2.1.8 |
|---|---|
| **§V217.1 object-bound observation + both barriers + A3 residual + mutation cuts** | Carried byte-for-byte; untouched. The reaper repair proves **nothing** about filesystem exclusion; `T_RUNTIME.lock` still serializes contract actors only. |
| **§V217.4 bound-language replacement** (ten loci, search terms, retained table, row 86, D1 ground) | Carried byte-for-byte; `B`'s unbounded loop reintroduces no fixed-total-CLI contradiction. |
| **§V216.2 `CLOSE_OWNED`** at every site incl. both lock closes | Carried byte-for-byte; `B` defers cleanup to whichever terminal it exits into. |
| **`MALFORMED` dominance / §V216.1.2 rule ordering / §V216.1.3 cross-product** | Carried byte-for-byte. |
| **Three branch bodies `B-P`/`B-QM`/`B-QN`** | Carried byte-for-byte (distinct from the stage-M `B` control label). |
| **K1 custody & accounting**, §N2.3 P1–P7, §V214.2.4 reconciliation | Carried byte-for-byte. |
| **Death-before-unlink** (§V216.3, §V217.3.1 table) | Carried and **strengthened**: the only unproved removal remains self-naming `SPAWNING.json`, and `B` does not even perform that. |
| **§V216.5 eight-end audit / §V216.4.1 pipe-only invariant** | Carried byte-for-byte. |
| **Bootstrap / forks / gates / GC / watchdog / singleton preflight** | Carried; the only additions are step `c3n` and the stage-M automaton. |
| **A3 / B1 / C1 / D1 / K1** | No cell reopened. A3 gains one new *named* residual (the zombie) and one *narrowed* one (`B` replaces v2.1.7's every-`T3`-case exposure). B1/C1/D1/K1 unchanged. |
| **Generic harness v2→v2.3.1 / batch settlement v1→v1.1.1** | Referenced unchanged; the `signal` delta **honours** the harness §9 amendment clause rather than contradicting it. |
| **Nine events / E1/E2/E3 / Q/C boundary / T** | Unchanged; every fact added here is control-plane, T-development-only, and non-citable. |

Overall: every signed surface carries, and the stage-M kill-safety property that was
the sole v2.1.7 defect is now sound.

---

## Explicit judgment on the two admitted residuals

1. **The new unreaped-zombie residual (residual 1).** **Accepted as correctly and
   completely scoped.** It is created by the necessary normalization; it holds one
   pid slot, no descriptors, and no lock reference (so it never wedges the
   singleton); it is bounded (≤ one outstanding per process between attempts);
   it is resolved by W-4 or by CLI exit; it is `/proc` state `Z` with a matching
   identity and is therefore **positively useful** as another process's §U6.1 P3
   death proof; and it is an A3-class resource residual, permanently non-citable
   and forbidden from selection/Q/C/blinding. Nothing about it can be read as a
   scientific or resource outcome.

2. **`B-CONTRADICTED` non-termination (residual 3), and `B-OWNED` (residual 2).**
   **Accepted as honest fail-closed states, not concealed wedges.** `B-OWNED` fails
   to terminate only under a same-UID `SIGSTOP` conjoined with a persistent signal
   fault unreachable for an own child at the same UID on the pinned host; a normally
   executing middle exits at its own `m0` bound and is reaped. `B-CONTRADICTED`
   holds the lock indefinitely only when the pinned premise is *violated* — i.e.
   under a contract violation or hostile same-UID environment — conjoined with a
   `/proc` fault so severe that no identity was ever captured; under a conforming
   host and implementation it is unreachable. In both cases the alternative to the
   visible stall is a false death proof or a signal to a recycled pid, which the
   required question forbids. Both are named in §V218.4.5, emit nothing citable, and
   preserve D1 (no supervisor waits on `SPAWN.lock`). This is the correct
   fail-closed direction.

---

## Author-cell and contract-conflict determination

**No scientific author cell is reopened, weakened, or reinterpreted.** The embedded
A3/B1/C1/D1/K1 selections are carried verbatim. The repairs are mechanical
process-identity, reaper, terminal-totality, and causal-proof corrections. The one
signed-engineering-surface change — adding `signal` to `ALLOWED_ABSOLUTE_IMPORTS` —
is an **engineering** amendment, not a scientific choice, and no new author-choice
token is proposed or required. **No contract conflict** exists with the signed
generic-harness composite or the signed batch-settlement amendment: the harness §9
import-discipline clause is *honoured* (the harness itself imports no `signal`), and
this supervisor layer *is* the reviewed amendment that clause anticipates. The
`verification.py` mutation (16 → 17 members) is specified, not performed; the file
is unedited and its digest matches.

## Authorization boundary

Because this X verdict is **CONFIRM**, Kirill's token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

is authorized **only conditionally**: it becomes signable if and only if the
independent **Y line also confirms the identical bytes** (digest
`33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50`). Until that
matching Y confirmation exists, the token remains **unavailable** and is not made
signable by this review alone.

This review authorizes **no** implementation, no commit of any dirty/untracked
implementation, no edit of `verification.py` or any code/test/contract/signature/
review/prompt, no `signal` allowlist edit, no T activation, no entropy, no runtime
construction (supervisor, controller, worker, watchdog, adapter, middle child,
grandchild, endpoint, pipe, FIFO, journal, spawn record, capability, lease,
operation, capacity artifact, custody disposition, author decision file,
freeze/fallback witness), no E1/E2/E3 spend, no Q/C work, no scientific work, and
no later gate.

## Custody and programme state

No repository code, test, probe, smoke command, or Officina process ran; this
review started no process of its own. The only computations were `sha256sum`,
`git` ancestry/status, directory listing, and text search over documented bytes,
in read-only inspection. No code, test, contract, signature, prior review, prompt,
or runtime artifact was edited; nothing was committed or staged; the pre-existing
dirty and untracked handover paths are preserved unmodified. Exactly one new file
was created — this review. No T/Q/C, runtime, capacity, custody, result-manifest,
entropy, world, learner, candidate, datum, outcome, or scientific artifact was
created.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
