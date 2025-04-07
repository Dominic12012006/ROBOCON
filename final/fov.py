import math

def calculate_fov(sensor_dimension, focal_length):
    # Calculate the FOV in radians
    fov_rad = 2 * math.atan(sensor_dimension / (2 * focal_length))
    # Convert to degrees
    fov_deg = math.degrees(fov_rad)
    return fov_deg

sensor_width = float(input("Enter the sensor width (mm): "))
focal_length = float(input("Enter the focal length (mm): "))

fov = calculate_fov(sensor_width, focal_length)
print(f"Field of View (FOV): {fov:.2f} degrees")
