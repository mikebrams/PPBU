from fraction2 import add, sub, mult, div
import pytest


@pytest.mark.parametrize('n1,d1,n2,d2, res',
                         [
                             (1, 1, 1, 1, (2, 1)),
                             (2, 1, 1, 2, (5, 2))
                         ])
def test_add(n1, d1, n2, d2, res):
    assert add(n1, d1, n1, d1) == res

def test_sub():
    assert sub(1, 1, 1, 1) == (0, 1)
    assert sub(2, 1, 1, 2) == (3, 2)


