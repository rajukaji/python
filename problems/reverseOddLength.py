def reverse_odd_words(sentence):
    return ' '.join([i[::-1] if len(i) % 2 != 0 else i for i in sentence.split(' ')])


# revese odd length words in a sentence

print(reverse_odd_words('Hello, Kathmandu, pokhara, Rara, Lalitpur, Patan'))