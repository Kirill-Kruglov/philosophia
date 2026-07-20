OFFICINA_WP3_V2_1_YLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE

# Literal bounded confirmation

I compared the complete v2.1 replacement at `237e65b` with v2, both focused v2 confirmations, Fable's v2.1 closure, and the signed charter. The committed delta `237e65b..HEAD` contains only the two final-confirmation prompts; the contract is unchanged. The inactive verifier returned `OK: Officina WP-1/WP-2 bootstrap is quarantined and inactive.` `git diff --check 237e65b..HEAD` reports only a trailing blank line in the review-only Opus prompt, not a contract or governing-artifact defect.

The two Y-line repairs landed in substance exactly, and the other v2→v2.1 changes are limited to Opus's bounded wire-classifier, path/hash, and T-dev wording corrections plus the necessary ownership/handoff bookkeeping. No previously accepted scientific or statistical cell is reopened or changed.

## 1. Common C-randomization protocol

Confirmed at `OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md:380-395`:

- one post-lock secret C root is used through distinct typed PRF domains for sample and orientation derivation;
- the design requires sample/orientation independence, not merely different labels on two root functions;
- under OR-2, the complete orientation vector is derived and sealed first, followed by sample membership;
- the vector and sample form one durable, sealed, non-redrawable `C_design_realization_id` before any C trajectory;
- any failure authorizes no redraw;
- WP-3 owns independence, order, and non-redraw, while WP-10 owns exact domain-byte tags and implementation after lock.

For fixed stratum size `n_h`, the displayed condition

`Pr(S_h=s | r)=1/binom(N_h,n_h)` for every eligible `s`

is correctly conditioned on the **entire** realized orientation vector `r`, not merely `r_h`, and is sufficient for the required orientation/sample independence at the stratum level. It is read together with the already normative “stratified SRSWOR” design in §6, whose standard joint meaning is independent SRSWOR across strata. Equivalently, the implementation must realize

`Pr(S_1=s_1,...,S_4=s_4 | r)=product_h 1/binom(N_h,n_h)`

for eligible stratum samples. That joint factorization is not a new cell; it is the existing stratified-SRSWOR requirement that makes the sum-of-stratum-variances formula valid. WP-10 must demonstrate the mapping, but may not choose a different sampling law. No further WP-3 sentence is required.

## 2. OR-1

Confirmed. OR-1's target, estimator, two-component variance, inability to estimate the orientation component from one orientation per block, WP-9 variance-route obligation, and census limitation are unchanged. Lines 399-401 only bind its already-required independent fair bits and SRSWOR sample to the common typed-domain protocol. No OR-1 estimand, variance scaling, resource consequence, or token changed.

## 3. OR-2

Confirmed at lines 415-435. Once the full vector `r` is realized, the fixed finite population is the selected C frame endowed with values `{D_b(r_b): b in F}`. The target is

`theta(r)=sum_h W_h(1/N_h)sum_{b in F_h}D_b(r_b)`.

Conditional on `r`, the estimator

`theta_hat(r)=sum_h(W_h/n_h)sum_{b in S_h}D_b(r_b)`

is design-unbiased. Under independent stratified SRSWOR its variance is correctly displayed as

`Var[theta_hat(r)|r]=sum_h W_h^2(1-f_h)S^2_{D(r),h}/n_h`.

The orientation vector is derived after the scientific lock and C-root creation, before sample membership and every trajectory. It is sealed into `C_design_realization_id` without replacing the pre-C `selection_scope_id`, and the public claim is conditional on it. The text now correctly says a sampled block reveals only its orientation-specific contribution, not the full-frame estimand.

Ordinary variance estimation remains subject to §2b: `n_h=1` cannot supply a within-stratum variance and needs the separately locked bounded/randomization-exact route; otherwise `n_h>=2`. Census FPC zero is exact for `theta(r)` only within the selected oriented finite frame and locked learner-seed scope. It does not create a learner-class or superpopulation claim.

## 4. Complete `H_preC` and Q information boundary

