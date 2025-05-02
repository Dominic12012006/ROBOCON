def find_min_platforms(arrival, departure):
    n = len(arrival)
    arrival.sort()
    departure.sort()

    platforms_needed = 1
    max_platforms = 1
    i, j = 1, 0

    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        max_platforms = max(max_platforms, platforms_needed)
    return max_platforms

# Sample Input
arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

# Output
print("Minimum Platforms Needed:", find_min_platforms(arrival, departure))
