from decimal import Decimal
from typing import Callable

class Calculation:
    """
    A basic class for mathematical calculations.
    """

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Initialize a calculation.
        """
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> Decimal:
        """
        Perform the calculation.
        """
        return self.operation(self.a, self.b)

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
        """
        Create a new Calculation instance.
        """
        return Calculation(a, b, operation)

    def __str__(self) -> str:
        """
        String representation of the calculation.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
