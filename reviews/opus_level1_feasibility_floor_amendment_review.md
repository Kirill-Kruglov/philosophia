# Opus 4.8 X-line — Level 1 feasibility-floor amendment review

Reviewer: Opus 4.8 (X-line, bounded to Fable's proposed feasibility-floor
amendment). Repository: `/home/master/llm_projects/philosophia`. **Nothing was
edited, committed, or run beyond read-only inspection and arithmetic
verification. No feasibility trajectory was executed; no entropy, comparative
datum, N3, lock, panel, escrow, or outcome was created or touched.** The
immutable v1 feasibility evidence (`censored_at_b: true`, execution HEAD
`c89a6b6…`, reviewed code `be53fdd…`) is non-outcome and was read only as the
prior it is.

I reviewed the candidate as written (`FEASIBILITY_GATE_DECISION_DRAFT.md` +
`fable_level1_feasibility_gate_closure.md`), against A8/A10 (v3.1), C6/C7
(v3.1.1), v3 §5–§8, the committed v1 report, the Sol scope review, and the
Level 0 anchor (`OUTCOME_RESULT.md`, `SCIENTIFIC_SPEC.json`,
`COMPANION_CONFIG_TRACE.md`). I re-derived the disputed arithmetic.

---

## Verdict

**`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`**

The **gate route is correct** (branch 1) and the **repair is a legitimate,
parameter-free, symmetric training-policy change** that aligns Level 1 with the
full-batch regime under which the platform's own modular-generalization result
was obtained. But three things must be corrected before Kirill signs: (1) the
scientific **justification overclaims on the wrong axis** — "example-gradient
budget ×31.5 / ≈400× below the Level 0 anchor" is not the axis that governs, and
on the axis that does (optimizer-update count) Level 1's count is *unchanged* and
already *below* Level 0's; (2) the **failure routing conflates a resource/process
stop with a learner-floor censoring**, which would convert a 36 h wall-hit into a
permanent scientific verdict against Level 1 — contrary to C6's own taxonomy; and
(3) the **v2 protocol is under-specified** (no report schema, no authorization
path, no reviewed-source pin over the *amended* code, no A5 §5 replacement text)
and the **branch-2 rejection predicts unobserved arms/worlds** (a forbidden
inference). None of these is fatal; all are exact, bounded edits.

---

## Findings (most severe first)

### Critical

**AM-1 — the "censored again, or invalid execution → BLOCKED" route converts
resource/process invalidity into learner-floor evidence.** The draft's §5 folds
two categorically different terminals into one: (a) a *completed* B = 2000 run
with no qualifying window (`censored_at_b: true`) — a genuine learner-floor
negative — and (b) *invalid execution* — which includes the 36 h wall-hit
(`capability.check_wall()` raising), OOM under the new full-batch memory profile,
environment/seal/hash failure, and any crash before or after the durable claim. A
wall-hit is a **RESOURCE_STOP**, not a zero-solve observation; the run never
completed B, so `censored_at_b` is not even defined for it. C6 (v3.1.1) itself
enumerates lock blockers as **distinct** categories — "resource infeasibility,
process/design invalidity, feasibility-gate failure, or Kirill's signed refusal"
— and A9's determinacy logic keeps resource stops off the scientific scale. Routing
(b) to `BLOCKED_LEVEL1_FEASIBILITY` would record "the locked learner class did not
reach a certified solve" when the true fact is "the resource cap or the platform
was insufficient," which is exactly the forbidden move (a process/resource limit
narrated as a learner verdict). This is especially live here because the 36 h wall
is set at 1.2× a *disputed* upper bound (see AM-4): a too-slow full-batch run at
`t → 2000` is a plausible wall-hit, and it must not read as a floor failure.

**Mandatory edit.** Separate the terminals explicitly (see the Q4 route table
below). Only a **completed** B = 2000 trajectory with no five-checkpoint
qualifying window is `censored_at_b: true → BLOCKED_LEVEL1_FEASIBILITY` (C1
untested by learner floor). Wall-hit / OOM / environment / seal / hash / crash →
a **signed resource-or-invalidity decision** that does **not** assert the learner
floor and does **not** consume the "no third floor amendment" budget. Scope the
"no third attempt" rule precisely to *no third learner/training-rule amendment*;
a resource-cap re-execution after a clean, mechanically-evidenced resource stop
(reproducing prefix hashes through the last checkpoint, update rule unchanged) is
the A6 process-re-execution category, not a third floor knob — otherwise a mere
timeout permanently and silently blocks Level 1.

