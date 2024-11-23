import pandas as pd
import matplotlib.pyplot as plt

death_toll= pd.read_csv('covid_avg_deaths.csv')

# https://data.who.int/dashboards/covid19/cases
# data

# creating plot with subplots that returns tuple of figure and axes
# for mobilefriendly, we set wight 6 and height 8 with figsize

# directly accessing object wtih axes[index]

# plotting line graph

fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(6, 8))
axes[0].plot(death_toll['Month'], death_toll['New_deaths'])
axes[1].plot(death_toll['Month'], death_toll['New_deaths'])
axes[2].plot(death_toll['Month'], death_toll['New_deaths'])
axes[3].plot(death_toll['Month'], death_toll['New_deaths'])
plt.show()