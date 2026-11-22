votes = ("A", "B", "A", "C", "A", "B")

# Count votes for each candidate
print("A =", votes.count("A"))
print("B =", votes.count("B"))
print("C =", votes.count("C"))

# Find the position of the first C
print("First C at index:", votes.index("C"))