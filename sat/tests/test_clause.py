import unittest

from ga.valuation import Valuation
from sat.clause import Clause
from sat.literal import Literal
from sat.variable import Variable


class TestClause(unittest.TestCase):

    def test_create_without_argument_fails(self):
        self.assertRaises(TypeError, lambda l: Clause())

    def test_create_with_invalid_argument_type_fails(self):
        self.assertRaises(TypeError, lambda l: Clause({}))

    def test_create_with_invalid_argument_fails(self):
        self.assertRaises(TypeError, lambda l: Clause([Variable('a')]))

    def test_create_with_valid_argument_sets_literals(self):
        literals = [Literal(Variable('a'), positive=False)]
        c = Clause(literals)
        self.assertEqual(literals, c.literals)

    def test_is_satisfied_with_invalid_argument_type_fails(self):
        c = Clause([Literal(Variable('a'))])
        self.assertRaises(TypeError, lambda l: c.is_satisfied({}))

    def test_invalid_valuation_does_not_satisfy(self):
        variable = Variable('a')
        v = Valuation({variable: False})

        c = Clause([Literal(variable)])
        self.assertFalse(c.is_satisfied(v))

    def test_valid_valuation_satisfies(self):
        variable = Variable('a')
        mapping = {variable: True}
        v = Valuation(mapping)

        c = Clause([Literal(variable)])
        self.assertTrue(c.is_satisfied(v))
