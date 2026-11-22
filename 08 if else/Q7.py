
bill = float(input("Enter your bill amount: "))

if bill >= 5000:
    discount = bill * 10 / 100

elif bill >= 2000:
    discount = bill * 5 / 100

else:
    discount = 0

final_amount = bill - discount

print("Discount:", discount)
print("Pay:", final_amount)
