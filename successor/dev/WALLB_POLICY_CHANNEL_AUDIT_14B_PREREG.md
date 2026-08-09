# WALLB_POLICY_CHANNEL_AUDIT_14B_PREREG

NON-CITABLE development gate. Written and committed before the audit-14b
generator, any instrument-sweep outcome, any fresh presentation, any fresh
panel, or any audit-14b frame outcome exists.

Supersedes the frozen-W audit-14 attempt. Audit 14 recorded
`POSITIVE_CONTROL_FAIL` under beam width `W=32` with a budget calibrated for
that width: CONTROL and a leaking TREATMENT were identical, so the forty-world
draw was correctly withheld. The missing step was a joint instrument-power
sweep before freezing the search operator.

## 1. Question and scope

Audits 12d and 13 tested experience delivered as additional library rules.
Audit 14 asked whether the policy channel is screenable, but froze a beam
width that nullified ordering. Audit 14b asks the same scientific-development
question after a preregistered hard-oracle screenability sweep:

Is there a calibrating search frame in which a ranking policy can move paired
outcomes, and if so, does that frozen frame yield at least five
`SCREEN_QUALIFIED` presentations among forty fresh units?

It does not estimate ACTIVE versus YOKED and cannot support a scientific claim.

## 2. Inherited pins and constants

- audit-12d source SHA-256:
  `927c15e773aea97c11b13eaa8ba53003617baa8dcada7e478bec3dee592976cc`
- audit-12d result SHA-256:
  `73afbec51b4769a51b6185ad1fed58b49ba749cc3a4e1f527d06657f0f183424`
- audit-13 source SHA-256:
  `68b74d3fb8f546f6329aed40f2d47eaf447ee9f98ecea32889e242b8230e387c`
- audit-13 result SHA-256:
  `77dfb82020cbfdd266495351a7d507be62940220177580759ff8ffbb46e67a78`
- audit-14 preregistration commit:
  `ec77d3719ea2de345e3b2b7313a8ca696c008073`
- audit-14 terminal commit:
  `bdcb09ef46e6ff2c2781dac1b8c288f60296611d`
- alphabet, equation sampler, seven-rule presentations, witness strata
  `(6,10,14)`, 64 goals per stratum (192 total), trie ISWU tariff, calibration
  target `0.40 +/- 0.05`, cap grid, `0.05B` restricted-mean floor, 20,000
  bootstrap resamples, Holm over 40, and the linear ranker feature rule from
  audit 14 are unchanged.
- Primary contrast still uses base equations only. No library macros enter
  CONTROL or TREATMENT.

## 3. One-dispatch hard-oracle instrument sweep

Before any of the forty fresh presentations is generated, run **one** dispatch
on the fixed historical world `21b64bd46791` from audit 12d.

### 3.1 Candidate frames

1. `best_first`: bidirectional best-first search with a global priority over
   open nodes. Expanding a node emits ISWU-charged matches; newly generated
   neighbors enter the open set of that side. Search meets when a generated
   neighbor lies in the other side's closed set. The work budget is the sole
   stop. There is no beam width.
2. `beam_W` for every
   `W in {1, 2, 4, 8, 16, 32, 64}`: the audit-14 level-synchronous
   bidirectional beam.

`W=1` is reported for diagnosis. It is **not selectable** for the forty-world
frame: it is greedy search, and a pass there is an artifact of a degenerate
procedure.

### 3.2 Joint `(frame, B)` calibration

For each candidate frame independently:

1. Run CONTROL on the calibration panel.
2. Choose `B` as the observed CONTROL work threshold whose solve rate is
   closest to `0.40` (tie: smaller `B`), exactly as in audits 12d/13/14.
3. Require the realized CONTROL calibration rate to lie in `[0.35, 0.45]`.
4. If no such `B` exists, the candidate is `CALIBRATION_INADMISSIBLE` and
   cannot pass power.

Budgets are **not** shared across widths or across beam versus best-first.
Reusing a `B` chosen under another frame is prohibited.

### 3.3 Hard-oracle power probe

On the evaluation panel of the same world, with that candidate's own `B`:

