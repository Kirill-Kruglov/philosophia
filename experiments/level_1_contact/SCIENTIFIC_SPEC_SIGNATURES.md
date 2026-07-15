# Level 1 scientific-specification signatures

Signed by Kirill Kruglov on 2026-07-13, before any Level 1 implementation run,
entropy draw, datum, feasibility run, comparative scout, N3 selection,
preregistration lock, escrow generation, or outcome.

Governing X-line verdict:
`LEVEL1_V3_1_3_XLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`.

Governing Y-line verdict:
`LEVEL1_V3_1_2_YLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`.

## Accepted decisions

```text
I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE
I_ACCEPT_LEVEL1_OPERATIONAL_MODULUS_CERTIFICATE
I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC
```

The third token accepts `SCIENTIFIC_SPEC_V3_DRAFT.md` together with the
normative v3.1, v3.1.1, v3.1.2, and v3.1.3 corrections.

These signatures accept, in particular:

- Level 1 measures online responsiveness only under the adjacent, distance-1,
  near-matched-scale construction; a null routes to
  `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`, not a general active-learning
  falsification;
- the S4 panel is an operational modulus certificate: a pass supports recovery
  of a contact-anchored `n` sufficient for novel `2n` versus `2n +/- 4`
  classification, not an abstract-period representation claim; failure remains
  censoring and never proves that the learner lacked `n`;
- the v3 scientific contract, including the 24-pair frame, ACTIVE/YOKED/RANDOM
  arms, fixed-budget censored BTCS endpoint, inference and routing rules,
  public-root/secret-panel separation, exact pool count, and bit-exact panel
  serialization.

This record authorizes implementation and tests only. It does not authorize the
one-shot public-root entropy draw, any learner execution producing scientific
data, feasibility/scout execution, N3 selection, a preregistration lock, real
panel escrow, or outcome execution.

## Governing source commit

```text
1a372f0f3c54f8732906ec99032abbd0dade0694
```

## Governing hashes

```text
ba2c2d4db9938a19839cb10d5a912f7395c72a1c71a4fa82a2ba5f8a86354e36  SCIENTIFIC_SPEC_V3_DRAFT.md
90b429be96da5fb3be17dd114edc17563c31e964be5f1a1a4ebe00b8cc68fd92  SCIENTIFIC_SPEC_V3_1_ADDENDUM.md
7b2177f9668965bdbf7f826cad54b336b692a33db266b7b900bf13e6f8c76999  SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md
1aba5dcf271a4d3ce4ed8314b6a00e50d00d108f2444866fe6ca475d5a9a0721  SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md
d95739230b74b94e6cd284296fbf6af78e494d7e69de3c43d941a6bdaf24aebf  SCIENTIFIC_SPEC_V3_1_3_CORRECTION.md
4559a5499573b07b2374b19c805dd68edef282b126794f41eb9f0011655ba5ed  opus_level1_v3_1_3_final_signature_confirmation.md
cfc08591bb778e67cc71cc4bca4e573ca26fc5144e4f101fc7957999e3209ab9  sol_level1_v3_1_2_signature_confirmation.md
```

Paths are relative to `experiments/level_1_contact/` for scientific specs and
to `reviews/` for review documents. Saved chat responses are provenance aids;
the formal documents and hashes above govern.

## Feasibility-floor amendment signature

Signed by Kirill Kruglov on 2026-07-15, after the immutable v1
non-comparative feasibility record and before any v2 implementation, resource
probe, v2 authorization, v2 trajectory, comparative scout, N3 selection,
preregistration lock, real-panel escrow, or Level 1 outcome.

Governing X-line verdict:
`LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_2_XLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`.

Governing Y-line verdict:
`LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_2_YLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`.

### Accepted amendment

```text
I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT
```

This token accepts `FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md` together with the
normative v2.1 and v2.2 corrections. It accepts, in particular:

- replacing stochastic minibatch-32 replay with one full-history, mean-CE,
  one-update-per-answer learner policy for every target and donor learner;
- conditioning all Level 1 potential outcomes and contrasts on that amended
  learner class while preserving the high-level ACTIVE-versus-YOKED question
  and estimator form;
- the explicit temporal weighting of retained contact, unchanged 2,000-update
  count, and the distinction between example-evaluation compute and learning
  capacity;
- the bit-exact v2 one-shot artifact contract, validity-first terminal routes,
  and the rule that only a valid completed v2 record may set `censored_at_b`;
- durable atomic claim creation before learner step 1 without a generated-claim
  Git commit, with process failure leaving the binary unset and authorizing no
  automatic rerun.

This signature authorizes implementation and tests of the amended learner and
v2 gate only. It does not authorize a resource probe, a v2 authorization
candidate, v2 execution, a comparative scout, N3 selection, a preregistration
lock, real-panel escrow, or outcome execution. The one-shot v2 run requires the
separate explicit token
`I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2` after implementation and
bounded review.

### Governing amendment source commit

```text
dbf7a977e92cd1a3eb2be766c6bd081deb0a460b
```

### Governing amendment hashes

```text
51d9833c79127c9a06b7e625b0f2af3c41cd0bdf54e5f63a950463ffc5c65fc8  FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md
d9ed5b562cbebef3e3b0a9c72d2d9dda35c834a044faf593d52b96b20c89ca14  FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md
5b413bc36e3468cb57c78b8832c471c51013bf160d71dc216c095907b2556c9b  FEASIBILITY_FLOOR_AMENDMENT_V2_2_CORRECTION.md
4b7f4b93ae0e9426329415b43b8cc87ca0005a939eb96e251393c5ff685b57c6  opus_level1_feasibility_floor_amendment_v2_2_signature_confirmation.md
5e0dea5d3b6a047ab2e652cfc493c4f79d352dc6bb8f5c59eceee8400381e594  sol_level1_feasibility_floor_amendment_v2_2_signature_confirmation.md
```

Paths are relative to `experiments/level_1_contact/` for amendment documents
and to `reviews/` for confirmations. The immutable v1 feasibility evidence
remains non-outcome and may never be interpreted as a v1/v2 contrast.
