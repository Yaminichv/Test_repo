"""
Calculation Test Module

A module to test the Calculation class.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def setup_calculations():
    """Setup calculations for testing"""
    Calculations.delete_calculation()
    Calculations.add_calculation(Calculation(Decimal('5'), Decimal('2'), add))
    Calculations.add_calculation(Calculation(Decimal('8'), Decimal('3'), subtract))
    Calculations.add_calculation(Calculation(Decimal('6'), Decimal('4'), multiply))
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('3'), divide))

def test_add_calculation():
    """Test adding a new calculation"""
    calc = Calculation(Decimal('7'), Decimal('3'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history"""
    history = Calculations.print_all_calculation()
    assert len(history) == 4

def test_clear_history():
    """Test clearing the calculation history"""
    Calculations.delete_calculation()
    assert len(Calculations.print_all_calculation()) == 0

def test_get_latest(setup_calculations):
    """Test retrieving the latest calculation"""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('15') and latest.b == Decimal('3')

def test_get_latest_empty():
    """Test retrieving the latest calculation when the history is empty"""
    Calculations.delete_calculation()
    assert Calculations.get_latest() is None

def test_filter_operations(setup_calculations):
    """Test filtering calculations by operation"""
    add_ops = Calculations.filter_with_operation("add")
    assert len(add_ops) == 1
    multiply_ops = Calculations.filter_with_operation("multiply")
    assert len(multiply_ops) == 1

def test_multiple_additions():
    """Test adding multiple calculations with the same operation"""
    Calculations.delete_calculation()
    Calculations.add_calculation(Calculation(Decimal('3'), Decimal('4'), add))
    Calculations.add_calculation(Calculation(Decimal('5'), Decimal('6'), add))
    add_ops = Calculations.filter_with_operation("add")
    assert len(add_ops) == 2
