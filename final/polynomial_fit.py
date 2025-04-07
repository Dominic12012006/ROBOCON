import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Provided data
distance = np.array([
    3.9, 3.6, 3.6, 3.65, 4.1, 3.85, 4, 4.4, 4.4, 4.4, 4.5, 4.6, 4.5, 4.7, 4.3, 
    3.4, 2.25, 2.1, 2.6, 2.2, 2.15, 2.15, 2.4, 2.4, 2.4, 2.3, 2.3, 2.75, 2.75, 2.75, 
    3, 3, 3.35, 3.5, 3.2, 3.55, 3.55, 3.65, 3.8, 4, 4, 4.05, 4.05, 4.25, 4.2, 4.2, 
    4.45, 4.2, 4.3, 4.3, 4.6, 4.7, 4.55, 4.7, 4.9, 4.8, 4.9, 5.1, 5, 5, 5.3, 5.3, 
    5.3, 5.7, 5.4, 
    5.5, 5.6, 5.9, 5.7, 5.8, 5.8, 6, 6, 6, 6.2, 6.35, 6.3, 6.6, 6.6, 
    6.6, 6.6, 6.6, 6.6, 6.5, 6.6, 6.1
])
rpm = np.array([
    2600, 2600, 2600, 2600, 2700, 2700, 2700, 2800, 2800, 2800, 2900, 2900, 2900, 
    3000, 2800, 2500, 2000, 2000, 2000, 2000, 2000, 2000, 2100, 2100, 2200, 2200, 
    2200, 2200, 2200, 2200, 2300, 2300, 2400, 2400, 2400, 2400, 2500, 2500, 2500, 
    2600, 2600, 2600, 2600, 2700, 2700, 2700, 2800, 2800, 2800, 2800, 2900, 2900, 
    2900, 3000, 3000, 3000, 3000, 3100, 3100, 3100, 3200, 3200, 3200, 3300, 3300, 
    3300, 3300, 3400, 3400, 3400, 3400, 3500, 3500, 3500, 3600, 3600, 3600, 3600, 
    3700, 3700, 3700, 3700, 3800, 3800, 3800, 3800
])

# Reshape for sklearn
X = distance.reshape(-1, 1)
y = rpm

# Set polynomial degree
degree = 3  # Adjust as needed
poly = PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(X)

# Train regression model
model = LinearRegression()
model.fit(X_poly, y)

# Function to predict RPM for a given distance
def predict_rpm(dist):
    dist_poly = poly.transform(np.array([[dist]]))
    predicted_rpm = model.predict(dist_poly)[0]
    return predicted_rpm

# Get user input
# user_distance = float(input("Enter the distance value: "))
# predicted_rpm = predict_rpm(user_distance)
# print(f"Predicted RPM for distance {user_distance}: {predicted_rpm:.2f}")

# # Plot the data and model
# plt.scatter(distance, rpm, color='red', label="Actual Data")
# x_range = np.linspace(min(distance), max(distance), 100).reshape(-1, 1)
# y_pred = model.predict(poly.transform(x_range))
# plt.plot(x_range, y_pred, color='blue', label="Polynomial Fit")
# plt.xlabel("Distance")
# plt.ylabel("RPM")
# plt.title("Polynomial Regression: Distance vs RPM")
# plt.legend()
# plt.show()