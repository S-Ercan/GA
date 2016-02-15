from max3sat.Literal import Literal
from max3sat.Valuation import Valuation


class Clause:
    """ Represents a clause in a MAX-3SAT problem. """

    def __init__(self, literals):
        if not isinstance(literals, list):
            raise TypeError("'literals' must be a list.")
        if not all(isinstance(l, Literal) for l in literals):
            raise TypeError("All elements in 'literals' must be Literal instances.")

        self.literals = literals

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

    def __str__(self):
        return self.literals
