#when yo are working fo infinite sequences of data, like billion, using range to store is not possible

values = [x * 2 for x in range(10)]#using 10000000000 instead 10 is not possible

for x in values:
    print(x)


#using a generator objects, they are iterable just like list
#they dont store all the values in the memory

from sys import getsizeof

values = (x * 2 for x in range(10))
print(values)

for x in values:
    print(x)


values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
#generator doesn't produce the length of how many items it produce