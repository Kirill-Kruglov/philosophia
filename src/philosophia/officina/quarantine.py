from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from .canonical import sha256_file


class QuarantineViolation(PermissionError):
    pass


class Surface(str, Enum):
    TEST = "TEST"
    T = "T"
    Q = "Q"
    C = "C"


@dataclass(frozen=True)
class FixtureGrant:
    path: Path
    sha256: str


@dataclass(frozen=True)
class ArtifactLabel:
    sources: tuple[str, ...]
    promotable: bool
    certified: bool

    @classmethod
    def native(cls) -> "ArtifactLabel":
        return cls(sources=("officina-storage",), promotable=False, certified=False)

    @classmethod
    def engineering_fixture(cls) -> "ArtifactLabel":
        return cls(sources=("engineering-fixture",), promotable=False, certified=True)

    @classmethod
    def test_only_native(cls) -> "ArtifactLabel":
        return cls(sources=("test-only-native",), promotable=False, certified=True)

    @classmethod
    def derived(cls, *parents: "ArtifactLabel") -> "ArtifactLabel":
        if not parents:
            raise ValueError("derived provenance requires at least one parent")
        sources = tuple(sorted({source for parent in parents for source in parent.sources}))
        return cls(
            sources=sources,
            promotable=all(parent.promotable for parent in parents),
            certified=all(parent.certified for parent in parents),
        )

    def require_promotable(self, surface: Surface) -> None:
        if surface in {Surface.Q, Surface.C} and (
            not self.certified or not self.promotable
        ):
            raise QuarantineViolation(
                f"{','.join(self.sources)} artifacts cannot enter {surface.value}"
            )


class PathPolicy:
    def __init__(
        self,
        *,
        repository_root: Path,
        successor_root: Path,
        fixture_grants: tuple[FixtureGrant, ...] = (),
    ) -> None:
        self.repository_root = repository_root.resolve(strict=True)
        self.successor_root = successor_root.resolve(strict=True)
        if not self.successor_root.is_relative_to(self.repository_root):
            raise ValueError("successor root must be inside repository")
        grants: dict[Path, FixtureGrant] = {}
        for grant in fixture_grants:
            resolved = grant.path.resolve(strict=True)
            if resolved in grants:
                raise ValueError("duplicate fixture grant")
            grants[resolved] = FixtureGrant(resolved, grant.sha256)
        self._fixture_grants = grants

    def authorize(
        self,
        path: Path,
        *,
        surface: Surface,
        write: bool = False,
    ) -> tuple[Path, ArtifactLabel]:
        candidate = path if path.is_absolute() else self.repository_root / path
        resolved = candidate.resolve(strict=False)
        if resolved.is_relative_to(self.successor_root):
            return resolved, ArtifactLabel.native()

        grant = self._fixture_grants.get(resolved)
        if grant is None:
            raise QuarantineViolation(f"path denied by default: {resolved}")
        if write:
            raise QuarantineViolation("engineering fixtures are read-only")
        if surface is not Surface.T:
            raise QuarantineViolation("engineering fixtures are T-only")
        if not resolved.is_file() or sha256_file(resolved) != grant.sha256:
            raise QuarantineViolation("engineering fixture hash mismatch")
        return resolved, ArtifactLabel.engineering_fixture()

    def read_bytes(self, path: Path, *, surface: Surface) -> tuple[bytes, ArtifactLabel]:
        resolved, label = self.authorize(path, surface=surface)
        if not label.certified:
            raise QuarantineViolation(
                "native reads require canonical ArtifactStore provenance"
            )
        return resolved.read_bytes(), label
