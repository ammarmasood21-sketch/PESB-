# Exercise 8: Print profile details using **kwargs and return their count.
def make_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

    return len(info)

count = make_profile(name="Sara", city="Multan", course="Python")
print("Number of details:", count)
