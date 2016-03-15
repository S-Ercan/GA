import unittest

from sat.literal import Literal
from sat.variable import Variable


class TestLiteral(unittest.TestCase):

    def test_create_without_variable_fails(self):
        self.assertRaises(TypeError, lambda l: Literal('a'))

    def test_create_without_boolean_fails(self):
        self.assertRaises(TypeError, lambda l: Literal(Variable('a'), positive=1))

    def test_create_sets_variable(self):
        v = Variable('a')
        l = Literal(v)
        self.assertEqual(v, l.variable)

    def test_create_with_positive_sets_positive(self):
        v = Variable('a')
        p = False
        l = Literal(v, positive=p)
        self.assertEqual(p, l.positive)

    def test_create_without_positive_sets_positive_to_true(self):
        l = Literal(Variable('a'))
        self.assertEqual(True, l.positive)
