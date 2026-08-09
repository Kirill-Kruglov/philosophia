# WALLB_POLICY_CHANNEL_AUDIT_14_PREREG

NON-CITABLE development gate. Written and committed before the audit-14
generator, any fresh presentation, any fresh panel, any ranker fit on a frame
world, or any audit-14 outcome exists.

## 1. Question and scope

Audits 12d and 13 tested experience delivered as additional library rules.
Neither tested the policy channel: reordering already-legal rewrite candidates
inside a fixed search budget, without growing the rule set. Closing the
equational cell without that carrier is incomplete.

Audit 14 asks only whether a trained ranking policy improves paired solve
outcomes often enough, under a frozen beam instrument, to supply five or more
`SCREEN_QUALIFIED` presentations among forty fresh units. It does not estimate
ACTIVE versus YOKED and cannot support a scientific claim.

## 2. Frozen inherited instrument

- source pins:
  - audit-12d source SHA-256:
    `927c15e773aea97c11b13eaa8ba53003617baa8dcada7e478bec3dee592976cc`
  - audit-12d result SHA-256:
    `73afbec51b4769a51b6185ad1fed58b49ba749cc3a4e1f527d06657f0f183424`
  - audit-13 source SHA-256: recorded by the implementation commit against the
    committed `wallb_frame_audit_13.py` bytes
  - audit-13 result SHA-256: recorded by the implementation commit against the
    committed `wallb_frame_audit_13_results.json` bytes
- alphabet, equation sampler, seven-rule presentation size, goal generator,
  witness strata `(6,10,14)`, 64 goals per stratum (192 total), trie matcher,
  ISWU primary tariff, calibration target `0.40 +/- 0.05`, cap grid, 20,000
  bootstrap resamples, and the `0.05B` restricted-mean floor are unchanged.
- Primary contrast uses base equations only. No completion macros enter CONTROL
  or TREATMENT search. Completion may still run solely as a structural screen.

Audit 14 may copy the one-file sampler/matcher/accounting substrate from audit
13. It may not import Officina, revive ACTIVE/YOKED, tune thresholds after the
first fresh presentation is generated, or inspect an audit-14 frame outcome
before generator and decision code are committed.

## 3. Sole frame change: bidirectional beam plus policy order

- Search is level-synchronous bidirectional beam search.
- Beam width `W = 32`, frozen here before code.
- Both arms use the same beam, the same ISWU tariff, and the same per-world
  budget `B` chosen on CONTROL.
- `CONTROL`: within each expansion, candidate neighbors are ordered by the
  deterministic non-informative key
  `(shortlex(neighbor), position, pattern, replacement)`; the beam retains the
  first `W` unique neighbors.
- `TREATMENT`: the same candidate set is ordered by a trained ranker score
  (higher first), with the same deterministic tie-break; the beam retains the
  first `W` unique neighbors.
- No other search operator, rule set, panel size, or ledger may differ between
  arms.

## 4. Policy object

- Model class: CPU linear ranker trained by binary logistic SGD. No GPU. A GBM
  is not required for the primary arm; if implemented later it is sensitivity
  only and cannot alter qualification.
- Features MUST include both:
  - surface identities at the rewrite site: one-hot alphabet features for the
    character before the match, the first matched character, the character
    immediately after the match, and the first replacement character;
  - structural goal geometry: signed and absolute length delta of the neighbor
    to the opposing-beam root, Parikh L1 distance to that root, per-symbol
    Parikh deltas, and the rewrite length change.
- A renaming of the alphabet must be able to change the feature vector. Perfect
  rename-transfer at initialization is a feature bug and invalidates the run.
- Training uses only the relevance panel. For each manufactured witness path,
  the on-path next word is a positive; every other legal neighbor of an on-path
  word is a negative. Evaluation goals are never seen by training on a frame
  world.
- Ranker hyperparameters frozen before code: learning rate `0.05`, epochs `20`,
  L2 `1e-4`, minibatch `64`, seed derived from
  `SHA256("14", presentation_identity, "ranker")`.

## 5. Positive control first (instrument power, not a result)

Before any of the forty fresh presentations is generated, run one cheap leaking
oracle check on the fixed historical world `21b64bd46791` from audit 12d:

1. Build the usual disjoint relevance / calibration / evaluation panels with
   audit-14 panel seeding under presentation identity `21b64bd46791`.
2. Fit the same feature ranker on the evaluation-panel witness paths
   (deliberate leakage).
