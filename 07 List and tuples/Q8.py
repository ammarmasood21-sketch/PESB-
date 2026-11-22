
# Create a student tuple
student = ("BSIT-12", "Sara", 88)

# 1. Unpack the tuple
roll_no, name, marks = student

# Print using f-strings
print(f"Roll Number: {roll_no}")
print(f"Name: {name}")
print(f"Marks: {marks}")

# 2. Try changing the tuple
# student[2] = 95
# This gives TypeError because tuples are immutable.

# 3. Convert tuple into a list
student = list(student)

# Change the marks
student[2] = 95

# Convert list back into a tuple
student = tuple(student)

# Print updated student record
print("Updated student:", student)
