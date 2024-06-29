number = [1, 2, 3]
print(number)
print(1, 2, 3)#to get output like this

#using unpacking operator
#in js we can use spread operator ... 3 dots, its the same

number = [1, 2, 3]
print(*number)#this is the unpacking operator, to get outputs without list

values = list(range(5))#printing 0 to 4
print(values)

#now without using the list
values = [*range(5), *"unpack"]#the outputs are stored in the values as a list
print(values)