### Major

**AM-2 — the Level 0 anchor is invoked on the wrong axis; the "×31.5 / ≈400×"
framing overclaims.** The arithmetic Fable cites is correct
(`Σ min(32,t) = 63,504`; `Σ t = 2,001,000`; ratio `31.51`), but it is the axis of
**cumulative examples processed**, which under CE `reduction='mean'` and `U = 1`
(one AdamW step per oracle answer — `train.py:46–57`, unchanged by the amendment)
governs **compute cost, not learning capacity**. The number of optimizer updates
is **2000 in both the original and the amended regime** — I verified this against
the code path. The amendment changes each of those 2000 updates from a 32-sample
*stochastic* mean-gradient to the exact *full-history* mean-gradient; it does not
create 31.5× more updates and does not scale any gradient by 31.5. On the axis
that actually anchors to Level 0 — **optimizer-update count** — Level 0 generalized
at **5,200–7,700 full-batch updates** (the GENERALIZE-start column), which is
**2.6–3.85× more updates than Level 1's unchanged 2000**, i.e. Level 1 sits
*below* the anchor on updates, not "≈400× below" and not "≈10× below after the
amendment." The "example-gradient budget" is not raised by the amendment in any
sense that Level 0 licenses.

What Level 0 *can* honestly anchor: **the optimizer family and betas
(`AdamW`, `(0.9, 0.98)`) and the viability of full-batch training for
modular-structure generalization at this ~2-layer / `d_model=128` scale.** That
is genuine, non-comparative provenance for *adopting* full-batch as the regime.
It cannot anchor update count (it undercuts the draft's direction), cannot anchor
"sample exposure" as a floor, and cannot anchor any solve-probability claim —
and the tasks differ (114-class residue vs binary EQ; seq 3 vs 277; 1-layer
causal vs 2-layer bidirectional; warmup+decay vs constant lr).

**Mandatory edit.** Rewrite §1's *Mechanics/Parameter-free* bullets and the
`fable_…_closure.md` "×31.5 work ratio" row to: (i) state that the update count is
unchanged at B = 2000; (ii) describe the change as *32-sample stochastic gradient
→ exact full-history mean gradient per update*; (iii) restrict the Level 0 anchor
to optimizer-family/betas + full-batch viability; (iv) delete every "example-
gradient budget," "≈400× below," and "≈10× below the anchor" quantitative claim.
Keep the `31.5×` figure **only** in §6 as a *compute-cost* multiplier, correctly
labelled (see AM-4).

**AM-3 — the v2 protocol is under-specified (paths, schemas, source pin,
spec-text replacement).** The draft names the claim schema
(`…feasibility-run-claim.v2`), an authorization schema
(`…feasibility-authorization.v2`), the token, and the output path
(`feasibility_v2/`), but omits, relative to the completeness the v1 driver
already demonstrates (`scripts/level1_run_feasibility.py`):

- the **report schema** (v1 = `philosophia.level1.noncomparative-feasibility.v1`;
  v2 needs an explicit `…v2`);
- the **authorization file path** (v1 =
  `FEASIBILITY_EXECUTION_AUTHORIZATION.json`; v2 needs a *distinct* path, e.g.
  `FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json`, so the v1 authorization cannot
  satisfy a v2 preflight);
- the **reviewed-source byte-pin set**, which must now be re-pinned over the
  **amended** `train.py` and `feasibility.py` (the current v1 `REVIEWED_SOURCE_PATHS`
  pins the *old* update rule) plus any `config.py` change and the amendment-doc
  hash;
- the **caps object**: the scorer is not re-run, so the v2 caps must set
  `scorer_steps: 0` (or omit the scorer path) and `wall_seconds: 129600`, and the
  driver must not execute the scorer microbenchmark;
- the **immutable v1 link must be *verified*, not merely recorded**: the v2
  preflight must recompute the v1 claim/report SHA-256 and **refuse on mismatch**
  (evidence mutation), and refuse if either v1 artifact is missing.

Separately, the amendment changes **signed spec text** — v3 §5's "minibatch = the
newest pair plus `min(31, t−1)` distinct history pairs" and A5's step-ordering
paragraph ("one shared minibatch per step … drawn under `("L1","replay",…)`") —
and retires the `("L1","replay", …)` PRF domain (A2 domain list, C2). A material
learner-rule change of this kind must be carried as **explicit replacement text
for A5 §5 / v3 §5**, signed, exactly as A5 requires that "a device switch is a
signed amendment … never a silent addendum change." It cannot live only as prose
in a decision draft.

**Mandatory edit.** Add the report schema, the distinct v2 authorization path,
the re-pinned amended-source set + amendment-doc hash, the `scorer_steps: 0` /
36 h caps, and the *verify-and-refuse-on-mutation* v1 link. Write the A5 §5 / v3
§5 replacement paragraph as signed text (the full-batch rule, `U = 1` unchanged,
`("L1","replay",…)` retired, history assembled in schedule order — order-immaterial
under mean reduction, but pin it for determinism).

**AM-4 — §6 labels a planning projection an "upper bound."** §6 asserts the
amended trajectory is bounded at "≤ ≈1.08×10⁵ s ≈ 30 h (upper bound — the
non-training overhead does not scale)." Multiplying v1's whole `random_static`
component (3,437 s, mean step 1.72 s) by 31.5 is **not** a defensible upper bound:
(i) it treats fixed overhead (oracle eval, checkpoint every 50 steps, panel eval)
as scaling, which over-counts in one direction but (ii) ignores that per-step
work is **super-linear-risk** at large `t` — the late steps carry a full batch of
up to 2000 × 277 tokens through a 4-member committee with retained backward state
on CPU float32, where batch-dependent kernels, allocation, cache pressure, and
the 2000 × 4-head × 277² attention score tensor (~2.4 GB retained per layer per
member) can make the true cost exceed linear. The per-step *example* ratio at
`t = 2000` is 62.5×, not 31.5×; the mean-based projection is not an envelope over
that tail. This is a **planning projection**, and the draft's own admission
("measuring the full-batch profile is part of the v2 check's job") is the correct
posture.

