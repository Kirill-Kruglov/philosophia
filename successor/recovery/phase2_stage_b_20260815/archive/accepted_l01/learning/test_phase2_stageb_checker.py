#!/usr/bin/env python3
"""L1 independent checker regressions. Hand-written fixtures only."""

from __future__ import annotations

import ast
import copy
import sys
import unittest
from pathlib import Path

LEARNING_DIR = Path(__file__).resolve().parent
if str(LEARNING_DIR) not in sys.path:
    sys.path.insert(0, str(LEARNING_DIR))

from phase2_stageb_canonical import canonical_bytes, canonical_hash
from phase2_stageb_causes import (
    CAUSE_PLAN_CONSTRAINT_INVALID,
    CAUSE_PLAN_NON_NORMAL,
    CAUSE_PLAN_SCHEMA_INVALID,
    CAUSE_PLAN_TYPE_INVALID,
    MUTATION_TO_CAUSE,
)
from phase2_stageb_checker import (
    _collect_assume_ids,
    _has_beta_redex,
    _type_proof,
    _walk_formulas,
    check_plan,
    collect_atom_names,
    formulas_equal,
    inference_depth,
    inference_node_count,
    public_atom_names,
    used_families,
)
from phase2_stageb_render import render_sequent
from phase2_stageb_schema import (
    EXPECTATION_SCHEMA_NAME,
    PLAN_SCHEMA_NAME,
    band_of_node_count,
)


def atom(name):
    return {'kind': 'ATOM', 'name': name}


def false_():
    return {'kind': 'FALSE'}


def not_(arg):
    return {'kind': 'NOT', 'arg': copy.deepcopy(arg)}


def and_(left, right):
    return {'kind': 'AND', 'left': copy.deepcopy(left), 'right': copy.deepcopy(right)}


def or_(left, right):
    return {'kind': 'OR', 'left': copy.deepcopy(left), 'right': copy.deepcopy(right)}


def hyp(ident, formula):
    return {'id': ident, 'formula': formula}


def assume(hid, conclusion):
    return {
        'kind': 'ASSUME',
        'hypothesis_id': hid,
        'conclusion': copy.deepcopy(conclusion),
    }


def and_intro(left, right):
    return {
        'kind': 'AND_INTRO',
        'left': left,
        'right': right,
        'conclusion': and_(left['conclusion'], right['conclusion']),
    }


def and_elim_left(source):
    return {
        'kind': 'AND_ELIM_LEFT',
        'source': source,
        'conclusion': copy.deepcopy(source['conclusion']['left']),
    }


def and_elim_right(source):
    return {
        'kind': 'AND_ELIM_RIGHT',
        'source': source,
        'conclusion': copy.deepcopy(source['conclusion']['right']),
    }


def or_intro_left(source, other):
    return {
        'kind': 'OR_INTRO_LEFT',
        'source': source,
        'conclusion': or_(copy.deepcopy(source['conclusion']), copy.deepcopy(other)),
    }


def or_intro_right(source, other):
    return {
        'kind': 'OR_INTRO_RIGHT',
        'source': source,
        'conclusion': or_(copy.deepcopy(other), copy.deepcopy(source['conclusion'])),
    }


def or_elim(major, left_ass, left_branch, right_ass, right_branch, conclusion):
    return {
        'kind': 'OR_ELIM',
        'major': major,
        'left_assumption': left_ass,
        'left_branch': left_branch,
        'right_assumption': right_ass,
        'right_branch': right_branch,
        'conclusion': copy.deepcopy(conclusion),
    }


def not_intro(assumption, body):
    return {
        'kind': 'NOT_INTRO',
        'assumption': assumption,
        'body': body,
        'conclusion': not_(copy.deepcopy(assumption['formula'])),
    }


def not_elim(negative, positive):
    return {
        'kind': 'NOT_ELIM',
        'negative': negative,
        'positive': positive,
        'conclusion': false_(),
    }


def exfalso(source, conclusion):
    return {
        'kind': 'EXFALSO',
        'source': source,
        'conclusion': copy.deepcopy(conclusion),
    }


def or_commute(hid, p, q, left_id, right_id):
    swapped = or_(copy.deepcopy(q), copy.deepcopy(p))
    return or_elim(
        assume(hid, or_(copy.deepcopy(p), copy.deepcopy(q))),
        hyp(left_id, copy.deepcopy(p)),
        or_intro_right(assume(left_id, p), q),
        hyp(right_id, copy.deepcopy(q)),
        or_intro_left(assume(right_id, q), p),
        swapped,
    )


def not_contra(local_id):
    payload = and_(atom('a0'), not_(atom('a0')))
    assumed = assume(local_id, payload)
    return not_intro(
        hyp(local_id, payload),
        not_elim(and_elim_right(assumed), and_elim_left(copy.deepcopy(assumed))),
    )


