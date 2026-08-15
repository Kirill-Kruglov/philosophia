#!/usr/bin/env python3
"""Stage-B L2 catalogue generator. No checker, renderer, Peano or search."""

from __future__ import annotations

import hashlib
import hmac
import math
from typing import Mapping

from phase2_stageb_canonical import canonical_bytes
from phase2_stageb_schema import (
    BAND_EDGES,
    BAND_NAMES,
    EXPECTATION_SCHEMA_NAME,
    FAMILY_ORDER,
    KIND_TO_FAMILY,
    MAX_FORMULA_NODES,
    PLAN_SCHEMA_NAME,
    PROOF_CHILD_FIELDS,
    band_of_node_count,
)


DRAW_SCHEMA = 'philosophia.stageb.generator-draw.v1'

L2_SUCCESS_KEYS = (
    'schema', 'ok', 'cause', 'draw_index', 'root_id', 'target_band',
    'target_node_count', 'words_consumed', 'plan', 'expectation',
)
L2_FAILURE_KEYS = (
    'schema', 'ok', 'cause', 'subcause', 'draw_index', 'root_id', 'target_band',
    'target_node_count', 'words_consumed',
)
L2_CONSTRUCTION_SUBCAUSES = (
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
)

L2_PRF_DOMAIN = b'philosophia.stageb-dev.v1'
L2_PRF_SEPARATOR = b'\x00'
ROOT_KEY_LEN = 32
WORDS_PER_BLOCK = 4
PRF_MAX_REJECTIONS_PER_CALL = 64
CHAIN_LEN_CAP = 11
MAX_FORMULA_RECURSION_FRAMES = MAX_FORMULA_NODES
MAX_DECISION_CALLS = 128
WORD_MODULUS = 2 ** 64

L2_SCAFFOLDS = ('A', 'B', 'C')
DIR_KINDS = ('AND_ELIM_LEFT', 'AND_ELIM_RIGHT')
CURSOR_KEYS = (
    'root_key', 'draw_index', 'word_index', 'rejections',
    'decision_calls', 'max_frames',
)

FIXTURE_KEY_0 = bytes.fromhex('00' * 32)
FIXTURE_KEY_1 = bytes.fromhex('ff' * 32)
FIXTURE_KEY_2 = bytes.fromhex('55' * 32)
FIXTURE_KEY_3 = bytes.fromhex('aa' * 32)
FIXTURE_KEY_4 = bytes.fromhex(
    '000102030405060708090a0b0c0d0e0f'
    '101112131415161718191a1b1c1d1e1f'
)
FIXTURE_KEYS = (
    FIXTURE_KEY_0, FIXTURE_KEY_1, FIXTURE_KEY_2, FIXTURE_KEY_3, FIXTURE_KEY_4,
)

FAM_CLOSED = {
    'A': frozenset({'AND_INTRO', 'OR_INTRO', 'OR_ELIM'}),
    'B': frozenset({'AND_INTRO', 'OR_ELIM', 'NOT_ELIM', 'EXFALSO'}),
    'C': frozenset({'AND_INTRO', 'AND_ELIM', 'NOT_INTRO', 'NOT_ELIM'}),
}

_BAND_RANGE = {name: (lo, hi) for name, lo, hi in BAND_EDGES}
_REFUSE_MARK = object()


def _refuse(subcause: str):
    return (_REFUSE_MARK, subcause)


def _is_refuse(value: object) -> bool:
    return (
        type(value) is tuple
        and len(value) in (2, 3)
        and value[0] is _REFUSE_MARK
    )


def _root_id(root_key: bytes) -> str:
    return hashlib.sha256(root_key).hexdigest()


def _failure(
        cursor: Mapping, subcause: str, draw_index: int, target_band: str,
        target_node_count,
) -> dict:
    return {
        'schema': DRAW_SCHEMA,
        'ok': False,
        'cause': 'PLAN_CONSTRUCTION_FAILED',
        'subcause': subcause,
        'draw_index': draw_index,
        'root_id': _root_id(cursor['root_key']),
        'target_band': target_band,
        'target_node_count': target_node_count,
        'words_consumed': cursor['word_index'],
    }


