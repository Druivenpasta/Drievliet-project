import model
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
#       constantes
# ---------------------------------
r_large = 7 #m
r_small = 4 #m
omega = 10.6 #rad/s
epsilon = 10 #rad/s
constants = (r_large, r_small, omega, epsilon)

t = np.linspace(40,120,10000) # time array tussen de lage draai en de verhoging
theta, theta_dot, theta_ddot = model.angle_function(t)
plt.figure()
plt.plot(theta, t, 'k.')