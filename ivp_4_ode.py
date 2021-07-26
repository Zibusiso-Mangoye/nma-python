"""
Initial-Value Problems for Ordinary Differential Equations
Implementation of the algorithms in chapter 5 of Numerical Analysis by Richard L. Burden and J. Douglas Faires
"""

def euler(f, a, b, N, y_0):
    """
    To approximate the solution of the initial-value problem
        y' = f(t, y), a ≤ t ≤ b, y(a) = α,
    at (N + 1) equally spaced numbers in the interval [a, b]:
    INPUT : function f, endpoints a, b; integer N; initial condition y_0.
    OUTPUT : approximation w to y at the (N + 1) values of t.
    """
    pass # Your code goes here