import random

from sat.literal import Literal
from sat.variable import Variable


class Valuation:
    """ Contains a 'Variable -> bool' mapping, representing a truth assignment.
    """

    def __init__(self, valuation):
        if not isinstance(valuation, dict):
            raise TypeError("'variables' must be a dict.")
        if not all(isinstance(k, Variable) for k in valuation.keys()):
            raise TypeError("The keys of 'variables' must be Variable instances.")
        if not all(isinstance(v, bool) for v in valuation.values()):
            raise TypeError("The values of 'variables' must be of type bool.")

        self._valuation = valuation

    @classmethod
    def init_random_from_variables(cls, variables):
        if not isinstance(variables, list):
            raise TypeError("'variables' must be a list.")
        if not all(isinstance(v, Variable) for v in variables):
            raise TypeError("'All elements of 'variables' must be Variable instances.'")

        valuation = {v: bool(random.getrandbits(1)) for v in variables}
        return cls(valuation)

    def get_value_for_literal(self, literal):
        """
        :param literal: literal to get truth value for
        :return: truth value for literal
        """
        if not isinstance(literal, Literal):
            raise TypeError("'variable' must be a Literal instance.")

        value = self.valuation.get(literal.variable)
        if not literal.positive:
            value = not value
        return value

    def set_value_for_literal(self, literal, value):
        if not isinstance(literal, Literal):
            raise TypeError("'literal' must be a Literal instance.")
        if not isinstance(value, bool):
            raise TypeError("'value' must be a bool.")

        self.valuation[literal.variable] = value

    @property
    def valuation(self):
        return self._valuation

    @valuation.setter
    def valuation(self, valuation):
        self._valuation = valuation
