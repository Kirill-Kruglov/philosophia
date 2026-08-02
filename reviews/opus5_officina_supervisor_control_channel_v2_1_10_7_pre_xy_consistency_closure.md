READY_FOR_OFFICINA_SUPERVISOR_P1_FINAL_XY_REVIEW

# Author closure — Officina supervisor/control-channel v2.1.10.7 pre-X/Y consistency repair

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only.** Not an
independent X-line or Y-line reviewer of this chain.

**This closure is an untrusted author self-assessment**, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` requires — and so was
v2.1.10.6's, which is why its verdict was treated here as a claim to be checked
rather than as evidence. **Every defect repaired in this layer was in my own
bytes.** This closure does not self-confirm.

## Byte and hash custody

Repository base: commit `c9f883d98375c0d961dae4821b44e0a2a818bd65`. The working
tree was already dirty at handover; every pre-existing tracked modification and
untracked path is preserved byte-for-byte.

Governing inputs, read in full and recomputed:

```text
8f806e33d85c00933871072dadda30110f18ea6bf34b5ebc388f23f8b067143e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md
65a32a6eeb0834b13207d1a6cf3ceff6501d4a895dab84ed0226b7500fa711cd  reviews/opus5_officina_supervisor_control_channel_v2_1_10_6_pre_xy_repair_closure.md
798d0cbd51e93cc1f4c0a443785f90d90a2e121d35738189cbee9c61acf557cc  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

This closure's companion:

```text
66dc6fdc26d8b27f50e8de9603e8ac217492a13385c04822a1450a938495d51a  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md
```

**Exactly two files were created and nothing else was touched.** v2.1.10.6 and
its closure, v2.1.10.5, v2.1.10.4, the P1 signature, every earlier layer, the
A3/B1/C1/D1/K1 and output-capacity signatures, the harness and batch composites,
the authorship note, and `verification.py` are all unedited and match their
digests. `scripts/officina_process_control_bootstrap.py` and
`scripts/officina_role_bootstrap.py` do not exist. No code, test, verifier,
manifest, prompt, prior review, or runtime object was edited, staged, or
committed. Method: static authoring only — read-only file and `git` inspection,
literal search, `sha256sum`, and reasoning from pinned Linux/CPython interfaces.

## Verdict

`READY_FOR_OFFICINA_SUPERVISOR_P1_FINAL_XY_REVIEW`.

The inconsistency and the three overstatements are closed **without** changing
process topology, adding a syscall, import or process, or requiring a new author
choice — so the `BLOCKED_…` branch does not fire. The repair is entirely a
correction to tables, prose, tests and verifier rules.

## Exact replacement index over v2.1.10.6

| # | v2.1.10.6 locus | Action |
|---|---|---|
| 1 | §P1S.1.3 caller-row cells "Direct children: the PCS … May wait on: **the PCS only**" | **replaced** — the wait-set is temporally explicit and includes dynamically adopted orphans |
| 2 | §P1S.1.3's table as a whole (static, one "Adopter if orphaned" column) | **replaced** by §P1T.1.2's dynamic table, adding an arbitrary higher ancestor `A*` as an explicit row |
| 3 | §P1S.1.5 "can" row — the **closed, small set** `{0, 3, named PCS exit tokens}` | **withdrawn as false**; replaced by §P1T.2's untrusted-OS-fact rule |
| 4 | §P1S.1.5 "cannot" row — "**forge or block** a death proof" | **split**: the false-positive impossibility is retained (§P1T.3.1); availability denial is **admitted** (§P1T.3.2) |
| 5 | §P1S.1.5 "cannot" row — "**gain Officina process authority**" | **replaced** by §P1T.4's three authorization clauses |
| 6 | §P1S.1.5's two can/cannot tables | **replaced** by §P1T.1.3's single dynamic capability table |
| 7 | §P1S.1.6's result sentence, insofar as it could read as liveness or availability | **scoped** by §P1T.6 to a safety result only |
| 8 | §P1S.4.2 test row **503** ("the same contract behaviour … identical routes") | **replaced** by 503R (non-interfering adopter: identical **decisions and records** only) plus new row 514 (interfering adopter: **fail-closed, not identical**) |
| 9 | §P1S.4.1's verifier list | **extended** by `S-26`, `S-27`, `S-28` |
| 10 | §P1S.5's weakest points | **extended** by §P1T.9 |
| 11 | §P1S.1.4's crash language where it implied eventual proof/EOF availability | **scoped** by §P1T.3.3 and §P1T.5 |

