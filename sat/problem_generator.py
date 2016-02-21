import random
import string

from sat.clause import Clause
from sat.literal import Literal
from sat.max3sat import MAX3SAT
from sat.variable import Variable


class ProblemGenerator:

    def __init__(self):
        self.variables_per_clause = 3
        self.min_num_variables = 5
        self.max_num_variables = 5
        self.min_num_clauses = 5
        self.max_num_clauses = 5

        self.variables = None
        self.clauses = None

    def generate_problem(self):
        self.variables = self.generate_variables()
        self.clauses = self.generate_clauses()
        return MAX3SAT(self.variables, self.clauses)

    def generate_variables(self):
        num_variables = random.randint(self.min_num_variables, self.max_num_variables)
        variables = []

        for i in range(num_variables - 1):
            variable = Variable(random.choice(string.ascii_lowercase))
            if variable not in variables:
                variables.append(variable)

        return variables

    def generate_clauses(self):
        num_clauses = random.randint(self.min_num_clauses, self.max_num_clauses)
        clauses = []

        for i in range(num_clauses - 1):
            literals = []
            for j in range(self.variables_per_clause):
                variable = random.choice(self.variables)
                if random.randint(0, 1) == 0:
                    literal = Literal(variable, positive=True)
                else:
                    literal = Literal(variable, positive=False)
                literals.append(literal)
            clauses.append(Clause(literals))

        return clauses
