# Exercise 11: Check prime numbers and list primes up to n.
def is_prime(n):
    if n < 2:
        return False

    for number in range(2, n):
        if n % number == 0:
            return False

    return True


def primes_up_to(n):
    primes = []

    for number in range(2, n + 1):
        if is_prime(number):
            primes.append(number)

    return primes

print(is_prime(1))
print(is_prime(29))
print(primes_up_to(20))
