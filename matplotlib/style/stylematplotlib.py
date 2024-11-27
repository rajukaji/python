import matplotlib.pyplot as plt
import matplotlib.style as style

print(style.available)
# to see available styles for plotting graph

style.use('_classic_test_patch')
plt.plot([1, 2, 3], [5, 2, 7])
plt.show()

style.use('ggplot')
plt.plot([2, 4, 6], [10, 15, 5])
plt.show()

style.use('default')
plt.plot([2, 4, 6], [10, 15, 5])
plt.show()