import matplotlib.pyplot as plt

years = [1990, 2000, 2010, 2020, 2030, 2040]
growth = [20000, 30000, 15000, 500000, 200000, 1500000]

plt.scatter(years, growth)
plt.title('scatter plot')
plt.legend(['China'])

plt.show()