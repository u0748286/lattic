import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the time interval
T_j = 2

# Define the initial and final conditions
d0, dot_d0, ddot_d0 = 1, 0, 0  # Initial conditions
d1, dot_d1, ddot_d1 = 5, 0, 0  # Final conditions

# Define the quintic polynomial function
def quintic_polynomial(t, a0, a1, a2, a3, a4, a5):
    return a0 + a1*t + a2*t**2 + a3*t**3 + a4*t**4 + a5*t**5

# Initial guess for the polynomial coefficients
initial_guess = [d0, dot_d0, ddot_d0, 0, 0, 0]

# Define the constraints for the end conditions
constraints = (np.array([T_j**i for i in range(6)]),
               np.array([i*T_j**(i-1) for i in range(1, 6)]),
               np.array([i*(i-1)*T_j**(i-2) for i in range(2, 6)]) + [0,0])

# Use curve fitting to find the polynomial coefficients
params, params_covariance = curve_fit(quintic_polynomial, [0, T_j], [d0, d1], p0=initial_guess)

# Plot the resulting quintic polynomial trajectory
t_values = np.linspace(0, T_j, num=100)
d_values = quintic_polynomial(t_values, *params)

plt.plot(t_values, d_values, label='Quintic Polynomial Trajectory')
plt.xlabel('Time (s)')
plt.ylabel('Lateral Displacement (d)')
plt.title('Generated Quintic Polynomial Trajectory')
plt.legend()
plt.grid(True)
plt.show()
