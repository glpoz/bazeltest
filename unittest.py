#this file includes test cases for calculation_module.py

import calculation_module

def test_add():
    assert calculation_module.add(2,2) == 4
    assert calculation_module.add(3,-5) == -2

def test_subtract():
    assert calculation_module.subtract(5,3) == 2
    assert calculation_module.subtract(3,-20) == 23
    assert calculation_module.subtract(-3,5) == -8

def test_multiply():
    assert calculation_module.multiply(3,2) == 6
    assert calculation_module.multiply(45,-2) == -90
    assert calculation_module.multiply(-33,0) == 0
    assert calculation_module.multiply(-3,-2) == 6
    assert calculation_module.multiply(0,0) == 0

def test_divide():
    assert calculation_module.divide(4,2) == 2
    assert calculation_module.divide(45,-3) == -15
    assert calculation_module.divide(-33,0) == "I can't divide by 0"
    assert calculation_module.divide(-4,-2) == 2