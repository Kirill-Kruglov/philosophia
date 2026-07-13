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
