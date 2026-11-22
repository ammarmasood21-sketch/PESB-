
students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)]

# 1. Print each student
for name, marks in students:
    print(name, "scored", marks)


# 2. Find the topper
topper_name = ""
highest_marks = 0

for name, marks in students:
    if marks > highest_marks:
        highest_marks = marks
        topper_name = name

print("Topper:", topper_name, highest_marks)


# 3. Find passed students
passed = []

for name, marks in students:
    if marks >= 70:
        passed.append(name)

print("Passed students:", passed)
