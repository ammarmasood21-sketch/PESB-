# Create a function to format the name
def format_name(name):

    # Remove extra spaces from the beginning and end
    name = name.strip()

    # Split the name into separate words
    words = name.split()

    # Capitalize the first letter of every word
    full_name = " ".join(word.capitalize() for word in words)

    # Create an empty string for initials
    initials = ""

    # Loop through every word
    for word in words:

        # Take the first letter and make it uppercase
        initials = initials + word[0].upper() + "."

    # Return full name and initials as a tuple
    return full_name, initials


# Call the function
print(format_name(" muhammad ali khan "))