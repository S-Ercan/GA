import unittest

from sat.clause import Clause
from sat.literal import Literal
from sat.max3sat import MAX3SAT
from sat.variable import Variable


class TestMAX3SAT(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable = Variable('a')
        self.literals = None

    def setUp(self):
        self.literals = [Literal(self.variable)]

    def test_create_with_invalid_variables_type_fails(self):
        self.assertRaises(TypeError, lambda l: MAX3SAT({}, [Clause(self.literals)]))

    def test_create_with_invalid_variables_fails(self):
        self.assertRaises(TypeError, lambda l: MAX3SAT([Literal(Variable('a'))], [Clause(self.literals)]))

    def test_create_with_invalid_clauses_type_fails(self):
        self.assertRaises(TypeError, lambda l: MAX3SAT(self.variables, {}))

    def test_create_with_invalid_clauses_fails(self):
        self.assertRaises(TypeError, lambda l: MAX3SAT(self.variables, [Literal(self.variable)]))
