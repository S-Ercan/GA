from sat.valuation import Valuation


class Chromosome:

    def __init__(self, max3sat):
        self._valuation = Valuation.init_random_from_variables(max3sat.variables)

    def get_fitness_value(self):
        pass

    def mutate(self):
        pass

    @property
    def valuation(self):
        return self._valuation

    @valuation.setter
    def valuation(self, valuation):
        self._valuation = valuation
