numbers = [12, 7, 9, 20, 33, 48, 51]

result = {"even": 0, "odd": 0} #dictionary
#Contain Even and Odd

for number in numbers:

    if number % 2 == 0:
        result["even"] = result["even"] + 1 #tell how many are even

    else:
        result["odd"] = result["odd"] + 1 #tell how many are odd

print(result)