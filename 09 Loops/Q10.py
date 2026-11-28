
cart = {}
#Create an empty dictionary

while True:                           #Start an infinite loop
    print("\n1. Add item")
    print("2. View cart")
    print("3. Checkout")
#Display the menu
#\n means start a new line with some spacing.

    choice = input("Enter your choice: ")

#Add an item

    if choice == "1":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))

        cart[name] = price

        print("Item added successfully!")

#View the cart

    elif choice == "2":
        total = 0

        for name, price in cart.items():
            print(name, "Rs", price)
            total = total + price

        print("Total: Rs", total)

    elif choice == "3":
        total = 0

        for price in cart.values():
            total = total + price

        if total > 5000:
            discount = total * 10 / 100
            final_amount = total - discount
            print("Discount: Rs", discount)
        else:
            final_amount = total

        print("Total: Rs", total)
        print("Final Amount: Rs", final_amount)         #print and stop the loop

        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice! Try again.")
