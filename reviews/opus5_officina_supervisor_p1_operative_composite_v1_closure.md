READY_FOR_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_XY_REVIEW

# Author closure — Officina supervisor P1 operative composite, version 1

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only.** Not the
independent X-line or Y-line reviewer.

**This closure is an untrusted author self-assessment**, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` requires — as was every
prior closure in this chain, including v2.1.10.7's, none of which was used as
evidence here. The governing evidence is the two independent reviews, the signed
selections, and the committed bytes.

## 1. Digests

**The composite (the review target):**

```text
d2975d19c553d9f9338bacff9d0a2af1855af45881e305a8706c110820896935  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1.md
```

**`NORMATIVE_BODY` digest** — the value a future
`PRODUCTION_CALL_GRAPH.json` records as `p1_composite_normative_sha256` and that
guard `G-6` enforces:

```text
4eb1ddc63dc92d476e79f8c312322a7f7ed6052f742162cd37c05057827c5d79
```

**Extraction algorithm, exactly, so a reviewer reproduces the same bytes:**
the concatenation of every line strictly **after** the first line equal to
`<!-- OFFICINA-P1-NORMATIVE-BEGIN -->` and strictly **before** the first
subsequent line equal to `<!-- OFFICINA-P1-NORMATIVE-END -->`, each line
including its terminating newline. That is 1 663 lines of the file's 2 117.

**Custody inputs, recomputed:**

```text
70df01e8af25303600425434353a707571354e385fff78e1663f30494cf4b7ac  reviews/opus_officina_supervisor_p1_final_xy_review.md
75002efea91c3960adb5bc2bfa4dcdacecdb45a1add14f3f2fc1dd300e591b1b  reviews/sol_officina_supervisor_p1_final_xy_review.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
66dc6fdc26d8b27f50e8de9603e8ac217492a13385c04822a1450a938495d51a  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md
02d13b9d8a6b34fd1d53a98de6e17ef9eeb8efb67f7f2981ba9c7bf51ada32a9  reviews/opus5_officina_supervisor_control_channel_v2_1_10_7_pre_xy_consistency_closure.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
daeef9b3a349aba48b126957ff027d946b7ad094e5c03c3c2ede717f27a660e6  successor/officina/T_ENVELOPE.json
```

The composite's §C16.2 carries the **complete transitive provenance table** —
all 37 entries, including the six supervisor corrections v2.1.2, v2.1.4,
v2.1.5, v2.1.6, v2.1.7 and both drafts that v2.1.10.7's abbreviated block
omitted, plus the full generic-harness v2→v2.3.1 and batch-settlement
v1→v1.1.1 chains and both new reviews.

**Confirmation that no existing file changed.** Exactly **two** files were
created — the composite and this closure. `git status` shows no modification to
any tracked file beyond the pre-existing dirty set that was already dirty at
handover, and the untracked `essay/OUTLINE.md`,
`src/philosophia/officina/generic_harness.py` and
`tests/test_officina_generic_harness.py` are preserved byte-for-byte.
`verification.py` is unmodified at `327b1bb2…`.
`scripts/officina_process_control_bootstrap.py` and
`scripts/officina_role_bootstrap.py` do not exist. Method: read-only file and
`git` inspection, `sha256sum`, `awk`/`grep`/`tr` text extraction over committed
bytes. **No code was implemented, no test or behavioural probe was run, and no
process-control experiment involving socket, pipe, fork, exec, signal, wait or
`prctl` was performed.**

## 2. Coverage map — historical chain into the single composite

| Historical source of the rule | Where it now lives, literally |
|---|---|
| v1/v2 drafts: control constants, signal literals, sole-root and argv rules | §C2.2, §C2.5, §C3.1 |
| v2.1 §W: spawn/singleton/takeover, watchdog registration and freeze, capacity mediation, entry surface | §C8, §C10.1–§C10.3, §C12 |
| v2.1.1 §Z: adapter root, fixed argv layout, ctrl fd indices, bootstrap-pipe design, revised constants | §C2.2, §C2.4, §C6.4, §C8.1 |
| v2.1.2 §N, v2.1.3 §U: `c1`–`c18`, `m0`–`m9`, four channels, four identity tiers, stuck-holder route, `EEXIST`/removal discipline | §C6.5, §C10.1–§C10.3 |
| v2.1.4–v2.1.6 §V214–§V216: `CLOSE_OWNED`, malformed dominance, stage-M route, EOF audit, bound language | §C6.5, §C6.6, §C10.5, §C10.7 |
| v2.1.7 §V217: object-bound observation, both revalidation barriers, bound-language sweep | §C12 (composition), §C6.5 |
| v2.1.8 §V218: `SIGCHLD` full-disposition reset, `ECHILD`/`ESRCH` never death, ownership model, ten-row identity table, `T3` deleted, no-discard invariant | §C6.2 `P-g`, §C9.1, §C9.2, §C9.4, §C10.5 |
| v2.1.9 §V219: shared wait automaton, five sites, mask width | §C9.2, §C6.3 |
| v2.1.10 §V2110: isolated construction, `-I -S -E -P`, object-bound source, platform pin, `STRUCTURAL_VIOLATION`, `B` state | §C2.1, §C6.1, §C6.2, §C9.2, §C10.5 |
| v2.1.10.1 §V21101: `_signal` inventory, per-primitive identity table, `posix_spawn` launcher, hoist, package/role provenance, PCS concept | §C3.2–§C3.5, §C5.3, §C6.1, §C6.2 `P-p` |
| v2.1.10.2 §T: `SCM_RIGHTS` transport, `t-pcs.v1`, isolated role root, `F_GETFL` test | §C7, §C6.4, §C6.2 |
| v2.1.10.3: role-bootstrap three imports, `generic_harness` `_socket`, parser-local cleanup | §C3.2, §C7.7 |
| v2.1.10.4 P1 binding: the P1 architecture, handle model, nine opcodes, journal automaton, watchdog model, verifier and test surface | §C1.3, §C4, §C7, §C8.2, §C13, §C14 |
| v2.1.10.5 F1–F5: lock `O_CLOEXEC` + readback, authority boundary, one watchdog rule, withdrawn no-callback theorem, non-aborting parse | §C5.1, §C6.5 `c1`, §C6.6, §C4.3, §C8.2, §C7.7 `B-1`/`B-2` |
| v2.1.10.6: child-subreaper semantics, phase-scoped `/proc/self/fd` | §C4.2, §C5.5 |
| v2.1.10.7: dynamic adopter table, untrusted adopter status, false-positive vs. availability, authorization distinction, safety/liveness boundary | §C4.3, §C4.4, §C11.1–§C11.3 |
| signed harness v2→v2.3.1, batch settlement v1→v1.1.1 | §C12, unchanged |

**Two supersessions the delta chain hid, now resolved literally in the
composite:** `T_SUPERVISOR_POLL_INTERVAL_NS` is **50_000_000** (an earlier draft
value of `100_000_000` does not govern and appears nowhere), and the
`SPAWN_MIDDLE` record's `cli_pid`/`cli_start_identity` fields denote the **PCS**,
which is the process that holds the lock, with schema and key set unchanged.

## 3. One-to-one disposition of the findings

| Finding | Disposition |
|---|---|
| **X MAJOR 1** — no operative composite exists; `S-23`/`S-26`/`S-27`/`S-28` have no decidable domain; applied to committed bytes they fire on the correct composite | **Closed on all three limbs.** (a) The composite is **materialized**: one self-contained document, 2 117 lines, with an explicit four-level authority hierarchy in which the historical chain is provenance only and is **never opened**. (b) The guard domain is now **`NORMATIVE_BODY`, a byte range of exactly one file**, delimited by two literal marker lines, with an exact normalization (§C13.2) and a substring decision rule. There is no allowlist, no exclusion list, no supersession inference, and the adjective "operative" appears in no verifier rule. (c) **Superseded predecessor bytes are categorically outside the domain because they are never read**, so the four rules — now `G-1`…`G-5` — cannot fire on them. **I ran the guards against my own normative body and one fired**: the pattern `holds every pid` matched §C1.3's *correct, qualified* "holds every PID it creates". Both halves were fixed — the pattern is now the precise overclaim `holds every pid in the system`, and the sentence reads "holds the numeric identity of every process it creates". The re-run is clean. `G-6` adds a **closed invariant stronger than any wording rule**: the normative body's digest is pinned in the manifest and recomputed, so any edit — including a novel phrasing of a withdrawn overclaim — fails |
| **X MINOR 1** — `S-25` cannot statically establish "its target is a direct PCS child" | **Closed by splitting it.** `S-24a` is the **statically decidable** half: exactly one decision branch consumes a wait-status word and it is the named `WIFSTOPPED` site. `S-24b` is the **topological** half: every controller and worker creation site is a `_posix_spawn` call in the PCS root and appears in no other root — so a future layer that moved role spawning off the PCS **fails `S-24b` even though `S-24a` still counts exactly one branch**. §C13.7 states **TI-1** as a named invariant carried by `S-24a` + `S-24b` + behavioural test 33 together, and says explicitly that **no single rule carries TI-1 alone and no rule is described as if it did** |
| **X MINOR 2** — v2.1.10.7's hash block is not self-sufficient for the chain it invokes | **Closed.** §C16.2 pins the **complete transitive table**, 37 entries, adding every correction and draft the abbreviated block omitted plus the full harness and batch chains. A reader verifying only this composite's block now covers the entire incorporated surface — and, because the historical chain is provenance rather than an operative input, that verification is a *derivation* check, not a prerequisite for reading the contract |
| **Sol's access blocker** — the prior Y prompt prohibited the only read/hash mechanism | **Not a merits finding, and not treated as one.** No conclusion of Sol's is relied on and no clearance is inferred. §5's Y questions are written for a prompt that **must explicitly permit read-only file access and SHA-256 computation**; §7 records that requirement so the next Y round is not blocked the same way. The materialized composite also **reduces** the read surface a Y reviewer needs: one file plus the signatures, rather than fifteen markdown files and eleven replacement indexes |

## 4. Summaries

**Constants.** `T_SUPERVISOR_POLL_INTERVAL_NS = 50_000_000`;
`T_CONTROL_FRAME_MAX_BYTES = 4096`; `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS =
30_000_000_000`; `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS =
T_SPAWN_SELF_STOP_TIMEOUT_NS = 10_000_000_000`;
`T_SPAWN_BOOTSTRAP_MAX_AGE_NS = T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS =
60_000_000_000`; the six K1 output constants unmoved; PCS descriptor indices
3–8; role slots 3–10 with `T_CTRL_FD_LOW/HIGH = 3/4` for controllers and
workers; signal literals 9/15/18/19/0 with `signal.SIGCHLD` the only symbolic
name. **Zero new numeric values are introduced by the composite.**

**Process and authority.** caller → PCS (`posix_spawn`) → `pid_mid` (`fork`
`c4`) → grandchild (`fork` `m7`) → supervisor (`execve`); PCS → watchdog,
controllers, workers (`posix_spawn`). The PCS is the direct parent and sole
reaper of `pid_mid`, controllers, workers and watchdogs. The supervisor is the
parent of nothing, holds opaque handles, and a wildcard wait in it returns
`ECHILD`. Orphans are adopted by the **nearest living ancestor subreaper, else
namespace init**, and no rule depends on which. The group anchor `pid_mid` is a
PCS child and is never orphaned while the PCS lives.

**Descriptors.** PCS 3–8 non-`CLOEXEC` by `POSIX_SPAWN_DUP2`; everything else,
including `lock_fd`, `sv_sock`, the journal and every per-handle end, `CLOEXEC`
by construction. Role sets are exactly `{0,1,2}` ∪ slots. The lock reaches only
the supervisor, at slot 3, created by the grandchild's own
`_dup2(..., 3, inheritable=True)` with an `F_GETFD` readback. `/proc/self/fd`
may be enumerated at exactly three sites: `P-f` read-only, `A-5` read-only,
`G-5` bounded-close — and nowhere else, ever.

**Opcodes.** Nine: `SPAWN_ROLE` (3 fds), `AWAIT_STOP`, `SIGNAL_ROLE`,
`SIGNAL_GROUP`, `REAP_ROLE`, `SPAWN_WATCHDOG` (2 fds), `RELEASE_HANDLE`,
`SHUTDOWN`, `PING`. Maximum 3 descriptors per message; `CMSG_SPACE(12)`; no
field carries a pid, descriptor, path, argv, signal number or unbounded integer;
both signal opcodes are refused for a watchdog.

**Crash and invalidity.** A 26-row matrix in §C10.7, with §C10.4's
no-adoption prohibition and §C10.6's single invalidity route. Every unknown
outcome settles through the signed `T_PROCESS_INVALID` and unknowable route.

**Verifier.** CHANGES 1–5; code rules `S-1`…`S-24b`; guard rules `G-1`…`G-6`
over `NORMATIVE_BODY` only; and an eleven-item runtime preflight for what static
analysis cannot decide.

**Tests.** 80 rows in §C14, covering launch, isolation, preflight, masks, lock,
grandchild handoff, role entry, wait/signal/identity totality, terminals,
transport, protocol, watchdog, adoption (both a non-interfering and an
**interfering** adopter), guards, manifest and composition.

## 5. Guard domain and acyclic custody

**Domain.** `CONTRACT_GUARD_TARGET` = `NORMATIVE_BODY`, the byte range of the
composite between two literal marker lines. The guard rules **open exactly one
file**. Historical documents are outside the domain because they are never read,
not because a rule excludes them. The guard **pattern data** lives in a
delimited appendix that is itself **outside** the target, so the patterns are
never matched against their own statement.

**Acyclic custody, four links, no back edge.** The composite contains no digest
of itself. (1) the composite's bytes → (2) this closure pins
`sha256(file) = d2975d19…` and `sha256(NORMATIVE_BODY) = 4eb1ddc6…` → (3) the
independent X and Y reviews recompute and confirm both → (4)
`PRODUCTION_CALL_GRAPH.json` records the reviewed values, which `G-6` then
enforces against the live bytes. Verification order is 1 → 2 → 3 → 4, and the
verifier at step 4 depends only on the manifest and the file.

## 6. Weakest points, against my own composite

1. **The composite is large and I am its only reader so far.** 2 117 lines
   consolidating fifteen documents. I reconstructed the process, descriptor and
   authority tables from the literal rules and checked internal equality, and I
   traced every opcode and crash cut to one continuation — but a consolidation
   error that survived my own audit would now be *harder* to catch, because the
   predecessor no longer disagrees with it visibly.
2. **`G-1`…`G-5` are substring rules over a normalization I chose.** They caught
   one real self-fire, which is evidence they work; but a novel phrasing of a
   withdrawn overclaim could still slip past them. `G-6` is the real protection,
   and it protects only by making *any* edit visible, not by judging it.
3. **The guard-pattern appendix is outside the digested region.** That is
   necessary to avoid self-matching, but it means the pattern list can be edited
   without changing `p1_composite_normative_sha256`. A reviewer should require
   the manifest to pin the **whole-file** digest as well, which §C13.5 and the
   manifest field `p1_composite_sha256` do.
4. **§C12 states composition points rather than restating the harness and batch
   contracts.** Those are signed peer contracts with their own digests, not
   superseded predecessor layers, so citing them is not a forbidden
   cross-reference — but a reviewer may judge that "self-contained" should have
   meant restating them too.
5. **Every platform fact is stated, not verified.** `scm_detach_fds()`
   truncation, `PR_SET_CHILD_SUBREAPER` reparenting, `PyOS_setsig`'s `sigaction`
   flags, `POSIX_SPAWN_DUP2`'s `CLOEXEC` clearing, and `/proc` mask rendering are
   all reviewer-verifiable, and each is load-bearing.
6. **The composite inherits, and does not fix, the honest weakness of P1**: no
   liveness guarantee and no confinement under A3 (§C11.2). A same-UID actor can
   stall any generation indefinitely. That is a deliberate posture, stated in
   both the safety and liveness lists, and a future acceptor should note it.
7. **Five consecutive author layers each found defects in the previous one, all
   mine.** This closure should be weighted accordingly; §2's coverage map and
   §C2's constants should be checked literally rather than trusted.

## 7. Negative space and authorization

This author round authorizes **no** X/Y verdict, implementation, code or test
edit, verifier or manifest change, commit, host change, process, socket, pipe,
fork, exec, signal, wait or `prctl` operation, behavioural probe, T activation,
entropy, E1/E2/E3 spend, Q/C work, datum, outcome, Proof, or claim movement. The
composite predicts no qualification and no C1–C6 outcome, and creates no
capability, world, learner, candidate, capacity artifact, custody disposition or
result manifest.

**No acceptance token is available from this author round.**
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable**; it becomes available only if **both** independent lines confirm the
identical composite bytes `d2975d19…`. **This closure asserts no verdict and
does not self-confirm.**

**The next Y-line prompt must explicitly permit read-only file access and
SHA-256 computation**, or the access blocker of the previous round will recur;
that is a prompt defect, not a defect in these bytes.

## 8. Bounded questions for the independent reviewers

Both lines review the **identical bytes** `d2975d19…`, recompute the file digest
and the `NORMATIVE_BODY` digest by §1's extraction algorithm, and treat this
closure as untrusted.

### X = Claude Code Opus 4.8 / 5

> **X-Q1.** Is the composite genuinely **self-contained and single-valued** —
> does any executable rule still require a historical document, a replacement
> index, or a forbidden phrase, and can you reconstruct the process, descriptor,
> authority, opcode and crash tables from its literal rules alone and find them
> internally consistent? Attack §C2's resolved supersessions in particular.
> **X-Q2.** Is **MAJOR 1 closed**: is `NORMATIVE_BODY` a mechanically decidable
> domain; do `G-1`…`G-5` pass on the correct composite while rejecting a
> bit-exact reintroduction of each withdrawn overclaim; is the pattern appendix
> correctly outside the target; and does `G-6` plus the four-link acyclic custody
> of §C13.5 close the self-hash problem without a cycle?
> **X-Q3.** Is **MINOR 1 closed** by the `S-24a` / `S-24b` split plus TI-1 and
> test 33 — would a future topology change that moved role spawning off the PCS
> fail a named check even with the AST count unchanged? And is **MINOR 2** closed
> by §C16.2's transitive table?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_X`
> or `REVISE_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE`.

