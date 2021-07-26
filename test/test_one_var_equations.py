"""
Tests for one_var_equations.py
"""
from one_var_equations import bisection

def test_bisection():
    """
    This test is Example 1 in chapter 2 of the textbook.
    """
    f  = lambda x : x**3 + 4*x**2 - 10
    assert bisection(f, 1, 2, 0.00001, 13) == 1.3651123046875