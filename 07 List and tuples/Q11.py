
scores = [45, 82, 67, 91, 73]

highest = 0
second_highest = 0

for score in scores:

    if score > highest:
        second_highest = highest
        highest = score

    elif score > second_highest:
        second_highest = score

print("Second highest score:", second_highest)
