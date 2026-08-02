READY_FOR_OFFICINA_SUPERVISOR_P1_PRE_XY_REPAIR_FINAL_CONFIRMATION

# Author closure — Officina supervisor/control-channel v2.1.10.6 pre-X/Y repair

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only.** Not an
independent X-line or Y-line reviewer of this chain.

**This closure is an untrusted self-assessment**, as
`reviews/officina_supervisor_v2_1_authorship_note.md` requires. **Both defects
repaired here were in my own bytes**, and a single static audit found them —
the third such round. This layer does not self-confirm.

## Byte and hash custody

Repository base: commit `c9f883d98375c0d961dae4821b44e0a2a818bd65`. The working
tree was already dirty at handover; every pre-existing tracked modification and
untracked path is preserved byte-for-byte.

Governing inputs, read in full and recomputed:

```text
798d0cbd51e93cc1f4c0a443785f90d90a2e121d35738189cbee9c61acf557cc  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md
68cf3b872f54346c2c03f646644318f585b51b99cf12cf037ce4cf1159c58041  reviews/opus5_officina_supervisor_control_channel_v2_1_10_5_p1_pre_xy_repair_closure.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

This closure's companion:

```text
8f806e33d85c00933871072dadda30110f18ea6bf34b5ebc388f23f8b067143e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md
```

**Exactly two files were created and nothing else was touched.** v2.1.10.5,
v2.1.10.4, v2.1.10.3, the P1 signature, every earlier layer and closure, the
A3/B1/C1/D1/K1 and output-capacity signatures, the harness and batch composites,
the authorship note, and `verification.py` are all unedited and match their
digests. `scripts/officina_process_control_bootstrap.py` and
`scripts/officina_role_bootstrap.py` do not exist. No code, test, verifier,
manifest, prompt, prior review, or runtime object was edited, staged, or
committed. Method: static authoring only — read-only file and `git` inspection,
literal search, `sha256sum`, and reasoning from pinned Linux/CPython interfaces.

## Verdict

`READY_FOR_OFFICINA_SUPERVISOR_P1_PRE_XY_REPAIR_FINAL_CONFIRMATION`.

Both defects close **without** a new author choice, a new process, a new
syscall or import, or any change to the signed P1 authority topology. In
particular the R1 item-4 branch — "if any carried decision actually relies on
exclusive init reaping or on preservation of an exit status, identify it and
stop with `BLOCKED_…`" — was tested and **does not fire**: §P1S.1.6's audit
finds exactly one status-dependent decision, and its target is never an orphan.
No `BLOCKED_…` is owed.

## Replacement index

| # | Locus | Action |
|---|---|---|
| 1–4 | v2.1.10.5 §P1R.2.1's two `init` clauses, §P1R.2.3's supervisor-row cell, test row 493 | replaced by the adopter semantics |
| 5 | v2.1.10.4 §P1B.2's tree line "re-parented to init" and its edge-table cell | replaced |
| 6 | v2.1.10.4 §P1B.8.2's "re-parented to init, which reaps them" and "init reaps it" | replaced |
| 7 | carried v2.1 §W2.1's parenthetical "**after the double fork its parent is `1`**" | **deleted as false**; the sentence's actual claim — `getppid()` is **not** used for the supervisor grandchild — is retained and re-affirmed, and is now load-bearing |
| 8 | v2.1.10.4 §P1B.9's `S-5` clause insofar as it implied init reaping | extended |
| 9 | the carried zombie-residual clause "reaped … by `init` after the CLI exits" | replaced |
| 10 | v2.1.10.4 test row 458 | replaced by 458R |
| 11 | v2.1.10.4 §P1B.11 rule **`S-18`** | **replaced** by `S-18'` (three pinned sites, per-site permission) |
| 12 | v2.1.10.4 test row 445 | replaced by 445R |
| 13 | v2.1.10.2 §T8 test row **359** ("`/proc/self/fd` contains exactly the pinned set") | **replaced** by 359R — the supervisor has no static pinned set; it grows with every live handle |
| 14 | v2.1.10.5 §P1R.5.2's sweep row "`S-18` forbids it" | replaced — the prohibition is phase-scoped, not universal |
| 15 | v2.1.10.2 §T8 row **425** ("never enumerated **for remediation** anywhere") | **retained unchanged** — already correctly scoped |

