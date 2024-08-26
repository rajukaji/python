def extend_vowels(word, n):
    return ''.join([i*n if i.lower() in 'aeiou' else i for i in word])

   # return ''.join(word) if word.lower() in 'aeiou' for i in word else word




#join with each vowel multiplied by n times, else, its only 1 time

print(extend_vowels('apple', 3))
#
