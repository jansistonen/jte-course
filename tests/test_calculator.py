import pytest
from src.calculator import Calculator

def testAdd():
    calc = Calculator()
    assert calc.add(2,3) == 5

def testDivide():
    calc = Calculator()
    assert calc.divide(10,5) == 2

def testMultiply():
    calc = Calculator()
    assert calc.multiply(2,2) == 4