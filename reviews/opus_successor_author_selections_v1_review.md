# Opus 4.8 X-line — successor author selections v1 review

**`SUCCESSOR_AUTHOR_SELECTIONS_V1_XLINE_CONFIRMED`**

Reviewer: Opus 4.8 (X-line, bounded review of Kirill's provisional A1–A5
selections — not a charter/implementation/population/Q-numeric/spec reopening).
Repository: `/home/master/llm_projects/philosophia`, commit `42a0c8c`. **I changed
no existing file, chose no alternative for Kirill, and ran nothing (no code,
entropy, world, model, T, Q, lock, escrow, or outcome). `essay/OUTLINE.md`
untouched. Nothing committed.** The charter (v2 + v2.1) is signed
(`CHARTER_SIGNATURE.md`); these selections instantiate its author cells and move
no scientific claim.

Every provisional selection is internally consistent with the signed charter,
single-valued at policy level, and derives from no stopped-line efficacy record.
No Critical or Major defect. What remains is a set of **WP-1/WP-2/WP-4/WP-6
implementation-and-test obligations** (not signature blockers) plus three Minor
record clarifications. The choices survive; Kirill may sign the consolidated
packet.

---

## 1. Findings

### Critical / Major
None. A1–A5 select recommended, charter-consistent options; each has an
executable, non-gameable realization; no scientific, statistical, terminal, or
authorization contract changed.

### Minor (record clarifications; none blocks signature)
- **M-1 — A4 token string is a custom label.** The packet's A4 tokens were
  `I_COMMIT_T_ENVELOPE_{MINIMAL,STANDARD,EXTENDED}`; Kirill signed a custom
  `I_SELECT_T_ENVELOPE_ONE_WEEK` (E1=168 h, E2=12, E3=48 wall / 40 device). This
  is legitimate — the packet states "every number is an author resource
  commitment … profiles are offers, not derivations" — and the **values are
  single-valued**. Reconcile in the final record by keeping the custom token
  explicitly bound to its E1/E2/E3 values (as the provisional record already
  does), so the token names a complete commitment rather than one of the three
  profiles it does not match.
- **M-2 — E3 "wall-hours" is calendar-vs-active-ambiguous.** "48 elapsed
  wall-hours after T-envelope activation" does not say whether power-off
  intervals count. Recommend pinning **elapsed calendar time (inclusive of any
  power-off interval)** at the WP-4 contract, which aligns with the 96-hour
  power-off (a review checkpoint then falls on a predictable calendar cadence
  across power cycles). Either reading is safe — a checkpoint is a review point,
  not a terminal — so this is a WP-4 clarification, not a blocker.
- **M-3 — the power-off/resume discipline should be named in the final record.**
  Add one line binding the operational constraint (below) as a WP-2/WP-4
  obligation, so a planned power-off is unambiguously a process pause, never a
  terminal.

---

## 2. Answers to the five required checks

### Check 1 — same-repo quarantine (A1 layout): ACHIEVABLE, mechanically.
Same-repo places the stopped-line trees in the same working copy as
`successor/officina/`, so the quarantine cannot be conventional — it must be a
**fail-closed path-allowlist** in every successor driver, resolving `realpath`
before checking, defaulting to **deny**. It is achievable: successor drivers open
files only through an allowlist wrapper that permits `successor/officina/**`
(read/write) and a small set of **declared, read-only, T-context-only
`engineering-fixture`** paths, and refuses everything else — while the
hash-pinned audit ancestry is preserved by git (the predecessor is an immutable
ancestor commit; ancestry is audit metadata, never a runtime content read).

The harder half — preventing fixture data from reaching Q/C and blocking
warm-starts — spans **WP-1 (path allowlist)** and **WP-2 (governance-library
dataflow tagging: fixture-derived data is `non-promotable`)**.

**Minimum tests WP-1/WP-2 must later satisfy (state only; do not implement):**
- *Positive:* (P1) read/write of any `successor/officina/**` path succeeds; (P2)
  a T-context read of a declared engineering-fixture returns data tagged
  `engineering-fixture`/`non-promotable`; (P3) git-ancestry/lineage audit resolves
  with **no** runtime read of stopped-line content; (P4) append to
  `successor/officina/T_LEDGER.md` succeeds.
