#!/usr/bin/env python3
"""Stage-R L3 projection-only identities. Imports only L0 modules and stdlib.

Provides exactly the three Stage-R frame-disjointness representations:
alpha-canonical theorem identity, canonical public-item bytes and canonical
rule-skeleton identity, plus an independent raw re-derivation of the theorem
from the plan's public fields.

There is no exact-plan identity, stage-6 collision seed, dev-root processing,
quota accounting, compile/replay, frame selection or execution here.
"""

from __future__ import annotations

from itertools import permutations
from typing import Iterator, Mapping, Optional, Tuple

from phase2_stageb_canonical import canonical_bytes, canonical_hash
from phase2_stageb_render import render_sequent
from phase2_stageb_schema import (
    FORMULA_KEYS,
    FORMULA_KINDS,
    HYPOTHESIS_KEYS,
    MAX_DECLARED_ATOMS,
    MIN_DECLARED_ATOMS,
    PLAN_KEYS,
    PROOF_NODE_KEYS,
    RULE_KINDS,
    THEORY_PREMISES,
    THEORY_SHA256,
    is_atom_name,
    is_global_id,
    is_local_id,
)

L3_SCHEMA_NAME = 'philosophia.stager.l3-projection.v1'
PUBLIC_ITEM_SCHEMA_NAME = 'philosophia.stageb.public-item.v1'

L3_SUCCESS_KEYS = (
    'schema', 'ok', 'cause', 'theorem_identity', 'theorem_name',
    'skeleton_identity', 'canonical_theorem', 'public_item',
)
L3_FAILURE_KEYS = ('schema', 'ok', 'cause', 'subcause')
PUBLIC_ITEM_KEYS = (
    'schema', 'theory_sha256', 'premises', 'theorem_name', 'goal',
)
THEOREM_KEYS = ('atoms', 'hypotheses', 'goal')

CAUSE_SEQUENT_REDERIVATION_MISMATCH = 'SEQUENT_REDERIVATION_MISMATCH'
L3_MISMATCH_SUBCAUSES = (
    'THEOREM_KEYSET_MISMATCH',
    'THEOREM_ATOMS_MISMATCH',
    'THEOREM_HYPOTHESES_MISMATCH',
    'THEOREM_GOAL_MISMATCH',
)

L3_INVARIANT_CODES = (
    'INPUT_NOT_L1_SHAPED',
    'DECLARED_ATOM_COUNT_OUT_OF_RANGE',
    'BIJECTION_BOUND_EXCEEDED',
    'FORMULA_RECURSION_BOUND_EXCEEDED',
    'PROOF_RECURSION_BOUND_EXCEEDED',
    'CANONICAL_THEOREM_PRECONDITION_VIOLATED',
)

FORMULA_RECURSION_BOUND = 24
PROOF_RECURSION_BOUND = 38
BIJECTION_BOUND = 720

THEOREM_NAME_PREFIX = 't_'

SKELETON_ASSUME_GLOBAL = 'ASSUME_GLOBAL'
SKELETON_ASSUME_LOCAL = 'ASSUME_LOCAL'
SKELETON_AND_ELIM_KINDS = ('AND_ELIM_LEFT', 'AND_ELIM_RIGHT')
SKELETON_OR_INTRO_KINDS = ('OR_INTRO_LEFT', 'OR_INTRO_RIGHT')


class L3InvariantError(Exception):
    """Closed internal-defect signal. Never a draw outcome."""

    def __init__(self, code: str) -> None:
        Exception.__init__(self, code)
        self.code = code


def _raise(code: str) -> None:
    raise L3InvariantError(code)


def _formula_shape(formula: object, code: str, depth: int) -> None:
    if depth > FORMULA_RECURSION_BOUND:
        _raise('FORMULA_RECURSION_BOUND_EXCEEDED')
    if type(formula) is not dict:
        _raise(code)
    kind = formula.get('kind')
    if kind not in FORMULA_KINDS:
        _raise(code)
    if set(formula.keys()) != set(FORMULA_KEYS[kind]):
        _raise(code)
    if kind == 'ATOM':
        if not is_atom_name(formula['name']):
            _raise(code)
        return
    if kind == 'FALSE':
        return
    if kind == 'NOT':
        _formula_shape(formula['arg'], code, depth + 1)
        return
    _formula_shape(formula['left'], code, depth + 1)
    _formula_shape(formula['right'], code, depth + 1)


