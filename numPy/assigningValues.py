# ndarray[location_of_values] = new_value
import numpy as np
a = np.array(['red', 'blue', 'black', 'blue', 'purple'])
a[0] = 'orange'
print(a)

# We can also update multiple values at once:

a[3:] = 'pink'
print(a)


# Now, let's try with a 2D ndarray. Just like with a 1D ndarray, we can change a specific index location:

ones = np.array([[1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1]])
ones[1, 2] = 99
print(ones)

# update the entire row
ones[0] = 2
print(ones)

# update entire column
ones[:, 3] = 3
print(ones)