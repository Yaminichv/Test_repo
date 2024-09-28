from calculator.calculation import Calculation
from decimal import Decimal
from typing import List

class Calculations:
    history = []

    @classmethod
    def add_calculation(cls, calculation):
        cls.history.append(calculation)

    @classmethod
    def delete_calculation(cls):
        cls.history.clear()

    @classmethod
    def get_latest(cls):
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def print_all_calculation(cls):
        return cls.history

    @classmethod
    def filter_with_operation(cls, operation):
        return [calc for calc in cls.history if calc.operation.__name__ == operation]