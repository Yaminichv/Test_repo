"""
Calculator Test Module

A module to test the Calculator class.
"""
import pytest
from calculator import Calculator

def test_addition():
    """Test addition operation"""
    result = Calculator.add(7, 3)
    assert result == 10

def test_subtraction():
    """Test subtraction operation"""
    result = Calculator.subtract(15, 6)
    assert result == 9

def test_multiplication():
    """Test multiplication operation"""
    result = Calculator.multiply(6, 4)
    assert result == 24

def test_division():
    """Test division operation"""
    result = Calculator.divide(21, 3)
    assert result == 7

def test_division_by_zero():
    """Test division by zero error"""
    with pytest.raises(ValueError):
        Calculator.divide(8, 0)
