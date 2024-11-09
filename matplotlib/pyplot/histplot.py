import matplotlib.pyplot as plt

horizontol = [0, 1, 2, 3, 4, 5]
vertical = [1, 2, 4, 5, 7, 6]

plt.hist(horizontol, bins=3)
# or without bins
plt.show()

plt.clf()
# clean above show
plt.hist(vertical)

plt.show()