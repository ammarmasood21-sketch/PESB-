char = input("Enter one character: ")

if char.isdigit():
    print("Digit")

elif char.isalpha():
    if char.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

else:
    print("Special character")