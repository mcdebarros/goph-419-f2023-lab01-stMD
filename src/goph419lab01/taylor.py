import numpy as np
from matplotlib import pyplot as plt

def exp(x):

    """Compute the value of the exponential function for real-valued scalar input
    Parameters
    __________
    x : float_like
        Argument of the exponential function
        
    Returns
    _______
    float
        Value of the exponential function at x
    """

    eps_s = 1e-16
    eps_a = 1
    tot = 0
    x = float(x)
    fact = 0
    k = 1

    while eps_a > eps_s:

        term = (x**k)/(k*fact)
        tot += term
        eps_a = abs(term/tot)
        k += 1
        fact = fact * k
    
    return tot

tot = exp(5)
print(tot)


