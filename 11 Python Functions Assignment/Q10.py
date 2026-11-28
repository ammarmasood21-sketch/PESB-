# Check if number is even
def is_even(n):
    return n % 2 == 0


# Check if number is prime
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Calculate sum of digits
def digit_sum(n):

    total = 0

    for digit in str(n):
        total = total + int(digit)

    return total


# Analyze the number
def analyze(n):

    even = is_even(n)
    prime = is_prime(n)
    digits = len(str(n))
    total = digit_sum(n)
    palindrome = str(n) == str(n)[::-1]

    return even, prime, digits, total, palindrome


# Test the functions
print(analyze(121))
print(analyze(13))