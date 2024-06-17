#sorting lists
number = [2, 5, 1, 10, 2, 1, 0, 20, 50, 30, 19, -20, -5]

number.sort()#method
#ascending order

print(number)

number.sort(reverse=True)#descending order

print(number)

#buildin function sorted(tosortlist)
#returns new list that is sorted


print(sorted(number))#sort ascending order


print(sorted(number, reverse=True))#descending order


#tuples sort

items = [
    ("Product1", 10),
    ("Product2", 29),
    ("Product3", 50),
]

items.sort()
print(items) #nothing changes


#we need to define a function

def sortItem(item):
    #sort item based on price
    return item[1]

items.sort(key=sortItem)#only pass reference of the function, not the function

print(items) 

print("sorted as per the price of the items")