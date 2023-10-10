import numpy as np

def launch_angle_range(ve_v0, alpha, tol_alpha):

    eps_s = 0.5e-5
    eps_a = 1
    tot = 0
    k = 1
    fact = 0

    sin_phi = (1 + alpha) * np.sqrt(1 - ((alpha/(1 + alpha))*((v_e/v_0)**2))) #sin of launch angle
    x = sin_phi

    while eps_a > eps_s:

        term = (((2*x)**(2*k)))/((k**2)*(((2*k)*fact)/(fact**2)))
        tot += term
        eps_a = abs(term/tot)
        k += 1
        fact = fact * k

    sin_sq = 0.5 * tot
    phi = np.sqrt(sin_sq)
    
    return phi
        