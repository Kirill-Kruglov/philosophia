REVISE_OFFICINA_WP3_CONTRACT

# Scope and basis

I reviewed the WP-3 draft at `2bc781d` against the signed charter, v2.1 correction, charter signature, author selections, WP-1/WP-2 closure, and Fable's closure memo. The load-bearing files at the working HEAD are unchanged from `2bc781d`; the committed delta after that anchor contains review prompts only. The inactive bootstrap verifier returned `OK: Officina WP-1/WP-2 bootstrap is quarantined and inactive.` `git diff --check 2bc781d..HEAD` found only a trailing blank line in the review-only Opus prompt, not in this contract or a governing artifact.

The fixed-finite-frame probability-sample interpretation is coherent in principle. This draft is not ready for author selection because its normative frame membership is internally contradictory, one CH-2 branch is not instantiated in the target measure, and neither the orientation-dependent estimand nor its design variance is defined. These are bounded pre-data repairs, not a reason to block Route B.

# Ordered findings

## Critical

1. **The printed Split-1 Q reserve is wrong and is not disjoint from the printed C frame.** The governing rule at `OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V1_DRAFT.md:108-119` gives `b_p={24+2p,25+2p}`, C positions `j={1,3,5}`, and Q positions `j={2,4}`. The resulting Q worlds are
   `{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}`,
   not the list at line 119. The printed list includes C blocks at `p=8,10,13,15,18,20` and omits six actual Q blocks. Consequently, the current canonical frame document cannot be reproduced consistently; the Q/C disjointness assertion, reserve arithmetic, frame hash, and any future generator refusal rule have no unique referent. No author token is signable while this contradiction remains.

2. **The elementary unit and orientation estimand are not defined consistently.** Lines 25-30 call `b_p` an ordered pair, serialize it as an unordered set, and then randomize which member is target. Lines 139-150 add an orientation bit without saying whether the finite-population quantity is conditional on that realized bit or averaged over both orientations. Lines 196-199 therefore do not name one estimand. The scientifically natural frame unit here is an unordered adjacent block, followed by a second-stage target/donor orientation randomization. For a locked numeric arm contrast `D_b(r)`, the orientation-averaged block effect is `Dbar_b={D_b(0)+D_b(1)}/2`. One independent fair orientation per sampled block makes the proposed estimator unbiased for the mean of `Dbar_b`, but does not reveal both potential orientations and therefore does not identify the orientation-randomization variance from the observed blocks alone. WP-3 must choose, with explicit author assent, between an orientation-averaged two-stage estimand with a valid conservative/replicated-orientation variance route and a finite-frame estimand conditional on a root-fixed orientation vector. Calling the bit merely “part of the design” is insufficient.

3. **The stated censored outcome is not a numeric object on which means and differences are defined.** Lines 38-40 and 65 use `[0,B] U {censored-at-B}` while lines 196-199 take weighted means and arm differences. The value `B` and the tagged censoring event are distinct scientific states, but the current notation neither makes that tagged union explicit nor defines its numeric functional. WP-3 should freeze only a typed terminal observation, such as `(X,Delta)` with `X=min(T,B)` and `Delta=1[T<=B]`, preserving achievement exactly at `B` separately from no achievement by `B`. WP-9 must still own the certificate, `B`, the numeric endpoint functional (including any restricted-mean functional), direction, margins, and analysis. Until that mapping is locked, `Y_a` cannot be averaged.

## Major

4. **The C target-measure section is CH-2a-only although CH-2b is a live author choice.** Lines 137-163 and 223-228 hard-code `N_h=3`, a 12-block frame, `pi_h=n_h/3`, and FPC `1-n_h/3`. Under CH-2b at lines 321-326, `N_h=2`, the C frame has eight blocks, `pi_h=n_h/2`, and FPC `1-n_h/2`. Both branches retain `W_h=1/4`. A future signature selecting CH-2b would otherwise accept mutually inconsistent normative cells.

5. **`n_h=1` is presented as unconditionally inferentially usable.** Lines 143-150 list it beside ordinary design weights and FPC. It gives an unbiased stratum-mean point estimate, but the within-stratum sample variance is undefined, not zero. With `N_h=2`, `n_h=1` leaves no degrees of freedom and no ordinary design-based variance estimate; with `N_h=3` the same issue remains. At census, sampling variance is exactly zero only for the finite set of outcomes actually defining the estimand. It is not evidence of homogeneous effects and does not remove orientation or learner-seed randomization unless the claim conditions on their realized values. WP-3 need not choose WP-9's final `n_h`, but it must state that ordinary variance-estimated inference requires `n_h>=2` in each non-census stratum. If WP-9 retains `n_h=1`, it must predeclare a bounded/randomization-exact confidence procedure that does not estimate a one-observation variance. A t or asymptotic interval is an approximation, not an exact finite-frame consequence.

