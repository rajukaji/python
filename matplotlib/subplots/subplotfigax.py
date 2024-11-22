import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(8, 5))
# figsize=(width, height)
#returns two tuples, figure, and axes
# we create graph with axes.bar()
# this is object oriented approach
ax.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'])
plt.show()
