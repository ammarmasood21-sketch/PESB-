nums = [3, 5, 3, 8, 5, 3, 9]

count = {}

for num in nums:
    if num in count:
        count[num] += 1  
    else:
        count[num] = 1

unique = list(count.keys())

#count the numbers total in string without repeated values.

most = 0

for num, frequency in count.items():
    if frequency > most:
        most = frequency
        most_number = num

        #tell the repeated values and store them

print("Unique:", unique)
print("Most frequent:", most_number, "(", most, "times)")