def _formula_atoms(formula: Mapping, acc: set, depth: int) -> None:
    if depth > FORMULA_RECURSION_BOUND:
        _raise('FORMULA_RECURSION_BOUND_EXCEEDED')
    kind = formula['kind']
    if kind == 'ATOM':
        acc.add(formula['name'])
        return
    if kind == 'FALSE':
        return
    if kind == 'NOT':
        _formula_atoms(formula['arg'], acc, depth + 1)
        return
    _formula_atoms(formula['left'], acc, depth + 1)
    _formula_atoms(formula['right'], acc, depth + 1)


def _fresh_formula(formula: Mapping, depth: int) -> dict:
    if depth > FORMULA_RECURSION_BOUND:
        _raise('FORMULA_RECURSION_BOUND_EXCEEDED')
    kind = formula['kind']
    if kind == 'ATOM':
        return {'kind': 'ATOM', 'name': formula['name']}
    if kind == 'FALSE':
        return {'kind': 'FALSE'}
    if kind == 'NOT':
        return {'kind': 'NOT', 'arg': _fresh_formula(formula['arg'], depth + 1)}
    return {
        'kind': kind,
        'left': _fresh_formula(formula['left'], depth + 1),
        'right': _fresh_formula(formula['right'], depth + 1),
    }


def _substitute_formula(formula: Mapping, renaming: Mapping, depth: int) -> dict:
    if depth > FORMULA_RECURSION_BOUND:
        _raise('FORMULA_RECURSION_BOUND_EXCEEDED')
    kind = formula['kind']
    if kind == 'ATOM':
        return {'kind': 'ATOM', 'name': renaming[formula['name']]}
    if kind == 'FALSE':
        return {'kind': 'FALSE'}
    if kind == 'NOT':
        return {
            'kind': 'NOT',
            'arg': _substitute_formula(formula['arg'], renaming, depth + 1),
        }
    return {
        'kind': kind,
        'left': _substitute_formula(formula['left'], renaming, depth + 1),
        'right': _substitute_formula(formula['right'], renaming, depth + 1),
    }


def _theorem_shape(theorem: object, shape_code: str, count_code: str) -> int:
    if type(theorem) is not dict:
        _raise(shape_code)
    if set(theorem.keys()) != set(THEOREM_KEYS):
        _raise(shape_code)
    atoms = theorem['atoms']
    if type(atoms) is not list:
        _raise(shape_code)
    for name in atoms:
        if not is_atom_name(name):
            _raise(shape_code)
    if len(atoms) != len(set(atoms)):
        _raise(shape_code)
    if atoms != sorted(atoms):
        _raise(shape_code)
    count = len(atoms)
    if not MIN_DECLARED_ATOMS <= count <= MAX_DECLARED_ATOMS:
        _raise(count_code)
    hypotheses = theorem['hypotheses']
    if type(hypotheses) is not list:
        _raise(shape_code)
    occurring: set = set()
    for formula in hypotheses:
        _formula_shape(formula, shape_code, 1)
        _formula_atoms(formula, occurring, 1)
    _formula_shape(theorem['goal'], shape_code, 1)
    _formula_atoms(theorem['goal'], occurring, 1)
    if not occurring <= set(atoms):
        _raise(shape_code)
    return count


def _bijections(count: int) -> Iterator[Tuple[int, ...]]:
    total = 1
    for factor in range(2, count + 1):
        total = total * factor
    if total > BIJECTION_BOUND:
        _raise('BIJECTION_BOUND_EXCEEDED')
    return permutations(range(count))