6. **The Q-to-C premise is not yet sufficient to make C spendable.** Lines 177-192 call fixed, publicly enumerated moduli “within-stratum exchangeable.” There is no probability law under which those fixed Q worlds are exchangeable with the distinct fixed C blocks; this is an untestable relevance/transport assertion, not a consequence of SRSWOR or interleaving. Moreover, Q observes a target learner on single worlds while C first introduces orientation, donor generation, yoking, and paired treatment machinery. A valid Q pass can license target-side spend only if Kirill explicitly accepts the transport premise, WP-6 makes its competence guarantee cover the locked C strata/support, and separate non-outcome engineering validation establishes that the donor/yoke machinery is executable. The Q binary may enter `H_preC` and trigger automatic promotion, but no Q-world identity, response, estimate, variance, or pass status may enter a C estimate, margin, sample-size choice, endpoint choice, or evidentiary narrative. Predeclared label-free resource telemetry may inform engineering caps only, as the charter already permits; it is not scientific evidence.

7. **The Q reserve constraint is not branch-complete and its example is mathematically ambiguous.** Lines 166-175 assume 16 worlds and reduce feasibility to `launches x sample size <= 16`. The exact constraints are per stratum and per launch: if attempt `ell` consumes `m_{ell h}` worlds from stratum `h`, then `sum_ell m_{ell h} <= q_h` for every `h`, as well as the total constraint. Here `q_h=4` under CH-2a and `q_h=6` under CH-2b. A two-world sample cannot cover four strata, so it cannot be called stratum-spanning in the ordinary sense. If every qualifying attempt must cover every stratum, the absolute launch ceilings are four and six, not eight and twelve. If WP-6 uses a different pooled or staggered coverage design, it must define that design and prove the family false-pass guarantee conditional on the complete adaptive/depletion history. E2=12 is a candidate-registration ceiling, not a promise that twelve candidates can each receive Q data. Neither CH-2 branch is intrinsically infeasible, but feasibility depends on later caps and the exact `m_{ell h}` schedule.

8. **Global adaptive depletion needs an attempt-indexed Q measure.** Lines 166-170 describe one uniform `P_Q` while earlier attempts remove worlds and their terminal identities may become public. A later candidate is sampled from a history-dependent remaining set, not from the original 16- or 24-world measure. WP-6 must define `P_{Q,ell}` conditional on `H_{<ell}`, the remaining registry, the frozen candidate/stack, and the attempt id; charge every launch; and show that its competence null, alpha spending, and Q-to-C transport statement hold under every admissible depletion history. No retry, candidate relabel, invalid launch, or root failure may replenish a world or error allocation. This prices adaptive T selection without silently changing the selected-design C estimand.

9. **The stratum multiplicity rule is overbroad across claims and underexplicit about descriptions.** Lines 200-209 correctly require pre-data ownership, but “any claim-bearing use of this frame's strata ... belongs to C1” would wrongly absorb a later C2-C5 stratum claim into C1 merely because it reused a descriptive world label. Family ownership follows the claim and endpoint: C1 interactions belong to C1; a registered C2-C4 or C5 interaction belongs to its charter-owned family. Descriptive stratum summaries must be locked in form and labeled non-inferential; they cannot carry p-values, claim-capable intervals, threshold language, direction-selective emphasis, or post-hoc subgroup narration.

10. **The high-band CH-1 option lacks a branch-complete enumeration formula.** Lines 89-91 say later text “scales,” but lines 105-119 hard-code the low-band offset. The generic formula below must govern both `[26,65]` and `[126,165]`; otherwise CH-1b does not determine a byte-reproducible frame. This is a specification defect, not evidence against either band.

## Minor

11. The CH-1 recommendation at lines 315-319 has valid non-outcome provenance as a word-length/resource-planning argument, not an expected-success argument. The CH-2 recommendation at lines 328-331 also has permissible structural provenance in principle, but its “about eight launches” rationale depends on the defective two-world example and must be withdrawn or made conditional on the eventual WP-6 sampling schedule. Neither recommendation is empirically selected by predecessor outcomes.

12. The public deterministic Q/C partition creates no design bias for an estimand defined only on the registered C frame: conditional on `H_preC`, the frozen candidate and stack, and the locked design, an independent post-lock C sample still supports design-based inference to that frame. It does create a finite-frame selection boundary: a candidate may be adapted to the public construct, strata, and even the full public C-frame support. C sampling weights correct only unequal C inclusion; they do not correct candidate selection, public-frame tailoring, or deterministic exclusion of Q/T/other moduli. The selected-design condition and forbidden wider claims at lines 151-155 and 223-236 must remain loud.

# Correct branch-complete frame and design formulas

Let `n0` be the selected lower endpoint (`26` or `126`), let
`p(h,j)=5(h-1)+j` for `h in {1,2,3,4}` and `j in {1,...,5}`, and define the unordered block

