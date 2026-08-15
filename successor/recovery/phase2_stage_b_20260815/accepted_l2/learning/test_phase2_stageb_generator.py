#!/usr/bin/env python3
"""Stage-B L2 generator gate. No silent 5x256 scan during discovery."""

from __future__ import annotations

import ast
import hashlib
import hmac
import json
import math
import os
import subprocess
import sys
import types
import unittest
from copy import deepcopy
from pathlib import Path

LEARNING_DIR = Path(__file__).resolve().parent
if str(LEARNING_DIR) not in sys.path:
    sys.path.insert(0, str(LEARNING_DIR))

from phase2_stageb_canonical import canonical_bytes, canonical_hash
from phase2_stageb_checker import check_plan
from phase2_stageb_generator import (
    CHAIN_LEN_CAP,
    CURSOR_KEYS,
    DIR_KINDS,
    DRAW_SCHEMA,
    FIXTURE_KEY_0,
    FIXTURE_KEY_1,
    FIXTURE_KEY_2,
    FIXTURE_KEY_3,
    FIXTURE_KEY_4,
    FIXTURE_KEYS,
    L2_CONSTRUCTION_SUBCAUSES,
    L2_FAILURE_KEYS,
    L2_PRF_DOMAIN,
    L2_PRF_SEPARATOR,
    L2_SCAFFOLDS,
    L2_SUCCESS_KEYS,
    MAX_DECISION_CALLS,
    MAX_FORMULA_RECURSION_FRAMES,
    PRF_MAX_REJECTIONS_PER_CALL,
    TRIPLES,
    WORD_MODULUS,
    WORDS_PER_BLOCK,
    _is_refuse,
    _nonvacuity,
    _randbelow_from_words,
    build_chain,
    colex_unrank,
    generate_draw,
    lehmer_decode,
    make_cursor,
    next_word,
    randbelow,
    sample_positive,
    sampler_word_count,
    summarize_plan,
)
from phase2_stageb_schema import (
    BAND_EDGES,
    BAND_NAMES,
    FAMILY_ORDER,
    MAX_FORMULA_NODES,
    PROOF_CHILD_FIELDS,
)

ANNEX_SHA256 = (
    '3a78a53ecb8e5275f433bc03c50b7b93746c597e3d2d1fcf0bedd4249f102da8'
)
CODE_GATE_SCHEMA = 'philosophia.stageb.l2-code-gate.v1'
SCAN_DRAW_INDEX_START = 0
SCAN_DRAW_INDEX_STOP_EXCLUSIVE = 256
RULE_KIND_ORDER = (
    'ASSUME',
    'AND_INTRO',
    'AND_ELIM_LEFT',
    'AND_ELIM_RIGHT',
    'OR_INTRO_LEFT',
    'OR_INTRO_RIGHT',
    'OR_ELIM',
    'NOT_INTRO',
    'NOT_ELIM',
    'EXFALSO',
)
TRIPLE_COUNTS = (
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 88, 96, 102, 106, 108,
    108, 106, 102, 96, 88, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1,
)
FORBIDDEN_IMPORTS = {
    'phase2_stageb_checker', 'phase2_stageb_render', 'peano', 'torch',
    'proofsearch', 'policy', 'phase2_policy', 'phase2_search', 'phase2_root',
    'phase2_isolated', 'phase2_actions', 'phase2_spec', 'transformers', 'numpy',
    'random', 'sec' + 'rets', 'os', 'subprocess', 'json',
}
ALLOWED_IMPORTS = {
    'phase2_stageb_schema', 'phase2_stageb_canonical', 'phase2_stageb_causes',
    'hmac', 'hashlib', 'math', 'typing', '__future__', 'annotations',
}
FORBIDDEN_SUBSTRINGS = (
    'check_plan', 'skeleton', 'bijection', 'public_projection', 'compile',
    'alpha', 'canonicaliz',
)
GEN_PATH = LEARNING_DIR / 'phase2_stageb_generator.py'
TEST_PATH = Path(__file__).resolve()

# Unfilled until the one frozen selection of annex section 10.7.
CODE_GATE_LITERAL_ROWS = (
    {
        'band': 'S1',
        'canonical_result_sha256': 'edae633493e2bddc23f6521c5de033af87f03047abf5269038241b3481869e7b',
        'dir': 'AND_ELIM_LEFT',
        'draw_index': 0,
        'families': ['AND_INTRO', 'AND_ELIM', 'NOT_INTRO', 'NOT_ELIM'],
        'fixture_name': 'l2_gate_00',
        'key_hex': '0000000000000000000000000000000000000000000000000000000000000000',
        'max_dependency_depth': 4,
        'node_count': 9,
        'raw_plan_sha256': '4a4993eb88b1cc4f01824b7886a1592573296fa05531bce765a48ded20b418c3',
        'raw_theorem_sha256': 'd495d65a1b408b875a045011b721cca64da186c1dc4fb9a4b740ce786170bfd3',
        'scaffold': 'C',
        'words_consumed': 33,
    },
    {
        'band': 'S2',
        'canonical_result_sha256': 'caea1a7533716a52f1852b14aec57dc903fc5d9e73b4cd07c62a09b35abd1105',
        'dir': 'AND_ELIM_LEFT',
        'draw_index': 1,
        'families': ['AND_INTRO', 'AND_ELIM', 'NOT_INTRO', 'NOT_ELIM'],
        'fixture_name': 'l2_gate_01',
        'key_hex': '0000000000000000000000000000000000000000000000000000000000000000',
        'max_dependency_depth': 6,
        'node_count': 13,
        'raw_plan_sha256': 'eceb400c1225033b50468815de0c13bceac81406c1d2383a55598e272c1fd827',
        'raw_theorem_sha256': 'da695ab886307f782a67f9e92188cfbf61b8d86ac01e74d4e40b490f41779122',
        'scaffold': 'C',
        'words_consumed': 40,
    },
    {
        'band': 'S3',
        'canonical_result_sha256': '6106fed8a5a02778f6f43ca81aa1b457675a06f8dcea5f2329858f25006652f4',
        'dir': 'AND_ELIM_LEFT',
        'draw_index': 2,
        'families': ['AND_INTRO', 'AND_ELIM', 'NOT_INTRO', 'NOT_ELIM'],
        'fixture_name': 'l2_gate_02',
        'key_hex': '0000000000000000000000000000000000000000000000000000000000000000',
        'max_dependency_depth': 11,
        'node_count': 23,
        'raw_plan_sha256': '92a8f53e3d9b6f311d51d50e5ce2bb38ea4c02f70a500262d80480a17426c2b4',
        'raw_theorem_sha256': 'd1e2b44c99cd6071bd69beb3667328a26e6e2760f1230a69e0e247ca45e9194f',
        'scaffold': 'C',
        'words_consumed': 40,
    },
    {
        'band': 'S4',
        'canonical_result_sha256': 'fb8f2551dcb2b85f1bcce6b10d7aff4304e1f5991822b72626bf0e93dcec52b1',
        'dir': 'AND_ELIM_RIGHT',
        'draw_index': 3,
        'families': ['AND_INTRO', 'AND_ELIM', 'NOT_INTRO', 'NOT_ELIM'],
        'fixture_name': 'l2_gate_03',
        'key_hex': '0000000000000000000000000000000000000000000000000000000000000000',
        'max_dependency_depth': 12,
        'node_count': 31,
        'raw_plan_sha256': 'ff340e64976d8f04ee35d5e5f9488cfa7d2f06af530221b6d553632f5a35fe56',
        'raw_theorem_sha256': '7944c568325dc2b5beb742eeed6a853d2be5355b12e54483cf8171f13f550707',
        'scaffold': 'C',
        'words_consumed': 59,
    },
    {
        'band': 'S1',
        'canonical_result_sha256': '38e21395835c5d5beb44ed11df303ac02e6d3809b207a071b4ddd258727f99f1',
        'dir': 'AND_ELIM_RIGHT',
        'draw_index': 4,
        'families': ['AND_INTRO', 'AND_ELIM', 'OR_ELIM', 'NOT_ELIM', 'EXFALSO'],
        'fixture_name': 'l2_gate_04',
        'key_hex': '0000000000000000000000000000000000000000000000000000000000000000',
        'max_dependency_depth': 4,
        'node_count': 8,
        'raw_plan_sha256': '00490e2cec70ede6844647627f5174e890b2f54647372ea6347a724b53118af3',
        'raw_theorem_sha256': 'f119dbda885f9604a08252b3e63b7becb75335571cb081be86d59d9ebb76ad6e',
        'scaffold': 'B',
        'words_consumed': 45,
    },
    {
        'band': 'S4',
        'canonical_result_sha256': '1ddf80c4ba56e6ac512e1490d69c482d42e35bd37f91a490cf0f559153eb4ba6',
        'dir': 'AND_ELIM_LEFT',
        'draw_index': 7,
        'families': ['AND_INTRO', 'AND_ELIM', 'OR_INTRO', 'OR_ELIM'],
        'fixture_name': 'l2_gate_05',
        'key_hex': '0000000000000000000000000000000000000000000000000000000000000000',
        'max_dependency_depth': 12,
        'node_count': 35,
        'raw_plan_sha256': '757db0e0fb73598266652faa3efed7ed7affa5a672373d63eda14b749f4649d7',
        'raw_theorem_sha256': '6a49b846889aa740d03e9280a9228f97da18cd3db8523c299f9f343bc694e0a8',
        'scaffold': 'A',
        'words_consumed': 57,
    },
)


