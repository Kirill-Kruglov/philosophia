#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import resource
import subprocess
import sys


REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from philosophia.level1.feasibility import report_payload, run_noncomparative_feasibility
from philosophia.level1.interlock import feasibility_capability
from philosophia.level1.model import configure_canonical_runtime
from philosophia.level1.public_root import atomic_create, canonical_json, sha256_file
from philosophia.level1.serialization import DeterministicKey


AUTHORIZATION_SCHEMA = "philosophia.level1.feasibility-authorization.v1"
REPORT_SCHEMA = "philosophia.level1.noncomparative-feasibility.v1"
AUTHORIZATION_TOKEN = "I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY"
AUTHORIZATION_RELATIVE = Path(
    "experiments/level_1_contact/FEASIBILITY_EXECUTION_AUTHORIZATION.json"
)
TRANSCRIPT_RELATIVE = Path(
    "experiments/level_1_contact/allocation/PUBLIC_ROOT_TRANSCRIPT.json"
)
CLAIM_SCHEMA = "philosophia.level1.feasibility-run-claim.v1"
CLAIM_NAME = "LEVEL1_NONCOMPARATIVE_FEASIBILITY_CLAIM.json"
REPORT_NAME = "LEVEL1_NONCOMPARATIVE_FEASIBILITY.json"
CANONICAL_OUTPUT_RELATIVE = Path("experiments/level_1_contact/feasibility")
REVIEWED_SOURCE_PATHS = (
    "scripts/level1_run_feasibility.py",
    "src/philosophia/level1/feasibility.py",
    "src/philosophia/level1/interlock.py",
    "src/philosophia/level1/train.py",
    "src/philosophia/level1/pool.py",
    "src/philosophia/level1/panel.py",
    "src/philosophia/level1/model.py",
    "src/philosophia/level1/acquisition.py",
    "src/philosophia/level1/config.py",
    "src/philosophia/level1/serialization.py",
    "src/philosophia/level1/scoring.py",
    "src/philosophia/level1/world.py",
)


def _git(repo: Path, *arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments],
        cwd=repo,
        check=check,
        capture_output=True,
        text=True,
    )


