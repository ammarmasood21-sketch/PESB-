# Create a function
def pak_zindabad(n):

    result = []

    # Check numbers from 1 to n
    for i in range(1, n + 1):

        # Check if number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            result.append("PakZindabad")

        # Check if number is divisible by 3
        elif i % 3 == 0:
            result.append("Pak")

        # Check if number is divisible by 5
        elif i % 5 == 0:
            result.append("Zindabad")

        # Add the original number
        else:
            result.append(i)

    return result


print(pak_zindabad(15))