#read only list
#sequential object
#cannot modify anything
#immutable

point = (1, 2, 3)
pointx = 1, 2, 3
pointy = 1,

print(type(point))
print(type(pointx))
print(type(pointy))

point = (1, 2) + (2, 3)
print(point)

point = (1, 2) * 3
print(point)

point = tuple([1, 2])
#pass iterables
print(point)

point = tuple("Tuple")
print(point)

print(point[0])
print(point[0:3])#slice

x, y, z, a, b = point
#unpack
#but, the number of tuples must equal to the variables

if 'p' in point:
    print("Exists")

