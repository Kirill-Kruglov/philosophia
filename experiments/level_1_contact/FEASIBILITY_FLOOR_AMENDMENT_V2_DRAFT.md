# Level 1 feasibility-floor amendment — v2 (reconciled)

Status: `LOUD_PRE_DATA_AMENDMENT_FOR_FINAL_CHECK`. This document
reconciles the Opus X-line review
(`reviews/opus_level1_feasibility_floor_amendment_review.md`, AM-1–AM-7)
and the Sol Y-line review
(`reviews/sol_level1_feasibility_floor_amendment_review.md`, C1–C2,
M1–M5, m1), both `REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`, into a
single amendment candidate. `FEASIBILITY_GATE_DECISION_DRAFT.md` and
`reviews/fable_level1_feasibility_gate_closure.md` are **preserved
unedited as the reviewed historical artifacts**; this v2 supersedes only
the sentences named in §8. Historical specs (v3–v3.1.4.1) and
`SCIENTIFIC_SPEC_SIGNATURES.md` are untouched; §2 gives the literal
replacement text for the exact governing cells this amendment changes.

This document creates no code, no authorization, no entropy, no
resource probe, no trajectory, no comparative datum, no N3, no lock, no
panel, no escrow, and no outcome. It runs nothing.

Closed decisions carried forward unopened: branch 1 (the original
learner is blocked at the feasibility gate; a signed floor amendment may
be reviewed before any comparative scout); the single candidate (one
full-history, CE-mean AdamW update per oracle answer, identical for
every target and donor learner; no alternatives, no numeric tuning
range); `B = 2,000`, `U = 1`, model, optimizer settings, committee size,
endpoint, cadence, persistence, panel, margins, population, yoke,
selector, and N3 rule all frozen; the v1 evidence and authorization
immutable and non-outcome.

## Verdict

**READY_FOR_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_FINAL_CHECK**

---

## 1. What the v1 evidence establishes (narrowed; Sol C1/M1, Opus AM-5)

> The valid v1 record establishes only a floor failure on the frozen
> original-policy fixture. Under the signed gate policy, that blocks the
> comparative scout under the original learner and permits — but does
> not empirically select — a signed floor amendment.

Exactly this and nothing more. The v1 binary
(`censored_at_b: true`, RANDOM-STATIC, `modulus 66, pair_slot 0`, one
replicate, original replay policy) does **not** establish: that other
worlds or arms would censor; that the development contrasts would be
all-censored; that any battery would return `INSUFFICIENT`; that the
learner lacks `n`; that RANDOM-STATIC is inferior; that Level 1 or C1 is
false; or that full-history training is empirically necessary or
uniquely selected. The gate declines to spend the one-shot scout under
the original learner **without pretending to know what that scout would
have returned.** A8 licenses consideration of a floor amendment; it does
not license a search for a preferred result. A future v2 pass is a gate
fact only — never evidence for ACTIVE, YOKED, RANDOM-STATIC, C1, an
outcome-world solve probability, or the programme.

## 2. The amendment as literal signed replacement text (Opus AM-3/AM-6/AM-7)

The single change: the minibatch-32 replay rule is replaced, identically
for **every** learner (target ACTIVE, donor ACTIVE, YOKED target,
RANDOM-STATIC, and every control/feasibility trajectory), by one
full-history, CE-mean AdamW update per oracle answer. The exact
governing cells change as follows; **every other sentence of every
signed document carries forward verbatim.**

### 2a. v3 §5, "Online step" bullet — replaced by:

> **Online step at oracle step `t` (exact order):** receive bit → each
> member records pre-update `p̂` → assemble the **full-history batch**:
> all `t` answered pairs of this learner's **own** contact history,
> in canonical contact-schedule order (oracle steps `1..t`), as one
> shared unchunked tensor → per member: one forward over the full
> batch, backward, `optimizer.step`, `optimizer.zero_grad`
> (`U = 1`; CE `reduction='mean'`) → optional checkpoint. No replay
> draw exists. No batch training after collection; no early stop; all
> arms run to common `B`.

