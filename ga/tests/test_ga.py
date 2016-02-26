import unittest

from ga.ga import GA
from sat.clause import Clause
from sat.max3sat import MAX3SAT
from sat.literal import Literal
from sat.variable import Variable


class TestGA(unittest.TestCase):

    def test_fitness_threshold_not_reached_for_one_clause_problem(self):
        self._create_one_clause_problem()
        ga = GA(self.max3sat, fitness_threshold=.75)
        iteration, solution, fitness = ga.run()

        self.assertEqual(0.5, fitness)

    def test_terminates_after_first_iteration_for_one_clause_problem(self):
        self._create_one_clause_problem()
        ga = GA(self.max3sat, fitness_threshold=.5)
        iteration, solution, fitness = ga.run()

        self.assertEqual(1, iteration)

    def test_terminates_after_max_iterations_for_one_clause_problem(self):
        self._create_one_clause_problem()
        max_iterations = 10
        ga = GA(self.max3sat, iterations=max_iterations, fitness_threshold=.75)
        iterations, solution, fitness = ga.run()

        self.assertEqual(max_iterations, iterations)

    def test_achieves_maximum_possible_fitness_for_two_clause_problem(self):
        self._create_two_clause_problem()
        ga = GA(self.max3sat, fitness_threshold=.75)
        iteration, solution, fitness = ga.run()

        self.assertEqual(0.75, fitness)

    def test_terminates_after_first_iteration_for_two_clause_problem(self):
        self._create_two_clause_problem()
        ga = GA(self.max3sat, fitness_threshold=.75)
        iteration, solution, fitness = ga.run()

        self.assertEqual(1, iteration)

    def test_terminates_after_max_iterations_for_two_clause_problem(self):
        self._create_two_clause_problem()
        max_iterations = 10
        ga = GA(self.max3sat, iterations=max_iterations, fitness_threshold=1)
        iterations, solution, fitness = ga.run()

        self.assertEqual(max_iterations, iterations)

    def _create_one_clause_problem(self):
        v1 = Variable('a')

        l1 = Literal(v1, positive=True)
        l2 = Literal(v1, positive=False)

        c1 = Clause([l1])
        c2 = Clause([l2])

        self.max3sat = MAX3SAT([v1], [c1, c2])

    def _create_two_clause_problem(self):
        v1 = Variable('a')
        v2 = Variable('b')

        l1 = Literal(v1, positive=True)
        l2 = Literal(v1, positive=False)
        l3 = Literal(v2, positive=True)
        l4 = Literal(v2, positive=False)

        c1 = Clause([l1, l3])
        c2 = Clause([l1, l4])
        c3 = Clause([l2, l3])
        c4 = Clause([l2, l4])

        self.max3sat = MAX3SAT([v1, v2], [c1, c2, c3, c4])
