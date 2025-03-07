import numpy as np

def euler_method(func, t0, y0, t_end, num_iterations):
    dt = (t_end - t0) / num_iterations
    t_values = np.zeros(num_iterations + 1)
    y_values = np.zeros(num_iterations + 1)
    
    t_values[0] = t0
    y_values[0] = y0
    
    for i in range(num_iterations):
        y_values[i + 1] = y_values[i] + dt * func(t_values[i], y_values[i])
        t_values[i + 1] = t_values[i] + dt
    
    return t_values, y_values

def func(t, y):
    return t - y**2

# Parameters
t0 = 0
y0 = 1
t_end = 2
num_iterations = 10 

t_values, y_values = euler_method(func, t0, y0, t_end, num_iterations)

expected_output = y_values[-1]
print("Expected output:", expected_output)


import numpy as np

def runge_kutta_method(func, t0, y0, t_end, num_iterations):
    
    # Calculate the time step
    dt = (t_end - t0) / num_iterations

    # Initialize arrays to store time and y values
    t_values = np.zeros(num_iterations + 1)
    y_values = np.zeros(num_iterations + 1)

    # Set initial conditions
    t_values[0] = t0
    y_values[0] = y0

    # Apply the Runge-Kutta Method
    for i in range(num_iterations):
        # Calculate the intermediate values
        k1 = func(t_values[i], y_values[i])
        k2 = func(t_values[i] + 0.5 * dt, y_values[i] + 0.5 * dt * k1)
        k3 = func(t_values[i] + 0.5 * dt, y_values[i] + 0.5 * dt * k2)
        k4 = func(t_values[i] + dt, y_values[i] + dt * k3)

        # Calculate the next y value using the Runge-Kutta formula
        y_values[i + 1] = y_values[i] + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        # Update the time value
        t_values[i + 1] = t_values[i] + dt

    return t_values, y_values

# Define the function that represents the differential equation
def func(t, y):
    return t - y**2

# Set the parameters
t0 = 0
y0 = 1
t_end = 2
num_iterations = 10  

# Call the Runge-Kutta Method function
t_values, y_values = runge_kutta_method(func, t0, y0, t_end, num_iterations)

# Print the expected output
expected_output = y_values[-1]
print("Expected output:", expected_output)

