REVISE_OFFICINA_SUPERVISOR_P1_COMPOSITE

# Independent X-line final review — Officina supervisor P1 composite (v2.1.10.7 pre-X/Y consistency repair over the carried P1 binding)

Reviewer: **Claude Code Opus 4.8, acting only as the independent X line.** I did
not author any layer of this chain. Every author closure and verdict in the
chain — including v2.1.10.7's `READY_FOR_OFFICINA_SUPERVISOR_P1_FINAL_XY_REVIEW`
and v2.1.10.6's — was treated as an untrusted claim to be checked, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` requires.

Static review only. I ran no code, test, or probe, and performed no
process/socket/pipe/fork/exec/signal/wait/prctl operation. I created exactly one
file (this one) and modified nothing else. T remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`.

## Hash custody (recomputed)

Both review-target bytes reproduce byte-for-byte:

```text
66dc6fdc26d8b27f50e8de9603e8ac217492a13385c04822a1450a938495d51a  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md
02d13b9d8a6b34fd1d53a98de6e17ef9eeb8efb67f7f2981ba9c7bf51ada32a9  reviews/opus5_officina_supervisor_control_channel_v2_1_10_7_pre_xy_consistency_closure.md
```

All **23** governing hashes pinned in v2.1.10.7's block (10.6, its closure, 10.5,
its closure, 10.4 binding, its closure, the P1 process-authority signature, the
10.3/10.2/10.1/10/9/8/1/1.1/3 corrections, the A3/B1/C1/D1/K1 and output-capacity
signatures, the harness and batch-settlement composites, the authorship note, and
`verification.py` at `327b1bb2…`) also reproduce byte-for-byte. The carried chain
is byte-intact. `verification.py` is the pinned 550-line pre-P1 verifier; the
untracked `generic_harness.py` contains **no** PCS/`t-pcs.v1`/`SCM_RIGHTS`/
`SPAWN_WATCHDOG`/`recvmsg` symbol (0 hits), i.e. the P1 architecture is entirely
unimplemented — a `CONFIRMED` verdict would authorize writing all of it.

---

## Findings (ordered by severity)

### CRITICAL — none

I could not construct a wrong-PID action, a false-positive death proof, an fd
capability reaching an unauthorized process, a two-owner handle/lease race, a
replayed-operation-becomes-valid path, a watchdog signalled on the no-signal
route, a `SPAWN.lock` leak past the controller/worker/watchdog `execve`, or an
adopter wait status consumed as a valid Officina decision. The safety core (see
"What holds", below) is sound and single-valued. The three withdrawals of
v2.1.10.7 are, on their own terms, correct.

### MAJOR 1 — The verifier/contract surface is not mechanically single-valued: the new prose guards (`S-23`, `S-26`, `S-27`, `S-28`) have no decidable domain, no materialized "operative composite" exists, and applied to the committed bytes they fail-closed on the *correct* composite

**Where.** v2.1.10.7 §P1T.7.1 (`S-26`/`S-27`/`S-28`); v2.1.10.6 §P1S.4.1
(`S-23`); the closure's "Exact future … verifier … surface" line
("`verification.py` (CHANGES 1–5 plus `S-19`…`S-28`, nothing else)"); and the
signed precondition in
`successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md:50`
("The selected P1 architecture **must be emitted as one operative composite
before independent review**").

**The defect.** These four rules quantify over *operative sentences of the
contract*:

- `S-23`: "no **operative sentence in the reviewed source or contract** asserts
  that an orphan is re-parented to, or reaped by, `init` or PID 1 without the
  … qualification";
- `S-26`: "No **operative sentence** states an exclusive wait-set … for the
  caller or any ancestor";
- `S-27`: "No **operative sentence** enumerates, bounds, or otherwise closes the
  set of wait-status values …";
- `S-28`: "no **operative sentence** asserts that the actor 'cannot block' …".

They are unambiguously **prose** rules — the phrasings they forbid are contract
English, not Python, and v2.1.10.7 §P1T.9.3 itself calls them "**wording
guards**" and §P1T.10 X-Q3 asks whether they are "sufficient as **mechanical**
guards." So implementability is squarely in scope. But:

1. **No operative-composite artifact exists.** The signed selection required the
   architecture be emitted "as **one** operative composite." Instead the P1
   contract is spread across ≥4 layered documents (10.4 binding, 10.5, 10.6,
   10.7) plus the entire carried v2.1–v2.1.10.3 chain, each superseding the
   prior only by a **prose replacement-index table** (§P1B.0.1, §P1S.0, §P1T.0).
   `find successor/ -i` shows no consolidated/operative/composite file; the only
   occurrence of "operative composite" as an existing object
   (v2.1.10.7:486) is a rhetorical review question, not a materialized document.
   The mandated precondition for this very review is therefore **unmet**.

2. **"Operative" is not a mechanically-computable property of the committed byte
   set.** Whether a sentence is operative is established only by transitively
   applying the ≥11 replacement-index rows across ~15 markdown files. A static
   verifier has no algorithm to reconstruct that. Three reasonable implementers
   diverge: (a) scan the committed markdown chain; (b) scan only the production
   roots' comments/docstrings ("reviewed source"); (c) scan a hand-rebuilt
   composite that does not exist. They produce different verdicts. That is
   precisely "implementation ambiguity between two reasonable implementers" and
   "a static verifier/test obligation that contradicts another required path."

3. **Applied to the committed bytes, the guards fire on the correct composite.**
   The forbidden phrasings physically persist in superseded predecessor layers,
   because each is retired by an index row, not by editing the file:
   - `S-26` (caller exclusive wait-set): `…10_6…:181` and `…10_5…:313` still
     read the caller "**May wait on: the PCS only**";
   - `S-27` (closed status set): the "**closed, small set — `0`, `3`, and the
     named PCS exit tokens**" survives in `…10_6…` (§P1S.1.5);
   - `S-28` ("forge or block" / unqualified authority): "**forge or block a
     death proof**" and "**gain Officina process authority**" survive in
     `…10_6…` (§P1S.1.5);
   - `S-23` (bare `init` adoption): `…10_4…:188,641,664` still read
     "re-parented to init", "re-parented to init, which reaps them", "init reaps
     it" with no subreaper qualification.
   A verifier implementing these rules over the committed contract **reports
   violations on a composite the author declares correct** — a verifier that
   fails-closed on valid input.

**Failure scenario.** Codex/Cursor, authorized by a `CONFIRMED` verdict, must
implement "`verification.py` (CHANGES 1–5 plus `S-19`…`S-28`, nothing else)."
There is no artifact for `S-23`/`S-26`/`S-27`/`S-28` to range over. If they scan
the committed markdown they get ≥4 spurious failures on correct predecessor
bytes; if they scan the production roots' comments the rules are near-vacuous and
do not guard the recurring **contract**-prose defect class they were added for; if
they invent a consolidated composite they are authoring a new normative artifact
the verdict did not authorize. The 10.7 layer's *only* new mechanical deliverable
— machine protection against reintroducing the three withdrawn overclaims — is
thus not achievable as written.

**Why this blocks CONFIRM and not merely a Minor.** The composite is being gated
on exactly the two properties this breaks: Q1 (mechanically single-valued and
implementable) and Q4 (can the verifier distinguish a shape-correct but
authority-wrong build). Repair requires a specification-author action — either
materialize the single operative composite the signature already ordered, or
define an operative-sentence predicate / restrict the rules' target to a named
artifact. That is a spec repair, not a Kirill author cell, so the correct verdict
is `REVISE`, not `BLOCKED`.

### MINOR 1 — `S-25` cannot statically establish its own load-bearing clause

`S-25` (v2.1.10.6 §P1S.4.1) reads: "no decision site branches on a wait status
word **except the single carried `WIFSTOPPED` test … whose target is a direct
PCS child**." An AST rule can verify the *count* (one `WIFSTOPPED` branch) but
cannot statically prove the semantic clause "its target is a direct PCS child."
Today that clause is true *by topology* — under P1 every role is a direct PCS
child (§P1B.2) — so nothing is wrong now. But v2.1.10.7 §P1T.9.4 leans the whole
`AWAIT_STOP` non-interception argument (§P1T.1.4) on this, saying "only `S-25`
guards the related property"; in fact `S-25` guards only the *count*, and the
direct-child property is guarded by the topology invariant, not by `S-25`. A
future layer that moved controller/worker spawning off the PCS would break
§P1T.1.4 silently, and `S-25` would still pass. The reliance is real and the
author flags the fragility, but the stated mechanical guard is weaker than
claimed. Low impact given the current topology.

### MINOR 2 — v2.1.10.7's governing-hash block is not self-sufficient for the "entire carried chain" it invokes

§P1T.0 says the layer carries "the whole carried P1 composite," and the brief
asks reviewers to read "v2.1 through v2.1.10.7, every replacement index they
incorporate." Yet 10.7's governing block pins only a subset of the carried
corrections (e.g. v2.1.2, v2.1.4, v2.1.5, v2.1.6, v2.1.7 corrections are not
pinned in 10.7's own block, though 10.4's block pins v2.1.7 and the chain is
transitively covered by predecessors' blocks). Integrity still holds transitively
— I recomputed the predecessor blocks — but a reader who verifies only 10.7's
block does not cover the full incorporated surface. Documentation completeness,
not a correctness defect.

---

## What holds (independently traced, single-valued and sound)

- **Process tree / authority (§P1B.2, §P1B.4).** caller →`posix_spawn`→ PCS;
  PCS `fork` `c4`→ `pid_mid` `fork` `m7`→ grandchild `execve`→ SUPERVISOR; PCS
  `posix_spawn`→ watchdog/controllers/workers. PCS is sole holder of every PID
  and sole caller of `fork`/`posix_spawn`/`kill`/`killpg`/`wait`-family. The
  supervisor holds opaque handles only, has an empty child set, and a wildcard
  wait returns `ECHILD`. Single-valued.
- **DUP2 / CLOEXEC leak proof (§P1B.3.3).** Correct against `dup2(2)`
  semantics: `POSIX_SPAWN_DUP2` clears `FD_CLOEXEC` on the destination; every PCS
  fd outside 3–8 is `CLOEXEC` by construction (sockets non-inheritable, pipes
  `_pipe2(_O_CLOEXEC)`, opens `_O_CLOEXEC`, `_dup` non-inheritable); sources are
  hoisted `>10`, destinations `≤10`, so every 3–8 is overwritten or explicitly
  closed; `SPAWN.lock` (deliberately non-`CLOEXEC`) reaches only SUPERVISOR
  slot 3, and the watchdog carries an explicit `(CLOSE,6)`. Any miss is
  fail-closed via `A-5`. Sound; the `SPAWN.lock` middle→grandchild→supervisor
  route survives correctly.
- **`SCM_RIGHTS` receive (§P1B.6).** The `scm_detach_fds()` fact is stated
  correctly: on a conforming Linux kernel the receiver installs
  `min(fits, queued)`, reports exactly the installed set, sets `MSG_CTRUNC`, and
  releases the remainder — so an installed-but-unreported descriptor cannot exist
  kernel-side. The only unenumerable case is an interpreter-side raise inside
  `_recvmsg`, handled by an immediate `_exit_` with no callback (`B-1`, guarded
  by `S-19`), with the interval named honestly as a transient capability leak
  inside A3. `B-4` closes exactly the parsed vector, de-duplicated, ascending,
  `EBADF`-tolerant, touching no live handle. No replay ever re-sends descriptors
  (§P1B.5.4). Single-valued.
- **Subreaper / adoption (10.6 §P1S.1, 10.7 §P1T.1).** The `prctl(2)`
  `PR_SET_CHILD_SUBREAPER` semantics are stated correctly (nearest living
  ancestor subreaper, else namespace init). The 10.7 dynamic table is internally
  consistent with those semantics and now covers an arbitrary higher ancestor
  `A*` as well as the caller, with wildcard waits stated affirmatively over the
  adopted union. Start-identity matching plus §U6.1 P3 ("live with a different
  start identity ⇒ treat as not live and NEVER kill") closes PID reuse.
- **`AWAIT_STOP` non-interception (§P1T.1.4).** Both halves hold: while PCS
  custody is live the target is a non-orphan direct PCS child no adopter can have
  adopted; if the PCS dies, custody is lost, the generation is already
  unrecoverable invalidity, and no `AWAIT_STOP` decision is taken.
- **Watchdog (§P1B.7).** One detector (update-pipe EOF); `getppid()` ignored
  (no false freeze on PCS death); no `waitpid` in the supervisor; termination by
  EOF only, never by signal (`SIGNAL_ROLE`/`SIGNAL_GROUP` refused for
  `WATCHDOG`); replacement uniform with the first via `SPAWN_WATCHDOG`. `F3`
  preserved.
- **`S-18'` (§P1S.2).** The prior `S-18`/`P-f`/`A-5`/`G-5` contradiction is
  genuinely resolved by the phase/permission table; the `G-5` disjointness proof
  (grandchild acts before `execve`, before any `SCM_RIGHTS` receipt) is sound and
  temporally exact; test 445R matches.
