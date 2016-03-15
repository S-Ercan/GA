import unittest

from algorithm.ga import GA
from algorithm.valuation import Valuation
from sat.problem_generator import ProblemGenerator
from sat.variable import Variable
from sat.literal import Literal
from sat.clause import Clause
from sat.maxsat import MAXSAT


class TestGA(unittest.TestCase):

    def setUp(self):
        self.rand_maxsat = ProblemGenerator().generate_problem()
        self.rand_ga = GA(self.rand_maxsat)

    def test_create_ga_without_problem_fails(self):
        self.assertRaises(TypeError, lambda l: GA())

    def test_ga_achieves_fitness_of_half(self):
        v1 = Variable('a')
        c1 = Clause([Literal(v1, positive=True)])
        c2 = Clause([Literal(v1, positive=False)])
        maxsat = MAXSAT([v1], [c1, c2])

        ga = GA(maxsat)
        _, fitness, _ = ga.run()

        self.assertEqual(0.5, fitness)

    def test_ga_achieves_fitness_of_one(self):
        v1 = Variable('a')
        c1 = Clause([Literal(v1)])
        maxsat = MAXSAT([v1], [c1])

        ga = GA(maxsat)
        _, fitness, _ = ga.run()

        self.assertEqual(1, fitness)

    def test_ga_uses_all_iterations_for_unsatisfiable_problem_if_below_threshold(self):
        v1 = Variable('a')
        c1 = Clause([Literal(v1, positive=True)])
        c2 = Clause([Literal(v1, positive=False)])
        maxsat = MAXSAT([v1], [c1, c2])

        ga = GA(maxsat)
        _, _, iteration = ga.run()
        self.assertEqual(iteration, ga.max_iterations)

    def test_ga_uses_one_iteration_for_unsatisfiable_problem_if_not_below_threshold(self):
        v1 = Variable('a')
        c1 = Clause([Literal(v1, positive=True)])
        c2 = Clause([Literal(v1, positive=False)])
        maxsat = MAXSAT([v1], [c1, c2])

        ga = GA(maxsat, fitness_threshold=0.5)
        _, _, iteration = ga.run()
        self.assertEqual(1, iteration)

    def test_ga_uses_one_iteration_for_trivially_satisfiable_problem(self):
        v1 = Variable('a')
        c1 = Clause([Literal(v1)])
        maxsat = MAXSAT([v1], [c1])

        ga = GA(maxsat)
        _, _, iteration = ga.run()
        self.assertEqual(1, iteration)

    def test_generate_population_returns_list(self):
        population = self.rand_ga.generate_population()
        self.assertTrue(isinstance(population, list))

    def test_generate_population_generates_population_of_correct_size(self):
        population_size = 32
        ga = GA(self.rand_maxsat, population_size=population_size)
        population = ga.generate_population()
        self.assertEqual(population_size, len(population))

    def test_generate_population_generates_population_of_valuation_instances(self):
        population = self.rand_ga.generate_population()
        self.assertTrue(all(isinstance(p, Valuation) for p in population))

    def test_get_candidate_fitness_returns_half(self):
        v1 = Variable('a')
        c1 = Clause([Literal(v1, positive=True)])
        c2 = Clause([Literal(v1, positive=False)])
        maxsat = MAXSAT([v1], [c1, c2])

        valuation = Valuation.init_random_from_variables([v1])

        ga = GA(maxsat)
        self.assertEqual(0.5, ga.get_candidate_fitness(valuation))

    def test_get_candidate_fitness_returns_one(self):
        v1 = Variable('a')
        v2 = Variable('b')
        c1 = Clause([Literal(v1, positive=True)])
        c2 = Clause([Literal(v2, positive=False)])
        maxsat = MAXSAT([v1, v2], [c1, c2])

        valuation = Valuation({v1: True, v2: False})

        ga = GA(maxsat)
        self.assertEqual(1, ga.get_candidate_fitness(valuation))

    def test_get_population_fitness_returns_list(self):
        population = self.rand_ga.generate_population()
        self.rand_ga.population = population
        candidate_fitnesses = self.rand_ga.get_population_fitness()

        self.assertEqual(list, type(candidate_fitnesses))

    def test_get_population_fitness_returns_list_containing_valuations(self):
        population = self.rand_ga.generate_population()
        self.rand_ga.population = population
        candidate_fitnesses = self.rand_ga.get_population_fitness()

        self.assertTrue(all(isinstance(k[0], Valuation) for k in candidate_fitnesses))

    def test_get_population_fitness_returns_list_containing_floats(self):
        population = self.rand_ga.generate_population()
        self.rand_ga.population = population
        candidate_fitnesses = self.rand_ga.get_population_fitness()

        self.assertTrue(all(isinstance(k[1], float) for k in candidate_fitnesses))

    def test_create_offspring_creates_two_children(self):
        valuation1 = Valuation.init_random_from_variables(self.rand_maxsat.variables)
        valuation2 = Valuation.init_random_from_variables(self.rand_maxsat.variables)

        offspring = self.rand_ga.create_offspring(valuation1, valuation2)
        self.assertEqual(2, len(offspring))

    def test_create_offspring_creates_first_child_correctly_until_crossover_point(self):
        variables = self.rand_maxsat.variables
        crossover_index = int(len(variables) / 2)
        valuation1 = Valuation.init_random_from_variables(variables)
        valuation2 = Valuation.init_random_from_variables(variables)

        offspring = self.rand_ga.create_offspring(valuation1, valuation2, crossover_index=crossover_index)
        child1 = offspring[0]

        self.assertTrue(
            all(child1.get_value_for_variable(v) == valuation1.get_value_for_variable(v)
                for v in variables[:crossover_index + 1])
        )

    def test_create_offspring_creates_first_child_correctly_after_crossover_point(self):
        variables = self.rand_maxsat.variables
        crossover_index = int(len(variables) / 2)
        valuation1 = Valuation.init_random_from_variables(variables)
        valuation2 = Valuation.init_random_from_variables(variables)

        offspring = self.rand_ga.create_offspring(valuation1, valuation2, crossover_index=crossover_index)
        child1 = offspring[0]

        self.assertTrue(
            all(child1.get_value_for_variable(v) == valuation2.get_value_for_variable(v)
                for v in variables[crossover_index + 1:])
        )

    def test_create_offspring_creates_second_child_correctly_until_crossover_point(self):
        variables = self.rand_maxsat.variables
        crossover_index = int(len(variables) / 2)
        valuation1 = Valuation.init_random_from_variables(variables)
        valuation2 = Valuation.init_random_from_variables(variables)

        offspring = self.rand_ga.create_offspring(valuation1, valuation2, crossover_index=crossover_index)
        child2 = offspring[1]

        self.assertTrue(
            all(child2.get_value_for_variable(v) == valuation2.get_value_for_variable(v)
                for v in variables[:crossover_index + 1])
        )

    def test_create_offspring_creates_second_child_correctly_after_crossover_point(self):
        variables = self.rand_maxsat.variables
        crossover_index = int(len(variables) / 2)
        valuation1 = Valuation.init_random_from_variables(variables)
        valuation2 = Valuation.init_random_from_variables(variables)

        offspring = self.rand_ga.create_offspring(valuation1, valuation2, crossover_index=crossover_index)
        child2 = offspring[1]

        self.assertTrue(
            all(child2.get_value_for_variable(v) == valuation1.get_value_for_variable(v)
                for v in variables[crossover_index + 1:])
        )
