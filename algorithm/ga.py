from algorithm.valuation import Valuation
from sat.max3sat import MAX3SAT


class GA:
    """ Genetic algorithm for the MAX-3SAT problem.
    """

    def __init__(self, max3sat, iterations=25, population_size=10, fitness_threshold=0.75):
        self._max3sat = max3sat

        self.iterations = iterations
        self.population_size = population_size
        self.fitness_threshold = fitness_threshold

        self.population = []

        print("Initialized GA with problem:\n{0}\n.".format(self.max3sat))

    def run(self):
        """ Works toward a solution for the given problem
            until either the fitness criterion has been met
            or the maximum number of iterations has been reached.
        :return: best solution found with its corresponding fitness measure
        """
        iteration = 0
        # solution = None
        fitness = 0

        self.generate_population()
        while fitness < self.fitness_threshold and iteration < self.iterations:
            fittest_candidates = self.get_fittest_candidates()
            self.generate_next_generation(fittest_candidates)
            iteration += 1

        # print("Terminated at iteration: {0};\nSolution: {1};\nFitness: {2}.".
        #       format(iteration, solution, fitness))

    def generate_population(self):
        """ Generates a population of random candidate solutions.
        """
        for i in range(self.population_size):
            self.population.append(Valuation.init_random_from_variables(self.max3sat.variables))

    def get_fittest_candidates(self):
        """ Determines the best solution in the current population.
        :return: best candidate solution with corresponding fitness measure
        """
        fitness_to_candidate_mapping = {}

        for candidate in self.population:
            candidate_fitness = self.evaluate_candidate_fitness(candidate)
            fitness_to_candidate_mapping[candidate_fitness] = candidate

        fittest_candidates = [
            fitness_to_candidate_mapping[k]
            for k in sorted(fitness_to_candidate_mapping)[:int(len(fitness_to_candidate_mapping) / 2)]
        ]

        return fittest_candidates

    def evaluate_candidate_fitness(self, candidate):
        """
        :param candidate: solution to evaluate
        :return: fitness of candidate
        """
        return self.max3sat.get_num_satisfied_clauses(candidate) / len(self.max3sat.clauses)

    def generate_next_generation(self, parents):
        next_generation = []

        for index, parent1 in enumerate(parents[:len(parents) / 2]):
            if not index % 2 == 0:
                continue

            parent2 = parents[index + 1]
            offspring = self.create_offspring(parent1, parent2)
            next_generation.extend(offspring)

        self.population = next_generation

    def create_offspring(self, parent1, parent2):
        return [parent1, parent2]

    @property
    def max3sat(self):
        return self._max3sat

    @max3sat.setter
    def max3sat(self, max3sat):
        if not isinstance(max3sat, MAX3SAT):
            raise TypeError("'max3sat' must be a MAX3SAT instance.")
        self._max3sat = max3sat