- **Fail-closed routing.** Every perturbed/unestablished control outcome settles
  through `T_PROCESS_INVALID` + §4c(c)/§4d with invalidity dominance
  (§P1B.8.4, §P1T.3.3, §P1T.5 S4). No adopter-observed value is consumed by any
  decision (§P1T.6 reliance audit; the single status-branching site is
  `WIFSTOPPED`, target never an orphan).

---

## Answers to the five deliverable questions

1. **Is the full P1 composite mechanically single-valued and implementable?**
   **The process-control core is** — the topology, nine opcodes, descriptor
   maps, journal/ACK automaton, `SCM_RIGHTS` rule, subreaper safety, and
   watchdog model are single-valued and implementable, and the code-level
   verifier rules (`S-1'`…`S-17`, `S-19`, `S-25`'s count) are codeable as AST
   checks. **The verifier/contract surface is not** (MAJOR 1): the prose guards
   `S-23`/`S-26`/`S-27`/`S-28` have no decidable target, no single operative
   composite was emitted despite the signature ordering one, and against the
   committed bytes they fail on the correct composite. So, taken whole, **no.**

2. **Are F1–F5 genuinely preserved through 10.6/10.7?** Yes, at the level of
   these two layers. 10.6/10.7 touch no lock, transport, topology, journal,
   ceiling, or accounting rule. `F1` (`SPAWN.lock` `O_CLOEXEC`+`F_GETFD`,
   `G-1`…`G-6`, fork-shared-lock theorem, `A-5` as verification), `F2` (authority
   boundary, supervisor outside the PCS child set), `F3` (one watchdog rule, no
   signal), `F4` (withdrawn no-callback theorem, `S-19` AST-only), and `F5`
   (non-aborting `B-2`/`B-3`) all carry byte-semantically. The one substantive
   move is that 10.7 §P1T.5 **generalizes** `F4` to the adopter case — a
   scope-widening honestly flagged, not a weakening. Preserved.

3. **Are the subreaper and A3 safety/liveness claims exact?** Yes. §P1T.3's
   split is exact and honest — no false-positive object-bound death proof, but an
   adopter or any same-UID actor may `SIGSTOP` a process and deny a death proof
   and a channel EOF **indefinitely**, admitted (previously overclaimed as
   "cannot forge or block"). §P1T.4's kernel-power-vs-authorization distinction
   is the right repair. §P1T.5's S1–S4 (safety, claimed) / L1–L5 (liveness, not
   claimed, non-citable) boundary is correctly drawn, and §P1T.6 scopes the
   reliance result to safety only. The claims are exact; the honest consequence
   is that P1 offers **no liveness and no confinement under A3** — a legitimate
   posture for these bytes, but one a future acceptor should note is a
   deliberate, unguaranteed-liveness control plane.

