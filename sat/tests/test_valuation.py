import unittest

from sat.literal import Literal
from sat.valuation import Valuation
from sat.variable import Variable


class TestValuation(unittest.TestCase):

    def test_create_without_argument_fails(self):
        self.assertRaises(TypeError, lambda l: Valuation())

    def test_create_with_invalid_argument_type_fails(self):
        self.assertRaises(TypeError, lambda l: Valuation([]))

    def test_create_with_invalid_key_fails(self):
        self.assertRaises(TypeError, lambda l: Valuation({'a': True}))

    def test_create_with_invalid_value_fails(self):
        self.assertRaises(TypeError, lambda l: Valuation({Variable('a'): 1}))

    def test_create_with_variables_creates_valuation(self):
        mapping = {Variable('a'): False}
        v = Valuation(mapping)
        self.assertEqual(mapping, v.valuation)

    def test_get_value_for_literal_returns_correct_value(self):
        variable = Variable('a')
        value = False
        mapping = {variable: value}
        v = Valuation(mapping)

        self.assertEqual(value, v.get_value_for_literal(Literal(variable, positive=True)))

    def test_get_value_for_negated_literal_returns_correct_value(self):
        variable = Variable('a')
        value = False
        mapping = {variable: value}
        v = Valuation(mapping)

        self.assertEqual(not value, v.get_value_for_literal(Literal(variable, positive=False)))

    def test_set_value_for_literal_returns_correct_value(self):
        variable = Variable('a')
        mapping = {variable: False}
        v = Valuation(mapping)

        l = Literal(variable)
        v.set_value_for_literal(l, True)
        self.assertEqual(True, v.get_value_for_literal(l))