def plan(atoms, hypotheses, goal, proof):
    return {
        'schema': PLAN_SCHEMA_NAME,
        'atoms': list(atoms),
        'hypotheses': hypotheses,
        'goal': goal,
        'proof': proof,
    }


def expectation_for(proof, families=None, depth=None, node_count=None):
    count = inference_node_count(proof) if node_count is None else node_count
    fams = used_families(proof) if families is None else list(families)
    dep = inference_depth(proof) if depth is None else depth
    return {
        'schema': EXPECTATION_SCHEMA_NAME,
        'node_count': count,
        'band': band_of_node_count(count),
        'families': fams,
        'max_dependency_depth': dep,
    }


A0 = atom('a0')
A1 = atom('a1')
A2 = atom('a2')
A3 = atom('a3')
A4 = atom('a4')
A5 = atom('a5')
A6 = atom('a6')


def valid_s1_or_and():
    h0 = or_(A0, A1)
    h1 = and_(A2, A2)
    inner = and_intro(
        and_elim_left(assume('h1', h1)),
        or_commute('h0', A0, A1, 'l0', 'l1'),
    )
    proof = and_intro(inner, or_commute('h0', A0, A1, 'l2', 'l3'))
    return plan(
        ['a0', 'a1', 'a2'],
        [hyp('h0', h0), hyp('h1', h1)],
        proof['conclusion'],
        proof,
    )


def valid_s1_not():
    h0 = and_(A1, A2)
    proof = and_intro(
        not_contra('l0'),
        and_intro(not_contra('l1'), assume('h0', h0)),
    )
    return plan(
        ['a0', 'a1', 'a2'],
        [hyp('h0', h0)],
        proof['conclusion'],
        proof,
    )


def valid_s2_exfalso():
    h0 = not_(A0)
    h1 = A0
    h2 = or_(A1, A2)
    false_src = not_elim(assume('h0', h0), assume('h1', h1))
    proof = and_intro(
        exfalso(false_src, and_(A1, A2)),
        and_intro(
            or_commute('h2', A1, A2, 'l0', 'l1'),
            and_intro(
                or_commute('h2', A1, A2, 'l2', 'l3'),
                or_commute('h2', A1, A2, 'l4', 'l5'),
            ),
        ),
    )
    return plan(
        ['a0', 'a1', 'a2'],
        [hyp('h0', h0), hyp('h1', h1), hyp('h2', h2)],
        proof['conclusion'],
        proof,
    )


def valid_s3_pair():
    left = valid_s1_or_and()
    right = valid_s1_or_and()

    def relabel_locals(node, offset):
        kind = node['kind']
        if kind == 'ASSUME':
            hid = node['hypothesis_id']
            if hid.startswith('l'):
                node['hypothesis_id'] = 'l' + str(int(hid[1:]) + offset)
            return
        if kind == 'OR_ELIM':
            for key in ('left_assumption', 'right_assumption'):
                ident = node[key]['id']
                node[key]['id'] = 'l' + str(int(ident[1:]) + offset)
        if kind == 'NOT_INTRO':
            ident = node['assumption']['id']
            node['assumption']['id'] = 'l' + str(int(ident[1:]) + offset)
        from phase2_stageb_schema import PROOF_CHILD_FIELDS
        for field in PROOF_CHILD_FIELDS[kind]:
            relabel_locals(node[field], offset)

    relabel_locals(right['proof'], 4)
    proof = and_intro(left['proof'], right['proof'])
    return plan(
        ['a0', 'a1', 'a2'],
        copy.deepcopy(left['hypotheses']),
        proof['conclusion'],
        proof,
    )


def valid_s4_exfalso_chain():
    source = assume('h0', false_())
    node = source
    for _ in range(22):
        node = exfalso(node, false_())
    proof = and_intro(
        node,
        and_intro(
            or_commute('h1', A0, A1, 'l0', 'l1'),
            and_elim_left(assume('h2', and_(A2, A2))),
        ),
    )
    return plan(
        ['a0', 'a1', 'a2'],
        [hyp('h0', false_()), hyp('h1', or_(A0, A1)), hyp('h2', and_(A2, A2))],
        proof['conclusion'],
        proof,
    )


def too_few_families_with_branching():
    h0 = and_(A0, A1)
    h1 = and_(A1, A2)
    h2 = and_(A2, A0)
    p1 = and_intro(
        and_elim_left(assume('h0', h0)),
        and_elim_right(assume('h0', h0)),
    )
    p2 = and_intro(
        and_elim_left(assume('h1', h1)),
        and_elim_right(assume('h1', h1)),
    )
    p3 = and_intro(
        and_elim_left(assume('h2', h2)),
        and_elim_right(assume('h2', h2)),
    )
    proof = and_intro(and_intro(p1, p2), p3)
    return plan(
        ['a0', 'a1', 'a2'],
        [hyp('h0', h0), hyp('h1', h1), hyp('h2', h2)],
        proof['conclusion'],
        proof,
    )


