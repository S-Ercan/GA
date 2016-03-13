import unittest

from algorithm.ga import GA
from sat.problem_generator import ProblemGenerator


class TestGA(unittest.TestCase):

    def setUp(self):
        self.max3sat = ProblemGenerator().generate_problem()

    def test_create_ga(self):
        ga = GA(self.max3sat)
        ga.run()
