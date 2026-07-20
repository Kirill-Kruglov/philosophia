from __future__ import annotations

import hashlib
from typing import Mapping

from .canonical import canonical_json


def salted_plaintext_commitment(*, salt: bytes, plaintext: bytes) -> str:
    if len(salt) != 32:
        raise ValueError("escrow salt must contain exactly 32 caller-provided bytes")
    return hashlib.sha256(salt + plaintext).hexdigest()


def envelope_metadata(
    *,
    ciphertext_sha256: str,
    salted_plaintext_sha256: str,
    contract_hashes: Mapping[str, str],
) -> bytes:
    hashes = {"ciphertext": ciphertext_sha256, "plaintext": salted_plaintext_sha256}
    hashes.update(contract_hashes)
    if any(len(value) != 64 for value in hashes.values()):
        raise ValueError("escrow metadata values must be SHA-256")
    return canonical_json(
        {
            "ciphertext_sha256": ciphertext_sha256,
            "contract_hashes": dict(contract_hashes),
            "salted_plaintext_sha256": salted_plaintext_sha256,
            "schema": "philosophia.officina.escrow-envelope.v1",
            "scientific_outcome": False,
        }
    )
