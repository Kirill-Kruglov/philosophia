#!/usr/bin/env python3
"""Independent L1 ND-plan checker. Imports only L0 modules and the stdlib."""

from __future__ import annotations

from typing import Any, Mapping

from phase2_stageb_canonical import canonical_bytes
from phase2_stageb_causes import (
    CAUSE_PLAN_CONSTRAINT_INVALID,
    CAUSE_PLAN_NON_NORMAL,
    CAUSE_PLAN_SCHEMA_INVALID,
    CAUSE_PLAN_TYPE_INVALID,
)
from phase2_stageb_render import render_sequent
from phase2_stageb_schema import (
    BAND_NAMES,
    BRANCHING_FAMILIES,
    EXPECTATION_KEYS,
    EXPECTATION_SCHEMA_NAME,
    FAMILY_ORDER,
    FORMULA_KEYS,
    FORMULA_KINDS,
    HYPOTHESIS_KEYS,
    KIND_TO_FAMILY,
    MAX_DECLARED_ATOMS,
    MAX_FORMULA_NODES,
    MIN_DECLARED_ATOMS,
    MIN_DEPENDENCY_DEPTH,
    MIN_FAMILY_COUNT,
    PLAN_KEYS,
    PLAN_SCHEMA_NAME,
    PROOF_CHILD_FIELDS,
    PROOF_NODE_KEYS,
    RULE_KINDS,
    band_of_node_count,
    is_atom_name,
    is_exact_int,
    is_global_id,
    is_local_id,
    is_printable_ascii,
)


def _fail(cause: str) -> dict:
    return {'ok': False, 'cause': cause}


def _keys_of(mapping: Mapping) -> tuple:
    return tuple(mapping.keys())


def _exact_keys(mapping: object, expected: tuple) -> bool:
    if type(mapping) is not dict:
        return False
    return _keys_of(mapping) == expected or set(mapping.keys()) == set(expected)


def formulas_equal(left: Mapping, right: Mapping) -> bool:
    return canonical_bytes(left) == canonical_bytes(right)


def formula_node_count(formula: Mapping) -> int:
    kind = formula['kind']
    if kind in ('ATOM', 'FALSE'):
        return 1
    if kind == 'NOT':
        return 1 + formula_node_count(formula['arg'])
    return 1 + formula_node_count(formula['left']) + formula_node_count(formula['right'])


def collect_atom_names(formula: Mapping, acc: set) -> None:
    kind = formula['kind']
    if kind == 'ATOM':
        acc.add(formula['name'])
        return
    if kind == 'FALSE':
        return
    if kind == 'NOT':
        collect_atom_names(formula['arg'], acc)
        return
    collect_atom_names(formula['left'], acc)
    collect_atom_names(formula['right'], acc)


def proof_children(node: Mapping) -> tuple:
    return tuple(node[field] for field in PROOF_CHILD_FIELDS[node['kind']])


def _schema_formula(formula: object) -> str | None:
    if type(formula) is not dict:
        return CAUSE_PLAN_SCHEMA_INVALID
    kind = formula.get('kind')
    if kind not in FORMULA_KINDS:
        return CAUSE_PLAN_SCHEMA_INVALID
    if set(formula.keys()) != set(FORMULA_KEYS[kind]):
        return CAUSE_PLAN_SCHEMA_INVALID
    if kind == 'ATOM':
        if not is_printable_ascii(formula['name']) or not is_atom_name(formula['name']):
            return CAUSE_PLAN_SCHEMA_INVALID
        return None
    if kind == 'FALSE':
        return None
    if kind == 'NOT':
        return _schema_formula(formula['arg'])
    err = _schema_formula(formula['left'])
    if err:
        return err
    return _schema_formula(formula['right'])


