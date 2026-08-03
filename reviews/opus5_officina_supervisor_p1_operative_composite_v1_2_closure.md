BLOCKED_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_V1_2_AUTHOR_CELL

# Author closure — P1 operative composite v1.2

**Author:** Claude Code Opus 5, acting **only as the specification author**. I
authored the whole supervisor/control-channel chain, v1, v1.1 and v1.2, and am
therefore **disqualified** as an independent X-line or Y-line reviewer of any of
them. **This closure is an untrusted self-assessment.**

**Verdict line 1 is `BLOCKED`, not `READY`.** Literal reconstruction of the peer
interface — exactly what this round commissioned — surfaced a conflict between
two separately signed contracts that the accepted chain does not resolve. Per
the round's instruction ("Do not guess: if the chain does not resolve it, emit
`BLOCKED_...` and name the author cell"), I did not choose. The cell is:

```text
AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS
```

**State unchanged by this round:** `T = NOT_ACTIVATED`; programme claim `OPEN`.
No X/Y verdict, implementation, code or test edit, verifier or manifest change,
process or behavioural probe, activation, entropy, E1/E2/E3 spend, Q/C work,
datum, outcome, Proof or claim movement was produced or authorized.

---

## 1. Deliverables and untouched-file confirmation

Exactly two new files. **No existing file was modified.**

| Path | Lines | Bytes |
|---|---|---|
| `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md` | 2 892 | 178 218 |
| `reviews/opus5_officina_supervisor_p1_operative_composite_v1_2_closure.md` | this file | — |

v1.2 was produced by copying v1.1's exact bytes to the new path and editing only
the new file, so every preserved mechanic is byte-faithful rather than retyped.
Only read-only commands were run against the repository: `grep`, `sed`, `wc`,
`sort`, `uniq`, `tr`, `cat`, `cp` (to the new path only) and `sha256sum`. No
test, behavioural probe or process-control operation was executed.

**No token is available.** `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`
is not signable and was not made signable. v1.2's status line reads
`BLOCKED_ON_AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS_NOT_ACCEPTED`.

---

## 2. Governing digests

Inputs, recomputed this round; **all five match what v1.1 pinned**:

```text
90ddf3ff76a1d08994c06d9c7f938e45f32fdeb46f58251ebb162bc96cf01680  …P1_OPERATIVE_COMPOSITE_V1_1.md
40a26dc1a7d2e6a8b9c122b7e09599a7b03470b0e98c86964bc4389ea4b0e5b3  reviews/opus5_…_v1_1_closure.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  …GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  …GENERIC_HARNESS_SIGNATURE.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  …BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

Output, computed on final v1.2 bytes:

```text
H_FILE       2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d
H_BODY       318cc6589c3840b8538b6818bfa3e42701fb25e55bfbf8a27897c5fc06ad82e1
H_GUARDDATA  0d3131b4a319d0bf03310e203485320253b671501ec44f87d67e8d47f8616733
H_NORMATIVE  2606e941bfe3400af49b5ecdb7fa02a9ef69a99a90aa0e55caeb476c033564cd
```

| Region | Sentinels | Content lines | Content bytes |
|---|---|---|---|
| `BODY` | 154 and 2786 | 155–2785, 2 631 lines | 161 651 |
| `GUARDDATA` | 2788 and 2823 | 2789–2822, 34 lines | 1 487 |
| `PROVENANCE` | 2825 and 2892 | 2826–2891, 66 lines | covered by `H_FILE` |

**`H_GUARDDATA` is byte-identical to v1.1's** — the guard data was not touched,
which is direct evidence for the §6 no-regression claim rather than an assertion
of it. v1.2 contains none of its own digests, so custody stays acyclic.

---

## 3. The blocking conflict, in full

### 3.1 What the two signed contracts each require

**Signed requirement A — the process-claim key set.** `t-process-claim.v1` is
fixed by the T activation protocol with exactly twenty keys, among them the
literal integers `controller_pid` and `process_group_id`:

> `successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:233-238` —
> "The process claim keys are exactly: … `controller_pid`,
> `controller_start_identity`, `process_group_id`, …"

The record is written by the generic-harness peer layer executing in the
supervisor process, at `successor/officina/runtime/T_PROCESS_CLAIMS/<process_id>.json`
(`OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:83`). Its
`process_group_id` is not decorative: the freeze-evidence acceptance predicate
reads it — "`pgid == the claim's process_group_id and start_identity == the
claim's …`"
(`…SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md:1047`, §Z4.6 conjunct 7).

