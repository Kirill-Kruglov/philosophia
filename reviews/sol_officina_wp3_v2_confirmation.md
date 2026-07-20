REVISE_OFFICINA_WP3_V2

# Review boundary

I reviewed the complete v2 replacement at `9f8bdc7` against the signed charter and v2.1 correction, charter signature, author selections, WP-1/WP-2 closure, both v1 reviews, and Fable's v2 closure memo. The committed delta `9f8bdc7..HEAD` contains only the two confirmation prompts; no load-bearing source or governing artifact differs. The inactive verifier returned `OK: Officina WP-1/WP-2 bootstrap is quarantined and inactive.` `git diff --check 9f8bdc7..HEAD` found only a trailing blank line in the review-only Opus confirmation prompt.

V2 closes the frame-arithmetic, typed-observation, small-stratum, Q-transport, Q-depletion, claim-boundary, multiplicity, and recommendation-provenance defects. One bounded statistical defect remains in OR-2, together with one selection-history wording defect. Neither requires reopening CH-1, CH-2, either orientation choice, or the transport premise.

# Findings

## Critical

None.

## Major

1. **OR-2 does not yet define a valid conditional SRSWOR realization completely.** At `OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_DRAFT.md:333-344`, “before/with C sampling” does not establish whether the full orientation vector is fixed before the sample is derived, and no domain-independence obligation separates the orientation vector from the block sample. Conditional finite-frame inference for `theta(r)` requires
   `Pr(S_h=s | r)=1/binom(N_h,n_h)` for every eligible stratum subset `s`. Two deterministic functions of one root do not acquire this property merely by being called orientation and sampling. The same secret C root may be used, but orientation and sample derivation must use distinct typed PRF domains (or an equivalently reviewed joint mapping proving conditional SRSWOR). This is a WP-3 design obligation; WP-10 owns the exact domain-byte encoding and implementation.

   The sentence “One orientation per sampled block observes exactly the estimand” is also false outside census. A sampled block reveals the orientation-specific block outcome entering the estimator; the stratified sample estimator is design-unbiased for the full-frame `theta(r)`, but does not observe it exactly. OR-2 needs its estimator and conditional variance displayed explicitly. The vector must be derived and sealed after the scientific lock and C-root creation, before sample membership is derived and before any C trajectory; it and the sample are one non-redrawable C design realization. This closes Sol finding 2/R3 only after the bounded replacement below.

2. **The Q information-boundary sentence narrows `H_preC` ambiguously and omits the competence binary by name.** At `...V2_DRAFT.md:301-307`, the charter requires `H_preC` to contain the complete committed T/Q attempt, validity, released-output, stopping, and promotion history. Saying Q contributes to it “only” the promoted identity and validity-qualified selection history can be read as excluding required attempt/depletion lineage. Conversely, “pass direction” is not the Q quantity: Q has a competence pass/fail binary. The scientific rule is that the complete history remains hashed and conditioned on, while the binary is usable only to perform automatic first-valid promotion and cannot tune or evidence C. The replacement below preserves automatic promotion without laundering Q into planning.

## Minor

None beyond the exact wording folded into the two Major repairs.

# Independent arithmetic confirmation

With `p(h,j)=5(h-1)+j` and
`b_{h,j}={n0+2[p(h,j)-1], n0+2[p(h,j)-1]+1}`, the v2 values recompute as follows:

| Quantity | CH-2a C-rich | CH-2b Q-rich |
|---|---:|---:|
| `J_C` | `{1,3,5}` | `{3,5}` |
| `J_Q` | `{2,4}` | `{1,2,4}` |
| `N_h` | 3 | 2 |
| `N_C` | 12 | 8 |
| `q_h=2|J_Q|` | 4 | 6 |
| total Q reserve | 16 | 24 |
| `W_h=N_h/N_C` | 1/4 | 1/4 |
| `pi_h` | `n_h/3` | `n_h/2` |
| FPC | `1-n_h/3` | `1-n_h/2` |
| point-estimation `n_h` | 1, 2, 3 | 1, 2 |
| claim-capable without special `n_h=1` method | 2, 3 | 2 |
| census | `n_h=3` in every stratum | `n_h=2` in every stratum |

