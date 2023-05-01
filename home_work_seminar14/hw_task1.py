"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
doctest,
unittest,
pytest.
"""
import unittest
import pytest


def factorial(n: int) -> int:
    """
    >>> factorial(5)
    120
    >>> factorial(6)
    720
    >>> factorial(-5)
    1
    """
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


class TestCaseFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_type(self):
        self.assertEqual(factorial(6), int(720))


def test_factorial1():
    assert factorial(5) == 120


def test_type1():
    assert factorial(6) == str(720)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    unittest.main(verbosity=2)
    pytest.main(['-vv'])
    # print(f'{factorial(-5) = }')

