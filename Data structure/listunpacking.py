numbers = [1, 2, 3]

first = numbers[0]
second = numbers[1]
thrid= numbers[2]

#to achieve this easily

first, second, third = numbers #this is called list unpacking

print(numbers)

numbers = [1, 2, 3, 4, 5, 5, 6, 7]

first, second, *others, last = numbers#first and second value unpacking
#others is the rest of teh list

print(first, last)

print(others)

#this is all about list unpacking

