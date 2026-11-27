students = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 76,
    "Hina": 58,
    "Bilal": 64
}
#We created a dictionary

total = 0 #initial value is 0

for name, marks in students.items(): #tell the name and marks 

    total = total + marks
     #condition applied greater then and equal

    if marks >= 80:      
        print(name, "A")

    elif marks >= 70:
        print(name, "B")

    elif marks >= 60:
        print(name, "C")

    else:
        print(name, "F")

average = total / len(students)  #Average result of Class

print("Average:", average)