4. **Can the verifier/test surface distinguish a shape-correct but
   authority-wrong implementation?** Partially. The **code** rules can: `S-24`
   (no `prctl`/`ctypes`), `S-25` (single `WIFSTOPPED` branch), `S-16` (no wire
   field from a descriptor), `S-14`/`S-15` (`MSG_CMSG_CLOEXEC`, `CMSG_SPACE(12)`),
   `S-19` (unenumerable-receive `_exit_`), and test 441/442/446/451/455 attack
   authority directly. But the **prose/authority-hygiene** rules
   `S-23`/`S-26`/`S-27`/`S-28`, which are the guard against reintroducing the
   withdrawn authority overclaims, are not mechanically applicable as specified
   (MAJOR 1). And `S-25`'s "target is a direct PCS child" clause is not itself
   statically decidable (MINOR 1). So the surface cannot yet be trusted to catch
   an authority-wrong *contract*, only an authority-wrong *code path*.

5. **What exact implementation scope would a confirmed verdict authorize?** Had
   I confirmed: preparation only, by Codex/Cursor, of
   `scripts/officina_process_control_bootstrap.py` (the PCS + `t-pcs.v1` server),
   `scripts/officina_role_bootstrap.py` (the four-role isolated entry), the P1
   rewrite of `src/philosophia/officina/generic_harness.py` (the `posix_spawn`
   launcher, `t-pcs.v1` client, four role entries, and removal of every
   `Popen`/`fork`/`waitpid`/`kill`/`killpg`), CHANGES 1–5 plus `S-19`…`S-28` in
   `verification.py`, `PRODUCTION_CALL_GRAPH.json`, and the §P1B.14/§P1T.7.2 test
   matrix — **for later review**, with no code execution, no T activation, no
   entropy, no E1/E2/E3 spend, and no T/Q/C datum, outcome, Proof, or claim
   movement. Because I return `REVISE`, **no implementation scope is authorized.**

