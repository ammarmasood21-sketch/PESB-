marks = [78, 45, 92, 33, 67, 88]

passed = 0        #intial value is 0

for mark in marks:        #for loop, list will be used marks

    if mark >= 40:                #marks must be equal to 40 or above 40.
        print(mark, "Pass")       #print the student marks with pass
        passed = passed + 1

    else:
        print(mark, "Fail")        # below 40 will be fail

print("Passed:", passed)           #tell how many passed.