### 2b. v3.1 A5, step-ordering paragraph — replaced by:

> **Step ordering:** forward → backward → `optimizer.step()` →
> `optimizer.zero_grad()`; **one shared full-history batch per step per
> arm-replicate**: at oracle step `t`, all `t` answered pairs of the
> learner's own contact history, assembled in canonical
> contact-schedule order as a single unchunked tensor; all 4 members
> train on this same tensor, each member taking exactly one
> forward/backward/AdamW step and zeroing its gradients. CE
> `reduction='mean'`; `U = 1`; no chunking, no gradient accumulation.
> The `("L1","replay", block, arm, replicate, step)` PRF domain is
> **retired**: it is drawn from nowhere and consumes no digest and no
> counter. Checkpoints at the evaluator cadence (every 50 steps + 0 +
> B), containing all members' parameters and optimizer moments, every
> PRF counter, contact history, answered set, and step counter;
> deterministic resume must reproduce state hashes.

**Batch-order pin (normative):** under exact arithmetic, mean-reduced CE
is permutation-invariant in the batch, so the contact-schedule order is
single-valued and inferentially immaterial; it is nevertheless **pinned
as the canonical assembly order** because float32 summation is not
associative and the checkpoint state hashes must be deterministic bytes.

### 2c. v3.1 A2, domain list — replaced by:

> Domains (complete list): `("L1","alloc","dev")`;
> `("L1","alloc","role")`; `("L1","alloc","sample", N3)`;
> `("L1","pool","reserve", d)` per `|d|` class;
> `("L1","pool","realize", a, b)` per cell;
> `("L1","panel", world_slot, stratum, item)`;
> `("L1","learner","init", block, replicate, member, tensor_name)`;
> `("L1","shortlist", block, arm_slot, step)`;
> `("L1","control","shuffle", world_slot, replicate)`; `("L1","feas")`.

(the sole edit: `("L1","replay", block, arm, replicate, step)` is
removed; the v3.1.1 C2 refinements of the allocation domains carry
forward unchanged on top of this list.)

### 2d. Retirement perturbs no other stream (proof; Opus AM-6)

`encode(domain)` is the concatenation of the domain's components, each
as `uint16_be(byte_length) || UTF-8 bytes` — an injective encoding, so
distinct domains produce disjoint HMAC message sets. By v3.1.1 C2, each
domain owns its own counter starting at zero, and no counter is ever
shared or reset across domains. Therefore the digest sequence of every
other domain — allocation (`dev`, `role`, `sample`), pool reservation
and realization, panel, learner init, shortlist, control shuffle, and
feasibility — is a function only of the root key and that domain's own
draw count, neither of which this amendment changes. Retiring the
replay domain removes only the replay digests; it perturbs **no**
allocation, init, shortlist, control, feasibility, panel, or pool
stream, byte for byte.

### 2e. Conforming edits, and cells explicitly unchanged

- **v3.1.1 C3 surface table**, public-root row: the word "replay" is
  deleted from "Allocation, pool, inits, shortlist, replay, controls,
  feasibility" (the retired domain has no surface). No other C3 text
  changes; the public-root/escrow-secret split is untouched.
- **v3.1.1 C2** is otherwise unchanged (its allocation-domain and
  counter-independence text is what §2d relies on).
- **v3.1.1 C4** is unchanged in full: input length 277, displacement/
  word-length bounds 128/138, `fan_in` enumeration, seed decoding,
  torch `2.9.1+cpu`, and the enumeration tests all carry forward.
- **Scorer contracts unchanged:** the side-effect-free scorer, its
  state-hash equality requirement (parameters, optimizer, training RNG
  unchanged by scoring), and the noninterference/canonicalization gates
  (v3 §5, v3.1 A7, v3.1.1 C5) carry forward verbatim. The amendment
  touches training only, never scoring or evaluation.

## 3. Learner-class scope (Sol M2; Opus AM-7)

