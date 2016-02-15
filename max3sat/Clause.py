from max3sat.Literal import Literal


class Clause:
    """ Represents a clause in a MAX-3SAT problem. """

    def __init__(self, literals):
        if not isinstance(literals, list):
            raise TypeError("'literals' must be a list.")
        if not all(isinstance(l, Literal) for l in literals):
            raise TypeError("All elements in 'literals' must be Literal instances.")

        self.literals = literals

    def is_satisfied(self, truth_assignment):
        pass
