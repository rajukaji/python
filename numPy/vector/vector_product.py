import numpy as np

u = np.array([1, -1])

v = np.array([1, 1])

z = u*v

print(z)

# can also do with the dot product, 

z = np.dot(u, v)

print(z) 
# but this is not matrix multiplication, dot product
