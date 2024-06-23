#easy swap

x, y = 3, 4
print(x, y)

x, y = y, x
#this is exactly as x, y = (4, 3), tuple
#its like defining tuple on the right side and unpacking to the left
print(x, y)