`b_{h,j}={n0+2[p(h,j)-1], n0+2[p(h,j)-1]+1}`.

Then the two CH-2 branches are:

| Quantity | CH-2a, C-rich | CH-2b, Q-rich |
|---|---:|---:|
| C positions `J_C` | `{1,3,5}` | `{3,5}` |
| Q positions `J_Q` | `{2,4}` | `{1,2,4}` |
| C blocks per stratum `N_h` | `3` | `2` |
| total C blocks `N_C` | `12` | `8` |
| Q worlds per stratum `q_h=2|J_Q|` | `4` | `6` |
| total Q worlds | `16` | `24` |
| C stratum weight `W_h=N_h/N_C` | `1/4` | `1/4` |
| admissible point-estimation sizes | `1<=n_h<=3` | `1<=n_h<=2` |
| first-stage claim-capable sizes without a special `n_h=1` method | `2<=n_h<=3` | `n_h=2` |
| first-order C inclusion probability | `pi_h=n_h/3` | `pi_h=n_h/2` |
| sampling FPC | `1-n_h/3` | `1-n_h/2` |
| analysis coefficient per sampled block | `W_h/n_h` | `W_h/n_h` |

For the low-band branch, the exact memberships are:

- CH-2a C block positions: `p={1,3,5,6,8,10,11,13,15,16,18,20}`. Q worlds:
  `{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}`.
- CH-2b C block positions: `p={3,5,8,10,13,15,18,20}`, namely blocks
  `{30,31}`, `{34,35}`, `{40,41}`, `{44,45}`, `{50,51}`, `{54,55}`, `{60,61}`, `{64,65}`. Q worlds:
  `{26,27,28,29,32,33,36,37,38,39,42,43,46,47,48,49,52,53,56,57,58,59,62,63}`.

The same `p(h,j)` formula, with `n0=126`, uniquely defines the high-band memberships without another hand-copied list.

# Orientation randomization and variance

For any WP-9-locked numeric contrast, write `D_b(r)` for the block contrast when orientation `r` chooses the target. If the author selects the orientation-averaged estimand, the finite-frame target is

`theta = sum_h W_h (1/N_h) sum_{b in F_h} Dbar_b`, where `Dbar_b={D_b(0)+D_b(1)}/2`.

With `S_h` drawn by SRSWOR and independent `R_b~Bernoulli(1/2)`, the estimator

`theta_hat = sum_h (W_h/n_h) sum_{b in S_h} D_b(R_b)`

is design-unbiased. Its design variance has both components:

`Var(theta_hat)=sum_h W_h^2[(1-f_h)S^2_{Dbar,h}/n_h + {1/(n_h N_h)}sum_{b in F_h} sigma^2_{R,b}]`,

where `f_h=n_h/N_h` and `sigma^2_{R,b}={D_b(0)-D_b(1)}^2/4`. One observed orientation per sampled block cannot estimate the second term without additional assumptions or a conservative bound. At a block census the first term is zero, but the second is not zero unless the claim conditions on a root-fixed orientation vector or both orientations are observed. Learner-seed randomization, if selected at WP-9, adds its own locked averaging/conditioning scope; an FPC does not remove it.

Therefore one orientation per block identifies the orientation-averaged point estimand only in the design-unbiased sense. WP-3 must explicitly lock the target and require WP-9 to own a valid variance/confidence method. It may instead present a bounded author choice for a conditional realized-orientation estimand, but that alternative must define the full-frame orientation vector before C sampling, bind it to a sealed `C_design_realization_id`, and limit the final claim to that oriented frame while retaining the pre-C `selection_scope_id`. The two meanings cannot be mixed.

# Q spendability answer

The present premise is not sufficient by itself. Interleaving fixed moduli is a transparent reason to propose transport, but does not prove exchangeability. A future non-comparative Q pass may license C spend without becoming C evidence only when all of the following are locked before the first Q launch:

1. an author-accepted target-side Q-to-C relevance/transport premise for every C stratum and every admissible depletion history;
2. one candidate-blind competence null, certificate, horizon, aggregation, sample design, false-pass guarantee, and stratum-support rule applying to the exact frozen candidate and stack;
3. automatic first-valid promotion with all Q information excluded from C planning and estimation, except the identity of the mechanically promoted design and its validity-qualified stack;
4. non-outcome engineering validation of orientation, donor, yoke, persistence, and arm-construction machinery before C authorization.

Q then establishes only that the selected target learner met the preregistered Q assurance rule on its Q design. It does not test a treatment contrast, donor validity as a scientific effect, the C endpoint, or any C-frame mean. A valid Q pass is part of selection history, not part of the C evidence.

# Exact mandatory repairs

