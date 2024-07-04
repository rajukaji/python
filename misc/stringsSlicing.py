#extracting elements from another string
#slicing
#by indexing[] or slice( , ,) function
# 3 optional arguements
# [start:stop:step]

#creating a subsstring

name = "Kath Mandu"

firstPart = name[0 : 4]#4 is exclusive, print from o index to 3

print(firstPart)

lastPart = name[5 :]#print all after index 5
print(lastPart)

evenIncrease = name[ : : 2]
print(evenIncrease)

reverse_name = name[: : -1]#reverse a string in python
print(reverse_name)

website = "https://google.com"

slice = slice(8, -4)#-4 = .

print(website[slice])