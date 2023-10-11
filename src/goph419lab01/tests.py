import numpy as np

def test_root(alpha,ve_v0):

    """Test for allowable values of the root
    Parameters
    __________
    ve_v0 : float_like
        Ratio of initial velocity to terminal velocity

    alpha : float_like
        Target altitude as fraction of earth radius
        
    Returns
    _______
    bool
        passed (1) or failed (0) test

    combined_i
        Problematic value of root
    """

    a_term = alpha[0] / (1 + alpha[0]) #Computes alpha term
    v_term = ve_v0 ** 2 #Computes velocity term
    combined_0 = a_term * v_term #Computes product of alpha and velocity terms

    a_term = alpha[1] / (1 + alpha[1]) #Computes alpha term
    combined_1 = a_term * v_term #Computes product of alpha and velocity terms

    if (combined_0 or combined_1) > 1: #Checks condition

        if combined_0 < combined_1: #Checks and returns probelmatic term

            return 0, combined_0 #Returns test pass/fail and problematic input
        
        else:

            return 0, combined_1 #Returns pass/fail and problematic input
    
    else: #Returns test pass

        return 1,1

def test_vel(alpha,v_e,v_0):

    """Test for allowable values of ve
    __________
    ve_v0 : float_like
        Ratio of initial velocity to terminal velocity

    alpha : float_like
        Target altitude as fraction of earth radius
        
    Returns
    _______
    bool
        passed (0) or failed (1) test

    condition_i
        Problematic v0 value
    """

    condition_0 = np.sqrt((alpha[0] * (v_e ** 2)) / (alpha[0] + 1)) #Computes minimum ve
    condition_1 = np.sqrt((alpha[1] * (v_e ** 2)) / (alpha[1] + 1)) #Computes maximum ve

    if v_0 < (condition_0 or condition_1): #Checks test pass/fail

        if condition_1 < condition_0: #Checks problematic input

            return 0, condition_1 #Returns test fail and problematic input
        
        else:

            return 0, condition_0 #Returns test fail and problemtic input
    
    else:

        return 1,1 #Returns test pass
    
def test_sin(alpha,ve_v0):

    """Test for allowable values of sin
    Parameters
    __________
    ve_v0 : float_like
        Ratio of initial velocity to terminal velocity

    alpha : float_like
        Target altitude as fraction of earth radius
        
    Returns
    _______
    bool
        passed (1) or failed (0) test

    sin_i
        problematic sin
    """

    sin_0 = (1 + alpha[0]) * np.sqrt(1 - ((alpha[0] / (1 + alpha[0])) * (ve_v0 ** 2))) #Computes minimum sin
    sin_1 = (1 + alpha[1]) * np.sqrt(1 - ((alpha[1] / (1 + alpha[1])) * (ve_v0 ** 2))) #Computes maximum sin

    if (sin_1 or sin_0) > 1: #Checks test pass/fail

        if sin_0 > sin_1: #Checks problematic input

            return 0,sin_0 #Returns test fail and problematic input
        
        else:

            return 0,sin_1 #Returns test fail and problematic input
    
    else:

        return 1,1 #Returns test pass
    