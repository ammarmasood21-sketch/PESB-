# Create a function to split the bill
def split_bill(total, people, tip_percent=10):

    # Calculate the tip amount
    tip = total * tip_percent / 100

    # Add the tip to the total bill
    total_bill = total + tip

    # Divide the bill equally among people
    share = total_bill / people

    # Round the share to 2 decimal places
    return round(share, 2)


# Call the function with 3000 bill and 4 people
print(split_bill(3000, 4))

# Call the function with 2500 bill, 3 people and 0% tip
print(split_bill(2500, 3, 0))