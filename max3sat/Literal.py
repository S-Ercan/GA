from max3sat.Variable import Variable


class Literal:

    def __init__(self, variable, positive=True):
        if not isinstance(positive, bool):
            raise TypeError("'positive' must be a boolean.")
        if not isinstance(variable, Variable):
            raise TypeError("'variable' must be a Variable instance.")

        self.positive = positive
        self.variable = variable

    def get_variable(self):
        return self.variable

    @property
    def is_positive(self):
        return self.positive

    def __str__(self):
        return self.get_variable() if self.is_positive else ""