**Carried verbatim:** §P1S.1.1's `prctl(2)` fact, §P1S.1.2's adoption wording,
§P1S.1.4's crash cuts, §P1S.1.6's audit, §P1S.1.7's nothing-architectural list,
§P1S.1.8's A3 statement, and **§P1S.2 in full** (`S-18'`, the phase/permission
table, the `G-5` disjointness proof).

## One-to-one disposition of the eight requirements

| Req | Disposition |
|---|---|
| **1** temporally explicit table, caller **and** arbitrary higher ancestor | §P1T.1.2: seven rows × six columns — initial direct children, initial wait-set, dynamically adopted set (conditional on being the *nearest living* subreaper at that moment), wait-set after adoption, and Officina authority. `A*` is an explicit row, not a footnote; the contract observes and names none of them |
| **2** wildcard waits range over adopted children; `AWAIT_STOP` preserved | stated **affirmatively** in the table and in §P1T.1.3. §P1T.1.4 proves non-interception in **both** halves: while PCS custody is live the target is a non-orphan direct PCS child that no adopter can have adopted; if the PCS dies, custody is lost, the generation is already unrecoverable invalidity, and **no `AWAIT_STOP` decision is being taken** |
| **3** withdraw the closed status set | §P1T.2. The set is **false** — under A3 an actor may terminate an adopted process with any signal. Replaced by: the status is an **untrusted OS fact**, may reflect A3 interference, carries **no authorized programme meaning**, and is **never consumed by any Officina decision, record, journal entry, settlement, capacity accounting, custody disposition or Q/C input**. The surviving half is re-grounded — it holds because **no route reads it**, not because the set is small |
| **4** exact false-positive vs. availability distinction | §P1T.3. Retained: **no false-positive** object-bound death proof — a live or stopped process with a matching start identity satisfies none of the carried predicates, and absence cannot be fabricated. Admitted: an adopter, or any same-UID actor, may `SIGSTOP` a process and thereby **deny a death proof and a channel EOF indefinitely**, including keeping the `t-pcs.v1` socket and the watchdog update pipe open. §P1T.3.3 routes each effect into a **carried** fail-closed path — the A3 stopped-process residual, the non-returning reaper state, `WATCHDOG_UNREAPED` with **no signal**, and `T_PROCESS_INVALID` + §4c(c)/§4d — so none becomes a valid status, outcome, resource datum, or scientific evidence |
| **5** authorization distinction | §P1T.4. **Admitted without hedging**: adoption confers kernel parent and reaper status, and A3 already permits same-UID signal interference with or without adoption. **Retained, and the whole of the claim**: (i) no Officina descriptor or handle is conferred — `SCM_RIGHTS` is point-to-point between the PCS and the supervisor; (ii) the actor is never an authorized control-plane participant — no endpoint, no reachable opcode, no journal actor entry, no handle; (iii) no interference can become a valid Officina decision or a scientific/resource outcome |
| **6** recompute R1.3, the table, crash language, weakest points, tests, verifier; add guards | done throughout; guards are `S-26` (no exclusive ancestor wait-set), `S-27` (no closed adopter status set), `S-28` (no "cannot block/delay/prevent/deny" and no unqualified "cannot gain process authority" in the adopter context, with the permitted forms enumerated) |
| **7** preserve the reliance result at earned strength | §P1T.6: retained as a **safety** result — no valid Officina decision consumes an orphan's wait status. Explicitly withdrawn from any reading of it: liveness, confinement, and uninterruptible death-proof availability |
| **8** preserve `S-18'`, `P-f`/`A-5`/`G-5`, F1–F5, topology, signed cells | §P1T.8's twelve-row no-regression table; all byte-semantically unchanged. **No syscall, import, process or role is added** |