> All Level 1 potential outcomes and contrasts are conditional on the
> full-history, mean-CE, one-update-per-answer learner policy. This
> replaces the stochastic replay learner class; it preserves the
> high-level ACTIVE-vs-YOKED question and estimator form but defines a
> new learner-class conditional estimand.

This scope text amends the question/estimand/treatment language of v3
§§1–2 wherever the learner policy is implicit. The estimator, endpoint,
margins, determinacy table, and N3 rule keep their mathematical forms;
the potential outcomes entering them are those of the amended learner
class. It is not the same locked-policy estimand numerically or
operationally.

**Temporal weighting (named, not implicit):** under full-history mean
CE, every retained pair is included in every later and current update
with per-update gradient weight `1/t`; the contact answered at step 1
participates in all 2,000 updates while the contact answered at step
2,000 participates in exactly one. This is a substantive reweighting of
contact history relative to the replay policy (newest pair guaranteed
once, older pairs stochastically replayed). Applying the same rule to
every learner prevents an arm-label implementation asymmetry; it does
**not** make the learner intervention neutral. Any differential effect
across arms is an effect under the new learner policy, not evidence
that the amendment itself is inert.

## 4. Provenance and work arithmetic, corrected (Opus AM-2; Sol M4, m1)

- **Update count is unchanged.** Both the v1 policy and the amended
  policy take exactly 2,000 AdamW updates per committee member (one per
  oracle answer; 8,000 member-updates per trajectory). The amendment
  changes each update from a 32-example stochastic mean gradient to the
  exact full-history mean gradient; it creates no additional updates
  and scales no gradient.
- **Units.** `Σ min(32, t) = 63,504` and `Σ t = 2,001,000` count
  **example evaluations** per member over the run — not gradients,
  conserved gradient mass, or learning-capacity units. Their exact
  ratio `2,001,000 / 63,504 = 31.5098…` (reported 31.51) is a
  **compute-work ratio only**. It quantifies the cost of the amendment;
  it licenses no capacity, floor, or solve-probability claim.
- **Level 0's role.** Level 0 is an engineering precedent that
  full-batch AdamW ran on this platform for a different locked task; it
  supplies no comparative evidence and no choice among Level 1 repairs.
  It anchors no update-count floor (Level 0 Arm A generalization starts
  occurred at ≈ 5,200–7,700 full-batch updates; Level 1 retains 2,000 —
  *below* that on the update axis), no sample-exposure floor, and no
  prediction. Architecture, sequence length, task, training set, decay
  specification, and threading all differ, and the Level 0 outcome
  itself forbids generalization beyond its locked task.
- **Why this candidate, honestly.** The defensible, non-empirical
  reasons for retaining full-history training as the sole candidate are
  its **simplicity** (no sampling policy at all), **determinism**
  (one fewer stochastic stream; a PRF domain retired, none added),
  **full use of the declared contact history**, and **removal of replay
  sampling as a nuisance source**. It contains no new numeric
  hyperparameter in the syntactic sense, but it is a substantive
  **capacity/optimization-policy change** — an outcome-triggered 31.51×
  increase in example evaluations plus the §3 history reweighting —
  authorized for review by A8, not "inferentially parameter-free," not
  uniquely likely to pass, and not mechanically predicted to pass or
  fail. The v2 binary check alone decides.

## 5. Resource matching and projection (Sol M3; Opus AM-4)

At every oracle step `t` of a valid trajectory:

