
# Starting balance
balance = 10000

# Empty list to save transactions
history = []

# Keep showing the menu
while True:

    # Display menu options
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    # Ask user to select an option
    choice = input("Enter your choice: ")

    # If user selects Deposit
    if choice == "1":

        # Ask for deposit amount
        amount = float(input("Enter deposit amount: "))

        # Add money to balance
        balance = balance + amount

        # Save deposit in history
        history.append("Deposited Rs " + str(amount))

        print("Deposit successful!")
        print("New balance:", balance)

    # If user selects Withdraw
    elif choice == "2":

        # Ask for withdrawal amount
        amount = float(input("Enter withdrawal amount: "))

        # Check if money is greater than balance
        if amount > balance:
            print("Insufficient balance")

        else:
            # Subtract money from balance
            balance = balance - amount

            # Save withdrawal in history
            history.append("Withdrawn Rs " + str(amount))

            print("Withdrawal successful!")
            print("Remaining balance:", balance)

    # If user selects Check balance
    elif choice == "3":

        # Display current balance
        print("Current balance:", balance)

    # If user selects Exit
    elif choice == "4":

        # Display transaction history
        print("\nTransaction History:")

        # Print every saved transaction
        for transaction in history:
            print(transaction)

        # Display thank you message
        print("Thank you for using our bank!")

        # Stop the loop
        break

    # If user enters an invalid option
    else:
        print("Invalid choice! Try again.")
