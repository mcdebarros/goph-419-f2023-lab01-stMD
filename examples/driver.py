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
    v_0 = v_e / 2 #Initial velocity
    ve_v0 = v_e / v_0 #Ratio of escape velocity to initial velocity
    tol_alpha = 0.02

    a_min = (1 + tol_alpha) * alpha #Alpha for minimum launch angle
    a_max = (1 - tol_alpha) * alpha #Alpha for maximum launch angle

    a_range = [a_min,a_max] #List of alpha values for lar() function

    pass_fail_root,root_term = tr(a_range,ve_v0) #Checks for allowable values of square root term
    pass_fail_vel,min_vel = tv(a_range,v_e,v_0) #Checks for allowable values of minimum launch velocity
    pass_fail_sin,sin_max = ts(a_range,ve_v0) #Checks for allowable values of sin function

    if pass_fail_vel == 0: #Closes program if root test failed

        print("Insufficient launch velocity for specified alpha and tolerance.")
        print("Minimum launch velocity for specified alpha is ",min_vel)
        exit()

    elif pass_fail_root == 0: #Closes program if velocity tests failed

        print("Non-real components deteced in launch angle. Square root term must be equal to greater than 0.")
        print("Largest computed square root term is ",1 - root_term)
        exit()

    elif pass_fail_sin == 0: #Closes program if sin test failed

        print("Sin term not in range of function. Sin term must not be greater than 1.")
        print("Largest computed sin term is ",sin_max)
        exit()

    else: #Computes range of launch angles if all tests passed

        print("Computing and testing launch angle range for alpha = ",alpha," and tol_alpha = ",tol_alpha," (...)",)
        print()
        domain = lar(ve_v0,alpha,tol_alpha)

#------------------------------------------------------------------------------------------

    a_max = 1/3 #Sets max alpha for ve/v0 = 2.0
    a_min = 0 #Sets minimum alpha for ve/v0 = 2.0
    tol_alpha = 0.04

    alpha = np.linspace(a_min,a_max,10000) #Creates array of alpha values to plot

    phi = np.zeros((len(alpha), 2)) #Creates zero-matrix to be populated by values of phi
    phi_min = phi #Creates zero-matrix to be populated by values of phi
    phi_max = phi #Creates zero-matrix to be populated by values of phi

    for i in range (0,len(alpha)): #Calculates maximum and minimum phi for some alpha in alpha

        phi[i] = lar(ve_v0,alpha[i],tol_alpha)

    phi_min = phi[:,0] #Populates array with minimum values of phi for some alpha
    phi_max = phi[:,1] #Populates array with maximum values of phi for some alpha

    plt.figure() #Initializes figure
    plt.xlabel("Alpha") #Sets x axis label
    plt.ylabel("Phi [rad]") #Sets y axis label
    plt.title("Figure 1: Launch angles as a function of alpha for ve/v0 = 2.0, tol = 0.04") #Sets figure title
    plt.plot(alpha,phi_min,"-c",label="Minimum phi") #Plots minimum values of phi against alpha
    plt.plot(alpha,phi_max,"-r",label="Maximum phi") #Plots maximum values of phi against alpha
    plt.legend() #Sets legend
    plt.savefig('C:\\Users\\Mauricio\\REPOS\\GOPH419\\goph-419-f2023-lab01-stMD\\figures\\alpha.png')
    plt.grid() #Grids figure

#-----------------------------------------------------------------------------

    alpha = 0.25 #Sets constant alpha

    ve_min = 3 * np.sqrt(1/5) #Minimum value of ve/v0 for alpha = 0.25
    ve_max = np.sqrt(5) #Maximum value of ve/v0 for alpha = 0.25

    ve_v0 = np.linspace(ve_min,ve_max,10000) #Creates array of ve/v0 values to plot

    phi = np.zeros((len(ve_v0), 2)) #Creates zero-matrix to be populated with values of phi
    phi_min = phi #Creates zero-matrix to be populated with values of phi
    phi_max = phi_min #Creates zero-matrix to be populated with values of phi

    for i in range (0,len(ve_v0)): #Calculates minimum and maximum values of phi for some ve/v0

        phi[i] = lar(ve_v0[i],alpha,tol_alpha)

    phi_min = phi[:,0] #Populates array with minimum values of phi for some ve/v0
    phi_max = phi[:,1] #Populates array with maximum values of phi for some ve/v0

    plt.figure() #Initializes figure
    plt.xlabel("ve/v0") #Sets x axis label
    plt.ylabel("Phi [rad]") #Sets y axis label
    plt.title("Figure 1: Launch angles as a function of ve/v0 for alpha = 0.25, tol = 0.04") #Sets figure title
    plt.plot(ve_v0,phi_min,"-c",label="Minimum phi") #Plots minimum values of phi for some ve/v0
    plt.plot(ve_v0,phi_max,"-r",label="Maximum phi") #Plots maximum values of phi for some ve/v0
    plt.legend() #Sets legend
    plt.grid() #Grids figure
    plt.savefig('C:\\Users\\Mauricio\\REPOS\\GOPH419\\goph-419-f2023-lab01-stMD\\figures\\vev0.png')
    plt.show() #Shows plots

if __name__ == "__main__": #Initializes program
    main()