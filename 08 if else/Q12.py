# Take distance from the user
km = float(input("Enter distance in km: "))

# Take the current hour from the user
hour = int(input("Enter hour (0-23): "))

# Calculate base fare and distance charges
fare = 100 + (40 * km)

# Check whether the ride is at night
if hour >= 22 or hour < 6:

    # Add 20% extra fare at night
    fare = fare + (fare * 0.20)

# Print the final fare
print("Final fare: Rs", fare)