- *Negative (must fail-closed / raise):* (N1) any read of an undeclared
  stopped-line path (`experiments/level_0_grokking/**`,
  `experiments/level_1_contact/**`, feasibility artifacts); (N2) use of any
  stopped-line stream (public-root transcript / derived) **as randomness**
  anywhere; (N3) a **Q- or C-context** read of any engineering-fixture (fixtures
  are T-only); (N4) warm-start of a successor learner from a v1/v2 checkpoint;
  (N5) an `engineering-fixture`-tagged datum reaching a Q or C surface; (N6)
  path-traversal/symlink escape (`successor/officina/../../experiments/…`)
  normalized and denied; (N7) an undeclared path denied by the default (fail-closed).

WP-1/WP-2 themselves touch **no real world** (dummy seeds + allowlist), so the
same-repo choice adds no reuse risk during the authorized work; the
fixture/warm-start surfaces arise only at WP-3+/WP-5+, behind these tests.

### Check 2 — Q positive path (A3 sealed post-freeze root): ONE executable, non-gameable path.
The policy skeleton leaves exactly one WP-6 realization: (1) candidate manifest +
attempt claim become durable; (2) the reviewed driver draws the OS-CSPRNG root
once — **the first entropy byte is the launch instant**, and from it the attempt
is charged (id, cap slot, α) even if it later invalidates; (3) Q worlds derive
from the sealed root; qualification yields `Q_VALID_PASS/FAIL` or
`Q_INVALID:<cause>` (charged); (4) no redraw — recovery is only a **new charged
attempt**, or, if failure preceded entropy, a **signed pre-attempt disposition**
with no charge and no silent retry.

Non-gameable on every axis: a pre-entropy abort gains **no** information (the
worlds do not exist until launch) and cannot be silently spammed (recovery needs
a signed disposition); redraw is forbidden (post-entropy failure charges);
mechanism/custody substitution is forbidden except by a signed pre-attempt
amendment permitted only when no launch is pending (so it cannot react to an
unfavorable draw); a standing fallback mechanism is forbidden (exactly one signed
mechanism). This **locates the charter's existing every-launch rule at a precise
instant** and adds no new charging law.

**WP-6 obligations (test, not now):** the launch-charge must be durably recorded
**atomically with / before** the first entropy byte, so no entropy can exist
without a durable charge; the **pre-entropy pending-claim** must be a distinct,
durably-recorded status resolved only by signed disposition (never an automatic
charge, never a silent reuse), so "no charge before entropy" cannot be exploited
to accumulate silent pending attempts.

### Check 3 — T envelope (A4): single-valued; power-off is a WP-2/WP-4 obligation, not a terminal.
E1=168 aggregate device-hours, E2=12 canonical candidates, E3=`min(48 wall,
40 device)` are numerically single-valued, and the attacks resolve at policy
level (enforcement is WP-2/WP-4):
- *Parallel accounting:* "concurrent real-T processes consume hours additively"
  — device-hour = Σ over processes of active training time on real T worlds;
  single-valued (WP-4 must pin "active" precisely: e.g., allocated-and-running,
  excluding idle/paused).
- *Restart/accounting gaps:* the append-only public ledger
  (`successor/officina/T_LEDGER.md`) is the durable record; resume reads
  accumulated E1/E2 from it and **never resets** — a WP-2/WP-4 durable-resume,
  no-double-count, no-off-time-accrual obligation.
- *Dummy-to-real promotion:* the boundary keys on touching a **real T world**
  (real-T-partition, real dev-root), not on a label; WP-2/WP-4 must make it
  mechanically true that any run reading/generating a real-T world charges E1 and
  test-only-seed worlds cannot exist in the T partition.
- *Ledger omission:* fail-closed — the T driver must durably write the E1/E2
  ledger entry **before** training on a real T world (claim-before-run analog),
  so no real run escapes accounting (WP-4).
