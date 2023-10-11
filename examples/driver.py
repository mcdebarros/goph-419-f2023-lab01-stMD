from goph419lab01.range import launch_angle_range as lar
from goph419lab01.tests import test_root as tr
from goph419lab01.tests import test_sin as ts
from goph419lab01.tests import test_vel as tv
from matplotlib import pyplot as plt
import numpy as np

def main():
    
    gc = 6.67e-11 #Gravitational constant
    gso = 35786000
    m_e = 5.972e24 #Earth mass
    r_e = 6.3781e6 #Earth radius
    v_e = np.sqrt((2*gc*m_e)/(r_e)) #Escape velocity
    alpha = 0.25 #Distance ratio 
    v_0 = v_e / 2 #Initial velocity
    ve_v0 = v_e / v_0
    tol_alpha = 0.02

    a_min = (1 + tol_alpha) * alpha
    a_max = (1 - tol_alpha) * alpha

    a_range = [a_min,a_max]

    pass_fail_root,root_term = tr(a_range,ve_v0)
    pass_fail_vel,min_vel = tv(a_range,v_e,v_0)
    pass_fail_sin,sin_max = ts(a_range,ve_v0)

    if pass_fail_vel == 0:

        print("Insufficient launch velocity for specified alpha and tolerance.")
        print("Minimum launch velocity for specified alpha is ",min_vel)
        exit()

    elif pass_fail_root == 0:

        print("Non-real components deteced in launch angle. Square root term must be equal to greater than 0.")
        print("Largest computed square root term is ",1 - root_term)
        exit()

    elif pass_fail_sin == 0:

        print("Sin term not in range of function. Sin term must not be greater than 1.")
        print("Largest computed sin term is ",sin_max)
        exit()

    else:

        print("Computing and testing launch angle range for alpha = ",alpha," and tol_alpha = ",tol_alpha," (...)",)
        print()
        domain = lar(ve_v0,alpha,tol_alpha)

    a_max = 1/3
    a_min = 0
    tol_alpha = 0.04

    alpha = np.linspace(a_min,a_max,30)

    phi = np.zeros((len(alpha), 2))
    phi_min = phi
    phi_max = phi

    for i in range (0,len(alpha)):

        phi[i] = lar(ve_v0,alpha[i],tol_alpha)

    phi_min = phi[:,0]
    phi_max = phi[:,1]

    plt.figure()
    plt.xlabel("Alpha")
    plt.ylabel("Phi [rad]")
    plt.title("Figure 1: Launch angles as a function of alpha for ve/v0 = 2.0, tol = 0.04")
    plt.plot(alpha,phi_min,"-c",label="Minimum phi")
    plt.plot(alpha,phi_max,"-r",label="Maximum phi")
    plt.legend()
    plt.grid()
    plt.savefig('C:\\Users\\Mauricio\\REPOS\\GOPH419\\goph-419-f2023-lab01-stMD\\figures\\alpha.png')

    alpha = 0.25

    ve_min = 3 * np.sqrt(1/5)
    ve_max = np.sqrt(5)

    ve_v0 = np.linspace(ve_min,ve_max,30)

    phi = np.zeros((len(ve_v0), 2))
    phi_min = phi
    phi_max = phi_min

    for i in range (0,len(ve_v0)):

        phi[i] = lar(ve_v0[i],alpha,tol_alpha)

    phi_min = phi[:,0]
    phi_max = phi[:,1]

    plt.figure()
    plt.xlabel("ve/v0")
    plt.ylabel("Phi [rad]")
    plt.title("Figure 1: Launch angles as a function of ve/v0 for alpha = 0.25, tol = 0.04")
    plt.plot(ve_v0,phi_min,"-c",label="Minimum phi")
    plt.plot(ve_v0,phi_max,"-r",label="Maximum phi")
    plt.legend()
    plt.grid()
    plt.savefig('C:\\Users\\Mauricio\\REPOS\\GOPH419\\goph-419-f2023-lab01-stMD\\figures\\vev0.png')
    plt.show()

if __name__ == "__main__":
    main()