- `CONTROL`: deterministic non-informative order for that frame.
  - beam: retain the first `W` neighbors under
    `(shortlex(neighbor), position, pattern, replacement)`;
  - best-first: pop the open node with least
    `(proof_length, shortlex(word), side, word)`.
- `HARD_ORACLE`: same frame and `B`, but order uses deliberate leakage from
  the evaluation witness path of the goal under test: any neighbor on that
  path (forward or reversed) outranks every off-path neighbor; ties break by
  the CONTROL key. This probe is not the learned ranker and is not a
  scientific result.

`POWER_PASS` for a calibrating candidate requires all of:

- HARD_ORACLE solve rate strictly greater than CONTROL;
- solve-rate improvement at least `0.10`;
- restricted-mean ISWU gain at least `0.05B`;
- exact one-sided McNemar raw `p <= 0.001`.

### 3.4 Selection rule

Among `POWER_PASS` candidates:

1. If `best_first` passes, freeze `best_first` with its calibrated `B`.
2. Otherwise freeze the **largest selectable** beam width among
   `W in {2, 4, 8, 16, 32, 64}` that passes, with that width's own `B`.
3. If nothing selectable passes, stop with
   `POLICY_CHANNEL_NOT_SCREENABLE_IN_A_CALIBRATING_FRAME`.
   The equational cell is then closed on both tested experience carriers
   (library and policy). No forty-world draw is performed.

The sweep, selection, and any subsequent frame share one process. No second
dispatch, no hand-picking after peeking, and no widening of the W grid after
outcomes exist.

## 4. Learned policy on the frozen frame

Only if section 3 freezes a selectable frame:

- Train the audit-14 CPU linear logistic ranker on the relevance panel only,
  with the same features and hyperparameters, seed
  `SHA256("14b", presentation_identity, "ranker")`.
- Evaluation goals never train the frame-world ranker.
- `CONTROL` / `TREATMENT` differ only in order under the frozen frame.
- Hard-oracle scores are never used inside the forty-world draw.

## 5. Fresh frame

- Exact attempted frame size: `N=40`.
- Presentation seed: `2026080903`.
- Reject exact canonical duplicates of any audit-12d, audit-13, or audit-14
  presentation identity (equation-only SHA-256 prefix) and of earlier accepted
  audit-14b presentations.
- Panel seeds: `SHA256("14b", presentation_identity, role)` for
  relevance / calibration / evaluation in that order; 192 goals; prospective
  disjointness; role attempt cap 200,000.
- Per-world `B` is re-chosen on that world's CONTROL calibration panel under
  the frozen frame; it is not copied from the sweep world.

## 6. Qualification and terminals

`SCREEN_QUALIFIED` on a fresh unit requires the audit-14 predicate under the
frozen frame: structural screens; TREATMENT solve rate > CONTROL; exact
one-sided McNemar significant after Holm over the forty process-valid units at
family alpha `0.05`; restricted-mean gain `>= 0.05B`; paired-bootstrap lower
bound at quantile `0.05/40` positive; per-goal outcomes stored in JSON.

Let `Q` be the number of `SCREEN_QUALIFIED` units among 40.

- Sweep failure: `POLICY_CHANNEL_NOT_SCREENABLE_IN_A_CALIBRATING_FRAME`.
- `Q >= 5`: `POLICY_CHANNEL_VIABLE`.
- `Q < 5` after a successful freeze: `POLICY_CHANNEL_ALSO_SPARSE`.
- Process failure: `FRAME_AUDIT_INVALID`.

Both substantive sparse/viable terminals remain equally useful when the
instrument is screenable. The new non-screenable terminal closes the cell on
both carriers without a prevalence estimate.

## 7. Required JSON fields and prohibitions

Embed `preregistration_commit` as the commit hash of this file. Record the
full sweep table `(frame, W, B, calibration_rate, power metrics, decision)`,
the frozen selection, positive-control/hard-oracle status, and either the
forty-world records or the explicit non-screenable stop.

No threshold, seed, W grid, selection rule, panel, or route may change after
the sweep begins. No ACTIVE/YOKED arm, world contract, or essay claim is
authorized here.
