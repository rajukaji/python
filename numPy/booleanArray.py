import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3
print(a_bool)

b_bool = b == 'blue'
print(b_bool)

c_bool = c > 100
print(c_bool)

# Think of the Boolean array as a filter: True values make the cut, 
# while False values are left behind.

result = c[c_bool]
# only true items

print(result)

column_bool = [True, False, True, True]

print(c[column_bool])