R1. Replace the low-band hand list and every branch-specific hard-coded offset with the generic `n0`, `p(h,j)`, and `b_{h,j}` formulas above; print and test the exact low-band CH-2a and CH-2b memberships. State that Q and C are disjoint by those computed sets, not by prose.

R2. Replace lines 137-163 and 223-228 with the branch table above. Bind the selected CH-2 token into `officina.frame.v1`, its hash, `N_h`, `N_C`, `q_h`, `W_h`, `pi_h`, FPC, and claim-scope text.

R3. Replace “ordered pair” with “unordered adjacent block” and add an author-visible orientation-estimand cell. If orientation averaging is selected, insert the two-stage estimand, estimator, and two-component variance obligation above. If realized-orientation conditioning is selected, specify when all frame orientations are fixed, how they are hashed, and that the claim conditions on them. Require an explicit token for the selected meaning.

R4. Replace `[0,B] U {censored-at-B}` with the typed observation `(X,Delta)` described above. State exactly: “WP-3 fixes the observation type only. WP-9 owns the certificate, budget, numeric functional, arm contrasts, margins, and inferential method; no mean or difference is defined until that mapping is locked.”

R5. Qualify the `n_h` cell exactly: “`n_h=1` supports a design-unbiased point estimate but no within-stratum sample-variance estimate. Claim-bearing inference with `n_h=1` requires a WP-9-locked bounded/randomization-exact method that does not substitute zero variance; otherwise every non-census stratum requires `n_h>=2`. Census FPC zero is a sampling fact only.”

R6. Replace the launch-product inequality with `sum_ell m_{ell h}<=q_h` for each stratum and `sum_{ell,h}m_{ell h}<=|Q|`; define what “balanced” or “scale-spanning” means. Require WP-6 to condition its test and alpha spending on `H_{<ell}`, candidate/stack, remaining worlds, attempt id, and every charged invalid launch. Remove the unconditional eight-launch example unless its sampling schedule actually proves the stated coverage and transport guarantee.

R7. Replace “within-stratum exchangeability” with “author-accepted fixed-frame target-competence transport premise.” State that it is neither design-identified nor tested by Q, and that C spend additionally requires non-outcome validation of donor/yoke machinery. Add a dedicated author token for this premise.

R8. Replace lines 207-209 with: “A claim-bearing stratum or interaction statement is assigned before data to the multiplicity family of the claim it supports: C1 for C1 contact claims, the C2-C4 family for those cascade claims, C5 for path-credit claims, and the separately controlled C6 family for any inferential C6 annotation. Unregistered and post-hoc subgroup claims are forbidden; locked descriptive summaries are non-inferential.”

R9. Add to the claim boundary: “The deterministic partition and public finite frame are conditioned-on design facts. C weights generalize only over the selected registered C frame and do not adjust for candidate selection, Q depletion, public-frame tailoring, or exclusion of Q, T, predecessor, and unenumerated worlds.”

R10. Correct the CH-2 recommendation rationale so it uses only branch-complete, explicitly conditional reserve arithmetic. Preserve the CH-1 non-outcome planning provenance and forbid any expected-qualification or expected-effect reading.

# Author cells and selection disposition

CH-1 and CH-2 are legitimate pre-data scientific choices, and their recommendations have non-outcome provenance: CH-1 trades word scale against the already signed resource envelope; CH-2 trades C-frame size against a finite Q reserve. They select no learner and use no predecessor outcome. However, neither token is eligible now because the artifact each would accept is internally inconsistent.

The repaired packet needs explicit author acceptance of both load-bearing assumptions. The least ambiguous additions are:

```text
I_ACCEPT_OFFICINA_Q_TO_C_TARGET_COMPETENCE_TRANSPORT_PREMISE
I_SELECT_OFFICINA_ORIENTATION_AVERAGED_BLOCK_ESTIMAND
```

If Fable instead offers a conditional realized-orientation estimand, the second token must name that alternative exactly. These meanings may be incorporated verbatim into an expanded contract-acceptance token, but a generic acceptance sentence must not hide them. After bounded revision and renewed X/Y confirmation, and not before, the eligible packet would be the repaired contract token, exactly one CH-1 token, exactly one CH-2 token, the transport assent, and exactly one orientation-estimand token.

# Negative space and authorization

This verdict authorizes only a bounded Fable revision addressing R1-R10 and a later bounded confirmation. It does not authorize author selection, WP-4, entropy, a root, world generation, frame or Q realization, sample, panel, candidate, ledger event, T activation, T/Q/C process, learner/device choice, WP-6 numerics, WP-9 numerics, lock, escrow, datum, outcome, or claim movement. T remains `NOT_ACTIVATED`. No qualification, contrast direction, or scientific outcome is predicted. T and Q remain permanently non-citable for C1-C6; only a valid independently locked C execution could move a claim within the selected-design, selected-frame, orientation, device, and learner-seed scope.
