# Officina P1 watchdog v2.6: exact schemas and honest temporal boundary

You are Claude Code Opus 5, specification author. Produce one bounded v2.6 correction. Do not reopen watchdog behavior or option design.

## Governing inputs

Read:

- the watchdog chain through v2.5;
- `reviews/fable_officina_p1_watchdog_v2_5_independent_x_confirmation.md`;
- `reviews/sol_officina_p1_watchdog_v2_5_final_y_confirmation.md`;
- the newly signed `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md` as current external state, without treating it as authority for the still-unsigned bounded-weakening token.

X confirmed v2.5. Y returned `REVISE` on generated-schema completeness, false retrospective-order/replay claims, and unique-attester wording. Adopt the honest procedural route below. Historical files remain byte-immutable.

## R1. Complete every generated schema and validator

In both new governing files, make two independent implementations produce the same bytes and the same validity predicate:

1. `M4`: define every top-level value type; define `reachable_closure` as one exact canonical JSON shape with exact element key set/types, sort key, uniqueness and ordering; define the exact mandatory `schema` value, version value and all field grammars.
2. `M7` and install record: state exact mandatory `schema` values, versions, key sets, nested shapes/types/order and canonical encodings.
3. Define one exact `created_utc` grammar and semantic validator wherever the field appears. It is provenance only and **not trusted temporal-order evidence**.
4. Stage A: state the three pre-selection paths as literal repository-relative strings, including the v2.6 successors actually reviewed; specify exact values/types for `schema`, `version`, `author`, `signature_algorithm`, option tokens, path/hash pairs, public key, key id, threat model and `created_utc`.
5. Stage B: specify exact values/types for every key, including `schema`, `version`, paths, hashes, option token, algorithm and `created_utc`.
6. Rewrite Stage-A and Stage-B verification as exhaustive field-by-field algorithms. Every mandatory literal and derived relation must be checked; no field may be merely present.
7. Add exact malformed/type/order/value/path fixtures for every generated object.

## R2. Narrow historical-order claims to what final bytes prove

Do **not** add an HSM, external service, timestamp oracle or new scientific gate. Use the existing procedural threat model honestly:

- `OR-1..OR-11` remains the sole conforming construction procedure and a mandatory operator obligation.
- `G-11` verifies the exact final state only. It does not claim to reconstruct creation history from identical final bytes.
- Withdraw every statement that an early install record, pre-test M7, pre-manifest id computation or late Stage A is retrospectively distinguishable after the exact valid final bytes exist.
- Rewrite test 106(h): it may test procedural driver state transitions/crash cuts while they occur, but it must not claim that the final-state verifier distinguishes byte-identical forbidden history.
- `created_utc` is never used as a trusted order proof.
- A discovered contemporaneous procedure violation routes to a named process/control invalidity and no production entry; an undiscoverable historical violation is inside the declared procedural residual.

## R3. State coherent rollback exactly

Extend `TR-2` and every summary:

- partial substitution, mixed generations and replay of a prior record against current members are mechanically refused;
- complete coherent restoration of a previously valid generation — Stage A, all members, Stage B, signature and sole record — is not distinguishable by the filesystem-resident verifier and remains possible at any later time for an actor able to replace the whole repository/control set;
- no sentence may claim every post-hoc substitution, complete rollback resistance, immutable external custody or cryptographic freshness;
- the Ed25519 chain authenticates Stage B relative to the Stage-A key and closes partial substitution under the procedural root; it does not create monotonic freshness.

Add an explicit coherent-rollback fixture classified as **outside the guarantee**, not falsely refused.

## R4. Remove false unique-attester claims

Replace `IR-4`, row 115 and all summaries so they state the actual directed integrity graph:

- the install record lists every M1..M7 member digest;
- M4 additionally binds the specified governing/selection inputs;
- M7 additionally binds M5/M6 and test execution;
- these additional bindings are intentional and are not self-attestation;
- no uniqueness of external attester is claimed.

## R5. Keep member accounting and identity selection honest

Preserve the literal, disjoint v2.5 M1..M7 set except for version/path/hash updates mechanically required by v2.6. Recompute all cardinalities and digests.

The new identity selection signature may be named as current author-state provenance or a prerequisite for the later combined binding, but it must not be misclassified as accepting `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, must not silently enter scientific evidence, and must not make the present watchdog pair operative. If it is not part of M1..M7, say so explicitly and state where the later combined binding must account for it.

## Preserved boundaries

Preserve all X-confirmed v2.5 behavior, literal enumeration/disjointness, two-stage Ed25519 format, option symmetry and non-selection, killer-watchdog rejection, process-only metadata, scientific negative space and `T = NOT_ACTIVATED`.

No key, entropy, Stage A/B artifact, install record, implementation or activation is authorized or created.

## Deliverables

Write new files only:

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_6_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_6.md`
- `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_6_closure.md`

The closure must:

- emit `READY_FOR_OFFICINA_P1_WATCHDOG_V2_6_INDEPENDENT_XY_CONFIRMATION` or a precise blocker;
- disposition every v2.5 Y finding one-to-one and show preservation of the v2.5 X confirmation;
- include exact hashes, complete schemas/validators, revised tests, integrity graph, final-state-versus-history truth table and updated residual;
- require independent X by Fable 5/Opus 4.8 and Y by Sol;
- authorize no watchdog token or downstream action.

Do not modify existing files and do not commit.
