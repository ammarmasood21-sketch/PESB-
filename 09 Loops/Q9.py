
students = [
    {"name": "Ali", "marks": [80, 75, 90]},
    {"name": "Sara", "marks": [95, 88, 92]},
    {"name": "Ahmed", "marks": [55, 62, 48]}
]
#Create the student record

topper_name = ""
highest_average = 0

for student in students:          #Start the loop

    name = student["name"]
    marks = student["marks"]
#We use dictionary keys to get information.

    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)           #average = total / len(marks) calculate average

    if average >= 60:
        result = "Pass"
    else:
        result = "Fail"                      #Check Pass or Fail

    print(name, round(average, 2), result)

    if average > highest_average:
        highest_average = average
        topper_name = name

#Find the topper

print("Topper:", topper_name)