def make_cursor(root_key: bytes, draw_index: int) -> dict:
    return {
        'root_key': root_key,
        'draw_index': draw_index,
        'word_index': 0,
        'rejections': 0,
        'decision_calls': 0,
        'max_frames': 0,
    }


def _block(root_key, draw_index, block_index):
    message = (
        L2_PRF_DOMAIN + L2_PRF_SEPARATOR
        + draw_index.to_bytes(8, 'big')
        + block_index.to_bytes(8, 'big')
    )
    return hmac.new(root_key, message, hashlib.sha256).digest()


def next_word(cursor: dict) -> int:
    w_index = cursor['word_index']
    block_index = w_index // WORDS_PER_BLOCK
    offset = w_index % WORDS_PER_BLOCK
    block = _block(cursor['root_key'], cursor['draw_index'], block_index)
    word = int.from_bytes(block[8 * offset:8 * offset + 8], 'big')
    cursor['word_index'] = w_index + 1
    return word


def _randbelow_from_words(words, n, *, budget=PRF_MAX_REJECTIONS_PER_CALL):
    if type(n) is not int or n < 1 or n > WORD_MODULUS:
        return _refuse('PRF_RANGE_REFUSED')
    limit = (WORD_MODULUS // n) * n
    rejected = 0
    consumed = 0
    while True:
        w = next(words)
        consumed += 1
        if w < limit:
            return (w % n, consumed, rejected)
        rejected += 1
        if rejected > budget:
            return _refuse('PRF_REJECTION_BUDGET_EXCEEDED')


def randbelow(cursor: dict, n):
    cursor['decision_calls'] += 1
    if cursor['decision_calls'] > MAX_DECISION_CALLS:
        return _refuse('WORK_BOUND_EXCEEDED')
    budget = PRF_MAX_REJECTIONS_PER_CALL

    def _words():
        while True:
            yield next_word(cursor)

    outcome = _randbelow_from_words(_words(), n, budget=budget)
    if _is_refuse(outcome):
        return outcome
    value, _consumed, rejected = outcome
    cursor['rejections'] += rejected
    return value


def colex_unrank(n: int, m: int, t: int) -> tuple:
    chosen = []
    remaining = t
    for k in range(m, 0, -1):
        c = k - 1
        while math.comb(c + 1, k) <= remaining:
            c += 1
        chosen.append(c)
        remaining -= math.comb(c, k)
    chosen.reverse()
    return tuple(chosen)


def lehmer_decode(m: int, p: int) -> tuple:
    items = list(range(m))
    perm = []
    remaining = p
    for i in range(m, 0, -1):
        fact = math.factorial(i - 1)
        idx = remaining // fact
        remaining = remaining % fact
        perm.append(items.pop(idx))
    return tuple(perm)


def TRIPLES(S):
    if type(S) is not int:
        return ()
    out = []
    cap = CHAIN_LEN_CAP
    for left in range(0, cap + 1):
        for mid in range(0, cap + 1):
            right = S - left - mid
            if 0 <= right <= cap:
                out.append((left, mid, right))
    return tuple(out)


def _push_frame(cursor: dict):
    cursor['max_frames'] += 1
    if cursor['max_frames'] > MAX_FORMULA_RECURSION_FRAMES:
        return _refuse('RECURSION_BOUND_EXCEEDED')
    return None


def _pop_frame(cursor: dict) -> None:
    cursor['max_frames'] -= 1


def fresh(formula: Mapping, cursor: dict):
    pushed = _push_frame(cursor)
    if _is_refuse(pushed):
        return pushed
    kind = formula['kind']
    try:
        if kind == 'ATOM':
            return {'kind': 'ATOM', 'name': formula['name']}
        if kind == 'FALSE':
            return {'kind': 'FALSE'}
        if kind == 'NOT':
            arg = fresh(formula['arg'], cursor)
            if _is_refuse(arg):
                return arg
            return {'kind': 'NOT', 'arg': arg}
        left = fresh(formula['left'], cursor)
        if _is_refuse(left):
            return left
        right = fresh(formula['right'], cursor)
        if _is_refuse(right):
            return right
        return {'kind': kind, 'left': left, 'right': right}
    finally:
        _pop_frame(cursor)


def formula_leaf_count(formula: Mapping) -> int:
    kind = formula['kind']
    if kind == 'ATOM':
        return 1
    if kind in ('FALSE',):
        return 0
    if kind == 'NOT':
        return formula_leaf_count(formula['arg'])
    return formula_leaf_count(formula['left']) + formula_leaf_count(formula['right'])


def formula_atoms(formula: Mapping, acc: set) -> None:
    kind = formula['kind']
    if kind == 'ATOM':
        acc.add(formula['name'])
        return
    if kind == 'FALSE':
        return
    if kind == 'NOT':
        formula_atoms(formula['arg'], acc)
        return
    formula_atoms(formula['left'], acc)
    formula_atoms(formula['right'], acc)


def eval_formula(formula: Mapping, nu: Mapping) -> bool:
    kind = formula['kind']
    if kind == 'ATOM':
        return bool(nu[formula['name']])
    if kind == 'FALSE':
        return False
    if kind == 'NOT':
        return not eval_formula(formula['arg'], nu)
    if kind == 'AND':
        return eval_formula(formula['left'], nu) and eval_formula(formula['right'], nu)
    return eval_formula(formula['left'], nu) or eval_formula(formula['right'], nu)


def _atom(name: str) -> dict:
    return {'kind': 'ATOM', 'name': name}


def _false() -> dict:
    return {'kind': 'FALSE'}


def _not(arg: Mapping) -> dict:
    return {'kind': 'NOT', 'arg': arg}


def _and(left: Mapping, right: Mapping) -> dict:
    return {'kind': 'AND', 'left': left, 'right': right}


def _or(left: Mapping, right: Mapping) -> dict:
    return {'kind': 'OR', 'left': left, 'right': right}


def _assume(hid: str, conclusion: Mapping) -> dict:
    return {
        'kind': 'ASSUME',
        'hypothesis_id': hid,
        'conclusion': conclusion,
    }


def _and_intro(left: Mapping, right: Mapping, cursor: dict):
    conc_left = fresh(left['conclusion'], cursor)
    if _is_refuse(conc_left):
        return conc_left
    conc_right = fresh(right['conclusion'], cursor)
    if _is_refuse(conc_right):
        return conc_right
    return {
        'kind': 'AND_INTRO',
        'left': left,
        'right': right,
        'conclusion': _and(conc_left, conc_right),
    }


def build_shape(cursor: dict, labels: list):
    pushed = _push_frame(cursor)
    if _is_refuse(pushed):
        return pushed
    try:
        if len(labels) == 1:
            return _atom(labels[0])
        nl_off = randbelow(cursor, len(labels) - 1)
        if _is_refuse(nl_off):
            return nl_off
        nl = 1 + nl_off
        ctor = randbelow(cursor, 2)
        if _is_refuse(ctor):
            return ctor
        kind = ('AND', 'OR')[ctor]
        left = build_shape(cursor, labels[0:nl])
        if _is_refuse(left):
            return left
        right = build_shape(cursor, labels[nl:])
        if _is_refuse(right):
            return right
        return {'kind': kind, 'left': left, 'right': right}
    finally:
        _pop_frame(cursor)


def sample_positive(cursor: dict, cover: tuple, n_max: int, declared_names=None):
    if type(n_max) is not int or n_max < len(cover):
        return _refuse('FORMULA_BOUND_UNSATISFIABLE')
    m = len(cover)
    if m < 1:
        return _refuse('FORMULA_BOUND_UNSATISFIABLE')
    if declared_names is not None:
        allowed = set(declared_names)
        for name in cover:
            if name not in allowed:
                return _refuse('ATOM_COVERAGE_UNSATISFIABLE')
    extra = randbelow(cursor, n_max - m + 1)
    if _is_refuse(extra):
        return extra
    n = m + extra
    comb_n = math.comb(n, m)
    t = randbelow(cursor, comb_n)
    if _is_refuse(t):
        return t
    pos = colex_unrank(n, m, t)
    p = randbelow(cursor, math.factorial(m))
    if _is_refuse(p):
        return p
    perm = lehmer_decode(m, p)
    labels = [None] * n
    for rank in range(m):
        labels[pos[rank]] = cover[perm[rank]]
    for i in range(n):
        if labels[i] is None:
            idx = randbelow(cursor, m)
            if _is_refuse(idx):
                return idx
            labels[i] = cover[idx]
    return build_shape(cursor, labels)


def _chain_formulas(tj: str, zs: tuple, dir_kind: str) -> list:
    current = _atom(tj)
    layers = [current]
    for z_name in zs:
        atom_z = _atom(z_name)
        if dir_kind == 'AND_ELIM_LEFT':
            current = _and(current, atom_z)
        else:
            current = _and(atom_z, current)
        layers.append(current)
    return layers


def build_chain(tj: str, zs: tuple, dir_kind: str, hid: str, cursor: dict):
    layers = _chain_formulas(tj, zs, dir_kind)
    hyp_formula = fresh(layers[-1], cursor)
    if _is_refuse(hyp_formula):
        return hyp_formula
    length = len(zs)
    if length == 0:
        conclusion = fresh(layers[0], cursor)
        if _is_refuse(conclusion):
            return conclusion
        return hyp_formula, _assume(hid, conclusion)
    assume_conc = fresh(layers[length], cursor)
    if _is_refuse(assume_conc):
        return assume_conc
    node_conclusion = fresh(layers[length - 1], cursor)
    if _is_refuse(node_conclusion):
        return node_conclusion
    node = {
        'kind': dir_kind,
        'source': _assume(hid, assume_conc),
        'conclusion': node_conclusion,
    }
    for idx in range(length - 2, -1, -1):
        conc = fresh(layers[idx], cursor)
        if _is_refuse(conc):
            return conc
        node = {'kind': dir_kind, 'source': node, 'conclusion': conc}
    return hyp_formula, node


def _frame(chain0, chain1, chain2, gadget, cursor: dict):
    inner_left = _and_intro(chain0, chain1, cursor)
    if _is_refuse(inner_left):
        return inner_left
    inner_right = _and_intro(chain2, gadget, cursor)
    if _is_refuse(inner_right):
        return inner_right
    return _and_intro(inner_left, inner_right, cursor)


def closed_form_depth(scaffold: str, lengths: tuple) -> int:
    l0, l1, l2 = lengths
    g_d = 1 if scaffold == 'A' else 2

    def c_len(length):
        return length - 1

    if l0 == 0 and l1 == 0:
        d_left = 0
    else:
        d_left = 1 + max(c_len(length) for length in (l0, l1) if length >= 1)
    right_args = [g_d]
    if l2 >= 1:
        right_args.append(c_len(l2))
    d_right = 1 + max(right_args)
    return 1 + max(d_left, d_right)


def closed_form_families(scaffold: str, s_sum: int) -> list:
    family_set = set(FAM_CLOSED[scaffold])
    if s_sum >= 1:
        family_set.add('AND_ELIM')
    return [family for family in FAMILY_ORDER if family in family_set]


def summarize_plan(proof: Mapping) -> dict:
    count = 0
    depth = 0
    families = set()
    stack = [(proof, False)]
    post = []
    while stack:
        node, visited = stack.pop()
        if visited:
            post.append(node)
            continue
        stack.append((node, True))
        kind = node['kind']
        for field in reversed(PROOF_CHILD_FIELDS[kind]):
            stack.append((node[field], False))
    memo = {}
    for node in post:
        ident = id(node)
        kind = node['kind']
        if kind == 'ASSUME':
            memo[ident] = (0, 0, set())
            continue
        child_counts = []
        child_depths = []
        fams = {KIND_TO_FAMILY[kind]}
        for field in PROOF_CHILD_FIELDS[kind]:
            c_count, c_depth, c_fams = memo[id(node[field])]
            child_counts.append(c_count)
            if node[field]['kind'] != 'ASSUME':
                child_depths.append(c_depth)
            fams.update(c_fams)
        node_count = 1 + sum(child_counts)
        node_depth = 0 if not child_depths else 1 + max(child_depths)
        memo[ident] = (node_count, node_depth, fams)
    count, depth, families = memo[id(proof)]
    return {
        'count': count,
        'depth': depth,
        'families': [family for family in FAMILY_ORDER if family in families],
        'family_set': families,
    }


def _n_max_field1(scaffold: str, k: int, m1: int) -> int:
    if scaffold == 'B':
        return 12 - k + m1
    return 9 - k + m1


def _n_max_field2(scaffold: str, n1: int) -> int:
    if scaffold == 'B':
        return min(9, 12 - n1)
    return 9 - n1


def _k_range(scaffold: str) -> tuple:
    if scaffold == 'A':
        return 3, 6
    return 4, 6


def _s_range(scaffold: str, k: int) -> tuple:
    if scaffold == 'A':
        return 1, k - 1
    return 1, k - 3


def _declared_names(k: int) -> tuple:
    return tuple('a' + str(i) for i in range(k))


def _valuation(scaffold: str, a_r: tuple, atoms: tuple) -> dict:
    if scaffold == 'A':
        return {name: True for name in atoms}
    false_set = set(a_r)
    return {name: (name not in false_set) for name in atoms}


def _nonvacuity(plan: Mapping, nu: Mapping):
    goal_bytes = canonical_bytes(plan['goal'])
    for hyp in plan['hypotheses']:
        formula = hyp['formula']
        if formula['kind'] == 'FALSE':
            return _refuse('NONVACUITY_GUARD_VIOLATED')
        if not eval_formula(formula, nu):
            return _refuse('NONVACUITY_GUARD_VIOLATED')
        if canonical_bytes(formula) == goal_bytes:
            return _refuse('NONVACUITY_GUARD_VIOLATED')
    return None


def _place(formula: Mapping, cursor: dict):
    return fresh(formula, cursor)


def _gadget_A(p_f, q_f, cursor: dict):
    p = _place(p_f, cursor)
    if _is_refuse(p):
        return p
    q = _place(q_f, cursor)
    if _is_refuse(q):
        return q
    major_f = _place(_or(p_f, q_f), cursor)
    if _is_refuse(major_f):
        return major_f
    w = _place(_or(q_f, p_f), cursor)
    if _is_refuse(w):
        return w
    p_local = _place(p_f, cursor)
    if _is_refuse(p_local):
        return p_local
    q_local = _place(q_f, cursor)
    if _is_refuse(q_local):
        return q_local
    p_src = _place(p_f, cursor)
    if _is_refuse(p_src):
        return p_src
    q_src = _place(q_f, cursor)
    if _is_refuse(q_src):
        return q_src
    w_left = _place(_or(q_f, p_f), cursor)
    if _is_refuse(w_left):
        return w_left
    w_right = _place(_or(q_f, p_f), cursor)
    if _is_refuse(w_right):
        return w_right
    w_node = _place(_or(q_f, p_f), cursor)
    if _is_refuse(w_node):
        return w_node
    gadget = {
        'kind': 'OR_ELIM',
        'conclusion': w_node,
        'major': _assume('h0', major_f),
        'left_assumption': {'id': 'l0', 'formula': p_local},
        'left_branch': {
            'kind': 'OR_INTRO_RIGHT',
            'source': _assume('l0', p_src),
            'conclusion': w_left,
        },
        'right_assumption': {'id': 'l1', 'formula': q_local},
        'right_branch': {
            'kind': 'OR_INTRO_LEFT',
            'source': _assume('l1', q_src),
            'conclusion': w_right,
        },
    }
    return gadget, w, major_f


def _gadget_B(r_f, qb_f, cursor: dict):
    r_not_arg = _place(r_f, cursor)
    if _is_refuse(r_not_arg):
        return r_not_arg
    not_r = {'kind': 'NOT', 'arg': r_not_arg}
    or_f = _place(_or(r_f, qb_f), cursor)
    if _is_refuse(or_f):
        return or_f
    qb_w = _place(qb_f, cursor)
    if _is_refuse(qb_w):
        return qb_w
    r_local = _place(r_f, cursor)
    if _is_refuse(r_local):
        return r_local
    qb_local = _place(qb_f, cursor)
    if _is_refuse(qb_local):
        return qb_local
    not_r_leaf = _place(r_f, cursor)
    if _is_refuse(not_r_leaf):
        return not_r_leaf
    r_pos = _place(r_f, cursor)
    if _is_refuse(r_pos):
        return r_pos
    qb_ex = _place(qb_f, cursor)
    if _is_refuse(qb_ex):
        return qb_ex
    qb_right = _place(qb_f, cursor)
    if _is_refuse(qb_right):
        return qb_right
    qb_conc = _place(qb_f, cursor)
    if _is_refuse(qb_conc):
        return qb_conc
    gadget = {
        'kind': 'OR_ELIM',
        'conclusion': qb_conc,
        'major': _assume('h0', or_f),
        'left_assumption': {'id': 'l0', 'formula': r_local},
        'left_branch': {
            'kind': 'EXFALSO',
            'source': {
                'kind': 'NOT_ELIM',
                'negative': _assume('h1', {'kind': 'NOT', 'arg': not_r_leaf}),
                'positive': _assume('l0', r_pos),
                'conclusion': _false(),
            },
            'conclusion': qb_ex,
        },
        'right_assumption': {'id': 'l1', 'formula': qb_local},
        'right_branch': _assume('l1', qb_right),
    }
    return gadget, qb_w, or_f, not_r


def _gadget_C(r_f, v_f, dir_kind: str, cursor: dict):
    if dir_kind == 'AND_ELIM_LEFT':
        m_f = _and(r_f, v_f)
    else:
        m_f = _and(v_f, r_f)
    m_ass = _place(m_f, cursor)
    if _is_refuse(m_ass):
        return m_ass
    m_src = _place(m_f, cursor)
    if _is_refuse(m_src):
        return m_src
    r_conc = _place(r_f, cursor)
    if _is_refuse(r_conc):
        return r_conc
    w = _place(_not(m_f), cursor)
    if _is_refuse(w):
        return w
    not_r = _place(_not(r_f), cursor)
    if _is_refuse(not_r):
        return not_r
    not_r_leaf = _place(_not(r_f), cursor)
    if _is_refuse(not_r_leaf):
        return not_r_leaf
    gadget = {
        'kind': 'NOT_INTRO',
        'assumption': {'id': 'l0', 'formula': m_ass},
        'body': {
            'kind': 'NOT_ELIM',
            'negative': _assume('h0', not_r_leaf),
            'positive': {
                'kind': dir_kind,
                'source': _assume('l0', m_src),
                'conclusion': r_conc,
            },
            'conclusion': _false(),
        },
        'conclusion': w,
    }
    return gadget, w, not_r


def generate_draw(root_key: bytes, draw_index: int) -> dict:
    if type(root_key) is not bytes or len(root_key) != ROOT_KEY_LEN:
        raise ValueError('invalid root_key')
    if type(draw_index) is not int:
        raise ValueError('invalid draw_index')
    if not 0 <= draw_index < WORD_MODULUS:
        raise ValueError('invalid draw_index')
    cursor = make_cursor(root_key, draw_index)
    target_band = BAND_NAMES[draw_index % 4]
    band_lo, band_hi = _BAND_RANGE[target_band]
    target_node_count = None
    built = _generate_body(cursor, draw_index, target_band, band_lo, band_hi)
    if _is_refuse(built):
        subcause = built[1]
        if len(built) == 3:
            target_node_count = built[2]
        return _failure(
            cursor, subcause, draw_index, target_band, target_node_count)
    return built


def _generate_body(cursor, draw_index, target_band, band_lo, band_hi):
    n_off = randbelow(cursor, band_hi - band_lo + 1)
    if _is_refuse(n_off):
        return n_off
    target_n = band_lo + n_off

    def refuse(subcause):
        return (_REFUSE_MARK, subcause, target_n)

    sc_idx = randbelow(cursor, len(L2_SCAFFOLDS))
    if _is_refuse(sc_idx):
        return (_REFUSE_MARK, sc_idx[1], target_n)
    scaffold = L2_SCAFFOLDS[sc_idx]
    k_lo, k_hi = _k_range(scaffold)
    k_off = randbelow(cursor, k_hi - k_lo + 1)
    if _is_refuse(k_off):
        return (_REFUSE_MARK, k_off[1], target_n)
    k = k_lo + k_off
    names = _declared_names(k)
    s_lo, s_hi = _s_range(scaffold, k)
    s_off = randbelow(cursor, s_hi - s_lo + 1)
    if _is_refuse(s_off):
        return (_REFUSE_MARK, s_off[1], target_n)
    split_s = s_lo + s_off
    subset_idx = randbelow(cursor, math.comb(k, split_s))
    if _is_refuse(subset_idx):
        return (_REFUSE_MARK, subset_idx[1], target_n)
    subset = colex_unrank(k, split_s, subset_idx)
    first_cover = tuple(names[i] for i in subset)
    first_set = set(first_cover)
    second_cover = tuple(name for name in names if name not in first_set)
    if scaffold == 'A':
        a_chain = names
        a_r = ()
    else:
        a_chain = second_cover
        a_r = first_cover
    n_max1 = _n_max_field1(scaffold, k, len(first_cover))
    field1 = sample_positive(cursor, first_cover, n_max1, names)
    if _is_refuse(field1):
        return (_REFUSE_MARK, field1[1], target_n)
    n1 = formula_leaf_count(field1)
    n_max2 = _n_max_field2(scaffold, n1)
    field2 = sample_positive(cursor, second_cover, n_max2, names)
    if _is_refuse(field2):
        return (_REFUSE_MARK, field2[1], target_n)
    remaining = list(a_chain)
    t_atoms = []
    for bound in (len(remaining), len(remaining) - 1, len(remaining) - 2):
        idx = randbelow(cursor, bound)
        if _is_refuse(idx):
            return (_REFUSE_MARK, idx[1], target_n)
        t_atoms.append(remaining.pop(idx))
    t0, t1, t2 = t_atoms
    s_sum = target_n - 6
    triples = TRIPLES(s_sum)
    if not triples:
        return refuse('TARGET_SIZE_UNREACHABLE')
    trip_idx = randbelow(cursor, len(triples))
    if _is_refuse(trip_idx):
        return (_REFUSE_MARK, trip_idx[1], target_n)
    lengths = triples[trip_idx]
    dir_idx = randbelow(cursor, 2)
    if _is_refuse(dir_idx):
        return (_REFUSE_MARK, dir_idx[1], target_n)
    dir_kind = DIR_KINDS[dir_idx]
    padding = []
    for length in lengths:
        zs = []
        for _ in range(length):
            z_idx = randbelow(cursor, len(a_chain))
            if _is_refuse(z_idx):
                return (_REFUSE_MARK, z_idx[1], target_n)
            zs.append(a_chain[z_idx])
        padding.append(tuple(zs))
    built = _assemble(
        cursor, scaffold, names, a_r, a_chain, field1, field2,
        (t0, t1, t2), lengths, padding, dir_kind, target_n, target_band,
        draw_index,
    )
    return built


def _assemble(
        cursor, scaffold, names, a_r, a_chain, field1, field2,
        t_atoms, lengths, padding, dir_kind, target_n, target_band, draw_index,
):
    t0, t1, t2 = t_atoms
    if scaffold == 'A':
        gadget_pack = _gadget_A(field1, field2, cursor)
    elif scaffold == 'B':
        gadget_pack = _gadget_B(field1, field2, cursor)
    else:
        gadget_pack = _gadget_C(field1, field2, dir_kind, cursor)
    if _is_refuse(gadget_pack):
        return (_REFUSE_MARK, gadget_pack[1], target_n)
    if scaffold == 'A':
        gadget, w, g0 = gadget_pack
        extra_globals = [('h0', g0)]
        chain_ids = ('h1', 'h2', 'h3')
    elif scaffold == 'B':
        gadget, w, g0, not_r = gadget_pack
        extra_globals = [('h0', g0), ('h1', not_r)]
        chain_ids = ('h2', 'h3', 'h4')
    else:
        gadget, w, not_r = gadget_pack
        extra_globals = [('h0', not_r)]
        chain_ids = ('h1', 'h2', 'h3')
    chains = []
    chain_hyps = []
    for j, hid in enumerate(chain_ids):
        packed = build_chain(t_atoms[j], padding[j], dir_kind, hid, cursor)
        if _is_refuse(packed):
            return (_REFUSE_MARK, packed[1], target_n)
        hyp_f, node = packed
        chain_hyps.append((hid, hyp_f))
        chains.append(node)
    proof = _frame(chains[0], chains[1], chains[2], gadget, cursor)
    if _is_refuse(proof):
        return (_REFUSE_MARK, proof[1], target_n)
    t0f = _place(_atom(t0), cursor)
    if _is_refuse(t0f):
        return (_REFUSE_MARK, t0f[1], target_n)
    t1f = _place(_atom(t1), cursor)
    if _is_refuse(t1f):
        return (_REFUSE_MARK, t1f[1], target_n)
    t2f = _place(_atom(t2), cursor)
    if _is_refuse(t2f):
        return (_REFUSE_MARK, t2f[1], target_n)
    w_goal = _place(w, cursor)
    if _is_refuse(w_goal):
        return (_REFUSE_MARK, w_goal[1], target_n)
    goal = _and(_and(t0f, t1f), _and(t2f, w_goal))
    hypotheses = []
    for hid, formula in extra_globals + chain_hyps:
        placed = _place(formula, cursor)
        if _is_refuse(placed):
            return (_REFUSE_MARK, placed[1], target_n)
        hypotheses.append({'id': hid, 'formula': placed})
    plan = {
        'schema': PLAN_SCHEMA_NAME,
        'atoms': list(names),
        'hypotheses': hypotheses,
        'goal': goal,
        'proof': proof,
    }
    s_sum = lengths[0] + lengths[1] + lengths[2]
    closed_count = 6 + s_sum
    closed_depth = closed_form_depth(scaffold, lengths)
    closed_fams = closed_form_families(scaffold, s_sum)
    summary = summarize_plan(proof)
    if summary['count'] != target_n or closed_count != target_n:
        return (_REFUSE_MARK, 'SIZE_CONSERVATION_VIOLATED', target_n)
    if (
            summary['count'] != closed_count
            or summary['depth'] != closed_depth
            or summary['families'] != closed_fams
    ):
        return (_REFUSE_MARK, 'EXPECTATION_DISAGREEMENT', target_n)
    nu = _valuation(scaffold, a_r, names)
    nv = _nonvacuity(plan, nu)
    if _is_refuse(nv):
        return (_REFUSE_MARK, nv[1], target_n)
    expectation = {
        'schema': EXPECTATION_SCHEMA_NAME,
        'node_count': summary['count'],
        'band': band_of_node_count(summary['count']),
        'families': summary['families'],
        'max_dependency_depth': summary['depth'],
    }
    return {
        'schema': DRAW_SCHEMA,
        'ok': True,
        'cause': None,
        'draw_index': draw_index,
        'root_id': _root_id(cursor['root_key']),
        'target_band': target_band,
        'target_node_count': target_n,
        'words_consumed': cursor['word_index'],
        'plan': plan,
        'expectation': expectation,
    }


def sampler_word_count(n: int, m: int) -> int:
    return 3 + (n - m) + 2 * (n - 1)
