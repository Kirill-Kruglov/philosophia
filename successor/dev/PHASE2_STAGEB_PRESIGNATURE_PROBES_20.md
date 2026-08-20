# PHASE2_STAGE_B pre-signature probes 20

Status: `DEV_PROBE_ONLY__NO_SIGNATURE_AUTHORIZED`

PRF domain: `philosophia.stageb-presignature-probe.v1` (distinct from `audit`).

Lenovo Legion excluded: 8 GiB VRAM gave no expected performance gain.

## Hashes

- script raw `6ee8bcfa4a9bb0ae057e708697691730cb211e7b189013a1ad538ad0ee499de6` lf `6ee8bcfa4a9bb0ae057e708697691730cb211e7b189013a1ad538ad0ee499de6`
- theory raw `2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507` lf `2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507`
- L01 exclusions raw `31e319bdbfc7b17c65ac7c8698022c761f4f05790e1f044e692f736cf99d680a` lf `31e319bdbfc7b17c65ac7c8698022c761f4f05790e1f044e692f736cf99d680a`
- L2 exclusions raw `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d` lf `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d`

## Probe A - per-premise enumerability

| premise | annotation | forward | backward | typed | compile | replay_empty |
|---|---|---|---|---|---|---|
| and_i | `#backward and_i.` | False | True | True | True | True |
| and_el | `#forward and_el ('_ : (and 'P 'Q)).` | True | False | True | True | True |
| and_er | `#forward and_er ('_ : (and 'P 'Q)).` | True | False | True | True | True |
| or_il | `#backward or_il.` | False | True | True | True | True |
| or_ir | `#backward or_ir.` | False | True | True | True | True |
| or_e | `#backward or_e infer infer infer infer subgoal subgoal.` | False | True | True | True | True |
| not_i | `#backward not_i.` | False | True | True | True | True |
| not_e | `ABSENT` | True | True | True | True | True |
| exfalso | `#backward exfalso.` | False | True | True | True | True |

Finding: `not_e` ABSENT yet forward+backward (wider footprint than annotated premises).

## Probe B / Item 1 - depth 1..8 under grammar A

| depth | grammar_A | typed | compile | replay_empty | statement_size |
|---:|---|---|---|---|---:|
| 1 | True | True | True | True | 78 |
| 2 | True | True | True | True | 118 |
| 3 | True | True | True | True | 158 |
| 4 | True | True | True | True | 198 |
| 5 | True | True | True | True | 238 |
| 6 | True | True | True | True | 278 |
| 7 | True | True | True | True | 318 |
| 8 | True | True | True | True | 358 |

first_failure: `None`; outcome: **realizable**.

## Item 2 - durable exclusions registry

File: `phase2_disposable_identity_registry.jsonl` (78 entries). Fail-closed: `refuse_if_registered`.

## Facts for the signature

1. `not_e` has a wider action footprint than every annotated premise.
2. Positive control realizable at depth 1..8 under A; choice A no longer blocked by section 9.

Excluded roots: `7aee8705b0398bdf9cfc24f1553ece0fe47be69b82781b2fcec2b35c832790c1`, `e713e1aea28b49ccee66da67ba3e6989b744c4173a62f1cc6562dfbaf18d80d8`, `219b998523d8a954bdd79b7c68feb942c372c41e878cf2f1d1b3db26b2134c7b`, `0d25148f933ce483e30dd1c32a6478319bdc6f742eea48ef9386386dda6de643`, `597a36f1834f0ae1109bdba3dad6d30298194b6b8dd01ea4c0ac1162c0edebc6`, `aa86f6e270cf9827c1c67fa6855b70dfe138d188cf5060e13f8bc9159fac91f1`, `3c348516b63c2530e5d2612a088b893fcf42f205f37cd843377d201540eab045`, `dfeb5610a2d72620b368d9287ab10d391f79fbe0a63116514f6447042da6ef9d`, `b392dff29878d9e35711864764d929fd50b6f46de4d0eb2c85d8eaee02e214c0`, `fc0662bfd8c96ec31834312ead74099d9c79496aef1bd2daf4a0b28f28db58b3`, `ceb2ce600031e08f17164ed99b3e74a3b7e709f97353b66e2f55d2836fdb7058`, `fa52a094e67b1ad076ddbe92134986b1bfd2219287cecf29be6677b724422594`, `e5ddd6300961a6a199cf6decafa01bd784a943125d171ab999744693d8b4dcf3`, `e83397e1f744ff818481a5dfff7786e2a4e98d465227cd0878f5542bc6748d47`, `82db765c232b31d33b4f641b6e5fb4a4f6ff7d483bffa24b615a6f710d528aec`, `6969d5e1390d43a3c258b784fd2478e492a427fb119d55683dbed558d4ac7ac5`, `145979079457204b75c636584af93b1915a57053784af589eb3f33b5063e9c76`, `cbd55186ce5972be866c96e636b58e6865f1225e9ae2e27678a181e531671a3b`, `4fa2c3012fc2403a59e7bc5ed37131ec08017bc5babb7996a024cac13f7439b3`

No threshold, band, cap, or calibration may be taken from this artifact.
