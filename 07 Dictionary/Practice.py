# Create a dictionary
#Store student information and print it.
student = {
    "name": "Ammar",
    "age": 25,
    "course": "Python",
    "city": "Bahawalpur"
}

# Print the complete dictionary
print(student)

# Get the student's name
print(student["name"])

# Get the student's age
print(student["age"])

# Get the student's course
print(student["course"])

#how to add new information, update existing information, and delete information.

# Create a dictionary
student = {
    "name": "Ali",
    "age": 22,
    "course": "Python"
}

# Print original dictionary
print(student)

# Add a new key and value
student["city"] = "Bahawalpur"
print(student)

# Update the student's age
student["age"] = 23
print(student)

# Delete the course information
del student["course"]
print(student)

