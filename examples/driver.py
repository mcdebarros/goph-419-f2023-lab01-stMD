from goph419lab01.range import launch_angle_range as lar
from matplotlib import pyplot as plt
import numpy as np

def main():
    
    gc = 6.67e-11 #Gravitational constant
    m_e = 5.972e24 #Earth mass
    r_e = 6.3781e6 #Earth radius
    v_e = np.sqrt((2*gc*m_e)/(r_e)) #Escape velocity
    alpha = 2.0 #Distance ratio 
    v_0 = 0 #Initial velocity
    e_o = v_e / v_0
    tol_alpha = 0.02

    x = np.linspace(-10,10,1)

    phi_range = lar(e_o,alpha,tol_alpha)





if __name__ == "__main__":
    main()