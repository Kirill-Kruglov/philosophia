# Officina supervisor and control-channel amendment — v2.1.10.6 pre-X/Y repair

Status: `P1_BOUND_REPAIRED_CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.
Layer prefix: **§P1S**.

> ## WHAT THIS LAYER REPAIRS
>
> Two remaining Linux-process defects, found by static audit before any reviewer
> time was spent. **Bounded correction only.** The signed
> `I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION` selection, the
> process topology, A3/B1/C1/D1/K1, the output-capacity selection, and all five
> v2.1.10.5 F1–F5 closures are **unchanged and re-confirmed** (§P1S.3).
>
> **R1 — "`init` adopts and reaps the orphan" is not a total Linux statement.**
> Under `PR_SET_CHILD_SUBREAPER` an orphan is re-parented to the **nearest still
> living ancestor subreaper**, and only if none exists to the PID namespace's
> init. Officina's own abstention from `prctl` proves nothing about a
> contaminated caller or a higher ancestor. Every absolute `init` / `pid 1`
> claim is replaced with the exact semantics (§P1S.1), and the proposed bounded
> interpretation is **PROVED, not merely asserted**: no carried decision
> anywhere in the P1 composite relies on exclusive init reaping or on the
> preservation of an orphan's exit status (§P1S.1.6). **No `prctl`, no `ctypes`,
> no subreaper role, no long-lived middle, no PID namespace, no cgroup, no new
> signal path, and no adoption or recovery protocol is added.**
>
> **R2 — `S-18` contradicted required verification.** "No `/proc/self/fd`
> directory enumeration appears anywhere" is false against the same contract's
> `P-f`, `A-5`, `G-5` and test 442R. The intent was narrower: forbid the
> **supervisor's remediation sweep**, which could close another live role's
> handle, while keeping bounded construction-time scrubbing and read-only
> topology verification. §P1S.2 replaces `S-18` with a **phase/permission
> table** that says which root, in which phase, may enumerate, and whether it
> may only inspect or may also close. **No sentence equivalent to "nowhere"
> survives.**
>
> The audit also caught two further affected loci the brief did not name:
> carried v2.1 §W2.1's parenthetical "**after the double fork its parent is
> `1`**", and v2.1.10.2 §T8 row **359**, which asserts a supervisor-side
> "pinned set" that in fact grows with every live role handle. Both are
> corrected here (§P1S.1.2 row 7, §P1S.2.4).

**Authorship.** Written by **Claude Code Opus 5 acting only as the specification
author**. This line wrote v2.1 through v2.1.10.5 and **cannot** serve as the
independent X or Y line for its own bytes
(`reviews/officina_supervisor_v2_1_authorship_note.md`). **Every prior author
verdict in this chain, including v2.1.10.5's, is an untrusted self-assessment,
and both defects repaired here were in my own bytes.** This layer does not
self-confirm.

**Signed state, carried unchanged:**

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
P: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
```

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable**. Creates nothing executable. Edits no existing file, code, test,
verifier, manifest, signature, prompt, prior review, or runtime artifact. Starts
no process, socket, pipe, fork, exec, signal, wait, or `prctl` operation. T
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes (recomputed)

