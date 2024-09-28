'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(3,4) == 7

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(9,5) == 4

def test_multiplication():
    '''Test that multiplication function works '''    
    assert multiply(3,6) == 18

def test_division():
    '''Test that multiplication function works '''    
    assert divide(15,3) == 5
