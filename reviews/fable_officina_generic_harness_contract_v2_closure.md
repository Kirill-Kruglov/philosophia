READY_FOR_OFFICINA_GENERIC_HARNESS_V2_CONFIRMATION

# Fable 5 — Officina generic harness contract v2 closure memo

Author: Fable 5. Companion to
`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md` (complete
self-contained replacement; v1, its closure, both formal reviews, and
all chat captures preserved unedited). Inputs: Opus
(`REVISE…_XLINE`, C-1..C-4, R5..R12 with exact §D text) and Sol
(`REVISE…_YLINE`, mandatory repairs 1..14). Exactly two files created;
nothing else changed; nothing committed or run beyond reading. The C4
namespace repair at `38ea2f3` was treated as engineering context only;
no manifest pinned, no T activated.

## 2. One-to-one disposition table

| Finding | Disposition | v2 |
|---|---|---|
| **Opus C-1 / Sol 6** — event-before-record inversion in valid close | **Adopted (R1 text in substance verbatim)**: charge → durable final record → `T_PROCESS_STOPPED` hashing that record; non-finiteness closes by this route | §2c.6–7 |
| **Opus C-2 / Sol 6** — missing INVALID process record; process vs global invalidity conflated | **Adopted (R2)**: 12 (live-process, full artifact chain incl. INVALID record bound to the event), 12a (no-process global fault creates no process record), 12b (siblings) | §2c.12 |
| **Opus C-3 / Sol 1** — flat recovery charge silently replaced signed v2.1 §1 | **Adopted (R3/Sol-1)**: three-case rule restored verbatim in substance; every "outstanding liability is the charge" sentence deleted; reservation = ceiling and deadline only; floor = never zero | §4c |
| **Opus C-4 / Sol 14** — roots/CLI contradict pinned verifier | **Adopted (R4)**: roots = exact pinned tuple; `generic_harness.py.__main__` is the CLI via `python -m`; `scripts/officina_t_process.py` deleted from the contract | §9, §11 |
| **Opus R5 / Sol 14** — cache-cut self-contradiction | **Adopted**: §3a sole idempotent completion = the cache/lease successor one event behind a consistent ledger+head, same lock epoch; every other mismatch (incl. ledger-ahead-of-head) record-first | §3, §3a |
| **Opus R6 / Sol 6** — G5 siblings left running | **Adopted**: 12b revoke/settle/invalid-close every live sibling; no admission during the batch | §2c.12b, §4d |
| **Opus R7 / Sol 5** — unpinned initial prior-charge hash | **Adopted**: seeded to the `T_PROCESS_STARTED` entry hash; per-settlement successor relation pinned; no cyclic hash | §2c.3, §2c.5 |
| **Opus R8 / Sol 3** — exhaustion vs reservation refusal | **Adopted**: event only at realized ≥ 168 h; sibling-caused `ℓ=0` refuses + recomputes, appends nothing | §2c.8, §4b |
| **Opus R9 / Sol 12** — draft manifest "order-free" false | **Adopted, stricter branch**: `created_utc` and the lineage tuple **removed** (see strictness table) | §8 |
| **Opus R10 / Sol 10** — adapters must be static | **Adopted**: statically imported reviewed modules; reflective discovery forbidden | §4f |
| **Opus R11** — import allowlist commitments | **Adopted**: CPU-only implementability list; cross-module import of `generic_harness` and any backend import = future reviewed amendments | §9 |
| **Opus R12** — ownership/durable-path/fake-type pins | **Adopted verbatim in substance** | §1 |
| **Sol 2** — global conserving settlement | **Adopted verbatim in substance**: batch algorithm, `D0/K/R`, single pool, `(process_sequence, stream_index)` order, `floor(R/m)` + remainder-ns, zero-additional-debit rule, positive-charge-events-only | §4d |
| **Sol 3** — multi-stream reservation arithmetic | **Adopted**: `ℓ = min(60 s, floor(E1_avail/k), floor(E3_avail/k))`, aggregate `k·ℓ`, shortened deadlines | §4b |
| **Sol 4** — boundary batch + dominance | **Adopted**: fixed order E1 > E3 > author stop > pause > close; invalidity dominates all valid endings; invalid-cause precedence fixed (see strictness table); every pair tested | §2a, §4d, §10 |
| **Sol 5** — hash relation + conservation equations | **Adopted**: pre-settlement lease hash; sole-increment rule; final record includes final event; rest-state equalities | §2c.5, §4e |
| **Sol 7** — durable resume + recovery without a tenth event | **Adopted verbatim in substance**: recovery-disposition artifact (v2 §F facts only, fixed action token, fresh ids); overdue resume = second `T_OPERATIONAL_PAUSE` with `RESUME_E3_REVIEW_PENDING`, `resets_e3:false`, durable post-state | §6b, §6c |
| **Sol 8** — physical pause fail-closed at every cut | **Adopted**: full condition list; power loss before any condition routes to invalidity/signed disposition; changed-vs-missing boot id split; per-cut tests | §6a, §10 |
| **Sol 9** — isolation-and-promotion replaces response wrapper | **Adopted verbatim in substance**: worker isolation of memory/IPC/FDs/temp/output; revoke→quiesce→sync→hash→charge→atomic promote→one-use token; invalid/escaped work exposes no result | §5b |
| **Sol 10** — CPU vs off-CPU meter semantics | **Adopted**: elapsed-wall vs submission-to-proven-completion; queued-not-free; unmeasurable → unknowable case | §4f |
| **Sol 11** — closed non-outcome inputs; honest author stop | **Adopted**: closed input schemas; recursive rejection; author stop honestly may be T-informed, quarantined, never Q/C evidence or scientific destination | §7 |
| **Sol 12** — pre-WP-6 channels | **Adopted, stricter branch**: timestamps and ordered lineage removed; whole-artifact Q/C rejection; opaque recomputed digest only; release tokens barred from candidate/Q/`H_preC`/`selection_scope_id`/C; labels only on separately closed dev schemas (signed runtime schemas keep only signed keys) | §8 |
| **Sol 13** — WP-6/WP-9 ownership | **Adopted verbatim in substance**: draft manifest non-normative; hooks confer no authority; WP-6 may replace the surface / require reviewed core change; WP-9 owns science | §8 |
| **Sol 14** — reconcile recovery/roots/tests | **Adopted**: distributed to §3a, §9, §10 | — |

