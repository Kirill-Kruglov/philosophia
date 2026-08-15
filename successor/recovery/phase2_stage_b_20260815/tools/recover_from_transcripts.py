#!/usr/bin/env python3
"""Recover the lost Phase-2 Stage-B checkpoint from local agent transcripts.

This script never calls the frozen selector.  It extracts already-recorded bytes,
verifies every authoritative SHA-256, and refuses to overwrite differing files.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_ROOT = Path(
    "/home/master/.claude/projects/-home-master-llm-projects-philosophia"
)
CODEX_SESSION = Path(
    "/home/master/.codex/sessions/2026/08/14/"
    "rollout-2026-08-14T10-19-58-019fff24-52b4-7962-a2d0-4fb697935c63.jsonl"
)
ANNEX_SESSION = CLAUDE_ROOT / "4a860db1-6296-4c4a-9f80-254624b5cb84.jsonl"
CODE_SESSION = CLAUDE_ROOT / "537c1991-a987-4007-aded-c85adb41ef5a.jsonl"
L01_SESSION = CLAUDE_ROOT / "91788c31-b8bd-4ad7-ad5b-04358301ff5a.jsonl"
AUTHORITY_SESSION = CLAUDE_ROOT / "4d096aa4-d0f3-41a7-a72d-1f2080a54ce6.jsonl"

ANNEX_PATH = "/tmp/PHASE2_STAGE_B_L2_GENERATOR_ANNEX_FINAL_XY_REVIEW.md"
V2_ANNEX_PATH = "/tmp/PHASE2_STAGE_B_L2_GENERATOR_ANNEX_V2_NONVACUOUS_DRAFT.md"
CHARTER_PATH = "/tmp/PHASE2_STAGE_B_DEV_CORE_CHARTER_V1_1_1_BOUNDARY_CORRECTION.md"
GENERATOR_PATH = (
    "/tmp/minimo_phase2_stageb_l2_final/learning/phase2_stageb_generator.py"
)

EXPECTED = {
    "accepted_authority/PHASE2_STAGE_B_DEV_CORE_CHARTER_V1_1_1_BOUNDARY_CORRECTION.md":
        "703bf39cfe8f875f9be3781659a7365c1bc99c42f7523e43fef2c0a2c47b8311",
    "accepted_l2/PHASE2_STAGE_B_L2_GENERATOR_ANNEX_FINAL_XY_REVIEW.md":
        "3a78a53ecb8e5275f433bc03c50b7b93746c597e3d2d1fcf0bedd4249f102da8",
    "accepted_l2/learning/phase2_stageb_generator.py":
        "de9b05d6732dfe07c5303439a1fd533f9d6053a62a04480db0659075b16d2a34",
    "accepted_l2/learning/test_phase2_stageb_generator.py":
        "01adece50de5dc4cece3acfed80b21725ca7400e5d375204d5010eaae0dca4e8",
    "accepted_l2/PHASE2_STAGE_B_L2_CODE_GATE_V1.json":
        "8961b5a97ee0972d83a071e1b1c82869a9841f5f01c45add12a88dbfee1010f0",
    "accepted_l2/PHASE2_STAGE_B_L2_RAW_FIXTURE_EXCLUSIONS_V3.json":
        "a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d",
    "archive/accepted_l01/PHASE2_STAGE_B_L01_RAW_FIXTURE_EXCLUSIONS_V2.json":
        "31e319bdbfc7b17c65ac7c8698022c761f4f05790e1f044e692f736cf99d680a",
    "archive/accepted_l01/learning/phase2_stageb_canonical.py":
        "4f1c2490801a05236caa1a10193eeb5c7f8e03ba70a0263e6e12374d304fe7a0",
    "archive/accepted_l01/learning/phase2_stageb_causes.py":
        "574a81b75e98fbccc1f8e0344cf8fefd1ccb9e83043ac72e321d49798cb88c2e",
    "archive/accepted_l01/learning/phase2_stageb_checker.py":
        "1cedff634a60955a05e88a437f8100b70783b1900e523385a4da48e822673d2b",
    "archive/accepted_l01/learning/phase2_stageb_render.py":
        "c56073d0c4718aa5a95c48e5c58522937a935ca637d68687770126564a6d6621",
    "archive/accepted_l01/learning/phase2_stageb_schema.py":
        "00df17136fe8acfe53f9a56a1ff9d56c39c2c6a3cf7121dc722cf3978279e4a7",
    "archive/accepted_l01/learning/test_phase2_stageb_checker.py":
        "f107d87c687efa119a92d12cce93f23a9de51a863b0f68ab71acfc6f065dc03c",
    "archive/accepted_l01/learning/test_phase2_stageb_l0.py":
        "5ef47d7e69b289c36957272779c4168b2c701edd0f1ab500df3fb2f843307e55",
    "archive/accepted_l01/learning/test_phase2_stageb_theory_enumerability.py":
        "6a75207e182ee2b24f306275f36b95d5583cf63f30c0f3d9152fc729759ef19e",
    "archive/accepted_l01/learning/theories/propositional-logic-intuitionistic-fragment.p":
        "2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507",
    "patches/minimo_phase2_stageb_l01_v1_1_1_repair_v3_delta.patch":
        "1a67b09fb63784662cce56359c5cff897023cceec2f3dd445739d0a04cf00736",
    "patches/minimo_phase2_stagea_stageb_l01_v1_1_1_repair_v3_cumulative.patch":
        "c0b0e9ab79a66696231e356a92f6ccace67911d2bbe5906918ca6f4cbbe9a065",
    "patches/minimo_phase2_stageb_l2_v5_delta.patch":
        "299114e32cbf59edced992a94cdf5c1e03e322cb32dbdb7a3f94f63dc4276b95",
    "patches/minimo_phase2_stagea_stageb_l01_l2_v5_cumulative.patch":
        "3a570b2e35b15dc796d86cd8a997230c00bbf5aed3b5c06f3b14dca78b46b683",
    "archive/unaccepted_l3/PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_DRAFT.md":
        "a3760d619f147ec083bcd7cab4b158d39f13bce963f12ff8db236c85a9c0601a",
    "archive/unaccepted_l3/PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_AUTHOR_CHOICES.md":
        "f36e620e0a99a98f939f7ee2b1013fb59b45e022f56bbc15abe8f13c84f18ef4",
    "archive/unaccepted_l3/PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_DRIVER_HANDOFF.md":
        "4cc3bf9f98ae45c5e307a90a46fa10aaf004bd5b490f1601eb7d25734d38afdd",
    "science_inputs/TASK_A_SCIENCE_CONTRACT_OPUS5.md":
        "8590ca4fbddfc74364cf4e95cdb23e8f976befd2f0fd9f3af27a7092f0b9951c",
    "science_inputs/TASK_B_NOVELTY_SCAN_CODEX.md":
        "8657e3ea6073aec3bea2b10153202e1fdd0d36dc2b137c4419ee270d556ac095",
    "science_inputs/TASK_C_SLICE_ENG_AUDIT_CURSOR.md":
        "9ba84e0749dc8925cfd6765704b209110de97cd4d75d1d8cff9406d8e5df6186",
    "science_inputs/TASK_BOUNDED_ROUTE_OPUS4.8.md":
        "c6c3c15a3b1be73db7255d090cd728b9a7b03f4a68061b30761011e40a080d4d",
    "science_inputs/TASK_SCIENTIFIC_REVIEW_GPT5.5.md":
        "89ab37c2829507fb89d620e0130cf8f3ad73111cdf5ba96bbbe47c32a689c78e",
    "science_inputs/TASK_SCIENTIFIC-CONTRACT_REVIEW_OPUS5.md":
        "6bdd05a09b17ecee30c262488da5de9fa9e9340b46fad3d2bb44b965785ce4ed",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def records(path: Path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            yield json.loads(line)


def claude_tool_uses(path: Path):
    for record in records(path):
        if record.get("type") != "assistant":
            continue
        for block in record.get("message", {}).get("content", []):
            if block.get("type") == "tool_use":
                yield block


def claude_read_payload(path: Path, file_path: str) -> bytes:
    """Return a byte-identical full-file Read payload recorded by Claude."""
    candidates = []
    for record in records(path):
        result = record.get("toolUseResult")
        if not isinstance(result, dict):
            continue
        file_result = result.get("file")
        if not isinstance(file_result, dict):
            continue
        if file_result.get("filePath") != file_path:
            continue
        content = file_result.get("content")
        if not isinstance(content, str):
            raise RuntimeError(f"non-text Claude Read payload {file_path}")
        candidates.append(content.encode("utf-8"))
    if not candidates:
        raise RuntimeError(f"missing Claude Read payload {file_path}")
    if any(candidate != candidates[0] for candidate in candidates[1:]):
        raise RuntimeError(f"conflicting Claude Read payloads {file_path}")
    return candidates[0]


def recover_charter() -> bytes:
    candidates = [
        claude_read_payload(session, CHARTER_PATH)
        for session in (ANNEX_SESSION, CODE_SESSION, AUTHORITY_SESSION)
    ]
    if any(candidate != candidates[0] for candidate in candidates[1:]):
        raise RuntimeError("conflicting cross-session Stage-B charter payloads")
    return candidates[0]


def replay_final_annex() -> bytes:
    files: dict[str, str] = {}
    copy_needle = (
        "cp PHASE2_STAGE_B_L2_GENERATOR_ANNEX_V2_NONVACUOUS_DRAFT.md "
        "PHASE2_STAGE_B_L2_GENERATOR_ANNEX_FINAL_XY_REVIEW.md"
    )
    for tool in claude_tool_uses(ANNEX_SESSION):
        name = tool.get("name")
        item = tool.get("input", {})
        path = item.get("file_path")
        if name == "Write" and isinstance(path, str):
            files[path] = item["content"]
        elif name == "Edit" and isinstance(path, str) and path in files:
            old = item["old_string"]
            new = item["new_string"]
            count = files[path].count(old)
            if count == 0:
                raise RuntimeError(f"annex replay needle missing in {path}")
            if item.get("replace_all"):
                files[path] = files[path].replace(old, new)
            else:
                if count != 1:
                    raise RuntimeError(f"non-unique annex replay needle in {path}")
                files[path] = files[path].replace(old, new, 1)
        elif name == "Bash" and copy_needle in item.get("command", ""):
            files[ANNEX_PATH] = files[V2_ANNEX_PATH]
    return files[ANNEX_PATH].encode("ascii")


def claude_tool_result(path: Path, tool_use_id: str) -> str:
    for record in records(path):
        if record.get("type") != "user":
            continue
        for block in record.get("message", {}).get("content", []):
            if not isinstance(block, dict):
                continue
            if (
                block.get("type") == "tool_result"
                and block.get("tool_use_id") == tool_use_id
            ):
                content = block.get("content")
                if not isinstance(content, str):
                    raise RuntimeError(f"non-text tool result {tool_use_id}")
                return content
    raise RuntimeError(f"missing Claude tool result {tool_use_id}")


def decode_numbered_read(content: str) -> bytes:
    values = []
    expected_line = 1
    for line in content.splitlines():
        match = re.match(r"^(\d+)\t(.*)$", line)
        if not match:
            continue
        number = int(match.group(1))
        if number != expected_line:
            raise RuntimeError(f"numbered Read gap at {expected_line}, got {number}")
        values.append(match.group(2))
        expected_line += 1
    if not values:
        raise RuntimeError("empty numbered Read result")
    return "\n".join(values).encode("ascii")


def apply_unified_diff(original: bytes, patch_text: str) -> bytes:
    """Apply the recorded V2->V3 single-file diff without external tools."""
    source = original.decode("ascii").splitlines(keepends=True)
    patch_lines = patch_text.splitlines(keepends=True)
    output: list[str] = []
    source_index = 0
    index = 0
    saw_hunk = False
    while index < len(patch_lines):
        header = re.match(r"^@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@", patch_lines[index])
        if not header:
            index += 1
            continue
        saw_hunk = True
        old_start = int(header.group(1)) - 1
        if old_start < source_index:
            raise RuntimeError("overlapping unified-diff hunks")
        output.extend(source[source_index:old_start])
        source_index = old_start
        index += 1
        while index < len(patch_lines) and not patch_lines[index].startswith("@@"):
            line = patch_lines[index]
            if line.startswith(" "):
                if source_index >= len(source) or source[source_index] != line[1:]:
                    raise RuntimeError("unified-diff context mismatch")
                output.append(source[source_index])
                source_index += 1
            elif line.startswith("-"):
                if source_index >= len(source) or source[source_index] != line[1:]:
                    raise RuntimeError("unified-diff deletion mismatch")
                source_index += 1
            elif line.startswith("+"):
                output.append(line[1:])
            elif line.startswith("\\ No newline at end of file"):
                pass
            else:
                break
            index += 1
    if not saw_hunk:
        raise RuntimeError("recorded V2->V3 diff has no hunks")
    output.extend(source[source_index:])
    return "".join(output).encode("ascii")


def recover_l01_v3_test() -> bytes:
    v2 = decode_numbered_read(
        claude_tool_result(L01_SESSION, "toolu_01LusWUUsMkvy7SE14yphWdK")
    )
    patch_text = claude_tool_result(
        L01_SESSION, "toolu_01A8eXVF3Nhe4fudgxiVXSeB"
    )
    return apply_unified_diff(v2, patch_text)


def recover_l01_sources() -> dict[str, bytes]:
    reads = {
        "phase2_stageb_schema.py": "toolu_01MmaMZjAEiMu2prpdinyqHD",
        "phase2_stageb_canonical.py": "toolu_01MfCavz3KJJ8ntVMBGmFxgG",
        "phase2_stageb_causes.py": "toolu_01E9PZqKvcKcdt9cBrih2v7g",
        "phase2_stageb_render.py": "toolu_01QStugWfvkhWKtShqBorvdX",
        "phase2_stageb_checker.py": "toolu_01K1A4Hac7kUoNUYrggi7PwL",
        "test_phase2_stageb_l0.py": "toolu_01BskNqTpEsguUY69QcmdYoS",
        "test_phase2_stageb_theory_enumerability.py":
            "toolu_01DTX9U7Cttq7dZjoaaLKJD4",
    }
    recovered = {
        f"archive/accepted_l01/learning/{name}": decode_numbered_read(
            claude_tool_result(L01_SESSION, tool_id)
        )
        for name, tool_id in reads.items()
    }
    recovered[
        "archive/accepted_l01/learning/test_phase2_stageb_checker.py"
    ] = recover_l01_v3_test()
    recovered[
        "archive/accepted_l01/learning/theories/"
        "propositional-logic-intuitionistic-fragment.p"
    ] = claude_tool_result(
        L01_SESSION, "toolu_01DVCk95aQpvRvUFFDo3PWwW"
    ).encode("ascii") + b"\n"
    return recovered


def run_git(arguments: list[str], cwd: Path) -> bytes:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=cwd,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def materialize(tree: Path, relative: str, data: bytes) -> None:
    destination = tree / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)


def generate_patches(
    l01_sources: dict[str, bytes], generator: bytes, generator_test: bytes
) -> dict[str, bytes]:
    minimo = Path("/home/master/llm_projects/minimo")
    base = "6066f482c6752915ad21119f93dc162f4cb9db72"
    stage_a = Path(
        "/home/master/llm_projects/philosophia/"
        "successor/dev/minimo_phase2_stage_a_19.patch"
    )
    if sha256(stage_a.read_bytes()) != (
        "e08a8d29d67d82297216722b3e13e6c1a3f4bd354962a2865b1cfc57a9980bbd"
    ):
        raise RuntimeError("Stage-A patch hash mismatch")
    if run_git(["rev-parse", base], minimo).decode("ascii").strip() != base:
        raise RuntimeError("MINIMO base commit is unavailable")

    source_prefix = "archive/accepted_l01/"

    def populate_l01(tree: Path) -> list[str]:
        paths = []
        for relative, data in l01_sources.items():
            if not relative.startswith(source_prefix):
                raise RuntimeError(f"unexpected L0/L1 source path {relative}")
            target = relative[len(source_prefix):]
            materialize(tree, target, data)
            paths.append(target)
        return sorted(paths)

    def fresh_tree(parent: Path) -> Path:
        tree = parent / "tree"
        run_git(["clone", "-q", "--no-local", str(minimo), str(tree)], parent)
        run_git(["checkout", "-q", base], tree)
        run_git(["apply", str(stage_a)], tree)
        return tree

    patches = {}
    with tempfile.TemporaryDirectory(prefix="phase2-l01-recovery-") as temp:
        tree = fresh_tree(Path(temp))
        l01_paths = populate_l01(tree)
        run_git(["add", "--", *l01_paths], tree)
        patches[
            "patches/minimo_phase2_stageb_l01_v1_1_1_repair_v3_delta.patch"
        ] = run_git(["diff", "--cached", "--binary"], tree)
        run_git(["add", "-A"], tree)
        patches[
            "patches/"
            "minimo_phase2_stagea_stageb_l01_v1_1_1_repair_v3_cumulative.patch"
        ] = run_git(["diff", "--cached", "--binary"], tree)

    with tempfile.TemporaryDirectory(prefix="phase2-l2-recovery-") as temp:
        tree = fresh_tree(Path(temp))
        populate_l01(tree)
        materialize(tree, "learning/phase2_stageb_generator.py", generator)
        materialize(tree, "learning/test_phase2_stageb_generator.py", generator_test)
        run_git(
            [
                "add", "--",
                "learning/phase2_stageb_generator.py",
                "learning/test_phase2_stageb_generator.py",
            ],
            tree,
        )
        patches["patches/minimo_phase2_stageb_l2_v5_delta.patch"] = run_git(
            ["diff", "--cached", "--binary"], tree
        )
        run_git(["add", "-A"], tree)
        patches[
            "patches/minimo_phase2_stagea_stageb_l01_l2_v5_cumulative.patch"
        ] = run_git(["diff", "--cached", "--binary"], tree)
    return patches


def recover_generator() -> bytes:
    content = claude_tool_result(CODE_SESSION, "toolu_013RQouNr8R1b5j96UX2v54t")
    return decode_numbered_read(content)


def codex_output(call_id: str) -> str:
    for record in records(CODEX_SESSION):
        payload = record.get("payload", {})
        if (
            record.get("type") == "response_item"
            and payload.get("type") == "custom_tool_call_output"
            and payload.get("call_id") == call_id
        ):
            return "".join(
                block.get("text", "")
                for block in payload.get("output", [])
                if isinstance(block, dict)
            )
    raise RuntimeError(f"missing Codex output {call_id}")


def numbered_map(text: str) -> dict[int, str]:
    result: dict[int, str] = {}
    for line in text.splitlines():
        match = re.match(r"^\s*(\d+)\t(.*)$", line)
        if not match:
            continue
        number = int(match.group(1))
        value = match.group(2)
        # A parallel tool result may contain several separately numbered files.
        # Required ranges below are unambiguous; retain their first occurrence.
        result.setdefault(number, value)
    return result


def line_block(lines: dict[int, str], start: int, stop: int) -> str:
    missing = [number for number in range(start, stop + 1) if number not in lines]
    if missing:
        raise RuntimeError(f"missing transcript lines: {missing[:5]}")
    return "".join(lines[number] + "\n" for number in range(start, stop + 1))


def recover_v5_test() -> bytes:
    v3 = numbered_map(codex_output("call_3L1lKpEDGUmCbOBkVJXgds0l"))
    second_v3 = numbered_map(codex_output("call_cuBUr9pIhRdYliqnNHXPjqQ1"))
    conflicts = []
    for number, value in second_v3.items():
        if number in v3 and v3[number] != value:
            conflicts.append(number)
        v3[number] = value
    # The first parallel transcript was output-budget truncated in the middle
    # of line 524.  The dedicated overlapping read supplies that complete line.
    if conflicts != [524]:
        raise RuntimeError(f"unexpected V3 transcript conflicts: {conflicts}")
    v4 = numbered_map(codex_output("call_IgjrouLyoiG2F26ZcKYJcO8d"))
    v5 = numbered_map(codex_output("call_PFIUXRmEWh3p2lj1gYf5MJPL"))

    source = line_block(v3, 1, 62)
    source += "    BAND_EDGES,\n    BAND_NAMES,\n"
    source += line_block(v3, 63, 642)
    source += line_block(v4, 645, 651)
    source += line_block(v3, 643, 650)
    source += line_block(v4, 660, 702)
    source += line_block(v3, 651, 1074)
    source += line_block(v4, 1127, 1535)

    repairs = (
        (line_block(v4, 1215, 1232), line_block(v5, 1215, 1233)),
        (line_block(v4, 1257, 1277), line_block(v5, 1258, 1281)),
    )
    for old, new in repairs:
        if source.count(old) != 1:
            raise RuntimeError("V4->V5 repair block is not unique")
        source = source.replace(old, new, 1)
    return source.encode("ascii")


def recover_one_line_json(label: str) -> bytes:
    text = codex_output("call_bQJrIJdPdbXQ1i0oh6wey9xV")
    marker = f"--- {label} ---\n"
    start = text.find(marker)
    if start < 0:
        raise RuntimeError(f"missing JSON section {label}")
    tail = text[start + len(marker):]
    match = re.search(r"(?m)^\s*1\t(\{.*\})$", tail)
    if not match:
        raise RuntimeError(f"missing JSON payload {label}")
    return (match.group(1) + "\n").encode("ascii")


def claude_last_write(file_path: str) -> bytes:
    content = None
    for tool in claude_tool_uses(ANNEX_SESSION):
        item = tool.get("input", {})
        if tool.get("name") == "Write" and item.get("file_path") == file_path:
            content = item["content"]
    if content is None:
        raise RuntimeError(f"missing Claude Write payload {file_path}")
    return content.encode("utf-8")


def write_verified(relative: str, data: bytes) -> None:
    expected = EXPECTED[relative]
    actual = sha256(data)
    if actual != expected:
        raise RuntimeError(f"hash mismatch for {relative}: {actual} != {expected}")
    destination = ROOT / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        old = destination.read_bytes()
        if old != data:
            raise RuntimeError(f"refusing to overwrite differing {destination}")
        return
    destination.write_bytes(data)


def main() -> None:
    generator = recover_generator()
    generator_test = recover_v5_test()
    recovered = {
        "accepted_authority/PHASE2_STAGE_B_DEV_CORE_CHARTER_V1_1_1_BOUNDARY_CORRECTION.md":
            recover_charter(),
        "accepted_l2/PHASE2_STAGE_B_L2_GENERATOR_ANNEX_FINAL_XY_REVIEW.md":
            replay_final_annex(),
        "accepted_l2/learning/phase2_stageb_generator.py": generator,
        "accepted_l2/learning/test_phase2_stageb_generator.py": generator_test,
        "accepted_l2/PHASE2_STAGE_B_L2_CODE_GATE_V1.json":
            recover_one_line_json("gate"),
        "accepted_l2/PHASE2_STAGE_B_L2_RAW_FIXTURE_EXCLUSIONS_V3.json":
            recover_one_line_json("ledger head"),
        "archive/accepted_l01/PHASE2_STAGE_B_L01_RAW_FIXTURE_EXCLUSIONS_V2.json":
            recover_one_line_json("v2"),
    }
    l01_sources = recover_l01_sources()
    recovered.update(l01_sources)
    recovered.update(generate_patches(l01_sources, generator, generator_test))

    for name in (
        "PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_DRAFT.md",
        "PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_AUTHOR_CHOICES.md",
        "PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_DRIVER_HANDOFF.md",
    ):
        relative = f"archive/unaccepted_l3/{name}"
        recovered[relative] = claude_last_write(f"/tmp/{name}")

    documents = Path("/home/master/Documents/my/philosophia")
    for name in (
        "TASK_A_SCIENCE_CONTRACT_OPUS5.md",
        "TASK_B_NOVELTY_SCAN_CODEX.md",
        "TASK_C_SLICE_ENG_AUDIT_CURSOR.md",
        "TASK_BOUNDED_ROUTE_OPUS4.8.md",
        "TASK_SCIENTIFIC_REVIEW_GPT5.5.md",
        "TASK_SCIENTIFIC-CONTRACT_REVIEW_OPUS5.md",
    ):
        recovered[f"science_inputs/{name}"] = (documents / name).read_bytes()

    for relative, data in recovered.items():
        write_verified(relative, data)

    manifest = "".join(
        f"{EXPECTED[relative]}  {relative}\n" for relative in sorted(recovered)
    ).encode("ascii")
    manifest_path = ROOT / "SHA256SUMS"
    if manifest_path.exists() and manifest_path.read_bytes() != manifest:
        for line in manifest_path.read_text(encoding="ascii").splitlines():
            old_hash, old_relative = line.split("  ", 1)
            if EXPECTED.get(old_relative) != old_hash:
                raise RuntimeError(
                    f"refusing to replace conflicting entry {old_relative}"
                )
    manifest_path.write_bytes(manifest)
    print(f"Recovered and verified {len(recovered)} artifacts under {ROOT}")


if __name__ == "__main__":
    main()