**Signed requirement B — the supervisor holds no PID.** From Kirill's signature
`OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md:24-26`:

> "The contaminated supervisor receives opaque handles only. It cannot express
> a PID and does not call `fork`, `Popen`, `waitpid`, `kill`, or `killpg` on a
> result-bearing path."

The P1 binding derives it mechanically
(`…V2_1_10_4_P1_BINDING.md:156-158`): "**The supervisor holds opaque handles
only.** `t-pcs.v1` has no PID field, so the supervisor cannot express a PID…"

### 3.2 The exhaustive gap proof

The signed nine-opcode response set returns, in total:

| Opcode | Response operands |
|---|---|
| `SPAWN_ROLE`, `SPAWN_WATCHDOG` | `handle_id` |
| `AWAIT_STOP` | `outcome`, `start_identity`, `pgid_is_leader` in `{0,1}` |
| `SIGNAL_ROLE`, `SIGNAL_GROUP` | a `result` token |
| `REAP_ROLE` | one of six classifier tokens |
| `RELEASE_HANDLE`, `SHUTDOWN` | none |
| `PING` | `pcs_uptime_ticks` |

Source for the `AWAIT_STOP` row, which is the only candidate:
`…V2_1_10_2_CORRECTION.md:366` — "`outcome` ∈ {`STOPPED`,`EXITED`,`TIMEOUT`};
`start_identity` (decimal); `pgid_is_leader` ∈ {`0`,`1`}". Carried identically
into v1 §C10.3, v1.1 §P1-8.3 and v1.2 §P1-8.3.

Field-by-field, for the layer that must write the claim:

```text
controller_start_identity  <- AWAIT_STOP's start_identity            AVAILABLE
argv                       <- argv_template + the fixed ctrl fds 3,4 AVAILABLE
controller_pid             <- no opcode returns a pid              UNAVAILABLE
process_group_id           <- pgid_is_leader is a PREDICATE over
                              {0,1}; it decides whether the group id
                              equals the process id but names neither UNAVAILABLE
```

`pgid_is_leader` is the near miss and it is not enough: knowing that the group
id equals the process id is worthless when the process id itself is unavailable.

### 3.3 Why this is a contract conflict and not an implementation gap

I searched the entire P1 chain — the binding `V2_1_10_4`, and the pre-review
repairs `V2_1_10_5`, `V2_1_10_6`, `V2_1_10_7` — for any handling of these two
keys. **There is none.** The single sentence in the chain that touches the
subject is `…V2_1_10_2_CORRECTION.md:648`, which asserts the claim is "written
after `AWAIT_STOP` returns `STOPPED` + `start_identity` | **unchanged**: the
same fact, obtained by the same syscall in a clean process" — an assertion about
*the stop fact* that never reaches the two identity keys. The word "unchanged"
there is exactly the kind of unverified carry-forward this chain has been
correcting for twelve rounds.

Neither contract can absorb the other silently:

- the PCS cannot write the claim: it has no access to `activation_record_sha256`,
  `behavior_source_sha256`, `config_sha256`, `stack_sha256`,
  `numerical_mode_sha256`, `device_identity` or `device_units`, which are
  peer-layer science and configuration data. This is not a choice I declined to
  make; it is infeasible without a redesign;
- the supervisor cannot obtain the two numbers, because no opcode emits one and
  P1 removed every other source (`fork`, `Popen`, `waitpid`);
- inventing a source, or writing a sentinel value into a signed record consumed
  by a freeze-acceptance predicate, would be a fabrication.

### 3.4 The two repairs, stated without preference

