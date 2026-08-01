REVISE_OFFICINA_SUPERVISOR_V2_1_7

# Opus 4.8 X-line: independent final confirmation of Officina supervisor/control-channel v2.1.7

Date: 2026-08-01
Reviewer line: X (adversarial Linux / process / signal / crash / hash-construction semantics)
Review base: commit `e965681` (HEAD), whose ancestry includes the required
`063d29042175e05d35eb3fee2b7403cca300c1a9` (verified with
`git merge-base --is-ancestor`). Working tree dirty exactly as handed over;
**nothing modified by this review** other than the creation of this one file.

**Independence.** I am Claude Opus 4.8 on a clean context. v2.1.7 was authored by
**Claude Code Opus 5 in the specification-author role** (Fable 5 unavailable). I
read the v2.1.7 closure and repair/chat responses **only as untrusted author
claims** and used none as evidence. I rebuilt the result from the normative bytes
(the full v2 → v2.1.7 chain, both signed author-selection files, the inherited
generic-harness v2.3.1 and batch-settlement v1.1.1 corrections, the authorship
note, and **both** v2.1.6 REVISE reviews). Both independent lines revised v2.1.6;
there was no formal X verdict for v2.1.5; no earlier confirmation carries across.

## Recomputed hash and base

Target digest, `sha256`:

```text
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
```

This **matches the expected value exactly**. Every governing hash printed in
v2.1.7 §"Governing hashes" reproduces byte-for-byte, including the two inherited
v2.1.6 reviews it must answer:

```text
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md
e395da8b6366b35da19dfeaf28a0fb25bedd9e07245ffb97b60f7f3b870ad9db  reviews/opus_officina_supervisor_control_channel_v2_1_6_final_confirmation.md
b38488cfeb422f16eda48561d5706d160ca7dc25969533e32265fa8a31c648c8  reviews/sol_officina_supervisor_control_channel_v2_1_6_final_confirmation.md
c8551990a9a794eb907ed31ab29488bb019c2e4d94783c713f66f3426f063906  reviews/sol_officina_supervisor_control_channel_v2_1_5_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
```

**Method.** Static, read-only. No repository code, test, probe, smoke command,
supervisor, controller, worker, watchdog, adapter, endpoint, pipe, journal, or
other Officina process ran. The only computations were `sha256`, `git`
ancestry/status, directory listing, and text search over documented bytes, plus
literal reasoning about Linux/CPython process semantics. No existing file or
runtime state was altered.

## VERDICT

```text
REVISE_OFFICINA_SUPERVISOR_V2_1_7
```

v2.1.7 **genuinely closes all five inherited findings** — Sol C1, M1, M2 and Opus
X216-M1, X216-m1 — by exact text I re-derived from the predicates, the syscall
enums, the terminal table, and an independent whole-chain bound-language sweep.
The object-bound selector + two barriers, the total stage-M syscall automaton,
the SPAWNING-only wedge removal, and the CLI-total-bound deletion are each sound.

