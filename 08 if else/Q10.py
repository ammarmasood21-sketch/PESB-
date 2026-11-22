#real life problems

balance = int(input("Enter your balance: "))
price = int(input("Enter package price: "))

if balance >= price:
    remaining = balance - price
    print("Package activated")
    print("Remaining balance:", remaining)

else:
    needed = price - balance
    print("Insufficient balance, need Rs", needed, "more")