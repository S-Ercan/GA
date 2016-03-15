import random
from operator import itemgetter

from algorithm.valuation import Valuation
from sat.maxsat import MAXSAT


class GA:
    """ Genetic algorithm for the MAXSAT problem.
    """

    def __init__(self, maxsat, max_iterations=25, population_size=16, fitness_threshold=0.75):
        """
        Creates a genetic algorithm instance for the given MAXSAT problem.
        :param maxsat:
                MAXSAT problem instance to solve
        :param max_iterations:
                maximum number of iterations to execute before termination
        :param population_size:
                size of candidate solution pool to maintain during execution
        :param fitness_threshold:
                fitness value that, if reached during execution,
                is considered sufficient and allows termination
        """
        if not isinstance(maxsat, MAXSAT):
            raise TypeError("'maxsat' must be an instance of MAXSAT.")

        self._maxsat = maxsat
        self._population = []

        self.max_iterations = max_iterations
        self.population_size = population_size
        self.fitness_threshold = fitness_threshold
        self.p_mutation = 0.01

        print("Initialized GA with problem:\n{0}\n.".format(self.maxsat))

    def run(self):
        """ Works toward a solution for the given problem until either the fitness criterion has been met
            or the maximum number of iterations has been reached.
            :return:    tuple containing the best solution,
                        its corresponding fitness value,
                        and the number of iterations executed
        """
        iteration = 0
        solution = None
        fitness = 0

        self.population = self.generate_population()
        while fitness < self.fitness_threshold and iteration < self.max_iterations:
            candidate_fitnesses = self.get_fitness_for_candidates()

            fittest_candidate = candidate_fitnesses[0]
            solution = fittest_candidate[0]
            fitness = fittest_candidate[1]

            self.population = self.generate_next_generation(candidate_fitnesses)
            iteration += 1

        print("Terminated at iteration: {0};\nSolution: {1};\nFitness: {2}.".format(iteration, solution, fitness))
        return solution, fitness, iteration

    def generate_population(self):
        """ Generates a population of random candidate solutions.
            :return: list of 'self.population_size' amount of Valuation instances
        """
        population = []
        for i in range(self.population_size):
            population.append(Valuation.init_random_from_variables(self.maxsat.variables))
        return population

    def get_fitness_for_candidates(self):
        """ Determines the fitness of each candidate solution present in self.population.
        :return: "Valuation -> fitness" mapping, sorted in descending order on fitness.
        """
        candidate_to_fitness_mapping = {}

        for candidate in self.population:
            candidate_fitness = self.evaluate_candidate_fitness(candidate)
            candidate_to_fitness_mapping[candidate] = candidate_fitness
        candidate_to_fitness_mapping = sorted(candidate_to_fitness_mapping.items(), key=itemgetter(1), reverse=True)

        return candidate_to_fitness_mapping

    def evaluate_candidate_fitness(self, candidate):
        """
        :param candidate: solution to evaluate
        :return: fitness of candidate
        """
        if not isinstance(candidate, Valuation):
            raise TypeError("'candidate' must be a Valuation instance.")
        return self.maxsat.get_num_satisfied_clauses(candidate) / len(self.maxsat.clauses)

    def generate_next_generation(self, population):
        """
        Given a list of candidate solution with corresponding fitness values, creates the next generation
        of candidate solutions by recombining pairs of candidates in 'population'.
        Candidates are selected using the stochastic acceptance method, where the probability of a candidate
        for being selected depends on its fitness.

        :param population: list of (Valuation, fitness) tuples, sorted in descending order on fitness
        :return: list of Valuation instances
        """
        if not isinstance(population, list):
            raise TypeError("'population' must be a list.")

        next_generation = []
        max_fitness = population[0][1]

        parent1 = None
        parent2 = None
        while len(next_generation) < self.population_size:
            while parent1 is None:
                parent1_candidate = random.choice(population)
                if random.randrange(0, 1) < (parent1_candidate[1] / max_fitness):
                    parent1 = parent1_candidate[0]

            while parent2 is None:
                parent2_candidate = random.choice(population)
                if random.randrange(0, 1) < (parent2_candidate[1] / max_fitness):
                    parent2 = parent2_candidate[0]

            next_generation.extend([parent1, parent2])
            parent1 = None
            parent2 = None

        return next_generation

    def create_offspring(self, parent1, parent2):
        """
        Recombines parent1 and parent2 to create two children.
        First, a crossover point is selected randomly.
        Then, child1 is created by copying values from parent1 up to and including the crossover point,
        and then by copying values from parent2 after the crossover point.
        Child2 is created in the opposite way by first copying from parent2 and then from parent1.

        :param parent1: first parent of offspring to be created
        :param parent2: second parent of offspring to be created
        :return: list of Valuation instances generated by recombining parent1 and parent2
        """
        if not isinstance(parent1, Valuation) and isinstance(parent2, Valuation):
            raise TypeError("'parent1' and 'parent'2 must be Valuation instances.")

        # Create valuations for offspring
        child1_valuation = {}
        child2_valuation = {}
        # Get problem variables
        variables = list(self.maxsat.variables)
        # Randomly pick crossover index
        crossover_index = random.randint(0, len(variables) - 1)

        # Up to and including crossover_index, copy parent1 to child1 and parent2 to child2
        for i in range(crossover_index + 1):
            child1_valuation[variables[i]] = parent1.get_value_for_variable(variables[i])
            child2_valuation[variables[i]] = parent2.get_value_for_variable(variables[i])
        # After crossover_index, copy parent2 to child1 and parent1 to child2
        for i in range(crossover_index + 1, len(variables)):
            child1_valuation[variables[i]] = parent2.get_value_for_variable(variables[i])
            child2_valuation[variables[i]] = parent1.get_value_for_variable(variables[i])

        # Create valuations for offspring
        child1 = Valuation(child1_valuation)
        child2 = Valuation(child2_valuation)
        # Mutate offspring
        child1 = self.mutate(child1)
        child2 = self.mutate(child2)

        return [child1, child2]

    def mutate(self, candidate):
        """
        Flips the value for each variable in the given Valuation instance with probability self.p_mutation.
        :param candidate: Valuation instance to mutate
        :return: updated Valuation instance
        """
        if not isinstance(candidate, Valuation):
            raise TypeError("'candidate' must be a Valuation instance.")

        valuation = candidate.valuation

        for variable, value in valuation.items():
            if random.uniform(0, 1) < self.p_mutation:
                candidate.set_value_for_variable(variable, not value)

        return candidate

    @property
    def maxsat(self):
        return self._maxsat

    @maxsat.setter
    def maxsat(self, maxsat):
        if not isinstance(maxsat, MAXSAT):
            raise TypeError("'maxsat' must be a maxsat instance.")
        self._maxsat = maxsat

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        if not isinstance(population, list):
            raise TypeError("'population' must be a maxsat instance.")
        if not all(isinstance(p, Valuation) for p in population):
            raise TypeError("'population' must be a list of Valuation instances.")
        self._population = population
