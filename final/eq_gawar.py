import math

# Constants 
g = 980.665  # Acceleration due to gravity (cm/s²)
theta = math.radians(58.03)  # Fixed shooter angle (converted to radians)
height = 123 # Height of the shooting mech to hoop (centimetres)
r_wheel = 6.35  # Radius of the shooter wheels (centimetres)

# User input for horizontal distance (x)
x = float(input("Enter the horizontal distance (cm): "))

# Calculate launch velocity (v)
numerator = g * (x ** 2)
denominator = 2 * (math.cos(theta) ** 2) * (x * math.tan(theta) - (height))
v = math.sqrt(numerator / denominator)

# Calculate angular velocity (omega)
omega = v / r_wheel  # in rad/s


# Convert to RPM
rpm = (omega * 60) / (2 * math.pi)
rpm = rpm * 1
# Display results
print(f"\nRequired Launch Velocity: {v:.2f} m/s")
print(f"Required Angular Velocity: {omega:.2f} rad/s")
print(f"Required RPM for Shooter Wheels: {rpm:.2f} RPM")