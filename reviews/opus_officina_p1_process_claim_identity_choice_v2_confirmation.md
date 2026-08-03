REVISE_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2

# Bounded X-line confirmation — P1 process-claim identity choice packet v2

**Reviewer:** Claude Code Opus, independent X-line. I did not author v2, v1, the
supervisor/control-channel chain, or either prior review. This is a bounded
confirmation round: I check, on the committed v2 bytes, whether each of the ten
prior findings is closed and whether the repairs introduced a new defect. I
treated the v2 closure as an untrusted author claim and re-derived every
load-bearing point from the signed contracts. Read-only; SHA-256 only; no file
edited but the one deliverable; no code, probe, or process-control operation
run. `T = NOT_ACTIVATED`; programme claim `OPEN`. This review authorizes no
selection, implementation, activation, spend, datum, or outcome.

---

## 0. Custody — all recomputed on committed bytes

**Targets:**

```text
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
```

**Prior reviews and v1, confirmed byte-untouched (match the closure's §2.1):**

```text
bfa7f6dd6a09313033b2a00c75f0e1e0632c63f65733b80424ee889433364f3b  reviews/opus_officina_p1_process_claim_identity_choice_review.md   [MATCH]
705b36b6ce1a9387261f66f2a473295be4384903b0e0240ae8e7496af6899e80  reviews/sol_officina_p1_process_claim_identity_choice_review.md    [MATCH]
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md   [MATCH]
```

**Governing contracts, recomputed — every digest matches the closure's §2.2:**

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  …P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  …PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  …V2_1_1_CORRECTION.md
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  …V2_1_10_CORRECTION.md
```

The bytes v2 repairs are the bytes the X and Y lines reviewed, and the contracts
I re-derive from are the signed ones.

---

## Verdict

**`REVISE_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2`.**

**Eight of the ten findings are confirmed closed on the v2 bytes** (X M-1, m-1,
m-2, m-3; Y-C2, Y-M1, Y-M2, Y-m1), each by a named repair I verified against the
cited contract bytes. **Determinations 3, 5, 6 and 7 are confirmed.**

**Two findings — X M-2 and Y-C1 — are substantially but not fully closed.** They
share one concrete residual defect: the §2.5/§2.6 *syntactic* closure is
equivalent to "no second sink" only in a root where reflective, iteration-based,
and attribute-based reads of the restricted values are foreclosed — and the root
where all the governed code lives, `generic_harness.py`, is **not** under that
lockdown. A concrete construct passes the stated verifier (S-25a–S-25h) and
reaches a second sink. This is exactly the failure mode the round was chartered
to catch (determination 2), so the honest answer to the closure's bounded
X-question is **NO**, and the verdict is a bounded revision with a small,
concrete repair (below). The occurrence-count idea is sound and the right
replacement for taint; it simply needs the peer root locked down and the record
representation pinned before it is airtight.

---

## Determination 2 — attack on the §2.5 occurrence whitelist (the residual defect)

**Decidable? Yes, in part.** S-25a/S-25b/S-25c/S-25e/S-25h are genuinely an
occurrence-count-plus-position-match over a single AST walk of the five roots,
with no fixpoint, call graph, or taint soundness — as claimed. The core insight
is correct: to launder a value *out of a named local*, code must reference the
Name, and any reference raises the count above the pinned three (S-25c). The four
laundering fixtures the v1 X-line named (`(lambda v:v)(attested_pid)`,
`(a,)=(attested_pid,)`, `[x for x in (attested_pid,)]`, `int(str(attested_pid))`)
are each genuinely rejected by the count, and A-T9 fixes them. That part of M-2
is real progress.

**Closed against *every* laundering path? No.** The count governs occurrences of
the two **Names**; S-25d/ACC-R1 govern **subscripts whose key operand is the
string literal** `"controller_pid"`/`"process_group_id"`. A read that uses
*neither* a governed Name *nor* those key literals is invisible to both, and
S-25f/S-25g — asserted "syntactic, no taint" (§2.11 decidability note) — can
recognize a `RESTRICTED_PROCESS_IDENTITY` value (defined *semantically* at
§2.6.1(e) as "every alias, copy, reload, … in-memory binding") only by its
whitelisted *shapes*, so they do not fire on a laundered shape. Three concrete
constructs pass the stated verifier and reach a second sink:

```python
# (all inside src/philosophia/officina/generic_harness.py — the peer layer)

# E1 — mapping-value iteration: no governed Name, no key-literal subscript
_vals = list(claim.values())          # claim is a t-process-claim.v1 mapping (C-1/reload)
_leaked = _vals[5]                     # controller_pid by position
<capacity / custody / selection / Q-C / scientific expr>(_leaked)

# E2 — reflective read: the Name "attested_pid" is a str Constant, not a Name node
_leaked = locals()["attested_pid"]     # S-25c count stays 3; ACC-R1 key is not governed
<peer-layer validity/science sink>(_leaked)

# E3 — attribute access on a dataclass claim (dataclasses is an allowed import)
_leaked = claim.controller_pid         # no Subscript, no key-operand literal
<peer-layer validity/science sink>(_leaked)
```

Why they pass, verified against the bytes:

- **S-25c blind:** none adds an occurrence of `attested_pid`/`attested_pgid`
  (E1/E3 never mention them; E2's identifier is a string literal). Count stays 3.
- **S-25d / ACC-R1 blind:** ACC-R1 governs only an access "whose key operand is
  the string literal" `"controller_pid"`/`"process_group_id"` (v2 line 626-629).
  `.values()`/`.items()` have no key operand; `locals()["attested_pid"]` keys on
  a different string; `claim.controller_pid` is an Attribute with no key operand.
- **S-25f / S-25g blind:** both are "the same syntactic reaching check v1
  already specified" (§2.11) — the v1 X-line's own M-2 finding recorded that such
  a check "catches only the sink shapes it enumerates." A value produced by
  `list(claim.values())[5]`, `locals()[…]`, or `claim.controller_pid` is not a
  whitelisted shape, so neither rule classifies it as restricted.
- **The peer root is not locked down.** The composite bans
  `locals/globals/vars/getattr/setattr/eval/exec/compile/__import__` and the
  builtin `open` only in **"the PCS and role roots"** (S-7, composite line 2581).
  When the framers mean all five roots they say so explicitly — "no production
  root" (S-23, line 2626), "all five roots" (CHANGE 5, line 2638) — so S-7's
  two-root scope is deliberate. `generic_harness.py` has a **17-module import
  allowlist** (§P1-3.2) that S-1's "six/three imports, no ImportFrom" cannot
  describe, so the S-1–S-24 grammar (including S-6's closed call-set and S-7) is
  the process-control-root grammar; the peer root is constrained only by its
  allowlist, S-12 (no process primitives), and CHANGE 4 (no `signal`/`sys`) —
  invariant 80 names no other. The packet's **own A-T9 fixture #5 uses `open()`
  in this scope**, confirming the S-7 lockdown does not reach it. Hence
  `locals`, `vars`, `.values()`, `.items()`, and attribute access are all
  available where the governed code lives.

**Consequence.** The control-plane half of §2.12's amended sentence ("no
control-plane sink"; no `kill`/`killpg`/`waitpid`/request-builder) stays robust —
S-12 independently bars those primitives from `generic_harness.py`. But the
broader half — that the values "remain in a restricted identity class whose
complete consumer set is [C-1..C-4]" with no capacity/custody/selection/Q-C/
scientific sink — is exactly what Y-C1 required and is **not** syntactically
enforced against E1/E2/E3, and those sinks live in the peer layer. So M-2's "no
second sink is a decidable syntactic check" and Y-C1's "every reloaded read
routes to invalidity" are not yet earned.

**Smallest repair (closes both M-2 and Y-C1; no mechanism change; keeps "no
taint"):** add S-25 clauses so that, across every production root the governed
Names/keys span — `generic_harness.py` included:

1. extend S-7's forbidden-name set (`locals, globals, vars, getattr, setattr,
   delattr, eval, exec, compile, __import__, importlib`, and reflective frame
   access) to that scope; and
2. pin the in-memory representation of `t-process-claim.v1` and
   `t-active-lease.v1` objects to a plain mapping, and make `ACC-2`/`ACC-3` the
   **sole** syntactic path by which any value of such a mapping is bound to a
   Name — i.e. forbid `.values()/.items()/.keys()`, `list()/dict()/tuple()/
   set()/sorted()` over such a mapping, `**`-unpacking of it, and attribute
   access to the two keys, outside `ACC-2`/`ACC-3` and the `C-2` whole-mapping
   copy.

With (1)+(2), every read of a restricted value requires either a governed Name
occurrence (caught by S-25c) or a key-literal subscript (caught by S-25d), so the
syntactic closure becomes equivalent to no-second-sink. After this, M-2 and Y-C1
are fully closed and v2 is confirmable.

---

## Determination 1 — finding-by-finding disposition, verified against the bytes

| Finding | Prior class | v2 status | Verification |
|---|---|---|---|
| **X M-1** journal durability asserted, not shown; schema edit missing from blast radius/handoff | Major | **CLOSED** | §2.8.1 withdraws "exactly as `start_identity` already is" verbatim. I confirmed the composite J4 at :1289 records only `{state, outcome, handle_id, fd_vector_len}` and the replay rows :1301/:1303 return only status/detail/handle — so the premise was genuinely unsupported. §2.8.2 amends J4 to the 13-key vector (E-1..E-4); §2.8.3 gives byte-identical replay (R-P1..R-P4, no re-observation, R-P4 cites WAIT_ONE :1566). §5.1/§5.5/§7.1 price the journal format into A's blast radius and withdraw v1's "one sentence and one response grammar." |
| **X M-2** no-second-sink rests on unproven taint | Major | **SUBSTANTIALLY CLOSED — residual** | S-25d withdrawn; occurrence whitelist replaces taint and closes direct-Name laundering (A-T9). Residual reflective/iteration/attribute reads in the unlocked peer root — see determination 2. |
| **X m-1** `getpgid` re-read vs stored `pgid_or_null`, authority unstated | Minor | **CLOSED** | §2.3 A-P4a (fresh read authoritative), A-P4b (stored value mandatory cross-check when non-null → STRUCTURAL_VIOLATION on disagreement), A-P4c (setsid equality mandatory), A-P4d (no other source). Single-valued. The fresh-read choice is an author judgment (closure weakest-point #5) but coherent. |
| **X m-2** 7-digit bound unjustified | Minor | **CLOSED** | §2.2 pins `PID_MAX_LIMIT = 4194304`; G-3 (value ≤ limit), G-5 (8+ digits fail closed), G-6 (7-digit over-limit fail closed), platform premise stated; A-T8. |
| **X m-3** supervisor/watchdog freeze cases conflatable | Minor | **CLOSED** | §6.1 separates Case 1 (supervisor / control-socket EOF / :1781 / recorded) from Case 2 (watchdog / update-pipe EOF / :1464 / unresolved) by actor, trigger, citation, status; states Case 1 is not evidence Case 2 is handled. |
| **Y-C1** sole-sink closure not closed across durable schemas; reload launders | Critical | **SUBSTANTIALLY CLOSED — residual** | §2.4 withdraws the false rule verbatim; §2.6 restricted class + C-1..C-4 (verified: C-2 lease copy per :241-246, C-4 conjunct-7 per :1047, C-3 immutability per :300-305) + P-R5 dominant invalidity + §2.6.4 recomputed readers + §2.6.5 SPAWNING_GROUP.json collision scoped by schema (NC-1..NC-3). The **enumeration** is complete and correct; the **syntactic enforcement** (ACC-R1/S-25d/S-25g) shares the determination-2 gap. The specific reopen-and-rebind fixture the Y line named *is* closed (A-T9 #5 via S-25d); the general "however obtained" (e)-class is not. |
| **Y-C2** replay not constructible from literal J4 | Critical | **CLOSED** | Same repair as M-1; the three bad continuations (absent fields / fresh observation / invented bytes) are excluded by R-P1..R-P4. Verified against :1289/:1301/:1303. |
| **Y-M1** crash table contradicts durable claim; EEXIST no-op accepts false claim | Major | **CLOSED** | §2.10.1 withdraws "PCS death ⇒ no claim" verbatim; §2.10.2 boundary-keyed matrix retains the claim on post-durability PCS death and routes it to signed invalid-process settlement (verified :338-341 "Recovery cannot delete/reuse a claim"); §2.10.3 EEXIST converges only after X-1 bytes / X-2 schema / X-3 cross-field / X-4 hash, else record-first invalidity, occupant never replaced; §2.10.4 binds every identity failure to the dominant surface. A-T11/A-T12. |
| **Y-M2** Option B blast radius overstated; `t-process-record.v1` does not inherit | Major | **CLOSED** | §3.2 withdraws the inheritance claim verbatim. Verified directly: `t-process-record.v1` keys at :248-257 contain **neither** `controller_pid` **nor** `process_group_id`, and carry `process_claim_sha256`. Corrected count "two record schemas superseded, not three." |
| **Y-m1** stale `/proc` rationale broader than source | Minor | **CLOSED** | §1.5 R-4 states the exact scope of the :188 deletion ("of a clean image, of a fresh execve, or of the executor set") and explicitly does not claim it deletes every argv-derived identity use; R-1/R-2/R-3 close the route independently. Verified :188 verbatim. |

---

## Determinations 3–7

**3 — J4 vector + byte-identical replay + the general repair. CONFIRMED.** J4
amended to the complete 13-key operand vector (§2.8.2) with pinned ASCII-token
encoding (E-1..E-4, no re-derivation from ints); COMPLETED/ACKED replay is a
verbatim redelivery with fields 4/7 overridden exactly as :1301/:1303 already
require, and R-P1..R-P4 forbid any re-observation. The **general all-opcode**
"J4 records the complete response operand vector" rule is **coherent** (a strict
superset making each opcode's J4 self-sufficient for replay) and **fully priced**
— it appears in A's blast radius as a durable-format change (§5.1/§5.5, "NEW IN
v2; v1 denied this") and is disclosed as broader than the finding (§2.8.2, closure
weakest-point #1). *Minor, non-blocking:* the generalization does not re-state
replay for the descriptor-bearing opcodes (SPAWN_ROLE/SPAWN_WATCHDOG) to confirm
`fds_redelivered` stays `0` under complete-vector recording; this is consistent
with the unchanged :1301/:1303 no-descriptor rule, but an explicit line would
remove all doubt.

**4 — persistent accessor surface. Design CONFIRMED; enforcement shares the
determination-2 gap.** Schema-scoped key recognition (NC-1..NC-3, decidable via
§P1-13.7 single-site opens) is sound; no declassification on reload is correct as
a *class* definition (§2.6.1(e)); the consumer enumeration C-1..C-4 is **complete
and correct** — I re-ran the key search: `controller_pid`/`process_group_id`
appear only in `t-process-claim.v1` (:231-238) and `t-active-lease.v1` (:241-246);
the SPAWNING_GROUP.json same-name key is the middle's group (:604), correctly
excluded; §2.6.7's disposal of the admission-time membership "fifth consumer" is
sound (group determination is P1's, keyed by handle, SIGNAL_GROUP precondition
:1223). P-R5 gives deterministic dominant invalidity for every other use. What is
**not** airtight is the *syntactic* enforcement of that design — ACC-R1 keys only
on the two string literals and misses iteration/attribute/reflection reads
(determination 2).

**5 — CONFIRMED.** Fresh `getpgid` authority + non-null cross-check + setsid
equality (§2.3 A-P4a..d); `PID_MAX_LIMIT` pinned with fail-closed G-5/G-6 (§2.2);
EEXIST canonical-identity convergence X-1..X-4 (§2.10.3); post-claim PCS-death
retains the claim and routes to signed invalid settlement (§2.10.2, verified
:338-341); corrected `/proc` rationale (§1.5, verified :188). All hold on the
bytes.

**6 — CONFIRMED.** Recomputed A/B blast radius (§3.2, §5.5): `t-process-record.v1`
does **not** inherit the fields (verified :248-257, carries `process_claim_sha256`)
and is removed from B's count; corrected count is two superseded schemas, not
three/four. **Option B remains non-selectable for authority reasons, not size:**
§3.3 states this in terms — B-1 (PCS gains a fifth peer-visible durable-write
class) and B-2 (a peer predicate opening a P1-owned artifact inverts R-L4,
:2022-2027) are authority gaps "unchanged by the corrected blast radius." A's own
larger-than-v1 surface is disclosed (§7.1 "What the correction did cost A").

**7 — CONFIRMED.** Neither option repairs or silently conditions
`AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM` (§6.2): A attests to the supervisor,
dead at watchdog-freeze time with no channel to the watchdog; B supplies the
watchdog no mechanism; "selecting A or B neither fixes nor worsens it." The cell
is quarantined, not opened. No hidden dependency runs the other way either.

---

## Authorization

Because the verdict is `REVISE`, this round authorizes **nothing** — not
selection, not the `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` token, not
implementation, not activation. The single residual defect (determination 2 /
X M-2 / Y-C1) has a concrete, bounded repair stated above; after it lands and a
subsequent bounded X/Y confirmation round confirms the repaired bytes, v2 should
be confirmable, at which point confirmation would authorize **only Kirill's
informed A/B selection** (and, conditional on A, the bounded-weakening token) —
never implementation or activation.

Preserved: `T = NOT_ACTIVATED`; programme claim `OPEN`; no selection; no process
control; no spend, datum, or outcome; no watchdog repair; no implementation
authority. No existing file was modified in producing this review; its sole
product is this file.
