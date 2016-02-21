import unittest

from sat.clause import Clause
from sat.literal import Literal
from sat.variable import Variable


class TestLiteral(unittest.TestCase):

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
