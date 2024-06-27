#when yo are working fo infinite sequences of data, like billion, using range to store is not possible

values = [x * 2 for x in range(10)]#using 10000000000 instead 10 is not possible

for x in values:
    print(x)