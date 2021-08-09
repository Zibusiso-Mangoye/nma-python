"""
Initial-Value Problems for Ordinary Differential Equations
Implementation of the algorithms in chapter 5 of Numerical Analysis by Richard L. Burden and J. Douglas Faires
"""


def runge_kutta_o4(f, a, b, N, y_0):
    """
    To approximate the solution of the initial-value problem
            y' = f(t, y), a ≤ t ≤ b, y(a) = α,
    at (N + 1) equally spaced numbers in the interval [a, b]:
    INPUT : function f, endpoints a, b; number of iterations N; initial condition alpha(α).
    OUTPUT : approximations (as a list of list) of w to y at the (N + 1) values of t.
    """
    # To hold the results
    result = []

    h = (b - a) / N
    t = a
    w = y_0
    result.append([t, w])
    for i in range(1, N + 1):
        K1 = h * f(t, w)
        K2 = h * f(t + h / 2, w + K1 / 2)
        K3 = h * f(t + h / 2, w + K2 / 2)
        K4 = h * f(t + h, w + K3)
        w = w + (K1 + 2 * K2 + 2 * K3 + K4) / 6  # (Compute wi.)
        t = a + i * h  # (Compute ti.)
        result.append([t, w])

    return result
