import matplotlib.pyplot as plt

# Given distances
# Sorted distances and corresponding errors
# Sorted distances and corresponding errors
distances = [152, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450]
errors = [0, -2, -2, -2, -3, 3, 1, -5, 10, 0, 0, 2, 0]

# Plotting the data
plt.figure(figsize=(8, 5))
plt.plot(distances, errors, marker='o', linestyle='-', color='b', label='Error')

# Labels and title
plt.xlabel("Distance")
plt.ylabel("Error")
plt.title("Error vs Distance Plot")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