For LOW x C-rich, Q is
`{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}` and C uses block positions
`{1,3,5,6,8,10,11,13,15,16,18,20}`. For LOW x Q-rich, Q is
`{26,27,28,29,32,33,36,37,38,39,42,43,46,47,48,49,52,53,56,57,58,59,62,63}` and C uses block positions `{3,5,8,10,13,15,18,20}`. The sets are disjoint and cover the selected 40-world band in both branches. Replacing `n0=26` by `126` gives the high-band designs without changing any count or weight.

The census statement is exact only for the selected finite frame and the selected orientation/seed scope. Under OR-1, census removes block-sampling variance but not orientation variance. Under OR-2, census exactly identifies `theta(r)` conditional on the full realized vector; learner-seed uncertainty remains unless WP-9 conditions on fixed seeds or fully represents its locked seed law.

# Orientation audit

## OR-1

The displayed target and estimator at lines 316-320 are correct. Let
`Dbar_b=[D_b(0)+D_b(1)]/2`, `f_h=n_h/N_h`, and
`sigma^2_{R,b}=[D_b(0)-D_b(1)]^2/4`. Then

`Var(theta_hat)=sum_h W_h^2[(1-f_h)S^2_{Dbar,h}/n_h + (1/(n_h N_h))sum_{b in F_h}sigma^2_{R,b}]`.

The scaling at lines 321-323 is therefore correct: the expected conditional orientation contribution is `sum sigma^2/(n_h N_h)`, not an FPC-adjusted term. One orientation per sampled block cannot identify that component separately. The WP-9 obligation to use a conservative bounded route, a properly declared replicated-orientation design, or a randomization-exact method is correctly placed. The common domain-separation sentence required below should cover OR-1 as well, implementing its already stated independence rather than changing the estimand.

## OR-2

After the bounded repair, the population is the selected public C block frame endowed with the complete post-lock vector `r`; its finite values for a locked contrast are `{D_b(r_b):b in F}`. The estimand is conditional on `r`, `H_preC`, `d*`, `s*`, `L*`, the selected frame, and the WP-9 learner-seed scope. The sealed `C_design_realization_id` binds the vector without replacing the pre-C `selection_scope_id`. The sample remains stratified SRSWOR from that oriented finite frame. Distinct orientation/sample root domains are scientifically load-bearing because the claim conditions on `r`; the obligation belongs in WP-3, while exact tags and implementation belong in WP-10.

# Typed observation and small-stratum audit

`(X,Delta)` at lines 27-35 is a proper tagged observation: certification exactly at `B` has `(B,1)`, while censoring at `B` has `(B,0)`. V2 does not prematurely select a numeric endpoint. Every later use of a mean or difference is explicitly a WP-9-locked numeric `D_b(r)`, not arithmetic on the typed pair. R4 is closed.

The table and lines 133-141 correctly distinguish point identification at `n_h=1` from claim-bearing inference. Undefined variance cannot be serialized or narrated as zero. A special bounded/randomization-exact WP-9 method is mandatory if `n_h=1` survives; otherwise `n_h>=2`. This is exact finite-frame logic, not a t/asymptotic guarantee. R5 is closed.

# Q transport, depletion, and evidentiary scope

The dedicated premise at lines 283-300 is sufficient for **target-side spendability only** as an explicitly author-accepted relevance assertion. It does not identify exchangeability, a C mean, donor/yoke validity, orientation behavior, or a treatment contrast. The separate non-outcome engineering validation is correctly required by WP-3 and implemented/tested later by WP-4 and the pre-C WP-9/WP-10 gate. Its content is not a Q scientific outcome.

