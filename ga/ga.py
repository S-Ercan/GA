from ga.valuation import Valuation
from sat.max3sat import MAX3SAT


class GA:

    def __init__(self, max3sat, iterations=25, population_size=10, fitness_threshold=0.75):
        self._max3sat = max3sat

        self.iterations = iterations
        self.population_size = population_size
        self.fitness_threshold = fitness_threshold

        self.population = []

        print("Initialized GA with problem:\n{0}\n.".format(self.max3sat))

    def run(self):
        iteration = 0
        solution = None
        fitness = 0
        while fitness < self.fitness_threshold and iteration < self.iterations:
            self.generate_population()
            solution, fitness = self.evaluate_population_fitness()
            iteration += 1

        print("Terminated at iteration: {0};\nSolution: {1};\nFitness: {2}.".
              format(iteration, solution, fitness))

    def generate_population(self):
        for i in range(self.population_size):
            self.population.append(Valuation.init_random_from_variables(self.max3sat.variables))

    def evaluate_population_fitness(self):
        fittest_candidate = None
        highest_fitness = 0

        for candidate in self.population:
            candidate_fitness = self.evaluate_candidate_fitness(candidate)
            if candidate_fitness > highest_fitness:
                highest_fitness = candidate_fitness
                fittest_candidate = candidate

        return fittest_candidate, highest_fitness

    def evaluate_candidate_fitness(self, candidate):
        return self.max3sat.get_num_satisfied_clauses(candidate) / len(self.max3sat.clauses)

    @property
    def max3sat(self):
        return self._max3sat

    @max3sat.setter
    def max3sat(self, max3sat):
        if not isinstance(max3sat, MAX3SAT):
            raise TypeError("'max3sat' must be a MAX3SAT instance.")
        self._max3sat = max3sat
