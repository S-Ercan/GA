from algorithm.valuation import Valuation
from sat.literal import Literal


class Clause:
    """ Represents a clause in a MAXSAT problem. """

    def __init__(self, literals):
        if not isinstance(literals, list):
            raise TypeError("'literals' must be a list.")
        if not all(isinstance(l, Literal) for l in literals):
            raise TypeError("All elements in 'literals' must be Literal instances.")

        self._literals = literals

    def is_satisfied(self, valuation):
        """
        :param valuation: truth assignment to use
        :return: True if valuation satisfies this clause, false otherwise
        """
        if not isinstance(valuation, Valuation):
            raise TypeError("'valuation' must be a Valuation instance.")

        for literal in self.literals:
            if valuation.get_value_for_literal(literal):
                return True
        return False

    @property
    def literals(self):
        return self._literals

    @literals.setter
    def literals(self, literals):
        if not isinstance(literals, list):
            raise TypeError("'literals' must be a list.")
        if not all(isinstance(l, Literal) for l in literals):
            raise TypeError("'literals' must be a list of Literal instances.")
        self._literals = literals

    def __str__(self):
        return "[{0}]".format(", ".join([literal.__str__() for literal in self.literals]))
