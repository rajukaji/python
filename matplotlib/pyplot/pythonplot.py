import matplotlib.pyplot as plt

x_coordinates = [1, 2, 3, 4, 5]

y_coordinates = [100, 200, 300, 400, 500]

plt.plot(x_coordinates, y_coordinates)
plt.ticklabel_format(axis='x', style='plain')
plt.title('matploptlib.pyplot')
plt.xlabel('months')
plt.ylabel('population')

plt.show()