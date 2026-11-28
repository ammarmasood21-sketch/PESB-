# Create a function
def class_report(records):

    total = 0
    highest = 0
    topper = ""
    below_60 = []

    # Check each student
    for name, marks in records:

        total = total + marks

        # Find the topper
        if marks > highest:
            highest = marks
            topper = name

        # Find students below 60
        if marks < 60:
            below_60.append(name)

    # Calculate average
    average = total / len(records)

    return round(average, 2), topper, below_60


records = [("Ali", 85), ("Sara", 92), ("Ahmed", 58)]

print(class_report(records))