```text
OPTION A — extend the P1 response set with a read-only identity tuple.
  AWAIT_STOP additionally returns the target's pid and process-group number as
  data; the peer layer then writes the claim with its present key set intact.
  Cost: t-pcs.v1 acquires PID-valued RESPONSE fields, so the binding's
  derivation "t-pcs.v1 has no PID field, so the supervisor cannot express a
  PID" no longer holds as written. It must be re-grounded on the weaker and
  separately arguable premise that RECEIVING a number as data is not
  EXPRESSING it as an operation target — and every opcode's request side must
  still be proved to reject a PID.

OPTION B — relocate the identity keys out of the supervisor's reach.
  The pair is supplied by some means that puts no pid in the supervisor, or
  t-process-claim.v1 is amended so the pair travels as a P1 handle plus a
  PCS-side binding.
  Cost: t-process-claim.v1 is a signed T-activation-protocol schema and its
  process_group_id is read by §Z4.6 conjunct 7. Amending it reopens that
  predicate and every route that consumes it.
```

**The bounded choice is exactly:** which option is taken, and under Option A
whether a PID-valued *response* field is compatible with the signed sentence "It
cannot express a PID". No other question is open, and no other part of v1.2
depends on the answer — which is why v1.2 was completed in every other respect
rather than abandoned.

---

## 4. v1.1 → v1.2 replacement table

| v1.1 element | v1.2 disposition |
|---|---|
| title, replacement sentence | version 1.2; full replacement for v1.1 |
| status line | `CANDIDATE_FOR_INDEPENDENT_X_AND_Y_REVIEW_NOT_ACCEPTED` → `BLOCKED_ON_AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS_NOT_ACCEPTED` |
| — | **added**: a blocking notice immediately under the title, stating the cell before any other content |
| authority hierarchy item 3 | extended to name v1.1 as historical; the stale "§P1-16's provenance region" pointer corrected to §P1-18 |
| §P1-13 preamble | rewritten: the interface is now a total ownership matrix |
| — | **added §P1-13.0**: three logical layers, five process kinds, and rules `R-L1`–`R-L6` |
| §P1-13.1 peer contracts | retained byte-for-byte |
| §P1-13.2 "What P1 reads" (1 row, unnamed path) | **replaced** by the four-artifact matrix, 13 fields per row, literal paths and key sets |
| §P1-13.3 "What P1 provides" | retained and extended with the `SIGNAL_GROUP` mediation row; the process-claim consumer row now points at the blocked cell |
| §P1-13.4 "names but neither reads nor writes" | **deleted as literally false**; its two artifacts are now matrix rows 3 and 4 with their real read/write sets |
| §P1-13.5 settlement | renumbered §P1-13.4 |
| §P1-13.6 invalidity | renumbered §P1-13.5 |
| — | **added §P1-13.6**: closed invariant `SW-1`–`SW-5` |
| — | **added §P1-13.7**: eight interface operations, each assigned to exactly one root and function |
| §P1-13.7 out of scope | **replaced** by §P1-13.8, which excludes only peer-internal state no P1 path touches and explicitly forbids excluding any of the four artifacts |
| §P1-9.2 properties 7 and 8 | reworded: the watchdog *physically emits* a peer-owned record and owns none of the decision; `killer` named; pointers retargeted to rows 4 and 3 |
| §P1-9.4 `S-1`, §P1-11.6 | cross-references retargeted to the renumbered §P1-13.4 and §P1-13.5 |
| tests 84, 85 | **recomputed** |
| — | **added tests 86–91** (wrong logical writer; missing identity read; duplicate claim write; wrong freeze writer; process-name ownership inference; `SW-1`–`SW-5`) |
| provenance region | v1.1 composite and v1.1 closure digests appended |
| edit surface | `generic_harness.py` row names the eight single-install interface sites |
| everything else | byte-identical to v1.1 |

---

## 5. One-to-one disposition of I1–I4 and the four contradictions

### The four confirmed contradictions