def _atom(name):
    return {'kind': 'ATOM', 'name': name}


def _and(left, right):
    return {'kind': 'AND', 'left': left, 'right': right}


def _or(left, right):
    return {'kind': 'OR', 'left': left, 'right': right}


def _not(arg):
    return {'kind': 'NOT', 'arg': arg}


def _false():
    return {'kind': 'FALSE'}


def iter_proof_nodes(node):
    yield node
    for field in PROOF_CHILD_FIELDS[node['kind']]:
        yield from iter_proof_nodes(node[field])


def collect_kinds(proof):
    return {node['kind'] for node in iter_proof_nodes(proof)}


def gadget_node(plan):
    return plan['proof']['right']['right']


def infer_scaffold(plan):
    gadget = gadget_node(plan)
    if gadget['kind'] == 'NOT_INTRO':
        return 'C'
    if gadget['kind'] == 'OR_ELIM' and gadget['left_branch']['kind'] == 'EXFALSO':
        return 'B'
    return 'A'


def infer_dir(plan):
    for node in iter_proof_nodes(plan['proof']):
        if node['kind'] in DIR_KINDS:
            return node['kind']
    raise AssertionError('no AND_ELIM direction in plan')


def formula_leaves(formula):
    kind = formula['kind']
    if kind == 'ATOM':
        return 1
    if kind == 'FALSE':
        return 0
    if kind == 'NOT':
        return formula_leaves(formula['arg'])
    return formula_leaves(formula['left']) + formula_leaves(formula['right'])


def formula_atoms(formula, acc=None):
    if acc is None:
        acc = set()
    kind = formula['kind']
    if kind == 'ATOM':
        acc.add(formula['name'])
        return acc
    if kind == 'FALSE':
        return acc
    if kind == 'NOT':
        return formula_atoms(formula['arg'], acc)
    formula_atoms(formula['left'], acc)
    formula_atoms(formula['right'], acc)
    return acc


def formula_node_count(formula):
    kind = formula['kind']
    if kind in ('ATOM', 'FALSE'):
        return 1
    if kind == 'NOT':
        return 1 + formula_node_count(formula['arg'])
    return 1 + formula_node_count(formula['left']) + formula_node_count(formula['right'])


def sampler_params(plan, scaffold):
    hyps = {hyp['id']: hyp['formula'] for hyp in plan['hypotheses']}
    if scaffold == 'A':
        field1 = hyps['h0']['left']
        field2 = hyps['h0']['right']
    elif scaffold == 'B':
        field1 = hyps['h1']['arg']
        field2 = plan['goal']['right']['right']
    else:
        field1 = hyps['h0']['arg']
        mid = plan['goal']['right']['right']['arg']
        left_bytes = canonical_bytes(mid['left'])
        if left_bytes == canonical_bytes(field1):
            field2 = mid['right']
        else:
            field2 = mid['left']
    return (
        formula_leaves(field1),
        len(formula_atoms(field1)),
        formula_leaves(field2),
        len(formula_atoms(field2)),
    )


def closed_form_words(plan, expectation):
    scaffold = infer_scaffold(plan)
    n1, m1, n2, m2 = sampler_params(plan, scaffold)
    size = expectation['node_count'] - 6
    return 10 + sampler_word_count(n1, m1) + sampler_word_count(n2, m2) + size


def generate_draw_with_captured_cursor(root_key, draw_index):
    import phase2_stageb_generator as gen_mod
    original_make = gen_mod.make_cursor
    captured = []

    def wrapped(key, index):
        cursor = original_make(key, index)
        captured.append(cursor)
        return cursor

    gen_mod.make_cursor = wrapped
    try:
        result = gen_mod.generate_draw(root_key, draw_index)
    finally:
        gen_mod.make_cursor = original_make
    if len(captured) != 1:
        raise AssertionError('public generate_draw must use exactly one cursor')
    return result, captured[0]


def walk_container_ids(obj, seen):
    if type(obj) is dict or type(obj) is list:
        ident = id(obj)
        if ident in seen:
            return False
        seen.add(ident)
        values = obj.values() if type(obj) is dict else obj
        return all(walk_container_ids(value, seen) for value in values)
    return True


def test_eval_formula(formula, nu):
    kind = formula['kind']
    if kind == 'ATOM':
        return bool(nu[formula['name']])
    if kind == 'FALSE':
        return False
    if kind == 'NOT':
        return not test_eval_formula(formula['arg'], nu)
    if kind == 'AND':
        return (
            test_eval_formula(formula['left'], nu)
            and test_eval_formula(formula['right'], nu)
        )
    return (
        test_eval_formula(formula['left'], nu)
        or test_eval_formula(formula['right'], nu)
    )


def exhaustive_globals_satisfiable(plan):
    atoms = list(plan['atoms'])
    k = len(atoms)
    hyps = [hyp['formula'] for hyp in plan['hypotheses']]
    for mask in range(1 << k):
        nu = {atoms[i]: bool((mask >> i) & 1) for i in range(k)}
        if all(test_eval_formula(formula, nu) for formula in hyps):
            return True
    return False


def locals_in_scope(node, bound=None):
    if bound is None:
        bound = set()
    kind = node['kind']
    if kind == 'OR_ELIM':
        left_bound = bound | {node['left_assumption']['id']}
        right_bound = bound | {node['right_assumption']['id']}
        if not locals_in_scope(node['major'], bound):
            return False
        if not locals_in_scope(node['left_branch'], left_bound):
            return False
        if not locals_in_scope(node['right_branch'], right_bound):
            return False
        return True
    if kind == 'NOT_INTRO':
        body_bound = bound | {node['assumption']['id']}
        return locals_in_scope(node['body'], body_bound)
    if kind in ('EXFALSO', 'NOT_ELIM'):
        if not bound:
            return False
    for field in PROOF_CHILD_FIELDS[kind]:
        if not locals_in_scope(node[field], bound):
            return False
    return True


def independent_nonvacuity(plan):
    if not exhaustive_globals_satisfiable(plan):
        return False
    goal_bytes = canonical_bytes(plan['goal'])
    for hyp in plan['hypotheses']:
        if hyp['formula']['kind'] == 'FALSE':
            return False
        if canonical_bytes(hyp['formula']) == goal_bytes:
            return False
    if plan['proof']['kind'] != 'AND_INTRO':
        return False
    if not locals_in_scope(plan['proof']):
        return False
    return True


