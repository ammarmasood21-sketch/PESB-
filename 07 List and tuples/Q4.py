#level 2


# Original list
nums = [3, 1, 3, 2, 1, 5]

# Create an empty list
unique = []

# Check every number
for num in nums:

    # Check if number is not already in unique
    if num not in unique:

        # Add number to the new list
        unique.append(num)

# Print final list
print(unique)
