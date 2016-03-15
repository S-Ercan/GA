class Variable:
    """ Represents a variable in a MAXSAT problem.
    """

    def __init__(self, value):
        if not str.isalpha(value):
            raise TypeError("'value' must be an alphabetic character.")

        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.value < other.value
        else:
            raise TypeError("Cannot compare a Variable instance to an instance of different type.")

    def __str__(self):
        return self.value
