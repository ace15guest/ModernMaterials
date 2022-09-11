import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

"""
Asa Guest
HW1 - Plotting Assignment
Plotting the flowfield of a free stream as a function of the eta which is derived to be a function of
the Reynolds number, x poisiton and y posiiton of the entrainment screen
"""

f = np.linspace(0,.9996,1000)
a=np.linspace(0,10,1000)
check = np.linspace(0,10,10)
one = np.ones_like(check)
#Flow field over walljet simplified for different flow conditions
eta = np.log(np.sqrt(1+np.sqrt(f)+f)/(1-np.sqrt(f)))+np.sqrt(3)*np.arctan(np.sqrt(3*f)/(2+np.sqrt(f)))
# Simple 2D Plotting scheme
cs = CubicSpline(eta,f,bc_type='clamped')
# plt.plot(check,one)
plt.plot(eta,f,'r')
plt.xlabel('$\eta$ (Non-Dimensional)')
plt.ylabel('f($\eta$) (Dimensionless)')
plt.title('$\eta$ vs f($\eta$)')
plt.grid(True)
plt.show()