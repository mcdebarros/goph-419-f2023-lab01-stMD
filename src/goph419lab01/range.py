import numpy as np

def launch_angle_range(ve_v0, alpha, tol_alpha):

    eps_s = 0.5e-5
    eps_a = 1
    tot = 0
    k = 0
    fact = 1
    d_fact = 1

    a_min = (1 + tol_alpha) * alpha
    a_max = (1 - tol_alpha) * alpha

    alpha = [a_min,a_max]


    sin_min = (1 + alpha[0]) * np.sqrt(1 - ((alpha[0] / (1 + alpha[0])) * (ve_v0 ** 2)))
    sin_max = (1 + alpha[1]) * np.sqrt(1 - ((alpha[1] / (1 + alpha[1])) * (ve_v0 ** 2)))

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

    print("Alpha = ",alpha)
    print("Expected minimum angle: ", phi_min_exp)
    print("Computed minimum angle: ",phi_min)

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
    print("Expected Maximum Angle: ", phi_max_exp)
    print("Computed Maximum Angle: ",phi_max)
    print()

    domain = np.array([phi_min,phi_max])
    
    return domain
        