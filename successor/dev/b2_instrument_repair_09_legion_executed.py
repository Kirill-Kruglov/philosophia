"""NON-CITABLE B2 instrument repair 09. Instrumentation R1-R5 only.

Copy of b2_path_pilot_08.py with instrument repairs. Frozen experiment
constants unchanged. Does not interpret DONE/KILL/INCONCLUSIVE.

Writes successor/dev/B2_INSTRUMENT_REPAIR_09.md (+ results JSON + run log).
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Sequence

import torch
import torch.nn.functional as F

_ROOT = Path(__file__).resolve().parents[2]
_SRC = _ROOT / "src"
_DEV = Path(__file__).resolve().parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_DEV) not in sys.path:
    sys.path.insert(0, str(_DEV))

from philosophia.level1.config import (  # noqa: E402
    BUDGET,
    CHECKPOINT_CADENCE,
    MODEL_INPUT_LENGTH,
    PANEL_SIZE,
    PANEL_STRATUM_COUNTS,
    PERSISTENCE_CHECKPOINTS,
)
from philosophia.level1.feasibility import _committee  # noqa: E402
from philosophia.level1.interlock import feasibility_v2_capability  # noqa: E402
from philosophia.level1.model import (  # noqa: E402
    D_MODEL,
    ContactTransformer,
    build_optimizer,
    committee_equal_probability,
    encode_pair,
)
from philosophia.level1.panel import DummyPanel, DummyPanelBuilder  # noqa: E402
from philosophia.level1.pool import (  # noqa: E402
    partition_cells,
    realize_pool_index,
    verify_partition,
)
from philosophia.level1.scoring import (  # noqa: E402
    ACCURACY_MINIMUM,
    PanelObservation,
    StratumScore,
    checkpoint_qualifies,
    score_stratum,
)
from philosophia.level1.serialization import (  # noqa: E402
    CounterStream,
    DeterministicKey,
    dummy_key,
    sample_without_replacement,
    shuffled,
)
from philosophia.level1.world import (  # noqa: E402
    admissible_paddings,
    displacement,
    fold,
    oracle_eq,
    unrank_word,
    word_count,
    word_length,
)

import gpu_committee_runner as runner  # noqa: E402
from capacity_diag_04 import (  # noqa: E402
    DEV_PANEL_LABEL,
    DEV_PUBLIC_LABEL,
    MODULUS,
    WORLD_SLOT,
    curated_rich_equal_schedule,
)

OUT_MD = _DEV / "B2_INSTRUMENT_REPAIR_09.md"
OUT_JSON = _DEV / "b2_repair_09_results.json"
OUT_LOG = _DEV / "b2_repair_09_run.log"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----- Locked constants (register BEFORE run; Sol C4) -----
N_MAX = 2000  # DIAG_04 curated distinct labeled-pair count (verified at runtime)
K = N_MAX // 8  # floor(N_max/8) = 250; do not sweep
H_DEST = 500  # destination / oracle-stage horizon (pilot lock)
M_PATH = 600  # path updates (pilot lock)
PATH_BATCH = 32  # length-matched positive pairs per path step
M_ROADS = 4  # roads drawn per displacement group
VICREG_INV = 25.0
VICREG_VAR = 25.0
VICREG_COV = 1.0
CONTRAST_TEMP = 0.1
MICROBATCH = 128
PILOT_SEEDS = (0, 1)
READOUT_EPOCHS = 80
PROBE_EPOCHS = 60

# Path displacement support FIXED independently of n=66 (Sol C2).
_D_PATH_LO, _D_PATH_HI = -80, 80

# Instrument-only (not experiment constants)
HOLDOUT_PAIRS = 512
LOG_CADENCE = 100
PROBE_CORPUS_TARGET = 2400  # start as pilot 08; R5 enlarges until stratum populated
PROBE_WITHIN_MIN = 60
PROBE_CORPUS_CAP = 24000
PROJECTOR_HIDDEN = 256
# Set by main for the conditional section-3 rerun only.
USE_BN_PROJECTOR = False


# =============================================================================
# Path firewall: path code may read ONLY token counts + exact-d sameness.
# =============================================================================

_FORBIDDEN_PATH_NAMES = frozenset(
    {
        "modulus",
        "n_mod",
        "residue",
        "fold_val",
        "oracle",
        "oracle_eq",
        "panel",
        "panel_item",
        "truth",
        "label_oracle",
        "MODULUS",
    }
)


def _assert_path_clean(context: str, **kwargs: object) -> None:
    """Assert path pipeline kwargs never carry n/residue/oracle/panel."""
    bad = [k for k in kwargs if k in _FORBIDDEN_PATH_NAMES or k.lower() in _FORBIDDEN_PATH_NAMES]
    if bad:
        raise RuntimeError(f"path firewall violation in {context}: {bad}")
    # Values must not be the frozen modulus smuggled as an int named otherwise
    # when the caller explicitly tags them — checked by name above.
    _ = context


def _pair_key(left: bytes, right: bytes) -> tuple[bytes, bytes]:
    return (left, right)


def _hash_pairs(pairs: Sequence[tuple[bytes, bytes]]) -> str:
    digest = hashlib.sha256()
    for left, right in pairs:
        digest.update(left)
        digest.update(b"|")
        digest.update(right)
        digest.update(b";")
    return digest.hexdigest()[:16]


# =============================================================================
# Activations / encoding helpers
# =============================================================================


def encode_word_self(word: bytes) -> torch.Tensor:
    return encode_pair(word, word)


@torch.no_grad()
def prehead(model: ContactTransformer, tokens: torch.Tensor) -> torch.Tensor:
    if tokens.device != DEVICE:
        tokens = tokens.to(DEVICE)
    key_mask = tokens.ne(0)
    positions = torch.arange(MODEL_INPUT_LENGTH, device=tokens.device)
    x = model.token_embedding[tokens] + model.position_embedding[positions][None, :, :]
    for layer in model.layers:
        x = layer(x, key_mask)
    return model.final_ln(x)[:, -1, :]


def prehead_grad(model: ContactTransformer, tokens: torch.Tensor) -> torch.Tensor:
    """Pre-head with grad (path training)."""
    if tokens.device != DEVICE:
        tokens = tokens.to(DEVICE)
    key_mask = tokens.ne(0)
    positions = torch.arange(MODEL_INPUT_LENGTH, device=tokens.device)
    x = model.token_embedding[tokens] + model.position_embedding[positions][None, :, :]
    for layer in model.layers:
        x = layer(x, key_mask)
    return model.final_ln(x)[:, -1, :]


def committee_mean_prehead(
    models: Sequence[ContactTransformer], tokens: torch.Tensor, *, chunk: int = 64
) -> torch.Tensor:
    outs = []
    with torch.no_grad():
        for start in range(0, tokens.shape[0], chunk):
            sl = tokens[start : start + chunk].to(DEVICE)
            vecs = torch.stack([prehead(m, sl) for m in models], dim=0).mean(dim=0)
            outs.append(vecs.cpu())
    return torch.cat(outs, dim=0)


# =============================================================================
# Path sampler (oracle-free; length-matched)
# =============================================================================


def _build_length_index() -> dict[int, list[tuple[int, int]]]:
    """length ℓ → list of (d, padding) with word_length(d,p)=ℓ. Skips empty (d=0,p=0)."""
    by_len: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for d in range(_D_PATH_LO, _D_PATH_HI + 1):
        for p in admissible_paddings(d):
            ell = word_length(d, p)
            if ell == 0:
                # d=0,p=0 → empty word; noted explicitly, excluded from path batches.
                continue
            if ell < 2:
                continue
            by_len[ell].append((d, p))
    # Keep lengths that admit ≥2 distinct displacements (for contrastive / variety).
    return {ell: vals for ell, vals in by_len.items() if len({d for d, _ in vals}) >= 2}


_LENGTH_INDEX = _build_length_index()
_LENGTHS = sorted(_LENGTH_INDEX.keys())


def _sample_word_at(d: int, padding: int, stream: CounterStream) -> bytes:
    _assert_path_clean("sample_word_at", d=d, padding=padding)
    n = word_count(d, padding)
    if n <= 0:
        raise RuntimeError("empty word_count")
    rank = stream.uniform(n)
    word = unrank_word(d, padding, rank)
    # Token-count check only (path-legal).
    if len(word) != abs(d) + 2 * padding:
        raise RuntimeError("token-count mismatch")
    if displacement(word) != d:
        raise RuntimeError("exact-displacement mismatch after unrank")
    return word


def sample_length_matched_positive_batch(
    stream: CounterStream,
    *,
    batch_pairs: int,
    roads_per_group: int,
    shuffle_groups: bool = False,
    exclude_words: frozenset[bytes] | None = None,
) -> tuple[list[bytes], list[bytes], list[int], int]:
    """Return (w1s, w2s, group_ids, length ℓ).

    Path-legal: uses only exact-d sameness + token counts. Never reads n/oracle/panel.
    If shuffle_groups: randomize pairing across groups (P_shuf fake ledger).
    If exclude_words is set, resample until no excluded word appears (asserted).
    """
    _assert_path_clean("sample_batch", batch_pairs=batch_pairs)
    exclude = exclude_words or frozenset()
    max_tries = 200
    for attempt in range(max_tries):
        w1s, w2s, gids, ell = _sample_length_matched_positive_batch_once(
            stream,
            batch_pairs=batch_pairs,
            roads_per_group=roads_per_group,
            shuffle_groups=shuffle_groups,
        )
        used = set(w1s) | set(w2s)
        if used.isdisjoint(exclude):
            return w1s, w2s, gids, ell
    raise RuntimeError(
        f"could not sample batch disjoint from held-out after {max_tries} tries"
    )


def _sample_length_matched_positive_batch_once(
    stream: CounterStream,
    *,
    batch_pairs: int,
    roads_per_group: int,
    shuffle_groups: bool = False,
) -> tuple[list[bytes], list[bytes], list[int], int]:
    ell = _LENGTHS[stream.uniform(len(_LENGTHS))]
    options = _LENGTH_INDEX[ell]
    # Distinct displacements available at this length.
    d_to_pads: dict[int, list[int]] = defaultdict(list)
    for d, p in options:
        d_to_pads[d].append(p)
    ds = list(d_to_pads.keys())
    n_groups = max(2, batch_pairs // max(1, roads_per_group // 2))
    chosen_ds = []
    for _ in range(n_groups):
        chosen_ds.append(ds[stream.uniform(len(ds))])

    roads: list[tuple[bytes, int]] = []  # (word, group_idx)
    for g, d in enumerate(chosen_ds):
        pads = d_to_pads[d]
        for _ in range(roads_per_group):
            p = pads[stream.uniform(len(pads))]
            w = _sample_word_at(d, p, stream)
            # Ensure distinctness within group when possible.
            tries = 0
            while any(w == rw for rw, rg in roads if rg == g) and tries < 20:
                w = _sample_word_at(d, p, stream)
                tries += 1
            roads.append((w, g))

    # Form positive pairs within groups (true d-sameness), or shuffled.
    by_g: dict[int, list[bytes]] = defaultdict(list)
    for w, g in roads:
        by_g[g].append(w)

    w1s: list[bytes] = []
    w2s: list[bytes] = []
    gids: list[int] = []
    if shuffle_groups:
        # Fake ledger: pair random roads ignoring true group (no true invariance).
        flat = [w for w, _ in roads]
        for _ in range(batch_pairs):
            i = stream.uniform(len(flat))
            j = stream.uniform(len(flat))
            while j == i and len(flat) > 1:
                j = stream.uniform(len(flat))
            w1s.append(flat[i])
            w2s.append(flat[j])
            gids.append(-1)
    else:
        for g, ws in by_g.items():
            if len(ws) < 2:
                continue
            for i in range(len(ws) - 1):
                w1s.append(ws[i])
                w2s.append(ws[i + 1])
                gids.append(g)
                if len(w1s) >= batch_pairs:
                    break
            if len(w1s) >= batch_pairs:
                break
        # Top up if short.
        while len(w1s) < batch_pairs:
            g = chosen_ds[stream.uniform(len(chosen_ds))]
            # find group index
            gi = chosen_ds.index(g) if g in chosen_ds else 0
            ws = by_g[gi]
            if len(ws) < 2:
                pads = d_to_pads[g]
                p = pads[stream.uniform(len(pads))]
                a = _sample_word_at(g, p, stream)
                b = _sample_word_at(g, p, stream)
            else:
                a = ws[stream.uniform(len(ws))]
                b = ws[stream.uniform(len(ws))]
            w1s.append(a)
            w2s.append(b)
            gids.append(gi)

    return w1s[:batch_pairs], w2s[:batch_pairs], gids[:batch_pairs], ell


def sample_length_matched_diff_batch(
    stream: CounterStream,
    *,
    batch_pairs: int,
    exclude_words: frozenset[bytes] | None = None,
) -> tuple[list[bytes], list[bytes]]:
    """Length-matched pairs with DIFFERENT exact displacement (path-legal)."""
    _assert_path_clean("diff_batch", batch_pairs=batch_pairs)
    exclude = exclude_words or frozenset()
    w1s: list[bytes] = []
    w2s: list[bytes] = []
    max_tries = batch_pairs * 50
    tries = 0
    while len(w1s) < batch_pairs and tries < max_tries:
        tries += 1
        ell = _LENGTHS[stream.uniform(len(_LENGTHS))]
        options = _LENGTH_INDEX[ell]
        d_to_pads: dict[int, list[int]] = defaultdict(list)
        for d, p in options:
            d_to_pads[d].append(p)
        ds = list(d_to_pads.keys())
        if len(ds) < 2:
            continue
        d_a = ds[stream.uniform(len(ds))]
        d_b = ds[stream.uniform(len(ds))]
        while d_b == d_a:
            d_b = ds[stream.uniform(len(ds))]
        p_a = d_to_pads[d_a][stream.uniform(len(d_to_pads[d_a]))]
        p_b = d_to_pads[d_b][stream.uniform(len(d_to_pads[d_b]))]
        a = _sample_word_at(d_a, p_a, stream)
        b = _sample_word_at(d_b, p_b, stream)
        if a in exclude or b in exclude:
            continue
        if displacement(a) == displacement(b):
            continue
        w1s.append(a)
        w2s.append(b)
    if len(w1s) < batch_pairs:
        raise RuntimeError("could not fill length-matched different-d batch")
    return w1s, w2s


def build_heldout_batch(stream: CounterStream) -> dict:
    """R2: fixed held-out pairs drawn once before training; words excluded from train."""
    _assert_path_clean("build_heldout", n=HOLDOUT_PAIRS)
    same_w1: list[bytes] = []
    same_w2: list[bytes] = []
    while len(same_w1) < HOLDOUT_PAIRS:
        need = min(PATH_BATCH, HOLDOUT_PAIRS - len(same_w1))
        w1s, w2s, _, _ = _sample_length_matched_positive_batch_once(
            stream,
            batch_pairs=need,
            roads_per_group=M_ROADS,
            shuffle_groups=False,
        )
        same_w1.extend(w1s)
        same_w2.extend(w2s)
    same_w1 = same_w1[:HOLDOUT_PAIRS]
    same_w2 = same_w2[:HOLDOUT_PAIRS]
    # Verify equal displacement (path-legal)
    for a, b in zip(same_w1, same_w2):
        if displacement(a) != displacement(b):
            raise RuntimeError("held-out same pair has unequal displacement")
    exclude_so_far = frozenset(same_w1) | frozenset(same_w2)
    diff_w1, diff_w2 = sample_length_matched_diff_batch(
        stream, batch_pairs=HOLDOUT_PAIRS, exclude_words=exclude_so_far
    )
    exclude = frozenset(same_w1) | frozenset(same_w2) | frozenset(diff_w1) | frozenset(
        diff_w2
    )
    return {
        "same_w1": same_w1,
        "same_w2": same_w2,
        "diff_w1": diff_w1,
        "diff_w2": diff_w2,
        "exclude_words": exclude,
        "n_same_pairs": len(same_w1),
        "n_diff_pairs": len(diff_w1),
        "n_exclude_words": len(exclude),
    }


def assert_batch_excludes(w1s: list[bytes], w2s: list[bytes], exclude: frozenset[bytes]) -> None:
    used = set(w1s) | set(w2s)
    hit = used & exclude
    if hit:
        raise RuntimeError(f"training batch leaked {len(hit)} held-out words")


def sample_contrastive_batch(
    stream: CounterStream,
    *,
    batch_pairs: int,
    exclude_words: frozenset[bytes] | None = None,
) -> tuple[list[bytes], list[bytes], list[bytes]]:
    """P0-neg: anchor, positive (same d), negative (different d), length-matched."""
    _assert_path_clean("contrastive_batch", batch_pairs=batch_pairs)
    exclude = exclude_words or frozenset()
    max_tries = 200
    for _ in range(max_tries):
        anchors, poss, negs = _sample_contrastive_batch_once(stream, batch_pairs=batch_pairs)
        used = set(anchors) | set(poss) | set(negs)
        if used.isdisjoint(exclude):
            return anchors, poss, negs
    raise RuntimeError("could not sample contrastive batch disjoint from held-out")


def _sample_contrastive_batch_once(
    stream: CounterStream, *, batch_pairs: int
) -> tuple[list[bytes], list[bytes], list[bytes]]:
    ell = _LENGTHS[stream.uniform(len(_LENGTHS))]
    options = _LENGTH_INDEX[ell]
    d_to_pads: dict[int, list[int]] = defaultdict(list)
    for d, p in options:
        d_to_pads[d].append(p)
    ds = list(d_to_pads.keys())
    anchors, poss, negs = [], [], []
    for _ in range(batch_pairs):
        d_pos = ds[stream.uniform(len(ds))]
        d_neg = ds[stream.uniform(len(ds))]
        while d_neg == d_pos and len(ds) > 1:
            d_neg = ds[stream.uniform(len(ds))]
        p_pos = d_to_pads[d_pos][stream.uniform(len(d_to_pads[d_pos]))]
        p_neg = d_to_pads[d_neg][stream.uniform(len(d_to_pads[d_neg]))]
        a = _sample_word_at(d_pos, p_pos, stream)
        b = _sample_word_at(d_pos, p_pos, stream)
        c = _sample_word_at(d_neg, p_neg, stream)
        anchors.append(a)
        poss.append(b)
        negs.append(c)
    return anchors, poss, negs


@torch.no_grad()
def eval_heldout_vicreg(
    models: list[ContactTransformer],
    projectors: list[VicregProjector] | None,
    heldout: dict,
) -> dict[str, float]:
    """R2: frozen-batch VICReg components (interpretable curve)."""
    for m in models:
        m.eval()
    if projectors:
        for p in projectors:
            p.eval()
    t1 = torch.stack([encode_word_self(w) for w in heldout["same_w1"]]).to(DEVICE)
    t2 = torch.stack([encode_word_self(w) for w in heldout["same_w2"]]).to(DEVICE)
    # Mean components across committee members (same scalar each would see).
    comps = []
    for i, model in enumerate(models):
        z1 = prehead(model, t1)
        z2 = prehead(model, t2)
        if projectors is not None:
            z1 = projectors[i](z1)
            z2 = projectors[i](z2)
        comps.append(vicreg_pair_components(z1, z2))
    keys = comps[0].keys()
    return {k: float(sum(c[k] for c in comps) / len(comps)) for k in keys}


@torch.no_grad()
def road_gap_metric(
    models: list[ContactTransformer],
    projectors: list[VicregProjector] | None,
    heldout: dict,
) -> dict[str, float]:
    """R3: align_same - align_diff on held-out; path-legal (exact-d only)."""
    _assert_path_clean("road_gap")
    for m in models:
        m.eval()
    t_s1 = torch.stack([encode_word_self(w) for w in heldout["same_w1"]])
    t_s2 = torch.stack([encode_word_self(w) for w in heldout["same_w2"]])
    t_d1 = torch.stack([encode_word_self(w) for w in heldout["diff_w1"]])
    t_d2 = torch.stack([encode_word_self(w) for w in heldout["diff_w2"]])
    z_s1 = committee_mean_projected(models, projectors, t_s1)
    z_s2 = committee_mean_projected(models, projectors, t_s2)
    z_d1 = committee_mean_projected(models, projectors, t_d1)
    z_d2 = committee_mean_projected(models, projectors, t_d2)
    z_s1 = F.normalize(z_s1, dim=-1)
    z_s2 = F.normalize(z_s2, dim=-1)
    z_d1 = F.normalize(z_d1, dim=-1)
    z_d2 = F.normalize(z_d2, dim=-1)
    align_same = float((z_s1 * z_s2).sum(dim=-1).mean().item())
    align_diff = float((z_d1 * z_d2).sum(dim=-1).mean().item())
    return {
        "align_same": align_same,
        "align_diff": align_diff,
        "road_gap": align_same - align_diff,
    }


# =============================================================================
# Losses
# =============================================================================


def _off_diagonal(x: torch.Tensor) -> torch.Tensor:
    n, m = x.shape
    assert n == m
    return x.flatten()[:-1].view(n - 1, n + 1)[:, 1:].flatten()


def vicreg_pair_loss(z1: torch.Tensor, z2: torch.Tensor) -> torch.Tensor:
    """Positive-only: align paired roads + VICReg anti-collapse (no negatives)."""
    inv = F.mse_loss(z1, z2)
    std_z1 = torch.sqrt(z1.var(dim=0) + 1e-4)
    std_z2 = torch.sqrt(z2.var(dim=0) + 1e-4)
    var = torch.mean(F.relu(1.0 - std_z1)) / 2 + torch.mean(F.relu(1.0 - std_z2)) / 2
    z1c = z1 - z1.mean(dim=0)
    z2c = z2 - z2.mean(dim=0)
    cov1 = (z1c.T @ z1c) / max(1, z1.shape[0] - 1)
    cov2 = (z2c.T @ z2c) / max(1, z2.shape[0] - 1)
    cov = (
        _off_diagonal(cov1).pow(2).sum() / z1.shape[1]
        + _off_diagonal(cov2).pow(2).sum() / z2.shape[1]
    ) / 2
    return VICREG_INV * inv + VICREG_VAR * var + VICREG_COV * cov


def vicreg_pair_components(z1: torch.Tensor, z2: torch.Tensor) -> dict[str, float]:
    """R1: same algebra as vicreg_pair_loss; returns components (not used in optim)."""
    inv = F.mse_loss(z1, z2)
    std_z1 = torch.sqrt(z1.var(dim=0) + 1e-4)
    std_z2 = torch.sqrt(z2.var(dim=0) + 1e-4)
    var = torch.mean(F.relu(1.0 - std_z1)) / 2 + torch.mean(F.relu(1.0 - std_z2)) / 2
    z1c = z1 - z1.mean(dim=0)
    z2c = z2 - z2.mean(dim=0)
    cov1 = (z1c.T @ z1c) / max(1, z1.shape[0] - 1)
    cov2 = (z2c.T @ z2c) / max(1, z2.shape[0] - 1)
    cov = (
        _off_diagonal(cov1).pow(2).sum() / z1.shape[1]
        + _off_diagonal(cov2).pow(2).sum() / z2.shape[1]
    ) / 2
    total = VICREG_INV * inv + VICREG_VAR * var + VICREG_COV * cov
    return {
        "loss_total": float(total.detach().item()),
        "inv_term": float((VICREG_INV * inv).detach().item()),
        "var_term": float((VICREG_VAR * var).detach().item()),
        "cov_term": float((VICREG_COV * cov).detach().item()),
        "mean_std": float(
            (0.5 * (std_z1.mean() + std_z2.mean())).detach().item()
        ),
    }


class VicregProjector(torch.nn.Module):
    """Section-3 conditional fix only: expander terminated by BatchNorm1d."""

    def __init__(self, in_dim: int = D_MODEL, hidden: int = PROJECTOR_HIDDEN):
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(in_dim, hidden),
            torch.nn.BatchNorm1d(hidden),
            torch.nn.ReLU(inplace=True),
            torch.nn.Linear(hidden, hidden),
            torch.nn.BatchNorm1d(hidden),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


def make_projectors(n: int) -> list[VicregProjector] | None:
    if not USE_BN_PROJECTOR:
        return None
    return [VicregProjector().to(DEVICE) for _ in range(n)]


def project_acts(
    models: Sequence[ContactTransformer],
    projectors: list[VicregProjector] | None,
    tokens: torch.Tensor,
    *,
    with_grad: bool = False,
) -> list[torch.Tensor]:
    """Per-model projected prehead (or raw prehead if no projector)."""
    outs = []
    for i, model in enumerate(models):
        z = prehead_grad(model, tokens) if with_grad else prehead(model, tokens)
        if projectors is not None:
            if with_grad:
                projectors[i].train()
            else:
                projectors[i].eval()
            z = projectors[i](z)
        outs.append(z)
    return outs


def committee_mean_projected(
    models: Sequence[ContactTransformer],
    projectors: list[VicregProjector] | None,
    tokens: torch.Tensor,
    *,
    chunk: int = 64,
) -> torch.Tensor:
    outs = []
    with torch.no_grad():
        for start in range(0, tokens.shape[0], chunk):
            sl = tokens[start : start + chunk].to(DEVICE)
            if projectors is None:
                vecs = torch.stack([prehead(m, sl) for m in models], dim=0).mean(dim=0)
            else:
                for p in projectors:
                    p.eval()
                vecs = torch.stack(
                    [projectors[i](prehead(m, sl)) for i, m in enumerate(models)],
                    dim=0,
                ).mean(dim=0)
            outs.append(vecs.cpu())
    return torch.cat(outs, dim=0)


def contrastive_loss(
    za: torch.Tensor, zp: torch.Tensor, zn: torch.Tensor, *, temp: float = CONTRAST_TEMP
) -> torch.Tensor:
    """Naive exact-d contrastive (P0-neg instrument)."""
    za = F.normalize(za, dim=-1)
    zp = F.normalize(zp, dim=-1)
    zn = F.normalize(zn, dim=-1)
    pos = (za * zp).sum(dim=-1) / temp
    neg = (za * zn).sum(dim=-1) / temp
    # Binary: prefer pos over neg
    logits = torch.stack([pos, neg], dim=-1)
    labels = torch.zeros(za.shape[0], dtype=torch.long, device=za.device)
    return F.cross_entropy(logits, labels)


# =============================================================================
# K-set / destination
# =============================================================================


def compute_n_max_and_k(public_key, partition) -> tuple[int, int, tuple[int, ...]]:
    schedule = curated_rich_equal_schedule(public_key, partition)
    n_max = len(schedule)
    if n_max != N_MAX:
        raise RuntimeError(f"N_max drifted: got {n_max}, locked {N_MAX}")
    k = n_max // 8
    if k != K:
        raise RuntimeError(f"K drifted: got {k}, locked {K}")
    print(f"N_max={n_max}; K=floor(N_max/8)={k}", flush=True)
    return n_max, k, schedule


def build_k_set(
    public_key,
    partition,
    schedule: tuple[int, ...],
    seed: int,
    k: int,
) -> tuple[list[tuple[bytes, bytes]], list[int], str]:
    """Label-balanced K distinct labeled pairs from DIAG_04 curated pool order.

    Path firewall: this is DESTINATION sampling — may use oracle_eq for labels.
    """
    stream = CounterStream(
        dummy_key(f"successor-dev-b2-pilot-seed-{seed}", purpose="public-root"),
        ("L1", "b2-pilot", "k-set", seed),
    )
    equals: list[tuple[bytes, bytes]] = []
    unequals: list[tuple[bytes, bytes]] = []
    # Walk shuffled schedule indices for diversity.
    order = shuffled(list(range(len(schedule))), stream)
    for idx in order:
        raw = realize_pool_index(partition, public_key, schedule[idx])
        pair = _pair_key(raw.left, raw.right)
        if oracle_eq(raw.left, raw.right, MODULUS):
            if pair not in equals:
                equals.append(pair)
        else:
            if pair not in unequals:
                unequals.append(pair)
        if len(equals) >= k // 2 and len(unequals) >= k - k // 2:
            break
    n_eq = k // 2
    n_neq = k - n_eq
    selected = equals[:n_eq] + unequals[:n_neq]
    if len(selected) != k:
        raise RuntimeError(f"could not build balanced K-set: got {len(selected)}")
    selected = shuffled(selected, stream)
    labels = [int(oracle_eq(a, b, MODULUS)) for a, b in selected]
    return selected, labels, _hash_pairs(selected)


def _stack_pairs(pairs: Sequence[tuple[bytes, bytes]]) -> torch.Tensor:
    return torch.stack([encode_pair(a, b) for a, b in pairs]).to(DEVICE)


# =============================================================================
# Training loops
# =============================================================================


def new_committee(seed: int) -> list[ContactTransformer]:
    key = dummy_key(f"successor-dev-b2-pilot-seed-{seed}", purpose="public-root")
    models, _ = _committee(key, block=WORLD_SLOT)
    models = [m.to(DEVICE) for m in models]
    for m in models:
        m.train()
    return models


def path_train_p0(
    models: list[ContactTransformer],
    stream: CounterStream,
    *,
    steps: int,
    shuffle_groups: bool = False,
    heldout: dict | None = None,
    projectors: list[VicregProjector] | None = None,
) -> tuple[float, list[dict], list[dict]]:
    """Positive-only VICReg path. Returns wall seconds, train_logs, heldout_logs."""
    opts = [build_optimizer(m) for m in models]
    proj_opts = (
        [torch.optim.Adam(p.parameters(), lr=1e-3, weight_decay=1e-4) for p in projectors]
        if projectors is not None
        else []
    )
    exclude = heldout["exclude_words"] if heldout is not None else frozenset()
    train_logs: list[dict] = []
    heldout_logs: list[dict] = []
    t0 = time.perf_counter()
    last_loss = 0.0
    last_ell = -1
    for step in range(1, steps + 1):
        w1s, w2s, _, _ell = sample_length_matched_positive_batch(
            stream,
            batch_pairs=PATH_BATCH,
            roads_per_group=M_ROADS,
            shuffle_groups=shuffle_groups,
            exclude_words=exclude,
        )
        assert_batch_excludes(w1s, w2s, exclude)
        t1 = torch.stack([encode_word_self(w) for w in w1s]).to(DEVICE)
        t2 = torch.stack([encode_word_self(w) for w in w2s]).to(DEVICE)
        step_comps = []
        for i, (model, opt) in enumerate(zip(models, opts)):
            model.train()
            opt.zero_grad(set_to_none=True)
            if projectors is not None:
                proj_opts[i].zero_grad(set_to_none=True)
                projectors[i].train()
            z1 = prehead_grad(model, t1)
            z2 = prehead_grad(model, t2)
            if projectors is not None:
                z1 = projectors[i](z1)
                z2 = projectors[i](z2)
            loss = vicreg_pair_loss(z1, z2)
            loss.backward()
            opt.step()
            if projectors is not None:
                proj_opts[i].step()
            step_comps.append(vicreg_pair_components(z1.detach(), z2.detach()))
        last_loss = float(sum(c["loss_total"] for c in step_comps) / len(step_comps))
        last_ell = int(_ell)
        if step % LOG_CADENCE == 0:
            train_entry = {
                "step": step,
                "loss_total": last_loss,
                "inv_term": float(sum(c["inv_term"] for c in step_comps) / len(step_comps)),
                "var_term": float(sum(c["var_term"] for c in step_comps) / len(step_comps)),
                "cov_term": float(sum(c["cov_term"] for c in step_comps) / len(step_comps)),
                "mean_std": float(sum(c["mean_std"] for c in step_comps) / len(step_comps)),
                "ell": last_ell,
                "not_interpretable": True,
            }
            train_logs.append(train_entry)
            print(
                f"  path step={step}/{steps} train_loss={last_loss:.4f} "
                f"ell={last_ell} (not_interpretable)",
                flush=True,
            )
            if heldout is not None:
                h = eval_heldout_vicreg(models, projectors, heldout)
                h_entry = {"step": step, **h, "not_interpretable": False}
                heldout_logs.append(h_entry)
                print(
                    f"  heldout step={step} loss={h['loss_total']:.4f} "
                    f"inv={h['inv_term']:.4f} var={h['var_term']:.4f} "
                    f"cov={h['cov_term']:.4f} mean_std={h['mean_std']:.4f}",
                    flush=True,
                )
    return time.perf_counter() - t0, train_logs, heldout_logs


def path_train_p0_neg(
    models: list[ContactTransformer],
    stream: CounterStream,
    *,
    steps: int,
    exclude_words: frozenset[bytes] | None = None,
) -> float:
    opts = [build_optimizer(m) for m in models]
    exclude = exclude_words or frozenset()
    t0 = time.perf_counter()
    for step in range(1, steps + 1):
        a, p, n = sample_contrastive_batch(
            stream, batch_pairs=PATH_BATCH, exclude_words=exclude
        )
        assert_batch_excludes(a + p, n, exclude)
        ta = torch.stack([encode_word_self(w) for w in a]).to(DEVICE)
        tp = torch.stack([encode_word_self(w) for w in p]).to(DEVICE)
        tn = torch.stack([encode_word_self(w) for w in n]).to(DEVICE)
        for model, opt in zip(models, opts):
            opt.zero_grad(set_to_none=True)
            za = prehead_grad(model, ta)
            zp = prehead_grad(model, tp)
            zn = prehead_grad(model, tn)
            loss = contrastive_loss(za, zp, zn)
            loss.backward()
            opt.step()
        if step % LOG_CADENCE == 0:
            print(f"  p0-neg step={step}/{steps} loss={float(loss):.4f}", flush=True)
    return time.perf_counter() - t0


def destination_train(
    models: list[ContactTransformer],
    pairs: Sequence[tuple[bytes, bytes]],
    labels: Sequence[int],
    *,
    horizon: int,
    freeze_trunk: bool = False,
) -> tuple[float, dict[int, bool], list[dict]]:
    """Oracle-stage CE on fixed K-set for `horizon` steps. Returns wall, qualifying, strip."""
    tokens = _stack_pairs(pairs)
    labs = torch.tensor(list(labels), dtype=torch.long, device=DEVICE)
    if freeze_trunk:
        for m in models:
            for name, p in m.named_parameters():
                p.requires_grad = name in ("head_W", "head_b")
    opts = [build_optimizer(m) for m in models]
    # Fresh capability per destination run (cap BUDGET).
    cap = feasibility_v2_capability()
    cap.claim_development_world(WORLD_SLOT)
    if horizon > BUDGET:
        raise RuntimeError("horizon exceeds trajectory cap")

    # Panel for checkpoints — loaded by caller via closure? Pass later.
    # We'll checkpoint outside; here only train and return.
    t0 = time.perf_counter()
    for step in range(1, horizon + 1):
        loss_result, _ = runner.memory_safe_feasibility_committee_step(
            models, opts, tokens, labs, cap, microbatch=MICROBATCH
        )
        if not loss_result.finite:
            raise RuntimeError(f"non-finite at dest step {step}")
        if step % 100 == 0:
            print(f"  dest step={step}/{horizon}", flush=True)
    wall = time.perf_counter() - t0
    if freeze_trunk:
        for m in models:
            for p in m.parameters():
                p.requires_grad = True
    return wall, {}, []


def score_panel_committee(models, panel: DummyPanel) -> tuple[bool, dict[str, StratumScore], dict]:
    for m in models:
        m.eval()
    toks = torch.stack(
        [encode_pair(it.left, it.right).to(DEVICE) for it in panel.items]
    )
    with torch.no_grad():
        probs = committee_equal_probability(models, toks).detach().cpu()
    obs = [
        PanelObservation(it.stratum, it.truth, float(p))
        for it, p in zip(panel.items, probs.tolist())
    ]
    by = {}
    for name in PANEL_STRATUM_COUNTS:
        vals = [o for o in obs if o.stratum == name]
        by[name] = score_stratum(name, vals)
    qualifies = checkpoint_qualifies(obs)
    detail = {
        name: {
            "correct": by[name].correct,
            "need": ACCURACY_MINIMUM[name],
            "abst": by[name].abstentions,
            "lies": by[name].confident_lies,
            "brier": by[name].brier,
            "qualifies": by[name].qualifies,
        }
        for name in PANEL_STRATUM_COUNTS
    }
    for m in models:
        m.train()
    return qualifies, by, detail


def fit_linear_equality_readout(
    models: list[ContactTransformer],
    stream: CounterStream,
    *,
    n_train: int = 2000,
    epochs: int = READOUT_EPOCHS,
    exclude_words: frozenset[bytes] | None = None,
) -> Callable[[torch.Tensor], torch.Tensor]:
    """Read-only linear equal? from frozen trunk; labels = exact-d sameness (path notion).

    Never uses oracle/modulus — path-legal labels only.
    """
    _assert_path_clean("fit_readout", n_train=n_train)
    exclude = exclude_words or frozenset()
    w1s, w2s, _, _ = sample_length_matched_positive_batch(
        stream,
        batch_pairs=n_train // 2,
        roads_per_group=M_ROADS,
        shuffle_groups=False,
        exclude_words=exclude,
    )
    # Negatives: reshuffle pairings across different groups → mostly different d.
    w1n, w2n, _, _ = sample_length_matched_positive_batch(
        stream,
        batch_pairs=n_train // 2,
        roads_per_group=M_ROADS,
        shuffle_groups=True,
        exclude_words=exclude,
    )
    pairs = [(a, b, 1) for a, b in zip(w1s, w2s)] + [(a, b, 0) for a, b in zip(w1n, w2n)]
    # Exact label by displacement sameness (path signal).
    labeled = []
    for a, b, _ in pairs:
        labeled.append((a, b, int(displacement(a) == displacement(b))))
    toks = torch.stack([encode_pair(a, b) for a, b, _ in labeled])
    y = torch.tensor([lab for _, _, lab in labeled], dtype=torch.long)
    with torch.no_grad():
        for m in models:
            m.eval()
        x = committee_mean_prehead(models, toks)
    mean = x.mean(0, keepdim=True)
    std = x.std(0, keepdim=True).clamp_min(1e-6)
    x = (x - mean) / std
    W = torch.zeros(D_MODEL, 2, requires_grad=True)
    b = torch.zeros(2, requires_grad=True)
    opt = torch.optim.Adam([W, b], lr=0.05, weight_decay=1e-2)
    x_dev = x  # CPU ok for small probe
    for _ in range(epochs):
        logits = x_dev @ W + b
        loss = F.cross_entropy(logits, y)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()
    W_f, b_f, mean_f, std_f = W.detach(), b.detach(), mean, std

    def predict_p_equal(pair_tokens: torch.Tensor) -> torch.Tensor:
        with torch.no_grad():
            for m in models:
                m.eval()
            acts = committee_mean_prehead(models, pair_tokens.cpu())
            acts = (acts - mean_f) / std_f
            probs = torch.softmax(acts @ W_f + b_f, dim=-1)[:, 1]
        return probs

    return predict_p_equal


def score_panel_readout(
    predict_p_equal: Callable[[torch.Tensor], torch.Tensor], panel: DummyPanel
) -> tuple[bool, dict, dict]:
    toks = torch.stack([encode_pair(it.left, it.right) for it in panel.items])
    probs = predict_p_equal(toks)
    obs = [
        PanelObservation(it.stratum, it.truth, float(p))
        for it, p in zip(panel.items, probs.tolist())
    ]
    by = {}
    for name in PANEL_STRATUM_COUNTS:
        vals = [o for o in obs if o.stratum == name]
        by[name] = score_stratum(name, vals)
    detail = {
        name: {
            "correct": by[name].correct,
            "need": ACCURACY_MINIMUM[name],
            "abst": by[name].abstentions,
            "lies": by[name].confident_lies,
            "brier": by[name].brier,
            "qualifies": by[name].qualifies,
        }
        for name in PANEL_STRATUM_COUNTS
    }
    # Per-item wrap diagnostics
    wrap_items = []
    for it, p in zip(panel.items, probs.tolist()):
        if it.truth and it.difference in (MODULUS, 2 * MODULUS):
            obs_i = PanelObservation(it.stratum, True, float(p))
            wrap_items.append(
                {
                    "stratum": it.stratum,
                    "diff": it.difference,
                    "p_equal": float(p),
                    "correct": obs_i.correct,
                    "anti_correct": (not obs_i.abstains) and (not obs_i.prediction),
                }
            )
    detail["_wrap"] = wrap_items
    return checkpoint_qualifies(obs), by, detail


def first_persistent_oracle_clock(qualifying: dict[int, bool], horizon: int) -> int | None:
    """Same rule as frozen first_persistent_step, on oracle clock 0..horizon."""
    steps = tuple(range(0, horizon + 1, CHECKPOINT_CADENCE))
    missing = [s for s in steps if s not in qualifying]
    if missing:
        raise RuntimeError(f"missing oracle checkpoint {missing[0]}")
    for i in range(len(steps) - PERSISTENCE_CHECKPOINTS + 1):
        window = steps[i : i + PERSISTENCE_CHECKPOINTS]
        if all(qualifying[s] for s in window):
            return window[0]
    return None


def destination_train_with_checkpoints(
    models: list[ContactTransformer],
    pairs: Sequence[tuple[bytes, bytes]],
    labels: Sequence[int],
    panel: DummyPanel,
    *,
    horizon: int,
    freeze_trunk: bool = False,
) -> tuple[float, int | None, dict, list]:
    tokens = _stack_pairs(pairs)
    labs = torch.tensor(list(labels), dtype=torch.long, device=DEVICE)
    if freeze_trunk:
        for m in models:
            for name, p in m.named_parameters():
                p.requires_grad = name in ("head_W", "head_b")
    opts = [build_optimizer(m) for m in models]
    cap = feasibility_v2_capability()
    cap.claim_development_world(WORLD_SLOT)
    qualifying: dict[int, bool] = {}
    strip: list[dict] = []
    t0 = time.perf_counter()

    def ckpt(step: int) -> None:
        q, _, detail = score_panel_committee(models, panel)
        qualifying[step] = q
        strip.append({"step": step, "qualifies": q, "strata": detail})
        print(
            f"  ckpt oracle_step={step} qualifies={q} "
            f"S3={detail['S3']['qualifies']} S2={detail['S2']['qualifies']}",
            flush=True,
        )

    ckpt(0)
    for step in range(1, horizon + 1):
        loss_result, _ = runner.memory_safe_feasibility_committee_step(
            models, opts, tokens, labs, cap, microbatch=MICROBATCH
        )
        if not loss_result.finite:
            raise RuntimeError(f"non-finite dest step {step}")
        if step % CHECKPOINT_CADENCE == 0:
            ckpt(step)
    wall = time.perf_counter() - t0
    if freeze_trunk:
        for m in models:
            for p in m.parameters():
                p.requires_grad = True
    persistent = first_persistent_oracle_clock(qualifying, horizon)
    final = strip[-1]["strata"] if strip else {}
    return wall, persistent, final, strip


# =============================================================================
# Mechanism probes (read-only)
# =============================================================================


def _fit_probe(x_tr, y_tr, x_te, y_te, n_classes: int, epochs: int = PROBE_EPOCHS) -> float:
    mean = x_tr.mean(0, keepdim=True)
    std = x_tr.std(0, keepdim=True).clamp_min(1e-6)
    x_tr = (x_tr - mean) / std
    x_te = (x_te - mean) / std
    W = torch.zeros(x_tr.shape[1], n_classes, requires_grad=True)
    b = torch.zeros(n_classes, requires_grad=True)
    opt = torch.optim.Adam([W, b], lr=0.05, weight_decay=1e-2)
    for _ in range(epochs):
        loss = F.cross_entropy(x_tr @ W + b, y_tr)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()
    with torch.no_grad():
        pred = (x_te @ W + b).argmax(-1)
        return float((pred == y_te).float().mean().item())


def run_mechanism_probes(
    models: list[ContactTransformer], stream: CounterStream, tag: str
) -> dict:
    """Displacement / length-control / sign(d) / residue probes on frozen acts."""
    print(f"  mechanism probes [{tag}]...", flush=True)
    for m in models:
        m.eval()

    from collections import Counter

    words: list[bytes] = []
    ds: list[int] = []
    lengths: list[int] = []

    def _append_uniform(n_draw: int) -> None:
        for _ in range(n_draw):
            ell = _LENGTHS[stream.uniform(len(_LENGTHS))]
            opts = _LENGTH_INDEX[ell]
            d, p = opts[stream.uniform(len(opts))]
            w = _sample_word_at(d, p, stream)
            words.append(w)
            ds.append(d)
            lengths.append(ell)

    _append_uniform(PROBE_CORPUS_TARGET)
    d_within: float | str = "INSUFFICIENT"
    within_n = 0
    corpus_n = len(words)

    while True:
        toks = torch.stack([encode_word_self(w) for w in words])
        acts = committee_mean_prehead(models, toks)
        unique_ds = sorted(set(ds))
        if len(unique_ds) > 40:
            unique_ds = unique_ds[:: max(1, len(unique_ds) // 40)][:40]
        d_to_id = {d: i for i, d in enumerate(unique_ds)}
        mask = [d in d_to_id for d in ds]
        x = acts[torch.tensor(mask)]
        y_d = torch.tensor([d_to_id[d] for d, m in zip(ds, mask) if m], dtype=torch.long)
        y_len = torch.tensor([lengths[i] for i, m in enumerate(mask) if m], dtype=torch.long)
        uniq_l = sorted(set(y_len.tolist()))
        l_to_id = {l: i for i, l in enumerate(uniq_l)}
        y_l = torch.tensor([l_to_id[int(v)] for v in y_len.tolist()], dtype=torch.long)

        len_counts = Counter(int(v) for v in y_len.tolist())
        top_ell = max(len_counts, key=len_counts.get)
        within = [i for i in range(x.shape[0]) if int(y_len[i]) == top_ell]
        within_n = len(within)
        corpus_n = len(words)
        if within_n >= PROBE_WITHIN_MIN:
            xw = x[within]
            yw = y_d[within]
            present = sorted(set(yw.tolist()))
            remap = {old: i for i, old in enumerate(present)}
            yw2 = torch.tensor([remap[int(v)] for v in yw.tolist()], dtype=torch.long)
            pw = torch.randperm(len(within))
            n_te_w = max(1, len(within) // 3)
            d_within = _fit_probe(
                xw[pw[n_te_w:]],
                yw2[pw[n_te_w:]],
                xw[pw[:n_te_w]],
                yw2[pw[:n_te_w]],
                len(present),
            )
            break
        if corpus_n >= PROBE_CORPUS_CAP:
            d_within = "INSUFFICIENT"
            break
        # Oversample top length stratum.
        raw_counts = Counter(lengths)
        top_raw = max(raw_counts, key=raw_counts.get)
        opts = _LENGTH_INDEX[top_raw]
        for _ in range(2000):
            d, p = opts[stream.uniform(len(opts))]
            w = _sample_word_at(d, p, stream)
            words.append(w)
            ds.append(d)
            lengths.append(top_raw)

    n = x.shape[0]
    perm = torch.randperm(n)
    n_te = max(1, n // 3)
    te, tr = perm[:n_te], perm[n_te:]
    d_acc = _fit_probe(x[tr], y_d[tr], x[te], y_d[te], len(d_to_id))
    len_acc = _fit_probe(x[tr], y_l[tr], x[te], y_l[te], len(l_to_id))

    sign_x = []
    sign_y = []
    abs_set = sorted({abs(d) for d in unique_ds if d != 0})
    for abs_d in abs_set[:30]:
        for sign, lab in ((+1, 1), (-1, 0)):
            d = sign * abs_d
            if d not in d_to_pads_safe(abs_d):
                continue
            for ell in _LENGTHS:
                opts = [(dd, pp) for dd, pp in _LENGTH_INDEX[ell] if dd == d]
                if not opts:
                    continue
                dd, pp = opts[0]
                for _ in range(8):
                    w = _sample_word_at(dd, pp, stream)
                    sign_x.append(w)
                    sign_y.append(lab)
                break
    if len(sign_x) >= 40:
        stx = committee_mean_prehead(
            models, torch.stack([encode_word_self(w) for w in sign_x])
        )
        sty = torch.tensor(sign_y, dtype=torch.long)
        sp = torch.randperm(len(sign_y))
        n_te_s = max(1, len(sign_y) // 3)
        sign_acc = _fit_probe(
            stx[sp[n_te_s:]], sty[sp[n_te_s:]], stx[sp[:n_te_s]], sty[sp[:n_te_s]], 2
        )
    else:
        sign_acc = float("nan")

    res_words, res_d, res_y = [], [], []
    for _ in range(3000):
        ell = _LENGTHS[stream.uniform(len(_LENGTHS))]
        opts = _LENGTH_INDEX[ell]
        d, p = opts[stream.uniform(len(opts))]
        w = _sample_word_at(d, p, stream)
        res_words.append(w)
        res_d.append(d)
        res_y.append(fold(w, MODULUS))
    all_d = sorted(set(res_d))
    mid = len(all_d) // 2
    d_train_set = set(all_d[:mid])
    d_test_set = set(all_d[mid:])
    tr_idx = [i for i, d in enumerate(res_d) if d in d_train_set]
    te_idx = [i for i, d in enumerate(res_d) if d in d_test_set]
    rx = committee_mean_prehead(
        models, torch.stack([encode_word_self(w) for w in res_words])
    )
    if tr_idx and te_idx:
        residue_acc = _fit_probe(
            rx[tr_idx],
            torch.tensor([res_y[i] for i in tr_idx], dtype=torch.long),
            rx[te_idx],
            torch.tensor([res_y[i] for i in te_idx], dtype=torch.long),
            MODULUS,
            epochs=PROBE_EPOCHS,
        )
    else:
        residue_acc = float("nan")

    chance_d = 1.0 / max(1, len(d_to_id))
    return {
        "tag": tag,
        "exact_d_acc": d_acc,
        "exact_d_chance": chance_d,
        "length_only_acc": len_acc,
        "length_chance": 1.0 / max(1, len(l_to_id)),
        "exact_d_within_length_acc": d_within,
        "exact_d_within_length_n": within_n,
        "probe_corpus_n": corpus_n,
        "sign_d_acc": sign_acc,
        "sign_d_chance": 0.5,
        "residue_acc_disjoint_d": residue_acc,
        "residue_chance": 1.0 / MODULUS,
    }


def probe_deltas(trained: dict, init: dict) -> dict:
    """R4: delta = trained - matched init."""
    keys = (
        "exact_d_acc",
        "length_only_acc",
        "sign_d_acc",
        "residue_acc_disjoint_d",
    )
    deltas = {}
    for k in keys:
        tv, iv = trained[k], init[k]
        if isinstance(tv, (int, float)) and isinstance(iv, (int, float)):
            deltas[f"delta_{k}"] = float(tv) - float(iv)
        else:
            deltas[f"delta_{k}"] = None
    tv = trained["exact_d_within_length_acc"]
    iv = init["exact_d_within_length_acc"]
    if isinstance(tv, (int, float)) and isinstance(iv, (int, float)):
        deltas["delta_exact_d_within_length_acc"] = float(tv) - float(iv)
    else:
        deltas["delta_exact_d_within_length_acc"] = "INSUFFICIENT"
        deltas["exact_d_within_length_n_trained"] = trained.get("exact_d_within_length_n")
        deltas["exact_d_within_length_n_init"] = init.get("exact_d_within_length_n")
    return deltas


def d_to_pads_safe(abs_d: int) -> set[int]:
    return {d for d in range(_D_PATH_LO, _D_PATH_HI + 1) if abs(d) == abs_d}


# =============================================================================
# Overlap report
# =============================================================================


def displacement_class_overlap(path_ds: set[int], panel: DummyPanel) -> dict:
    """Report |d| overlap between path support and panel cell differences."""
    panel_diffs = {it.difference for it in panel.items}
    # Path uses signed d; panel cells use nonnegative difference.
    path_abs = {abs(d) for d in path_ds}
    return {
        "path_abs_d_count": len(path_abs),
        "panel_diff_count": len(panel_diffs),
        "abs_d_intersect_panel_diff": sorted(path_abs & panel_diffs),
        "n_overlap": len(path_abs & panel_diffs),
        "note": (
            "word-level intersect=0 does not establish content independence: "
            "path road-pool and panel can still share displacement classes."
        ),
    }


# =============================================================================
# Arm runners
# =============================================================================



@dataclass
class ArmResult:
    arm: str
    seed: int
    k_hash: str
    path_wall_s: float = 0.0
    dest_wall_s: float = 0.0
    first_persistent_step: int | None = None
    strata: dict = field(default_factory=dict)
    probes: dict = field(default_factory=dict)
    probe_deltas: dict = field(default_factory=dict)
    road_gaps: dict = field(default_factory=dict)
    train_logs: list = field(default_factory=list)
    heldout_logs: list = field(default_factory=list)
    wrap_anti_correct: int | None = None
    wrap_n: int | None = None
    scoring_mode: str = "committee_head"


def run_seed(
    seed: int,
    public_key,
    partition,
    panel: DummyPanel,
    schedule: tuple[int, ...],
    path_d_support: set[int],
    heldout: dict,
) -> list[ArmResult]:
    results: list[ArmResult] = []
    pairs, labels, k_hash = build_k_set(public_key, partition, schedule, seed, K)
    panel_pairs = {_pair_key(it.left, it.right) for it in panel.items}
    if set(pairs) & panel_pairs:
        raise RuntimeError("K-set ∩ panel nonempty")
    exclude = heldout["exclude_words"]
    print(
        f"\n=== SEED {seed} K={K} k_hash={k_hash} heldout_words={len(exclude)} "
        f"USE_BN_PROJECTOR={USE_BN_PROJECTOR} ===",
        flush=True,
    )

    def path_stream(tag: str) -> CounterStream:
        return CounterStream(
            dummy_key(f"successor-dev-b2-pilot-seed-{seed}", purpose="public-root"),
            ("L1", "b2-pilot", "path", seed, tag),
        )

    # --- D ---
    print(f"[seed {seed}] arm D...", flush=True)
    models = new_committee(seed)
    probes_init = run_mechanism_probes(models, path_stream("probe-init-D"), "init")
    dest_wall, persistent, strata, _ = destination_train_with_checkpoints(
        models, pairs, labels, panel, horizon=H_DEST, freeze_trunk=False
    )
    probes_d = run_mechanism_probes(models, path_stream("probe-D"), "D")
    results.append(
        ArmResult(
            "D", seed, k_hash,
            dest_wall_s=dest_wall,
            first_persistent_step=persistent,
            strata=strata,
            probes={"init": probes_init, "D": probes_d},
            probe_deltas=probe_deltas(probes_d, probes_init),
            scoring_mode="committee_head",
        )
    )

    # --- P0 ---
    print(f"[seed {seed}] arm P0...", flush=True)
    models = new_committee(seed)
    projectors = make_projectors(len(models))
    probes_init = run_mechanism_probes(models, path_stream("probe-init-P0"), "init")
    rg_init = road_gap_metric(models, projectors, heldout)
    path_wall, train_logs, heldout_logs = path_train_p0(
        models, path_stream("P0"), steps=M_PATH, shuffle_groups=False,
        heldout=heldout, projectors=projectors,
    )
    probes_p0 = run_mechanism_probes(models, path_stream("probe-P0"), "P0")
    rg_p0 = road_gap_metric(models, projectors, heldout)
    readout = fit_linear_equality_readout(
        models, path_stream("readout-P0"), exclude_words=exclude
    )
    _, _, detail = score_panel_readout(readout, panel)
    wrap = detail.pop("_wrap")
    anti = sum(1 for w in wrap if w["anti_correct"])
    results.append(
        ArmResult(
            "P0", seed, k_hash,
            path_wall_s=path_wall,
            strata=detail,
            probes={"init": probes_init, "P0": probes_p0},
            probe_deltas=probe_deltas(probes_p0, probes_init),
            road_gaps={"init": rg_init, "P0": rg_p0},
            train_logs=train_logs,
            heldout_logs=heldout_logs,
            wrap_anti_correct=anti,
            wrap_n=len(wrap),
            scoring_mode="path_exact_d_linear_readout",
        )
    )

    # --- P0-neg ---
    print(f"[seed {seed}] arm P0-neg...", flush=True)
    models = new_committee(seed)
    probes_init = run_mechanism_probes(models, path_stream("probe-init-P0neg"), "init")
    path_wall = path_train_p0_neg(
        models, path_stream("P0-neg"), steps=M_PATH, exclude_words=exclude
    )
    probes_tr = run_mechanism_probes(models, path_stream("probe-P0neg"), "P0-neg")
    readout = fit_linear_equality_readout(
        models, path_stream("readout-P0neg"), exclude_words=exclude
    )
    _, _, detail = score_panel_readout(readout, panel)
    wrap = detail.pop("_wrap")
    anti = sum(1 for w in wrap if w["anti_correct"])
    results.append(
        ArmResult(
            "P0-neg", seed, k_hash,
            path_wall_s=path_wall,
            strata=detail,
            probes={"init": probes_init, "P0-neg": probes_tr},
            probe_deltas=probe_deltas(probes_tr, probes_init),
            wrap_anti_correct=anti,
            wrap_n=len(wrap),
            scoring_mode="path_exact_d_linear_readout",
        )
    )

    # --- P+ ---
    print(f"[seed {seed}] arm P+...", flush=True)
    models = new_committee(seed)
    projectors = make_projectors(len(models))
    probes_init = run_mechanism_probes(models, path_stream("probe-init-Pplus"), "init")
    path_wall, train_logs, heldout_logs = path_train_p0(
        models, path_stream("Pplus-path"), steps=M_PATH, shuffle_groups=False,
        heldout=heldout, projectors=projectors,
    )
    probes_p0b = run_mechanism_probes(models, path_stream("probe-Pplus-pre"), "P0preP+")
    dest_wall, persistent, strata, _ = destination_train_with_checkpoints(
        models, pairs, labels, panel, horizon=H_DEST, freeze_trunk=True
    )
    probes_pp = run_mechanism_probes(models, path_stream("probe-Pplus"), "P+")
    results.append(
        ArmResult(
            "P+", seed, k_hash,
            path_wall_s=path_wall,
            dest_wall_s=dest_wall,
            first_persistent_step=persistent,
            strata=strata,
            probes={"init": probes_init, "P0pre": probes_p0b, "P+": probes_pp},
            probe_deltas=probe_deltas(probes_pp, probes_init),
            train_logs=train_logs,
            heldout_logs=heldout_logs,
            scoring_mode="committee_head_frozen_trunk",
        )
    )

    # --- P_shuf ---
    print(f"[seed {seed}] arm P_shuf...", flush=True)
    models = new_committee(seed)
    projectors = make_projectors(len(models))
    probes_init = run_mechanism_probes(models, path_stream("probe-init-Pshuf"), "init")
    rg_init = road_gap_metric(models, projectors, heldout)
    path_wall, train_logs, heldout_logs = path_train_p0(
        models, path_stream("Pshuf-path"), steps=M_PATH, shuffle_groups=True,
        heldout=heldout, projectors=projectors,
    )
    rg_shuf = road_gap_metric(models, projectors, heldout)
    probes_tr = run_mechanism_probes(models, path_stream("probe-Pshuf"), "P_shuf")
    dest_wall, persistent, strata, _ = destination_train_with_checkpoints(
        models, pairs, labels, panel, horizon=H_DEST, freeze_trunk=True
    )
    results.append(
        ArmResult(
            "P_shuf", seed, k_hash,
            path_wall_s=path_wall,
            dest_wall_s=dest_wall,
            first_persistent_step=persistent,
            strata=strata,
            probes={"init": probes_init, "P_shuf": probes_tr},
            probe_deltas=probe_deltas(probes_tr, probes_init),
            road_gaps={"init": rg_init, "P_shuf": rg_shuf},
            train_logs=train_logs,
            heldout_logs=heldout_logs,
            scoring_mode="committee_head_frozen_trunk",
        )
    )
    _ = path_d_support
    return results


def _fmt_strata_row(arm: str, seed: int, strata: dict, persistent, mode: str) -> str:
    cells = []
    for name in PANEL_STRATUM_COUNTS:
        s = strata.get(name, {})
        cells.append(
            f"{s.get('correct', '?')}/{s.get('need', '?')}"
            f"{'*' if s.get('qualifies') else ''}"
        )
    pers = "censored" if persistent is None else str(persistent)
    return (
        f"| {arm} | {seed} | " + " | ".join(cells) + f" | {pers} | {mode} |"
    )


def m3_check(p0_results: list[ArmResult]) -> tuple[bool, str]:
    flags = []
    ok_all = True
    for r in p0_results:
        s = r.strata
        s1 = s["S1"]["qualifies"]
        s2 = s["S2"]["qualifies"]
        s3 = s["S3"]["qualifies"]
        s4 = s["S4"]["qualifies"]
        s5 = s["S5"]["qualifies"]
        expect = s1 and s3 and (not s2) and (not s4) and (not s5)
        if not expect:
            ok_all = False
            flags.append(
                f"seed{r.seed}: S1={s1} S2={s2} S3={s3} S4={s4} S5={s5} "
                f"(want S1&S3=True, S2/S4/S5=False)"
            )
        else:
            flags.append(f"seed{r.seed}: M3 pattern matched")
    return ok_all, "; ".join(flags)


def _fmt_within(v) -> str:
    if v == "INSUFFICIENT" or isinstance(v, str):
        return str(v)
    if v is None or (isinstance(v, float) and v != v):
        return "nan"
    return f"{float(v):.3f}"


def serialize_arm(r: ArmResult) -> dict:
    return {
        "arm": r.arm,
        "seed": r.seed,
        "k_hash": r.k_hash,
        "path_wall_s": r.path_wall_s,
        "dest_wall_s": r.dest_wall_s,
        "first_persistent_step": r.first_persistent_step,
        "strata": r.strata,
        "probes": r.probes,
        "probe_deltas": r.probe_deltas,
        "road_gaps": r.road_gaps,
        "train_logs": r.train_logs,
        "heldout_logs": r.heldout_logs,
        "wrap_anti_correct": r.wrap_anti_correct,
        "wrap_n": r.wrap_n,
        "scoring_mode": r.scoring_mode,
    }


def write_report(
    all_results: list[ArmResult],
    overlap: dict,
    n_max: int,
    k: int,
    total_wall: float,
    *,
    run_tag: str,
    input_hashes: dict,
    script_hash: str,
    conditional_fix_fired: bool,
    mean_std_at_600: dict,
    collapse_persists: bool,
) -> str:
    p0s = [r for r in all_results if r.arm == "P0"]
    m3_ok, m3_txt = m3_check(p0s)

    lines = [
        "# B2_INSTRUMENT_REPAIR_09",
        "",
        f"run_tag = `{run_tag}`",
        "",
        "## 1. Input hashes",
        "",
    ]
    for name, h in input_hashes.items():
        lines.append(f"- `{name}`: `{h}`")
    lines += [
        f"- `b2_instrument_repair_09.py`: `{script_hash}`",
        "",
        "## 2. Frozen constants (unchanged)",
        "",
        "```text",
        f"N_MAX={N_MAX}",
        f"K={K}",
        f"H_DEST={H_DEST}",
        f"M_PATH={M_PATH}",
        f"PATH_BATCH={PATH_BATCH}",
        f"M_ROADS={M_ROADS}",
        f"VICREG_INV={VICREG_INV}",
        f"VICREG_VAR={VICREG_VAR}",
        f"VICREG_COV={VICREG_COV}",
        f"CONTRAST_TEMP={CONTRAST_TEMP}",
        f"PILOT_SEEDS={PILOT_SEEDS}",
        f"_D_PATH_LO={_D_PATH_LO}",
        f"_D_PATH_HI={_D_PATH_HI}",
        "```",
        "",
        "## 3. Held-out loss and components (interpretable)",
        "",
        "| seed | arm | step | loss_total | inv_term | var_term | cov_term | mean_std |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for r in all_results:
        for e in r.heldout_logs:
            lines.append(
                f"| {r.seed} | {r.arm} | {e['step']} | {e['loss_total']:.4f} | "
                f"{e['inv_term']:.4f} | {e['var_term']:.4f} | {e['cov_term']:.4f} | "
                f"{e['mean_std']:.4f} |"
            )

    lines += [
        "",
        "## 4. Training-loss curve (`not_interpretable`)",
        "",
        "| seed | arm | step | loss_total | inv_term | var_term | cov_term | mean_std | ell |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for r in all_results:
        for e in r.train_logs:
            lines.append(
                f"| {r.seed} | {r.arm} | {e['step']} | {e['loss_total']:.4f} | "
                f"{e['inv_term']:.4f} | {e['var_term']:.4f} | {e['cov_term']:.4f} | "
                f"{e['mean_std']:.4f} | {e['ell']} |"
            )

    lines += [
        "",
        "## 5. road_gap table",
        "",
        "| seed | tag | align_same | align_diff | road_gap |",
        "| ---: | --- | ---: | ---: | ---: |",
    ]
    for r in all_results:
        for tag, rg in r.road_gaps.items():
            lines.append(
                f"| {r.seed} | {tag} | {rg['align_same']:.4f} | "
                f"{rg['align_diff']:.4f} | {rg['road_gap']:.4f} |"
            )

    lines += [
        "",
        "## 6. Mechanism probes with delta vs matched init",
        "",
        "| arm | seed | tag | exact_d | Δexact_d | length_only | Δlength | "
        "d_within_len | sign(d) | Δsign | residue | Δresidue |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for r in all_results:
        init = r.probes.get("init")
        for tag, pr in r.probes.items():
            if tag == "init":
                lines.append(
                    f"| {r.arm} | {r.seed} | init | {pr['exact_d_acc']:.3f} | — | "
                    f"{pr['length_only_acc']:.3f} | — | "
                    f"{_fmt_within(pr['exact_d_within_length_acc'])} | "
                    f"{pr['sign_d_acc']:.3f} | — | "
                    f"{pr['residue_acc_disjoint_d']:.3f} | — |"
                )
            else:
                d = r.probe_deltas if tag in (r.arm, "D", "P0", "P+", "P_shuf", "P0-neg") else {}
                # Prefer arm-level deltas (trained final vs init)
                if tag == r.arm or (r.arm == "P+" and tag == "P+") or (
                    r.arm == "D" and tag == "D"
                ):
                    d = r.probe_deltas
                else:
                    d = probe_deltas(pr, init) if init else {}
                dw = pr["exact_d_within_length_acc"]
                if dw == "INSUFFICIENT":
                    dw_s = f"INSUFFICIENT(n={pr.get('exact_d_within_length_n')})"
                else:
                    dw_s = _fmt_within(dw)
                lines.append(
                    f"| {r.arm} | {r.seed} | {tag} | {pr['exact_d_acc']:.3f} | "
                    f"{d.get('delta_exact_d_acc', float('nan')):+.3f} | "
                    f"{pr['length_only_acc']:.3f} | "
                    f"{d.get('delta_length_only_acc', float('nan')):+.3f} | "
                    f"{dw_s} | {pr['sign_d_acc']:.3f} | "
                    f"{d.get('delta_sign_d_acc', float('nan')):+.3f} | "
                    f"{pr['residue_acc_disjoint_d']:.3f} | "
                    f"{d.get('delta_residue_acc_disjoint_d', float('nan')):+.3f} |"
                )

    lines += [
        "",
        "Footnote chance columns (not the comparison): exact_d_chance≈1/n_classes, "
        "length_chance≈1/n_lengths, sign_d_chance=0.5, residue_chance=1/66.",
        "",
        "## 7. d_within_len",
        "",
    ]
    for r in all_results:
        for tag, pr in r.probes.items():
            v = pr["exact_d_within_length_acc"]
            n = pr.get("exact_d_within_length_n")
            if v == "INSUFFICIENT":
                lines.append(
                    f"- {r.arm} seed{r.seed} [{tag}]: INSUFFICIENT "
                    f"(achieved stratum size n={n}, corpus={pr.get('probe_corpus_n')})"
                )
            else:
                lines.append(
                    f"- {r.arm} seed{r.seed} [{tag}]: {float(v):.3f} (stratum n={n})"
                )

    rows = [
        _fmt_strata_row(r.arm, r.seed, r.strata, r.first_persistent_step, r.scoring_mode)
        for r in all_results
    ]
    lines += [
        "",
        "## 8. Per-arm per-stratum floor table and M3",
        "",
        "| arm | seed | S1 | S2 | S3 | S4 | S5 | first_persistent_step | scoring |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        *rows,
        "",
        f"**M3_PASS = {m3_ok}**",
        "",
        m3_txt,
        "",
        "## 9. Section-3 conditional fix",
        "",
        f"- conditional_fix_fired = **{conditional_fix_fired}**",
        f"- USE_BN_PROJECTOR (this run) = **{USE_BN_PROJECTOR}**",
        f"- mean_std at held-out step 600 (P0): {mean_std_at_600}",
        f"- collapse_persists_after_fix = **{collapse_persists}**",
        "",
        "## 10. Wall time per arm",
        "",
        "| arm | seed | path_wall_s | dest_wall_s |",
        "| --- | ---: | ---: | ---: |",
    ]
    for r in all_results:
        lines.append(
            f"| {r.arm} | {r.seed} | {r.path_wall_s:.1f} | {r.dest_wall_s:.1f} |"
        )
    lines += [
        "",
        f"- total_wall_s = {total_wall:.1f}",
        f"- overlap = {overlap}",
        "",
    ]
    report = "\n".join(lines)
    OUT_MD.write_text(report, encoding="utf-8")
    return report


def _mean_std_p0_at_600(results: list[ArmResult]) -> dict:
    out = {}
    for r in results:
        if r.arm != "P0":
            continue
        hit = [e for e in r.heldout_logs if e["step"] == M_PATH]
        if not hit:
            out[r.seed] = None
        else:
            out[r.seed] = hit[-1]["mean_std"]
    return out


def run_once(
    *,
    run_tag: str,
    public_key,
    partition,
    panel,
    schedule,
    path_d_support,
    overlap,
    n_max,
    k,
    input_hashes,
    script_hash,
) -> tuple[list[ArmResult], dict, float]:
    all_results: list[ArmResult] = []
    t0 = time.perf_counter()
    for seed in PILOT_SEEDS:
        held_stream = CounterStream(
            dummy_key(f"successor-dev-b2-pilot-seed-{seed}", purpose="public-root"),
            ("L1", "b2-pilot", "heldout", seed, run_tag),
        )
        heldout = build_heldout_batch(held_stream)
        print(
            f"heldout seed={seed}: same={heldout['n_same_pairs']} "
            f"diff={heldout['n_diff_pairs']} exclude={heldout['n_exclude_words']}",
            flush=True,
        )
        all_results.extend(
            run_seed(
                seed, public_key, partition, panel, schedule, path_d_support, heldout
            )
        )
    wall = time.perf_counter() - t0
    mean_std = _mean_std_p0_at_600(all_results)
    return all_results, mean_std, wall


def main() -> None:
    global USE_BN_PROJECTOR
    log_f = open(OUT_LOG, "w", encoding="utf-8")

    class Tee:
        def __init__(self, *files):
            self.files = files

        def write(self, data):
            for f in self.files:
                f.write(data)
                f.flush()

        def flush(self):
            for f in self.files:
                f.flush()

        def buffer(self):
            return self

        def encode_write(self, data):
            self.write(data.decode("utf-8", errors="replace") if isinstance(data, bytes) else data)

    import sys as _sys

    _sys.stdout = Tee(log_f, _sys.__stdout__)
    _sys.stderr = Tee(log_f, _sys.__stderr__)

    input_hashes = {
        "B2_INSTRUMENT_REPAIR_09_TICKET.md": hashlib.sha256(
            (_DEV / "B2_INSTRUMENT_REPAIR_09_TICKET.md").read_bytes()
        ).hexdigest(),
        "B2_PATH_VS_DESTINATION_DESIGN_V2.md": hashlib.sha256(
            (_DEV / "B2_PATH_VS_DESTINATION_DESIGN_V2.md").read_bytes()
        ).hexdigest(),
        "B2_PILOT_08.md": hashlib.sha256((_DEV / "B2_PILOT_08.md").read_bytes()).hexdigest(),
        "b2_path_pilot_08.py": hashlib.sha256(
            (_DEV / "b2_path_pilot_08.py").read_bytes()
        ).hexdigest(),
        "b2_pilot_08_results.json": hashlib.sha256(
            (_DEV / "b2_pilot_08_results.json").read_bytes()
        ).hexdigest(),
    }
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print("input_hashes:", input_hashes, flush=True)
    print("script_hash:", script_hash, flush=True)

    if not torch.cuda.is_available():
        msg = (
            "STOP: CUDA unavailable on this host. Pilot 08 ran on cuda "
            "(wall ~2432 s). Refusing CPU fallback to protect the ticket budget. "
            f"DEVICE would have been {DEVICE}."
        )
        print(msg, flush=True)
        stop_payload = {
            "status": "STOP_NO_CUDA",
            "device": str(DEVICE),
            "cuda_available": False,
            "input_hashes": input_hashes,
            "script_hash": script_hash,
            "frozen_constants": {
                "N_MAX": N_MAX,
                "K": K,
                "H_DEST": H_DEST,
                "M_PATH": M_PATH,
                "PATH_BATCH": PATH_BATCH,
                "M_ROADS": M_ROADS,
                "VICREG_INV": VICREG_INV,
                "VICREG_VAR": VICREG_VAR,
                "VICREG_COV": VICREG_COV,
                "CONTRAST_TEMP": CONTRAST_TEMP,
                "PILOT_SEEDS": list(PILOT_SEEDS),
                "_D_PATH_LO": _D_PATH_LO,
                "_D_PATH_HI": _D_PATH_HI,
            },
            "note": (
                "Instrument R1-R5 implemented in b2_instrument_repair_09.py; "
                "full seed 0/1 pilot not executed on this host."
            ),
            "partial_progress": {
                "halted_at": "before_training_cuda_gate",
                "prior_attempt": (
                    "CPU attempt halted during seed0 arm D dest training after "
                    "ckpt 350 (~29 min wall); process killed per budget rule."
                ),
            },
            "sections_3_to_10": "NOT_PRODUCED",
        }
        OUT_JSON.write_text(json.dumps(stop_payload, indent=2), encoding="utf-8")
        hash_lines = "\n".join(f"- `{n}`: `{h}`" for n, h in input_hashes.items())
        OUT_MD.write_text(
            "\n".join(
                [
                    "# B2_INSTRUMENT_REPAIR_09",
                    "",
                    "status = `STOP_NO_CUDA`",
                    "",
                    "## 1. Input hashes",
                    "",
                    hash_lines,
                    f"- `b2_instrument_repair_09.py`: `{script_hash}`",
                    "",
                    "## 2. Frozen constants (unchanged)",
                    "",
                    "```text",
                    f"N_MAX={N_MAX}",
                    f"K={K}",
                    f"H_DEST={H_DEST}",
                    f"M_PATH={M_PATH}",
                    f"PATH_BATCH={PATH_BATCH}",
                    f"M_ROADS={M_ROADS}",
                    f"VICREG_INV={VICREG_INV}",
                    f"VICREG_VAR={VICREG_VAR}",
                    f"VICREG_COV={VICREG_COV}",
                    f"CONTRAST_TEMP={CONTRAST_TEMP}",
                    f"PILOT_SEEDS={PILOT_SEEDS}",
                    f"_D_PATH_LO={_D_PATH_LO}",
                    f"_D_PATH_HI={_D_PATH_HI}",
                    "```",
                    "",
                    "## 3. Held-out loss and components (interpretable)",
                    "",
                    "NOT_PRODUCED — no CUDA; run not executed.",
                    "",
                    "## 4. Training-loss curve (`not_interpretable`)",
                    "",
                    "NOT_PRODUCED — no CUDA; run not executed.",
                    "",
                    "## 5. road_gap table",
                    "",
                    "NOT_PRODUCED — no CUDA; run not executed.",
                    "",
                    "## 6. Mechanism probes with delta vs matched init",
                    "",
                    "NOT_PRODUCED — no CUDA; run not executed.",
                    "",
                    "Footnote chance columns (not the comparison): exact_d_chance≈1/n_classes, "
                    "length_chance≈1/n_lengths, sign_d_chance=0.5, residue_chance=1/66.",
                    "",
                    "## 7. d_within_len",
                    "",
                    "NOT_PRODUCED — no CUDA; run not executed.",
                    "",
                    "## 8. Per-arm per-stratum floor table and M3",
                    "",
                    "NOT_PRODUCED — no CUDA; run not executed.",
                    "",
                    "## 9. Section-3 conditional fix",
                    "",
                    "- conditional_fix_fired = **not evaluated**",
                    "- mean_std at held-out step 600 (P0): NOT_PRODUCED",
                    "",
                    "## 10. Wall time per arm",
                    "",
                    "NOT_PRODUCED — no CUDA; run not executed.",
                    "",
                    "Prior CPU attempt: ~29 min wall, halted seed0 arm D after dest ckpt 350.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        print(f"wrote {OUT_MD}, {OUT_JSON}, {OUT_LOG}", flush=True)
        raise SystemExit(2)

    runner.patch_contact_transformer_device_guard()

    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    partition = partition_cells(public_key)
    verify_partition(partition)
    panel = DummyPanelBuilder(
        public_key, dummy_key(DEV_PANEL_LABEL, purpose="panel")
    ).build(MODULUS, world_slot=WORLD_SLOT)
    if len(panel.items) != PANEL_SIZE:
        raise RuntimeError("panel size drifted")

    n_max, k, schedule = compute_n_max_and_k(public_key, partition)
    path_d_support = set(range(_D_PATH_LO, _D_PATH_HI + 1))
    overlap = displacement_class_overlap(path_d_support, panel)
    print("displacement-class overlap:", overlap, flush=True)

    USE_BN_PROJECTOR = False
    pre_results, mean_std_pre, wall_pre = run_once(
        run_tag="pre_fix",
        public_key=public_key,
        partition=partition,
        panel=panel,
        schedule=schedule,
        path_d_support=path_d_support,
        overlap=overlap,
        n_max=n_max,
        k=k,
        input_hashes=input_hashes,
        script_hash=script_hash,
    )

    vals = [v for v in mean_std_pre.values() if v is not None]
    fire = bool(vals) and any(v < 0.5 for v in vals)
    print(f"mean_std_at_600 pre_fix={mean_std_pre} fire_conditional={fire}", flush=True)

    all_payload = {
        "pre_fix": {
            "results": [serialize_arm(r) for r in pre_results],
            "mean_std_at_600": mean_std_pre,
            "total_wall_s": wall_pre,
            "USE_BN_PROJECTOR": False,
        }
    }
    collapse_persists = False
    post_results = None
    mean_std_post = {}
    wall_post = 0.0

    if fire:
        print("Section-3 conditional fix FIRED: enabling BN projector; rerun once.", flush=True)
        USE_BN_PROJECTOR = True
        post_results, mean_std_post, wall_post = run_once(
            run_tag="post_fix",
            public_key=public_key,
            partition=partition,
            panel=panel,
            schedule=schedule,
            path_d_support=path_d_support,
            overlap=overlap,
            n_max=n_max,
            k=k,
            input_hashes=input_hashes,
            script_hash=script_hash,
        )
        vals2 = [v for v in mean_std_post.values() if v is not None]
        collapse_persists = bool(vals2) and any(v < 0.5 for v in vals2)
        all_payload["post_fix"] = {
            "results": [serialize_arm(r) for r in post_results],
            "mean_std_at_600": mean_std_post,
            "total_wall_s": wall_post,
            "USE_BN_PROJECTOR": True,
            "collapse_persists": collapse_persists,
        }
        report_results = post_results
        report_mean = mean_std_post
        report_wall = wall_pre + wall_post
        report_tag = "post_fix"
    else:
        print("Section-3 conditional fix NOT fired (mean_std >= 0.5).", flush=True)
        report_results = pre_results
        report_mean = mean_std_pre
        report_wall = wall_pre
        report_tag = "pre_fix"

    # Recompute script hash after run (file unchanged during run)
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    write_report(
        report_results,
        overlap,
        n_max,
        k,
        report_wall,
        run_tag=report_tag,
        input_hashes=input_hashes,
        script_hash=script_hash,
        conditional_fix_fired=fire,
        mean_std_at_600=report_mean,
        collapse_persists=collapse_persists,
    )

    # Also emit a combined markdown if both runs exist: append pre_fix tables into JSON only;
    # MD uses the governing run (post if fired else pre). Dual-run detail lives in JSON.
    OUT_JSON.write_text(
        json.dumps(
            {
                "N_max": n_max,
                "K": k,
                "H_DEST": H_DEST,
                "M_PATH": M_PATH,
                "frozen_constants": {
                    "N_MAX": N_MAX,
                    "K": K,
                    "H_DEST": H_DEST,
                    "M_PATH": M_PATH,
                    "PATH_BATCH": PATH_BATCH,
                    "M_ROADS": M_ROADS,
                    "VICREG_INV": VICREG_INV,
                    "VICREG_VAR": VICREG_VAR,
                    "VICREG_COV": VICREG_COV,
                    "CONTRAST_TEMP": CONTRAST_TEMP,
                    "PILOT_SEEDS": list(PILOT_SEEDS),
                    "_D_PATH_LO": _D_PATH_LO,
                    "_D_PATH_HI": _D_PATH_HI,
                },
                "input_hashes": input_hashes,
                "script_hash": script_hash,
                "overlap": overlap,
                "conditional_fix_fired": fire,
                "collapse_persists_after_fix": collapse_persists,
                "runs": all_payload,
                "device": str(DEVICE),
            },
            indent=2,
            default=str,
        ),
        encoding="utf-8",
    )

    # Dual-run detail lives in JSON only; MD stays at the ten required sections.

    if collapse_persists:
        print(
            "STOP: mean_std < 0.5 persists after the single BN-projector fix. "
            "No further attempts authorized.",
            flush=True,
        )
    print(f"wrote {OUT_MD}, {OUT_JSON}, {OUT_LOG}", flush=True)


if __name__ == "__main__":
    main()