| Learner | Oracle answers accessible | Committee | Updates at `t` | Batch size | Scorer work | Donor-generation work |
|---|---|---|---|---|---|---|
| target ACTIVE | its own `t` target answers | 4 | 1 per member | `t` | shortlist `S = 512` × `E = 4` forwards per step | none |
| donor ACTIVE | its own `t` donor answers | 4 | 1 per member | `t` | shortlist `S = 512` × `E = 4` forwards per step | is itself the donor trajectory for its block's YOKED |
| YOKED target | its own `t` target answers (queries = the donor's frozen realized geometry) | 4 | 1 per member | `t` | none | requires one completed donor ACTIVE trajectory (package level) |
| RANDOM-STATIC | its own `t` target answers | 4 | 1 per member | `t` | none | none |

- **Matched:** target scientific query exposure (`t` answers by step
  `t`, `B` total) and per-trajectory training work (2,000 updates × 4
  members; batch size `t` at step `t`; identical tensor shapes) are
  matched across arms at every `t`. Every donor ACTIVE trajectory obeys
  the same rule for its own members and its own answers; replicates use
  the same schedule.
- **Not matched, and not claimed matched:** total arm-**package**
  compute. ACTIVE and donor ACTIVE incur shortlist scoring that YOKED
  and RANDOM-STATIC do not; the YOKED package requires a separate donor
  trajectory. These are fixed parts of the treatments — **treatment
  machinery** — and belong in the later operational resource ledger.
  They give the YOKED target no extra training examples and no extra
  target answers. Donor answers and donor state never enter the YOKED
  learner; only the frozen query geometry does, exactly as the signed
  yoke defines.
- **Projection (relabeled):** the v1 `random_static` component
  (3,437 s) times 31.51 gives ≈ 1.08 × 10⁵ s ≈ **30 h — a
  linear-scaling planning projection, not a guaranteed or demonstrated
  bound.** It assumes at-most-linear scaling of an unchunked
  full-history forward/backward despite changing batch size, memory
  traffic, allocator behavior, and possible paging; the per-step
  example ratio at `t = 2,000` is 62.5×, not 31.51×. The full-batch
  memory/latency profile is unknown until the v2 check measures it
  (v1 peak RSS 1,474,896 KiB was at batch ≤ 32).
- **Wall cap semantics:** the cap is **129,600 s (36 h)**, frozen
  outcome-independently (from the resource projection, not from any
  desired pass/fail observation) — but **not known sufficient**. It is
  enforced against wall-clock only and **checked without consulting
  panel or evaluator performance**. Reaching the cap before a valid
  terminal report is a **resource-stop invalidity** (§7 route 4): a
  partial wall-stopped run has **no `censored_at_b` value** and may
  never be called pass or censored.

## 6. Bit-exact v2 artifact contract (Opus AM-3; frozen names)

| Element | Frozen value |
|---|---|
| Authorization path | `experiments/level_1_contact/FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json` |
| Output directory | `experiments/level_1_contact/feasibility_v2/` |
| Claim file | `LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2_CLAIM.json` |
| Report file | `LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2.json` |
| Authorization schema | `philosophia.level1.feasibility-authorization.v2` |
| Claim schema | `philosophia.level1.feasibility-run-claim.v2` |
| Report schema | `philosophia.level1.noncomparative-feasibility.v2` |
| Execution token | `I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2` |
| Caps | `{development_worlds: 1, trajectory_steps: 2000, scorer_steps: 0, wall_seconds: 129600}` |
| Arm / world | `RANDOM-STATIC`, `{pair_slot: 0, modulus: 66}` |

The scorer microbenchmark is **not executed** (`scorer_steps: 0`); the
scorer is untouched by this amendment and its v1 aggregates stand. The
fixture, dummy panel, cadence, persistence rule, and pass criterion are
byte-identical to v1; only the update rule differs.

**Preflight (fail-closed, all mandatory):** canonical JSON throughout;
exact environment (torch `2.9.1+cpu`, CPython 3.12.3, CPU float32,
deterministic algorithms, single thread, fingerprint match); clean
tracked tree and empty index; `EXPECTED_HEAD == HEAD`; source-byte pins
over **every amended and reachable module** (the amended training and
feasibility paths, any config change, and the full reviewed set — the
v1 pin set pinned the old update rule and cannot be reused); the
**committed hash of this amendment document**; recompute and verify the
exact v1 evidence hashes

```text
357baef22226bfb92b909192d2264420923facd55115b9c272bb2cb848c106ab  feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY_CLAIM.json
1c3843ec66f57e8a7e05b88d5f942093113f11f5ac36746f202f1a6556820b7f  feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY.json
```

and **refuse** if either file is missing or either recomputed hash
mismatches (evidence mutation); **refuse** if any v2 claim/report path
already exists; **refuse** if any later-gate artifact exists
(comparative scout, N3 selection, lock, real panel, escrow, outcome).
The durable v2 claim is written and committed **before any learner
step**; the report is written **atomically after valid completion**.

*Transcription correction (loud):* the gate decision draft abbreviated
the v1 report hash as "`1c3843ec…820f7f`"; the recomputed full value
above ends `…820b7f`. The historical draft is not edited; the full
recomputed values here govern the preflight.

**Not created here:** the v2 authorization candidate JSON itself is not
drafted in this task; it may be drafted only after Kirill signs this
amendment, and its execution requires Kirill's explicit
`I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2`.

## 7. Validity-first terminal table (Opus AM-1; Sol C1/C2/M5)

`censored_at_b` exists **only after validity is established**. The five
routes are mutually exclusive and exhaustive:

| # | State | Record | Route |
|---|---|---|---|
| 1 | Valid completed v2 (`B = 2,000` reached, all seals/hashes verified), ≥ 1 complete five-checkpoint qualifying window | `censored_at_b: false` | **PASS** → comparative-scout **review** only (gate 7 review under the re-signed contract). *A v2 pass is a gate condition only and has no arm, C1, outcome-world, or programme interpretation.* |
| 2 | Valid completed v2, no qualifying window | `censored_at_b: true` | **`BLOCKED_LEVEL1_FEASIBILITY`** — C1 untested; no third learner-policy intervention. *The amended fixture did not clear the floor; the C1 detector remains unrun and untested.* |
| 3 | Validly recorded scientific non-finiteness (loss/parameter divergence under the signed A6 routing) | per A6: a complete qualifying window **before** the first non-finite state stands (route 1, with the divergence a mandatory recorded diagnostic); otherwise **scientific censoring** with the non-finite flag set (route 2 terminal) | the already signed A6 rule, preserved exactly; **never relabeled a hardware or process fault**, never silent |
| 4 | Environment mismatch / resource-cap hit (36 h wall before a valid terminal report; memory exhaustion) / process fault (crash, missing artifact, non-resumable run) | `LEVEL1_FEASIBILITY_V2_INVALID:<ENVIRONMENT\|RESOURCE_CAP\|PROCESS>`; **`censored_at_b` unset** | no learner inference in either direction; no pass/censor narration; **no automatic retry**; a signed invalidity disposition |
| 5 | Hash/seal/evidence/source violation (v1 SHA mismatch or missing; v2 source-byte drift; canonical-JSON failure; any seal breach) | `LEVEL1_FEASIBILITY_V2_INVALID:<HASH\|SEAL>` — whole-check invalidity | **fail closed**; produce no evidence; the governing `PLATFORM_OR_DESIGN_INVALID` destination is preserved wherever v3 §7 requires it |

**No invalidity subtype authorizes a rerun or another learner
intervention.** Reconciling the one reviewer difference conservatively
(Opus AM-1 would classify a clean, mechanically evidenced resource stop
as the A6 process-re-execution category; Sol forbids any automatic
recovery): **the strict Sol resolution is adopted.** An invalid run
authorizes nothing automatically. Any future mechanically justified
resource recovery — e.g. a reviewed wall-cap change after a clean
`RESOURCE_CAP` stop with prefix hashes intact — would require a **new
explicit Kirill-signed process/resource decision and its own bounded
review, with the learner rule unchanged**. Such a decision would not be
a third floor amendment (it touches no learner policy), but **this
amendment does not pre-authorize it.**

The "no third attempt" rule is thereby scoped exactly: no third
**learner/training-policy** intervention exists on any branch; and no
process/resource recovery exists without a new signed decision.

**Future canonical status lines (exact; not written now — the ledger
and ROADMAP are not edited by this amendment):**

- valid second censoring, ledger: "Level 1 feasibility floor —
  `BLOCKED_LEVEL1_FEASIBILITY`; C1 untested; no comparative scout; no
  programme evidence."
- valid second censoring, ROADMAP: "Level 1 — BLOCKED BY VALID V2
  FEASIBILITY CENSORING; detector not run; no third feasibility
  intervention."
- invalid v2, ledger: "Level 1 feasibility v2 —
  `LEVEL1_FEASIBILITY_V2_INVALID:<cause>`; feasibility binary unset; no
  learner-floor evidence; C1 untested," followed by the governing
  `PLATFORM_OR_DESIGN_INVALID` route where applicable.
- invalid v2, ROADMAP: "Level 1 — V2 INVALID (<cause>); no pass/censor
  result; no automatic rerun or intervention."

**Non-inferential gate (Sol M5):** because the v1 binary triggered this
amendment, v2 is not independent confirmation and cannot estimate
improvement; **no v1/v2 contrast may ever be formed.** A pass merely
removes the feasibility blocker and opens comparative-scout review.

## 8. Superseded sentences (named, nothing silently dropped)

From `FEASIBILITY_GATE_DECISION_DRAFT.md` (preserved unedited):

1. "Under the current contract the development scout would predictably
   yield all-censored contrasts, the N3 projection would run on the
   `B²` fallback everywhere, and the outcome battery would be an
   experiment designed to route to `INSUFFICIENT`." — **withdrawn**
   (Opus AM-5; Sol M1). Branch 2's rejection now rests on §1's narrow
   statement plus the A10/C7 gate order alone.
2. Every "example-gradients" usage — **renamed "example evaluations"**;
   the "≈ 400× below that anchor" comparison, "the floor failure is
   mechanically unsurprising," "raises the budget to … (≈ 31.5×) by
   adopting the platform's own regime," and "still ≈ 10× below the
   Level 0 anchor" — **withdrawn** (Opus AM-2; Sol M4). §4 governs.
3. "*Parameter-free:* … contains no free number" as a characterization
   of the amendment's inferential status — **replaced** by "no new
   numeric hyperparameter; a substantive capacity/optimization-policy
   change" (Sol m1; §4).
4. §5's merged route "Censored again, or invalid execution →
   `BLOCKED_LEVEL1_FEASIBILITY` … no third attempt" — **superseded** by
   §7's validity-first table (Opus AM-1; Sol C1).
5. §6's "upper bound — the non-training overhead does not scale" and
   "bounds the amended trajectory component at ≤ ≈ 1.08 × 10⁵ s ≈ 30 h
   (upper bound…)" — **relabeled** "30 h linear-scaling planning
   projection" (Opus AM-4; Sol C2).
6. §4's abbreviated v1 report hash "`1c3843ec…0f7f` / …820f7f" —
   **corrected** to the recomputed full value in §6 here.

From `reviews/fable_level1_feasibility_gate_closure.md` (preserved
unedited): the allowed-use row "component upper bound for the amended
trajectory (×31.5 work ratio)" — **superseded**: the 3,437 s component
supports only the §5 planning projection, and 31.51 is a compute-work
ratio only.

Everything else in both historical documents — the branch-1 route, the
narrow v1 interpretation, the fixture identity, the one-shot
no-delete/no-retry discipline, and all §2 unchanged-cell lists —
carries forward.

## 9. Author signature token

After the bounded Opus and Sol **final confirmations of this v2 text**:

`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`

The token is **not signable until both final confirmations accept this
v2 text.** (Alternative: a named refusal, which — branch 2 being
closed — routes Level 1 to `BLOCKED_LEVEL1_FEASIBILITY` by decision
rather than by evidence.) The three scientific-spec tokens and the
panel token remain valid for all unchanged science; §3's learner-class
scope is exactly what this new token accepts.

All signed negative destinations are preserved unweakened: only a valid
comparative C1 result can reach
`BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`; unresolved executed
comparisons route to `INSUFFICIENT`; applicable process/design failures
retain `PLATFORM_OR_DESIGN_INVALID`; certificate failure or censoring
never proves the learner lacked `n`; censored/`UNKNOWN` never success,
equivalence, or a narrated boundary; development artifacts non-citable
forever; neither feasibility gate can support `PROOF_CORE`; Level 1
remains a detector, not programme evidence, in every branch.