**Mandatory edit.** Relabel the §6 figure "planning projection, not a guaranteed
bound"; state that the full-batch memory/latency profile is unknown until the v2
check (or the bounded pre-check of Q3) measures it, and that a wall-hit routes per
AM-1, not to a floor verdict.

**AM-5 — the branch-2 rejection predicts unobserved arms/worlds.** The decision
draft's argument against proceeding under the current contract states the scout
"would predictably yield all-censored contrasts, the N3 projection would run on
the `B²` fallback everywhere, and the outcome battery would be an experiment
designed to route to `INSUFFICIENT`." That is precisely the inference A8 and the
signed negative space forbid: one n = 66 **RANDOM-STATIC** fixture censoring
cannot predict ACTIVE, YOKED, or donor arms (ACTIVE out-solving RANDOM is the
entire C1 hypothesis), cannot predict the other 11 development worlds up to
n = 125, and cannot pre-determine an `INSUFFICIENT` battery. The gate block does
**not** need this prediction — it stands on the gate-order prudence (don't spend
the one-shot scout/battery on a config whose only feasibility datum is a
zero-solve) plus the mechanical budget/full-batch-regime argument.

**Mandatory edit.** Strike the "predictably … all-censored … designed to route to
`INSUFFICIENT`" sentence; rest branch-2's rejection on the gate order (A10/C7
gate 6 before gate 7) and the mechanical-budget motivation alone. Keep the
existing verbatim narrow interpretation (the censoring says only that the single
predeclared RANDOM-STATIC fixture did not complete a window within B).

### Minor

**AM-6 — replay-stream retirement is clean; state it as a proof, not an
assertion.** Because each PRF domain owns an independent counter keyed by its
domain encoding inside the HMAC message (C2; `CounterStream`), removing
`("L1","replay",…)` perturbs **no** other stream, allocation counter, or init/
shortlist/feasibility digest — the retired domain simply produces no digests. The
amendment consumes no replay draw. Add the one-line non-perturbation statement
(and note that under `reduction='mean'` the full-history batch is order-invariant,
so "exact history order" is single-valued and immaterial to the update).

