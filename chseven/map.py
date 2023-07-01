
from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return '_'.join(anagram)

words = ['adverb', 'pronoun', 'noun', 'adjective']
anagrams = []

# Using for loop

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)


# Uisng map

# result = list(map(jumble, words))
# print(result)

# Using 

print([jumble(word) for word in words])