Nothing dropped; every repair is a rule, ordering, formula, schema, or
test row — no prose-only resolution.

## 3. Strictness/conflict table

| Overlap | X-line | Y-line | Resolution |
|---|---|---|---|
| Recovery charge | R3 three-case rule | 1 (same) + 2 (global pool) | identical rules; **both adopted** — three-case per stream, single conserving pool for unknowables |
| Draft manifest ordering channels | R9: delete `created_utc` **or** keep as provenance-only | 12: remove, or never-read; lineage exception removed | **stricter branch: removal** of both `created_utc` and the lineage tuple; lineage lives only in quarantined dev schemas |
| Invalid-cause precedence | not specified | 4: one fixed precedence required | **named deterministic resolution** (no author choice invented): `HASH > FILESYSTEM > CLOCK > PROCESS > RESOURCE` — integrity-first ordering justified against the signed protocol's fail-closed posture (the least recoverable, most evidence-destroying cause names the public event; the detail record lists every observed cause). Any equally fixed order would serialize; this one is now normative |
| Silent completion scope | R5: cache row (after 5→6) only; v1's head-behind row = signed recovery | 14: "interrupted, fully derivable cache/lease successor" | **stricter intersection**: §3a covers the cache/lease successor only; ledger-ahead-of-head remains record-first with head repair only under the signed disposition |
| Roots/CLI | R4 pinned tuple + `__main__` | 14 (same) | identical; adopted |
| Author-stop neutrality | (not raised) | 11: cannot claim outcome-independence | Sol's honest wording adopted; mechanical closure limited to infrastructure inputs |

No literal conflict between the two reviews survived analysis; the two
"or" branches (R9, R5-scope) were resolved to the stricter member, and
the one underdetermined cell (cause precedence) was fixed
deterministically rather than delegated.

## 4. Totality summary

Global: eight states G0–G7 with a fixed dominance order for fault-free
compounds, invalidity dominating every valid ending, and E1/E3
simultaneity resolved (exhaustion once, E3-due retained). Process:
P0→P1→P2→P3→{P4,P5} with exactly one artifact/event order per exit —
valid close (charge → record → stopped), invalid close (settlement →
detail record → event → INVALID record), no-process global fault (no
process record). Every §3 crash cut has one legal action; the sole
silent action is the §3a cache/lease successor; pause has a fail-closed
route at every condition; overdue resume is a durable second-pause
entry; G5 exit requires exactly one verified signed disposition per
invalidity. No tenth event, no automatic retry, no liability erasure,
no invalid→valid relabelling exists anywhere in the machine.

## 5. Accounting invariants and worked examples

Invariants (§4e): global E1 = Σ per-process cumulative charges; live
aggregate liability = Σ installed-lease liabilities; every charge event
has `charge_ns > 0` and increments exactly one lease and the global
state.

**Example A (concurrent, all known, no crossing).** Cap 604,800
device-s; `D0 = 100,000 s`. Stream A (1 unit) timely-quiesced at +42 s
→ case (a), charge 42 s (≤ 60 reservation). Stream B late-known at
+95 s → case (b), charge 95 s in full (> reservation, no clipping).
`K = 137 s`; no unknowable stream, pool untouched. Post-total
100,137 s; invariants hold; both close per their routes.

**Example B (unknowable batch with crossing).** `D0 = 604,700 s`
(100 s remaining). Three streams: A timely at +40 s → `K = 40`.
`R = max(0, 604,800 − 604,740) = 60 s`. B and C unknowable, `m = 2`:
each `floor(60e9/2) = 30e9 ns`; remainder 0. Post-total exactly
604,800 s → the batch appends `T_ENVELOPE_EXHAUSTED` once (realized
cap reached); **B and C still close as `T_PROCESS_INVALID`** —
invalidity dominates; exhaustion is a retained resource fact, not
their ending. The pool debited once, not once per lease: without Sol-2
the naive rule would have charged 60 s twice (120 s > remaining 100 s)
or, worse, "all remaining E1" twice.

