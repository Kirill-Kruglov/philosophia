from __future__ import annotations

import math

import torch


def real_fourier_basis(
    modulus: int = 113,
    *,
    dtype: torch.dtype = torch.float64,
    device: torch.device | str = "cpu",
) -> torch.Tensor:
    if modulus < 3 or modulus % 2 == 0:
        raise ValueError("the real basis requires an odd modulus")
    positions = torch.arange(modulus, dtype=dtype, device=device)
    columns = [torch.ones_like(positions) / math.sqrt(modulus)]
    scale = math.sqrt(2.0 / modulus)
    for frequency in range(1, (modulus + 1) // 2):
        phase = 2.0 * math.pi * frequency * positions / modulus
        columns.append(scale * torch.cos(phase))
        columns.append(scale * torch.sin(phase))
    return torch.stack(columns, dim=1)


def project_residue_axis(
    values: torch.Tensor,
    *,
    modulus: int = 113,
) -> torch.Tensor:
    if values.ndim < 1 or values.shape[0] != modulus:
        raise ValueError(f"first axis must contain {modulus} residues")
    basis = real_fourier_basis(modulus, dtype=values.dtype, device=values.device)
    return torch.einsum("pf,p...->f...", basis, values)


def frequency_energy(coefficients: torch.Tensor) -> torch.Tensor:
    if coefficients.ndim < 1:
        raise ValueError("coefficients require a frequency axis")
    flattened = coefficients.reshape(coefficients.shape[0], -1)
    return flattened.square().sum(dim=1)