def three_families_without_branching():
    h0 = not_(A2)
    h1 = A2
    node = not_elim(assume('h0', h0), assume('h1', h1))
    for _ in range(5):
        node = exfalso(node, false_())
    node = exfalso(node, A0)
    proof = or_intro_left(node, A1)
    return plan(
        ['a0', 'a1', 'a2'],
        [hyp('h0', h0), hyp('h1', h1)],
        proof['conclusion'],
        proof,
    )


def hidden_only_declared_atom():
    h0 = not_(A0)
    h1 = A0
    h2 = or_(A1, A2)
    extracted = and_elim_right(
        exfalso(
            not_elim(assume('h0', h0), assume('h1', h1)),
            and_(A3, A0),
        )
    )
    proof = and_intro(
        extracted,
        and_intro(
            or_commute('h2', A1, A2, 'l0', 'l1'),
            or_commute('h2', A1, A2, 'l2', 'l3'),
        ),
    )
    return plan(
        ['a0', 'a1', 'a2', 'a3'],
        [hyp('h0', h0), hyp('h1', h1), hyp('h2', h2)],
        proof['conclusion'],
        proof,
    )


def two_atom_otherwise_valid():
    h0 = or_(A0, A1)
    h1 = and_(A0, A1)
    proof = and_intro(
        or_commute('h0', A0, A1, 'l0', 'l1'),
        and_intro(
            and_elim_left(assume('h1', h1)),
            and_intro(
                or_commute('h0', A0, A1, 'l2', 'l3'),
                and_elim_right(assume('h1', h1)),
            ),
        ),
    )
    return plan(
        ['a0', 'a1'],
        [hyp('h0', h0), hyp('h1', h1)],
        proof['conclusion'],
        proof,
    )


def seven_atom_otherwise_valid():
    h0 = or_(A0, A1)
    h1 = and_(A2, A2)
    h2 = A3
    h3 = A4
    h4 = A5
    h5 = A6
    proof = and_intro(
        and_elim_left(assume('h1', h1)),
        and_intro(
            or_commute('h0', A0, A1, 'l0', 'l1'),
            and_intro(
                assume('h2', h2),
                and_intro(
                    assume('h3', h3),
                    and_intro(assume('h4', h4), assume('h5', h5)),
                ),
            ),
        ),
    )
    return plan(
        ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'],
        [
            hyp('h0', h0), hyp('h1', h1), hyp('h2', h2),
            hyp('h3', h3), hyp('h4', h4), hyp('h5', h5),
        ],
        proof['conclusion'],
        proof,
    )


def beta_and_elim_of_intro():
    h0 = or_(A0, A1)
    h1 = and_(A2, A2)
    inner = and_elim_left(
        and_intro(
            or_commute('h0', A0, A1, 'l0', 'l1'),
            and_elim_left(assume('h1', h1)),
        )
    )
    proof = and_intro(copy.deepcopy(inner), copy.deepcopy(inner))
    # deepcopy shares local ids; relabel right copy
    def relabel(node, offset):
        kind = node['kind']
        if kind == 'ASSUME':
            hid = node['hypothesis_id']
            if hid.startswith('l'):
                node['hypothesis_id'] = 'l' + str(int(hid[1:]) + offset)
            return
        if kind == 'OR_ELIM':
            for key in ('left_assumption', 'right_assumption'):
                ident = node[key]['id']
                node[key]['id'] = 'l' + str(int(ident[1:]) + offset)
        from phase2_stageb_schema import PROOF_CHILD_FIELDS
        for field in PROOF_CHILD_FIELDS[kind]:
            relabel(node[field], offset)

    relabel(proof['right'], 2)
    return plan(
        ['a0', 'a1', 'a2'],
        [hyp('h0', h0), hyp('h1', h1)],
        proof['conclusion'],
        proof,
    )


def beta_or_elim_of_intro():
    h0 = A0
    h1 = or_(A1, A2)
    major = or_intro_left(assume('h0', A0), or_(A1, A2))
    payload = or_(or_(A1, A2), A0)
    node = or_elim(
        major,
        hyp('l0', A0),
        or_intro_right(assume('l0', A0), or_(A1, A2)),
        hyp('l1', or_(A1, A2)),
        assume('l1', or_(A1, A2)),
        payload,
    )
    # too small / maybe ill-typed: right branch assume l1 concludes or(A1,A2) not payload
    # skip this shape; pad a well-typed redex below
    proof = and_intro(
        or_elim(
            or_intro_left(assume('h0', A0), A1),
            hyp('l0', A0),
            or_intro_right(assume('l0', A0), A1),
            hyp('l1', A1),
            or_intro_left(assume('l1', A1), A0),
            or_(A1, A0),
        ),
        and_intro(
            or_commute('h1', A1, A2, 'l2', 'l3'),
            or_commute('h1', A1, A2, 'l4', 'l5'),
        ),
    )
    return plan(
        ['a0', 'a1', 'a2'],
        [hyp('h0', h0), hyp('h1', h1)],
        proof['conclusion'],
        proof,
    )


