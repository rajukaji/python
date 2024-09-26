lst = set([1, 2, 3, 4, 5])
# converted into set

lst1 = {3, 4, 5, 6}

uni = lst & lst1
print(uni)
# intersection

#intersection with method
uni = lst.intersection(lst1)
print(uni)


# union of lst with lst1
# all of lst, but, only matched of lst1
# this is simply the first lst
uni = lst or lst1
print(uni)


uni = lst.union(lst1)
print(uni)
# it is a proper set union

uni.add(7)
uni.remove(6)
print(uni)
# add and remove methods of set


print(lst.issubset(lst1))
print(lst.issuperset(lst1))