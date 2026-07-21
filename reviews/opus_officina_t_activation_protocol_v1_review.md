# Opus 4.8 X-line — Officina T activation protocol v1 review

**`REVISE_OFFICINA_T_ACTIVATION_PROTOCOL`**

Reviewer: Opus 4.8 (X-line, adversarial transaction/runtime stance). Repository:
`/home/master/llm_projects/philosophia`. **I implemented and invoked no
activation; created no authorization record, runtime artifact, real world, process
lease, candidate, entropy, Q/C object, datum, or outcome. T remains pristine and
`NOT_ACTIVATED` (`T_ENVELOPE.json activated:false`, ledger at genesis). Nothing
committed; no existing file edited.** I verified the governing pins and read the
draft adversarially.

The protocol is well-structured and sound in principle — claim-before-effect,
capability-only-after-commit, typed process-invalidity with no auto-retry/rollback/
deletion, signed bounded recovery, overshoot retention, the WP-6/E2 boundary, and
the four non-collapsing boundaries are all correct, and all six §1 governing-pin
hashes match the committed files. But three **Major** specification gaps leave two
independent implementers building different state machines (the git-durability/
clean-HEAD model, the runtime lock scope, and the state-bearing event set), plus
several Minor pins. It authorizes nothing and prematurely chooses no WP-6 numeric,
but it is not yet an unambiguous, byte-reproducible contract.

---

## Findings

### Critical
None. No forbidden inference; no authorization; the four boundaries (§2) hold and
scientific evidence is confined to a locked C run.

### Major

- **P-1 — the durability/commit model for *metering* vs *activation* is
  inconsistent, and it collides with the "clean HEAD" capability precondition
  (§5.7 vs §6 vs §7).** §5.7 makes activation a **git commit** of
  {claim, state, record, envelope, ledger, head}; §6 requires capability issuance
  only "at the current clean HEAD"; but §7 metering **appends the ledger and
  replaces `T_STATE.json` without a commit**, so after the first charge the tracked
  worktree is dirty and the next lease's "clean HEAD" precondition cannot hold. Two
  implementers diverge — a git commit per heartbeat (clean-HEAD-preserving, very
  heavy) vs a working-tree-durable dirty tree (violating §6 as written).
  **Bounded repair:** state the durability model explicitly — metering events are
  **working-tree-durable** (fsync file + parent dir) and committed only at defined
  checkpoints (lease close, E3 review, pause, author stop, exhaustion), and scope
  the §6 "clean HEAD" invariant to **the non-runtime tracked tree**, with the
  actively-metered runtime files (`T_STATE.json`, the ledger + head, the lease
  files) explicitly exempt while their process holds the runtime lock. Fix the
  commit cadence and the exact staged-path set for each committing step.

- **P-2 — the "exclusive runtime lock" mechanism and scope are unspecified
  (§5, §7.2/6).** "An exclusive lock on the resolved canonical runtime directory"
  has no portable meaning; concurrent additive E1 correctness depends on it.
  **Bounded repair:** name a dedicated lock file
  (`successor/officina/runtime/T_RUNTIME.lock`), require `flock(LOCK_EX)` on a
  descriptor opened `O_NOFOLLOW`, held across the **entire** read-verify-append-
  replace of every state-mutating transaction (activation, charge, review, pause,
  author-stop, process start/stop), and state that all metering/state reads and
  writes occur only under it.

- **P-3 — the set of "state-bearing" ledger events is not enumerated (§4).** §4
  says runtime state is "a checked cache of the last state-bearing ledger event"
  that "never … contradict[s] or truncate[s] the ledger," but which events carry a
  full post-`t_state` is never fixed. Reconciliation (cache == last state-bearing
  event) is then implementer-defined. **Bounded repair:** enumerate exactly which
  events are state-bearing (e.g., `T_ACTIVATED`, `T_DEVICE_TIME_CHARGED`,
  `T_REVIEW_COMPLETED`, `T_OPERATIONAL_PAUSE`, `T_PROCESS_STOPPED`,
  `T_AUTHOR_STOP`, `T_ENVELOPE_EXHAUSTED`) and specify that the cache must equal the
  last one, and that non-state-bearing events (e.g. `T_PROCESS_STARTED` if it
  carries no state) never advance the cache.

### Minor

- **P-4 — runtime artifacts should carry the WP-4 descriptor-anchor discipline.**
  The just-confirmed WP-4 lesson is that ledger/state integrity needs **held-fd
  `samestat` anchoring**, not pathname-stat. The protocol relies on "hash-linked"
  + the runtime lock; it should additionally require the WP-4 `_open_anchor`/
  `_anchor_matches` pattern (and `AppendOnlyLedger.append(expected_file_descriptor=…)`)
  for the runtime ledger, head, and state so a mid-transaction inode substitution
  is rejected before mutation.

- **P-5 — pin the metering clock source (§7.5).** "A monotonic clock that excludes
  powered-off intervals" and "non-monotone clock → invalid" must name the exact
  source (e.g. `time.monotonic()`/`CLOCK_MONOTONIC`, which excludes suspend on
  Linux, contrasted with `CLOCK_BOOTTIME`) so two implementers meter identically,
  and state explicitly that a lease **cannot span a power-off** (a power-off
  orphans the lease → `T_RUNTIME_INVALID:PROCESS` → signed recovery), which the
  design already implies via §8's zero-active-leases pause requirement.

