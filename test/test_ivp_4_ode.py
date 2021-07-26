"""
Tests for ivp_4_ode.py
"""
from ivp_4_ode import euler

def test_euler():
    """
    This test is Example 1 in chapter 5 of the textbook.
    """
    f  = lambda y, t : y - t**2 + 1
    assert euler(f, 0, 2, 10, 0.5) == 4.8657845 # @ t = 2