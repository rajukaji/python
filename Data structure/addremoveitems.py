letters = ["a", "b", "c"]

#to add use append() method at the end of the list

letters.append("d")
print(letters)

#insert() method to any specific location

letters.insert(0, "-")#at [[position 0]]
print(letters)

#pop() method to remove object at the end of the list

letters.pop()

print(letters)

letters.pop(2)#remove with index
print(letters)

letters.remove("a")#remove first object b in teh list
print(letters)

#del statement to delete an item or range of items, while pop() will only delete one item

del letters[0]#or range of items# del letters[0:3]

#remove all the objects in the list, use clear() methon

letters.clear()
print(letters)

 

