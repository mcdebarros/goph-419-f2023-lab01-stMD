import numpy as np

def test_root(alpha,ve_v0):

    a_term = alpha[0] / (1 + alpha[0])
    v_term = ve_v0 ** 2
    combined_0 = a_term * v_term

    a_term = alpha[1] / (1 + alpha[1])
    combined_1 = a_term * v_term

    if (combined_0 or combined_1) > 1:

        if combined_0 < combined_1:

            return 0, combined_0
        
        else:

            return 0, combined_1
    
    else:

        return 1,1

def test_vel(alpha,v_e,v_0):

    condition_0 = np.sqrt((alpha[0] * (v_e ** 2)) / (alpha[0] + 1))
    condition_1 = np.sqrt((alpha[1] * (v_e ** 2)) / (alpha[1] + 1))

    if v_0 < (condition_0 or condition_1):

        if condition_1 < condition_0:

            return 0, condition_1
        
        else:

            return 0, condition_0
    
    else:

        return 1,1
    
def test_sin(alpha,ve_v0):

    sin_0 = (1 + alpha[0]) * np.sqrt(1 - ((alpha[0] / (1 + alpha[0])) * (ve_v0 ** 2)))
    sin_1 = (1 + alpha[1]) * np.sqrt(1 - ((alpha[1] / (1 + alpha[1])) * (ve_v0 ** 2)))

    if (sin_1 or sin_0) > 1:

        if sin_0 > sin_1:

            return 0,sin_0
        
        else:

            return 0,sin_1
    
    else:

        return 1,1
    