| # | v1.1 defect | v1.2 disposition |
|---|---|---|
| 1 | §P1-13.2 said the supervisor makes the spawn intent durable, then said P1 writes no field of it | **CLOSED.** Row 1 states: logical writer = generic-harness peer layer; executing process = supervisor role process; P1 layer = reader only, of five named fields. `R-L1` makes the split a stated rule, not an inference |
| 2 | §P1-13.3 said the claim is written by the supervisor, then said P1 writes it nowhere | **OWNERSHIP CLOSED, VALUES BLOCKED.** Row 2 states writer = peer layer, executing process = supervisor, P1 reads nothing, P1 provides a three-field evidence tuple. The ownership confusion is gone; the field-availability conflict of §3 is what blocks |
| 3 | §P1-13.4's title "neither reads nor writes" was literally false — `c17` reads the identity record, the watchdog reads it, the watchdog writes the freeze record | **CLOSED.** That subsection is deleted. Row 3 lists four reader classes including `c17` and the watchdog; row 4 names the watchdog as an executing process |
| 4 | test 84 and the out-of-scope table inherited the incomplete read/write set | **CLOSED.** Test 84 recomputed against the matrix; test 85 now fails a build that moves any of the four artifacts into the out-of-scope list; §P1-13.8 states that prohibition in its own text |

### I1 — logical ownership separate from process residence

§P1-13.0 delivers: a three-layer table (owner of decision, code roots, schema
authority); a five-process table (creator, layers executing inside, notes),
covering the PCS bootstrap, middle, supervisor role, watchdog role and
controller/worker role; and six rules. `R-L1` states that a supervisor-process
write is not automatically a P1-layer write. `R-L2` states that a peer-owned
schema may be read or physically emitted by a P1-created role and must then
appear in the matrix. `R-L3` states that no artifact has two logical writers and
that residence never decides schema authority. `R-L4` fixes co-resident call
direction as one-way, peer → P1, through the nine opcodes and nothing else. No
new module was invented and no process was split.

### I2 — the four artifacts, literalized with sources

Every literal below is traced to an accepted document, cited in §7.

1. **Spawn intent** — path `…/T_SUPERVISOR/CHILDREN/<spawn_intent_id>.json`;
   nine keys; `role` enum is `{CONTROLLER, WORKER}` with `WATCHDOG` removed;
   peer writes no-replace under `T_RUNTIME.lock` durably **before** `SPAWN_ROLE`;
   the PCS reads five fields and rebuilds argv; **no argv crosses the wire**.
2. **Process claim** — path `…/runtime/T_PROCESS_CLAIMS/<process_id>.json`;
   twenty keys listed literally; peer writes after `AWAIT_STOP` returns
   `STOPPED`; P1 reads nothing; **blocked on the two identity keys**.
3. **Supervisor identity** — path `…/T_SUPERVISOR/SUPERVISOR_IDENTITY.json`;
   eight keys; `supervisor_generation_sha256` identified as the digest of the
   record's canonical bytes and *not* a key; installed by the peer layer
   executing in the supervisor role while `SPAWN.lock` is held at slot 3;
   read by `c17`, by the watchdog, by every freeze writer for its generation
   check, and by peer takeover; **removed only by peer takeover phase 1 — P1
   removes it on no route, including every §P1-11.5 terminal**.
4. **Freeze observation** — path `…/WATCHDOG/FREEZE/<witness_id>.json` with
   `witness_id` = SHA-256 of the canonical `{supervisor_generation_sha256,
   process_id, table_seq}`; fifteen keys; the production order (re-read the
   identity record, refuse on generation mismatch, write, then emit the pipe
   event) and the no-replace collision rule stated literally.

**The fallback question I was told not to guess at — answered from the chain,
not chosen.** The accepted chain **does** permit the supervisor to write
`t-freeze-observation.v1`. The evidence is two-part and mutually confirming:
the signed key set contains `killer ∈ {WATCHDOG, SUPERVISOR}`
(`V2_1_1_CORRECTION.md:1005-1012`), and §W3.5's ack-absence row reads
"watchdog declared dead: supervisor freezes all live groups itself per §W3.3
with `killer = SUPERVISOR`" (`V2_1_CORRECTION.md:831`).

