# Create a function
def total_expense(*amounts, budget=5000):

    total = 0

    # Add all expenses
    for amount in amounts:
        total = total + amount

    # Calculate remaining money
    left = budget - total

    # Check the budget
    if total <= budget:
        status = "Within budget"
    else:
        status = "Over budget"

    return total, left, status


# Test the function
print(total_expense(1200, 800, 2500))
print(total_expense(3000, 2500))