def _load_canonical(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    value = json.loads(raw)
    if not isinstance(value, dict) or canonical_json(value) != raw:
        raise ValueError(f"artifact is not canonical JSON: {path}")
    return value


def _preflight(repo: Path, expected_head: str, output_dir: Path) -> tuple[dict[str, object], dict[str, object]]:
    head = _git(repo, "rev-parse", "HEAD").stdout.strip()
    if head != expected_head:
        raise RuntimeError("HEAD does not match the reviewed execution command")
    if _git(repo, "diff", "--quiet", check=False).returncode != 0:
        raise RuntimeError("tracked working tree must be clean")
    if _git(repo, "diff", "--cached", "--quiet", check=False).returncode != 0:
        raise RuntimeError("git index must be empty")

    canonical_output = (repo / CANONICAL_OUTPUT_RELATIVE).resolve()
    if output_dir.resolve() != canonical_output:
        raise ValueError("feasibility output directory is frozen")
    authorization_path = repo / AUTHORIZATION_RELATIVE
    if not authorization_path.is_file():
        raise PermissionError("reviewed feasibility authorization is absent")
    for relative in (AUTHORIZATION_RELATIVE, TRANSCRIPT_RELATIVE):
        tracked = _git(
            repo,
            "ls-files",
            "--error-unmatch",
            relative.as_posix(),
            check=False,
        )
        if tracked.returncode != 0:
            raise PermissionError(f"required authorization artifact is untracked: {relative}")
    authorization = _load_canonical(authorization_path)
    if authorization.get("schema") != AUTHORIZATION_SCHEMA:
        raise ValueError("feasibility authorization schema mismatch")
    if authorization.get("token") != AUTHORIZATION_TOKEN:
        raise PermissionError("Kirill feasibility authorization token is absent")
    if authorization.get("scientific_outcome") is not False:
        raise ValueError("authorization must declare scientific_outcome false")
    if authorization.get("execution_once") is not True:
        raise ValueError("authorization must be one-shot")
    if authorization.get("arm") != "RANDOM-STATIC":
        raise ValueError("authorization arm must be RANDOM-STATIC")
    if authorization.get("caps") != {
        "development_worlds": 1,
        "trajectory_steps": 2000,
        "scorer_steps": 200,
        "wall_seconds": 43200,
    }:
        raise ValueError("authorization caps differ from the reviewed contract")
    if authorization.get("development_world") != {"pair_slot": 0, "modulus": 66}:
        raise ValueError("authorization development world changed")
    if authorization.get("output_directory") != CANONICAL_OUTPUT_RELATIVE.as_posix():
        raise ValueError("authorization output directory changed")
    reviewed_head = authorization.get("reviewed_code_head")
    if not isinstance(reviewed_head, str) or len(reviewed_head) != 40:
        raise ValueError("reviewed code HEAD is missing")
    source_diff = _git(
        repo,
        "diff",
        "--quiet",
        reviewed_head,
        head,
        "--",
        *REVIEWED_SOURCE_PATHS,
        check=False,
    )
    if source_diff.returncode != 0:
        raise RuntimeError("reviewed feasibility source bytes changed")

    transcript_path = repo / TRANSCRIPT_RELATIVE
    transcript = _load_canonical(transcript_path)
    if transcript.get("schema") != "philosophia.level1.public-root.v1":
        raise ValueError("public-root transcript schema mismatch")
    if transcript.get("scientific_outcome") is not False:
        raise ValueError("public-root transcript is not non-outcome")
    if transcript.get("forbidden_derivations") != [
        "real evaluator panel",
        "panel raw realizations",
        "panel ordering",
        "encryption salt",
        "escrow plaintext",
    ]:
        raise ValueError("public-root forbidden derivations changed")
    claim_path = output_dir / CLAIM_NAME
    report_path = output_dir / REPORT_NAME
    if claim_path.exists() or report_path.exists():
        raise FileExistsError("refusing to repeat feasibility execution")
    for forbidden in (
        repo / "experiments/level_1_contact/PREREG.lock",
        repo / "experiments/level_1_contact/escrow/REAL_PANEL.enc",
        repo / "experiments/level_1_contact/outcomes/decision.json",
    ):
        if forbidden.exists():
            raise RuntimeError(f"later-gate artifact already exists: {forbidden}")
    return authorization, transcript


def _development_world(transcript: dict[str, object]) -> tuple[int, int]:
    allocations = transcript.get("allocations")
    if not isinstance(allocations, dict):
        raise ValueError("public-root allocations are missing")
    pairs = allocations.get("development_pairs")
    if not isinstance(pairs, list) or len(pairs) != 6:
        raise ValueError("signed development-pair allocation changed")
    first = pairs[0]
    if not isinstance(first, dict):
        raise ValueError("development pair is malformed")
    slot, modulus = first.get("slot"), first.get("lower")
    if not isinstance(slot, int) or not isinstance(modulus, int):
        raise ValueError("development pair lacks integer slot/modulus")
    return slot, modulus


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-head", required=True)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments/level_1_contact/feasibility"),
    )
    args = parser.parse_args()
    output_dir = args.output_dir if args.output_dir.is_absolute() else REPO / args.output_dir
    authorization, transcript = _preflight(REPO, args.expected_head, output_dir)

    configure_canonical_runtime()
    root_hex = transcript.get("root_hex")
    if not isinstance(root_hex, str) or len(root_hex) != 64:
        raise ValueError("public root is malformed")
    key = DeterministicKey(bytes.fromhex(root_hex), purpose="public-root", test_only=False)
    pair_slot, modulus = _development_world(transcript)
    if authorization["development_world"] != {
        "pair_slot": pair_slot,
        "modulus": modulus,
    }:
        raise ValueError("authorized world differs from the public-root allocation")
    claim = {
        "schema": CLAIM_SCHEMA,
        "status": "started-no-delete-no-retry",
        "scientific_outcome": False,
        "git_head": args.expected_head,
        "authorization_sha256": sha256_file(REPO / AUTHORIZATION_RELATIVE),
        "public_root_transcript_sha256": sha256_file(REPO / TRANSCRIPT_RELATIVE),
        "arm": "RANDOM-STATIC",
        "development_world": {"pair_slot": pair_slot, "modulus": modulus},
    }
    atomic_create(output_dir / CLAIM_NAME, canonical_json(claim))
    capability = feasibility_capability()
    run = run_noncomparative_feasibility(
        key,
        pair_slot=pair_slot,
        modulus=modulus,
        capability=capability,
    )
    capability.check_wall()

    report = {
        "schema": REPORT_SCHEMA,
        "kind": "level1-noncomparative-feasibility",
        "scientific_outcome": False,
        "interpretation": "resource-and-binary-feasibility-only-no-arm-inference",
        "git_head": args.expected_head,
        "public_root_transcript_sha256": sha256_file(REPO / TRANSCRIPT_RELATIVE),
        "authorization_sha256": sha256_file(REPO / AUTHORIZATION_RELATIVE),
        "arm": "RANDOM-STATIC",
        "development_world": {"pair_slot": pair_slot, "modulus": modulus},
        "replicate": 1,
        "caps": {
            "development_worlds": 1,
            "trajectory_steps": 2000,
            "scorer_steps": 200,
            "wall_seconds": 43200,
        },
        "measurements": report_payload(run),
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "contamination_guards": {
            "second_arm": False,
            "arm_contrast": False,
            "real_panel": False,
            "escrow": False,
            "n3_selection": False,
            "preregistration_lock": False,
            "outcome_decision": False,
            "query_series_persisted": False,
            "loss_series_persisted": False,
            "solve_series_persisted": False,
        },
        "authorization": {
            "schema": authorization["schema"],
            "token": authorization["token"],
            "reviewed_code_head": authorization["reviewed_code_head"],
        },
    }
    atomic_create(output_dir / REPORT_NAME, canonical_json(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
