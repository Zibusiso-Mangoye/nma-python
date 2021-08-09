"""
Tests for ivp_4_ode.py
"""
from nma.ivp_4_ode import euler, runge_kutta_o4


def test_runge_kutta_o4():
    """
    This test is Example 3 in chapter 5 of the textbook.
    """
    f = lambda t, y: y - t ** 2 + 1
    assert runge_kutta_o4(f, 0, 2, 10, 0.5)[-1][1] == 5.305363000692653  # @ t = 2
