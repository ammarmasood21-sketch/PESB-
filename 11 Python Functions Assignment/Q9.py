# Create a function
def is_valid_mobile(number):

    # Check number length
    if len(number) != 12:
        return False

    # Check starting digits
    if number[0:2] != "03":
        return False

    # Check dash at index 4
    if number[4] != "-":
        return False

    # Check all other characters
    for i in range(len(number)):

        if i != 4 and not number[i].isdigit():
            return False

    return True


print(is_valid_mobile("0300-1234567"))
print(is_valid_mobile("0300 1234567"))
print(is_valid_mobile("1300-1234567"))
print(is_valid_mobile("030012345"))