"""
Calculation Test Module

A module to test the Calculation class.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_calculations(a, b, operation, expected):
    """Test various calculations"""
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected
def test_addition():
    """Test addition operation"""
    calc = Calculation(Decimal('7'), Decimal('3'), add)
    assert calc.perform() == Decimal('10')

def test_subtraction():
    """Test subtraction operation"""
    calc = Calculation(Decimal('15'), Decimal('6'), subtract)
    assert calc.perform() == Decimal('9')

def test_multiplication():
    """Test multiplication operation"""
    calc = Calculation(Decimal('5'), Decimal('4'), multiply)
    assert calc.perform() == Decimal('20')

def test_division():
    """Test division operation"""
    calc = Calculation(Decimal('21'), Decimal('3'), divide)
    assert calc.perform() == Decimal('7')

def test_string_representation():
    """Test string representation of Calculation instance"""
    calc = Calculation(Decimal('3'), Decimal('4'), add)
    assert str(calc) == "Calculation(3, 4, add)"

def test_division_by_zero():
    """Test division by zero error"""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError):
        calc.perform()

def test_create():
    """Test create method"""
    calc = Calculation.create(Decimal('5'), Decimal('2'), add)
    assert calc.a == Decimal('5')
    assert calc.b == Decimal('2')
