REVISE_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_PACKET

# X-line engineering review — P1 process-claim identity author-choice packet v1

**Reviewer:** Claude Code Opus 4.8, independent X-line. I did not author this
packet or any document in the supervisor/control-channel chain. Read-only
inspection and SHA-256 only; no file was edited, no code implemented, no
behavioural probe or process-control operation run. `T` remains `NOT_ACTIVATED`;
the programme claim remains `OPEN`. This review authorizes nothing: not a
selection, not an implementation, not a spend, datum or outcome. A `REVISE`
verdict is not a Y-line verdict and not a signature.

---

## 0. Custody — hashes recomputed

Both target artifacts hash to the exact expected values on the committed bytes:

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md   [MATCH]
e8bceb8098c9a1d96fcd76f0796fccdcd49b79ce4cd690d1ef3a7d9ced54e128  reviews/opus5_officina_p1_process_claim_identity_author_choice_packet.md      [MATCH]
```

The two files are **not** byte-identical (they were never meant to be: two
distinct expected digests). The `successor/` file is the 664-line choice packet;
the `reviews/` file is the 318-line author closure whose first line is
`READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_XY_REVIEW`. I reviewed the
committed bytes of each, and I treated every sentence of the author closure as
untrusted, re-deriving each load-bearing claim from the signed contracts rather
than from either author document.

**Source contracts inspected directly** (not via the packet's quotations):
`OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md`;
`OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md`;
`OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md`;
`…_V2_1_10_2_CORRECTION.md`; `…_V2_1_1_CORRECTION.md`; `…_V2_1_10_CORRECTION.md`;
`…_V2_1_10_4_P1_BINDING.md`.

---

## 1. Findings first

### CRITICAL

None. The conflict is real, Option A's architecture is sound and does not weaken
the safety property, and Option B is honestly non-selectable. Nothing here would
make Option A unsafe or the choice ill-posed. The two Major findings are
accuracy/completeness defects in the packet-as-written, not defeats of Option A.

### MAJOR

**M-1 — §2.7 / §2.9 / §5.3: replay durability of the tuple is asserted on an
existing guarantee that the cited bytes do not establish, and the resulting
journal-schema edit is missing from the blast-radius (§5) and the v1.3 handoff
(§7).**

§2.7 states the tuple "is part of the recorded response of the J4 COMPLETED
journal entry, **exactly as `start_identity` already is**," and §2.9's `J4→J5`
cut promises "a redelivery returns the recorded tuple with no re-observation."
The whole B1 argument for Option A rests on that premise. But the committed v1.2
journal and replay text does not carry it:

- §P1-8.6 `J4` records exactly
  `{ ..., state: COMPLETED, outcome, handle_id, fd_vector_len }`
  (composite line 1289). It names `outcome` but **not** `start_identity` and
  **not** `pgid_is_leader`.
- The `COMPLETED` replay row returns "the recorded **status, detail and handle**,
  with status REPLAYED" (composite line 1301). It, too, names neither
  `start_identity` nor `pgid_is_leader`.

So the AWAIT_STOP-specific operands are not shown, by the cited bytes, to be
journaled or redelivered today. Two consequences:

1. The premise "exactly as `start_identity` already is" is **not verifiable from
   the contract**. Either v1.2 already redelivers the full response payload —
   in which case the `J4` record and the replay row are under-enumerated even for
   v1.2 (a pre-existing documentation gap the packet leans on without naming), or
   it does not — in which case a crash in the `J4→peer-claim-write` window would
   already lose `start_identity`, and Option A inherits that hole for all four of
   `start_identity`, `pgid_is_leader`, `attested_pid`, `attested_pgid`.
2. Whichever is true, making the tuple crash-durable under Option A **requires
   amending the `J4` record schema and the `COMPLETED`/`ACKED` replay rows** to
   name the full AWAIT_STOP operand set. That edit is a change to the durable
   journal record format. §5.4/§5.5 describe A's surface as "one opcode's
   response, one signature sentence, four verifier rules" and "delete two
   response fields … nothing durable changes shape," and §7 step 8 speaks only of
   "the §2.7 replay prohibition." **None of these mentions the journal record
   schema.** The comparative recommendation in §6/§7 — "A touches one sentence and
   one response grammar" — is materially understated if A also touches the
   process-control journal record format, which by M-1 it must.

Counterexample that the packet's current text does not close: crash between `J4`
and the peer's claim write; PCS restarts, supervisor replays the AWAIT_STOP
request; per the literal §P1-8.6 `COMPLETED` row the reply carries `status,
detail, handle` — reconstructing `outcome` from the record but with no specified
carrier for `start_identity`, `pgid_is_leader`, `attested_pid`, `attested_pgid`.
The peer then cannot write a complete claim, and the both-or-neither invariant
(§2.2) is satisfied only vacuously (neither present). This is exactly the
"produce … a tuple detached from its handle/generation" hazard the round asked me
to attack, surviving because durability was assumed rather than specified.

Required to clear M-1: v1.3 must (a) state that `J4` records the complete
AWAIT_STOP operand vector including the two new fields; (b) rewrite the
`COMPLETED`/`ACKED` replay rows to redeliver that vector verbatim; (c) move the
journal record schema into A's blast-radius in §5 and into the §7 handoff; and
(d) correct §2.7's "exactly as `start_identity` already is" to state plainly that
`start_identity`'s own journal durability is being made explicit here, not merely
inherited.

**M-2 — §2.6 / §5.6: the no-second-sink guarantee — Option A's entire safety
delta over a naive PID field — rests on `S-25d` taint completeness that the
packet asserts but does not establish, and the enumerated propagation classes are
not closed under Python semantics.**

Option A's honest case (§5.6) is that it weakens the *English sentence* but not
the *safety property*, because `S-25a`–`S-25d` prove the two integers reach only
the two claim keys. That reduction is only as strong as `S-25d`. §2.6 justifies
decidability with: "the supervisor's code lives in one reviewed root and both
values are plain ints, never containers or callables," and `S-25d` propagates
taint "through assignment, arithmetic, formatting and container insertion."

The stated propagation set is **not complete** for the language. Values are
laundered to a fresh, untainted binding through constructs outside those four
classes — function/lambda application `p2 = (lambda v: v)(attested_pid)`,
iterable unpacking `(a,) = (attested_pid,)`, comprehension binding
`[x for x in (attested_pid,)]`, and builtin round-trips such as
`int(str(attested_pid))`. "Never containers or callables" constrains the
*values*, not the *code* that may wrap an int and hand the result to a later
sink. If `S-25d`'s taint is unsound at any one of these, a derived value reaches
a log, a second durable artifact, or a request builder **without being flagged**,
and the "reaches exactly two keys" claim fails silently. The packet's own §9.3
concedes `S-25d` "is the only genuinely new verification technique … and has had
the least scrutiny," and X-line question 3 asks precisely whether a container, a
format string, or an arithmetic round-trip defeats it — so this is in scope and
unresolved by the text.

`S-25a` (parsed at exactly one site, one plain Name, assigned once, never
rebound) plus `S-25c` (syntactic reaching check over control-plane sinks) are
strong and make evasion hard, but they do not by themselves prove completeness:
`S-25c` catches only the sink shapes it enumerates, and `S-25d` is the component
that is supposed to close the residual. Asserting its completeness is not proving
it.

Required to clear M-2: rather than rely on taint soundness, v1.3 should pin a
**closed whitelist of the operations permitted on the two Names** — bind once
from the parse site, pass unmodified as the `controller_pid` / `process_group_id`
arguments of the claim constructor, and nothing else (no arithmetic, no
formatting, no insertion, no call, no unpack). Any other syntactic use of either
Name is a static violation. That makes the no-second-sink property a decidable
syntactic check independent of taint-propagation completeness, which is the
guarantee §5.6 needs and currently over-claims.

### MINOR

**m-1 — §2.3 A-P4 re-reads `getpgid` although the PCS handle table already holds
`pgid_or_null`.** §P1-8.5 stores `handle_id -> { pid, start_identity,
pgid_or_null, … }` (composite line 1260), so the PCS already owns a pgid for the
handle. A-P4 instead calls `os.getpgid(attested_pid)` fresh "immediately after
A-P2." This is safe (`setsid=True`, verified below, forces `pgid==pid`; the
target argv has not run at the `A-12` self-stop, so the role cannot have called
`setpgid`), but the packet should say which value is authoritative and why a
fresh read is preferred over the stored one, so an implementer does not diverge.
Not a defect in the proof; a specification-tightening.

**m-2 — §2.10 / §2.2 pid digit bound is correct but its justification is
absent.** `attested_pid` is bounded to `1..7 digits, value ≥ 1`. On 64-bit Linux
`PID_MAX_LIMIT` is `0x400000 = 4194304` (7 digits), so the bound is exactly
adequate and the +16-byte frame arithmetic is right. The packet asserts the
7-digit bound without stating the kernel limit it relies on; if any deployment
raised `pid_max` past `4194304` the bound would truncate. Recommend recording
`PID_MAX_LIMIT` as the pinned justification and an explicit refusal
(`TRANSPORT_STRUCTURAL`) on an 8-digit value rather than a silent field-width
assumption.

**m-3 — §6 wording risk.** The composite already documents, at line 1781, that
freeze is unavailable *to the supervisor* on channel EOF (PCS death). §6's defect
is the distinct *watchdog* freeze on update-pipe EOF (supervisor death),
§P1-9.2 property 12. Both are real and independent, but a reader skimming both
sentences could conflate them. §6 should cite property 12 and line 1781 side by
side and state they are two different actors, so the orthogonal defect is not
mistaken for the already-noted supervisor case. (Content correct; see §5.)

---

## 2. Conflict — independently re-derived, CONFIRMED

I re-established the conflict from the contracts, treating both author documents
as untrusted. It holds, and the composite states it identically at its own Row 2.

| Claim | Independent verification |
|---|---|
| `t-process-claim.v1` has 20 keys incl. `controller_pid`, `controller_start_identity`, `process_group_id` | `…ACTIVATION_PROTOCOL_V2_CORRECTION.md:233-238` — counted 20 keys; the three integers present. **Confirmed.** Also mirrored at composite §P1-13.2 Row 2, lines 2104-2110. |
| lease = "claim keys plus five" ⇒ both integers propagate | `…ACTIVATION_PROTOCOL_V2_CORRECTION.md:240-245`. **Confirmed.** |
| `process_group_id` is load-bearing — §Z4.6 conjunct 7 dereferences it | `…V2_1_1_CORRECTION.md:1047`: "pgid == the claim's process_group_id and start_identity == the claim's controller_start_identity". **Confirmed.** Restated at composite line 2116-2119. |
| supervisor holds no numeric identity ("opaque handles only … cannot express a PID") | `…PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md:24-26`, verbatim. Derivation at `…V2_1_10_4_P1_BINDING.md:156-158`. **Confirmed.** |
| all nine opcode responses carry no pid/pgid | Recomputed from the **signed** opcode table at composite §P1-8.3 (lines 1218-1228), not from the packet's §1.3 table. Total response operand set: `handle_id` (SPAWN_ROLE, SPAWN_WATCHDOG); `outcome`/`start_identity`/`pgid_is_leader` (AWAIT_STOP); `result` (SIGNAL_ROLE, SIGNAL_GROUP); the six-token WAIT_ONE classifier (REAP_ROLE); nothing (RELEASE_HANDLE, SHUTDOWN); `pcs_uptime_ticks` (PING). **No pid, no pgid, anywhere.** `pgid_is_leader ∈ {0,1}` names neither number. The enumeration of §1.3 is **exhaustive and correct** (answers author X-question 1: nothing missed). |
| every alternative source excluded | Four singleton records name only PCS/middle/supervisor (§P1-5.1); `t-fork-child.v1` is a supervisor-forked watchdog, P1-orphaned; the worker status pipe is empty because the role self-stops at `A-12` before writing (§P1-7.4); `os.getpgid` needs a pid (circular). **Confirmed.** |

The composite itself certifies the gap (lines 2130-2136): `controller_pid ←
no source UNAVAILABLE`, `process_group_id ← no source UNAVAILABLE`, everything
else `AVAILABLE`. The conflict is a genuine clash between two separately signed
contracts, not an implementation gap.

**§Z3.4 correction (§1.5) — CONFIRMED, and it does not change the choice.** The
`/proc/*/cmdline` discovery predicate is real (`…V2_1_1_CORRECTION.md:758-778`)
and requires `cmdline[3] == "--officina-bootstrap"` and `cmdline[6] ==
"--officina-spawn-intent"`. The selected P1 role argv (composite §P1-7.4, lines
961-983) fixes index 3 = `-E` and index 6 = `--officina-role`, with the
spawn-intent marker at index 12 and the hex at 13. The predicate therefore
matches **zero** P1 processes — verified by direct index comparison. Independently,
argv-as-evidence was deleted outright (`…V2_1_10_CORRECTION.md:188`, verbatim:
"No layer of this contract henceforth treats argv as evidence of a clean image,
of a fresh `execve`, or of the executor set."). Both of the packet's grounds
hold; v1.2's "cannot obtain" was correctly softened to "no *authorized,
non-stale* source." That §Z3.4 is stale is a separate peer-chain defect, rightly
recorded and not repaired here. The stale route does **not** reopen the choice:
re-indexing it is Option C, which is dominated by A (same numeric exposure, no
PCS proof) and remains deleted-basis; see §4.

---

## 3. Option A — mechanical attack

### 3.1 Grammar, field order, bounds, frame arithmetic — PASS (see m-2)

The v1.2 response prefix is 8 fields (schema, version, generation_id,
request_id, status, detail, handle_id, fds_redelivered — composite lines
1210-1216) and AWAIT_STOP appends `outcome`, `start_identity`, `pgid_is_leader`
at 8/9/10. The packet's §2.2 indices 0-10 are therefore exact, and
`attested_pid`/`attested_pgid` at 11/12 are genuinely *appended* — an old
fixed-count parser fails closed, as claimed. Both-or-neither and the cross-field
invariant (`pgid_is_leader == 1 ⇔ attested_pid == attested_pgid`) are internally
consistent: for CONTROLLER/WORKER, `setsid=True` (composite lines 480-481) forces
`pgid==pid`, so both sides are always true and the invariant is a genuine
redundancy check, not dead weight. Frame worst case +16 bytes against a 4096
ceiling is correct given the 7-digit bound (m-2). AWAIT_STOP `STOPPED` is reached
only for self-stopping roles (controllers/workers), so the invariant is never
exercised on a non-leader watchdog.

### 3.2 A-P1…A-P6 bind pid/pgid/start-identity/handle to one stopped direct child — PASS

- **A-P1 (OWNED):** ownership model §P1-10.1 (lines 1520-1538) — `OWNED` is set
  only at a PCS `posix_spawn`/`fork` return; `CONTRADICTED`/`REAPED` are the only
  exits. Sound gate.
- **A-P2 (stopped direct child):** the single `_waitpid(pid, WNOHANG|WUNTRACED)`
  on the PCS's own direct child, `WIFSTOPPED` true. Matches §P1-10.2 WAIT_ONE
  precondition (line 1566: "OWNERSHIP(pid) is not REAPED").
- **A-P3 (provenance):** `attested_pid` is the PCS's own `posix_spawn` return —
  never `/proc`, never cmdline, never a peer artifact. This is the correct
  anti-stale-observation construction; the value pre-exists in the handle table
  `pid` field (line 1260), so no new observation is introduced (see m-1).
- **A-P4 (pgid):** `os.getpgid(attested_pid)` with `setsid=True` ⇒ `pgid==pid`;
  inequality ⇒ STRUCTURAL_VIOLATION, CONTRADICTED, no tuple. **Verified
  load-bearing fact:** `setsid=True` for CONTROLLER/WORKER at composite lines
  480-481. Because the role self-stops at `A-12` **before** any target argv runs
  (§P1-7.4), the contaminated payload cannot have called `setpgid` before the
  attestation instant, so `pgid==pid` cannot be subverted at claim time. This is
  the strongest link in the proof, not the weakest — contrary to the author's
  §9.2 worry, the self-stop ordering closes the setpgid attack.
- **A-P5 (start-identity):** `STAT_OBSERVE` PRESENT_VALID with matching start
  identity and state `T` — §P1-10.3 / I-3 table (lines 1623, 1640). Sound.
- **A-P6 (direct child):** follows from A-P3 + TI-1, not re-derived from `/proc`.
  Consistent with §P1-8.5 invariant "every handled process is a direct child of
  the PCS" (line 1274).

The conjuncts jointly bind both integers to the same stopped, unreaped,
direct-child process the handle denoted, at an instant the process provably holds
its pid. **No stale observation enters.** Answers author X-question 2
affirmatively, with the setsid ordering as the reason A-P4 cannot have changed
under it.

### 3.3 Counterexamples attempted

| Attack | Outcome |
|---|---|
| **PID reuse** between attestation and claim consumption | Closed by §P1-10.1 reuse proof (lines 1541-1550): `SIGCHLD` normalized to `SIG_DFL`, neither `SIG_IGN` nor `SA_NOCLDWAIT`, **before the child existed**; the task holds its pid as a zombie until the PCS's own targeted reap. `REAPED` then forbids further use. A recycled pid additionally fails §Z4.6 conjunct 7 unchanged, since the claim also stores `controller_start_identity` and the predicate compares both. **Prevented.** |
| **Child exit/reap between A-P2 and A-P4** | The tuple is emitted only while `OWNED` and unreaped; A-P4 runs immediately after A-P2 on a still-stopped, still-owned child. Any `ECHILD`/`ESRCH`/mismatch drives `CONTRADICTED` and no tuple. `getpgid` on a still-unreaped zombie is well-defined. **Prevented.** |
| **Replayed COMPLETED** | Intended: recorded bytes, no re-observation, and re-running A-P2 post-`REAPED` would violate WAIT_ONE's precondition (line 1566) — correctly prohibited in §2.7. **But durability of the recorded bytes is not established by the cited journal text — see M-1.** Mechanism right, spec incomplete. |
| **Malformed decimal / leading zero / 8-digit pid** | `attested_*` grammar rejects leading zero and `< 1`; both-or-neither and cross-field checks are TRANSPORT_STRUCTURAL. 8-digit value handling is not explicitly refused — m-2. |
| **STOPPED/EXITED confusion** | Tuple only on `outcome==STOPPED`; `EXITED`/`TIMEOUT`/refusals emit `-`/`-` (A-T1, A-T6). Enforced and tested. **Prevented.** |
| **Wrong handle** | Selection is by `handle_id` only (A-R2); `attested_pid` is never a selector (§2.2). Request grammar unchanged (§P1-8.3 line 1240). **Prevented.** |
| **Mismatched pgid** | `pgid != pid` ⇒ STRUCTURAL_VIOLATION, no tuple (A-P4). **Prevented.** |
| **Taint via container/alias/serialization / future second sink** | The stated `S-25d` propagation classes do not cover lambda/function application, unpacking, comprehension binding, or builtin round-trips — **M-2**. This is the one attack the verifier does not provably stop as written. |

### 3.4 Request grammar stays PID-free — PASS

A-R1…A-R6 close the request side, and the signed §P1-8.3 already states "No
field of any request or response carries a PID" (line 1240). Under A the
*response* gains a PID but no request field does; handle selection, signal
targets, journal key `(generation_id, request_id)` and retry key are all
unchanged and PID-free. **Confirmed.**

### 3.5 A3 / bounded weakening — PASS on substance

§5.6's three-way separation (OS information the same-UID supervisor can already
read; authorized addressing, untouched; same-UID kernel capability, unchanged) is
sound. v1.2 §P1-12.3 affirms the same-UID actor already can "stop, kill, or delay
any same-UID process," so A transfers no capability; it adds a response field
feeding one already-signed sink, and R-L4 is preserved because P1 still opens no
peer artifact (§P1-13.2 Row 2, line 2120: "fields P1 reads: none"). The amended
sentence (§2.10) is a genuine, correctly-labelled *bounded weakening* — lexical
"no PID exists" becomes dataflow "PIDs exist, proved to reach one sink" — and the
packet says so plainly rather than claiming equivalence. **Substantively
correct.** The residual real cost is testability, and M-2 is exactly where that
cost is currently under-secured: the dataflow property is only as sound as
`S-25d`, which the packet has not closed.

---

## 4. Option B — non-selectability CONFIRMED; Option C rejection CONFIRMED

B's two blocking sub-cells are real, verified against the architecture:

- **B-1 (PCS gains a peer-visible durable-write role):** under v1.2 the PCS
  writes exactly the four singleton spawn records and its journal (composite line
  471, line 1995). A fifth peer-visible PCS-written artifact class expands a
  signed property of the selected architecture. The "supervisor writes the
  binding from an attested response" alternative **is** Option A — so it is no
  alternative. Correct.
- **B-2 (peer predicate reads a P1-owned artifact):** making §Z4.6 conjunct 7
  dereference a P1-owned binding inverts **R-L4**, verified verbatim at composite
  lines 2022-2027: "Co-resident call direction is one-way: the … peer layer calls
  INTO the P1 layer … The P1 layer never … opens a peer artifact except the one
  row 1 names." A peer predicate opening a P1-owned file crosses that boundary the
  other way and needs its own signature. Correct.

B is therefore fully specified and correctly marked non-selectable behind two
named author cells (answers author Y-question 3: they are genuinely separate;
neither is resolvable inside the signed chain). **The stale §Z3.4 route does not
make B or C selectable** and does not change the recommendation — §3/§2 above.

Option C (re-index §Z3.4 to P1 argv) is correctly examined and rejected: it makes
the contaminated supervisor's own unattested scan the identity source, is
argv-as-evidence (deleted), and is strictly dominated by A. Recording it for
audit rather than offering it is the right call.

---

## 5. Watchdog-freeze defect (§6) — orthogonal, real, does not clear A

Independently confirmed as a genuine v1.2 defect, not a packet artifact:

- §P1-9.2 property 12 (composite line 1464): on update-pipe EOF the watchdog
  "freezes the groups it knows, writes their observations, and exits."
- §P1-9.2 property 6 (line 1446): it "communicates only over its two sealed pipes
  at slots 3 and 4" — the update pipe and the ack pipe.
- Watchdog fdmap is `{3,4,5,7,8,9,10}` (lines 680, 978); slot 6 — the sole
  supervisor↔PCS control socket (line 1167) — is **absent**. The watchdog thus
  holds no PCS socket, cannot issue `SIGNAL_GROUP`, and under P1 all process
  authority is the PCS's. At freeze time the supervisor is already dead, so no
  relay exists. A `killpg(SIGSTOP)` + quiescence proof is therefore unexecutable
  by the only actor property 12 assigns it to.

This is distinct from the already-documented supervisor-side unavailability at
line 1781 (which is PCS death, a different actor and trigger — see m-3).

**Interaction with A:** the defect shares A's root class (numeric-identity
provenance) — the freeze witness carries a numeric `pgid` key (conjunct 9,
`…V2_1_1_CORRECTION.md:1049`; witness schema at composite line 2241) whose source
is as open as the claim's `process_group_id`. **But Option A does not touch it:**
A attests the tuple to the *supervisor*, which is dead at watchdog-freeze time and
has no channel to the watchdog; the watchdog writes its own witness `pgid` after
supervisor death by a mechanism A neither supplies nor removes. B likewise leaves
it unaddressed. The packet's §6 states this correctly and does not smuggle a fix.
**Recorded, per the round's instruction, as an interaction that neither clears A
nor is cleared by A.** It means that even with A selected, P1 remains
non-operative until `AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM` is resolved — a
scope fact, not a defect in this packet.

---

## 6. Why REVISE, not CONFIRMED or BLOCKED

`CONFIRMED` would authorize Kirill's informed selection after Y confirms. An
informed selection depends on two things this packet currently states inaccurately
or leaves unproven, both of which bear directly on the criteria the recommendation
is built on:

- **M-1** understates Option A's edit surface (it also touches the durable journal
  record schema and the replay rows) and rests the B1/replay argument on an
  existing guarantee the cited bytes do not show. The recommendation's headline —
  "A touches one sentence and one response grammar" — is the criterion in
  question, so this is not cosmetic.
- **M-2** leaves Option A's sole safety delta (no second sink) resting on
  `S-25d` completeness that is asserted, self-described as least-scrutinized, and
  not closed against ordinary Python laundering. A closed operation-whitelist on
  the two Names would make the guarantee syntactic and decidable, which is what
  §5.6 needs.

Neither is a Critical: the conflict is real, the A-P proof is sound (with the
setsid ordering *strengthening* it), the request side stays PID-free, A3 is
correctly analysed, B is honestly non-selectable, and the watchdog defect is
correctly quarantined. So `BLOCKED` is not warranted either. The right verdict is
a bounded revision: fix M-1 and M-2, address the three Minors, and the packet
should be confirmable on the next pass.

---

## 7. Verdict

```text
REVISE_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_PACKET
```

Required for a subsequent `CONFIRMED`:

1. **M-1** — v1.3 (or a packet revision) must specify that the AWAIT_STOP `J4`
   journal record carries the full operand vector including `start_identity`,
   `pgid_is_leader`, `attested_pid`, `attested_pgid`; rewrite the
   `COMPLETED`/`ACKED` replay rows to redeliver it verbatim; add the journal
   record schema to A's blast-radius (§5) and the §7 handoff; and correct §2.7's
   "exactly as `start_identity` already is."
2. **M-2** — replace reliance on `S-25d` taint completeness with a closed
   whitelist of permitted operations on the two parsed Names (bind once,
   pass-through to the claim constructor only; any other syntactic use is a static
   violation), so the no-second-sink property is decidable and independent of
   propagation soundness.
3. **m-1 / m-2 / m-3** — state whether the stored `pgid_or_null` or a fresh
   `getpgid` is authoritative in A-P4; pin `PID_MAX_LIMIT` as the 7-digit
   justification and refuse an 8-digit value explicitly; and cite property 12 and
   line 1781 side by side in §6 to keep the watchdog and supervisor freeze cases
   distinct.

This verdict authorizes no implementation, activation, spend, datum, outcome,
selection or Y-line verdict. `T` remains `NOT_ACTIVATED`; the programme claim
remains `OPEN`. A selection token becomes signable only if a revised packet is
confirmed by both the X and Y lines on identical bytes and Kirill then signs.
