# Exercise 7: Calculate the average of marks using *args.
def average(*marks):
    if len(marks) == 0:
        return 0

    total = 0
    for mark in marks:
        total += mark

    return total / len(marks)

print(average(80, 90, 70))
print(average(55, 65))
print(average())
