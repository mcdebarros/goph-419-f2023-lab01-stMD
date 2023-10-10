from goph419lab01.range import launch_angle_range as lar
from goph419lab01.tests import test_root as tr
from goph419lab01.tests import test_sin as ts
from goph419lab01.tests import test_vel as tv
from matplotlib import pyplot as plt
import numpy as np

def main():
    
    gc = 6.67e-11 #Gravitational constant
    m_e = 5.972e24 #Earth mass
    r_e = 6.3781e6 #Earth radius
    v_e = np.sqrt((2*gc*m_e)/(r_e)) #Escape velocity
    alpha = 0.25 #Distance ratio 
    v_0 = 0 #Initial velocity
    ve_v0 = 2.0
    tol_alpha = 0.02

    a_min = (1 + tol_alpha) * alpha
    a_max = (1 - tol_alpha) * alpha

    a_range = [a_min,a_max]

    pass_fail_root = tr()

    domain = lar(ve_v0,alpha,tol_alpha)

if __name__ == "__main__":
    main()