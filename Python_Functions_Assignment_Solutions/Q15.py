# Exercise 15: Generate a countdown using yield.
def countdown(n):
    while n >= 1:
        yield n
        n -= 1

for number in countdown(5):
    print(number)

print("Go!")
