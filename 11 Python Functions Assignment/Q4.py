# Create a function
def merge_unique(list1, list2):

    # Create an empty list
    result = []

    # Join both lists
    numbers = list1 + list2

    # Check every number
    for num in numbers:

        # Assume the number is not repeated
        found = False

        # Check numbers already in result
        for x in result:

            # Check if number already exists
            if num == x:
                found = True

        # Add number if it is not repeated
        if found == False:
            result.append(num)

    # Sort the final list
    result.sort()

    # Return the final list
    return result


# Call the function
print(merge_unique([3, 1, 5], [5, 2, 3]))