def canonical_theorem(theorem: Mapping) -> dict:
    """Alpha-canonical theorem: minimum canonical bytes over all k! bijections."""
    count = _theorem_shape(theorem, 'INPUT_NOT_L1_SHAPED',
                           'DECLARED_ATOM_COUNT_OUT_OF_RANGE')
    source_atoms = list(theorem['atoms'])
    target_atoms = ['a' + str(index) for index in range(count)]
    best: Optional[dict] = None
    best_bytes: Optional[bytes] = None
    for permutation in _bijections(count):
        renaming = {
            source_atoms[index]: target_atoms[permutation[index]]
            for index in range(count)
        }
        hypotheses = [
            _substitute_formula(formula, renaming, 1)
            for formula in theorem['hypotheses']
        ]
        hypotheses.sort(key=canonical_bytes)
        candidate = {
            'atoms': list(target_atoms),
            'hypotheses': hypotheses,
            'goal': _substitute_formula(theorem['goal'], renaming, 1),
        }
        candidate_bytes = canonical_bytes(candidate)
        if best_bytes is None or candidate_bytes < best_bytes:
            best = candidate
            best_bytes = candidate_bytes
    return best


def theorem_identity(theorem: Mapping) -> str:
    return canonical_hash(canonical_theorem(theorem))


def _skeleton_sort2(first: Mapping, second: Mapping) -> list:
    if canonical_bytes(first) <= canonical_bytes(second):
        return [first, second]
    return [second, first]


def _rule_skeleton(node: object, depth: int) -> dict:
    if depth > PROOF_RECURSION_BOUND:
        _raise('PROOF_RECURSION_BOUND_EXCEEDED')
    if type(node) is not dict:
        _raise('INPUT_NOT_L1_SHAPED')
    kind = node.get('kind')
    if kind not in RULE_KINDS:
        _raise('INPUT_NOT_L1_SHAPED')
    if set(node.keys()) != set(PROOF_NODE_KEYS[kind]):
        _raise('INPUT_NOT_L1_SHAPED')
    if kind == 'ASSUME':
        identifier = node['hypothesis_id']
        if is_global_id(identifier):
            return {'kind': SKELETON_ASSUME_GLOBAL}
        if is_local_id(identifier):
            return {'kind': SKELETON_ASSUME_LOCAL}
        _raise('INPUT_NOT_L1_SHAPED')
    if kind == 'AND_INTRO':
        return {
            'kind': 'AND_INTRO',
            'children': _skeleton_sort2(
                _rule_skeleton(node['left'], depth + 1),
                _rule_skeleton(node['right'], depth + 1),
            ),
        }
    if kind == 'OR_ELIM':
        children = [_rule_skeleton(node['major'], depth + 1)]
        children.extend(_skeleton_sort2(
            _rule_skeleton(node['left_branch'], depth + 1),
            _rule_skeleton(node['right_branch'], depth + 1),
        ))
        return {'kind': 'OR_ELIM', 'children': children}
    if kind == 'NOT_ELIM':
        return {
            'kind': 'NOT_ELIM',
            'children': [
                _rule_skeleton(node['negative'], depth + 1),
                _rule_skeleton(node['positive'], depth + 1),
            ],
        }
    if kind == 'NOT_INTRO':
        return {
            'kind': 'NOT_INTRO',
            'children': [_rule_skeleton(node['body'], depth + 1)],
        }
    if kind in SKELETON_AND_ELIM_KINDS:
        erased = 'AND_ELIM'
    elif kind in SKELETON_OR_INTRO_KINDS:
        erased = 'OR_INTRO'
    else:
        erased = 'EXFALSO'
    return {
        'kind': erased,
        'children': [_rule_skeleton(node['source'], depth + 1)],
    }


def rule_skeleton(node: Mapping) -> dict:
    """Erase formulas, atoms, conclusions, identifiers and elim/intro direction."""
    return _rule_skeleton(node, 1)


