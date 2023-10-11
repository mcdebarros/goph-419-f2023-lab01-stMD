import numpy as np

def launch_angle_range(ve_v0, alpha, tol_alpha):

    """Compute the square of arcsin for input parameters
    Parameters
    __________
    ve_v0 : float_like
        Ratio of initial velocity to terminal velocity

    alpha : float_like
        Target altitude as fraction of earth radius

    tol_alpha : float_like
        Allowable error in target altitude
        
    Returns
    _______
    domain : array_like
        Minimum and maximum values of launch angle
    """

    eps_s = 0.5e-5 #Stopping criteria for 5 significant digits of precision
    eps_a = 1 #Default value for initial relative error
    tot = 0 #Default for summation total
    k = 0 #Default for iteration number
    fact = 1 #Default for factorial
    d_fact = 1 #Default for double factorial

    a_min = (1 + tol_alpha) * alpha #Minimum allowable alpha
    a_max = (1 - tol_alpha) * alpha #Maximum allowable alpha

    alpha = [a_min,a_max] #Combined values of alpha


    sin_min = (1 + alpha[0]) * np.sqrt(1 - ((alpha[0] / (1 + alpha[0])) * (ve_v0 ** 2))) #Calculates sin of launch angle for some minimum alpha and constant ve/v0
    sin_max = (1 + alpha[1]) * np.sqrt(1 - ((alpha[1] / (1 + alpha[1])) * (ve_v0 ** 2))) #Calculates sin of launch angle for some maximum alpha and constant ve/v0

    while eps_a > eps_s: #Iterates loop until stopping criteria met

        k += 1 #Increases iteration counter
        fact *= k #Sets iteration factorial
        d_fact *= (2 * k) * ((2 * k) - 1) #Sets iteration double factorial
        term = 0.5 * (((2 * sin_min) ** (2 * k)) / (((k ** 2) * (d_fact / (fact ** 2))))) #Calculates iteration term
        tot += term #Adds term to sum total
        eps_a = abs(term/tot) #Calculates relative error of iteration

    sin_sq = tot #Sets loop sum as square of sinverse sin
    phi_min = np.sqrt(sin_sq) #Calculates root of sum
    phi_min_exp = np.arcsin(sin_min) #Sets trusted calculation of arcsin for given inputs

    print("Alpha = ",alpha) #Displays alpha used
    print("Expected minimum angle: ", phi_min_exp) #Shows computed arcsin value
    print("Computed minimum angle: ",phi_min) #Shows expected arcsin

    eps_a = 1 #Default value for relative error
    tot = 0 #Initializes summation
    k = 0 #Initializes iteration counter
    fact = 1 #Intializes factorial
    d_fact = 1 #Initializes double factorial

    while eps_a > eps_s: #Iterates loop until stopping criteria met

        k += 1 #Increases iteration counter
        fact *= k #Sets iteration factorial
        d_fact *= (2 * k) * ((2 * k) - 1) #Sets iteration double factorial
        term = 0.5 * (((2 * sin_max) ** (2 * k)) / (((k ** 2) * (d_fact / (fact ** 2))))) #Calculates iteration term
        tot += term #Adds term to sum
        eps_a = abs(term/tot) #Calculates relative error

    sin_sq = tot #Sets total as square of arcsin
    phi_max = np.sqrt(sin_sq) #Calculates root of sum
    phi_max_exp = np.arcsin(sin_max) #Computes expected arcsin
    print("Expected Maximum Angle: ", phi_max_exp) #Displays computed arcsin
    print("Computed Maximum Angle: ",phi_max) #Displays expected arcsin
    print()

    domain = np.array([phi_min,phi_max]) #Creates array of minimum and maximum phi values
    
    return domain #returns domain
        