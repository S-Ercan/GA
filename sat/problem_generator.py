import random
import string

from sat.clause import Clause
from sat.literal import Literal
from sat.maxsat import MAXSAT
from sat.variable import Variable


class ProblemGenerator:
    """ Randomly generates MAXSAT problem instances.
    """

    def __init__(self):
        self.max_variables_per_clause = 3
        self.min_num_variables = 5
        self.max_num_variables = 5
        self.min_num_clauses = 5
        self.max_num_clauses = 5

        self.variables = None
        self.clauses = None

    def generate_problem(self):
        # todo: prevent duplicate clauses
        self.variables = self.generate_variables()
        self.clauses = self.generate_clauses()
        return MAXSAT(self.variables, self.clauses)

    def generate_variables(self):
        num_variables = random.randint(self.min_num_variables, self.max_num_variables)
        variables = []

        for i in range(num_variables):
            variable = Variable(string.ascii_lowercase[i])
            if variable not in variables:
                variables.append(variable)

        return variables

    def generate_clauses(self):
        num_clauses = random.randint(self.min_num_clauses, self.max_num_clauses)
        clauses = []

        for i in range(num_clauses):
            variables = []
            literals = []
            for j in range(self.max_variables_per_clause):
                # Choose a random variable to include in clause
                variable = random.choice([v for v in self.variables if v not in variables])
                # Randomly determine whether to include variable
                # as a positive or negative literal in clause
                if random.randint(0, 1) == 0:
                    literal = Literal(variable, positive=True)
                else:
                    literal = Literal(variable, positive=False)

                variables.append(variable)
                literals.append(literal)
            clauses.append(Clause(literals))

        return clauses