3. Compare CONTROL versus leaking TREATMENT under the frozen beam and the
   CONTROL-chosen `B`.

`POSITIVE_CONTROL_PASS` requires all of:

- TREATMENT solve rate strictly greater than CONTROL;
- restricted-mean ISWU gain at least `0.05B`;
- exact one-sided McNemar raw `p <= 0.001`;
- solve-rate improvement at least `0.10`.

Failure is `POSITIVE_CONTROL_FAIL`: the beam/policy instrument lacks power.
Stop. Do not draw the forty-world frame. This check is not pooled into Q and is
not a scientific policy result.

## 6. Fresh frame

- Exact attempted frame size: `N=40`.
- Presentation seed: `2026080902`.
- Draw presentations sequentially with the inherited `sample_presentation`.
- Canonical presentation identity is SHA-256 of its sorted seven equation pairs,
  truncated to twelve hex characters, without an index component.
- Reject exact canonical duplicates of any audit-12d presentation, any audit-13
  presentation, or an earlier accepted audit-14 presentation. Duplicate
  rejection consumes the draw and continues the same PRNG stream. No
  outcome-dependent replacement exists.
- Stop after 40 unique fresh presentations or 100,000 sampler calls. Exhaustion
  is `FRAME_AUDIT_INVALID`.

## 7. Panels and validity

For each presentation, derive separate relevance, calibration and evaluation
seeds from `SHA256("14", presentation_identity, role)`. Generate roles in that
fixed order. Each role contains 64 unique goals in each witness stratum, 192 in
total. A `(start,target)` pair already accepted in the current or an earlier
role is rejected during generation. The role attempt cap is 200,000 calls;
failure is `FRAME_AUDIT_INVALID` for the whole audit, with no top-up or rerun.

Every presentation is retained in the output. Failure of a scientific screen
condition is a valid `NOT_QUALIFIED` result, not process invalidity. Any panel
shortfall, overlap, duplicate presentation, source-pin mismatch, verifier
failure, positive-control skip, or non-deterministic rerun is
`FRAME_AUDIT_INVALID`.

## 8. Fixed per-presentation predicate

`SCREEN_QUALIFIED` requires all of the following on the fresh evaluation panel:

1. structural screens pass: complete disjoint panels; CONTROL calibration rate
   in `[0.35,0.45]`; bounded completion not converged; CONTROL beam not
   saturated (`solved_rate < 0.80` and restricted mean `> 0.20B`); no
   length/Parikh ladder correlation at `|r| >= 0.80`; relevance training set
   contains at least one positive and one negative;
2. TREATMENT solve rate is strictly greater than CONTROL solve rate;
3. exact one-sided McNemar raw p, after Holm step-down across the forty
   process-valid units at family alpha `0.05`, is significant;
4. restricted-mean ISWU gain is at least `0.05B`; and
5. the paired-bootstrap lower bound at quantile `alpha/m = 0.05/40` is positive.

Per-goal CONTROL/TREATMENT outcomes must be stored in the JSON. There is no
best-world rule and no ACTIVE/YOKED arm.

## 9. Frame endpoint and terminal routing

Let `Q` be the number of `SCREEN_QUALIFIED` presentations among all 40.

- `Q >= 5`: `POLICY_CHANNEL_VIABLE`. The policy carrier is alive under this
  generator and screen; library sparsity was not a property of the whole
  equational cell.
- `Q < 5`: `POLICY_CHANNEL_ALSO_SPARSE`. Closure of the equational cell is
  complete on both experience carriers tested in this programme.
- Any process-validity failure: `FRAME_AUDIT_INVALID`, regardless of Q.

Both substantive terminals are equally useful. Five remains the engineering
minimum at which presentation can act as a blocking factor. No world contract,
ACTIVE/YOKED comparison, scientific lock or essay claim is authorized here.

## 10. Required report fields and prohibitions

Report CONTROL and TREATMENT solve rates, restricted means, gains/losses, raw
and Holm-adjusted McNemar p, restricted-mean gain, bootstrap lower bound,
calibration `B`, positive-control block, all forty per-world records, and
implementation nonblank line count. The results JSON must embed
`preregistration_commit` as the commit hash of this file.

No presentation may be manually removed, renamed or replaced. No threshold,
seed, beam width, panel, frame size or route may change after the first
audit-14 presentation is generated. No library-growth arm is reopened by this
gate.
