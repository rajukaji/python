import numpy as np

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numpyArray = np.array(lst)

numpyArray[numpyArray % 2 == 0] = 0 #assign 0 to all the even elements

print(numpyArray)

print(numpyArray[[1, 0, 3]])# index inside index,, this is used to only select the indexed at 1, 0, and 3