**AM-7 — name the temporal-weighting property honestly.** Under online
full-history full-batch training, a step-1 contact participates in all 2000
updates while a step-2000 contact participates in 1 — an implicit recency-anti-
weighting. This is a legitimate, standard consequence of incremental full-batch
retraining, and because it is applied **identically to every arm** it does not
confound the C1 contrast (which is differenced within block across arms sharing
member inits). But it *is* a real property of the amended learner and should be
named in the A5 §5 replacement text, not left implicit — so no later reader
mistakes it for a bug or a tuning choice.

---

## Answers to the five required questions

**1. Is branch 1 (amendment before comparative scout) the correct gate route?**
**Yes.** A10 gate 6 ("any signed feasibility amendment + re-review") sits before
gate 7 (comparative scout) precisely so the one-shot scout and battery are never
spent on a configuration with an observed zero-solve floor; C7 preserves that
order; A8 licenses exactly a *binary feasibility-floor amendment* as the sole
consequence of `censored_at_b`. Not branch 2 (proceeding spends the scout on an
observed-zero-solve config, against the gate order — but the branch-2 rejection
must be re-argued per AM-5, without predicting unobserved arms). Not branch 3
(a bounded, parameter-free repair in exactly A8's licensed class exists). Branch 1
is correct **conditional on** the AM-1..AM-5 edits.

**2. Is full-history training an honest single repair, and what claim can Level 0
support?** It is honest as a **single, parameter-free, symmetric training-policy
change** — no tunable knob, applied identically to all arms, retiring one PRF
stream and adding none. Its *justification* is not yet honest: it overclaims on
the example-gradient axis (AM-2). Level 0 supports **only** the optimizer
family/betas and the viability of full-batch AdamW for modular-structure
generalization at this scale — provenance for *adopting the regime*, not a
quantitative budget floor. It cannot support update-count (Level 1's 2000 is
*below* Level 0's 5,200–7,700), sample-exposure-as-floor, or any solve
probability. With the AM-2 rewording it becomes an honest single repair.

**3. Is a bounded implementation/resource audit eligible before signature, after
it, or unnecessary?** **After author signature of the amendment, before the v2
authorization/execution** — eligible and advisable, mirroring the gate-3 →
gate-5 split. The full-batch memory/latency profile is genuinely unknown and the
30 h "bound" is not rigorous (AM-4), so a **capped, non-outcome** implementation
check (unit tests of the new full-batch committee step + a shape/memory/timing
smoke probe at a representative `t`, e.g. one or few steps at `t ≈ 2000`, hard
step/wall cap) is warranted. It must be structured so it **cannot become a
configuration search**: the single fixed full-batch rule, no knob, no reading of
any loss/solve/score series, unit-only plus a bounded resource probe — never a
tuning loop and never folded into the outcome-bearing v2 check.

**4. What exact valid/censored/process-invalid routes must v2 implement?** At
least these five, kept categorically distinct:

| # | State | Route |
|---|---|---|
| 1 | Valid v2, run completes B = 2000, ≥ 1 five-checkpoint qualifying window | `censored_at_b: false` → **PASS** → gate-7 comparative-scout review under the amended, re-signed contract |
| 2 | Valid v2, run completes B = 2000, **no** qualifying window | `censored_at_b: true` → **`BLOCKED_LEVEL1_FEASIBILITY`** (learner floor; C1 untested), no third **floor** amendment |
| 3 | Non-finite learner state (loss/param divergence) under the signed routing | recorded non-finite; if no window completed before the non-finite stop → censored (state 2 terminal), **explicitly flagged non-finite**, never silent |
| 4 | Wall-hit (36 h) / OOM / environment mismatch / crash before or after the durable claim | **signed resource-or-process-invalidity decision** — **not** `censored_at_b`, **not** a learner-floor verdict; a clean resource stop may be re-executed under a reviewed resource-cap amendment (A6 category), never a learner re-tune |
| 5 | Evidence/seal/hash violation (v1 claim/report SHA mismatch or missing; v2 source-byte drift; canonical-JSON failure) | **whole-check invalidity**, refuse, produce no evidence |

Plus the full artifact contract (AM-3): distinct v2 report schema and
authorization path; caps `{development_worlds:1, trajectory_steps:2000,
scorer_steps:0, wall_seconds:129600}`, arm `RANDOM-STATIC`, world
`{pair_slot:0, modulus:66}`; reviewed-source byte-pin over the **amended** paths +
amendment-doc hash + `EXPECTED_HEAD == HEAD`, clean tracked tree, empty index;
environment enforcement (`torch 2.9.1+cpu`, CPU float32, deterministic); canonical
JSON; **durable claim written before the run**; atomic report after; fail-closed
refusal if `feasibility_v2/` already holds a claim/report; refusal on any
later-gate artifact; and the **verify-and-refuse-on-mutation** link to the
immutable v1 claim/report hashes. No quiet retry; no third floor intervention.

**5. After corrections, may Kirill sign
`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`, or is another bounded review
required?** **Another bounded review is required first** — a short confirmation
pass, not a fresh full review. Because the corrections change **signed spec text**
(the A5 §5 / v3 §5 replacement paragraph, AM-3) and the **failure taxonomy**
(AM-1), the edited amendment must be re-checked to confirm (a) the AM-1..AM-5
edits landed exactly and nothing else moved, (b) the A5 §5 replacement is
literal signed text with `("L1","replay",…)` retired and update count unchanged,
and (c) the v2 route table matches state-for-state. Sol's statistical cross-check
(endpoint/inference untouched; Level-0 provenance admissibility; 36 h cap) is
also outstanding per Fable's memo. After that bounded re-confirmation and the Sol
check, Kirill may sign.

---

## Implementation authorization boundary

This review authorizes **preparation only**, and only after author signature of
the *corrected* amendment: Codex/Fable may draft the corrected amendment document
(the reworded §1/§6, the A5 §5 replacement text, the five-state route table) and
may draft the **v2 authorization-candidate JSON** with the frozen structural
fields (v2 schema, token `I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2`,
`scientific_outcome:false`, `execution_once:true`, arm `RANDOM-STATIC`, caps
`{1, 2000, 0, 129600}`, world `{pair_slot:0, modulus:66}`, the distinct v2
output/authorization paths, the amended `reviewed_code_head`, and the verified
immutable v1 SHA links) as a **reviewable candidate**. The bounded
implementation/resource pre-check of Q3 may be prepared as unit tests + a capped
non-outcome probe.

Codex/Fable must **not**: assert the `I_ACCEPT_…` or `I_AUTHORIZE_…_V2` tokens on
Kirill's behalf; commit the authorization; invoke any feasibility driver (v1 or
v2); execute a feasibility trajectory; run the scorer; draw entropy; inspect or
reconstruct any query/loss/score/solve series; compare arms; select N3; create a
preregistration lock; build a real panel; create escrow; or produce any outcome.
Execution of the v2 check remains a separate, human-authorized one-shot after the
bounded re-confirmation and Kirill's signatures.

## Negative space (preserved, unweakened)

Adjacent-only C1 detector scope and the distance-1 boundary; the operational-
modulus certificate and its sole S4 tooth; `censored`/`UNKNOWN` never success,
never equivalence, never a boundary by narration; a certificate/feasibility
failure never evidence the learner lacked `n`; the public-root / escrow-secret-
panel separation and R_h-deferred; feasibility is `scientific_outcome:false`,
single-arm, one replicate — never a contrast, N3, lock, escrow, or decision;
development artifacts non-citable forever; Level 1 is a detector, not a programme
falsifier, and never evidence for `PROOF_CORE` in either direction. The v1
evidence is immutable and non-outcome and was neither deleted, renamed, nor
narrated as a failed attempt.

## Confirmation

I ran **no** feasibility trajectory and created **no** entropy, comparative
datum, N3, lock, panel, escrow, or outcome. I edited and committed nothing. I
inspected no loss/query/score/solve series (none exists). My only actions were
reading the governing files and re-deriving the amendment's arithmetic
(`63,504` / `2,001,000` / `31.51`; 2000 unchanged updates; Level 0's 5,200–7,700
updates) to adjudicate the claims above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
