# Exercise 10: Return names of students who passed.
def filter_passed(students, pass_mark=50):
    passed = []

    for name, marks in students.items():
        if marks >= pass_mark:
            passed.append(name)

    return passed

students = {"Ali": 45, "Sara": 78, "Ahmed": 52, "Hina": 90}
print(filter_passed(students))
print(filter_passed(students, 60))