def maximal_and_elim_lengths(proof):
    lengths = []

    def walk(node, parent_elim):
        kind = node['kind']
        is_elim = kind in DIR_KINDS
        if is_elim and not parent_elim:
            length = 0
            cursor = node
            while cursor['kind'] in DIR_KINDS:
                length += 1
                cursor = cursor['source']
            lengths.append(length)
        for field in PROOF_CHILD_FIELDS[kind]:
            walk(node[field], is_elim)

    walk(proof, False)
    return lengths


def longest_exfalso_chain(proof):
    best = 0

    def walk(node):
        nonlocal best
        kind = node['kind']
        if kind == 'EXFALSO':
            length = 0
            cursor = node
            while cursor['kind'] == 'EXFALSO':
                length += 1
                cursor = cursor['source']
            if length > best:
                best = length
        for field in PROOF_CHILD_FIELDS[kind]:
            walk(node[field])

    walk(proof)
    return best


def structurally_diverse_S4(plan, expectation):
    if expectation['band'] != 'S4':
        return False
    if len(expectation['families']) < 4:
        return False
    if expectation['max_dependency_depth'] < 5:
        return False
    if len(plan['hypotheses']) < 4:
        return False
    kinds = collect_kinds(plan['proof'])
    if 'OR_ELIM' not in kinds and 'NOT_INTRO' not in kinds:
        return False
    long_chains = [length for length in maximal_and_elim_lengths(plan['proof']) if length >= 1]
    if len(long_chains) < 2:
        return False
    if longest_exfalso_chain(plan['proof']) > 1:
        return False
    return True


def coverage_elements(result):
    plan = result['plan']
    expectation = result['expectation']
    elements = {('band', expectation['band'])}
    for kind in collect_kinds(plan['proof']):
        if kind in RULE_KIND_ORDER:
            elements.add(('kind', kind))
    for family in expectation['families']:
        elements.add(('family', family))
    elements.add(('scaffold', infer_scaffold(plan)))
    elements.add(('dir', infer_dir(plan)))
    return elements


COVER_UNIVERSE = (
    {('band', name) for name in ('S1', 'S2', 'S3', 'S4')}
    | {('kind', kind) for kind in RULE_KIND_ORDER}
    | {('family', family) for family in FAMILY_ORDER}
    | {('scaffold', name) for name in L2_SCAFFOLDS}
    | {('dir', kind) for kind in DIR_KINDS}
)


def fixture_key_hex_list():
    return [key.hex() for key in FIXTURE_KEYS]


def selected_row_record(fixture_name, key, draw_index, result, checked):
    plan = result['plan']
    expectation = result['expectation']
    return {
        'band': expectation['band'],
        'canonical_result_sha256': canonical_hash(result),
        'dir': infer_dir(plan),
        'draw_index': draw_index,
        'families': list(expectation['families']),
        'fixture_name': fixture_name,
        'key_hex': key.hex(),
        'max_dependency_depth': expectation['max_dependency_depth'],
        'node_count': expectation['node_count'],
        'raw_plan_sha256': canonical_hash(plan),
        'raw_theorem_sha256': canonical_hash(checked['theorem']),
        'scaffold': infer_scaffold(plan),
        'words_consumed': result['words_consumed'],
    }


def coverage_payload(rows, results_by_name):
    bands = []
    kinds = []
    families = []
    scaffolds = []
    directions = []
    diverse = False
    for row in rows:
        result = results_by_name[row['fixture_name']]
        if row['band'] not in bands:
            bands.append(row['band'])
        for kind in RULE_KIND_ORDER:
            if kind in collect_kinds(result['plan']['proof']) and kind not in kinds:
                kinds.append(kind)
        for family in FAMILY_ORDER:
            if family in row['families'] and family not in families:
                families.append(family)
        if row['scaffold'] not in scaffolds:
            scaffolds.append(row['scaffold'])
        if row['dir'] not in directions:
            directions.append(row['dir'])
        if structurally_diverse_S4(result['plan'], result['expectation']):
            diverse = True
    return {
        'bands': [name for name in ('S1', 'S2', 'S3', 'S4') if name in bands],
        'catalogue': [name for name in L2_SCAFFOLDS if name in scaffolds],
        'directions': [kind for kind in DIR_KINDS if kind in directions],
        'diverse_s4': diverse,
        'families': [family for family in FAMILY_ORDER if family in families],
        'rule_kinds': [kind for kind in RULE_KIND_ORDER if kind in kinds],
    }


def select_l2_code_gate_rows():
    """Annex 10.7 greedy coverage plus diverse-S4 append. Not a test_*."""
    accepted = []
    first_diverse = None
    for key in FIXTURE_KEYS:
        for draw_index in range(
                SCAN_DRAW_INDEX_START, SCAN_DRAW_INDEX_STOP_EXCLUSIVE):
            result = generate_draw(key, draw_index)
            if not result['ok']:
                continue
            checked = check_plan(result['plan'], result['expectation'])
            if not checked['ok']:
                continue
            item = (key, draw_index, result, checked)
            accepted.append(item)
            if first_diverse is None and structurally_diverse_S4(
                    result['plan'], result['expectation']):
                first_diverse = item
    uncovered = set(COVER_UNIVERSE)
    selected = []
    for item in accepted:
        elements = coverage_elements(item[2])
        if elements & uncovered:
            selected.append(item)
            uncovered -= elements
            if not uncovered:
                break
    if uncovered:
        raise RuntimeError('L2_FROZEN_SCAN_COVERAGE_BLOCKER')
    if first_diverse is not None:
        marker = (first_diverse[0], first_diverse[1])
        if all((item[0], item[1]) != marker for item in selected):
            selected.append(first_diverse)
    rows = []
    results_by_name = {}
    for index, (key, draw_index, result, checked) in enumerate(selected):
        name = 'l2_gate_{:02d}'.format(index)
        rows.append(selected_row_record(name, key, draw_index, result, checked))
        results_by_name[name] = result
    return rows, results_by_name


def build_code_gate_document(rows, results_by_name):
    return {
        'annex_sha256': ANNEX_SHA256,
        'coverage': coverage_payload(rows, results_by_name),
        'fixture_key_hex': fixture_key_hex_list(),
        'scan_draw_index_start': SCAN_DRAW_INDEX_START,
        'scan_draw_index_stop_exclusive': SCAN_DRAW_INDEX_STOP_EXCLUSIVE,
        'schema': CODE_GATE_SCHEMA,
        'selected_rows': rows,
    }


def canonical_json_bytes(obj):
    text = json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True)
    return (text + '\n').encode('ascii')


def load_mutated_generator(replacements, name):
    source = GEN_PATH.read_text(encoding='ascii')
    for old, new in replacements:
        if old not in source:
            raise AssertionError('missing mutation needle: ' + old)
        source = source.replace(old, new, 1)
    module = types.ModuleType(name)
    exec(source, module.__dict__)
    return module


def first_stream_word(root_key, draw_index):
    message = (
        L2_PRF_DOMAIN + L2_PRF_SEPARATOR
        + draw_index.to_bytes(8, 'big')
        + (0).to_bytes(8, 'big')
    )
    block = hmac.new(root_key, message, hashlib.sha256).digest()
    return int.from_bytes(block[0:8], 'big')


def expected_d1_node_count(root_key, draw_index):
    band = BAND_NAMES[draw_index % 4]
    band_lo, band_hi = {name: (lo, hi) for name, lo, hi in BAND_EDGES}[band]
    width = band_hi - band_lo + 1
    return band_lo + (first_stream_word(root_key, draw_index) % width)


