num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Yes")

elif num % 5 != 0 or num % 11 != 0:
    print("No")