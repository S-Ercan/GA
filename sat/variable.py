class Variable:

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

    def __str__(self):
        return self.value