- *Checkpoint reset:* each checkpoint resets both counters and re-applies
  `min(48 wall, 40 device)` — single-valued, modulo M-2's calendar-vs-active
  pinning.
- *Behavior-inert vs effective change:* decidable at the registry from the
  canonical manifest **iff** canonicalization is a **conservative whitelist
  normalization** (strip the declared inert set — names, comments, packaging,
  timestamps, serialization order — via AST/config normalization; anything
  outside it counts as behavior-relevant → new candidate → E2 slot). The
  fail-safe direction is correct (unknown ⇒ new candidate ⇒ charge; it can
  overcharge a slot but never undercharge). WP-1/WP-2 own the normalizer.
- *Author-stop/exhaustion:* clean and distinct — `T_ENVELOPE_EXHAUSTED` fires
  **mechanically** at E1 or E2; `T_AUTHOR_STOP` is a **distinct signed** decision
  at a checkpoint; separate ledger records.

**Operational power-off (96 wall-hours):** confirmed consistent. E1 is a
**cumulative** envelope, explicitly "not a continuous-run promise or deadline,"
so 168 device-hours may span multiple ≤96-hour power sessions. A planned power-off
is a **process pause**, owned by **WP-2/WP-4**: it (a) occurs only after a durable
T checkpoint + ledger flush, (b) records **neither** `T_AUTHOR_STOP` **nor**
`T_ENVELOPE_EXHAUSTED`, (c) does **not** erase E1/E2 consumption (durable ledger),
and (d) permits resume from the durable T state. It creates **no new scientific
terminal** — the §8 taxonomy is untouched; the pause is invisible between ledger
entries. Because **no real T run is authorized before this review or expected
before the shutdown**, and WP-1/WP-2 touch no real world, no live T state is at
risk during the authorized work; the discipline binds WP-2/WP-4 before the first
real T run (WP-5+).

