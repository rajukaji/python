list1 = [1, 2, 3]
list2 = [10, 20, 30]

#combine multiple list and put into tuple
#using zip()
#zip(iterable, ite, ite, tie, *)

print(list(zip(list1, list2)))

#can do
print(list(zip("abc", list1, list2)))
#we do not alway have to pass list to zip, but, 
#can also pass strings, 