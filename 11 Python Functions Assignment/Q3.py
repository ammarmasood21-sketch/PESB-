# Create a function to count different characters
def count_types(text):

    # Start all counters from zero
    letters = 0
    digits = 0
    spaces = 0
    others = 0

    # Loop through every character in the text
    for char in text:

        # Check if the character is a letter
        if char.isalpha():
            letters += 1

        # Check if the character is a number
        elif char.isdigit():
            digits += 1

        # Check if the character is a space
        elif char == " ":
            spaces += 1

        # If it is not a letter, number or space
        else:
            others += 1

    # Return all four counts as a tuple
    return letters, digits, spaces, others


# Call the function and print the result
print(count_types("Pakistan 2026!"))