#looping over lists

letters = ["a", "b", "c"]

for letter in enumerate(letters):
    print(letter)
    print(letter[1])

#tuple is read only, 

#use enumerate to tuple list

#it will produce (index, list item)

items = (0, "a")#tuple

index, letter = items#this is the concept of tuple

for index, letter in enumerate(letters):#using list unpacking
    print(index, letter)#useful in listing items

