#to deal with large sequential numbers, 
#takes less memorry, 
#faster
#only if you deal with large list of numbers

#import from array module
from array import array
#first array module, 2nd is the class 

numbers = array("i", [1, 2, 3])
#"i" is type code, that meals a signed integer
#cannot add other types, like float to this integer type
#otherwise, you get the type error
numbers.append(4)
numbers.pop()
numbers.insert(3, 1)
print(numbers)

#typecode search online
#only to deal with larger numbers of elements
#for performance, 
#else, use list, tuple