# Level 1 feasibility v2 — scientific-scope audit

`REVISE_LEVEL1_FEASIBILITY_V2_SCOPE`

## Ordered findings

1. **Critical — signed A6 parameter non-finiteness is not detected at the first
   non-finite learner state.** In `feasibility_committee_step`, `finite` is
   computed from the four CE losses before backward/AdamW. The optimizers then
   step, but no model-parameter finiteness check occurs before the function
   returns. `run_noncomparative_feasibility_v2` consequently may evaluate the
   dummy panel or begin the next oracle step after an optimizer-created
   non-finite parameter. At a checkpoint, `PanelObservation` can turn the
   resulting non-finite probability into an exception, producing process
   invalidity instead of the signed scientific non-finiteness terminal. At
   `B`, the run can also miss the mandatory non-finite diagnostic because no
   next loss exists to expose the bad parameter. This violates the A6
   loss/**parameter** routing and is the sole scope blocker.

2. **Major — subject to finding 1, the report surface is scientifically
   inert.** The production path contains one RANDOM-STATIC fixture, one
   four-member committee, one replicate, `pair_slot=0`, `n=66`, `B=2000`, and
   no scorer. The v2 report exposes only terminal/resource aggregates: latency
   count/mean/median/min/max, steps completed, finiteness/computability flags,
   the single binary, an in-memory checkpoint-size estimate, peak RSS, frozen
   lineage/cap fields, and contamination attestations. It persists no query,
   loss, score, solve, checkpoint, or panel-result series. Dummy-panel
   observations and qualifying checkpoints remain in memory. That binary
   surface is sufficient for the signed gate and insufficient for an arm or
   effect claim, as intended.

3. **Major — no field licenses an arm contrast, a v1/v2 effect, or learner
   tuning.** The v1 references in the claim/report are hashes used to reject
   lineage mutation; they do not import a v1 measurement into the v2 payload.
   The arm is fixed rather than selectable, `scorer_steps` is exactly zero, and
   the driver imports no contrast estimator or N3 selector. A reader can of
   course see both immutable binary records, but the signed contract and the
   explicit `v1_v2_contrast:false` attestation forbid estimating an improvement
   or treating the two different learner policies as an effect comparison.
   Latency, RSS, and size may support a separately signed resource decision;
   they cannot tune the learner, endpoint, B, margins, or pass criterion.

4. **Major — the amended learner-class description is honest and the code
   implements it.** `full_history_committee_step` stacks every item of the
   learner's own contact history in canonical order, uses mean CE, and takes one
   shared-batch update per member. The v2 path does not call replay or scoring.
   The signed amendment explicitly names temporal weighting, the new
   learner-class conditional estimand, and the fact that symmetric application
   prevents an arm-label implementation asymmetry without making the change
   neutral. It calls the change neither empirically selected nor predicted to
   pass, and distinguishes “no new numeric hyperparameter” from a substantive
   capacity/optimization-policy change.

5. **Major — resource reporting is dimensionally honest.** The executable v2
   report contains measured trajectory latency aggregates, peak RSS, and a size
   estimate; it contains no 31.51× capacity claim, Level 0 success claim, or
   projected solve probability. The amendment confines 31.51 to an
   example-evaluation compute-work ratio, keeps optimizer updates at 2,000, and
   labels 30 h as a linear-scaling planning projection rather than a bound. A
   36 h wall exception occurs before report installation and therefore cannot
   become censoring. Finding 1 concerns scientific parameter divergence, not
   the resource route.

6. **Major — the one-shot and lineage controls are adequate for the signed
   procedural threat model.** The driver requires a distinct tracked v2
   authorization, exact token/caps/world/path, clean tracked tree and empty
   index, `EXPECTED_HEAD == HEAD`, an empty canonical claim/report path, the
   signed amendments/signature hashes, exact immutable v1 hashes, and no named
   later-gate artifact. It compares the entire reviewed source-pin set against
   the authorization's reviewed commit. The claim is durably installed without
   replacement before the learner call; report installation occurs only after
   return from a valid scientific terminal. After-claim failure leaves the
   claim's binary status unset and makes the canonical path refuse another run.
   Deletion or malicious filesystem interference remains a procedural
   violation, not a claimed security guarantee.

7. **Minor — exact public-root environment equality is fail-closed but
   operationally over-specific.** The gate compares the whole recorded
   environment dictionary, including `platform.platform()` (kernel/glibc text)
   and `machine`, rather than only Python 3.12.3, Torch 2.9.1+cpu, CPU/float32,
   deterministic algorithms, and thread counts. Thus scientifically irrelevant
   host-metadata drift can cause an `ENVIRONMENT` refusal. This cannot create a
   false learner result: it occurs before claim/report creation and exposes no
   performance. It faithfully enforces the already signed exact-fingerprint
   contract, so it is not a scientific-inertness blocker. Any future desire to
   make the gate portable must be a signed bounded environment correction, not
   a silent implementation relaxation.

8. **Verification — reviewed source and lineage are intact.** Current HEAD
   `db9b39e75a93c47bb4d529a98cd314866fb8375f` has an empty diff from reviewed
   commit `d8c46637adf6f0caab039559c9031b1af65985b4` over the driver's complete
   source-pin set and `tests/test_level1_feasibility_v2.py`. The signature,
   v2/v2.1/v2.2 amendments, and both immutable v1 artifacts hash to the values
   embedded in the driver. The focused tests pass 9/9; the repository suite
   passes 152/152; the admitted-decision verifier reports the inherited and
   Level 0 decisions `VALID`. No v2 authorization, claim/report, or named
   later-gate artifact exists. The only untracked path is the user-owned
   `essay/OUTLINE.md`, which was not touched.

## Mandatory edits

1. Make the committee step's terminal finiteness result cover both the
   pre-update CE losses and every model parameter immediately after all AdamW
   steps. Perform that post-step scan before any dummy-panel evaluation or next
   oracle step. A post-step non-finite parameter must return the signed A6
   scientific non-finiteness state, not raise later from panel scoring.

2. Make the v2 terminal payload accurately attest parameter as well as loss
   finiteness—either with separate loss/parameter flags or one unambiguously
   named learner-state flag. Preserve the rule: an already completed qualifying
   window before the first non-finite state stands; otherwise the valid
   non-finite terminal is censored. Persist no non-finiteness series or exact
   checkpoint curve.

3. Add bounded tests for optimizer-created parameter non-finiteness (including
   at a checkpoint and at `B`), both with and without an earlier complete
   qualifying window. Assert that the result is a valid A6 scientific terminal,
   that panel evaluation never occurs after the first non-finite state, and that
   process/resource/hash/seal exceptions still install no report and leave the
   binary unset. Re-run the focused and full suites and perform another bounded
   source-scope review.

No endpoint, persistence rule, binary interpretation, resource cap, learner
policy, artifact path, or gate route is reopened by these edits.

## Allowed and forbidden interpretation table

| Terminal/state | Allowed narration | Forbidden narration |
|---|---|---|
| Valid pass (`censored_at_b:false`) | The one predeclared `n=66` RANDOM-STATIC fixture under the full-history learner completed at least one signed five-checkpoint qualifying window; comparative-scout **review** may be considered. | Level 1 result; evidence for RANDOM-STATIC, ACTIVE, YOKED, C1, an outcome world, or the programme; evidence that full history improved on v1; direct scout execution authorization. |
| Valid B censor (`censored_at_b:true`) | The same amended fixture reached B without a complete qualifying window; route to `BLOCKED_LEVEL1_FEASIBILITY`, with C1 unrun and untested. | Learner lacks `n`; Level 1 or C1 is false; arm inferiority; a v1/v2 effect; `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`; permission to tune or make a third learner-policy intervention. |
| Signed A6 non-finite terminal | If a complete window finished before the first non-finite loss/parameter state, the pass stands and non-finiteness is a mandatory diagnostic; otherwise it is valid scientific censoring with the non-finite flag. | Hardware/process invalidity by narration; dropping the fixture; using divergence time as a curve or arm comparison; treating a post-step bad parameter as a later panel/process failure. |
| Environment invalidity | The exact frozen environment did not match; no v2 binary exists and a signed invalidity disposition is required. | Pass/censor, learner-floor evidence, or an automatic retry after changing the host. |
| Resource invalidity | The wall or memory resource was insufficient before a valid terminal; `censored_at_b` is unset. | A no-solve observation, evidence against the learner, conversion of the 30 h projection into a guarantee, or automatic cap increase/rerun. |
| Process invalidity | The execution/artifact process failed; the durable claim, if already installed, remains and the binary is unset. | Learner inference, pass/censor narration, deletion/replacement of the claim, or automatic rerun. |
| Hash/source/evidence invalidity | A governing byte or immutable v1 reference failed verification; fail closed with no learner evidence. | Treating the mismatch as censoring, repairing lineage silently, or using the failed attempt to change the learner. |
| Seal/later-gate invalidity | The isolation/gate boundary was breached or a forbidden later artifact existed; follow the governing invalidity destination with no binary. | Any learner-floor, arm, C1, or programme statement; continuing to scout, N3, lock, panel, escrow, or outcome. |

## Authorization-candidate boundary

Codex may **not yet** prepare the v2 authorization candidate against reviewed
commit `d8c4663…`, because the A6 parameter-finiteness implementation is
load-bearing. After the bounded fix, tests, and source-scope re-review pass,
Codex may prepare a canonical v2 authorization candidate for separate review,
binding the newly reviewed code HEAD and the already frozen token, caps, world,
paths, signature/amendment hashes, and v1 hashes. Preparation never authorizes
execution; only Kirill may supply the execution token, and the driver must not
be invoked during candidate review.

## Negative space

This gate remains one development fixture and one learner class, not a Level 1
result. It creates no arm comparison, v1/v2 effect, N3 information,
preregistration lock, real panel, escrow, or outcome. The dummy panel is not a
real evaluator panel; panel observations and persistence history are not report
fields. Resource measurements are not capacity or success evidence. Level 0 is
engineering precedent only. Pass opens comparative-scout review only; censoring
blocks feasibility without deciding C1; invalidity has no binary and no
automatic rerun. Censored/`UNKNOWN` never mean success, equivalence, or a
narrated boundary. Level 1 remains a detector and cannot support `PROOF_CORE` or
any programme claim in either direction.

This audit created only this Markdown review. It created no code,
authorization, entropy, probe, trajectory, comparative datum, N3, lock, panel,
escrow, or outcome, and it did not run the v2 driver. Only read-only inspection,
tests, hash/source comparisons, and admitted-decision verification were
performed; no file was committed.
