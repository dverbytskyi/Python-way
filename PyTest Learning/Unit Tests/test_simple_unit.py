import pytest

def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    elif isMultiple(value, 5):
        return "Buzz"

    return str(value)

def isMultiple(value, mod):
    return (value % mod) == 0

def checkFizzBuzz(arg, expectedVal):
    retVal = fizzBuzz(arg)
    assert retVal == expectedVal

def test_return1With1():
    checkFizzBuzz(1, "1")

def test_return2With2():
    checkFizzBuzz(2, "2")

def test_returnFizzWith3():
    checkFizzBuzz(3, "Fizz")

def test_returnBuzzWith5():
    checkFizzBuzz(5, "Buzz")

def test_returnFizzWith6():
    checkFizzBuzz(6, "Fizz")

def test_returnBuzzWith10():
    checkFizzBuzz(10, "Buzz")

def test_returnFizzBuzzWith15():
    checkFizzBuzz(15, "FizzBuzz")