Confirmed at lines 358-371. The phrase “complete charter-required” preserves the signed charter's full `H_preC` object rather than redefining it: the committed T/Q registry and attempt, validity, released-output, stopping, depletion, and promotion history remain retained, hashed, conditioned on, and auditable.

For downstream routing and design identity, Q contributes only the mechanical first-valid-`Q_PASS` fact and the exact automatically promoted candidate/stack. Neither is C evidence. The competence binary is explicitly routing-only. Q-world identities, responses, estimates, variances, depletion history, and every other scientific Q quantity cannot tune C sample size, endpoint, margins, population, or analysis and cannot enter C evidence. The sole preserved exception is the charter's predeclared label-free resource telemetry for engineering caps only.

This closes the former `H_preC` narrowing and the erroneous “pass direction” terminology without changing automatic promotion, Q depletion, transport, or selection-conditional inference.

## 5. Five-token packet

The packet remains complete and unchanged:

```text
I_ACCEPT_OFFICINA_WP3_POPULATION_CONTRACT
I_SELECT_OFFICINA_FRAME_BAND_LOW | I_SELECT_OFFICINA_FRAME_BAND_HIGH
I_SELECT_OFFICINA_SPLIT_C_RICH | I_SELECT_OFFICINA_SPLIT_Q_RICH
I_SELECT_OFFICINA_ORIENTATION_AVERAGED_BLOCK_ESTIMAND |
  I_SELECT_OFFICINA_ORIENTATION_CONDITIONAL_FIXED_VECTOR_ESTIMAND
I_ACCEPT_OFFICINA_Q_TO_C_TARGET_COMPETENCE_TRANSPORT_PREMISE
```

This exposes contract acceptance, exactly one CH-1 choice, exactly one CH-2 choice, exactly one orientation estimand, and the dedicated Q-to-C transport premise. The shared randomization protocol is a common design-validity obligation accepted by the contract token, not another scientific choice; no new author token is needed.

The complete five-token packet is eligible for Kirill's informed selection and signature. This verdict authorizes only those author tokens. It does not select an option for Kirill and does not authorize WP-4 or any downstream work.

## 6. Exact-delta and provenance confirmation

The v2→v2.1 diff changes only the five bounded correction families recorded by Fable:

1. Opus's total ordered oracle-wire classifier;
2. the corrected v1 path, exact acyclic `contract_sha256` definition, and softened T-dev characterization;
3. the common C-randomization protocol;
4. the corrected OR-2 conditional estimator/variance and realization wording;
5. the complete `H_preC` information boundary.

The associated §6 cross-reference, §9 ownership entries, front matter, and WP-4 handoff are mechanical propagation of those corrections. Frame membership, CH-1/CH-2 values, weights, inclusion probabilities, FPC, typed outcome, small-stratum rule, depletion arithmetic, transport premise, multiplicity, claim boundary, both OR choices, and all author tokens otherwise remain unchanged. No stopped-line outcome or comparative datum supplies any value, recommendation, or inference.

# Direct answers to Fable's two Sol questions

1. **Yes.** The common protocol and corrected OR-2 establish the required conditional SRSWOR, domain independence, orientation-first ordering, conditional estimator and variance, and contribution-only observation statement. The displayed per-stratum probability is sufficient in conjunction with the governing stratified-SRSWOR joint design.
2. **Yes.** The complete charter-required history remains in `H_preC`; only the mechanical first-valid-pass fact and promoted identity route downstream, neither is evidence, and the competence binary is named correctly and restricted to routing.

# Negative space

This confirmation creates and authorizes no WP-4 work, entropy, world, frame instance, sample, panel, candidate, manifest, ledger event, root, lock, escrow, T activation, T/Q/C process, learner run, datum, outcome, Proof, or claim movement. T remains `NOT_ACTIVATED`. The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; its records are non-citable and selected nothing here. Officina T and Q cannot earn, kill, or boundary-label C1-C6; a future Q pass is a spendability routing fact only. S remains unavailable. Only a valid independently locked C execution may move an Officina claim within its selection-conditional, selected-frame, orientation, device, and learner-seed scope. No qualification, contrast direction, or programme success is predicted.
