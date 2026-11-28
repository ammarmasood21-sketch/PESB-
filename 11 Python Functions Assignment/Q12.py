# Create a function
def reverse_text(text):

    # Stop when text has one or zero characters
    if len(text) <= 1:
        return text

    # Reverse the remaining text and add the first letter
    return reverse_text(text[1:]) + text[0]


# Call the function
print(reverse_text("Lahore"))