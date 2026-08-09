# WALLB_FRAME_AUDIT_13_PREREG

NON-CITABLE development gate. Written and committed before the frame generator,
any fresh presentation, any fresh panel, or any audit-13 outcome exists.

## 1. Question and scope

Audit 12d found one powered library-usefulness signal among eight sampled
presentations. Audit 13 asks only whether that mechanism occurs often enough in
the declared presentation generator to supply a multi-world development frame.
It does not estimate ACTIVE versus YOKED and cannot support a scientific claim.

The target is the joint generator-and-panel probability that a fresh
presentation is `SCREEN_QUALIFIED` under the fixed predicate below. It is not a
claim that every semi-Thue presentation benefits from a library.

## 2. Frozen inherited instrument

- source commit: `7394063ce636c32ac6fcbda12c728daa3edcc2cd`
- audit-12d source SHA-256:
  `927c15e773aea97c11b13eaa8ba53003617baa8dcada7e478bec3dee592976cc`
- audit-12d result SHA-256:
  `73afbec51b4769a51b6185ad1fed58b49ba749cc3a4e1f527d06657f0f183424`
- alphabet, equation sampler, seven-rule presentation size, completion caps,
  goal generator, witness strata `(6,10,14)`, 64 goals per stratum, trie search,
  calibration target `0.40 +/- 0.05`, cap grid, K=8 primary library, ISWU tariff,
  expanded-match sensitivity and 20,000 bootstrap resamples are unchanged.

Audit 13 may copy this one-file standard-library implementation. It may not
import or revive Officina, add a learner, tune a selector, change a comparator,
or inspect an audit-13 outcome before the generator and decision code are
committed.

## 3. Fresh frame

- Exact attempted frame size: `N=40`. This is the midpoint of the independently
  proposed planning range 30--50, selected before new data.
- Presentation seed: `2026080901`.
- Draw presentations sequentially with audit 12c/12d `sample_presentation`.
- Canonical presentation identity is SHA-256 of its sorted seven equation pairs,
  without an index component.
- Reject only exact canonical duplicates of the eight audit-12d presentations
  or an earlier accepted audit-13 presentation. Duplicate rejection consumes
  the draw and continues the same PRNG stream. No outcome-dependent replacement
  exists.
- Stop after 40 unique fresh presentations or 100,000 sampler calls. Exhaustion
  is `FRAME_AUDIT_INVALID`.

## 4. Panels and validity

For each presentation, derive separate relevance, calibration and evaluation
seeds from `SHA256("13", presentation_identity, role)`. Generate roles in that
fixed order. Each role contains 64 unique goals in each witness stratum, 192 in
total. A `(start,target)` pair already accepted in the current or an earlier
role is rejected during generation. This is a prospective sampling rule, not a
post-outcome repair. The role attempt cap is 200,000 calls; failure is
`FRAME_AUDIT_INVALID` for the whole audit, with no top-up or rerun.

Every presentation is retained in the output. Failure of a scientific screen
condition is a valid `NOT_QUALIFIED` result, not process invalidity. Any panel
shortfall, overlap, duplicate presentation, source-pin mismatch, verifier
failure or non-deterministic rerun is `FRAME_AUDIT_INVALID`.

## 5. Fixed per-presentation predicate

`SCREEN_QUALIFIED` requires all of the following on the fresh evaluation panel:

1. all inherited structural checks pass: complete panels, calibration in
   `[0.35,0.45]`, at least 64 verified completion macros, bounded completion not
   converged, matched surface search not saturated, no length/Parikh ladder
   correlation at `|r| >= 0.80`, and a nonzero relevance signal;
2. K=8 solve rate is greater than K=0 solve rate;
3. exact one-sided McNemar raw `p <= 0.00625`, the fixed Bonferroni threshold
   `0.05/8` inherited from 12d and independent of frame size;
4. restricted-mean ISWU gain is at least `0.05B`; and
5. the paired-bootstrap lower bound at quantile `0.00625` is positive.

The predicate is evaluated independently for every unit. There is no Holm
selection across 40 worlds and no best-world rule. Holm was appropriate for the
12d search for any signal; audit 13 instead estimates the prevalence of a fixed,
already-frozen qualification event.

## 6. Frame endpoint and terminal routing

Let `Q` be the number of `SCREEN_QUALIFIED` presentations among all 40 and
`p_hat=Q/40`. Report the two-sided 95% Wilson interval for the joint
generator-and-panel prevalence, all 40 per-world records, and the full
gains/losses and restricted-mean values. No independence is claimed for goals
within a presentation.

- `Q >= 5`: `MULTI_WORLD_DEVELOPMENT_FRAME_AVAILABLE`. Retain all qualified
  presentations as a finite development frame. This opens only a new author
  scope decision and a preregistered learner-design contract. It does not
  authorize ACTIVE/YOKED.
- `Q = 1..4`: `SPARSE_SELECTION_CONDITIONAL_FRAME_ONLY`. A broad or multi-world
  route is not supported. Any singleton/sparse continuation requires an
  explicit selection-conditional author decision before learner design.
- `Q = 0`: `NO_USABLE_FRAME_EQUATIONAL_CELL_VOID`.
- Any process-validity failure: `FRAME_AUDIT_INVALID`, regardless of Q.

Five is fixed because the prior review identified five presentation blocks as
the minimum at which presentation can function as an actual blocking factor
rather than one selected anchor with goal-level pseudo-replication. This is an
engineering gate, not a prevalence hypothesis test.

## 7. Required sensitivity and prohibitions

Report K=32, K=64, completion-order K=8, expanded-match K=8 and surface K=0
exactly as in 12d. They cannot alter qualification or routing. Report the eight
audit-12d worlds separately as historical calibration; they are never pooled
into Q.

No presentation may be manually removed, renamed or replaced. No threshold,
seed, cap, panel, macro count, frame size or route may change after the first
audit-13 presentation is generated. No world contract, ACTIVE/YOKED arm,
learner training, scientific outcome or essay claim is authorized here.
