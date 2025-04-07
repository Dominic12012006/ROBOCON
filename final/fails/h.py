import math

def horizontal(angle, range_, h_target, g=980.665):
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Calculate the initial velocity v using the range formula
    v = math.sqrt((range_ * g) / math.sin(2 * angle_rad))
    
    # Calculate time when projectile reaches the target height
    # Using the vertical motion equation: y = v * sin(angle) * t - (1/2) * g * t^2
    a = -0.5 * g
    b = v * math.sin(angle_rad)
    c = -h_target
    
    # Solving quadratic equation at^2 + bt + c = 0 for t
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None  # No solution, target height is unreachable
    
    # Two solutions for t (ascending and descending times)
    t1 = (-b + math.sqrt(discriminant)) / (2 * a)
    t2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    # We are interested in the positive time
    t = max(t1, t2)
    
    # Horizontal distance at this time
    x = v * math.cos(angle_rad) * t
    return x

# Example usage
angle = 45  # Launch angle in degrees
range_ = 100  # Range in meters
h_target = 5  # Target height in meters

horizontal_distance = horizontal(angle, range_, h_target)
print(f"Horizontal distance at height {h_target} meters: {horizontal_distance:.2f} meters")

# h=[]
# r = [
#     1.3, 1.9, 1.8, 2.3, 2.35, 2.5, 2.2, 2.65, 2.55, 2.7, 3.4, 3.1, 3.35, 3.5, 3.7, 3.75,
#     3.3, 3.2, 3.6, 3.45, 3.9, 3.65, 4.1, 3.85, 4.0, 4.4, 4.5, 4.6, 4.7, 4.3, 2.25, 2.1,
#     2.6, 2.15, 2.4, 2.75, 3.0, 3.55, 3.8, 4.05, 4.25, 4.2, 4.45, 4.55, 4.9, 4.8, 5.1, 5.0,
#     5.3, 5.7, 5.4, 5.5, 5.6, 5.9, 5.8, 6.0, 6.2, 6.35, 6.3, 6.6, 6.5, 6.1
# ]
# for i in r:
#     horizontal_distance = horizontal(v, 58.03, 2.43)
#     h.append(horizontal_distance)
# print(h)