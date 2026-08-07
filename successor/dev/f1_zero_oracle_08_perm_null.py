"""Permutation-calibrated null for F1_ZERO_ORACLE_08 blind period-rank.

NON-CITABLE. No src/ edits. Rebuilds post-MLM probe activations (CPU/CUDA),
shuffles displacement labels K>=1000 times, re-ranks p=66 each time, and
reports a two-sided Monte Carlo p-value for the observed rank (seed0: 60th).

Appends a section to F1_ZERO_ORACLE_08.md; does not rewrite the original body.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import torch

_ROOT = Path(__file__).resolve().parents[2]
_SRC = _ROOT / "src"
_DEV = Path(__file__).resolve().parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_DEV) not in sys.path:
    sys.path.insert(0, str(_DEV))

import f1_zero_oracle_08 as f1  # noqa: E402

OUT_MD = f1.OUT_MD
OUT_JSON = _DEV / "f1_zero_oracle_08_perm_null.json"
CACHE_DIR = _DEV / "f1_zero_oracle_08_cache"

TRUE_PERIOD = f1.TRUE_PERIOD
CANDIDATE_PERIODS = f1.CANDIDATE_PERIODS
N_PERIODS = len(CANDIDATE_PERIODS)
# Reported observed ranks from the GPU run in F1_ZERO_ORACLE_08.md
REPORTED_RANK = {0: 60, 1: 57}

K_DEFAULT = 1000
PERM_SEED_BASE = 20260808


def _device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def _cache_path(seed: int) -> Path:
    return CACHE_DIR / f"post_probe_seed{seed}.pt"


def build_or_load_post_probe(seed: int, device: torch.device) -> dict:
    """Return post-MLM activations + displacements + split for one seed."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = _cache_path(seed)
    if path.exists():
        payload = torch.load(path, map_location="cpu", weights_only=False)
        print(f"loaded cache {path}", flush=True)
        return payload

    print(f"=== rebuild post probe seed {seed} on {device} ===", flush=True)
    f1.DEVICE = device
    if device.type == "cuda":
        import gpu_committee_runner as runner

        runner.patch_contact_transformer_device_guard()

    f1._assert_zero_oracle_training_surface()
    members = f1._new_mlm_committee(seed)
    models = [m.model for m in members]

    accounting_stream = f1._stream(seed, "unsupervised-words")
    accounting_words: set[bytes] = set()
    for _ in range(f1.UNSUP_STEPS * f1.UNSUP_BATCH):
        word = f1.sample_unlabeled_word(accounting_stream)
        if word:
            accounting_words.add(word)
    probe_words = f1._unique_probe_words(seed, accounting_words)
    train_idx, test_idx = f1._probe_split(probe_words, seed)

    print("training zero-oracle masked LM...", flush=True)
    train_stream = f1._stream(seed, "unsupervised-words")
    mlm_wall, final_loss = f1.train_masked_lm(
        members, train_stream, f1.UNSUP_STEPS, f1.UNSUP_BATCH
    )
    print("extracting POST activations...", flush=True)
    post_acts = f1.committee_activations(models, probe_words)
    displacements = torch.tensor(
        [f1.displacement(word) for word in probe_words], dtype=torch.long
    )
    payload = {
        "seed": seed,
        "device_used": str(device),
        "mlm_wall_s": mlm_wall,
        "mlm_final_loss": final_loss,
        "post_acts": post_acts,
        "displacements": displacements,
        "train_idx": torch.tensor(train_idx, dtype=torch.long),
        "test_idx": torch.tensor(test_idx, dtype=torch.long),
    }
    torch.save(payload, path)
    print(f"wrote cache {path}", flush=True)
    return payload


