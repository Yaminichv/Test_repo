from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    """
    A basic calculator class for arithmetic operations.
    """

    @staticmethod
    def calculate(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """
        Perform a calculation and return the result.
        """
        return operation(a, b)
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        Add two numbers.
        """
        return Calculator.calculate(a, b, lambda x, y: x + y)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        Subtract b from a.
        """
        return Calculator.calculate(a, b, lambda x, y: x - y)
    
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """
        Multiply two numbers.
        """
        return Calculator.calculate(a, b, lambda x, y: x * y)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Divide a by b.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return Calculator.calculate(a, b, lambda x, y: x / y)