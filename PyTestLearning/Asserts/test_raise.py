from pytest import approx
from pytest import raises

def test_Float():
    assert (0.1 + 0.2) == approx(0.3)

def raiseValueException():
    raise ValueError

def test_exception():
    with raises(ValueError):
        raiseValueException()
