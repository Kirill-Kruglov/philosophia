# Level 1 scientific specification — v3.1.3 bit-exact closure

Status: `CLOSURE_FOR_FINAL_XLINE_CONFIRMATION`. v3 + v3.1 + v3.1.1 +
v3.1.2 carry forward unchanged except for the two exact F-3 sentences below.
This correction adopts Opus's B-1/B-2 replacement text verbatim. It reopens no
scientific choice and creates or authorizes no code, entropy, datum,
feasibility/scout, lock, escrow, or outcome.

## B-1. Collision redraw surface

This sentence supersedes v3.1.2 F-3's ambiguous collision-counter sentence:

> On a duplicate `(u,v)` within an item, `u` and both pad draws are held fixed
> and **only the `v`-side `rank` domain's counter advances**, redrawing `v` until
> `(u,v)` is novel; no other domain is re-drawn on a collision, and exhaustion
> of the `v`-side word set (impossible under the A3 availability proof) is design
> invalidity.

## B-2. `cell_identity` serialization

This sentence completes v3.1.2 F-3's common-domain skeleton:

> `cell_identity` is serialized as its canonical integer rank for
> S1/S2/S3/S5, and for S4 as **two consecutive integer components `a` then
> `b`** (each decimal ASCII under the A2 `uint16_be(len)‖bytes` rule), never as
> a single composite token.

No other v3.1.2 text changes. In particular, F-1's operational-certificate
scope, F-2's exact `68,848` pool count, F-3's secret/public separation, the
three-token author packet, and every gate remain unchanged. Author signature
waits for one bounded X-line confirmation of B-1/B-2.
