# Exercise 4: Return a grade based on marks.
def grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

print(grade(85))
print(grade(72))
print(grade(64))
print(grade(40))