def _schema_hypothesis(hyp: object, *, local: bool) -> str | None:
    if type(hyp) is not dict or set(hyp.keys()) != set(HYPOTHESIS_KEYS):
        return CAUSE_PLAN_SCHEMA_INVALID
    ident = hyp['id']
    if not is_printable_ascii(ident):
        return CAUSE_PLAN_SCHEMA_INVALID
    if local:
        if not is_local_id(ident):
            return CAUSE_PLAN_SCHEMA_INVALID
    elif not is_global_id(ident):
        return CAUSE_PLAN_SCHEMA_INVALID
    return _schema_formula(hyp['formula'])


def _schema_proof(node: object, local_ids: list, global_ids: set) -> str | None:
    if type(node) is not dict:
        return CAUSE_PLAN_SCHEMA_INVALID
    kind = node.get('kind')
    if kind not in RULE_KINDS:
        return CAUSE_PLAN_SCHEMA_INVALID
    if set(node.keys()) != set(PROOF_NODE_KEYS[kind]):
        return CAUSE_PLAN_SCHEMA_INVALID
    err = _schema_formula(node['conclusion'])
    if err:
        return err
    if kind == 'ASSUME':
        hid = node['hypothesis_id']
        if not is_printable_ascii(hid):
            return CAUSE_PLAN_SCHEMA_INVALID
        if not (is_global_id(hid) or is_local_id(hid)):
            return CAUSE_PLAN_SCHEMA_INVALID
        return None
    if kind == 'OR_ELIM':
        err = _schema_hypothesis(node['left_assumption'], local=True)
        if err:
            return err
        err = _schema_hypothesis(node['right_assumption'], local=True)
        if err:
            return err
        for ident in (
                node['left_assumption']['id'], node['right_assumption']['id']):
            if ident in global_ids or ident in local_ids:
                return CAUSE_PLAN_SCHEMA_INVALID
            local_ids.append(ident)
        if node['left_assumption']['id'] == node['right_assumption']['id']:
            return CAUSE_PLAN_SCHEMA_INVALID
    if kind == 'NOT_INTRO':
        err = _schema_hypothesis(node['assumption'], local=True)
        if err:
            return err
        ident = node['assumption']['id']
        if ident in global_ids or ident in local_ids:
            return CAUSE_PLAN_SCHEMA_INVALID
        local_ids.append(ident)
    for child in proof_children(node):
        err = _schema_proof(child, local_ids, global_ids)
        if err:
            return err
    return None


def _schema_plan(plan: object) -> str | None:
    if type(plan) is not dict or set(plan.keys()) != set(PLAN_KEYS):
        return CAUSE_PLAN_SCHEMA_INVALID
    if plan['schema'] != PLAN_SCHEMA_NAME:
        return CAUSE_PLAN_SCHEMA_INVALID
    atoms = plan['atoms']
    if type(atoms) is not list or not atoms:
        return CAUSE_PLAN_SCHEMA_INVALID
    for name in atoms:
        if not is_printable_ascii(name) or not is_atom_name(name):
            return CAUSE_PLAN_SCHEMA_INVALID
    if len(atoms) != len(set(atoms)):
        return CAUSE_PLAN_SCHEMA_INVALID
    if atoms != sorted(atoms):
        return CAUSE_PLAN_SCHEMA_INVALID
    hyps = plan['hypotheses']
    if type(hyps) is not list:
        return CAUSE_PLAN_SCHEMA_INVALID
    global_ids = []
    for hyp in hyps:
        err = _schema_hypothesis(hyp, local=False)
        if err:
            return err
        if hyp['id'] in global_ids:
            return CAUSE_PLAN_SCHEMA_INVALID
        global_ids.append(hyp['id'])
    err = _schema_formula(plan['goal'])
    if err:
        return err
    return _schema_proof(plan['proof'], [], set(global_ids))


