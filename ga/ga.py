from ga.valuation import Valuation
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
        :return:
            - number of iterations executed
            - best solution found
            - fitness of best solution
        """
        iteration = 0
        solution = None
        fitness = 0

        while fitness < self.fitness_threshold and iteration < self.iterations:
            self.create_next_generation()
            solution, fitness = self.evaluate_population_fitness()
            iteration += 1

        print("Terminated at iteration: {0};\nSolution: {1};\nFitness: {2}.".
              format(iteration, solution, fitness))
        return iteration, solution, fitness

    def create_next_generation(self):
        """ Generates a population of candidate solutions if it doesn't exist,
            or evolves the current population.
        """
        if not self.population:
            self.generate_population()
        else:
            self.evolve_population()

    def generate_population(self):
        """ Generates a population of random candidate solutions.
        """
        for i in range(self.population_size):
            self.population.append(Valuation.init_random_from_variables(self.max3sat.variables))

    def evolve_population(self):
        """ Evolves the current population of candidate solutions.
        """
        for candidate in self.population:
            candidate.change_value_for_random_variable()

    def evaluate_population_fitness(self):
        """ Determines the best solution in the current population.
        :return: best candidate solution with corresponding fitness measure
        """
        fittest_candidate = None
        highest_fitness = 0

        for candidate in self.population:
            candidate_fitness = self.evaluate_candidate_fitness(candidate)
            if candidate_fitness > highest_fitness:
                highest_fitness = candidate_fitness
                fittest_candidate = candidate

        return fittest_candidate, highest_fitness

    def evaluate_candidate_fitness(self, candidate):
        """
        :param candidate: solution to evaluate
        :return: fitness of candidate
        """
        return self.max3sat.get_num_satisfied_clauses(candidate) / len(self.max3sat.clauses)

    @property
    def max3sat(self):
        return self._max3sat

    @max3sat.setter
    def max3sat(self, max3sat):
        if not isinstance(max3sat, MAX3SAT):
            raise TypeError("'max3sat' must be a MAX3SAT instance.")
        self._max3sat = max3sat
