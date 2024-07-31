import numpy as np

#size attribute of array numpy

lst = [1, 2, 3, 5, 6, 5]

numpyArray = np.array(lst)
print(numpyArray)#print the list of array
print(numpyArray.size)#print the size of array
print(numpyArray.nbytes)#total size of entire array

#ndim dimension of array 
print(numpyArray.ndim)#dimention 1d 2d 3d, nested array

print(numpyArray.shape)#how many elements in each nested array
print(type(numpyArray.shape))#returns tuple

#dtype for datatype
print(numpyArray.dtype)#int64