**Explicitly unchanged and re-confirmed:** the P1 selection; A3, B1, C1, D1, K1
and the output-capacity selection; the process topology and the PCS authority
boundary; v2.1.10.5's F1–F5 in full; nine opcodes; five roots; 6 / 3 / 17
imports; `CMSG_SPACE(12)` and the 3-descriptor maximum; §P1B.6.2's
`scm_detach_fds()` fact.

## One-to-one R1 / R2 disposition

| Req | Disposition |
|---|---|
| **R1.1** replace every absolute claim | Every operative `init` / `pid 1` / "re-parented to init" clause is replaced by *"re-parented to the nearest still-living ancestor subreaper, and to the PID namespace's init only if no such ancestor exists; that adopting process is the one that may reap it."* Seven loci are tabulated in §P1S.1.2, including two the brief did not name: carried v2.1 §W2.1's "its parent is `1`", and the carried zombie residual |
| **R1.2** recompute tables and the four crash cuts | §P1S.1.3 gives a seven-column parent/adopter/reaper/authority table; §P1S.1.4 gives supervisor orphaning after `m9`, supervisor exit, PCS death, role exit after PCS death — plus a fifth row proving the **group anchor** `pid_mid` is a direct PCS child and therefore never orphaned while the PCS lives, so subreaper semantics cannot touch the post-`c11` `killpg` route |
| **R1.3** what a contaminated ancestor subreaper can reap and steal | §P1S.1.5, in two tables. It **can** become parent of the supervisor after `m9` and of `pid_mid`/roles after PCS death, reap them including by wildcard wait, learn each PID and wait status (values from a closed set carrying no scientific, capacity, custody, resource or Q/C content), delay or hasten reaping, and kill or stop what it adopts. It **cannot** obtain any descriptor or capability, make `/proc` report absence for a live process, forge or block a death proof, or gain Officina process authority |
| **R1.4** prove or reject the bounded interpretation | **PROVED.** §P1S.1.6 audits every consumer of a wait result or exit status in the composite. **Exactly one decision branches on a status word** — `AWAIT_STOP`'s carried `WIFSTOPPED` requirement — and its target is a **direct child of the PCS**, never an orphan. Every other consumer uses the returned **pid** of the PCS's own child, an object-bound `/proc` fact (absence, state `Z` with matching start identity, or a start-identity mismatch), or a channel EOF. The caller's view of the PCS already treats the exit status as advisory with the pipe reply authoritative. **No carried decision relies on exclusive init reaping or on preservation of an orphan's exit status**, so the `BLOCKED_…` branch does not fire |
| **R1.5** add nothing architectural | §P1S.1.7: **no** `prctl`, `PR_SET_CHILD_SUBREAPER`, `ctypes`, subreaper role, long-lived middle, PID namespace, cgroup, new signal path, or adoption/recovery protocol. Import closures and root count unchanged; `S-24` enforces it |
| **R1.6** keep A3 honest | §P1S.1.8: a contaminated ancestor may already kill, stop, delay or reap what it adopts, exactly as the carried A3 rescope says. **Nothing is upgraded into adversarial confinement**; the surface stays procedural and non-citable |
| **R1 grounding** | §P1S.1.1 names the primary interface fact — `prctl(2)`, `PR_SET_CHILD_SUBREAPER`: a subreaper "fulfills the role of `init(1)` for its descendant processes"; the orphan re-parents to the **nearest still-living ancestor subreaper**, `getppid()` returns that subreaper, and the subreaper receives `SIGCHLD` and may `wait(2)` for the status; only absent any such ancestor does namespace init receive it — and marks it **reviewer-verifiable**, with no probe executed |
| **R2.1** define who may enumerate, and whether they may close | §P1S.2.2's seven-row phase/permission table |
| **R2.2** permit `A-5` read-only | permitted, **read-only**, and re-affirmed as a verification rather than the mechanism (carried from v2.1.10.5 §P1R.1.6) |
| **R2.3** permit `G-5` bounded, with a disjointness proof | permitted with the pinned keep-set `{0,1,2}` ∪ slots `3…10`. §P1S.2.3 proves it cannot touch a live supervisor handle: `G-5` runs before `G-6`'s `execve`, hence before `A-10` and `A-13`; a role handle's descriptors reach the supervisor **only** by `SCM_RIGHTS` after its first `SPAWN_ROLE`, which is after `A-13`; and `G-5` acts only on its own inherited table. The same argument covers `P-f`, which precedes the PCS's first fork |
| **R2.4** keep forbidding the supervisor sweep | forbidden in the `SCM_RIGHTS` receive path, in any runtime error remediation, in any handle-release path, and in any phase where unrelated live role handles coexist |
| **R2.5** preserve the parser-local cleanup and the `_exit_` rule | both **explicitly preserved**; neither is replaced by a sweep |
| **R2.6** recompute `S-18` and every affected row; no "nowhere" may survive | `S-18` → `S-18'` with two distinct failure results; rows 359R, 442R, 445R recomputed; row 425 retained because it was already remediation-scoped. **No sentence equivalent to "nowhere" survives** |