The premise is load-bearing and therefore correctly requires
`I_ACCEPT_OFFICINA_Q_TO_C_TARGET_COMPETENCE_TRANSPORT_PREMISE`; generic contract acceptance must not hide it. Refusal makes the signed T/Q/C spend architecture unusable as designed and correctly routes to an author-signed charter-level redesign, never to a Q/C scientific terminal or a programme result.

The constraints `sum_l m_{l,h}<=q_h` and `sum_{l,h}m_{l,h}<=|Q|` are correct. `P_{Q,l}` is appropriately conditional on prior history, remaining worlds, frozen candidate/stack, and attempt id. Every charged invalid launch burns its planned worlds, id, cap slot, and error allocation; no failure or relabel can replenish them. Full-stratum-coverage ceilings are four and six, while any pooled/staggered schedule and its conditional family guarantee remain WP-6 obligations. E2=12 remains only a canonical-candidate registration cap. The signed automatic first-valid promotion rule remains governing and v2 creates no discretionary winner selection.

After the information-boundary replacement below, complete Q lineage stays inside `H_preC`, but no Q quantity beyond the mechanical first-valid-pass routing fact and promoted manifest can affect C planning or evidence. Label-free resource telemetry remains limited to engineering caps.

# Multiplicity and claim boundary

Lines 360-368 correctly assign a claim-bearing stratum statement to the family of the claim it supports. Descriptive strata cannot become inferential through p-values, claim-capable intervals, thresholds, directional emphasis, selective emphasis, or subgroup narration. The phrase “directional emphasis” already covers selective directional highlighting; adding “selective” explicitly is optional, not a blocker. R8 is closed.

Lines 239-252 correctly limit design-based generalization to the selected registered C frame. Weights do not repair public-frame tailoring, adaptive candidate selection, Q depletion, deterministic partitioning, or excluded worlds. Conditional on the complete pre-C selection history and an independent post-lock C design, inference remains about the selected design on that exact frame, not a learner class or construct superpopulation. R9 and findings 11-12 are closed.

# Closure table for Sol findings 1-12 and R1-R10

| V1 item | V2 disposition |
|---|---|
| Finding 1 / R1 | Closed: corrected memberships, generic formula, regression vectors, fail-closed disjointness/coverage checks. |
| Finding 2 / R3 | **Not yet closed:** OR-1 is correct; OR-2 needs conditional-SRS domain/order, estimator, and variance wording. |
| Finding 3 / R4 | Closed: typed `(X,Delta)` and deferred numeric functional. |
| Finding 4 / R2 | Closed: both CH-2 target measures are branch-complete. |
| Finding 5 / R5 | Closed: `n_h=1` cannot borrow zero/undefined variance. |
| Finding 6 / R7 | Closed: dedicated fixed-frame target-competence transport premise and non-outcome machinery gate. |
| Findings 7-8 / R6 | Substantively closed; the complete-history wording requires the bounded clarification below. |
| Finding 9 / R8 | Closed: multiplicity follows the claim family; descriptive strata are non-inferential. |
| Finding 10 / R1 | Closed: `n0` parameterizes both bands. |
| Finding 11 / R10 | Closed: recommendations have structural/resource provenance only. |
| Finding 12 / R9 | Closed: exact selected-frame boundary and non-adjustment list. |

# Exact mandatory bounded correction

1. Insert before the OR alternatives in §8:

> **Common C-randomization protocol:** The block sample and every orientation realization are derived from the same post-lock secret C root under distinct typed PRF domains whose exact byte encodings are locked and reviewed at WP-10. The joint mapping must make the stratum sample SRSWOR and independent of orientation randomization; under OR-2 this requires `Pr(S_h=s | r)=1/binom(N_h,n_h)` for every eligible `s`. Under OR-1, the sample is derived under the sample domain and fair bits for sampled blocks under the independent orientation domain. Under OR-2, the complete orientation vector is derived and sealed first under the orientation domain, then sample membership is derived under the sample domain. Both components become one durable, sealed, non-redrawable `C_design_realization_id` before any C trajectory; any failure does not authorize a redraw.

