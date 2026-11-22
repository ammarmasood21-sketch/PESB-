
# Create original list
a = [1, 2, 3]

# b refers to the same list as a
b = a

# c creates a separate copy of a
c = a.copy()

# Add 4 to list a
a.append(4)

# Print all lists
print(a)
print(b)
print(c)

# Explanation:
# b changed because b and a refer to the same list.
# c did not change because copy() created a separate list.
