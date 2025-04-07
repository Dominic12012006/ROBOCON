# rpm_predictor.py

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Dataset
distances_cm = np.array([300,330,350,380,410,465,500,530,560,590,620,650,680,720,750]).reshape(-1, 1)
min_rpm = np.array([2940,2960,3080,3130,3200,3570,3610,3680,3760,3870,3960,4050,4120,4200,4350])
max_rpm = np.array([2970,3110,3180,3280,3375,3680,3740,3840,3910,4040,4070,4180,4300,4380,4460])
avg_rpm = (min_rpm + max_rpm) / 2

# Polynomial Regression setup
degree = 2
poly = PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(distances_cm)

model = LinearRegression()
model.fit(X_poly, avg_rpm)

def predict_rpm(distance_cm):
    """k
    Predicts RPM for a given distance in cm using trained polynomial regression model.
    """
    input_poly = poly.transform(np.array([[distance_cm]]))
    return model.predict(input_poly)[0]










# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression

# # Given data
# distances_cm = np.array([300,330,350,380,410,465,500,530,560,590,620,650,680,720,750]).reshape(-1, 1)
# min_rpm = np.array([2940,2960,3080,3130,3200,3570,3610,3680,3760,3870,3960,4050,4120,4200,4350])
# max_rpm = np.array([2970,3110,3180,3280,3375,3680,3740,3840,3910,4040,4070,4180,4300,4380,4460])
# avg_rpm = (min_rpm + max_rpm) / 2

# # Polynomial Regression
# degree = 5  # You can experiment with higher degrees if needed
# poly = PolynomialFeatures(degree=degree)
# X_poly = poly.fit_transform(distances_cm)

# model = LinearRegression()
# model.fit(X_poly, avg_rpm)

# # Plot the data and polynomial fit
# x_range = np.linspace(distances_cm.min(), distances_cm.max(), 300).reshape(-1, 1)
# y_pred = model.predict(poly.transform(x_range))

# plt.scatter(distances_cm, avg_rpm, color='red', label='Average RPM Data')
# plt.plot(x_range, y_pred, color='blue', label=f'Polynomial Fit (degree={degree})')
# plt.xlabel('Distance (cm)')
# plt.ylabel('Average RPM')
# plt.title('Polynomial Regression: Distance vs RPM')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Predict RPM for a user-input distance
# user_input = float(input("Enter a distance (in cm) to predict RPM: "))
# user_input_poly = poly.transform([[user_input]])
# predicted_rpm = model.predict(user_input_poly)

# print(f"Predicted RPM for distance {user_input} cm is: {predicted_rpm[0]:.2f}")