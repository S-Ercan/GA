import unittest

from algorithm.valuation import Valuation
from sat.clause import Clause
from sat.literal import Literal
from sat.maxsat import MAXSAT
from sat.variable import Variable


class TestMAXSAT(unittest.TestCase):

    def setUp(self):
        self.v1 = Variable('a')
        self.v2 = Variable('b')
        self.variables = [self.v1, self.v2]

        self.l1 = Literal(self.v1, positive=True)
        self.l2 = Literal(self.v2, positive=False)
        self.literals = [self.l1, self.l2]

        self.c1 = Clause([self.l1])
        self.c2 = Clause([self.l2])
        self.clauses = [self.c1, self.c2]

        self.m = MAXSAT(self.variables, self.clauses)

    def test_create_with_invalid_variables_type_fails(self):
        self.assertRaises(TypeError, lambda l: MAXSAT({}, self.clauses))

    def test_create_with_invalid_variables_fails(self):
        self.assertRaises(TypeError, lambda l: MAXSAT([self.l1], self.clauses))

    def test_create_with_invalid_clauses_type_fails(self):
        self.assertRaises(TypeError, lambda l: MAXSAT(self.variables, {}))

    def test_create_with_invalid_clauses_fails(self):
        self.assertRaises(TypeError, lambda l: MAXSAT(self.variables, [self.l1]))

    def test_create_sets_variables(self):
        self.assertEqual(self.variables, self.m.variables)

    def test_create_sets_clauses(self):
        self.assertEqual(self.clauses, self.m.clauses)

    def test_invalid_valuation_satisfies_zero_clauses(self):
        v = Valuation({self.v1: False, self.v2: True})
        self.assertEquals(0, self.m.get_num_satisfied_clauses(v))

    def test_valid_valuation_satisfies_one_clause(self):
        v = Valuation({self.v1: True, self.v2: True})
        self.assertEqual(1, self.m.get_num_satisfied_clauses(v))

    def test_valid_valuation_satisfies_all_clauses(self):
        v = Valuation({self.v1: True, self.v2: False})
        self.assertEqual(2, self.m.get_num_satisfied_clauses(v))
