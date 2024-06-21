#lambda expressions or lambda functions

#one line single anonymous function that we can pass to other functions

#lets take examples of tuple
#to sort the tuple

items = [
    ("mango", 20),
    ("rice", 2),
    ("APPLE", 5),
]

def Sort(item):
    return item[1]#return 2nd items of each iteration

items.sort(key=Sort)
print(items)

#we use now lambda anonymous function, we done need to define the functions as above

items.sort(key=lambda item:item[1])#items.sort(key=lambda parameters:expression)

print(items)
#syntax of lambda function one line function
#lambda parameters:expression