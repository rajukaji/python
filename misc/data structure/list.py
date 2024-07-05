#list
#store multiple items within single variale.
food = ["pizza", "fruit", 25, "garlic"]
print(food)
#you can index too
print(food[3])
for i in food:
    print(i, end=", ")

#important functions
food.append("ice cream")#append at last
food.remove(25)
food.pop()#remove the last element
food.insert(0, "cake")#insert at index 0
food.sort()#sort alphabetically
food.clear()#remove all of the elements of the list