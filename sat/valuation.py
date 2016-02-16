from sat.literal import Literal


class Valuation:
    """ Contains a 'Literal -> bool' mapping, representing a truth assignment.
    """

    def __init__(self, variables):
        self.valuation = {v: None for v in variables}

    def get_value_for_literal(self, literal):
        """
        :param literal: literal to get truth value for
        :return: truth value for literal
        """
        if not isinstance(literal, Literal):
            raise TypeError("'variable' must be a Literal instance.")

        value = self.valuation.get(literal.get_variable())
        if literal.is_positive:
            value = 1 - value
        return value
