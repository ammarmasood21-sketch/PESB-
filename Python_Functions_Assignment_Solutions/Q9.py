# Exercise 9: Count words in a sentence and return a dictionary.
def count_words(sentence):
    word_counts = {}
    words = sentence.lower().split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

print(count_words("The cat and the dog and the bird"))