def _plan_shape(plan: object) -> None:
    if type(plan) is not dict:
        _raise('INPUT_NOT_L1_SHAPED')
    if set(plan.keys()) != set(PLAN_KEYS):
        _raise('INPUT_NOT_L1_SHAPED')
    if type(plan['atoms']) is not list:
        _raise('INPUT_NOT_L1_SHAPED')
    if type(plan['hypotheses']) is not list:
        _raise('INPUT_NOT_L1_SHAPED')
    for hypothesis in plan['hypotheses']:
        if type(hypothesis) is not dict:
            _raise('INPUT_NOT_L1_SHAPED')
        if set(hypothesis.keys()) != set(HYPOTHESIS_KEYS):
            _raise('INPUT_NOT_L1_SHAPED')
        if not is_global_id(hypothesis['id']):
            _raise('INPUT_NOT_L1_SHAPED')


def skeleton_identity(plan: Mapping) -> str:
    _plan_shape(plan)
    return canonical_hash(rule_skeleton(plan['proof']))


def rederive_theorem(plan: Mapping) -> dict:
    """Rebuild the raw theorem from public plan fields only. No proof walk."""
    _plan_shape(plan)
    for name in plan['atoms']:
        if not is_atom_name(name):
            _raise('INPUT_NOT_L1_SHAPED')
    hypotheses = []
    for hypothesis in plan['hypotheses']:
        _formula_shape(hypothesis['formula'], 'INPUT_NOT_L1_SHAPED', 1)
        hypotheses.append(_fresh_formula(hypothesis['formula'], 1))
    _formula_shape(plan['goal'], 'INPUT_NOT_L1_SHAPED', 1)
    return {
        'atoms': list(plan['atoms']),
        'hypotheses': hypotheses,
        'goal': _fresh_formula(plan['goal'], 1),
    }


def public_projection(canon_theorem: Mapping) -> dict:
    """Five-key sealed public item, rendered only from a canonical theorem."""
    code = 'CANONICAL_THEOREM_PRECONDITION_VIOLATED'
    count = _theorem_shape(canon_theorem, code, code)
    if canon_theorem['atoms'] != ['a' + str(index) for index in range(count)]:
        _raise(code)
    encoded = [canonical_bytes(formula) for formula in canon_theorem['hypotheses']]
    for index in range(1, len(encoded)):
        if not encoded[index - 1] < encoded[index]:
            _raise(code)
    return {
        'schema': PUBLIC_ITEM_SCHEMA_NAME,
        'theory_sha256': THEORY_SHA256,
        'premises': list(THEORY_PREMISES),
        'theorem_name': THEOREM_NAME_PREFIX + canonical_hash(canon_theorem),
        'goal': render_sequent(
            canon_theorem['atoms'],
            canon_theorem['hypotheses'],
            canon_theorem['goal'],
        ),
    }


def _mismatch(subcause: str) -> dict:
    return {
        'schema': L3_SCHEMA_NAME,
        'ok': False,
        'cause': CAUSE_SEQUENT_REDERIVATION_MISMATCH,
        'subcause': subcause,
    }


def identify(plan: Mapping, checker_theorem: Mapping) -> dict:
    """Raw compare, then canonical theorem, identities and public projection."""
    raw = rederive_theorem(plan)
    if type(checker_theorem) is not dict:
        return _mismatch('THEOREM_KEYSET_MISMATCH')
    if set(checker_theorem.keys()) != set(THEOREM_KEYS):
        return _mismatch('THEOREM_KEYSET_MISMATCH')
    if canonical_bytes(raw['atoms']) != canonical_bytes(checker_theorem['atoms']):
        return _mismatch('THEOREM_ATOMS_MISMATCH')
    if canonical_bytes(raw['hypotheses']) != canonical_bytes(
            checker_theorem['hypotheses']):
        return _mismatch('THEOREM_HYPOTHESES_MISMATCH')
    if canonical_bytes(raw['goal']) != canonical_bytes(checker_theorem['goal']):
        return _mismatch('THEOREM_GOAL_MISMATCH')
    canon = canonical_theorem(raw)
    identity_hex = canonical_hash(canon)
    return {
        'schema': L3_SCHEMA_NAME,
        'ok': True,
        'cause': None,
        'theorem_identity': identity_hex,
        'theorem_name': THEOREM_NAME_PREFIX + identity_hex,
        'skeleton_identity': skeleton_identity(plan),
        'canonical_theorem': canon,
        'public_item': public_projection(canon),
    }
