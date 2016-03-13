from algorithm.valuation import Valuation
from sat.clause import Clause
from sat.variable import Variable


class MAX3SAT:
    """ Representation of a MAX-3SAT problem instance.
        Contains:
            - a list of variables
            - a list of clauses, which in turn contain literals
    """

    def __init__(self, variables, clauses):
        if not isinstance(variables, list):
            raise TypeError("'variables' must be a list.")
        if not all(isinstance(v, Variable) for v in variables):
            raise TypeError("All elements in 'variables' must be Variable instances.")

        if not isinstance(clauses, list):
            raise TypeError("'clauses' must be a list.")
        if not all(isinstance(c, Clause) for c in clauses):
            raise TypeError("All elements in 'clauses' must be Clause instances.")

        self._variables = variables
        self._clauses = clauses

    def get_num_satisfied_clauses(self, valuation):
        """
        :param valuation: truth assignment to use
        :return: number of clauses satisfied by the given valuation
        """
        if not isinstance(valuation, Valuation):
            raise TypeError("'valuation' must be a Valuation instance.")

        return len([c for c in self.clauses if c.is_satisfied(valuation)])

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, variables):
        self._variables = variables

    @property
    def clauses(self):
        return self._clauses

    @clauses.setter
    def clauses(self, clauses):
        self._clauses = clauses

    def __str__(self):
        return "Variables: {0};\nClauses: {1}.".format(
            ", ".join([variable.__str__() for variable in self.variables]),
            ", ".join([clause.__str__() for clause in self.clauses])
        )
