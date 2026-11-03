import pytest

from ci_practice.calculator import add, divide, is_even, multiply


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError, match="divide by zero"):
        divide(1, 0)


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0


@pytest.mark.parametrize("n, expected", [(2, True), (3, False), (0, True)])
def test_is_even(n, expected):
    assert is_even(n) is expected