- **Which logical layer owns it:** the generic-harness peer layer's
  **freeze-witness function** — one logical writer, two possible executing
  processes.
- **Why single-writer is not violated:** the record carries a mandatory
  discriminator, `killer`, naming which process executed the write. No reader
  infers authority from residence and no two writers race. This is `R-L5`, and
  row 4 is the only artifact in that class.
- **Why C1 is not violated:** C1 selected a dedicated freezer watchdog as the
  *normal* witness; the supervisor branch is part of the signed watchdog failure
  table itself, not a competing watchdog. Under P1 that branch additionally
  requires `SIGNAL_GROUP`, so the supervisor's freeze is PCS-mediated like every
  other group stop.
- **What P1 replaced in that same route:** only the tail clause. The historical
  route ended by having the supervisor *fork a new watchdog*; under P1
  replacement is `SPAWN_WATCHDOG`, uniform with the first
  (`V2_1_10_4_P1_BINDING.md:131`). The freeze-and-observe half, including the
  `SUPERVISOR` discriminator value, is retained.

I also named two adjacent peer artifacts — the freeze **fallback** record
(supervisor-written, in a namespace the watchdog has no path to) and the
**replacement-freeze** record — so that their absence from the matrix is not
misread as an omission. Neither is touched by any P1 path.

### I3 — interface tests and out-of-scope boundary

§P1-13.2–§P1-13.7 replaced by the matrix plus the single-writer invariant plus
the implementation surface. Test 84 recomputed. Tests 86–90 are the five
commissioned negative tests, one per line, each phrased as a build that must
fail. Test 91 covers `SW-1`–`SW-5`. §P1-13.8 excludes only peer-internal state
and carries its own prohibition against excluding the four artifacts. §P1-13.7
assigns all eight interface operations to exactly one root and function each,
and states that **no P1 root contains an install site for any of the four
artifacts** — the PCS root opens exactly two peer-owned artifacts, both
read-only.

### I4 — v1.1 mechanics preserved

Verified mechanically in §6.

---

## 6. No-regression table

| Preserved property | Evidence on final v1.2 bytes |
|---|---|
| six unique sentinels, correct order | lines 154, 2786, 2788, 2823, 2825, 2892; substring count exactly 1 for each of the six across the whole file |
| extraction/order/cardinality rules, `G-8`, `G-9`, byte-construction | in `BODY`, untouched by this round's edits |
| `BODY` normative, `GUARDDATA` normative, `PROVENANCE` non-normative | region scheme untouched; `H_GUARDDATA` **byte-identical to v1.1** |
| zero placeholders in normative regions | 27-pattern audit over 2 665 lines / 163 138 bytes: all zero. `identical to` = 1, the same benign §P1-11.1 P2a comparison predicate classified in the v1.1 closure |
| zero guard fires | all 30 guard patterns vs `NORMALIZE(REGION(BODY))`: **TOTAL GUARD FIRES: 0** |
| `G-1`…`G-10`, `S-1`…`S-24b` | untouched |
| region/file hashes, acyclic custody | four digests recomputed; v1.2 contains none of its own |
| all 85 v1.1 test obligations | rows 1–83 untouched; 84 and 85 recomputed as commissioned; 86–91 added; highest row number 91, count 91 |
| topology, descriptors, opcodes, journals, crash cuts | untouched; §P1-13.0's process table is a map over the existing topology and adds no process |
| subreaper/A3 safety–liveness boundary, `S1`–`S4`, `L1`–`L5` | untouched |
| signed A3/B1/C1/D1/K1/P1 | untouched; C1's dedicated-freezer semantics re-grounded in §P1-13.2 row 4 without weakening |
| `T NOT_ACTIVATED`, claim `OPEN`, no implementation authority | restated; status line now additionally blocked |

