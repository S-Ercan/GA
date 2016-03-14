import unittest

from algorithm.ga import GA
from algorithm.valuation import Valuation
from sat.problem_generator import ProblemGenerator
from sat.variable import Variable
from sat.literal import Literal
from sat.clause import Clause
from sat.max3sat import MAX3SAT


class TestGA(unittest.TestCase):

    def setUp(self):
        max3sat = ProblemGenerator().generate_problem()
        self.rand_ga = GA(max3sat)

    def test_ga_can_run(self):
        self.rand_ga.run()

    def test_evaluate_fitness_returns_half(self):
        v1 = Variable('a')
        c1 = Clause([Literal(v1, positive=True)])
        c2 = Clause([Literal(v1, positive=False)])
        max3sat = MAX3SAT([v1], [c1, c2])

        valuation = Valuation.init_random_from_variables([v1])

        ga = GA(max3sat)
        self.assertEqual(0.5, ga.evaluate_candidate_fitness(valuation))

    def test_evaluate_fitness_returns_one(self):
        v1 = Variable('a')
        v2 = Variable('b')
        c1 = Clause([Literal(v1, positive=True)])
        c2 = Clause([Literal(v2, positive=False)])
        max3sat = MAX3SAT([v1, v2], [c1, c2])

        valuation = Valuation({v1: True, v2: False})

        ga = GA(max3sat)
        self.assertEqual(1, ga.evaluate_candidate_fitness(valuation))

    def test_get_fitness_for_candidates_returns_list(self):
        candidate_fitnesses = self.rand_ga.get_fitness_for_candidates()

        self.assertEqual(list, type(candidate_fitnesses))

    def test_create_offspring_creates_two_children(self):
        v1 = Variable('a')
        c1 = Clause([Literal(v1)])
        max3sat = MAX3SAT([v1], [c1])

        valuation1 = Valuation.init_random_from_variables([v1])
        valuation2 = Valuation.init_random_from_variables([v1])

        ga = GA(max3sat)
        offspring = ga.create_offspring(valuation1, valuation2)
        self.assertEqual(2, len(offspring))