## Corrected parent / reaper / authority table

| Process | Direct parent | Adopter if orphaned | Direct children | May `wait` on | May signal | Holds numeric PIDs of |
|---|---|---|---|---|---|---|
| caller | host | — | the PCS | the PCS only | nothing | the PCS |
| **PCS** | caller | nearest living ancestor subreaper, else namespace init | `pid_mid`, controllers, workers, watchdogs | exactly those | exactly those, plus the supervisor's **group** only after `c11` | exactly those |
| middle (`pid_mid`) | PCS | as above (only if the PCS dies first) | grandchild until `m9` | nothing | nothing | none |
| **supervisor** | `pid_mid` until `m9`, then **its adopter** | nearest living ancestor subreaper, else namespace init | none | nothing (`ECHILD`) | nothing | **none — handles only** |
| watchdog | PCS | as above | none | nothing | nothing | none |
| controller / worker | PCS | as above | per carried contracts | unchanged | unchanged | none |

## Corrected `/proc/self/fd` phase / permission table

| Root | Phase | Enumerate | May close | Rule |
|---|---|---|---|---|
| PCS bootstrap | `P-f`, pre-fork | **yes** | **no** | exact set `{0,1,2,3,4,5,6,7,8}` + the transient listing fd; deviation ⇒ refuse, no fork |
| role bootstrap | `A-5`, before any project import | **yes** | **no** | exact set `{0,1,2}` ∪ slot set; deviation ⇒ `os._exit(3)` |
| grandchild | `G-5`, before `G-6`'s `execve` | **yes** | **yes, bounded** | close everything outside `{0,1,2}` ∪ slots `3…10`; ascending, once each, `EBADF` tolerated |
| supervisor | `SCM_RIGHTS` receive and its error path | **no** | **no** | parser-local rule only: close exactly the parsed vector |
| supervisor | any runtime remediation / handle release / shutdown | **no** | **no** | forbidden |
| any root | any phase where unrelated live role handles coexist | **no** | **no** | forbidden |
| PCS | any phase after the first role handle exists | **no** | **no** | forbidden |

## No-regression

| Surface | Status |
|---|---|
| **F1** lock `O_CLOEXEC` + readback, `G-1`…`G-6`, fork-shared-lock theorem, `A-5` as verification | unchanged; `G-5` is re-affirmed as a permitted bounded scrub, which F1 already required |
| **F2** authority boundary, supervisor outside the PCS child set, post-`c11` group route | unchanged in substance; only the `init` cell becomes the adopter semantics |
| **F3** one watchdog rule, no signal on any path | unchanged |
| **F4** withdrawn no-callback theorem, `S-19` AST-only, named capability exposure inside A3 | unchanged and explicitly preserved |
| **F5** non-aborting `B-2`/`B-3`, `B-4` the only actor | unchanged and explicitly preserved |
| **P1 selection**; **A3 / B1 / C1 / D1 / K1**; output-capacity selection | unchanged; no option reopened; C1's one-detector model and `getppid()`-ignoring watchdog stand, and §P1S.1.2 row 7 makes the latter more clearly correct |
| topology, nine opcodes, five roots, 6/3/17 imports, `CMSG_SPACE(12)`, 3-fd maximum | unchanged |
| object-bound observation, both barriers, bound-language sweep, `CLOSE_OWNED`, custody P1–P7, §Z3.3 layout, §Z3.2 role enum | carried byte-unchanged |

## Exact future implementation / verifier / test surface

