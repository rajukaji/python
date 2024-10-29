import numpy as np

np.genfromtxt(filename, delimiter=None)
np.genfromtxt('file.csv', delimiter=',', skip_header=1)
# for comma separated values
# skip_header=1 to avoid the first row, header section
# the ndarray is only of a single type, so it can be float64, etc.