2. Replace OR-2's sentences from “Before/with C sampling” through “census FPC = 0 is then exact for `theta(r)`” with:

> After the scientific lock and C-root creation, and before C sample membership or any trajectory, the full-frame orientation vector `r in {0,1}^{N_C}` (ascending block `p`) is derived, sealed, and bound into `C_design_realization_id` under the common protocol above. The target is `theta(r)=sum_h W_h(1/N_h)sum_{b in F_h}D_b(r_b)`, and the public claim is explicitly conditional on that sealed vector. Conditional on `r`, `theta_hat(r)=sum_h(W_h/n_h)sum_{b in S_h}D_b(r_b)` is design-unbiased, with `Var[theta_hat(r)|r]=sum_h W_h^2(1-f_h)S^2_{D(r),h}/n_h`; each sampled block reveals its orientation-specific contribution, not the full-frame estimand. Ordinary SRSWOR variance estimation is available subject to §2b's small-stratum rule, and census FPC zero is exact for `theta(r)` subject to the locked learner-seed scope.

3. Replace §7's information-boundary paragraph with:

> **Information boundary:** `H_preC` retains and hashes the complete charter-required Q attempt, validity, released-output, stopping, depletion, and promotion history. For downstream routing and design identity, Q may contribute only the mechanical fact that the first valid `Q_PASS` occurred and the exact automatically promoted candidate/stack identity; neither fact is C evidence. The competence binary is used only for that routing; it, Q-world identities, responses, estimates, variances, depletion history, and every other scientific Q quantity may not tune C sample size, endpoint, margins, population, or analysis and may not enter C evidence. Predeclared label-free resource telemetry may inform engineering caps only.

These sentences close the defect without selecting OR-1 or OR-2, choosing a root value or domain-byte encoding, changing a frame, or moving a WP-6/WP-9 numeric.

# Direct answers to Fable's three Sol questions

1. **Orientation:** OR-1's target, estimator, two-component variance, non-identifiability caveat, census rule, and WP-9 obligation are correct. OR-2's target and conditional scope are sound, but its estimator/order/domain-independence surface is incomplete and one sentence overstates sample observation. The exact bounded correction above is required; no orientation option is rejected or selected.
2. **Q depletion and transport:** The inequalities, attempt-indexed measure, charged-invalid depletion, withdrawn eight-launch example, dedicated token, and licensed/not-identified lists land R6/R7. The engineering-validation requirement is at the correct WP-3 ownership level with later implementation/gate ownership. The `H_preC`/binary wording needs the exact clarification above.
3. **Typed outcome, small strata, boundary, and multiplicity:** Yes. `(X,Delta)` remains nonnumeric until WP-9; no later sentence averages it. `n_h=1` has no zero-variance escape. The selected-frame boundary is exact, and no C2-C5 stratum claim is absorbed into C1.

# Token eligibility and authorization boundary

The complete five-token packet is correctly exposed as: contract acceptance, exactly one CH-1 token, exactly one CH-2 token, exactly one OR token, and the dedicated transport token. LOW, C_RICH, the conditional OR option, and transport acceptance are recommendations with pre-data arithmetic/resource/governance provenance only; none uses a stopped-line outcome. The packet is **not yet eligible** for Kirill because the OR-2 and information-boundary corrections require another focused X/Y confirmation. No additional author token is needed after those bounded repairs.

This review authorizes only the three bounded replacement clauses above and another focused confirmation. It authorizes no token, author selection, WP-4, entropy, T activation, world or frame realization, sample, panel, candidate, ledger event, Q/C process, root, lock, escrow, datum, outcome, or claim movement. T remains `NOT_ACTIVATED`. No qualification, contrast direction, or programme success is predicted.
