# Create a function
def print_triangle(n):

    # Outer loop controls the rows
    for i in range(1, n + 1):

        # Inner loop prints numbers in each row
        for j in range(1, i + 1):
            print(j, end=" ")

        # Move to the next line
        print()


# Call the function
print_triangle(4)