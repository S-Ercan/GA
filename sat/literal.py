from sat.variable import Variable


class Literal:

    def __init__(self, variable, positive=True):
        if not isinstance(positive, bool):
            raise TypeError("'positive' must be a boolean.")
        if not isinstance(variable, Variable):
            raise TypeError("'variable' must be a Variable instance.")

        self._positive = positive
        self._variable = variable

    @property
    def positive(self):
        return self._positive

    @positive.setter
    def positive(self, positive):
        self._positive = positive

    @property
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, variable):
        self._variable = variable

    def __str__(self):
        return self.variable if self.positive else ""