## Corrected dynamic parent / adopter / wait / authority table

`A*` = any higher ancestor. Adoption applies **iff** that process is the nearest
living ancestor subreaper at that moment.

| Process | Initial direct children | Initial wait-set | Dynamically adopted | Wait-set after adoption | Officina authority |
|---|---|---|---|---|---|
| **`A*`** | host-given | its own children | supervisor after `m9`; after PCS death `pid_mid`, controllers, workers, watchdogs | its own children **∪** adopted; wildcard waits range over the union | **none** |
| **caller** | the PCS | the PCS | same set, if it is the nearer living subreaper | the PCS **∪** adopted; wildcard waits range over the union | none beyond launching the PCS and `L-1`…`L-4` |
| **PCS** | `pid_mid`, controllers, workers, watchdogs | exactly those | nothing | unchanged | **full** — sole holder of numeric process authority |
| middle | grandchild until `m9` | **nothing** | nothing | nothing | none |
| **supervisor** | **none** | nothing (`ECHILD`) | nothing | nothing | **handles only, never a PID** |
| watchdog | none | nothing | nothing | nothing | none |
| controller / worker | per carried contracts | unchanged | nothing | unchanged | none |

**Adoption adds exactly two powers** (§P1T.1.3): reaper status — hence
observation of the wait status and control of when the zombie clears — and
`getppid()` visibility, which confers nothing because **no Officina route reads
`getppid()` in any process**. It adds **no** signalling power, since A3 already
grants that to any same-UID actor with or without adoption.

## Exact safety-versus-liveness statement under A3

**Guaranteed (safety), and claimed:** S1 no false-positive death proof and no
removal of a record naming a possibly-live process without an object-bound proof
or an authoritative parent reap; S2 no capability transfer to any unauthorized
actor; S3 no interference accepted as an Officina decision and no
adopter-observed value consumed by one; S4 every perturbed or unestablished
control outcome settles through `T_PROCESS_INVALID` and the signed §4c(c)/§4d
unknowable route with invalidity dominance — never as a completion, capacity
fact, custody disposition, E1/E2/E3 fact, Q/C input, or scientific evidence.

**Not guaranteed (liveness), and explicitly not claimed:** L1 that any
generation completes; L2 that a death proof ever becomes available for a stopped
process; L3 that a sealed channel ever reaches EOF; L4 that a fail-closed stall
ever terminates; L5 that a same-UID actor is confined, detected, or prevented.

**A3 is a procedural rescope, not confinement and not adversarial same-UID
security, and it is not upgraded here.** Every liveness loss is permanently
non-citable and forbidden from selection, Q, C, C1–C6, any blinding claim, and
any scientific or resource interpretation.

## No-regression

| Surface | Status |
|---|---|
| **10.6 R2** — `S-18'`, the `P-f`/`A-5`/`G-5` phase/permission table, the `G-5` disjointness proof, rows 359R/442R/445R/425 | **byte-semantically unchanged** |
| **10.6 R1** — subreaper adoption wording, seven replaced loci, four crash cuts, group-anchor row, nothing-architectural list, A3 statement | unchanged; only the table's staticness and three adjacent overstatements are corrected |
| **10.6 reliance audit** | retained, scoped to safety (§P1T.6) |
| **F1** lock `O_CLOEXEC` + `F_GETFD` readback, `G-1`…`G-6`, fork-shared-lock theorem, `A-5` as verification | unchanged |
| **F2** authority boundary, supervisor outside the PCS child set, post-`c11` group route | unchanged |
| **F3** one watchdog rule, no signal on any path | unchanged |
| **F4** withdrawn no-callback theorem, `S-19` AST-only, named capability exposure inside A3 | unchanged; §P1T.5 generalizes it to the adopter case |
| **F5** non-aborting `B-2`/`B-3`, `B-4` the only actor | unchanged |
| **P1 selection**, topology, nine opcodes, five roots, 6/3/17 imports, `CMSG_SPACE(12)`, 3-fd maximum | unchanged |
| **A3** | carried and **not upgraded**; its limits are made more explicit, never stronger |
| **B1, C1, D1, K1**, output-capacity selection | unchanged |
| object-bound observation, both barriers, bound-language sweep, `CLOSE_OWNED`, custody P1–P7, §Z3.3 layout, §Z3.2 role enum | carried byte-unchanged |