def assert_failure_record(test, record, subcause):
    test.assertEqual(tuple(record.keys()), L2_FAILURE_KEYS)
    test.assertIs(record['ok'], False)
    test.assertEqual(record['cause'], 'PLAN_CONSTRUCTION_FAILED')
    test.assertEqual(record['subcause'], subcause)
    test.assertEqual(record['schema'], DRAW_SCHEMA)


def run_injected_public_draw(module, root_key, draw_index, install=None):
    original_make = module.make_cursor
    captured = []

    def wrapped_make(key, index):
        cursor = original_make(key, index)
        captured.append(cursor)
        return cursor

    restore = None
    module.make_cursor = wrapped_make
    try:
        if install is not None:
            restore = install(module)
        record = module.generate_draw(root_key, draw_index)
    finally:
        if restore is not None:
            restore()
        module.make_cursor = original_make
    if len(captured) != 1:
        raise AssertionError('public generate_draw must use exactly one cursor')
    return record, captured[0]


def assert_public_failure_record(
        test, record, cursor, root_key, draw_index, subcause, target_node_count):
    test.assertEqual(tuple(record.keys()), L2_FAILURE_KEYS)
    test.assertEqual(record['schema'], DRAW_SCHEMA)
    test.assertIs(record['ok'], False)
    test.assertEqual(record['cause'], 'PLAN_CONSTRUCTION_FAILED')
    test.assertEqual(record['subcause'], subcause)
    test.assertEqual(record['draw_index'], draw_index)
    test.assertEqual(record['root_id'], hashlib.sha256(root_key).hexdigest())
    test.assertEqual(record['target_band'], BAND_NAMES[draw_index % 4])
    test.assertEqual(record['target_node_count'], target_node_count)
    test.assertIs(type(record['words_consumed']), int)
    test.assertNotIsInstance(record['words_consumed'], bool)
    test.assertGreaterEqual(record['words_consumed'], 0)
    test.assertEqual(record['words_consumed'], cursor['word_index'])
    test.assertIs(cursor['root_key'], root_key)
    test.assertEqual(cursor['draw_index'], draw_index)


class TestL2APISchema(unittest.TestCase):
    def test_argument_validation(self):
        with self.assertRaises(ValueError):
            generate_draw(bytearray(32), 0)
        with self.assertRaises(ValueError):
            generate_draw(b'\x00' * 31, 0)
        with self.assertRaises(ValueError):
            generate_draw(FIXTURE_KEY_0, True)
        with self.assertRaises(ValueError):
            generate_draw(FIXTURE_KEY_0, -1)
        with self.assertRaises(ValueError):
            generate_draw(FIXTURE_KEY_0, WORD_MODULUS)

    def test_success_and_failure_key_tuples(self):
        result = generate_draw(FIXTURE_KEY_0, 0)
        self.assertEqual(tuple(result.keys()), L2_SUCCESS_KEYS)
        self.assertIs(result['ok'], True)
        self.assertIsNone(result['cause'])
        self.assertEqual(result['schema'], DRAW_SCHEMA)
        self.assertEqual(result['draw_index'], 0)
        self.assertEqual(L2_SCAFFOLDS, ('A', 'B', 'C'))
        self.assertEqual(
            L2_CONSTRUCTION_SUBCAUSES,
            (
                'PRF_RANGE_REFUSED',
                'PRF_REJECTION_BUDGET_EXCEEDED',
                'TARGET_SIZE_UNREACHABLE',
                'FORMULA_BOUND_UNSATISFIABLE',
                'ATOM_COVERAGE_UNSATISFIABLE',
                'NONVACUITY_GUARD_VIOLATED',
                'SIZE_CONSERVATION_VIOLATED',
                'EXPECTATION_DISAGREEMENT',
                'RECURSION_BOUND_EXCEEDED',
                'WORK_BOUND_EXCEEDED',
            ),
        )
        self.assertEqual(CURSOR_KEYS, (
            'root_key', 'draw_index', 'word_index', 'rejections',
            'decision_calls', 'max_frames',
        ))
        cursor = make_cursor(FIXTURE_KEY_0, 1)
        self.assertEqual(tuple(cursor.keys()), CURSOR_KEYS)

    def test_first_word_binds_target_node_count(self):
        for draw_index in range(8):
            result = generate_draw(FIXTURE_KEY_0, draw_index)
            band = ('S1', 'S2', 'S3', 'S4')[draw_index % 4]
            self.assertEqual(result['target_band'], band)
            width = {'S1': 4, 'S2': 6, 'S3': 8, 'S4': 12}[band]
            lo = {'S1': 8, 'S2': 12, 'S3': 18, 'S4': 26}[band]
            word = first_stream_word(FIXTURE_KEY_0, draw_index)
            self.assertEqual(result['target_node_count'], lo + (word % width))