**Prior X findings, still closed.** MAJOR 1 (no operative composite; `S-23`,
`S-26`, `S-27`, `S-28` had no decidable domain) — closed by the single composite
and retained. MINOR 1 (`S-25` could not statically prove a direct PCS child) —
the `S-24a`/`S-24b` split plus test 33 retained untouched. MINOR 2 (hash block
not self-sufficient) — the four-digest scheme retained. v1.1's own three
closures — R1 marker collision, R2 placeholders, R3 guard-data authority — all
re-verified above on v1.2 bytes.

---

## 7. Peer-contract source locations for every literal

| Literal | Source |
|---|---|
| spawn-intent path, schema, nine keys, role enum minus `WATCHDOG` | `…V2_1_1_CORRECTION.md:672-679` (§Z3.2) |
| spawn-intent writer, lock, no-replace, removal authority | `…V2_1_1_CORRECTION.md:1699` (artifact table) |
| spawn intent durable **before** `SPAWN_ROLE`; PCS reads and rebuilds argv; no argv on the wire | `…V2_1_10_2_CORRECTION.md:365-376` |
| process-claim path | `OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:83` |
| process-claim twenty keys | `OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:233-238` |
| claim written after `AWAIT_STOP` returns `STOPPED` | `…V2_1_10_2_CORRECTION.md:648` |
| `AWAIT_STOP` response operands | `…V2_1_10_2_CORRECTION.md:366` |
| supervisor-identity schema and eight keys; `supervisor_generation_sha256` is the record's digest | `…SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md:216-232` (§S2.2) |
| supervisor-identity writer (grandchild under `SPAWN.lock`), no-replace, removed by client takeover phase 1 | `…V2_1_1_CORRECTION.md:1694` |
| freeze-observation `witness_id` preimage, path, fifteen keys, `killer` enum | `…V2_1_1_CORRECTION.md:999-1012` (§Z4.5) |
| freeze production order, generation re-read, no-replace collision rule, removal authority | `…V2_1_1_CORRECTION.md:1014-1027` |
| freeze writer "watchdog (or supervisor when the watchdog is dead)", witness authority | `…V2_1_1_CORRECTION.md:1704` |
| §W3.5 ack-absence row: supervisor freezes with `killer = SUPERVISOR` | `…V2_1_CORRECTION.md:831` |
| P1 replaces only the "forks a new watchdog" clause with `SPAWN_WATCHDOG` | `…V2_1_10_4_P1_BINDING.md:131` |
| C1 retained with `WATCHDOG/FREEZE/<witness_id>.json` observations | `…V2_1_10_4_P1_BINDING.md:857-866` (§P1B.13) |
| freeze **fallback** schema, supervisor-only, watchdog has no path | `…V2_1_2_CORRECTION.md:833-871`, `:1351` (§N5) |
| replacement-freeze record | `…V2_1_2_CORRECTION.md:950-960` (§N5.6) |
| §Z4.6 conjunct 7 reads the claim's `process_group_id` | `…V2_1_1_CORRECTION.md:1047` |
| "cannot express a PID" | `OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md:24-26`; derived at `…V2_1_10_4_P1_BINDING.md:156-158` |

The current untracked `generic_harness.py` and its tests were consulted only as
non-authoritative evidence of where `t-process-claim.v1` is constructed
(`src/philosophia/officina/runtime.py:47`, `:391-404`). Nothing in them was
treated as governing and neither was modified.

---

## 8. Exact implementation, verifier, test and manifest surface

| Surface | Change v1.2 would require, once the cell is signed |
|---|---|
| `scripts/officina_process_control_bootstrap.py` | the PCS; opens exactly two peer-owned artifacts, both read-only (spawn intent at `SPAWN_ROLE`; supervisor identity at `c17`); contains **no** install site for any of the four artifacts |
| `scripts/officina_role_bootstrap.py` | the four-role isolated entry; unchanged by this round |
| `src/philosophia/officina/generic_harness.py` | the eight single-install interface sites of §P1-13.7, including exactly **one** freeze-witness function called from both the watchdog role entry and the supervisor dead-watchdog route, setting `killer` from its caller |
| `src/philosophia/officina/verification.py` | CHANGES 1–5, rules `S-1`…`S-24b`, guards `G-1`…`G-10`; plus the single-install check backing tests 86, 88 and 91 |
| `PRODUCTION_CALL_GRAPH.json` | five roots, reachable closure, five root digests, four composite digest fields |
| test modules | §P1-15's 91 rows, of which 84–91 are this round's |
| manifest | `p1_composite_sha256`, `p1_composite_body_sha256`, `p1_composite_guarddata_sha256`, `p1_composite_normative_sha256` |