def beta_not_elim_of_intro():
    h0 = and_(A1, A2)
    redex = not_elim(not_contra('l0'), assume('h0', A0))
    # not_contra concludes not(and(a0,not a0)), not not(a0); this would be TYPE
    # Build NOT_INTRO of a0 from hyp a0 -> false, then NOT_ELIM it with a0.
    # We have h1: a0 and h2: not needed if NOT_INTRO derives not a0 from
    # assuming a0 and using h_false.
    # Simpler: hyp h_false false, NOT_INTRO assume a0, body EXFALSO? EXFALSO needs false
    # from ASSUME h_false. Then NOT_ELIM(that NOT_INTRO, assume a0) is the redex.
    h_not = not_(A0)
    h_a0 = A0
    intro = not_intro(
        hyp('l0', A0),
        not_elim(assume('h0', h_not), assume('l0', A0)),
    )
    redex = not_elim(intro, assume('h1', h_a0))
    proof = and_intro(
        exfalso(redex, and_(A1, A2)),
        and_intro(
            or_commute('h2', A1, A2, 'l1', 'l2'),
            or_commute('h2', A1, A2, 'l3', 'l4'),
        ),
    )
    return plan(
        ['a0', 'a1', 'a2'],
        [hyp('h0', h_not), hyp('h1', h_a0), hyp('h2', or_(A1, A2))],
        proof['conclusion'],
        proof,
    )


def deep_not(n):
    formula = false_()
    for _ in range(n):
        formula = not_(formula)
    return formula


VALID_PLAN_BUILDERS = (
    ('valid_s1_or_and', valid_s1_or_and),
    ('valid_s1_not', valid_s1_not),
    ('valid_s2_exfalso', valid_s2_exfalso),
    ('valid_s3_pair', valid_s3_pair),
    ('valid_s4_exfalso_chain', valid_s4_exfalso_chain),
)