class TestL2PRF(unittest.TestCase):
    def test_domain_length_and_raw_key(self):
        self.assertEqual(L2_PRF_DOMAIN, b'philosophia.stageb-dev.v1')
        self.assertEqual(len(L2_PRF_DOMAIN), 25)
        self.assertEqual(L2_PRF_SEPARATOR, b'\x00')
        self.assertEqual(WORDS_PER_BLOCK, 4)
        self.assertEqual(PRF_MAX_REJECTIONS_PER_CALL, 64)
        cursor = make_cursor(FIXTURE_KEY_0, 7)
        self.assertEqual(next_word(cursor), first_stream_word(FIXTURE_KEY_0, 7))
        self.assertEqual(cursor['word_index'], 1)

    def test_singleton_consumes_one_word(self):
        cursor = make_cursor(FIXTURE_KEY_1, 3)
        value = randbelow(cursor, 1)
        self.assertEqual(value, 0)
        self.assertEqual(cursor['word_index'], 1)

    def test_randbelow_from_words_core(self):
        n = 10
        limit = (WORD_MODULUS // n) * n
        accepted = _randbelow_from_words(iter([limit - 1]), n)
        self.assertEqual(accepted[0], (limit - 1) % n)
        self.assertEqual(accepted[1], 1)
        self.assertEqual(accepted[2], 0)
        skipped = _randbelow_from_words(iter([limit, WORD_MODULUS - 1, 3]), n)
        self.assertEqual(skipped[0], 3 % n)
        self.assertEqual(skipped[1], 3)
        self.assertEqual(skipped[2], 2)
        refused = _randbelow_from_words(iter([limit]), n, budget=0)
        self.assertTrue(_is_refuse(refused))
        self.assertEqual(refused[1], 'PRF_REJECTION_BUDGET_EXCEEDED')
        ranged = _randbelow_from_words(iter([0]), 0)
        self.assertTrue(_is_refuse(ranged))
        self.assertEqual(ranged[1], 'PRF_RANGE_REFUSED')
        huge = _randbelow_from_words(iter([0]), WORD_MODULUS + 1)
        self.assertTrue(_is_refuse(huge))
        self.assertEqual(huge[1], 'PRF_RANGE_REFUSED')
        self.assertTrue(_is_refuse(randbelow(make_cursor(FIXTURE_KEY_0, 0), True)))


class TestL2Triples(unittest.TestCase):
    def test_direct_enumeration_matches_oracle(self):
        total = 0
        for size in range(34):
            triples = TRIPLES(size)
            count = len(triples)
            total += count
            self.assertEqual(count, TRIPLE_COUNTS[size])
            self.assertEqual(triples, tuple(sorted(triples)))
            for left, mid, right in triples:
                self.assertEqual(left + mid + right, size)
                self.assertTrue(0 <= left <= CHAIN_LEN_CAP)
                self.assertTrue(0 <= mid <= CHAIN_LEN_CAP)
                self.assertTrue(0 <= right <= CHAIN_LEN_CAP)
            closed = math.comb(size + 2, 2)
            if size - 10 >= 2:
                closed -= 3 * math.comb(size - 10, 2)
            if size - 22 >= 2:
                closed += 3 * math.comb(size - 22, 2)
            if size < 2:
                closed = 1 if size == 0 else 3
            self.assertEqual(count, closed)
            self.assertEqual(count, len(TRIPLES(33 - size)))
        self.assertEqual(total, 12 ** 3)
        self.assertEqual(total, 1728)
        self.assertEqual(TRIPLES(2)[:5], (
            (0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0),
        ))
        self.assertEqual(TRIPLES(34), ())
        self.assertEqual(TRIPLES(-1), ())

    def test_colex_and_lehmer_are_deterministic(self):
        self.assertEqual(colex_unrank(5, 3, 0), (0, 1, 2))
        self.assertEqual(lehmer_decode(3, 0), (0, 1, 2))
        seen = set()
        for rank in range(math.comb(6, 2)):
            seen.add(colex_unrank(6, 2, rank))
        self.assertEqual(len(seen), math.comb(6, 2))


class TestL2Conservation(unittest.TestCase):
    def test_key4_draw_0_to_63(self):
        bands = []
        seen = []
        for draw_index in range(64):
            result = generate_draw(FIXTURE_KEY_4, draw_index)
            seen.append(draw_index)
            if not result['ok']:
                self.assertEqual(tuple(result.keys()), L2_FAILURE_KEYS)
                bands.append(result['target_band'])
                continue
            self.assertEqual(tuple(result.keys()), L2_SUCCESS_KEYS)
            expectation = result['expectation']
            self.assertEqual(expectation['node_count'], result['target_node_count'])
            self.assertEqual(expectation['band'], result['target_band'])
            self.assertEqual(
                result['target_band'],
                ('S1', 'S2', 'S3', 'S4')[draw_index % 4],
            )
            bands.append(result['target_band'])
            checked = check_plan(result['plan'], result['expectation'])
            self.assertTrue(checked['ok'])
            self.assertTrue(independent_nonvacuity(result['plan']))
            self.assertTrue(walk_container_ids(result['plan'], set()))
            self.assertEqual(
                result['words_consumed'],
                closed_form_words(result['plan'], expectation),
            )
            self.assertEqual(
                summarize_plan(result['plan']['proof'])['count'],
                expectation['node_count'],
            )
        self.assertEqual(seen, list(range(64)))
        self.assertEqual(len(seen), len(set(seen)))
        self.assertEqual(bands.count('S1'), 16)
        self.assertEqual(bands.count('S2'), 16)
        self.assertEqual(bands.count('S3'), 16)
        self.assertEqual(bands.count('S4'), 16)


class TestL2NonvacuityIndependent(unittest.TestCase):
    def test_independent_sat_on_sample_draws(self):
        for key in FIXTURE_KEYS:
            for draw_index in range(8):
                result = generate_draw(key, draw_index)
                if not result['ok']:
                    continue
                self.assertTrue(independent_nonvacuity(result['plan']))
                self.assertNotIn('eval_formula', independent_nonvacuity.__code__.co_names)


class TestL2AliasingAndExpectation(unittest.TestCase):
    def test_no_aliasing_and_canonical_stability(self):
        result = generate_draw(FIXTURE_KEY_2, 5)
        self.assertTrue(result['ok'])
        self.assertTrue(walk_container_ids(result['plan'], set()))
        first = canonical_bytes(result)
        second = canonical_bytes(result)
        self.assertEqual(first, second)
        again = generate_draw(FIXTURE_KEY_2, 5)
        self.assertEqual(canonical_bytes(again), first)

    def test_size_and_band_and_family_and_depth(self):
        result = generate_draw(FIXTURE_KEY_3, 11)
        self.assertTrue(result['ok'])
        expectation = result['expectation']
        self.assertIs(type(expectation['node_count']), int)
        self.assertIs(type(expectation['max_dependency_depth']), int)
        self.assertNotIsInstance(expectation['node_count'], bool)
        self.assertGreaterEqual(expectation['max_dependency_depth'], 2)
        self.assertGreaterEqual(len(expectation['families']), 3)
        self.assertEqual(
            expectation['families'],
            [family for family in FAMILY_ORDER if family in expectation['families']],
        )
        checked = check_plan(result['plan'], expectation)
        self.assertTrue(checked['ok'])


class TestL2Mutations(unittest.TestCase):
    def _reference(self):
        return canonical_bytes(generate_draw(FIXTURE_KEY_0, 0))

    def test_prf_and_schedule_mutations_change_output(self):
        references = [
            canonical_bytes(generate_draw(FIXTURE_KEY_0, draw_index))
            for draw_index in range(8)
        ]
        mutations = [
            (("L2_PRF_DOMAIN = b'philosophia.stageb-dev.v1'",
              "L2_PRF_DOMAIN = b'philosophia.stageb-dev.v2'"),),
            (("L2_PRF_DOMAIN = b'philosophia.stageb-dev.v1'",
              "L2_PRF_DOMAIN = b'philosophia.stageb-dev.v'"),),
            (("L2_PRF_SEPARATOR = b'\\x00'",
              "L2_PRF_SEPARATOR = b''"),),
            (("hmac.new(root_key, message, hashlib.sha256).digest()",
              "hmac.new(hashlib.sha256(root_key).hexdigest().encode('ascii'), message, hashlib.sha256).digest()"),),
            (("        + draw_index.to_bytes(8, 'big')\n"
              "        + block_index.to_bytes(8, 'big')",
              "        + block_index.to_bytes(8, 'big')\n"
              "        + draw_index.to_bytes(8, 'big')"),),
            (("draw_index.to_bytes(8, 'big')",
              "draw_index.to_bytes(8, 'little')"),
             ("block_index.to_bytes(8, 'big')",
              "block_index.to_bytes(8, 'little')")),
            (("draw_index.to_bytes(8, 'big')",
              "draw_index.to_bytes(4, 'big')"),
             ("block_index.to_bytes(8, 'big')",
              "block_index.to_bytes(4, 'big')")),
            (("block_index = w_index // WORDS_PER_BLOCK",
              "block_index = 10 ** 9 - (w_index // WORDS_PER_BLOCK)"),),
            (("block[8 * offset:8 * offset + 8]",
              "block[4 * offset:4 * offset + 8]"),),
            (("int.from_bytes(block[8 * offset:8 * offset + 8], 'big')",
              "int.from_bytes(block[8 * offset:8 * offset + 8], 'little')"),),
            (("L2_SCAFFOLDS = ('A', 'B', 'C')",
              "L2_SCAFFOLDS = ('B', 'A', 'C')"),),
            (("for z_name in zs:",
              "for z_name in zs[::-1]:"),),
            (("t_atoms.append(remaining.pop(idx))",
              "t_atoms.insert(0, remaining.pop(idx))"),),
        ]
        for index, replacements in enumerate(mutations):
            mutated = load_mutated_generator(replacements, 'mut_prf_{}'.format(index))
            outputs = [
                canonical_bytes(mutated.generate_draw(FIXTURE_KEY_0, draw_index))
                for draw_index in range(8)
            ]
            self.assertNotEqual(
                outputs, references, msg='mutation {}'.format(index))

    def test_d13_padding_order_reversed_changes_frozen_output(self):
        mutated = load_mutated_generator(
            (("for z_name in zs:",
              "for z_name in zs[::-1]:"),),
            'mut_d13_padding',
        )
        changed = False
        for row in CODE_GATE_LITERAL_ROWS:
            result = mutated.generate_draw(
                bytes.fromhex(row['key_hex']), row['draw_index'])
            if canonical_hash(result) != row['canonical_result_sha256']:
                changed = True
                break
        self.assertTrue(
            changed,
            'D13 padding-order reversal must change at least one frozen output',
        )

    def test_plain_modulo_and_reuse_on_word_core(self):
        n = 10
        limit = (WORD_MODULUS // n) * n
        modulo = load_mutated_generator(
            (("if w < limit:\n            return (w % n, consumed, rejected)",
              "return (w % n, consumed, rejected)\n        if w < limit:\n            return (w % n, consumed, rejected)"),),
            'mut_modulo',
        )
        reused = load_mutated_generator(
            (("if rejected > budget:\n            return _refuse('PRF_REJECTION_BUDGET_EXCEEDED')",
              "return (w % n, consumed, rejected)\n        if rejected > budget:\n            return _refuse('PRF_REJECTION_BUDGET_EXCEEDED')"),),
            'mut_reuse',
        )
        words = [limit, 3]
        production = _randbelow_from_words(iter(words), n)
        self.assertEqual(production[0], 3 % n)
        self.assertEqual(modulo._randbelow_from_words(iter(words), n)[0], limit % n)
        self.assertEqual(reused._randbelow_from_words(iter(words), n)[0], limit % n)

    def test_singleton_skip_mutation(self):
        mutated = load_mutated_generator(
            (("cursor['decision_calls'] += 1\n"
              "    if cursor['decision_calls'] > MAX_DECISION_CALLS:\n"
              "        return _refuse('WORK_BOUND_EXCEEDED')\n"
              "    budget = PRF_MAX_REJECTIONS_PER_CALL",
              "cursor['decision_calls'] += 1\n"
              "    if n == 1:\n"
              "        return 0\n"
              "    if cursor['decision_calls'] > MAX_DECISION_CALLS:\n"
              "        return _refuse('WORK_BOUND_EXCEEDED')\n"
              "    budget = PRF_MAX_REJECTIONS_PER_CALL"),),
            'mut_singleton',
        )
        cursor = mutated.make_cursor(FIXTURE_KEY_0, 0)
        self.assertEqual(mutated.randbelow(cursor, 1), 0)
        self.assertEqual(cursor['word_index'], 0)
        live = make_cursor(FIXTURE_KEY_0, 0)
        randbelow(live, 1)
        self.assertEqual(live['word_index'], 1)

    def test_decision_order_mutations_change_output(self):
        reference = canonical_bytes(generate_draw(FIXTURE_KEY_0, 0))
        d1_after_d2 = load_mutated_generator(
            (("n_off = randbelow(cursor, band_hi - band_lo + 1)\n"
              "    if _is_refuse(n_off):\n"
              "        return n_off\n"
              "    target_n = band_lo + n_off\n"
              "\n"
              "    def refuse(subcause):\n"
              "        return (_REFUSE_MARK, subcause, target_n)\n"
              "\n"
              "    sc_idx = randbelow(cursor, len(L2_SCAFFOLDS))\n"
              "    if _is_refuse(sc_idx):\n"
              "        return (_REFUSE_MARK, sc_idx[1], target_n)\n"
              "    scaffold = L2_SCAFFOLDS[sc_idx]",
              "sc_idx = randbelow(cursor, len(L2_SCAFFOLDS))\n"
              "    if _is_refuse(sc_idx):\n"
              "        return sc_idx\n"
              "    scaffold = L2_SCAFFOLDS[sc_idx]\n"
              "    n_off = randbelow(cursor, band_hi - band_lo + 1)\n"
              "    if _is_refuse(n_off):\n"
              "        return n_off\n"
              "    target_n = band_lo + n_off\n"
              "\n"
              "    def refuse(subcause):\n"
              "        return (_REFUSE_MARK, subcause, target_n)"),),
            'mut_d1d2',
        )
        self.assertNotEqual(
            canonical_bytes(d1_after_d2.generate_draw(FIXTURE_KEY_0, 0)),
            reference,
        )
        swapped_fields = load_mutated_generator(
            (("field1 = sample_positive(cursor, first_cover, n_max1, names)\n"
              "    if _is_refuse(field1):\n"
              "        return (_REFUSE_MARK, field1[1], target_n)\n"
              "    n1 = formula_leaf_count(field1)\n"
              "    n_max2 = _n_max_field2(scaffold, n1)\n"
              "    field2 = sample_positive(cursor, second_cover, n_max2, names)",
              "field2 = sample_positive(cursor, second_cover, n_max1, names)\n"
              "    if _is_refuse(field2):\n"
              "        return (_REFUSE_MARK, field2[1], target_n)\n"
              "    n1 = formula_leaf_count(field2)\n"
              "    n_max2 = _n_max_field2(scaffold, n1)\n"
              "    field1 = sample_positive(cursor, first_cover, n_max2, names)"),),
            'mut_d6d7',
        )
        self.assertNotEqual(
            canonical_bytes(swapped_fields.generate_draw(FIXTURE_KEY_0, 0)),
            reference,
        )

    def test_chain_cap_and_false_sampler_assertions(self):
        mutated_cap = load_mutated_generator(
            (('CHAIN_LEN_CAP = 11', 'CHAIN_LEN_CAP = 12'),),
            'mut_cap',
        )
        padding = tuple('a0' for _ in range(12))
        cursor = mutated_cap.make_cursor(FIXTURE_KEY_0, 0)
        packed = mutated_cap.build_chain('a1', padding, 'AND_ELIM_LEFT', 'h1', cursor)
        self.assertFalse(_is_refuse(packed))
        hyp_formula, _node = packed
        self.assertGreater(formula_node_count(hyp_formula), MAX_FORMULA_NODES)
        mutated_false = load_mutated_generator(
            (("if len(labels) == 1:\n            return _atom(labels[0])",
              "if len(labels) == 1:\n            return {'kind': 'FALSE'}"),),
            'mut_false',
        )
        cursor = mutated_false.make_cursor(FIXTURE_KEY_0, 1)
        formula = mutated_false.sample_positive(cursor, ('a0',), 1)
        self.assertEqual(formula['kind'], 'FALSE')
        plan = {
            'atoms': ['a0', 'a1', 'a2'],
            'hypotheses': [{'id': 'h0', 'formula': formula}],
            'goal': _atom('a1'),
            'proof': {'kind': 'AND_INTRO', 'left': None, 'right': None},
        }
        self.assertFalse(exhaustive_globals_satisfiable(plan))

    def test_per_chain_direction_duplicate_globals(self):
        # L_i = L_j = 1, T_i = Z_j = a0, Z_i = T_j = a1.
        cursor_left = make_cursor(FIXTURE_KEY_0, 0)
        packed_left = build_chain(
            'a0', ('a1',), 'AND_ELIM_LEFT', 'h1', cursor_left)
        cursor_right = make_cursor(FIXTURE_KEY_0, 1)
        packed_right = build_chain(
            'a1', ('a0',), 'AND_ELIM_RIGHT', 'h2', cursor_right)
        self.assertFalse(_is_refuse(packed_left))
        self.assertFalse(_is_refuse(packed_right))
        hyp_left, _node_left = packed_left
        hyp_right, _node_right = packed_right
        self.assertIsNot(hyp_left, hyp_right)
        self.assertEqual(canonical_bytes(hyp_left), canonical_bytes(hyp_right))
        cursor_same = make_cursor(FIXTURE_KEY_0, 2)
        packed_same = build_chain(
            'a1', ('a0',), 'AND_ELIM_LEFT', 'h3', cursor_same)
        self.assertFalse(_is_refuse(packed_same))
        hyp_same, _node_same = packed_same
        self.assertNotEqual(canonical_bytes(hyp_left), canonical_bytes(hyp_same))


class TestL2SubcauseInjection(unittest.TestCase):
    def test_each_subcause_via_internal_boundary(self):
        # No draw index is known to reach any subcause. Section 9 proves nine of
        # the ten cannot fire. PRF_REJECTION_BUDGET_EXCEEDED carries no
        # unreachability proof.
        cursor = make_cursor(FIXTURE_KEY_0, 0)
        ranged = randbelow(cursor, 0)
        self.assertTrue(_is_refuse(ranged))
        self.assertEqual(ranged[1], 'PRF_RANGE_REFUSED')
        huge = randbelow(make_cursor(FIXTURE_KEY_0, 0), WORD_MODULUS + 1)
        self.assertEqual(huge[1], 'PRF_RANGE_REFUSED')

        mutated_budget = load_mutated_generator(
            (('PRF_MAX_REJECTIONS_PER_CALL = 64',
              'PRF_MAX_REJECTIONS_PER_CALL = 0'),),
            'mut_budget',
        )
        n = 10
        limit = (WORD_MODULUS // n) * n
        refused = mutated_budget._randbelow_from_words(iter([limit]), n, budget=0)
        self.assertEqual(refused[1], 'PRF_REJECTION_BUDGET_EXCEEDED')

        empty_triples = load_mutated_generator(
            (('def TRIPLES(S):\n    if type(S) is not int:\n        return ()\n    out = []',
              'def TRIPLES(S):\n    if type(S) is not int:\n        return ()\n    return ()\n    out = []'),),
            'mut_triples',
        )
        record, cursor = run_injected_public_draw(
            empty_triples, FIXTURE_KEY_0, 0)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, 0,
            'TARGET_SIZE_UNREACHABLE',
            expected_d1_node_count(FIXTURE_KEY_0, 0),
        )

        cursor = make_cursor(FIXTURE_KEY_0, 0)
        ceiling = sample_positive(cursor, ('a0',), -1)
        self.assertEqual(ceiling[1], 'FORMULA_BOUND_UNSATISFIABLE')

        cursor = make_cursor(FIXTURE_KEY_0, 0)
        coverage = sample_positive(cursor, ('zzz',), 3, declared_names=('a0', 'a1', 'a2'))
        self.assertEqual(coverage[1], 'ATOM_COVERAGE_UNSATISFIABLE')

        live = generate_draw(FIXTURE_KEY_0, 0)
        false_plan = deepcopy(live['plan'])
        false_plan['hypotheses'][0]['formula'] = _false()
        nv_false = _nonvacuity(false_plan, {name: True for name in false_plan['atoms']})
        self.assertEqual(nv_false[1], 'NONVACUITY_GUARD_VIOLATED')
        goal_plan = deepcopy(live['plan'])
        goal_plan['hypotheses'][0]['formula'] = deepcopy(goal_plan['goal'])
        nv_goal = _nonvacuity(goal_plan, {name: True for name in goal_plan['atoms']})
        self.assertEqual(nv_goal[1], 'NONVACUITY_GUARD_VIOLATED')

        import phase2_stageb_generator as gen_mod
        original_summarize = gen_mod.summarize_plan

        def install_size(module):
            def size_perturbed(proof):
                summary = original_summarize(proof)
                summary['count'] = summary['count'] + 1
                return summary
            module.summarize_plan = size_perturbed
            return lambda: setattr(module, 'summarize_plan', original_summarize)

        record, cursor = run_injected_public_draw(
            gen_mod, FIXTURE_KEY_0, 0, install_size)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, 0,
            'SIZE_CONSERVATION_VIOLATED',
            expected_d1_node_count(FIXTURE_KEY_0, 0),
        )

        def install_depth(module):
            def depth_perturbed(proof):
                summary = original_summarize(proof)
                summary['depth'] = summary['depth'] + 1
                return summary
            module.summarize_plan = depth_perturbed
            return lambda: setattr(module, 'summarize_plan', original_summarize)

        record, cursor = run_injected_public_draw(
            gen_mod, FIXTURE_KEY_0, 0, install_depth)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, 0,
            'EXPECTATION_DISAGREEMENT',
            expected_d1_node_count(FIXTURE_KEY_0, 0),
        )

        def install_work(module):
            current_make = module.make_cursor

            def loaded(root_key, draw_index):
                cursor = current_make(root_key, draw_index)
                cursor['decision_calls'] = MAX_DECISION_CALLS - 1
                return cursor

            module.make_cursor = loaded
            return lambda: setattr(module, 'make_cursor', current_make)

        record, cursor = run_injected_public_draw(
            gen_mod, FIXTURE_KEY_0, 0, install_work)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, 0,
            'WORK_BOUND_EXCEEDED',
            expected_d1_node_count(FIXTURE_KEY_0, 0),
        )
        self.assertEqual(cursor['decision_calls'], MAX_DECISION_CALLS + 1)

        def install_frames(module):
            current_make = module.make_cursor

            def loaded(root_key, draw_index):
                cursor = current_make(root_key, draw_index)
                cursor['max_frames'] = MAX_FORMULA_RECURSION_FRAMES
                return cursor

            module.make_cursor = loaded
            return lambda: setattr(module, 'make_cursor', current_make)

        record, cursor = run_injected_public_draw(
            gen_mod, FIXTURE_KEY_0, 0, install_frames)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, 0,
            'RECURSION_BOUND_EXCEEDED',
            expected_d1_node_count(FIXTURE_KEY_0, 0),
        )

        self.assertEqual(len(L2_CONSTRUCTION_SUBCAUSES), 10)


