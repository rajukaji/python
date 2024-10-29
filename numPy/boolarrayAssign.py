import numpy as np

a2 = np.array([1, 2, 3, 4, 5])
a2_bool = a2 > 2
a2[a2_bool] = 99
print(a2)

a2[a2>2] = 88
print(a2)