temperature = int(input("Enter temperature in Celsius: "))

if temperature < 10:
    print("Cold, wear a jacket")

elif temperature <= 25:
    print("Pleasant")

elif temperature <= 35:
    print("Warm")

else:
    print("Very hot, stay hydrated")