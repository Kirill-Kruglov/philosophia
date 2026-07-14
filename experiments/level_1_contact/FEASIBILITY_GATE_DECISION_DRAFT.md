# Level 1 feasibility-gate decision draft

Status: `GATE_DECISION_FOR_BOUNDED_REVIEW`. Inputs: the committed one-shot
non-comparative feasibility evidence (claim SHA-256 `357baef2…c106ab`,
report SHA-256 `1c3843ec…820f7f`-class record at commit `052a341`,
execution HEAD `c89a6b6…2147`), the signed contract (v3 → v3.1.4.1 +
`SCIENTIFIC_SPEC_SIGNATURES.md`), and the Sol scope / Opus hardening
reviews. The raw claim and report are immutable, non-citable,
`scientific_outcome:false` evidence and are not touched. This draft runs
nothing, inspects no series, compares no arms, selects no N3, and creates
no lock, panel, escrow, or outcome.

## Verdict

**READY_FOR_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_REVIEW**

**The observed `censored_at_b: true` blocks the comparative scout pending
a signed floor amendment (branch 1).** Reasoning against the other two
branches:

- **Not branch 2 (proceed under the current contract).** A8's binary
  floor — "the locked architecture/B produced at least one complete
  development solve, or did not" — resolved to **did not**. C6 names
  `feasibility-gate failure` as a lock blocker, and the v3.1 A10 /
  v3.1.1 C7 gate order places reviewed feasibility (gate 5) and "any
  signed feasibility amendment + re-review" (gate 6) **before** the
  comparative scout (gate 7) precisely so the one-shot scout and battery
  are never spent on a configuration with an observed zero-solve floor.
  Under the current contract the development scout would predictably
  yield all-censored contrasts, the N3 projection would run on the `B²`
  fallback everywhere, and the outcome battery would be an experiment
  designed to route to `INSUFFICIENT`. Ambiguity is not resolved in
  favor of progress.
- **Not branch 3 (Level 1 blocked).** A bounded, honest, single-valued
  repair class exists and is exactly the class A8 licenses: a
  feasibility-floor amendment justified by the binary observation plus
  the platform's own non-comparative anchor, with a second one-shot
  binary check. Level 1 is blocked only if that amended check is also
  censored (§5).

The signed narrow interpretation is preserved verbatim: the censoring
says only that the single predeclared RANDOM-STATIC development fixture
did not complete a five-checkpoint dummy-panel solve window within B. It
does not say the learner lacks the modulus, that RANDOM-STATIC is
inferior, or that Level 1 is false.

## 1. The one frozen change, and why the binary observation licenses it

**Amendment (single-valued, no alternatives):** the online update rule of
v3 §5 — "minibatch = the newest pair plus `min(31, t−1)` distinct history
pairs, `U = 1`" — is replaced, identically for **every** arm (target
ACTIVE, donor ACTIVE, YOKED, RANDOM-STATIC), by:

> At oracle step `t`, each member takes exactly one AdamW step on the
> **entire accumulated own contact history** (all `t` answered pairs) as
> a single full batch, with CE `reduction='mean'`, computed as one
> unchunked forward/backward. `U = 1` is unchanged. The
> `("L1","replay", …)` PRF domains are retired (the amended rule consumes
> no replay draw); every other stream, domain, and counter is unchanged.

**Why this class:** A8 permits exactly one thing to follow from
`censored_at_b`: a binary feasibility-floor amendment to the locked
architecture/B-regime, never a value tuned toward a solve rate. **Why
this member of the class:**

- *Mechanics:* the current rule caps optimization at
  `Σ min(32, t) = 63,504` example-gradients per member over the whole
  run. The programme's only non-comparative, Level-1-external anchor for
  modular-structure generalization at this model scale is the **Level 0
  earned platform decision**: full-batch AdamW (same optimizer family,
  same betas), which reached generalization at ≈ 5,200–7,700 epochs ×
  3,830 examples ≈ 2–3 × 10⁷ example-gradients. The current budget sits
  ≈ 400× below that anchor; the floor failure is mechanically
  unsurprising.
- *Parameter-free:* "train on everything you have, full-batch" contains
  **no free number** — nothing can be tuned toward a desired solve rate.
  It raises the budget to `Σ t = 2,001,000` example-gradients per member
  (≈ 31.5×) by adopting the platform's own regime, not by choosing a
  knob. (Honesty: this is still ≈ 10× below the Level 0 anchor; the
  amendment does not guarantee a pass — the binary re-check decides.)
- *Not an endpoint or inference change:* B, the oracle budget, cadence,
  persistence, panel, margins, and estimator are all denominated in
  oracle steps/queries and are untouched.

## 2. Every unchanged cell

