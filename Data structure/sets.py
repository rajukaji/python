#set
#data structure
#collections with no duplicates
#not in order
#cannot use indexing fo sets 
#data are at random places

numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)

second = {1, 4}
#set defined
second.add(5)
second.remove(4)
print(len(second))

#important in powerful mathematical operations,

#to get the union of the set,
print(second | uniques)

#to get the intersection of the sets
print(second & uniques)

#subracting, only uniques
print(uniques - second)

#exclusive OR, that are not matched
#symmetric difference
print(second ^ uniques)

#we cannot index, so we cannot access using an index, only to check if the
#item is actually in the list of not. 
#eg

if 3 in uniques:
    print("Exists!")