import unittest

from sat.literal import Literal
from sat.valuation import Valuation
from sat.variable import Variable


class TestValuation(unittest.TestCase):

    def setUp(self):
        self.variable = Variable('a')
        self.variables = [self.variable, Variable('b'), Variable('c')]

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

    def test_get_value_for_variable_returns_correct_value(self):
        value = False
        mapping = {self.variable: value}
        v = Valuation(mapping)

        self.assertEqual(value, v.get_value_for_variable(self.variable))

    def test_set_value_for_variable_sets_value(self):
        mapping = {self.variable: False}
        v = Valuation(mapping)

        v.set_value_for_variable(self.variable, True)
        self.assertEqual(True, v.get_value_for_variable(self.variable))

    def test_get_value_for_literal_returns_correct_value(self):
        value = False
        mapping = {self.variable: value}
        v = Valuation(mapping)

        self.assertEqual(value, v.get_value_for_literal(Literal(self.variable, positive=True)))

    def test_get_value_for_negated_literal_returns_correct_value(self):
        value = False
        mapping = {self.variable: value}
        v = Valuation(mapping)

        self.assertEqual(not value, v.get_value_for_literal(Literal(self.variable, positive=False)))

    def test_set_value_for_literal_sets_value(self):
        mapping = {self.variable: False}
        v = Valuation(mapping)

        l = Literal(self.variable)
        v.set_value_for_literal(l, True)
        self.assertEqual(True, v.get_value_for_literal(l))

    def test_init_random_creates_valuation_of_correct_length(self):
        v = Valuation.init_random_from_variables(self.variables)
        self.assertEqual(len(self.variables), len(v.valuation))

    def test_init_random_creates_valuation_with_bools(self):
        v = Valuation.init_random_from_variables(self.variables)
        self.assertTrue(all(isinstance(k, bool) for k in v.valuation.values()))