def _schema_expectation(expectation: object) -> str | None:
    if type(expectation) is not dict or set(expectation.keys()) != set(EXPECTATION_KEYS):
        return CAUSE_PLAN_SCHEMA_INVALID
    if expectation['schema'] != EXPECTATION_SCHEMA_NAME:
        return CAUSE_PLAN_SCHEMA_INVALID
    if not is_exact_int(expectation['node_count']):
        return CAUSE_PLAN_SCHEMA_INVALID
    if expectation['band'] not in BAND_NAMES:
        return CAUSE_PLAN_SCHEMA_INVALID
    if not is_exact_int(expectation['max_dependency_depth']):
        return CAUSE_PLAN_SCHEMA_INVALID
    families = expectation['families']
    if type(families) is not list:
        return CAUSE_PLAN_SCHEMA_INVALID
    for family in families:
        if family not in FAMILY_ORDER:
            return CAUSE_PLAN_SCHEMA_INVALID
    if len(families) != len(set(families)):
        return CAUSE_PLAN_SCHEMA_INVALID
    ranked = tuple(FAMILY_ORDER.index(family) for family in families)
    if ranked != tuple(sorted(ranked)):
        return CAUSE_PLAN_SCHEMA_INVALID
    return None


def _constraint_expectation_bounds(expectation: Mapping) -> str | None:
    if expectation['node_count'] < 0:
        return CAUSE_PLAN_CONSTRAINT_INVALID
    if expectation['max_dependency_depth'] < 0:
        return CAUSE_PLAN_CONSTRAINT_INVALID
    if band_of_node_count(expectation['node_count']) != expectation['band']:
        return CAUSE_PLAN_CONSTRAINT_INVALID
    return None


def public_atom_names(plan: Mapping) -> set:
    occurring: set = set()
    for hyp in plan['hypotheses']:
        collect_atom_names(hyp['formula'], occurring)
    collect_atom_names(plan['goal'], occurring)
    return occurring


def _type_proof(node: Mapping, env: dict) -> tuple[str | None, Mapping | None]:
    kind = node['kind']
    stated = node['conclusion']
    if kind == 'ASSUME':
        hid = node['hypothesis_id']
        if hid not in env:
            return CAUSE_PLAN_TYPE_INVALID, None
        if not formulas_equal(stated, env[hid]):
            return CAUSE_PLAN_TYPE_INVALID, None
        return None, stated
    if kind == 'AND_INTRO':
        err, left = _type_proof(node['left'], env)
        if err:
            return err, None
        err, right = _type_proof(node['right'], env)
        if err:
            return err, None
        derived = {'kind': 'AND', 'left': left, 'right': right}
        if not formulas_equal(stated, derived):
            return CAUSE_PLAN_TYPE_INVALID, None
        return None, stated
    if kind in ('AND_ELIM_LEFT', 'AND_ELIM_RIGHT'):
        err, source = _type_proof(node['source'], env)
        if err:
            return err, None
        if source['kind'] != 'AND':
            return CAUSE_PLAN_TYPE_INVALID, None
        derived = source['left'] if kind == 'AND_ELIM_LEFT' else source['right']
        if not formulas_equal(stated, derived):
            return CAUSE_PLAN_TYPE_INVALID, None
        return None, stated
    if kind in ('OR_INTRO_LEFT', 'OR_INTRO_RIGHT'):
        err, source = _type_proof(node['source'], env)
        if err:
            return err, None
        if stated['kind'] != 'OR':
            return CAUSE_PLAN_TYPE_INVALID, None
        expected = stated['left'] if kind == 'OR_INTRO_LEFT' else stated['right']
        if not formulas_equal(source, expected):
            return CAUSE_PLAN_TYPE_INVALID, None
        return None, stated
    if kind == 'OR_ELIM':
        err, major = _type_proof(node['major'], env)
        if err:
            return err, None
        if major['kind'] != 'OR':
            return CAUSE_PLAN_TYPE_INVALID, None
        left_ass = node['left_assumption']
        right_ass = node['right_assumption']
        if not formulas_equal(left_ass['formula'], major['left']):
            return CAUSE_PLAN_TYPE_INVALID, None
        if not formulas_equal(right_ass['formula'], major['right']):
            return CAUSE_PLAN_TYPE_INVALID, None
        left_env = dict(env)
        left_env[left_ass['id']] = left_ass['formula']
        right_env = dict(env)
        right_env[right_ass['id']] = right_ass['formula']
        err, left_conc = _type_proof(node['left_branch'], left_env)
        if err:
            return err, None
        err, right_conc = _type_proof(node['right_branch'], right_env)
        if err:
            return err, None
        if not formulas_equal(left_conc, stated):
            return CAUSE_PLAN_TYPE_INVALID, None
        if not formulas_equal(right_conc, stated):
            return CAUSE_PLAN_TYPE_INVALID, None
        return None, stated
    if kind == 'NOT_INTRO':
        assumption = node['assumption']
        body_env = dict(env)
        body_env[assumption['id']] = assumption['formula']
        err, body = _type_proof(node['body'], body_env)
        if err:
            return err, None
        if body['kind'] != 'FALSE':
            return CAUSE_PLAN_TYPE_INVALID, None
        derived = {'kind': 'NOT', 'arg': assumption['formula']}
        if not formulas_equal(stated, derived):
            return CAUSE_PLAN_TYPE_INVALID, None
        return None, stated
    if kind == 'NOT_ELIM':
        err, negative = _type_proof(node['negative'], env)
        if err:
            return err, None
        err, positive = _type_proof(node['positive'], env)
        if err:
            return err, None
        if negative['kind'] != 'NOT':
            return CAUSE_PLAN_TYPE_INVALID, None
        if not formulas_equal(negative['arg'], positive):
            return CAUSE_PLAN_TYPE_INVALID, None
        if stated['kind'] != 'FALSE':
            return CAUSE_PLAN_TYPE_INVALID, None
        return None, stated
    if kind == 'EXFALSO':
        err, source = _type_proof(node['source'], env)
        if err:
            return err, None
        if source['kind'] != 'FALSE':
            return CAUSE_PLAN_TYPE_INVALID, None
        return None, stated
    return CAUSE_PLAN_TYPE_INVALID, None


