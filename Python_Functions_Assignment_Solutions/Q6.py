# Exercise 6: Return the smallest and largest numbers using a loop.
def min_max(numbers):
    low = numbers[0]
    high = numbers[0]

    for number in numbers:
        if number < low:
            low = number
        if number > high:
            high = number

    return low, high

low, high = min_max([45, 12, 89, 33])
print("Smallest:", low)
print("Largest:", high)