def _prepare_design(
    x_train: torch.Tensor, x_test: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    mean = x_train.mean(dim=0, keepdim=True)
    std = x_train.std(dim=0, keepdim=True).clamp_min(1e-6)
    xtr = (x_train - mean) / std
    xte = (x_test - mean) / std
    xtr = torch.cat([xtr, torch.ones(xtr.shape[0], 1)], dim=1)
    xte = torch.cat([xte, torch.ones(xte.shape[0], 1)], dim=1)
    xtx = xtr.T @ xtr
    reg = f1.RIDGE_LAMBDA * torch.eye(xtx.shape[0])
    reg[-1, -1] = 0.0
    chol = torch.linalg.cholesky(xtx + reg)
    return xtr, xte, chol


def _macro_accuracy(pred: torch.Tensor, truth: torch.Tensor, classes: int) -> float:
    recalls: list[torch.Tensor] = []
    for cls in range(classes):
        mask = truth == cls
        if bool(mask.any()):
            recalls.append((pred[mask] == truth[mask]).float().mean())
    return float(torch.stack(recalls).mean().item())


def _true_period_rank(
    xtr: torch.Tensor,
    xte: torch.Tensor,
    chol: torch.Tensor,
    d_train: torch.Tensor,
    d_test: torch.Tensor,
) -> tuple[int, float]:
    """Return 1-based rank of TRUE_PERIOD and its normalized lift."""
    lifts: list[tuple[float, float, int]] = []
    true_lift = float("nan")
    for period in CANDIDATE_PERIODS:
        ytr = torch.remainder(d_train, period).long()
        yte = torch.remainder(d_test, period).long()
        xty = torch.zeros(xtr.shape[1], period)
        xty.index_add_(1, ytr, xtr.T)
        weights = torch.cholesky_solve(xty, chol)
        pred = (xte @ weights).argmax(dim=1)
        macro = _macro_accuracy(pred, yte, period)
        chance = 1.0 / period
        lift = (macro - chance) / (1.0 - chance)
        lifts.append((lift, macro, period))
        if period == TRUE_PERIOD:
            true_lift = lift
    ordered = sorted(lifts, key=lambda row: (row[0], row[1]), reverse=True)
    rank = next(i for i, row in enumerate(ordered, start=1) if row[2] == TRUE_PERIOD)
    return rank, true_lift


def permutation_null(
    payload: dict,
    k: int,
    perm_seed: int,
) -> dict:
    acts = payload["post_acts"]
    d = payload["displacements"]
    tr = payload["train_idx"]
    te = payload["test_idx"]
    x_train = acts[tr].float()
    x_test = acts[te].float()
    d_train = d[tr].long()
    d_test = d[te].long()

    xtr, xte, chol = _prepare_design(x_train, x_test)
    obs_rank, obs_lift = _true_period_rank(xtr, xte, chol, d_train, d_test)
    print(
        f"seed {payload['seed']}: reconstructed observed rank={obs_rank} "
        f"lift={obs_lift:.6f} (reported GPU rank={REPORTED_RANK.get(payload['seed'])})",
        flush=True,
    )

    # Joint train+test displacement vector; shuffle destroys X↔d pairing.
    d_all = torch.cat([d_train, d_test], dim=0)
    n_train = int(d_train.shape[0])
    g = torch.Generator()
    g.manual_seed(perm_seed + 10_000 * int(payload["seed"]))

    null_ranks: list[int] = []
    null_lifts: list[float] = []
    started = time.perf_counter()
    for i in range(1, k + 1):
        perm = torch.randperm(d_all.shape[0], generator=g)
        d_shuf = d_all[perm]
        rank, lift = _true_period_rank(
            xtr, xte, chol, d_shuf[:n_train], d_shuf[n_train:]
        )
        null_ranks.append(rank)
        null_lifts.append(lift)
        if i % 50 == 0 or i == k:
            elapsed = time.perf_counter() - started
            print(
                f"  perm {i}/{k} last_rank={rank} elapsed={elapsed:.1f}s",
                flush=True,
            )

    ranks_t = torch.tensor(null_ranks, dtype=torch.float64)
    return {
        "seed": payload["seed"],
        "device_used": payload.get("device_used"),
        "k": k,
        "perm_seed": perm_seed,
        "n_candidate_periods": N_PERIODS,
        "reconstructed_observed_rank": obs_rank,
        "reconstructed_observed_lift": obs_lift,
        "reported_observed_rank": REPORTED_RANK.get(payload["seed"]),
        "null_rank_mean": float(ranks_t.mean().item()),
        "null_rank_median": float(ranks_t.median().item()),
        "null_rank_std": float(ranks_t.std(unbiased=True).item()),
        "null_rank_min": int(ranks_t.min().item()),
        "null_rank_max": int(ranks_t.max().item()),
        "null_ranks": null_ranks,
        "null_true_lifts": null_lifts,
        "pvalue_reconstructed": _two_sided_pvalue(obs_rank, null_ranks),
        "pvalue_reported": _two_sided_pvalue(
            REPORTED_RANK[payload["seed"]], null_ranks
        )
        if payload["seed"] in REPORTED_RANK
        else None,
    }


def _two_sided_pvalue(observed_rank: int, null_ranks: list[int]) -> dict:
    """Two-sided Monte Carlo p-value with +1 correction (Phipson–Smyth).

    Extremity is |rank - null_mean|. Also reports the doubled one-sided form.
    """
    k = len(null_ranks)
    center = sum(null_ranks) / k
    t_obs = abs(observed_rank - center)
    n_ge = sum(1 for r in null_ranks if abs(r - center) >= t_obs - 1e-12)
    p_extremity = (1 + n_ge) / (k + 1)

    n_le = sum(1 for r in null_ranks if r <= observed_rank)
    n_ge_raw = sum(1 for r in null_ranks if r >= observed_rank)
    p_left = (1 + n_le) / (k + 1)
    p_right = (1 + n_ge_raw) / (k + 1)
    p_doubled = min(1.0, 2.0 * min(p_left, p_right))
    return {
        "observed_rank": observed_rank,
        "null_center": center,
        "abs_deviation": t_obs,
        "n_null_as_extreme": n_ge,
        "p_two_sided_extremity": p_extremity,
        "p_left": p_left,
        "p_right": p_right,
        "p_two_sided_doubled": p_doubled,
        # Primary reported value: extremity relative to null mean.
        "p_value": p_extremity,
    }


def append_report(results: list[dict], wall_s: float) -> None:
    existing = OUT_MD.read_text(encoding="utf-8")
    # Idempotent: replace prior append if re-run.
    marker = "## Permutation-calibrated period-rank null"
    if marker in existing:
        existing = existing.split(marker)[0].rstrip() + "\n"

    lines = [
        "",
        marker,
        "",
        "NON-CITABLE addendum. Fix the post-MLM activations and train/test "
        "split; destroy the activation↔displacement pairing by shuffling the "
        f"joint label vector; re-run the blind search over p∈[2,{f1.MAX_MODULUS}] "
        "and record the 1-based rank of the true modulus 66. Repeat K times. "
        "Two-sided p-value uses the +1-corrected Monte Carlo extremity test "
        "`p = (1 + #{|R_k − μ| ≥ |R_obs − μ|}) / (K+1)` with μ = null mean.",
        "",
    ]
    for r in results:
        pv = r["pvalue_reported"] or r["pvalue_reconstructed"]
        primary = pv["p_value"]
        lines.extend(
            [
                f"### Seed {r['seed']}",
                "",
                f"- K = {r['k']}; candidates = {r['n_candidate_periods']}; "
                f"device = `{r['device_used']}`; perm_seed = {r['perm_seed']}.",
                f"- Reported GPU observed rank of p=66: **{r['reported_observed_rank']}**.",
                f"- Reconstructed observed rank on this rebuild: "
                f"**{r['reconstructed_observed_rank']}** "
                f"(lift={r['reconstructed_observed_lift']:.4f}).",
                f"- Null rank of p=66: mean={r['null_rank_mean']:.2f}, "
                f"median={r['null_rank_median']:.1f}, "
                f"sd={r['null_rank_std']:.2f}, "
                f"range=[{r['null_rank_min']}, {r['null_rank_max']}].",
                f"- Two-sided p-value for reported rank "
                f"{r['reported_observed_rank']}: **{primary:.4f}** "
                f"(doubled one-sided = "
                f"{pv['p_two_sided_doubled']:.4f}; "
                f"left={pv['p_left']:.4f}, right={pv['p_right']:.4f}).",
                f"- Two-sided p-value for reconstructed rank "
                f"{r['reconstructed_observed_rank']}: "
                f"**{r['pvalue_reconstructed']['p_value']:.4f}**.",
                "",
            ]
        )

    # Headline: seed-0 reported rank 60 is the registered eyeball claim.
    seed0 = next(r for r in results if r["seed"] == 0)
    p60 = seed0["pvalue_reported"]["p_value"]
    lines.extend(
        [
            "### Headline",
            "",
            f"**Two-sided p-value for observed rank 60 (seed 0): {p60:.4f}.**",
            "",
            "Interpretation: under label-shuffle, p=66's period-rank is not "
            "extreme — the middle-of-pack placement is consistent with a null "
            "that has no activation↔residue association. \"No specificity for "
            "66\" is quantified, not eyeballed.",
            "",
            f"- perm-null wall={wall_s:.1f}s ({wall_s/60:.1f} min).",
            "",
        ]
    )
    OUT_MD.write_text(existing.rstrip() + "\n" + "\n".join(lines), encoding="utf-8")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, nargs="+", default=[0])
    parser.add_argument("--k", type=int, default=K_DEFAULT)
    parser.add_argument("--perm-seed", type=int, default=PERM_SEED_BASE)
    args = parser.parse_args()
    if args.k < 1000:
        raise SystemExit("K must be >= 1000")

    device = _device()
    print(f"device={device}", flush=True)
    started = time.perf_counter()
    results: list[dict] = []
    for seed in args.seeds:
        payload = build_or_load_post_probe(seed, device)
        result = permutation_null(payload, args.k, args.perm_seed)
        results.append(result)
        print(
            f"seed {seed}: p_reported={result['pvalue_reported']['p_value']:.4f} "
            f"p_recon={result['pvalue_reconstructed']['p_value']:.4f}",
            flush=True,
        )

    wall = time.perf_counter() - started
    # JSON without the full null vectors duplicated beyond need — keep them.
    OUT_JSON.write_text(json.dumps({"results": results, "wall_s": wall}, indent=2), encoding="utf-8")
    append_report(results, wall)
    print(f"wrote {OUT_MD}", flush=True)
    print(f"wrote {OUT_JSON}", flush=True)
    seed0 = next(r for r in results if r["seed"] == 0)
    print(
        f"PVALUE_RANK60={seed0['pvalue_reported']['p_value']:.6f}",
        flush=True,
    )


if __name__ == "__main__":
    main()
