from max3sat.Clause import Clause


class MAX3SAT:

    def __init__(self):
        self.variables = []
        self.clauses = []

    def set_variables(self, variables):
        self.variables = variables

    def set_clauses(self, clauses):
        if not isinstance(clauses, list):
            raise TypeError("'clauses' must be a list.")
        if not all(isinstance(c, Clause) for c in clauses):
            raise TypeError("All elements in 'clauses' must be Clause instances.")

        self.clauses = clauses