---

## Direct answers to §P1T.10 X-Q1 / X-Q2 / X-Q3

- **X-Q1.** §P1T.1.2's dynamic table **is** internally consistent with the
  carried subreaper semantics (initial vs. adopted sets; `A*` and the caller;
  wildcard waits stated affirmatively over adopted children), and §P1T.1.4's
  `AWAIT_STOP` argument holds in **both** halves. No defect here.
- **X-Q2.** The three withdrawals are individually correct and complete **within
  the operative reading**: the closed status set is gone and replaced by the
  untrusted-OS-fact rule; "forge or block" is split into a retained
  false-positive impossibility and an admitted availability denial; "cannot gain
  process authority" is replaced by the three §P1T.4 clauses. **However**, the
  withdrawn forms still physically occur in committed predecessor bytes
  (`…10_6…` §P1S.1.5; `…10_5/10_6…` caller rows; `…10_4…` `init` lines), and the
  mechanism meant to prove they no longer carry force — `S-26`/`S-27`/`S-28`/
  `S-23` — cannot mechanically make that distinction (MAJOR 1). So the
  *substance* is correct but the *closure of the withdrawal* is not mechanically
  established.
- **X-Q3.** §P1T.5's safety/liveness boundary is the right one and §P1T.6 is
  correctly scoped to safety **without** reopening P1, the topology,
  A3/B1/C1/D1/K1, `S-18'`, or any F1–F5 closure. But `S-26`/`S-27`/`S-28` are
  **not** sufficient as mechanical guards against reintroduction (MAJOR 1;
  MINOR 1) — they are well-posed as English but have no implementable target.

