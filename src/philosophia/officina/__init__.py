"""Governance primitives for the Officina successor line.

WP-1/WP-2 expose no real-world, entropy, training, qualification, or outcome
entry point. All test randomness is caller supplied and explicitly test-only.
"""

from .canonical import canonical_json, sha256_bytes, sha256_file
from .interlock import ExecutionNotAuthorized

__all__ = [
    "ExecutionNotAuthorized",
    "canonical_json",
    "sha256_bytes",
    "sha256_file",
]