class TestL2PublicFailureRecords(unittest.TestCase):
    def test_public_prf_range_refused(self):
        import phase2_stageb_generator as gen_mod
        state = {'calls': 0}

        def install(module):
            original = module.randbelow

            def wrapped(cursor, n):
                state['calls'] += 1
                if state['calls'] == 2:
                    return original(cursor, 0)
                return original(cursor, n)

            module.randbelow = wrapped
            return lambda: setattr(module, 'randbelow', original)

        record, cursor = run_injected_public_draw(
            gen_mod, FIXTURE_KEY_0, 0, install)
        self.assertEqual(state['calls'], 2)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, 0,
            'PRF_RANGE_REFUSED',
            expected_d1_node_count(FIXTURE_KEY_0, 0),
        )

    def test_public_prf_rejection_budget_exceeded(self):
        import phase2_stageb_generator as gen_mod
        draw_index = 1
        width = 6
        limit = (WORD_MODULUS // width) * width

        def install(module):
            original_budget = module.PRF_MAX_REJECTIONS_PER_CALL
            original_next = module.next_word
            module.PRF_MAX_REJECTIONS_PER_CALL = 0

            def wrapped_next(cursor):
                original_next(cursor)
                return limit

            module.next_word = wrapped_next

            def restore():
                module.PRF_MAX_REJECTIONS_PER_CALL = original_budget
                module.next_word = original_next

            return restore

        record, cursor = run_injected_public_draw(
            gen_mod, FIXTURE_KEY_0, draw_index, install)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, draw_index,
            'PRF_REJECTION_BUDGET_EXCEEDED', None)

    def test_public_formula_bound_unsatisfiable(self):
        import phase2_stageb_generator as gen_mod

        def install(module):
            original = module._n_max_field1
            module._n_max_field1 = lambda scaffold, k, m1: -1
            return lambda: setattr(module, '_n_max_field1', original)

        record, cursor = run_injected_public_draw(
            gen_mod, FIXTURE_KEY_0, 0, install)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, 0,
            'FORMULA_BOUND_UNSATISFIABLE',
            expected_d1_node_count(FIXTURE_KEY_0, 0),
        )

    def test_public_atom_coverage_unsatisfiable(self):
        import phase2_stageb_generator as gen_mod

        def install(module):
            original = module.sample_positive
            state = {'first': True}

            def wrapped(cursor, cover, n_max, declared_names=None):
                if state['first']:
                    state['first'] = False
                    poisoned = ('zzz',) + tuple(cover[1:])
                    if len(poisoned) != len(cover):
                        raise AssertionError('cover arity must be unchanged')
                    return original(cursor, poisoned, n_max, declared_names)
                return original(cursor, cover, n_max, declared_names)

            module.sample_positive = wrapped
            return lambda: setattr(module, 'sample_positive', original)

        record, cursor = run_injected_public_draw(
            gen_mod, FIXTURE_KEY_0, 0, install)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, 0,
            'ATOM_COVERAGE_UNSATISFIABLE',
            expected_d1_node_count(FIXTURE_KEY_0, 0),
        )

    def test_public_nonvacuity_guard_violated(self):
        import phase2_stageb_generator as gen_mod

        def install(module):
            original = module._nonvacuity

            def wrapped(plan, nu):
                perturbed = deepcopy(plan)
                perturbed['hypotheses'][0]['formula'] = _false()
                return original(perturbed, nu)

            module._nonvacuity = wrapped
            return lambda: setattr(module, '_nonvacuity', original)

        record, cursor = run_injected_public_draw(
            gen_mod, FIXTURE_KEY_0, 0, install)
        assert_public_failure_record(
            self, record, cursor, FIXTURE_KEY_0, 0,
            'NONVACUITY_GUARD_VIOLATED',
            expected_d1_node_count(FIXTURE_KEY_0, 0),
        )