def _walk_formulas(plan: Mapping) -> list:
    formulas = []
    for hyp in plan['hypotheses']:
        formulas.append(hyp['formula'])
    formulas.append(plan['goal'])

    def walk(node: Mapping) -> None:
        formulas.append(node['conclusion'])
        kind = node['kind']
        if kind == 'OR_ELIM':
            formulas.append(node['left_assumption']['formula'])
            formulas.append(node['right_assumption']['formula'])
        if kind == 'NOT_INTRO':
            formulas.append(node['assumption']['formula'])
        if kind in ('OR_INTRO_LEFT', 'OR_INTRO_RIGHT') and node['conclusion']['kind'] == 'OR':
            formulas.append(node['conclusion']['left'])
            formulas.append(node['conclusion']['right'])
        for child in proof_children(node):
            walk(child)

    walk(plan['proof'])
    return formulas


def _collect_assume_ids(node: Mapping, acc: set, scoped: dict) -> None:
    kind = node['kind']
    if kind == 'ASSUME':
        acc.add(node['hypothesis_id'])
        return
    if kind == 'OR_ELIM':
        _collect_assume_ids(node['major'], acc, scoped)
        left_acc: set = set()
        right_acc: set = set()
        _collect_assume_ids(node['left_branch'], left_acc, scoped)
        _collect_assume_ids(node['right_branch'], right_acc, scoped)
        acc.update(left_acc)
        acc.update(right_acc)
        scoped[node['left_assumption']['id']] = left_acc
        scoped[node['right_assumption']['id']] = right_acc
        return
    if kind == 'NOT_INTRO':
        body_acc: set = set()
        _collect_assume_ids(node['body'], body_acc, scoped)
        acc.update(body_acc)
        scoped[node['assumption']['id']] = body_acc
        return
    for child in proof_children(node):
        _collect_assume_ids(child, acc, scoped)


def inference_node_count(node: Mapping) -> int:
    if node['kind'] == 'ASSUME':
        return 0
    return 1 + sum(inference_node_count(child) for child in proof_children(node))