- **P-6 — name the activated-envelope schema and the verifier transition
  (§5.5).** "A new explicit schema" is unnamed; give it (e.g.
  `philosophia.officina.t-envelope-active.v1`). State that activation **supersedes
  the inactive `verify_officina_wp12`** for the committed tree (the envelope
  becomes `activated:true`, so the pre-activation verifier will and must fail
  post-activation), and that the §10 active-state verifier governs thereafter.

- **P-7 — fix the exact commit staged-set and authorship trailers (§5.7, §10).**
  "Exact staged-path commit set" and "fixed authorship trailers" must be literal:
  list the exact paths for each committing step and the exact trailer string, so
  the activation commit is byte-reproducible in scope.

- **P-8 (confirmation, no repair) — the heartbeat max-uncharged-interval is
  correctly deferred (§7 last para).** It is a **named runtime engineering
  constant**, not a scientific/WP-6 numeric, and the draft correctly requires it be
  fixed before activation review rather than choosing a value here. Good; keep it
  distinct from any learner/Q numeric.

---

## Adversarial confirmations (sound as drafted)

- **Governing pins (§1):** all six SHA-256 pins match the committed artifacts
  (verified), and the pinned anchor-confirmation reviews are git-tracked.
- **Claim-before-effect / capability-after-commit:** §5.2 durable claim precedes
  every effect; §5.7 "no real-world/work capability exists before step 7's commit
  succeeds"; §6 requires a durable lease first. Correct.
- **Failure routing:** pre-claim failure → pristine T + new reviewed invocation;
  claim-through-commit failure → `T_ACTIVATION_INVALID:PROCESS`, no auto-retry/
  completion/rollback/deletion/capability, signed bounded recovery; a durable
  activation before a commit failure still governs E3 ("git failure never creates
  free calendar time"). §7's `T_RUNTIME_INVALID:PROCESS` covers orphan claim,
  start-without-lease, lease-without-start, state/ledger disagreement, open lease
  after process loss, non-monotone clock, ambiguous charge — no auto-retry, no
  estimated-zero charge, actual overrun recorded. Correct routing.
- **Overshoot / exhaustion:** the E1-crossing charge is retained in full; new work
  refused once exhausted (§7). Consistent with the accounting primitive.
- **E3 / pause / resume / author stop (§8):** both E3 clocks checked at every
  admission/heartbeat against actual UTC; a due review makes capabilities unusable
  until a durable `T_REVIEW_COMPLETED`; a planned power-off requires zero active
  leases + a full-quiescence checkpoint + the existing hash-linked
  `T_OPERATIONAL_PAUSE`; resume uses the confirmed `ResumeGate` with
  `resume_review_pending` blocking work; powered-off time advances E3 not E1;
  `T_AUTHOR_STOP` is signature-bound to a just-completed E3 review and distinct
  from exhaustion and pause. Sound.
- **E2 / WP-6 boundary (§9):** no production candidate-registration method; manifest
  functions usable on drafts but no `candidate_ids` update, E2 consumption, Q arming,
  or eligibility; WP-6 must first freeze candidate-blind Q numerics, attempt/
  depletion/alpha, stack-family, and the breathing-check tolerance/procedure. **No
  WP-6 numeric is prematurely chosen and no WP-4 cell is improperly deferred.**
- **Capability binding (§6):** exact-type, private-token, bound to activation
  record/process id/source HEAD/T bands/lease, revalidated at every constructor and
  use; cannot be relabeled Q/C, copied across processes, used after lease closure,
  or used for `[26,65]`/`[66,125]`. Extends the WP-4 anchor pattern.

## Implementation surface that would become eligible

After the bounded repairs (P-1..P-7) and a positive re-review, the eligible work
is **inactive implementation and tests only**: the activation-driver and metered-
runtime **state-machine library** (transaction sequencer, runtime-lock + fd-anchor
primitives, process-lease/charge/E3/pause/author-stop transitions, the active-state
verifier) plus the §10 test matrix, all exercised on **disposable repository
mirrors** — with **no** activation, real world, entropy, process lease, E1/E2/E3
spend, candidate registration, learner run, Q/C activity, authorization record, or
runtime artifact in the real tree. Implementation then needs its own X/Y review,
then a separate exact authorization candidate and Kirill's explicit
`I_AUTHORIZE_OFFICINA_T_ACTIVATION`, before the driver is invoked exactly once.

## Negative space

No token authorizes `I_AUTHORIZE_OFFICINA_T_ACTIVATION`; none is signable from this
draft. The predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; its records are non-citable and chose no value here.
Officina's T and Q are permanently non-citable for C1–C6; activation, leases, tuning
observations, breathing checks, draft manifests, E3 reviews, and every T ending are
non-scientific and move no claim; a future Q pass is a spendability gate fact only;
S is unavailable; only a valid, independently locked C execution may ever move an
Officina claim, within its selection-conditional, selected-frame, orientation,
device, and learner-seed scope. Censored/`UNKNOWN`/every invalid state are never
success, equivalence, a boundary, or learner impossibility. `PROOF_CORE`/
`PROOF_STRONG` remain earned by nothing; the programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this review), authorized
nothing, activated no T state, and committed nothing. `essay/OUTLINE.md` untouched.
My actions were reading the protocol and verifying the governing-pin hashes and the
pristine T state.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
