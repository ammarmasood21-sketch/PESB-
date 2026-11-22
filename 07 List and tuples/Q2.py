
# Create a list of marks
marks = [78, 92, 65, 88, 54]

# Calculate total
total = 0

for mark in marks:
    total = total + mark

print(total)

# Calculate average
average = total / len(marks)

print(average)

# Find highest and lowest
print(max(marks))
print(min(marks))

# Count marks above 70
count = 0

for mark in marks:
    if mark > 70:
        count = count + 1

print("Above 70:", count)
