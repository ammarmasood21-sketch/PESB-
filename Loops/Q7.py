products = [
    ("Laptop", 150000, 3),
    ("Mouse", 2500, 0),
    ("Keyboard", 5000, 12),
    ("Monitor", 45000, 2)
]
#products tells product name, price, inventory

total = 0 #starting value is 0

for name, price, quantity in products:

    if quantity == 0:
        print("Out of stock:", name)  #condition out of stock stock if 0

    elif quantity >= 1 and quantity <= 4:
        print("Low stock:", name)      #condition low stock if 4 or less then 4

    total = total + (price * quantity) #tell the total price of available stock

print("Total stock value:", total)    #tell the total left stock price.