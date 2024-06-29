#program to find most repeated character in the text or sentence
from pprint import pprint


sentence = "This is a common interview question"

#solution, we have to know how many times each character is repeated
#we have Dictionary data structure to store these sorts of data value

mostCharRepeated = {}
for char in sentence:
    if char in mostCharRepeated:
        mostCharRepeated[char] += 1
    else:
        mostCharRepeated[char] = 1

print(mostCharRepeated)

#use pretty printing
pprint(mostCharRepeated, width=1)

print(sorted(mostCharRepeated.items(), key=lambda kv: kv[1]))