### Y = GPT-5.6 Sol

> **Y-Q1.** With read-only file access and hashing permitted, do both digests
> reproduce, and is the composite safe to authorize for **implementation
> preparation only** — does any process event (adopter wait status, signal,
> stall, EOF denial, reap, PID reuse, PCS loss, ancillary violation) have more
> than one permissible interpretation, or reach a success, capacity, custody,
> E1/E2/E3 or Q/C fact rather than §C10.6?
> **Y-Q2.** Are the A3 limitations and P1 costs **loud enough for later
> publication** — the absence of confinement and of every liveness guarantee
> (§C11.2 L1–L5), B1's descriptor non-redelivery, C1's single supervisor-death
> detector, D1's mandatory unrecoverable PCS, and K1's fixed ceiling — or is any
> of them softened anywhere in the normative body?
> **Y-Q3.** Does the four-level authority hierarchy hold as governance: are the
> signed selections still the sole source of accepted choices; is the historical
> chain genuinely inert; and does confirmation preserve `NOT_ACTIVATED` while
> authorizing implementation **preparation** only?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_Y`
> or `REVISE_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE`.

Both lines: static review only — run no code, test, or behavioural probe, and
perform no process/socket/pipe/fork/exec/signal/wait/prctl operation; read-only
file inspection and SHA-256 computation **are** permitted and required; create
exactly one review file; modify nothing; authorize no implementation,
activation, entropy, spend, Q/C work, datum, outcome, Proof, or claim movement.

---

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
