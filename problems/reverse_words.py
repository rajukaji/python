def reverse_words(text):
  #go for it
    return ' '.join(i[::-1] for i in text.split(' '))


print(reverse_words('hello, kathmandu, Nepal!'))