def inference_depth(node: Mapping) -> int:
    if node['kind'] == 'ASSUME':
        return 0
    depths = [
        inference_depth(child)
        for child in proof_children(node)
        if child['kind'] != 'ASSUME'
    ]
    if not depths:
        return 0
    return 1 + max(depths)


def used_families(node: Mapping) -> list:
    found = set()

    def walk(cur: Mapping) -> None:
        if cur['kind'] == 'ASSUME':
            return
        found.add(KIND_TO_FAMILY[cur['kind']])
        for child in proof_children(cur):
            walk(child)

    walk(node)
    return [family for family in FAMILY_ORDER if family in found]


def _has_beta_redex(node: Mapping) -> bool:
    kind = node['kind']
    if kind in ('AND_ELIM_LEFT', 'AND_ELIM_RIGHT'):
        if node['source']['kind'] == 'AND_INTRO':
            return True
    if kind == 'OR_ELIM':
        if node['major']['kind'] in ('OR_INTRO_LEFT', 'OR_INTRO_RIGHT'):
            return True
    if kind == 'NOT_ELIM':
        if node['negative']['kind'] == 'NOT_INTRO':
            return True
    return any(_has_beta_redex(child) for child in proof_children(node))


def rederived_theorem(plan: Mapping, goal: Mapping) -> dict:
    return {
        'atoms': list(plan['atoms']),
        'hypotheses': [hyp['formula'] for hyp in plan['hypotheses']],
        'goal': goal,
    }


def check_plan(plan: object, expectation: object) -> dict:
    err = _schema_plan(plan)
    if err:
        return _fail(err)
    err = _schema_expectation(expectation)
    if err:
        return _fail(err)
    env = {hyp['id']: hyp['formula'] for hyp in plan['hypotheses']}
    err, derived = _type_proof(plan['proof'], env)
    if err:
        return _fail(err)
    if not formulas_equal(derived, plan['goal']):
        return _fail(CAUSE_PLAN_TYPE_INVALID)

    atoms = list(plan['atoms'])
    if not (MIN_DECLARED_ATOMS <= len(atoms) <= MAX_DECLARED_ATOMS):
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    occurring: set = set()
    for formula in _walk_formulas(plan):
        if formula_node_count(formula) > MAX_FORMULA_NODES:
            return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
        collect_atom_names(formula, occurring)
    declared = set(atoms)
    if not occurring <= declared:
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    if not declared <= public_atom_names(plan):
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)

    global_formulas = [canonical_bytes(hyp['formula']) for hyp in plan['hypotheses']]
    if len(global_formulas) != len(set(global_formulas)):
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)

    referenced: set = set()
    scoped_uses: dict = {}
    _collect_assume_ids(plan['proof'], referenced, scoped_uses)
    for hyp in plan['hypotheses']:
        if hyp['id'] not in referenced:
            return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    for local_id, uses in scoped_uses.items():
        if local_id not in uses:
            return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)

    node_count = inference_node_count(plan['proof'])
    depth = inference_depth(plan['proof'])
    families = used_families(plan['proof'])
    band = band_of_node_count(node_count)
    if band is None:
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    err = _constraint_expectation_bounds(expectation)
    if err:
        return _fail(err)
    if node_count != expectation['node_count']:
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    if band != expectation['band']:
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    if depth != expectation['max_dependency_depth']:
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    if families != list(expectation['families']):
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    if depth < MIN_DEPENDENCY_DEPTH:
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    if len(families) < MIN_FAMILY_COUNT:
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)
    if not any(family in families for family in BRANCHING_FAMILIES):
        return _fail(CAUSE_PLAN_CONSTRAINT_INVALID)

    if _has_beta_redex(plan['proof']):
        return _fail(CAUSE_PLAN_NON_NORMAL)

    theorem = rederived_theorem(plan, derived)
    return {
        'ok': True,
        'cause': None,
        'node_count': node_count,
        'band': band,
        'families': families,
        'max_dependency_depth': depth,
        'theorem': theorem,
        'rendered_sequent': render_sequent(
            theorem['atoms'], theorem['hypotheses'], theorem['goal']),
    }
