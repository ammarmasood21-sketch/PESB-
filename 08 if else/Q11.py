# Take Matric marks from the student
matric = float(input("Enter Matric percentage: "))

# Take Intermediate marks from the student
inter = float(input("Enter Inter percentage: "))

# Take Entry Test marks from the student
entry_test = float(input("Enter Entry Test marks: "))

# Check admission eligibility using two possible conditions
if (matric >= 60 and inter >= 50) or entry_test >= 70:

    # If the condition is True, print Eligible
    print("Eligible")

# If the above condition is False
else:

    # Print Not eligible
    print("Not eligible")