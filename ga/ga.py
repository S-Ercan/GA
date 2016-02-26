from ga.valuation import Valuation
from sat.max3sat import MAX3SAT


class GA:

    def __init__(self, max3sat):
        self._max3sat = max3sat

        self.iterations = 25
        self.population_size = 10
        self.fitness_threshold = 0.75

        self.population = []

    def run(self):
        pass

    def generate_population(self):
        for i in range(self.population_size):
            self.population.append(Valuation.init_random_from_variables(self.max3sat.variables))

    def evaluate_population_fitness(self):
        for candidate in self.population:
            self.evaluate_candidate_fitness(candidate)

    def evaluate_candidate_fitness(self, candidate):
        return self.max3sat.get_num_satisfied_clauses(candidate)

    @property
    def max3sat(self):
        return self._max3sat

    @max3sat.setter
    def max3sat(self, max3sat):
        if not isinstance(max3sat, MAX3SAT):
            raise TypeError("'max3sat' must be a MAX3SAT instance.")
        self._max3sat = max3sat
