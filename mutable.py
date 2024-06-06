x = 1
print(id(x)) #prints address of x

x = x + 1
print(id(x))

#prints different addrsses

x = [1, 3, 5]#list, or list of objects
#lists are mutable

print(id(x))

x.append(7)

print(id(x))

#numbers, strings, booleans, are immutables, 
#their values cannot be changed, therefore

#integers are immutable

