import numpy as np

def test_root(alpha,ve_v0):

    a_term = (1 + alpha[0]) / alpha[0]

    if a_term < ve_v0:

        return 0
    
    else:

        return 1

def test_vel(ve_v0):

    if ve_v0 <= 1:

        return 0
    
    else:

        return 1
    
def test_sin(sin):

    if sin < 1:

        return 0
    
    else:

        return 1
    
