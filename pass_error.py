import numpy as np
import matplotlib.pyplot as plt

# Data

distances = np.array([390,317,285,245,220,415,460])  # meters
rpm = np.array([3535,3265,3050,2830,2755,3750,4025])
coefficients = np.polyfit(distances,rpm ,2)
   

# Fit a quadratic polynomial: actual = f(measured)

# Corrected distance function
def corrected_distance(measured_distance):
    return coefficients[0] * measured_distance**2 + coefficients[1] * measured_distance + coefficients[2]
polynomial = np.poly1d(coefficients)

# Generate x values for a smooth curve
x_fit = np.linspace(distances.min(), distances.max(), 500)
y_fit = polynomial(x_fit)

# Plotting
plt.scatter(distances, rpm, color='red', label='Data Points')
plt.plot(x_fit, y_fit, color='blue', label='Fitted Curve')
plt.xlabel('Distance (meters)')
plt.ylabel('RPM')
plt.title('RPM vs Distance')
plt.legend()
plt.grid(True)
plt.show()