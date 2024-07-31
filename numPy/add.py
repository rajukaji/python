import numpy as np

lst1 = np.array([1, 2, 3, 4, 5])
lst2 = np.array([1, 2, 3, 4, 5])

print(lst1 + lst2)

print(np.add(lst1, lst2))
print(np.subtract(lst1, lst2)) # or use - operator

print(np.divide(lst1, lst2)) # float divide