All of it remains unwritten. This round created no code, no test and no manifest.

---

## 9. Weakest points, and bounded X/Y questions on identical bytes

These are where I judge my own work weakest. Offered as attack surface.

1. **The blocking analysis is the load-bearing claim of this round.** If a
   reviewer finds any accepted document that supplies `controller_pid` or
   `process_group_id` to the supervisor, the block is wrong and v1.2 should be
   `READY` with row 2 completed. I searched the P1 chain and the artifact
   tables; I did not read every line of every historical draft.
2. **`R-L5` and the `killer` discriminator are my reconciliation**, not a
   sentence any signed document contains. The chain gives the enum and the
   §W3.5 row; the inference that these together preserve single-writer is mine.
3. **Row 3's claim that P1 removes the supervisor identity record on no route**
   should be checked against every §P1-11.5 terminal and §P1-11.3's removal
   order, which lists only the four singleton spawn records.
4. **§P1-13.0's five-process table** asserts the supervisor is the only process
   with two co-resident layers. A reviewer should test that against the watchdog,
   which executes a P1 role entry and then peer witness code.
5. **§P1-13.8's boundary** is a judgement about what "no P1 path consumes or
   produces" means. The freeze-evidence acceptance predicate is excluded, yet
   its input is a record a P1-created role emits.
6. **Carried from v1.1 and not re-examined this round:** the preamble/`H_BODY`
   split; `G-10` being discipline rather than mechanism; the `_recvmsg` handler
   residual; the `S-24a`/`S-24b` decomposition of `TI-1`.

**Bounded questions for X and Y on identical bytes:**

1. Recompute all four digests. Is the block of §3 real — does any accepted
   document supply the two identity keys to the supervisor under P1?
2. If real, is Option A compatible with "It cannot express a PID", or does a
   PID-valued response field break the binding's derivation?
3. Does the `killer` discriminator genuinely preserve single-writer, or is the
   dead-watchdog route two writers wearing one name?
4. Does §P1-13.2 partition the interface with no gap and no overlap — are there
   a fifth artifact, or a P1 read, that the matrix omits?
5. Does §P1-13.7's single-install assignment actually prevent both layers from
   installing the same no-replace record, given they share a process?
6. Do tests 86–91 have decidable failure conditions, or does test 90 in
   particular require a judgement a verifier cannot make?

---

## 10. Scope and negative space

This closure creates nothing executable. It authorizes no implementation,
commit, host change, verifier edit, manifest write, process, socket, pipe, fork,
exec, signal, wait or `prctl` call; no supervisor, PCS, controller, worker or
watchdog; no capability, world, learner, entropy, capacity artifact, custody
disposition, result manifest, quarantine record, promoted object, freeze
witness, spend, datum, outcome, Proof or claim movement. It predicts no
qualification and no comparison outcome.

## 11. Verdict

```text
BLOCKED_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_V1_2_AUTHOR_CELL
AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS
```

Meaning, precisely: I1, I3 and I4 are complete; three of the four artifact rows
of I2 are complete; all four named ownership contradictions are closed as
ownership defects. The fourth artifact row cannot be completed because two
separately signed contracts disagree about whether the layer that must write
`t-process-claim.v1` can obtain `controller_pid` and `process_group_id`, and the
accepted chain does not resolve it. Both coherent repairs are stated with their
costs. **I chose neither.** The rest of v1.2 is a finished replacement for v1.1
so that the signed decision lands in a document that is otherwise ready for
X-line and Y-line review.

This is not an X or Y verdict, and it clears nothing. `T` remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