Unchanged in full: architecture and all A5/C4 pins; optimizer family,
lr, betas, eps, decay groups; `B = 2,000`; cadence 50 and the
five-checkpoint window; the panel contract (v3.1.4 + v3.1.4.1) and the
operational-modulus certificate; endpoint, censoring, margins `±60`,
determinacy table, estimator, N3 rule; C1 scope and the detector
asymmetry; arm definitions and the donor yoke; acquisition rule,
shortlist, scorer and its state-hash contract; population, allocation,
public-root/secret-panel separation; all leakage gates; all invalidity
routing; all three signed tokens and the panel token; every gate after
gate 6. The only implementation-surface consequences: the replay stream
retirement (deterministic — a stream is removed, none added) and the
memory profile of the full-batch step, which the amended check itself
measures.

## 3. Exact amended feasibility protocol and report surface

One reviewed, capped, one-shot **amended** check — a new experiment, not
a rerun:

- **Fixture:** identical to v1 — the predeclared development world
  (`modulus 66, pair_slot 0`), RANDOM-STATIC arm, one replicate, the
  same dummy panel, cadence, persistence rule, and pass criterion
  (**identical to v1**: at least one complete five-checkpoint qualifying
  window within B; only the update rule differs).
- **Caps:** trajectory 2,000 steps; scorer microbenchmark **not
  repeated** (the scorer is untouched; its v1 aggregates stand); wall
  cap **129,600 s (36 h)** — 1.2× the §6 upper-bound component
  projection, an outcome-independent resource cap.
- **Allowed report surface (A8, unchanged):** latency aggregates, peak
  memory, projected wall components, artifact sizes, finiteness flags,
  and the single-arm `censored_at_b` indicator. No query, loss, score,
  or solve series; `scientific_outcome: false`; the no-arm-inference
  interpretation string verbatim.

## 4. New one-shot artifact schema/path/token

- Path: `experiments/level_1_contact/feasibility_v2/` with
  `LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2_CLAIM.json` and
  `LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2.json`.
- Schemas: `philosophia.level1.feasibility-run-claim.v2` /
  `philosophia.level1.feasibility-authorization.v2`.
- The claim binds: a **new reviewed code HEAD**, the amendment-document
  hash, a **new explicit Kirill execution token**
  (`I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2`), and an
  **immutable link to the censored v1 evidence** (claim SHA
  `357baef2…c106ab`, report SHA `1c3843ec…0f7f`).
- **Fail-closed no-delete/no-retry:** the driver refuses if the v2 path
  exists; the v1 artifacts are never deleted, renamed, or re-labeled a
  "failed attempt"; a process failure before durable commit routes to a
  signed invalidity decision, never a quiet re-run.

## 5. Deterministic pass/fail route

- **Pass** (`censored_at_b: false` under the identical v1 criterion) →
  proceed to **comparative-scout review** (gate 7 review) under the
  amended, re-signed contract.
- **Censored again, or invalid execution** → **`BLOCKED_LEVEL1_FEASIBILITY`**,
  with **no third attempt**: Level 1 is recorded `INSUFFICIENT` by
  feasibility; the untested claim is named — *whether online
  responsiveness at distance 1 shortens budget-to-certified-solve
  remains untested, because the locked learner class did not reach a
  certified development solve within the frozen budget under either the
  original or the platform-anchored regime.* The only exits are Kirill's
  signed redesign of the learner/world contract (a new programme
  decision with full review, not an amendment) or the standing record.
  A third knob-turn would be optimizing toward a solve rate — A8's
  forbidden move — and is not scientifically honest.

## 6. Resource implications (component projections only)

Using only the committed aggregates, never as a full-run forecast: the
training-work multiplier is `Σt / Σmin(32,t) = 2,001,000 / 63,504 ≈
31.5×`; the v1 RANDOM-STATIC component (3,437 s for B, which already
includes oracle and checkpoint overhead) bounds the amended trajectory
component at **≤ ≈ 1.08 × 10⁵ s ≈ 30 h** (upper bound — the non-training
overhead does not scale). The ACTIVE scorer component (14,467 s) is
unchanged by this amendment. Peak memory rises with batch size (v1 peak
RSS 1,474,896 KiB at batch ≤ 32); measuring the full-batch profile is
part of the v2 check's job on the 128 GB platform. Full-battery
implications are deferred to the resource wall at lock and are
explicitly **not** forecast here.

## 7. Author signature token

After bounded Opus and Sol reviews of this amendment:

`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`

(alternative: a named refusal, which — because branch 2 is closed —
routes Level 1 to `BLOCKED_LEVEL1_FEASIBILITY` by decision rather than
by evidence). The three scientific-spec tokens and the panel token
remain valid for all unchanged science.
