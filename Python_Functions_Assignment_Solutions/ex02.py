# Exercise 2: Return a welcome message using a default course.
def greet_student(name, course="Python"):
    return f"Welcome {name} to the {course} class"

print(greet_student("Sara"))
print(greet_student("Ali", "Django"))