class TestL2ImportGraphAndKeys(unittest.TestCase):
    def test_production_import_allowlist(self):
        source = GEN_PATH.read_text(encoding='ascii')
        tree = ast.parse(source)
        imported = set()
        math_attrs = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imported.add(node.module.split('.')[0])
            elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                if node.value.id == 'math':
                    math_attrs.add(node.attr)
        self.assertTrue(imported <= ALLOWED_IMPORTS)
        self.assertTrue(imported.isdisjoint(FORBIDDEN_IMPORTS))
        self.assertTrue(math_attrs <= {'comb', 'factorial'})
        for needle in FORBIDDEN_SUBSTRINGS:
            self.assertNotIn(needle, source)

    def test_fixture_keys_are_the_only_keys(self):
        self.assertEqual(FIXTURE_KEY_0, bytes.fromhex('00' * 32))
        self.assertEqual(FIXTURE_KEY_1, bytes.fromhex('ff' * 32))
        self.assertEqual(FIXTURE_KEY_2, bytes.fromhex('55' * 32))
        self.assertEqual(FIXTURE_KEY_3, bytes.fromhex('aa' * 32))
        self.assertEqual(
            FIXTURE_KEY_4,
            bytes.fromhex(
                '000102030405060708090a0b0c0d0e0f'
                '101112131415161718191a1b1c1d1e1f'
            ),
        )
        joined = GEN_PATH.read_text(encoding='ascii') + TEST_PATH.read_text(encoding='ascii')
        banned = (
            'sec' + 'rets',
            'os.urand' + 'om',
            'root-regist' + 'ration',
            'hk' + 'df',
            'derive_' + 'key',
        )
        for needle in banned:
            self.assertNotIn(needle, joined)
        self.assertFalse(select_l2_code_gate_rows.__name__.startswith('test_'))


