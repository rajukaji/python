import numpy as np

ndarray = np.array([
    [1, 2, 3, 4],
    [2, 3, 4, 5], 
    [9, 0, 2, 3]
])

print(ndarray.max())
print(ndarray.min())
print(ndarray.mean())
print(ndarray.sum())

print(ndarray.max(axis=1))
# max value of each row

print(ndarray.max(axis=0))
# max value of each column
