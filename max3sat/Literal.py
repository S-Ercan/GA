from max3sat.Variable import Variable


class Literal:

    def __init__(self, positive, variable):
        if not isinstance(positive, bool):
            raise TypeError("'positive' must be a boolean.")
        if not isinstance(variable, Variable):
            raise TypeError("'variable' must be a Variable instance.")

        self.positive = positive
        self.variable = variable
