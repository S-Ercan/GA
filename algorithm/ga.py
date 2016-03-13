import random
from operator import itemgetter

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
        self.p_mutation = 0.01

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
        candidate_to_fitness_mapping = {}

        for candidate in self.population:
            candidate_fitness = self.evaluate_candidate_fitness(candidate)
            candidate_to_fitness_mapping[candidate] = candidate_fitness
        candidate_to_fitness_mapping = sorted(candidate_to_fitness_mapping.items(), key=itemgetter(1), reverse=True)

        fittest_candidates = [
            k[0] for k in candidate_to_fitness_mapping[:int(len(candidate_to_fitness_mapping) / 2)]
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

        for index, parent1 in enumerate(parents[:int(len(parents) / 2)]):
            if not index % 2 == 0:
                continue

            parent2 = parents[index + 1]
            offspring = self.create_offspring(parent1, parent2)
            next_generation.extend(offspring)

        self.population = next_generation

    def create_offspring(self, parent1, parent2):
        # Get parent valuations
        parent1_valuation = parent1.valuation
        parent2_valuation = parent2.valuation
        # Create valuations for offspring
        child1_valuation = {}
        child2_valuation = {}
        # Get problem variables
        variables = list(parent1_valuation)
        # Determine crossover index
        crossover_index = random.randint(0, len(parent1.valuation) - 1)

        # Up to and including crossover_index, copy parent1 to child1 and parent2 to child2
        for i in range(crossover_index + 1):
            child1_valuation[variables[i]] = parent1_valuation[variables[i]]
            child2_valuation[variables[i]] = parent2_valuation[variables[i]]
        # From crossover_index onwards, copy parent2 to child1 and parent1 to child2
        for i in range(crossover_index + 1, len(parent1_valuation) - 1):
            child1_valuation[variables[i]] = parent2_valuation[variables[i]]
            child2_valuation[variables[i]] = parent1_valuation[variables[i]]

        # Create valuations for offspring
        child1 = Valuation(child1_valuation)
        child2 = Valuation(child2_valuation)
        # Apply mutations to offspring
        child1 = self.mutate(child1)
        child2 = self.mutate(child2)

        return [child1, child2]

    def mutate(self, candidate):
        valuation = candidate.valuation

        for variable, value in valuation.items():
            if random.uniform(0, 1) < self.p_mutation:
                valuation.set_value_for_variable(variable, not value)

        return candidate

    @property
    def max3sat(self):
        return self._max3sat

    @max3sat.setter
    def max3sat(self, max3sat):
        if not isinstance(max3sat, MAX3SAT):
            raise TypeError("'max3sat' must be a MAX3SAT instance.")
        self._max3sat = max3sat
