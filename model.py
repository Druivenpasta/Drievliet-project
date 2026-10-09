# this python file will contain the model code
import numpy as np
import matplotlib.pyplot as plt
import pathlib

# this folder marked here will be used for comparison, as it received the most post-processing
DATA_DIR = pathlib.Path(r'Drievliet-project\Drievliet - Marte 2 2026-09-25 14-33-49')

# lets first just define the model
def angle_function(t):
    """Returns an angle in radians, which is estimated from a video of the attraction"""
    # FIXME this probably shouldnt be hardcoded, but instead given values angle_start, angle_end, t_start and t_end for fitting.
    if t <= 70:
        return -np.pi / 12
    elif t >= 85:
        return np.pi / 4
    else:
        fraction = (t - 70) / (85 - 70)
        return -np.pi / 12 + fraction * (np.pi / 4 + np.pi / 12)

def determine_psi(data):
    """This function should be ran first to find out how much the cart is out of phase, so we fit properly"""

def model(t, r_small, r_large, omega, epsilon, theta, h_0, psi):
    """Inserting the model params and a timestep,
      returns a predicted position vector with the midpoint taken as origin."""
    
    output_vector = np.array([0.,0.,0.])

    # the approach with least causes of eye disorders is inputting each vec seperately
    # the vectors in order found in the pdf
    vector1 = np.array([
        r_large*np.cos(theta)*np.cos(omega*t),
        h_0 + r_large*np.sin(theta),
        r_large*np.cos(theta)*np.sin(omega*t)
    ])
    vector2 = np.array([
        r_small*np.cos(epsilon*t)*np.sin(omega*t),
        0,
        -r_small*np.cos(epsilon*t)*np.cos(omega*t)
    ])
    vector3 = np.array([
        -r_small*np.sin(epsilon*t)*np.cos(omega*t)*np.cos(theta),
        -r_small*np.sin(epsilon*t)*np.sin(theta),
        -r_small*np.sin(epsilon*t)*np.sin(omega*t)*np.cos(theta)
    ])
    output_vector = vector1 + vector2 + vector3
    return output_vector

    