**Example C (zero share after prior crossing).** A's case-(b) charge
of 95 s crossed the cap (`D0 + 95 > cap`, retained in full). A later
unknowable stream finds `R = 0`: zero *additional* debit, recorded as
such — never evidence of zero work, never a valid close; its ending
remains invalid with liability facts preserved in its records.

## 6. Production surface and handoff

Roots exactly `scripts/officina_activate_t.py`,
`scripts/verify_officina_active.py`,
`src/philosophia/officina/generic_harness.py` (CLI = `__main__`, via
`python -m philosophia.officina.generic_harness`; no
`scripts/officina_t_process.py`). Sole issuance and sole writers pinned
in §1; runtime schemas keep only signed keys; dev artifacts get their
own closed quarantined schemas; the production manifest remains absent
until implementation review. Cursor implements `generic_harness.py` and
its test file mechanically from the contract; Codex integrates and
reviews conformance; Opus/Sol confirm; Kirill signs. Cursor has no
authority over constants, schemas, entry points, imports, refusals, or
activation.

## 7. Compatibility classification and tokens

Every v2 clause classifies as **inherited signed rule** (constants,
events, schemas, three-case charge, lock/archival discipline, E2
barrier, T bands) or **deterministic clarification necessary to
implement it** (state machine, cut table, batch algorithm arithmetic,
hash seeding, isolation protocol, pause conditions, resume second-pause
entry, recovery-disposition artifact, cause precedence, draft-manifest
key set). **No protocol amendment is proposed**; the completed table
supports the claim because the two v1 silent amendments (flat charge;
extra CLI root) are repaired *back to* the signed v2.1 rule and the
pinned verifier tuple — repair toward signed text is not an amendment.
Genuinely future amendments, named and not taken: off-CPU adapter
admission, any allowlist expansion, any new entry point. **No author
token is required beyond the eventual
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`;** no author choice was
invented to avoid reconciliation.

## 8. Bounded yes/no confirmation questions

**Opus (three):**
1. Do §2c.6/12/12a/12b and §3–§3a close C-1, C-2, R5, and R6 exactly —
   record-before-event everywhere, distinct invalidity cases, siblings
   settled, and the sole silent completion bounded to the cache/lease
   successor?
2. Do §9/§11 now match the pinned immutable-control verifier
   byte-for-byte in intent — roots tuple, `__main__` CLI, no new entry
   point, static adapters, allowlist commitments — with every future
   amendment named rather than implied (C-4, R10–R12)?
3. Given §4b–§4d, is the no-amendment classification of §7 of this
   memo now correct (C-3 repaired back to v2.1, not around it)?

**Sol (three):**
1. Do §4c–§4e implement your repairs 1–5 exactly — three-case charge,
   single conserving pool with the stated allocation, multi-stream
   reservation, dominance batch, hash relation, and rest-state
   conservation — such that the worked examples A–C are forced, not
   merely permitted?
2. Do §5b, §6, and §7 implement repairs 7–11 — isolation-and-promotion
   with no result exposure on any invalid path, fail-closed pause at
   every cut, the durable second-pause overdue-resume, the closed
   recovery disposition, closed non-outcome inputs, and the honest
   author-stop statement?
3. Does §8 close repairs 12–13 — no pre-WP-6 ordering/evidence channel
   (timestamps and lineage removed, whole-artifact rejection, opaque
   recomputed digest only, release tokens barred), with WP-6/WP-9
   ownership explicit and unconstrained?

## 9. Negative authorization surface and confirmation

This contract and memo authorize only: one bounded Opus/Sol
confirmation of these repairs, then Kirill's contract signature; after
signature, §11 implementation and its bounded review. Created here:
exactly the two mandated files. Not created, not run, not authorized:
`generic_harness.py` or any code; any CLI; `runtime_control/` or any
production call-graph manifest; any activation authorization or
activation; any capability, world, learner, process, lease; entropy;
any draft-manifest instance; E1/E2/E3 spend; any T/Q/C datum, ledger
event, root, lock, escrow, outcome, or claim movement. No
implementation hash, reviewed HEAD, or production source set was
pinned (the `2277331`/`38ea2f3` confirmations proceed in parallel). No
learner, architecture, optimizer, training rule, certificate numeric,
Q predicate, alpha, margin, candidate, device winner, or scientific
endpoint was selected. T remains `NOT_ACTIVATED` at genesis; the
predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain permanently non-citable
for C1–C6; `Q_CAP_EXHAUSTED_NO_QUALIFIER`, invalidity, author stop,
and E1 exhaustion remain non-scientific destinations; no prediction is
made about any learner or about Philosophia being proved, falsified,
or bounded. The intended next step is one bounded confirmation, not a
design round: two independent implementers can now derive identical
classifications, charges, durable orderings, and admission decisions
from the contract alone.
