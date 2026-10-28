from fraction2 import add, sub, mult, div
import pytest


def test_add():
    assert add(1, 1, 1, 1) == (2, 1)
    assert add(2, 1, 1, 2) == (5, 2)

def test_sub():
    assert sub(1, 1, 1, 1) == (0, 1)
    assert sub(2, 1, 1, 2) == (3, 2)


