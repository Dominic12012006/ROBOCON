import numpy as np
actual_distances = np.array([325,353,400,410,490,280,255])  # meters
measured_distances = np.array([325,355,40,400,450,280,255])
coefficients = np.polyfit(measured_distances, actual_distances, 2)  # quadratic fit
def corrected_distance(measured_distance):
    return coefficients[0] * measured_distance**2 + coefficients[1] * measured_distance + coefficients[2]
