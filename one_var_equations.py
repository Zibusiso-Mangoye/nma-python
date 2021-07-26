"""
Implementation of the algorithms in chapter 2 of Numerical Analysis by Richard L. Burden and J. Douglas Faires
"""
def bisection(f, a, b, TOL, N):
    """
    To find a solution to f(x) = 0 given the continuous function f on the interval [a, b], where
    f(a) and f(b) have opposite signs:
    INPUT : the function f, endpoints a, b; tolerance TOL; maximum number of iterations N.
    OUTPUT : an approximate solution p or message of failure.
    """
    p = a
    if (f(a) * f(b) >= 0):
        print("f(a) and f(b) need to have opposite signs\n")
        return
    
    i = 1
    FA = f(a)
    while i <= N:
        p = a + (b - a)/2 #(Compute pi.)
        FP = f(p)
        if (FP == 0.0 or (b - a)/2 < TOL):
            #(Procedure completed successfully.)
            break
        i = i + 1
        if (FA * FP > 0):
            a = p #(Compute ai, bi.)
            FA = FP
        else:
            b = p #(FA is unchanged.)
    
    if i == N:
        print(f'Method failed after {N} iterations') #(The procedure was unsuccessful.)
    return p