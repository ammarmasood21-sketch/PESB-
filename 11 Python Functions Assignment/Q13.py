# Create a function
def check_guesses(secret, guesses, max_tries=5):

    # Start counting tries
    tries = 0

    # Check each guess
    for guess in guesses:

        tries = tries + 1

        # Stop if maximum tries are reached
        if tries > max_tries:
            break

        # Check if guess is correct
        if guess == secret:
            return "Won in " + str(tries) + " tries"

    # If no correct guess is found
    return "Lost, the number was " + str(secret)


# Test the function
print(check_guesses(7, [3, 9, 7]))
print(check_guesses(7, [1, 2, 3, 4, 5, 7]))