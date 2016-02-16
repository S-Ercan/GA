import unittest

from sat.variable import Variable


class TestVariable(unittest.TestCase):

    def test_create_with_non_alphabetic_character_fails(self):
        self.assertRaises(TypeError, lambda l: Variable(1))

    def test_create_sets_value(self):
        v = Variable('a')
        self.assertEqual('a', v.value)
