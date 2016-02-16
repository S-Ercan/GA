import random

from sat.max3sat import MAX3SAT


class ProblemGenerator:

    def generate_problem(self):
        variables = self.generate_variables()
        clauses = self.generate_clauses()

        max3sat = MAX3SAT(variables, clauses)

    def generate_variables(self):
        variables = []
        num_variables = random.randint(1, 5)
        for i in range(num_variables - 1):
            pass
        return variables

    def generate_clauses(self):
        clauses = []
        num_clauses = random.randint(1, 5)
        for i in range(num_clauses - 1):
            pass
        return clauses
