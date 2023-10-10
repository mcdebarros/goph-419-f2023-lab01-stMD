import numpy as np
from goph419lab01.tests import test_root as tr

def launch_angle_range(ve_v0, alpha, tol_alpha):

    eps_s = 0.5e-5
    eps_a = 1
    tot = 0
    k = 0
    fact = 1
    d_fact = 1

    if (pass_fail_min or pass_fail_max) == 0:



    sin_min = (1 + a_min) * np.sqrt(1 - ((a_min / (1 + a_min)) * (ve_v0 ** 2)))
    sin_max = (1 + a_max) * np.sqrt(1 - ((a_max / (1 + a_max)) * (ve_v0 ** 2)))

    while eps_a > eps_s:

        k += 1
        fact *= k 
        d_fact *= (2 * k) * ((2 * k) - 1)
        term = 0.5 * (((2 * sin_min) ** (2 * k)) / (((k ** 2) * (d_fact / (fact ** 2)))))
        tot += term
        eps_a = abs(term/tot)

    sin_sq = tot
    phi_min = np.sqrt(sin_sq)
    phi_min_exp = np.arcsin(sin_min)
    print("expected phi_min: ", phi_min_exp)
    print("computed phi_min: ",phi_min)

    eps_a = 1
    tot = 0
    k = 0
    fact = 1
    d_fact = 1

    while eps_a > eps_s:

        k += 1
        fact *= k 
        d_fact *= (2 * k) * ((2 * k) - 1)
        term = 0.5 * (((2 * sin_max) ** (2 * k)) / (((k ** 2) * (d_fact / (fact ** 2)))))
        tot += term
        eps_a = abs(term/tot)

    sin_sq = tot
    phi_max = np.sqrt(sin_sq)
    phi_max_exp = np.arcsin(sin_max)
    print("expected phi_max: ", phi_max_exp)
    print("computed phi_max: ",phi_max)

    domain = np.array([phi_min,phi_max])
    
    return domain
        