## Exact future implementation / verifier / test surface

**Verifier:** `S-26`, `S-27`, `S-28` added; `S-1'`…`S-25` and CHANGES 1–5
unchanged.

**Tests:** row 503 replaced by 503R; rows 514–527 added.

**Files:** `scripts/officina_process_control_bootstrap.py` and
`scripts/officina_role_bootstrap.py` (neither exists);
`src/philosophia/officina/verification.py` (CHANGES 1–5 plus `S-19`…`S-28`,
nothing else); `PRODUCTION_CALL_GRAPH.json`; `generic_harness.py` and the test
modules — the last two **untracked Cursor work, preserved byte-for-byte**.
Everything else byte-unchanged.

## Weakest points against my own repair

1. **This layer makes the composite honestly weaker, not stronger.** It admits a
   same-UID actor can stall any generation indefinitely and that **no** liveness
   property is guaranteed. A reviewer may judge that a control plane with no
   liveness guarantee under its own stated threat model is unacceptable — which
   would be a **new author cell**, not a defect in these bytes, and I have put
   that question to Y explicitly.
2. **The safety set S1–S4 is my own enumeration.** A missing fifth property
   would make the boundary incomplete rather than wrong, and nothing mechanical
   would catch it.
3. **`S-26`/`S-27`/`S-28` are wording guards.** They forbid the phrasings that
   went wrong — the recurring defect class — but a future layer could restate
   the same overclaim in words they do not match.
4. **§P1T.1.4's argument depends on the topology**: it holds only because
   controllers and workers are direct PCS children. A future change to who
   spawns them would break it silently.
5. **Four consecutive author layers have each found defects in the previous
   one, all mine.** That is the strongest reason to weight this closure low and
   to check §P1T.0's index and §P1T.1.2's table literally.

## Bounded questions for the independent lines

Both review the **identical bytes** of this repair with the carried composite,
recompute every governing hash, and treat every author verdict — including this
one — as untrusted. §P1T.10 carries them verbatim.

**X = Claude Code Opus 4.8 / 5.** X-Q1: is §P1T.1.2's dynamic table consistent
with the carried subreaper semantics — initial versus adopted sets, `A*` as well
as the caller, wildcard waits stated affirmatively — and does §P1T.1.4's
`AWAIT_STOP` argument hold in both halves? X-Q2: are the three withdrawals
correct and complete, and does any operative sentence anywhere still carry a
withdrawn form? X-Q3: is §P1T.5's safety-versus-liveness boundary right, is
§P1T.6 correctly scoped to safety, and are `S-26`/`S-27`/`S-28` sufficient
guards — without reopening P1, the topology, A3/B1/C1/D1/K1, `S-18'`, or any
F1–F5 closure? Verdict line 1 exactly
`CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_7_X` or
`REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_7`.

**Y = GPT-5.6 Sol.** Y-Q1: is the inconsistency genuinely closed — does any
statement still give a process a static exclusive wait-set its own subreaper
analysis contradicts? Y-Q2: is §P1T.3's distinction exact and honest — no
false-positive proof, but indefinite denial of proof and EOF admitted — and does
§P1T.3.3 route every such effect into a carried fail-closed path with nothing
becoming a valid status, outcome, resource datum or scientific evidence? Y-Q3:
is §P1T.4's authorization-versus-kernel-power distinction right, and is §P1T.5
honest about what is not guaranteed — and if you judge a control plane with no
liveness guarantee unacceptable, say so explicitly, since that is a new author
cell rather than a defect in these bytes. Verdict line 1 exactly
`CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_7_Y` or
`REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_7`.

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