```text
798d0cbd51e93cc1f4c0a443785f90d90a2e121d35738189cbee9c61acf557cc  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md
68cf3b872f54346c2c03f646644318f585b51b99cf12cf037ce4cf1159c58041  reviews/opus5_officina_supervisor_control_channel_v2_1_10_5_p1_pre_xy_repair_closure.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
5889461b86870c357a61e1b7327c1285773c4263dd9640bf3e2da202b9bde302  reviews/opus5_officina_supervisor_control_channel_v2_1_10_4_p1_binding_closure.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
d46414389187bb87068e5105a0a914a56f5f49f1244bdb5b527ccea89acba18c  reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_closure.md
c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

---

## §P1S.0. Literal replacement index over v2.1.10.5 and the carried chain

**Everything not named carries verbatim.** In particular v2.1.10.5 §P1R.1
(`SPAWN.lock`), §P1R.2 (authority boundary), §P1R.3 (watchdog signalling),
§P1R.4 (the withdrawn no-callback theorem), §P1R.5.1 (the non-aborting parse),
and every rule, count and table they carry.

| # | Locus, quoted | Action |
|---|---|---|
| 1 | v2.1.10.5 §P1R.2.1's clause "The orphaned supervisor is reaped by `init`." | **replaced** by §P1S.1.2 |
| 2 | v2.1.10.5 §P1R.2.3's supervisor row cell "`pid_mid` until `m9`, then **`init`**" | **replaced** by §P1S.1.3 |
| 3 | v2.1.10.5 §P1R.2.1's closing clause "`init` reaps it." (death proofs paragraph) | **replaced** by §P1S.1.2 |
| 4 | v2.1.10.5 test row **493** ("`init` reaps the orphaned supervisor") | **replaced** by §P1S.4.2 row 493R |
| 5 | v2.1.10.4 §P1B.2's tree line "`└─ m9 _exit ; [3'] re-parented to init`" and its edge-table cell "[2] until `m9`, then `init` \| `init`" | **replaced** by §P1S.1.2 and §P1S.1.3 |
| 6 | v2.1.10.4 §P1B.8.2's clauses "`pid_mid` and every role are re-parented to init, which reaps them" and "the watchdog … exits; `init` reaps it" | **replaced** by §P1S.1.4 |
| 7 | carried v2.1 §W2.1's parenthetical "`getppid()` is **not** used for the supervisor grandchild (**after the double fork its parent is `1`**)" | **replaced** by §P1S.1.2 row 7. The **claim that `getppid()` is not used is retained and re-affirmed**; only the false parenthetical about the parent being `1` is corrected |
| 8 | v2.1.10.4 §P1B.9's shutdown/`S-5` clause "the watchdog, if alive, exits at its own update-EOF route" insofar as it implies init reaping | **extended** by §P1S.1.4 |
| 9 | v2.1.10 §V218.4.5 / carried zombie-residual clause "reaped … by `init` after the CLI exits" | **replaced** by §P1S.1.2 |
| 10 | v2.1.10.4 §P1B.14 row **458** ("PCS death: `init` adoption …") | **replaced** by §P1S.4.2 row 458R |
| 11 | v2.1.10.4 §P1B.11 CHANGE 3 rule **`S-18`** ("no `/proc/self/fd` directory enumeration appears anywhere ⇒ 'global fd sweep present'") | **replaced** by §P1S.2.4's `S-18'` |
| 12 | v2.1.10.4 test row **445** ("no `/proc/self/fd` enumeration exists anywhere (`S-18`)") | **replaced** by §P1S.4.2 row 445R |
| 13 | v2.1.10.2 §T8 test row **359** ("after a violation, `/proc/self/fd` contains exactly the pinned set") | **replaced** by §P1S.4.2 row 359R — the supervisor has **no** static pinned set; it grows with every live role handle |
| 14 | v2.1.10.5 §P1R.5.2's sweep-row cell "global `/proc/self/fd` remediation sweep \| absent; `S-18` forbids it" | **replaced** by §P1S.2.4 (the prohibition is now phase-scoped, not universal) |
| 15 | v2.1.10.2 §T8 row **425** ("`/proc/self/fd` is never enumerated **for remediation** anywhere") | **retained unchanged** — it was already correctly remediation-scoped and is consistent with `S-18'` |

**Explicitly unchanged and re-confirmed** (§P1S.3 audits each): the P1
selection; A3, B1, C1, D1, K1 and the output-capacity selection; the process
topology and the PCS authority boundary; v2.1.10.5's F1 lock repair, F2 authority
wording, F3 watchdog rule, F4 withdrawn theorem, F5 non-aborting parse; the nine
opcodes; five roots; the 6 / 3 / 17 import counts; `CMSG_SPACE(12)` and the
3-descriptor maximum; §P1B.6.2's `scm_detach_fds()` fact; and every carried
signed surface.

---

## §P1S.1. R1 — orphan re-parenting, stated exactly

### §P1S.1.1 The primary interface fact

> **Linux `prctl(2)`, `PR_SET_CHILD_SUBREAPER` (Linux 3.4+).** A process marked
> a child subreaper "fulfills the role of `init(1)` for its descendant
> processes": when a descendant becomes orphaned, it is re-parented to the
> **nearest still-living ancestor subreaper**, `getppid()` in the orphan
> thereafter returns that subreaper's PID, and it is the **subreaper** that
> receives `SIGCHLD` and may `wait(2)` to obtain the termination status. Only
> **if no ancestor subreaper exists** is the orphan re-parented to the init
> process of its PID namespace.
>
> **This is the reviewer-verifiable primary interface fact of this section**
> (`prctl(2)`, `PR_SET_CHILD_SUBREAPER`). Both lines are asked to verify it
> against the man page rather than accept it here.
>
> **Officina abstains from `prctl` and does not become a subreaper. That
> abstention proves nothing about its ancestors.** The contaminated caller — or
> any process above it — may already be a subreaper, and this contract has no
> way to observe or prevent that.

### §P1S.1.2 The replacement wording

> **Every operative clause of the form "re-parented to `init`", "`init` reaps
> it", "its parent is `1`", or any equivalent absolute is replaced by:**
>
> > *re-parented to the nearest still-living ancestor subreaper, and to the PID
> > namespace's init process only if no such ancestor exists; that adopting
> > process, whichever it is, is the one that may reap it.*
>
> **The contract makes no claim about which process that is**, does not observe
> it, does not depend on it, and does not attempt to influence it.

Applied to each locus:

| # | Locus | Corrected reading |
|---|---|---|
| 1 | supervisor after `m9` | re-parented to the nearest living ancestor subreaper of `pid_mid` — which may be the **contaminated caller** — otherwise namespace init |
| 2 | supervisor on its own exit | reaped by whichever process adopted it |
| 3 | `pid_mid`, controllers, workers, watchdogs after PCS death | each re-parented to the nearest living ancestor subreaper, otherwise namespace init |
| 4 | the watchdog after PCS death, on its update-EOF exit | reaped by its adopter |
| 5 | the carried unreaped-zombie residual | reaped by its adopter after the PCS exits |
| 6 | v2.1.10.4 §P1B.2's tree annotation and edge table | §P1S.1.3 |
| 7 | carried v2.1 §W2.1's "(after the double fork its parent is `1`)" | **the parenthetical is false and is deleted.** The sentence's actual claim — "`getppid()` is **not** used for the supervisor grandchild; its identity is established by §W2.2 instead" — is **retained and re-affirmed**, and is now load-bearing: because the adopter may be any ancestor, `getppid()` in the supervisor is meaningless to this contract and is read by no route |

### §P1S.1.3 Corrected parent / reaper / authority table

| Process | Direct parent | Adopter if orphaned | Direct children | May `wait` on | May signal | Holds numeric PIDs of |
|---|---|---|---|---|---|---|
| caller | host | — | the PCS | **the PCS only** | nothing (forbidden) | the PCS |
| **PCS** | caller | nearest living ancestor subreaper, else namespace init | `pid_mid`, controllers, workers, watchdogs | **exactly those** | exactly those, plus the supervisor's **group** only after `c11` | exactly those |
| middle (`pid_mid`) | PCS | as above (only if the PCS dies first) | the grandchild until `m9` | nothing | nothing | none |
| **supervisor** | `pid_mid` until `m9`, then **its adopter** | nearest living ancestor subreaper, else namespace init | **none** | **nothing** — a wildcard wait returns `ECHILD` | **nothing** | **none — handles only** |
| watchdog | PCS | as above | none | nothing | nothing | none |
| controller / worker | PCS | as above | per carried role contracts | unchanged | unchanged | none |

**Death proofs, by target, unchanged in substance:** `pid_mid`, controllers,
workers and watchdogs — the PCS's own targeted `waitpid` through the carried
`WAIT_ONE` classifier, where only `REAPED_POSITIVE` proves death. **Supervisor**
— never by wait; by `t-pcs.v1` `PEER_EOF`, and where a death proof is required
by the carried §U2.5 stage-2 route, by **object-bound `/proc` absence or zombie
identity**, exactly as already signed. **No proof anywhere consumes an orphan's
reaped status or exit code.**

### §P1S.1.4 Corrected crash cuts

| Cut | Corrected continuation |
|---|---|
| **supervisor orphaning after `m9`** | `pid_mid` exits; the supervisor is adopted by the nearest living ancestor subreaper, else namespace init. **No contract route observes the adopter, reads the supervisor's `getppid()`, or waits on the supervisor.** The PCS continues to hold every handle and observes the supervisor only through `t-pcs.v1` |
| **supervisor exit** | its adopter reaps it. The PCS learns of the exit by `PEER_EOF`, never by a wait. Where the carried §U2.5 stage-2 route requires a death proof for the group, it uses `/proc` absence or state `Z` with matching start identity; **prompt reaping by an adopter makes absence true sooner, which the carried proof already accepts, and a recycled PID appears as "live with a different start identity", which §U6.1 P3 already routes to "treat as not live and NEVER kill"** |
| **PCS death** | `pid_mid` and every role are adopted by the nearest living ancestor subreaper, else namespace init, and reaped by that adopter. The supervisor observes `PEER_EOF` and has lost all authority; freeze is unavailable; the generation is **unrecoverable invalidity** through the signed `T_PROCESS_INVALID` and §4c(c)/§4d route; **no new PCS may adopt a live generation.** None of that depends on who adopted the orphans |
| **role exit after PCS death** | reaped by its adopter. No contract decision consumes the result, because the generation is already invalid and no death proof is being taken |
| **the group anchor** | the process-group id used by the carried post-`c11` `killpg` route is `pid_mid`'s pid. `pid_mid` is the **PCS's own direct child** and is therefore **never orphaned while the PCS lives**, so subreaper semantics cannot touch the anchor. If the PCS dies, `pid_mid` is orphaned — but the generation is by then unrecoverable invalidity and no `killpg` decision is taken |

### §P1S.1.5 What a contaminated ancestor subreaper can do, stated plainly

| It can | Detail |
|---|---|
| become the parent of orphans | the supervisor after `m9`; and after PCS death, `pid_mid`, controllers, workers and watchdogs |
| reap them, including by wildcard wait | `wait()`, `waitpid(-1, …)`, `waitid(P_ALL, …)` in the subreaper reach every process it has adopted |
| learn each orphan's PID and wait status | the exit code or terminating signal. In this contract those values come from a closed, small set — `0`, `3`, and the named PCS exit tokens — and carry **no** scientific, capacity, custody, resource, or Q/C content |
| delay reaping, holding zombies | which only prolongs `/proc` state `Z` — an accepted death proof |
| reap promptly | which only makes `/proc` absence true sooner — also an accepted death proof |
| kill or stop what it has adopted | already the signed A3 same-UID residual, unchanged |

| It cannot | Why |
|---|---|
| obtain any descriptor or capability | reaping conveys no descriptor; capabilities move only by `SCM_RIGHTS` or inheritance, neither of which a reap touches |
| make `/proc` report absence for a live process | absence follows death, not adoption |
| forge or block a death proof | the proofs are object-bound `/proc` facts with start-identity matching, never reap-based |
| gain Officina process authority | §P1S.1.6 |

### §P1S.1.6 The bounded interpretation — PROVED, with the reliance audit

> **Claim.** Adoption by a contaminated ancestor subreaper does **not** grant
> that ancestor Officina process authority, because **no PCS or supervisor
> decision consumes an orphan's reaped status, exit code, or numeric PID after
> custody is lost.**

**Audit of every place a wait result or exit status is consumed in the P1
composite:**

| Consumer | Target | Orphan? | Consumes a status? | Verdict |
|---|---|---|---|---|
| `WAIT_ONE` / `REAP_ROLE` (`REAPED_POSITIVE`) | `pid_mid`, controllers, workers, watchdogs — **all direct children of the PCS** | **no**, while the PCS lives | only the returned **pid**; the status word is structurally range-checked and **no branch reads its content** | safe |
| `AWAIT_STOP`'s `WIFSTOPPED` requirement (carried §W2.5) | controller / worker | **no** — a direct PCS child | **yes**, it branches on the status | safe: never an orphan, so no adopter can intercept it |
| supervisor-death detection | supervisor | **yes** after `m9` | **no** — `t-pcs.v1` `PEER_EOF` only | safe |
| watchdog-death detection | watchdog | **no** while the PCS lives | ack absence and `REAP_ROLE`'s returned pid | safe |
| §U6.1 P3 death proof | any recorded process | may be | **no** — `/proc` absence, state `Z` with matching identity, or a start-identity mismatch | safe |
| §U2.5 stage-2 per-member death proof | group members incl. the supervisor | may be | **no** — `/proc` absence or state `Z` | safe |
| the caller's view of the PCS | the PCS | no | **no** — v2.1.10 §V2110.2.4 already makes the exit status **advisory only** and the pipe reply authoritative | safe |
| PCS loss | — | — | — | unrecoverable generation invalidity; no status is consulted |

> **Result: the interpretation is PROVED.** Exactly one decision in the whole
> composite branches on a wait status — `AWAIT_STOP`'s `WIFSTOPPED` — and its
> target is a direct child of the PCS, which is never orphaned while the PCS
> lives. Every other consumer uses either the returned pid of the PCS's own
> child, an object-bound `/proc` fact, or a channel EOF. **No carried decision
> relies on exclusive init reaping or on the preservation of an orphan's exit
> status, so no `BLOCKED_…` verdict is required and no architecture changes.**

### §P1S.1.7 What is deliberately not added

**None of the following appears anywhere in this repair, and each would be an
architectural choice that only Kirill may make:** `prctl` in any form,
`PR_SET_CHILD_SUBREAPER`, `ctypes`, a child-subreaper role for the PCS or any
Officina process, a long-lived middle child kept alive to retain parentage, a
PID namespace, a cgroup, any new signal path, and any adoption, hand-back, or
recovery protocol. The import closures remain `{os, sys, _signal, time, fcntl,
_socket}` and `{os, sys, fcntl}`; the root count remains five.

### §P1S.1.8 A3 honesty, not upgraded

A contaminated ancestor that becomes a subreaper may already kill, stop, delay,
or reap the processes it adopts — and, as the carried A3 rescope has always
said, a same-UID actor may already interfere with this contract's processes and
files. **This repair changes none of that and upgrades nothing into adversarial
confinement.** The contract offers **procedural discipline**; it asserts no
same-UID confinement mechanism, and it invents none here. The surface remains
permanently non-citable, forbidden from selection, Q, C, C1–C6, any blinding
claim, and any scientific or resource interpretation.

---

## §P1S.2. R2 — `/proc/self/fd`, phase-scoped

### §P1S.2.1 The contradiction

`S-18` says "no `/proc/self/fd` directory enumeration appears anywhere". The
same operative contract **requires** three enumerations: the PCS's `P-f`
preflight, the role's `A-5` exact-set check, and the grandchild's `G-5`
pre-`exec` scrub — and asserts them in tests 442R and others. The rule as
written is unsatisfiable, and the intent was narrower: forbid the
**supervisor's receive-error remediation sweep**, which could close another live
role's handle because the supervisor's legitimate descriptor set **grows with
every live handle** and its members sit at kernel-chosen numbers.

### §P1S.2.2 The phase / permission table

| Root | Phase | Enumerate? | May close? | Scope and rule |
|---|---|---|---|---|
| PCS bootstrap | `P-f`, pre-fork preflight | **yes** | **no — read-only** | require the set to be exactly `{0,1,2,3,4,5,6,7,8}` plus the transient listing descriptor; any deviation is a fail-closed refusal with **no fork** |
| role bootstrap | `A-5`, before any project import | **yes** | **no — read-only** | require exactly `{0,1,2}` ∪ the role's slot set; any deviation is `os._exit(3)` with nothing written. **`A-5` is a verification, not the mechanism** (v2.1.10.5 §P1R.1.6, carried) |
| grandchild, inside the role-bootstrap image | `G-5`, after `G-2`/`G-3`/`G-4`, **before** `G-6`'s `execve` and therefore before any project import | **yes** | **yes, bounded** | close every inherited descriptor **not** in the pinned keep-set `{0,1,2}` ∪ slots `3…10`; ascending order, once each, `EBADF` tolerated. This is the carried §W2.2/§Z3.5 scrub |
| supervisor | `B-1`…`B-5` `SCM_RIGHTS` receive and its error path | **NO** | **NO** | **forbidden.** Cleanup is exactly v2.1.10.5 §P1R.5.1's parser-local rule: close exactly the parsed vector, de-duplicated, ascending, once each, `EBADF` tolerated, and nothing else |
| supervisor | any runtime error remediation, any handle-release path, any shutdown step | **NO** | **NO** | **forbidden** |
| any root | any phase in which unrelated live role handles coexist | **NO** | **NO** | **forbidden** |
| PCS | any phase after the first role handle exists | **NO** | **NO** | **forbidden** — `P-f` is pre-fork and is the only PCS enumeration |

### §P1S.2.3 Why `G-5` cannot touch a live supervisor handle — proof

1. `G-5` executes in the **grandchild**, in the role-bootstrap image, **before**
   `G-6`'s `execve` and therefore before `A-10`'s project import and before
   `A-13`'s entry into the supervisor role. **At that instant the process is not
   the supervisor.**
2. A live role handle's descriptors reach the supervisor **only** by
   `SCM_RIGHTS` on the `t-pcs.v1` channel, and the supervisor issues its first
   `SPAWN_ROLE` only **after** `A-13`. **No such descriptor can exist in the
   process at `G-5` time.**
3. `G-5` acts **only on this process's own inherited descriptor table**. It
   cannot reach another process's table at all, and the only descriptors present
   are those inherited from the middle plus the slots `G-2` installed.
4. Therefore the set `G-5` may close and the set of live role handles are
   **temporally and structurally disjoint**. ∎

The same argument applies to `P-f`, which runs before the PCS's first fork and
therefore before any role or handle exists.

### §P1S.2.4 `S-18'`, replacing `S-18`

```text
S-18'  (replacing S-18) An enumeration of `/proc/self/fd` — a `_listdir` of that
       directory, or any equivalent traversal — may appear ONLY at the three
       pinned sites below, and its permission is exactly as stated:

         (a) the PCS bootstrap's P-f preflight            — READ-ONLY
         (b) the role bootstrap's A-5 check               — READ-ONLY
         (c) the grandchild's G-5 pre-`execve` scrub      — MAY CLOSE, bounded
             by the pinned keep-set {0,1,2} ∪ slots 3…10

       Any enumeration at any other site, in any root, is a violation; and any
       enumeration at (a) or (b) that is followed by a `_close` whose argument
       derives from the listing is a violation.
       In particular an enumeration or enumerate-and-close sweep is FORBIDDEN in
       the supervisor's SCM_RIGHTS receive path, in any runtime error
       remediation, in any handle-release path, and in any phase in which
       unrelated live role handles coexist.
       ⇒ "proc-fd enumeration outside the three pinned sites"
       ⇒ "proc-fd close derived from a read-only enumeration"
```

**No sentence equivalent to "nowhere" survives.** v2.1.10.2 §T8 row 425 —
"`/proc/self/fd` is never enumerated **for remediation** anywhere" — was already
remediation-scoped, is consistent with `S-18'`, and is **retained unchanged**.

**v2.1.10.5 §P1R.5.1's parser-local cleanup and v2.1.10.5 §P1R.4.2's
single-statement `_exit_` handler are preserved exactly and are not replaced by
any sweep.**

---

## §P1S.3. No-regression over v2.1.10.5 and the signed cells

| Surface | Status under this repair |
|---|---|
| **F1** — `SPAWN.lock` `O_CLOEXEC` + `F_GETFD` readback; `G-1`…`G-6`; the fork-shared-lock theorem table; `A-5` demoted to verification | **unchanged.** `G-5` is re-affirmed by §P1S.2.2 as a permitted bounded scrub, which is exactly what F1 already required |
| **F2** — the authority boundary, the supervisor not in the PCS child set, the post-`c11` group route | **unchanged in substance**; §P1S.1.3 only replaces the `init` cell with the adopter semantics |
| **F3** — one watchdog rule, no signal to a watchdog on any path | **unchanged**; §P1S.1.4's watchdog rows add no signal |
| **F4** — the withdrawn no-callback theorem, `S-19`'s AST-only property, the named capability exposure inside A3 | **unchanged and explicitly preserved** (§P1S.2.4) |
| **F5** — the non-aborting `B-2`/`B-3`, `B-4` as the only actor | **unchanged and explicitly preserved** (§P1S.2.2, §P1S.2.4) |
| **P1 selection** | **unchanged.** No option is reopened; no P2/P3/P4 text is added |
| **A3** | carried; §P1S.1.8 states the subreaper case inside it **without upgrade** |
| **B1** | unchanged — no journal, ack, redelivery, or descriptor-non-redelivery rule is touched |
| **C1** | unchanged — the one-detector model, the update-pipe EOF, `REAP_ROLE`, ack absence, and the no-signal rule all stand. **The watchdog still ignores `getppid()`**, which §P1S.1.2 row 7 makes more clearly correct, since an adopter may be any ancestor |
| **D1** | unchanged — no idle exit; PCS loss remains unrecoverable generation invalidity |
| **K1** and the output-capacity selection | unchanged — nothing here touches the ceiling, the accounting, the transport mediation, or the custody proof |
| **Process topology** | unchanged — same tree, same four role classes, same nine opcodes, same five roots, same 6 / 3 / 17 imports, same `CMSG_SPACE(12)` and 3-descriptor maximum |
| **Object-bound observation, both revalidation barriers, the bound-language sweep, `CLOSE_OWNED`, custody P1–P7, `§Z3.3`'s layout, `§Z3.2`'s role enum** | carried byte-unchanged |

---

## §P1S.4. Verifier and test delta

### §P1S.4.1 Verifier

```text
S-18   → REPLACED by S-18' (§P1S.2.4). Two distinct failure results.
S-23   (new) no operative sentence in the reviewed source or contract asserts
       that an orphan is re-parented to, or reaped by, `init` or PID 1 without
       the nearest-living-ancestor-subreaper qualification
       ⇒ "absolute init adoption claim present"
S-24   (new) `prctl`, `PR_SET_CHILD_SUBREAPER`, and `ctypes` appear nowhere in
       any production root ⇒ "subreaper or prctl surface present"
S-25   (new) no decision site branches on a wait status word except the single
       carried `WIFSTOPPED` test in the PCS's AWAIT_STOP handler, whose target
       is a direct PCS child ⇒ "wait status consumed off the direct-child path"
Everything else — CHANGES 1, 2, 4, 5 and rules S-1'…S-17, S-19…S-22 — unchanged.
```

### §P1S.4.2 Tests

Replaced:

- **359R** — after an ancillary violation the supervisor's descriptor table
  contains exactly its prior contents **minus the parsed vector**; assert there
  is **no static "pinned set" in the supervisor** and that every live role
  handle's descriptors survive.
- **442R** (amended) — the post-`execve` exact-set property is established **by
  construction**; `A-5`'s enumeration is **read-only** and is a verification.
- **445R** — `/proc/self/fd` enumeration appears at exactly the three pinned
  sites of `S-18'` and nowhere else; assert `(a)` and `(b)` perform no `_close`
  derived from the listing, and `(c)` closes only outside the pinned keep-set.
- **458R** — PCS death: `pid_mid` and every role are adopted by the nearest
  living ancestor subreaper, else namespace init; assert **no contract decision
  reads the adopter, the reap, or the exit status**, and that the generation
  routes to `T_PROCESS_INVALID` and §4c(c)/§4d.
- **493R** — the orphaned supervisor is reaped by **its adopter**, whichever
  process that is; the caller reaps only the PCS; assert no route observes the
  adopter.

Added:

| # | Test |
|---|---|
| 501 | no operative text contains an absolute `init` / `pid 1` adoption or reaping claim (`S-23`); every such clause carries the subreaper qualification |
| 502 | carried v2.1 §W2.1's "its parent is `1`" parenthetical is superseded, while its actual claim — `getppid()` is not used for the supervisor — is retained and asserted |
| 503 | a fixture in which an ancestor is a child subreaper produces the same contract behaviour as one in which none is: identical decisions, identical records, identical routes |
| 504 | **the reliance audit**: exactly one decision site branches on a wait status (`AWAIT_STOP`'s `WIFSTOPPED`), and its target is a direct PCS child (`S-25`) |
| 505 | supervisor-death detection uses `PEER_EOF` only, never a wait, never `getppid()`, never an exit status |
| 506 | the group anchor `pid_mid` is a direct PCS child and is never orphaned while the PCS lives |
| 507 | a promptly reaped orphan yields `/proc` absence, and a recycled PID yields "live with a different start identity" — both already routed by §U6.1 P3 with **no kill** |
| 508 | `prctl`, `PR_SET_CHILD_SUBREAPER` and `ctypes` appear in no production root (`S-24`); the import closures and root count are unchanged |
| 509 | `G-5` runs before `G-6`'s `execve`, therefore before `A-10` and `A-13`; assert no `SCM_RIGHTS`-received descriptor can exist in the process at that instant |
| 510 | `P-f` runs before the PCS's first fork, therefore before any role or handle exists |
| 511 | the supervisor's receive path performs **no** `/proc/self/fd` enumeration; `B-4` closes exactly the parsed vector; a concurrent live role's ctrl and status descriptors survive |
| 512 | v2.1.10.5's F1–F5 all still hold verbatim after this repair (§P1S.3) |
| 513 | whole-composite no-regression diff over every carried surface |

---

## §P1S.5. Weakest points of this repair

1. **R1 makes the contract truthful, not stronger.** After it, the composite
   admits that a contaminated ancestor may become the parent of the supervisor
   and of every role after PCS death, and may reap them. I have proved no
   decision depends on that — but the *proof* is now what carries the safety,
   and it rests on my own audit of every wait-status consumer. A single missed
   consumer would falsify it. `S-25` and row 504 are the mechanical guard, and
   they are the first thing a reviewer should attack.
2. **`AWAIT_STOP`'s `WIFSTOPPED` is the single status-dependent decision.** It
   is safe only because its target is a direct PCS child. If any future layer
   moved that handshake off the direct-child path, the R1 proof would break
   silently.
3. **`S-18'` enumerates permitted sites by name.** That is single-valued today,
   but it means any future phase that legitimately needs a topology check must
   amend the rule rather than inherit a principle. I judged an explicit
   whitelist safer than a general criterion, but it is more brittle.
4. **`G-5`'s disjointness proof is temporal.** It holds because `G-5` precedes
   the role entry. It would be defeated by any future change that let the
   grandchild receive descriptors before `execve`, and nothing but the ordering
   forbids that.
5. **The `prctl(2)` semantics are stated, not verified.** They are cheap for a
   reviewer to confirm and are load-bearing for the whole of R1.
6. **Both defects were in my own bytes, and a static audit found them in one
   pass** — the third such round. That is a reason to weight this layer's
   self-assessment low and to check §P1S.0's index and §P1S.1.6's audit
   literally.

---

## §P1S.6. The two bounded confirmation questions

Both lines review the **identical bytes** of this repair together with the
carried composite, recompute every governing hash, and treat every author
verdict in this chain — including this one — as untrusted.

### For the X line (Claude Code Opus 4.8 / 5, clean context)

> **Yes or no:** do these repair bytes correctly replace every absolute
> `init` / `pid 1` adoption and reaping claim with the nearest-living-ancestor
> child-subreaper semantics, is §P1S.1.6's reliance audit complete — that
> exactly one decision (`AWAIT_STOP`'s `WIFSTOPPED`) branches on a wait status
> and its target is never an orphan — and does `S-18'` make `/proc/self/fd`
> enumeration single-valued while preserving `P-f`, `A-5`, `G-5` and forbidding
> every supervisor-side sweep, **without** reopening the P1 selection, the
> topology, A3/B1/C1/D1/K1, or any v2.1.10.5 F1–F5 closure?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_6_X` or
> `REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_6`. Static review only: run no code,
> test, probe, or process/socket/pipe/fork/exec/signal/wait/prctl operation;
> create exactly one review file; modify nothing; authorize no implementation,
> activation, entropy, spend, Q/C work, datum, outcome, or claim movement.

### For the Y line (GPT-5.6 Sol, clean context)

> **Yes or no:** are both defects closed without a new author choice, a new
> process, a new syscall or import, or any change to the signed P1 authority
> topology — specifically, is the §P1S.1.6 interpretation genuinely **proved**
> rather than assumed (so that no `BLOCKED_…` was owed), is §P1S.1.5's account
> of what a contaminated ancestor subreaper can reap and learn complete and
> honest without upgrading A3 into confinement, and is §P1S.2.3's proof that
> `G-5` cannot touch a live supervisor handle sound?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_6_Y` or
> `REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_6`. Static review only: run no code,
> test, probe, or process/socket/pipe/fork/exec/signal/wait/prctl operation;
> create exactly one review file; modify nothing; authorize no implementation,
> activation, entropy, spend, Q/C work, datum, outcome, or claim movement.

---

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. **No acceptance token is available
from this author round.** It becomes available only if both independent lines
confirm the identical corrected composite. This layer authorizes no
implementation, no code, test, verifier or manifest edit, no commit, no host
change, no process or probe, no T activation, no entropy, no E1/E2/E3 spend, no
Q/C work, no datum, no outcome, no Proof, and no claim movement.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