But required **attack item 4** exposes a **new Major, X217-M1**, in the very
machinery v2.1.7 adds. §V217.2.4's `ECHILD ⇒ PROVED_DEAD` rule *and* its
PID-reuse safety ("a terminated child is a zombie whose pid cannot be
reassigned") both rest on the premise that the middle child is **never
auto-reaped**. v2.1.7 pins that premise only by "this contract installs no signal
disposition anywhere (`signal` is outside `ALLOWED_ABSOLUTE_IMPORTS`)." That is a
**non-sequitur**: on Linux a `SIGCHLD == SIG_IGN` disposition is **inherited
across `execve`**, so an ancestor/launcher can hand the CLI an auto-reaping
disposition the contract neither resets nor can even observe — because `signal`
is not importable. The premise is therefore **not mechanically pinned before
fork**, and per attack 4's stated criterion the `ECHILD` rule and the
zombie-pid-reservation must be rejected as written. The required question gates on
"no ... false death proof, untracked live process" and "no new ... Major," so the
token remains unavailable.

The defect is a single bounded repair, but — unlike the author's "zero import
delta" framing — the only repair that *preserves* the safety property touches the
signed import allowlist (reset `SIGCHLD` to `SIG_DFL` before the first fork). It
reopens no scientific author cell.

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT   — NOT signable
```

---

## Disposition of all five inherited findings

| Inherited finding (v2.1.6) | v2.1.7 locus | Independent disposition | Basis (re-derived) |
|---|---|---|---|
| **Sol C1** (Critical) — presence/validity not one object-bound snapshot ⇒ TOCTOU release of a canonical opposite terminal installed after its `P*` observation | §V217.1 | **CLOSED** | `OBSERVE` binds enumeration + `follow_symlinks=False` `lstat` + `O_NOFOLLOW/O_CLOEXEC` open + `fstat (dev,ino)==lstat (dev,ino)` + a full `pread` through the **retained** descriptor + `bytes_sha256`; every predicate consumes only that record; the fd is pinned for the epoch. Two barriers (`BRANCH_ENTRY`, `DISPOSITION`) re-run the identical algorithm and require unchanged paired-absence / identity / bytes / decode **and the same §V216.1.2 rule**. The exact Y-line attack (install `QUARANTINE.json` after `PQ=0`) flips `absence_paired` at barrier 1 ⇒ `R-a` fails ⇒ nothing released. Barrier 2 runs *after* the §N2.3 P1–P7 custody proof, catching the `QUARANTINE.json`-as-L2-control-record case Sol named. The "impossible by two independent conjuncts" claim is deleted; the post-barrier-2 window is named as the signed A3 residual, not claimed impossible (§V217.1.5). |
| **Sol M1** (Major) — `STAGE_M_ROUTE` does not classify unreadable/unparsable `/proc`, or `os.kill`/`waitpid` results | §V217.2 | **CLOSED for the enumerated syscall results, but its identity-safety totality inherits the X217-M1 premise defect** | `STAT_OBSERVE` (5 results), `SIGNAL_ATTEMPT` (5), `WAIT_PROVE` (3) each close over an exhaustive enum with a pinned continuation; "no exception may escape." `UNREADABLE`/`UNPARSABLE`/`ERROR` are not identity-safe (no kill, no unlink, no death). This is the exact repair Sol M1 and Opus X216-m1 demanded. **Caveat:** `IDENTITY_SAFE` has no branch for `PRESENT_VALID ∧ no captured identity ∧ ppid ≠ getpid()`; that case is unreachable *only under default `SIGCHLD`* (an own child, alive or zombie, always has `ppid==getpid()`), and becomes reachable under the inherited-`SIG_IGN` auto-reap of X217-M1. Closed conditional on the premise X217-M1 disputes. |
| **Sol M2** (Major) — stage-M fail-closed continuation permanently wedges a long-lived CLI via a `SPAWNING.json`-only survivor | §V217.3 | **CLOSED** | `SPAWNING.json` names only the CLI, so the abandoning CLI **always** removes its own `SPAWNING.json` on every terminal (T1/T2/T3) while holding the lock; no live long-lived CLI can leave one behind, so P2b can never be triggered by it. T2 installs the already-signed `SPAWNING_MIDDLE.json` (no fabricated field) resolved by the **existing** `s4` tier; T3-at-`c5`/`c6` leaves nothing; T3-at-`c7` leaves `SPAWNING_MIDDLE.json`. Death-before-unlink is preserved for the three records naming other processes. Two-supervisor safety holds by the `m5`-EOF argument (below), independent of `SIGCHLD`. |
| **Opus X216-M1** (Major) — Sol M3 not closed by *total* text: operative fixed-CLI-total-bound claims (§U2.4, §N12 row 86, §N3.5, §U2.7) contradict §V216.4.1; §V216.4's completeness assertions false | §V217.4 | **CLOSED** | I independently reproduced the declared search over all operative layers. The stale loci are exactly §N3.5 (v2.1.2:683–688), §N11 crash row (v2.1.2:1407), §N12 row 86 (v2.1.2:1462), §U2.4 (v2.1.3:375–377), §U2.7 residual-1 (v2.1.3:479) — all routed to §V217.4.3/§V217.4.4 replacement — plus the grandchild-gate loci already replaced in v2.1.5/v2.1.6. The false universal ("no statement anywhere") and false completeness ("no others") are deleted and replaced by scoped, reproducible claims. No additional operative fixed-total-CLI-bound statement survives; `v2.1.1 §Z... / §W2.2 / v2.1.1:613 "no unbounded waitpid inside a T_RUNTIME.lock epoch"` are true *specific* statements, correctly retained. Rows 86/121/126/159–162 are jointly satisfiable. |
| **Opus X216-m1** (Minor) — `STAGE_M_ROUTE` step 2 does not route a non-`ENOENT` unreadable/parse-failing `/proc` stat to fail-closed | §V217.2.1, §V217.2.5 | **CLOSED** | `STAT_OBSERVE` maps `EACCES`/`EPERM`→`UNREADABLE`, parse failure→`UNPARSABLE`, other→`ERROR`, all "not identity-safe ⇒ no kill, no unlink ⇒ §V217.3." Named as "Opus X216-m1's exact gap" and closed. |

All five inherited findings are answered by exact text. The verdict is REVISE only
because of the **new** X217-M1 in the added death-proof machinery.

---

## The eight required attack traces

### 1 & 2. Object-bound observation and the two barriers (Sol C1)

`OBSERVE` (O1–O9) is object-bound: presence is the negation of *paired* absence
(`ENOENT` **and** non-enumeration), so a symlink, directory, device, FIFO,
socket, multiply-linked, zero-byte, truncated, partially written, or replaced
object is **present + invalid**, never absence (O3/O4 + the O5 `ELOOP`/O6
`(dev,ino)` guard). The bytes hashed are read **through the pinned descriptor**
(O7), and `HS`/`HQ` consume `bytes_sha256`, so a manifest swap after the read
cannot change the compared value. A retained fd pins an inode, not a name — and
v2.1.7 acknowledges this exactly: barriers **re-`lstat` the canonical name** and
require the retained descriptor's `(fstat_dev,fstat_ino)` to still equal the
fresh `lstat`'s, plus unchanged paired-absence and the **same rule**. I mutated
each canonical name in every window: before O1 (observed state governs); O1↔O2
listed-then-removed (`OBSERVATION_INCONCLUSIVE`); O1↔O2 created-after-listing
(present, validity decides); O2↔O5 symlink (`ELOOP`⇒invalid), removed
(`INCONCLUSIVE`), replaced-regular (`(dev,ino)` mismatch⇒`INCONCLUSIVE`); O5↔O7
in-place rewrite (length/EOF/`fstat_size`⇒coherent or `INCONCLUSIVE`); O7↔O8
(decode uses already-read bytes); snapshot↔barrier1 opposite-terminal create
(**barrier 1 refuses — the exact Y-line attack**); branch↔barrier2 any change
(**barrier 2 refuses; no `.disposed.json`, no release**). Only the
**post-barrier-2** window remains, honestly signed as the A3 procedural residual
(§V217.1.5), never claimed impossible or citable. **Both barriers rebind the
canonical name and all three records to one coherent rule, or release nothing.**
Closed.

### 3. Stat/signal/wait automaton (Sol M1, X216-m1)

`STAT_OBSERVE`/`SIGNAL_ATTEMPT`/`WAIT_PROVE` enumerate every `/proc` result,
`SIGTERM`/`SIGKILL` errno, and `waitpid` result, with a deadline edge treated as
`≥`-expired, ordinary-exit races routed to `PROVED_DEAD`, and the reap boundary
("never signal/stat/wait on `pid_mid` after `PROVED_DEAD`"). No parser, signal,
or wait result escapes. The one residual gap in `IDENTITY_SAFE` (the
`ppid ≠ getpid()`-with-no-captured-identity case) is *unreachable under default
`SIGCHLD`* and becomes reachable only under the inherited auto-reap of
**attack 4**, to which it is subordinate.

### 4. `ECHILD` premise — **THIS TRACE FAILS (X217-M1)**

§V217.2.4 rests two load-bearing claims on "no auto-reaping":

1. `ECHILD ⇒ PROVED_DEAD` — "the only reaper is this route";
2. PID-reuse safety — "while the terminated child is unreaped it is a zombie and
   its pid cannot be reassigned, so every signal and stat before `PROVED_DEAD`
   targets this child or nothing."

Both depend on the middle child's death producing a **zombie** rather than an
auto-reap. v2.1.7 pins this only by "this contract installs no signal disposition
anywhere." I independently verified the launcher/inherited state and reject that
as sufficient:

- **`SIGCHLD == SIG_IGN` is inherited across `execve`.** On Linux, caught
  handlers reset to default at `exec`, but a disposition of `SIG_IGN` is
  **preserved**; CPython does **not** reset `SIGCHLD` at interpreter start (it
  touches `SIGINT`/`SIGPIPE`, not `SIGCHLD`). So any ancestor that did
  `signal(SIGCHLD, SIG_IGN)` before spawning the CLI leaves the CLI auto-reaping
  its children — a legitimate, common launcher/init/test-harness state.
- **The contract cannot pin or even observe the disposition.** The signed
  `ALLOWED_ABSOLUTE_IMPORTS` is exactly `os, fcntl, subprocess, time`; `signal`
  and `ctypes` are explicitly **outside** it (confirmed at
  `.../V1_DRAFT.md:472` and reasserted in v2.1.7's Engineering Constants). There
  is no `signal.signal(SIGCHLD, SIG_DFL)`, no `SIG_DFL`, no reset, no `pidfd`
  anywhere in the operative chain (grep clean). "This contract installs none" is
  precisely the phrasing attack 4 rules insufficient: **a disposition can be
  inherited, and the premise is not mechanically pinned before fork.**

Consequences under an inherited `SIGCHLD == SIG_IGN`:

- The *death conclusion* survives (a live child ⇒ `waitpid`→`0`; an
  auto-reaped dead child ⇒ `ECHILD`), so `ECHILD ⇒ dead` stays true. But the
  **PID-reuse safety is defeated**: a terminated child is auto-reaped *instantly*
  (no zombie), so its pid is free **before** the route reaches `PROVED_DEAD`.
  Between an identity-safe `STAT_OBSERVE` and the `os.kill` in `SIGNAL_ATTEMPT`,
  the child can die → be auto-reaped → its pid be reused by an unrelated same-UID
  process → `SIGNAL_ATTEMPT(pid_mid, SIGTERM/SIGKILL)` **signals the innocent
  process**. `os.kill` cannot check-and-signal atomically, and the whole
  no-wrong-kill guarantee rested on the (now false) zombie reservation. This is
  the "untracked live process" harm the required question forbids.
- Separately, `IDENTITY_SAFE`'s missing `ppid ≠ getpid()` branch becomes
  reachable (a reused pid whose new owner is not our child), and is unmapped.

**Severity — Major, not Critical, not Minor.** Not Critical: it requires an
atypical inherited disposition, corrupts no scientific/capacity/custody state,
harms only a same-UID process, and T is `NOT_ACTIVATED`. Not Minor: it defeats a
core safety property of the exact death/kill machinery this round adds, rests on
a **false universal in signed text** ("children are **never** auto-reaped"), and
the required question gates on it.

**Smallest repair.** Mechanically pin the premise before `c4`'s fork. The only
repair that *preserves* the safety property is to add `signal` to
`ALLOWED_ABSOLUTE_IMPORTS` and, as the CLI's first bootstrap action before any
fork, `signal.signal(signal.SIGCHLD, signal.SIG_DFL)` (this defeats an inherited
`SIG_IGN`; `SA_NOCLDWAIT` is already cleared by `exec`). Then `waitpid` sees
zombies, the pid-reservation holds, and both claims are true. This **touches the
signed import allowlist** — so the author's "zero import-allowlist delta" no
longer holds and must be surfaced as an allowlist amendment for X/Y re-review.
(Alternatives — a `pidfd` captured at fork and `pidfd_send_signal` for all kills;
or demoting the guarantee to a named launcher precondition and proving no wrong
kill can occur when it is violated — are strictly larger changes or cannot
preserve safety with `os.kill`.)

### 5. T1/T2/T3 recovery (Sol M2)

Long-lived CLI, stopped middle, unreadable `/proc`, every signal/wait error,
crash cuts and restart each map to exactly one terminal (§V217.3.2, §V217.3.5). A
stopped middle is reached by `SIGKILL` (uncatchable) ⇒ `WAIT_PROVE`⇒`PROVED_DEAD`
⇒ T1. T2 installs a **truthful, already-signed** `SPAWNING_MIDDLE.json` (every
field known) before removing `SPAWNING.json`, resolved by the existing `s4` tier.
T3 fabricates nothing and never erases a live middle's only handle when one
exists at `c7` (`SPAWNING_MIDDLE.json` survives). The CLI always removes its own
`SPAWNING.json`. Consistent and total. (The one residual — a deliberately
`SIGSTOP`ed, host-unobservable middle in T3 — is honestly signed as the A3
residual, strictly narrower than v2.1.6's every-long-lived-CLI wedge.)

### 6. Two-supervisor safety

For every scheduling cut a middle surviving T3 cannot become a second supervisor:
`m5` (stage-2 gate) requires the CLI's `c12` write on `rel2_w`; the abandoning
CLI has closed `rel2_w` via `CLOSE_OWNED`, and the middle closed its own `rel2_w`
copy at `m1`, so `m5` observes **EOF** and exits (or its bound expires first). A
middle that never passes `m5` never forks the grandchild and never installs
`SUPERVISOR_IDENTITY.json`. This holds for stopped/resumed middles, buffered
release data, inherited writer copies, timeout edges, and a new CLI starting
immediately after `SPAWNING` removal, and is **independent of `SIGCHLD`**. Sound.

### 7. Bound-language sweep

Reproduced independently over v2, v2.1, v2.1.1–v2.1.6 with the declared terms plus
`bounded proof`, `lock-hold`, `sufficient`, `healthy launch`, `30 s +`, `10 s +`.
The stale fixed-total-CLI-bound loci are exactly the ten enumerated
(§N3.5/§N11/row86 in v2.1.2; §U2.4/§U2.7 in v2.1.3; and the five already-replaced
grandchild/no-blocking loci). No additional operative total-CLI-bound survives;
`v2.1.1:613` and `§W2.2`/`§Z3.5` are true specific statements. Rows 86, 121, 126,
159, 160, 161, 162 are jointly satisfiable with `/proc`/installs/`fsync`s left
unbounded. Only lock acquisition and pipe reads/writes carry signed deadlines.
X216-M1 closed.

### 8. No regression

Verified below. Aside from the newly-introduced X217-M1, no earlier executable
rule is disturbed: §V216.1.2's rule structure and cross-product, §V216.2
`CLOSE_OWNED`, §V216.3.1, §V216.5's eight-end EOF audit, the three branch bodies,
K1 accounting, GC, watchdog partition, singleton preflight, manifest binding,
generic harness v2.3.1, batch settlement v1.1.1, the nine events, E1/E2/E3, Q/C
boundary, and T inactivity all carry verbatim.

---

## New findings

### X217-M1 (Major) — the `ECHILD`/no-auto-reap death premise is not mechanically pinned before fork; an inherited `SIGCHLD == SIG_IGN` defeats the PID-reuse safety

**Loci.** v2.1.7 §V217.2.4 ("**PID reuse.** While the terminated child is
unreaped it is a zombie and its pid **cannot** be reassigned…"; the `ECHILD`
bullet "children are **never auto-reaped**; the only reaper is this route"), and
test 199 ("`SIGCHLD` keeps its default and no child is auto-reaped"). Premise
source: the Engineering-Constants claim that `signal` is outside
`ALLOWED_ABSOLUTE_IMPORTS`.

**Defect.** "Installs no disposition" ⇏ "has the default disposition." On Linux a
`SIGCHLD == SIG_IGN` disposition is inherited across `execve` and is not reset by
CPython, so the CLI can inherit auto-reaping. The contract cannot reset or query
it (`signal` not importable), so the premise is unpinned and, within the current
allowlist, **unpinnable**.

**Failure scenario.** Launcher does `signal(SIGCHLD, SIG_IGN)`, then execs the
CLI. At stage M the route is identity-safe on `pid_mid` (STAT match). Before the
next `os.kill`, the middle exits; the kernel auto-reaps it immediately (no
zombie); `pid_mid` is reused by an unrelated same-UID process; `SIGNAL_ATTEMPT`
delivers `SIGTERM`/`SIGKILL` to that innocent process. The zombie-reservation the
route relies on to prove "targets this child or nothing" does not exist.

**Smallest repair.** As above: reset `SIGCHLD` to `SIG_DFL` before the first fork
(requires a one-line signed-allowlist amendment adding `signal`), restoring the
zombie reservation and making both claims true. Surface that this **is** an
import-allowlist delta, contradicting v2.1.7's "zero delta." Requires fresh X/Y
review of the amended bytes.

### X217-m1 (Minor) — `IDENTITY_SAFE` omits the `PRESENT_VALID ∧ uncaptured ∧ ppid ≠ getpid()` case

**Locus.** §V217.2.2. The five listed clauses do not cover a `PRESENT_VALID`
stat with no captured identity whose `ppid ≠ os.getpid()`. Under default
`SIGCHLD` this is unreachable (own child ⇒ `ppid==getpid()`), so it is
**non-blocking on the pinned target**; it becomes reachable only under X217-M1's
inherited auto-reap. **Smallest repair:** add one clause — "`PRESENT_VALID` with
no captured identity and `ppid ≠ getpid()` ⇒ not identity-safe; no kill; §V217.3"
— which also hardens the route against X217-M1's reuse window.

No new Critical survived re-derivation.

---

## No-regression table

| Signed / inherited surface | Status under v2.1.7 |
|---|---|
| **A3** | Preserved and made *more* honest: §V217.1.5 names the post-barrier selector window and §V217.3.4 the stopped-middle case as procedural, non-citable residuals; the four output residuals and the bootstrap residuals are untouched. |
| **B1** | Not reopened; no journal/ack/frontier/prefix/GC/classification change. |
| **C1 (watchdog)** | Not reopened; witness/freezer holds no lock/capability, settles nothing. |
| **D1** | No idle exit; the M2 wedge that could have blocked all future construction is removed; D1's true ground ("no supervisor waits on `SPAWN.lock`") is now stated (§V217.4.3). |
| **K1** | Five constants, one-write/one-hash, full reservation accounting, complete P1–P7 custody, three branch bodies unchanged; §V217.1's barriers **narrow** the release window. C1's TOCTOU release path is closed. |
| **Bootstrap / forks / CLOSE_OWNED** | Four nonblocking pipes, both middle gates, grandchild gate, verified `setsid`, pre-group `kill`/post-group `killpg`, fd remap, `CLOSE_OWNED` at every site including both lock closes — all carry. `m5`-EOF two-supervisor safety intact. |
| **Selector / manifest binding** | `MALFORMED` dominance, rule structure, cross-product, sole-pass tuples, orphan branch, no-content-reread — carry, now over object-bound facts. |
| **Singleton records** | Death-before-unlink preserved for `SPAWNING_CHILD/GROUP/MIDDLE`; only self-naming `SPAWNING.json` removed without proof; `s4` tier reused unchanged. **Stage-M kill safety is defective (X217-M1).** |
| **Author authority** | Derived path, acyclic disposition id, eight-line file, timestamp equality, manifest-bound id set, single use — unchanged; illustrative digests reproduce as in prior reviews. |
| **Generic harness v2.3.1 / batch v1.1.1** | §J1–§J3, §D1/§D2, nine events, inline `meter_evidence`, E1/E2/E3, roots, archival order — unchanged. |
| **Bound language / test obligations** | Rows 86/121/126/159–162 jointly satisfiable; only lock-acquire and pipe I/O carry signed deadlines. Closed. |
| **Q/C and T boundary** | No T activation, Q/C authority, spend, entropy, or science introduced; all new facts control-plane and non-citable. |

Overall: every signed surface carries **except** the stage-M kill-safety property,
which is the sole reason for REVISE.

---

## Author-cell determination

**No scientific author cell is reopened.** X217-M1 and X217-m1 are mechanical
process-semantics repairs over the already-signed A3/B1/C1/D1/K1 policy. However,
the minimal safety-preserving repair for X217-M1 **does** touch a signed
engineering artifact — the `ALLOWED_ABSOLUTE_IMPORTS` allowlist (adding `signal`
to reset `SIGCHLD`). This is not a new resource value, invalidity cause, custody
destination, scientific field, or author token, but it is an **allowlist
amendment** and must be reviewed as such; v2.1.7's "zero import-allowlist delta"
claim cannot survive the repair. No new author-choice token is required.

## Authorization boundary

Because the verdict is **REVISE**, Kirill's token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

remains **unavailable** and is not made signable. Confirmation would have
required this X-line verdict to be `CONFIRM_OFFICINA_SUPERVISOR_V2_1_7_X` **and**
the independent Y line to confirm the **same bytes** (digest
`789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8`); neither
condition is met here. The bounded repair (X217-M1's disposition pin plus
X217-m1's clause) must be prepared as a v2.1.8 layer and receive a **fresh
independent X-line and Y-line review** of its own bytes; no earlier confirmation
carries across.

This review authorizes **no** implementation, no commit of the untracked/dirty
implementation, no code or test edit, no T activation, no entropy, no runtime
construction (supervisor, controller, worker, watchdog, adapter, middle child,
endpoint, pipe, FIFO, journal, spawn record, operation, capacity artifact,
custody disposition, author decision file, freeze/fallback witness), no E1/E2/E3
spend, no Q/C work, and no scientific work.

## Custody and programme state

No repository code, test, probe, smoke command, or Officina process ran; this
review started no process of its own. The only computations were `sha256`, `git`
ancestry/status/listing, directory listing, and text search over documented
bytes, in read-only inspection. No code, test, contract, signature, prior review,
prompt, or runtime artifact was edited; nothing was committed or staged; the
pre-existing dirty and untracked handover paths are preserved unmodified. Exactly
one new file was created — this review. No T/Q/C, runtime, capacity, custody,
result-manifest, entropy, world, learner, candidate, datum, outcome, or
scientific artifact was created.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
