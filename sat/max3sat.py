from sat.clause import Clause
from sat.variable import Variable


class MAX3SAT:

    def __init__(self, variables, clauses):
        if not isinstance(variables, list):
            raise TypeError("'variables' must be a list.")
        if not all(isinstance(v, Variable) for v in variables):
            raise TypeError("All elements in 'variables' must be Variable instances.")

        if not isinstance(clauses, list):
            raise TypeError("'clauses' must be a list.")
        if not all(isinstance(c, Clause) for c in clauses):
            raise TypeError("All elements in 'clauses' must be Clause instances.")

        self.variables = variables
        self.clauses = clauses

    def __str__(self):
        return ""