Under §P1T.10's own required X labels the corresponding verdict is
`REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_7`; expressed in the tokens this prompt
fixes, it is `REVISE_OFFICINA_SUPERVISOR_P1_COMPOSITE`.

---

## Suggested minimal repair (non-binding; for the author line, not authorized here)

Emit the single operative composite the P1 signature already ordered — one
document that is the P1 contract with every replacement index already applied —
and re-scope `S-23`/`S-26`/`S-27`/`S-28` (and the "or contract" clause) to range
over **that named artifact** plus the production roots, so the guards have a
decidable target that does not include superseded bytes. Restate `S-25` so the
"direct PCS child" clause is carried by an explicit topology invariant rather
than implied to be checked by `S-25`. None of this requires a new Kirill author
cell; it is a specification-author repair, hence `REVISE` rather than `BLOCKED`.

---

## Authorization boundary

This review authorizes nothing. `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`
remains **not signable**; no acceptance token is produced; because one
independent line (this X line) returns `REVISE`, the composite is not confirmed.
No implementation, code/test/verifier/manifest edit, commit, host change,
process, socket, pipe, fork, exec, signal, wait, or `prctl` operation is
authorized; no T activation, entropy, E1/E2/E3 spend, Q/C work, datum, outcome,
Proof, or claim movement.

**Confirmed: I wrote no code; ran no test or probe; performed no
process/socket/pipe/fork/exec/signal/wait/prctl operation; created exactly one
file; and modified nothing else.** T remains `NOT_ACTIVATED`; the programme claim
remains `OPEN`.
