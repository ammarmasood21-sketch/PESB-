
# Keep asking for password
while True:

    # Take password from user
    password = input("Enter your password: ")

    # Check password length
    if len(password) < 8:
        print("Weak password (too short)")

    else:
        # Start both flags as False
        has_digit = False
        has_upper = False

        # Check every character in password
        for char in password:

            # Check if character is a number
            if char.isdigit():
                has_digit = True

            # Check if character is a capital letter
            if char.isupper():
                has_upper = True

        # Check all password conditions
        if has_digit and has_upper:
            print("Password accepted")
            break

        else:
            print("Weak password")
