class Variable:

    def __init__(self, value):
        if not str.isalpha(value):
            raise TypeError("'value' must be an alphabetic character.")

        self.value = value