### Check 4 — device positive path (A5 off-CPU + breathing check): achievable, no Level 0 pretense; ownership exact.
Off-CPU T development is permitted; before a candidate on an off-CPU **stack
family** may register for Q, that family must pass a **bounded, deterministic,
non-citable breathing check** under a later reviewed WP-2/WP-6 contract, and
"Level 0's CPU result does not transfer." No pretense: the breathing check
**re-earns** engineering platform assurance where Level 0 does not reach; it is
never citable and never a Level 0 transfer. Ownership is exact at policy level —
**property** (bounded/deterministic/non-citable breathing check), **timing**
(before the family's first Q registration), **owner** (WP-2/WP-6), and
**non-citability** are all fixed; only the numerics (tolerance, reproducibility
criterion, precise "stack family" definition) are deferred. Because the check is
non-citable, single-stack (no arms), deterministic, and a **gate before**
candidate-blind Q numerics are even set, it **cannot become a selection channel**
into Q/C — WP-2/WP-6 must preserve that (the check's outputs never feed competence
numerics). It pays platform risk in **uncharged T** rather than **capped, α-charged
Q**, which is the correct placement under unified charging.

### Check 5 — authorization boundary: YES, Kirill may sign the packet + the WP gate.
The earlier bare `I_AUTHORIZE_SUCCESSOR_WP1_WP2_IMPLEMENTATION` is correctly
recorded as **not effective** (it missed the review precondition). With the
selections confirmed here (and pending Sol's parallel confirmation), Kirill may
sign the **complete selection packet together with the WP gate in one final
author record**, and that token authorizes **only WP-1 and WP-2 code and tests** —
namespace/manifests/quarantine allowlist/T-ledger skeleton (WP-1) and the tested
governance library with dummy-seed fail-closed fixtures (WP-2), **including the
Check-1/Check-2 test obligations** — and **no real world, entropy, candidate, T
run, Q attempt, promotion, spec, lock, escrow, C, or outcome**. WP-3 (population
contract) and every later WP retain their own draft, review, signature, and
authorization.

---

## 3. Signature-blockers vs later WP obligations

**Repairs required before author signature:** none. (M-1/M-2/M-3 are record
clarifications; the values and policies are already single-valued.)

**Owned by later WP-1/WP-2/WP-4/WP-6 implementation + tests** (enumerated above,
to be reproduced in their contracts, not now): the path-allowlist positive/negative
test set (P1–P4, N1–N7) and fixture `non-promotable` dataflow tagging; the atomic
launch-charge + pre-entropy-pending-claim handling; the precise "active
device-hour" definition, durable-resume no-double-count/no-off-time-accrual, the
mechanical real-vs-dummy world boundary, and fail-closed ledger-before-real-run;
the conservative canonical-manifest normalizer; and the breathing-check
tolerance/reproducibility/"stack family" definition with its non-selection-channel
guarantee.

---

## 4. Exact final packet Kirill may sign

Verbatim, with the values bound (M-1: the A4 token is the custom one-week
commitment; M-3: the power-off line added):

```text
SUCCESSOR AUTHOR SELECTIONS — signed by Kirill Kruglov on [date]
Base: CHARTER_SIGNATURE.md (v2 + v2.1), commit [hash]

A1 name:    I_NAME_SUCCESSOR_LINE_OFFICINA
A1 layout:  I_SELECT_SUCCESSOR_LAYOUT_SAME_REPO
A2:         I_SELECT_C_INTERPRETATION_FINITE_FRAME_SAMPLE
A3:         I_SELECT_Q_ENTROPY_SEALED_POSTFREEZE_ROOT
A4:         I_SELECT_T_ENVELOPE_ONE_WEEK
            E1 = 168 device-hours   E2 = 12 canonical candidates
            E3 = 48 wall-hours or 40 device-hours, whichever first
            ledger = successor/officina/T_LEDGER.md (append-only, public)
A5:         I_SELECT_DEVICE_POLICY_OFFCPU_WITH_BREATHING_CHECK
Power-off:  a planned host power-off is a WP-2/WP-4 process pause — durable
            T checkpoint + ledger flush first; not T_AUTHOR_STOP; not
            T_ENVELOPE_EXHAUSTED; E1/E2 consumption preserved; resume from
            durable T state
WP gate:    I_AUTHORIZE_SUCCESSOR_WP1_WP2_IMPLEMENTATION
```

**This packet authorizes:** WP-1 (lineage bootstrap: `successor/officina`
namespace, manifests, fail-closed quarantine path-allowlist, empty T-ledger
skeleton) and WP-2 (governance-library implementation + tests: validity-first
taxonomy, one-shot atomic drivers, PRF/serialization/escrow machinery,
dummy-seed fail-closed fixtures, and the Check-1/Check-2 test obligations) — code
and tests only.

**It does not authorize:** any real T world or dev-root entropy; any candidate
registration, T training run, or E1/E2 consumption; any Q attempt, promotion,
scout/S surface, scientific specification, preregistration lock, C-root/escrow, C
execution, outcome, or claim transition; the WP-3 population contract; any device
stack, Q numeric, C interpretation value, or final public/essay name. Each later
WP keeps its own specification, bounded review, signature, and authorization.

## 5. Negative space and confirmation

The five Route B tokens and the three charter tokens remain exact and are not
re-signed here. The predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; its C1 unrun and untested; v1/v2 non-comparable,
non-citable, and choosing nothing in these selections. T and Q can never earn,
kill, or boundary-label C1–C6; S is unavailable; only a valid, independently
locked C execution may move a successor claim, within its selection-conditional
scope. "No qualifier," censored, `UNKNOWN`, and every invalid state are never
success, equivalence, a boundary, or evidence that no competent learner exists.
Implementation promises no qualifier, no C run, and no Proof; the strongest
in-charter endpoint is a reviewed one-shot C package awaiting separate author
authorization. `PROOF_CORE`/`PROOF_STRONG` remain earned by nothing; the programme
claim stays `OPEN`.

I changed no existing file, created exactly one new file (this review), chose no
alternative for Kirill, and committed nothing. No code, entropy, world, model, T,
Q, lock, escrow, or outcome was created or run; no series inspected; no arms
compared; no v1/v2 contrast formed; no open cell was selected by me. My only
actions were reading the governing chain and reasoning about the provisional
selections and the operational power-off constraint.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
