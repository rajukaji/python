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

# it can be done using a for loop
for ax in axes:
    ax.plot(death_toll['Month'], death_toll['New_deaths'], color='#af0b1e', alpha=0.1)
    # alpha reduce transparency, color red for all the line charts
#     plot 4 rows 1 cols

    ax.set_xticklabels([])
    ax.set_yticklabels([])
#     remove both labels

    ax.tick_params(axis='both', which='both', bottom=False, left=False)
#     removing ticks x and y

    ax.spines[:].set_visible(False)
#     removing box

# now taking month by month period
# we will draw the same graph once again, over the previous line chart, this is how we will highlight month by month

axes[0].plot(death_toll['Month'][:3], death_toll['New_deaths'][:3],
         color='#af0b1e', linewidth=2.5)
# jan to march
#     line width to hightlight the months taken with bold width
#     color to choose a color to highlight for the line

axes[1].plot(death_toll['Month'][2:6], death_toll['New_deaths'][2:6],
         color='#af0b1e', linewidth=2.5)
# march to june

axes[2].plot(death_toll['Month'][5:10], death_toll['New_deaths'][5:10], color='#af0b1e', linewidth=2.5)
# june to oct

axes[3].plot(death_toll['Month'][9:12], death_toll['New_deaths'][9:12], color='#af0b1e', linewidth=2.5)
# oct to dec


axes[0].text(0.5, -80, '0', alpha=0.5)
axes[0].text(3.5, 2000, '1,844', alpha=0.5)
axes[0].text(11.5, 2400, '2,247', alpha=0.5)
# label added for each points
# first graph



axes[1].text(0.5, -80, '0', alpha=0.5)
axes[1].text(3.5, 2000, '1,844', alpha=0.5)
axes[1].text(11.5, 2400, '2,247', alpha=0.5)
# 2nd graph

axes[2].text(0.5, -80, '0', alpha=0.5)
axes[2].text(3.5, 2000, '1,844', alpha=0.5)
axes[2].text(11.5, 2400, '2,247', alpha=0.5)
# 3rd graph

axes[3].text(0.5, -80, '0', alpha=0.5)
axes[3].text(3.5, 2000, '1,844', alpha=0.5)
axes[3].text(11.5, 2400, '2,247', alpha=0.5)
# 4th graph

axes[0].text(1.1, -300, 'Jan - Mar', color='#af0b1e',
         weight='bold', rotation=3)
# to add label for the highlighted specific month

axes[1].text(3.7, 800, 'Mar - Jun', color='#af0b1e', weight='bold')
axes[2].text(7.1, 500, 'Jun - Oct', color='#af0b1e', weight='bold')
axes[3].text(10.5, 600, 'Oct - Dec', color='#af0b1e', weight='bold', rotation=45)
# rotation to rotate the text

# add title to the first axes object
# write title and subtitle with axes.text(x, y, s, size, weight)
# x y cordinate, fontsize, and weight bold

axes[0].text(0.5, 3500, s='The virus kills 851 people each day', size=14, weight='bold')

# subtitle
axes[0].text(0.5, 3150, 'Average number of daily deaths per month in the US', size=12)

# creating horizontal line 
# Make the line shorter — we control the line's length using xmin and xmax parameters.
# Increase the line's width to make it look like a rectangle — we use the linewidth parameter.
# Change the color to '#af0b1e' and increase its transparency — we use the color and alpha parameters.

axes[0].axhline(y=1600, xmin=0.5, xmax=0.8, linewidth=6, color='#af0b1e', alpha=0.1)
axes[1].axhline(y=1600, xmin=0.5, xmax=0.8, linewidth=6, color='#af0b1e', alpha=0.1)
axes[2].axhline(y=1600, xmin=0.5, xmax=0.8, linewidth=6, color='#af0b1e', alpha=0.1)
axes[3].axhline(y=1600, xmin=0.5, xmax=0.8, linewidth=6, color='#af0b1e', alpha=0.1)

# we can do is create line and add values as below
for ax, xmax, death in zip(axes, xmax_vals, deaths):
    ax.axhline(y=1600, xmin=0.5, xmax=0.8,
               linewidth=6, color='#af0b1e',
               alpha=0.1)
    # created the line with low transparency

    ax.axhline(y=1600, xmin=0.5, xmax=xmax,
               linewidth=6, color='#af0b1e')

    ax.text(7.5, 1850, format(death,','), color='#af0b1e', weight='bold')
    # to label horizontol line we created with death numbers

plt.show()