class TestStageBChecker(unittest.TestCase):
    def test_checker_imports_only_l0_and_stdlib(self):
        source = (LEARNING_DIR / 'phase2_stageb_checker.py').read_text(encoding='utf-8')
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imported.add(node.module.split('.')[0])
        allowed = {
            'phase2_stageb_canonical',
            'phase2_stageb_causes',
            'phase2_stageb_render',
            'phase2_stageb_schema',
            'typing',
            'annotations',
            '__future__',
        }
        self.assertTrue(imported <= allowed, imported)
        forbidden = {
            'peano', 'torch', 'proofsearch', 'policy', 'phase2_policy',
            'phase2_search', 'phase2_root', 'phase2_isolated', 'phase2_actions',
            'phase2_spec', 'transformers', 'numpy', 'random',
        }
        self.assertTrue(imported.isdisjoint(forbidden))
        self.assertNotIn('generator', source)
        self.assertNotIn('compiler', source)
        self.assertNotIn('public_projection', source)
        self.assertNotIn('skeleton', source.lower())
        self.assertNotIn('bijection', source)

    def test_valid_plans_cover_rules_and_bands(self):
        seen_kinds = set()
        seen_bands = set()

        def walk_kinds(node):
            seen_kinds.add(node['kind'])
            from phase2_stageb_schema import PROOF_CHILD_FIELDS
            for field in PROOF_CHILD_FIELDS[node['kind']]:
                walk_kinds(node[field])

        for name, builder in VALID_PLAN_BUILDERS:
            with self.subTest(name=name):
                item = builder()
                walk_kinds(item['proof'])
                exp = expectation_for(item['proof'])
                result = check_plan(item, exp)
                self.assertTrue(result['ok'], result)
                self.assertIsNone(result['cause'])
                seen_bands.add(result['band'])
                rendered = render_sequent(
                    result['theorem']['atoms'],
                    result['theorem']['hypotheses'],
                    result['theorem']['goal'],
                )
                self.assertEqual(result['rendered_sequent'], rendered)
                self.assertEqual(result['theorem']['atoms'], item['atoms'])
                self.assertEqual(
                    result['theorem']['hypotheses'],
                    [h['formula'] for h in item['hypotheses']],
                )
        self.assertEqual(
            seen_kinds,
            {
                'ASSUME', 'AND_INTRO', 'AND_ELIM_LEFT', 'AND_ELIM_RIGHT',
                'OR_INTRO_LEFT', 'OR_INTRO_RIGHT', 'OR_ELIM',
                'NOT_INTRO', 'NOT_ELIM', 'EXFALSO',
            },
        )
        self.assertEqual(seen_bands, {'S1', 'S2', 'S3', 'S4'})

    def test_frozen_mutation_mapping_is_exact(self):
        self.assertEqual(len(MUTATION_TO_CAUSE), 12)
        self.assertEqual(MUTATION_TO_CAUSE[0][1], CAUSE_PLAN_SCHEMA_INVALID)
        self.assertEqual(MUTATION_TO_CAUSE[-1][1], CAUSE_PLAN_NON_NORMAL)

    def _mutate_cause(self, item, exp, cause):
        result = check_plan(item, exp)
        self.assertFalse(result['ok'], result)
        self.assertEqual(result['cause'], cause)
        return result

    def test_mutation_wrong_kind_key_type_string_atom_id_list(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad = copy.deepcopy(item)
        bad['proof']['kind'] = 'UNKNOWN'
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)
        bad = copy.deepcopy(item)
        bad['extra'] = 'x'
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)
        bad = copy.deepcopy(item)
        bad['atoms'] = ['a0', True, 'a2']
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)
        bad = copy.deepcopy(item)
        bad['goal']['kind'] = 'ATOM'
        bad['goal']['name'] = 'a0\n'
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)
        bad = copy.deepcopy(item)
        bad['atoms'] = ['a0', 'a2', 'a1']
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)
        bad = copy.deepcopy(item)
        bad['hypotheses'][0]['id'] = 'H0'
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)
        bad = copy.deepcopy(item)
        bad['atoms'][0] = 'b0'
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)

    def test_mutation_duplicate_or_shadowed_id(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad = copy.deepcopy(item)
        bad['hypotheses'][1]['id'] = 'h0'
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)
        bad = copy.deepcopy(item)
        bad['proof']['right']['left_assumption']['id'] = 'l0'
        bad['proof']['right']['left_branch']['source']['hypothesis_id'] = 'l0'
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)

    def test_mutation_missing_or_out_of_scope_hypothesis(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad = copy.deepcopy(item)
        bad['proof']['left']['left']['source']['hypothesis_id'] = 'h9'
        self._mutate_cause(bad, exp, CAUSE_PLAN_TYPE_INVALID)
        bad = copy.deepcopy(item)
        bad['proof']['left']['left']['source']['hypothesis_id'] = 'l0'
        self._mutate_cause(bad, exp, CAUSE_PLAN_TYPE_INVALID)

    def test_mutation_wrong_child_conclusion_or_root_goal(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad = copy.deepcopy(item)
        bad['proof']['conclusion'] = atom('a0')
        self._mutate_cause(bad, exp, CAUSE_PLAN_TYPE_INVALID)
        bad = copy.deepcopy(item)
        bad['goal'] = atom('a0')
        self._mutate_cause(bad, exp, CAUSE_PLAN_TYPE_INVALID)

    def test_mutation_wrong_discharge_formula(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad = copy.deepcopy(item)
        bad['proof']['right']['left_assumption']['formula'] = atom('a2')
        self._mutate_cause(bad, exp, CAUSE_PLAN_TYPE_INVALID)

    def test_mutation_undeclared_or_unused_atom(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad = copy.deepcopy(item)
        bad['atoms'] = ['a0', 'a1', 'a2', 'a3']
        self._mutate_cause(bad, exp, CAUSE_PLAN_CONSTRAINT_INVALID)
        xf = copy.deepcopy(valid_s2_exfalso())
        xf['proof']['left']['conclusion'] = atom('a3')
        xf['proof']['conclusion'] = and_(atom('a3'), xf['proof']['right']['conclusion'])
        xf['goal'] = copy.deepcopy(xf['proof']['conclusion'])
        self._mutate_cause(
            xf, expectation_for(xf['proof']), CAUSE_PLAN_CONSTRAINT_INVALID)

    def test_mutation_unused_global_or_local_hypothesis(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad = copy.deepcopy(item)
        bad['hypotheses'].append(hyp('h2', atom('a0')))
        self._mutate_cause(bad, exp, CAUSE_PLAN_CONSTRAINT_INVALID)
        not_item = valid_s1_not()
        not_exp = expectation_for(not_item['proof'])
        bad = copy.deepcopy(not_item)
        bad['proof']['left']['body'] = assume('h0', and_(A1, A2))
        bad['proof']['left']['conclusion'] = not_(and_(A0, not_(A0)))
        # body no longer references l0; also type-invalid because body not false.
        # Force a type-valid unused local: NOT_INTRO body EXFALSO from global false.
        # Use a dedicated fixture:
        h_false = false_()
        intro = not_intro(hyp('l0', A0), assume('h0', h_false))
        proof = and_intro(
            intro,
            and_intro(
                or_commute('h1', A1, A2, 'l1', 'l2'),
                or_commute('h1', A1, A2, 'l3', 'l4'),
            ),
        )
        unused_local = plan(
            ['a0', 'a1', 'a2'],
            [hyp('h0', h_false), hyp('h1', or_(A1, A2))],
            proof['conclusion'],
            proof,
        )
        self._mutate_cause(
            unused_local,
            expectation_for(unused_local['proof']),
            CAUSE_PLAN_CONSTRAINT_INVALID,
        )

    def test_mutation_duplicate_global_formula(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad = copy.deepcopy(item)
        bad['hypotheses'][1]['formula'] = copy.deepcopy(bad['hypotheses'][0]['formula'])
        # h1 unused shape now differs; still referenced by and_elim which needs AND
        # so this is TYPE. Make a type-valid duplicate: two AND hyps equal.
        h0 = and_(A0, A1)
        proof = and_intro(
            and_elim_left(assume('h0', h0)),
            and_intro(
                or_commute('h2', A1, A2, 'l0', 'l1'),
                or_commute('h2', A1, A2, 'l2', 'l3'),
            ),
        )
        dup = plan(
            ['a0', 'a1', 'a2'],
            [hyp('h0', h0), hyp('h1', copy.deepcopy(h0)), hyp('h2', or_(A1, A2))],
            proof['conclusion'],
            proof,
        )
        # h1 unused AND duplicate formula. First cause: unused vs duplicate.
        # Mapping: unused global -> CONSTRAINT, duplicate formula -> CONSTRAINT.
        # Check unused first in checker... we check duplicate formulas before unused.
        result = check_plan(dup, expectation_for(dup['proof']))
        self.assertFalse(result['ok'])
        self.assertEqual(result['cause'], CAUSE_PLAN_CONSTRAINT_INVALID)
        # Reference both copies so unused does not fire; only duplicate remains.
        proof2 = and_intro(
            and_elim_left(assume('h0', h0)),
            and_intro(
                and_elim_right(assume('h1', copy.deepcopy(h0))),
                and_intro(
                    or_commute('h2', A1, A2, 'l0', 'l1'),
                    or_commute('h2', A1, A2, 'l2', 'l3'),
                ),
            ),
        )
        dup2 = plan(
            ['a0', 'a1', 'a2'],
            [hyp('h0', h0), hyp('h1', copy.deepcopy(h0)), hyp('h2', or_(A1, A2))],
            proof2['conclusion'],
            proof2,
        )
        self._mutate_cause(
            dup2, expectation_for(dup2['proof']), CAUSE_PLAN_CONSTRAINT_INVALID)

    def test_mutation_formula_bound_including_free_payloads(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        huge = deep_not(24)
        src = assume('h0', A0)
        or_node = or_intro_left(src, huge)
        padded = and_intro(
            or_node,
            and_intro(
                or_commute('h1', A1, A2, 'l0', 'l1'),
                or_commute('h1', A1, A2, 'l2', 'l3'),
            ),
        )
        free_or = plan(
            ['a0', 'a1', 'a2'],
            [hyp('h0', A0), hyp('h1', or_(A1, A2))],
            padded['conclusion'],
            padded,
        )
        self._mutate_cause(
            free_or, expectation_for(free_or['proof']), CAUSE_PLAN_CONSTRAINT_INVALID)
        # EXFALSO payload.
        false_src = not_elim(assume('h0', not_(A0)), assume('h1', A0))
        xf = exfalso(false_src, huge)
        padded_x = and_intro(
            xf,
            and_intro(
                or_commute('h2', A1, A2, 'l0', 'l1'),
                or_commute('h2', A1, A2, 'l2', 'l3'),
            ),
        )
        free_x = plan(
            ['a0', 'a1', 'a2'],
            [hyp('h0', not_(A0)), hyp('h1', A0), hyp('h2', or_(A1, A2))],
            padded_x['conclusion'],
            padded_x,
        )
        self._mutate_cause(
            free_x, expectation_for(free_x['proof']), CAUSE_PLAN_CONSTRAINT_INVALID)

    def test_mutation_node_count_band_expectation_mismatch(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad_exp = copy.deepcopy(exp)
        bad_exp['node_count'] = exp['node_count'] + 1
        bad_exp['band'] = band_of_node_count(bad_exp['node_count'])
        self._mutate_cause(item, bad_exp, CAUSE_PLAN_CONSTRAINT_INVALID)

    def test_mutation_shallow_or_too_few_families_or_no_branching(self):
        h0 = and_(A0, A1)
        shallow = plan(
            ['a0', 'a1', 'a2'],
            [hyp('h0', h0), hyp('h1', A2)],
            A0,
            and_elim_left(assume('h0', h0)),
        )
        # 1 node, not in band
        exp = {
            'schema': EXPECTATION_SCHEMA_NAME,
            'node_count': 8,
            'band': 'S1',
            'families': ['AND_ELIM'],
            'max_dependency_depth': 2,
        }
        self._mutate_cause(shallow, exp, CAUSE_PLAN_CONSTRAINT_INVALID)

    def test_beta_redexes_are_plan_non_normal(self):
        and_beta = beta_and_elim_of_intro()
        self._mutate_cause(
            and_beta,
            expectation_for(and_beta['proof']),
            CAUSE_PLAN_NON_NORMAL,
        )
        or_beta = beta_or_elim_of_intro()
        self._mutate_cause(
            or_beta,
            expectation_for(or_beta['proof']),
            CAUSE_PLAN_NON_NORMAL,
        )
        not_beta = beta_not_elim_of_intro()
        self._mutate_cause(
            not_beta,
            expectation_for(not_beta['proof']),
            CAUSE_PLAN_NON_NORMAL,
        )

    def test_inference_depth_ignores_assume_edges(self):
        item = valid_s1_or_and()
        self.assertGreaterEqual(inference_depth(item['proof']), 2)
        only_assumes = and_intro(assume('h0', A0), assume('h1', A1))
        self.assertEqual(inference_depth(only_assumes), 0)
        self.assertEqual(inference_node_count(only_assumes), 1)

    def test_plan_wide_local_id_uniqueness_across_siblings(self):
        item = valid_s3_pair()
        ids = []

        def walk(node):
            kind = node['kind']
            if kind == 'OR_ELIM':
                ids.append(node['left_assumption']['id'])
                ids.append(node['right_assumption']['id'])
            if kind == 'NOT_INTRO':
                ids.append(node['assumption']['id'])
            from phase2_stageb_schema import PROOF_CHILD_FIELDS
            for field in PROOF_CHILD_FIELDS[kind]:
                walk(node[field])

        walk(item['proof'])
        self.assertEqual(len(ids), len(set(ids)))
        result = check_plan(item, expectation_for(item['proof']))
        self.assertTrue(result['ok'], result)

    def test_first_cause_schema_before_type(self):
        item = valid_s1_or_and()
        exp = expectation_for(item['proof'])
        bad = copy.deepcopy(item)
        bad['proof']['kind'] = 'NOT_A_RULE'
        bad['goal'] = atom('a0')
        self._mutate_cause(bad, exp, CAUSE_PLAN_SCHEMA_INVALID)

    def test_valid_plan_raw_hashes_are_stable(self):
        item = valid_s1_or_and()
        result = check_plan(item, expectation_for(item['proof']))
        self.assertTrue(result['ok'])
        self.assertEqual(len(canonical_hash(item)), 64)
        self.assertEqual(len(canonical_hash(result['theorem'])), 64)

    def test_isolated_too_few_families_with_branching(self):
        item = too_few_families_with_branching()
        families = used_families(item['proof'])
        self.assertEqual(families, ['AND_INTRO', 'AND_ELIM'])
        self.assertIn('AND_INTRO', families)
        self.assertEqual(inference_node_count(item['proof']), 11)
        self.assertGreaterEqual(inference_depth(item['proof']), 2)
        self._mutate_cause(
            item,
            expectation_for(item['proof']),
            CAUSE_PLAN_CONSTRAINT_INVALID,
        )

    def test_isolated_three_families_without_branching(self):
        item = three_families_without_branching()
        families = used_families(item['proof'])
        self.assertGreaterEqual(len(families), 3)
        self.assertNotIn('AND_INTRO', families)
        self.assertNotIn('OR_ELIM', families)
        self.assertEqual(inference_node_count(item['proof']), 8)
        self.assertGreaterEqual(inference_depth(item['proof']), 2)
        self._mutate_cause(
            item,
            expectation_for(item['proof']),
            CAUSE_PLAN_CONSTRAINT_INVALID,
        )

    def test_isolated_hidden_only_declared_atom(self):
        item = hidden_only_declared_atom()
        self.assertEqual(item['atoms'], ['a0', 'a1', 'a2', 'a3'])
        self.assertEqual(public_atom_names(item), {'a0', 'a1', 'a2'})
        exp = expectation_for(item['proof'])
        self.assertIn(exp['band'], {'S1', 'S2', 'S3', 'S4'})
        self.assertGreaterEqual(len(exp['families']), 3)
        self.assertTrue(
            'AND_INTRO' in exp['families'] or 'OR_ELIM' in exp['families']
        )
        self._mutate_cause(item, exp, CAUSE_PLAN_CONSTRAINT_INVALID)

    def test_malformed_expectation_is_schema_invalid(self):
        item = valid_s1_or_and()
        good = expectation_for(item['proof'])
        extra = copy.deepcopy(good)
        extra['extra'] = 1
        self._mutate_cause(item, extra, CAUSE_PLAN_SCHEMA_INVALID)
        missing = copy.deepcopy(good)
        del missing['families']
        self._mutate_cause(item, missing, CAUSE_PLAN_SCHEMA_INVALID)
        wrong_schema = copy.deepcopy(good)
        wrong_schema['schema'] = 'philosophia.stageb.plan-expectation.v0'
        self._mutate_cause(item, wrong_schema, CAUSE_PLAN_SCHEMA_INVALID)
        bad_band = copy.deepcopy(good)
        bad_band['band'] = 'S9'
        self._mutate_cause(item, bad_band, CAUSE_PLAN_SCHEMA_INVALID)
        bad_family = copy.deepcopy(good)
        bad_family['families'] = ['AND_INTRO', 'NOT_A_FAMILY']
        self._mutate_cause(item, bad_family, CAUSE_PLAN_SCHEMA_INVALID)
        duplicate = copy.deepcopy(good)
        duplicate['families'] = ['AND_INTRO', 'AND_INTRO']
        self._mutate_cause(item, duplicate, CAUSE_PLAN_SCHEMA_INVALID)
        unsorted = copy.deepcopy(good)
        unsorted['families'] = list(reversed(good['families']))
        if unsorted['families'] != good['families']:
            self._mutate_cause(item, unsorted, CAUSE_PLAN_SCHEMA_INVALID)
        else:
            unsorted['families'] = ['OR_ELIM', 'AND_INTRO']
            self._mutate_cause(item, unsorted, CAUSE_PLAN_SCHEMA_INVALID)
        bad_type = copy.deepcopy(good)
        bad_type['node_count'] = True
        self._mutate_cause(item, bad_type, CAUSE_PLAN_SCHEMA_INVALID)
        bad_list = copy.deepcopy(good)
        bad_list['families'] = tuple(good['families'])
        self._mutate_cause(item, bad_list, CAUSE_PLAN_SCHEMA_INVALID)

    def test_valid_expectation_mismatch_is_constraint_invalid(self):
        item = valid_s1_or_and()
        good = expectation_for(item['proof'])
        wrong_count = copy.deepcopy(good)
        wrong_count['node_count'] = good['node_count'] + 1
        wrong_count['band'] = band_of_node_count(wrong_count['node_count'])
        self._mutate_cause(item, wrong_count, CAUSE_PLAN_CONSTRAINT_INVALID)
        wrong_depth = copy.deepcopy(good)
        wrong_depth['max_dependency_depth'] = good['max_dependency_depth'] + 1
        self._mutate_cause(item, wrong_depth, CAUSE_PLAN_CONSTRAINT_INVALID)
        wrong_families = copy.deepcopy(good)
        wrong_families['families'] = ['AND_INTRO', 'AND_ELIM', 'EXFALSO']
        self._mutate_cause(item, wrong_families, CAUSE_PLAN_CONSTRAINT_INVALID)
        negative = copy.deepcopy(good)
        negative['max_dependency_depth'] = -1
        self._mutate_cause(item, negative, CAUSE_PLAN_CONSTRAINT_INVALID)
        unbanded = copy.deepcopy(good)
        unbanded['node_count'] = 7
        unbanded['band'] = 'S1'
        self._mutate_cause(item, unbanded, CAUSE_PLAN_CONSTRAINT_INVALID)

    def _assert_otherwise_valid_except_cardinality(self, item, declared_count):
        self.assertEqual(len(item['atoms']), declared_count)
        self.assertEqual(item['atoms'], sorted(item['atoms']))
        declared = set(item['atoms'])
        self.assertEqual(public_atom_names(item), declared)
        occurring = set()
        for formula in _walk_formulas(item):
            collect_atom_names(formula, occurring)
        self.assertTrue(occurring <= declared)
        env = {hyp_row['id']: hyp_row['formula'] for hyp_row in item['hypotheses']}
        err, derived = _type_proof(item['proof'], env)
        self.assertIsNone(err)
        self.assertTrue(formulas_equal(derived, item['goal']))
        global_formulas = [
            canonical_bytes(hyp_row['formula']) for hyp_row in item['hypotheses']
        ]
        self.assertEqual(len(global_formulas), len(set(global_formulas)))
        referenced = set()
        scoped = {}
        _collect_assume_ids(item['proof'], referenced, scoped)
        for hyp_row in item['hypotheses']:
            self.assertIn(hyp_row['id'], referenced)
        for local_id, uses in scoped.items():
            self.assertIn(local_id, uses)
        node_count = inference_node_count(item['proof'])
        self.assertIsNotNone(band_of_node_count(node_count))
        self.assertGreaterEqual(inference_depth(item['proof']), 2)
        families = used_families(item['proof'])
        self.assertGreaterEqual(len(families), 3)
        self.assertTrue('AND_INTRO' in families or 'OR_ELIM' in families)
        self.assertFalse(_has_beta_redex(item['proof']))

    def test_two_atom_cardinality_is_constraint_invalid(self):
        item = two_atom_otherwise_valid()
        self._assert_otherwise_valid_except_cardinality(item, 2)
        self._mutate_cause(
            item,
            expectation_for(item['proof']),
            CAUSE_PLAN_CONSTRAINT_INVALID,
        )

    def test_seven_atom_cardinality_is_constraint_invalid(self):
        item = seven_atom_otherwise_valid()
        self._assert_otherwise_valid_except_cardinality(item, 7)
        self._mutate_cause(
            item,
            expectation_for(item['proof']),
            CAUSE_PLAN_CONSTRAINT_INVALID,
        )


if __name__ == '__main__':
    unittest.main()
