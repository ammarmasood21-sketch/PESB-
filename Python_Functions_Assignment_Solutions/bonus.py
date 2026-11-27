# Bonus: Create a percentage calculator using a closure.
def make_percent(total):
    def calculate(obtained):
        return obtained / total * 100

    return calculate

out_of_50 = make_percent(50)
print(out_of_50(40))

out_of_75 = make_percent(75)
print(out_of_75(60))
