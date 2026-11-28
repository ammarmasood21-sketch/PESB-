# Exercise 12: Check whether a word is a palindrome, ignoring capitals.
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(is_palindrome("Madam"))
print(is_palindrome("level"))
print(is_palindrome("python"))