class TestL2FreshProcessDeterminism(unittest.TestCase):
    def test_hash_stable_across_hashseeds(self):
        self.assertEqual(len(CODE_GATE_LITERAL_ROWS), 6)
        for row in CODE_GATE_LITERAL_ROWS:
            snippet = (
                "import sys; sys.path.insert(0, %r); "
                "from phase2_stageb_generator import generate_draw; "
                "from phase2_stageb_canonical import canonical_bytes; "
                "import hashlib; "
                "r = generate_draw(bytes.fromhex(%r), %d); "
                "print(hashlib.sha256(canonical_bytes(r)).hexdigest())"
            ) % (str(LEARNING_DIR), row['key_hex'], row['draw_index'])
            hashes = []
            for seed in ('0', '1'):
                env = dict(os.environ)
                env['PYTHONHASHSEED'] = seed
                proc = subprocess.run(
                    [sys.executable, '-c', snippet],
                    env=env,
                    check=True,
                    capture_output=True,
                    text=True,
                )
                hashes.append(proc.stdout.strip())
            self.assertEqual(hashes[0], hashes[1], msg=row['fixture_name'])
            self.assertEqual(
                hashes[0],
                row['canonical_result_sha256'],
                msg=row['fixture_name'],
            )
            self.assertEqual(len(hashes[0]), 64)


class TestL2RejectionWordAccount(unittest.TestCase):
    def test_selected_rows_account_for_rejection_words(self):
        self.assertEqual(len(CODE_GATE_LITERAL_ROWS), 6)
        for row in CODE_GATE_LITERAL_ROWS:
            root_key = bytes.fromhex(row['key_hex'])
            result, cursor = generate_draw_with_captured_cursor(
                root_key, row['draw_index'])
            self.assertIs(cursor['root_key'], root_key)
            self.assertEqual(cursor['draw_index'], row['draw_index'])
            self.assertEqual(tuple(cursor.keys()), CURSOR_KEYS)
            self.assertTrue(result['ok'])
            self.assertEqual(cursor['word_index'], result['words_consumed'])
            self.assertIs(type(cursor['rejections']), int)
            self.assertNotIsInstance(cursor['rejections'], bool)
            self.assertGreaterEqual(cursor['rejections'], 0)
            self.assertEqual(
                result['words_consumed'],
                closed_form_words(result['plan'], result['expectation'])
                + cursor['rejections'],
            )
            self.assertEqual(canonical_hash(result), row['canonical_result_sha256'])
            self.assertEqual(result['words_consumed'], row['words_consumed'])
            self.assertEqual(canonical_hash(result['plan']), row['raw_plan_sha256'])


class TestL2CodeGateLiterals(unittest.TestCase):
    def test_frozen_rows_match_literals_without_rescan(self):
        if not CODE_GATE_LITERAL_ROWS:
            self.skipTest('code-gate literals unfilled until frozen selection')
        seen_names = []
        bands = set()
        kinds = set()
        families = set()
        scaffolds = set()
        directions = set()
        diverse = False
        for row in CODE_GATE_LITERAL_ROWS:
            seen_names.append(row['fixture_name'])
            result = generate_draw(bytes.fromhex(row['key_hex']), row['draw_index'])
            self.assertTrue(result['ok'])
            checked = check_plan(result['plan'], result['expectation'])
            self.assertTrue(checked['ok'])
            self.assertEqual(canonical_hash(result), row['canonical_result_sha256'])
            self.assertEqual(canonical_hash(result['plan']), row['raw_plan_sha256'])
            self.assertEqual(canonical_hash(checked['theorem']), row['raw_theorem_sha256'])
            self.assertEqual(result['words_consumed'], row['words_consumed'])
            self.assertEqual(result['expectation']['node_count'], row['node_count'])
            self.assertEqual(result['expectation']['band'], row['band'])
            self.assertEqual(list(result['expectation']['families']), row['families'])
            self.assertEqual(
                result['expectation']['max_dependency_depth'],
                row['max_dependency_depth'],
            )
            self.assertEqual(infer_scaffold(result['plan']), row['scaffold'])
            self.assertEqual(infer_dir(result['plan']), row['dir'])
            self.assertTrue(independent_nonvacuity(result['plan']))
            self.assertTrue(walk_container_ids(result['plan'], set()))
            bands.add(row['band'])
            kinds.update(collect_kinds(result['plan']['proof']))
            families.update(row['families'])
            scaffolds.add(row['scaffold'])
            directions.add(row['dir'])
            if structurally_diverse_S4(result['plan'], result['expectation']):
                diverse = True
        self.assertEqual(
            seen_names,
            ['l2_gate_{:02d}'.format(i) for i in range(len(seen_names))],
        )
        self.assertEqual(bands, {'S1', 'S2', 'S3', 'S4'})
        self.assertTrue(set(RULE_KIND_ORDER) <= kinds)
        self.assertEqual(set(families), set(FAMILY_ORDER))
        self.assertEqual(scaffolds, set(L2_SCAFFOLDS))
        self.assertEqual(directions, set(DIR_KINDS))
        self.assertTrue(diverse)

    def test_selection_helper_is_not_a_discovered_test(self):
        self.assertTrue(callable(select_l2_code_gate_rows))
        self.assertFalse(select_l2_code_gate_rows.__name__.startswith('test_'))


if __name__ == '__main__':
    unittest.main()