**Verifier:** `S-18` → `S-18'`; `S-23` (no absolute init adoption claim),
`S-24` (no `prctl`/`PR_SET_CHILD_SUBREAPER`/`ctypes` in any production root),
`S-25` (no wait-status branch off the direct-child path) added. CHANGES 1, 2, 4,
5 and rules `S-1'`…`S-17`, `S-19`…`S-22` unchanged.

**Tests:** 359R, 442R, 445R, 458R, 493R replaced; 501–513 added.

**Files:** `scripts/officina_process_control_bootstrap.py` and
`scripts/officina_role_bootstrap.py` (neither exists);
`src/philosophia/officina/verification.py` (CHANGES 1–5 plus the three new
rules, nothing else); `PRODUCTION_CALL_GRAPH.json`; `generic_harness.py` and the
test modules — the last two being **untracked Cursor work, preserved
byte-for-byte**. Everything else byte-unchanged.

## Weakest points against my own repair

1. **R1 makes the contract truthful, not stronger.** The composite now admits a
   contaminated ancestor may parent and reap the supervisor and every role after
   PCS death. Safety rests on §P1S.1.6's audit of every wait-status consumer; a
   single missed consumer would falsify it. `S-25` and row 504 are the guard and
   the first thing a reviewer should attack.
2. **`AWAIT_STOP`'s `WIFSTOPPED` is the single status-dependent decision**, safe
   only because its target is a direct PCS child. Any future layer moving that
   handshake off the direct-child path would break the proof silently.
3. **`S-18'` is a named whitelist**, single-valued today but brittle: a future
   phase needing a topology check must amend the rule rather than inherit a
   principle. I chose explicitness over generality.
4. **`G-5`'s disjointness proof is temporal**, defeated by any future change
   letting the grandchild receive descriptors before `execve`; only the ordering
   forbids it.
5. **The `prctl(2)` semantics are stated, not verified**, and are load-bearing
   for all of R1.
6. **Both defects were mine, found in one static pass — the third such round.**
   Weight this closure low; check §P1S.0's index and §P1S.1.6's audit literally.

## Bounded confirmation questions

Both lines review the **identical repair bytes** with the carried composite,
recompute every governing hash, and treat every author verdict — including this
one — as untrusted. §P1S.6 carries them verbatim.

**X = Claude Code Opus 4.8 / 5 — yes or no:** do these bytes correctly replace
every absolute `init` / `pid 1` claim with the nearest-living-ancestor
child-subreaper semantics, is §P1S.1.6's reliance audit complete (exactly one
status-dependent decision, target never an orphan), and does `S-18'` make
`/proc/self/fd` enumeration single-valued while preserving `P-f`, `A-5`, `G-5`
and forbidding every supervisor-side sweep — **without** reopening P1, the
topology, A3/B1/C1/D1/K1, or any F1–F5 closure? Verdict line 1 exactly
`CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_6_X` or
`REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_6`.

**Y = GPT-5.6 Sol — yes or no:** are both defects closed without a new author
choice, process, syscall or import, or any change to the signed P1 topology —
specifically, is §P1S.1.6 genuinely **proved** rather than assumed (so no
`BLOCKED_…` was owed), is §P1S.1.5's account of what a contaminated ancestor
subreaper can reap and learn complete and honest without upgrading A3 into
confinement, and is §P1S.2.3's `G-5` disjointness proof sound? Verdict line 1
exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_6_Y` or
`REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_6`.

Both lines: static review only — run no code, test, probe, or
process/socket/pipe/fork/exec/signal/wait/prctl operation; create exactly one
review file; modify nothing; authorize no implementation, activation, entropy,
spend, Q/C work, datum, outcome, Proof, or claim movement.

## Authorization boundary

**No acceptance token is available from this author round.**
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **unavailable**
and is not made signable here; it becomes available only if **both** independent
lines confirm the identical corrected composite. **This closure asserts no X/Y
verdict and does not self-confirm.**

This author round authorizes no implementation, no code/test edit, no
verifier/manifest change, no commit, no host change, no process or probe, no T
activation, no entropy, no E1/E2/E3 spend, no Q/C work, no datum, no outcome, no
Proof, and no claim movement.

**Confirmed: no code was written; no test or probe was run; and no
process/socket/pipe/fork/exec/signal/wait/prctl operation was performed.**

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
