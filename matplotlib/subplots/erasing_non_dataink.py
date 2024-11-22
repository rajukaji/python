import pandas as pd
import matplotlib.pyplot as plt
# less is more attractive and impactive
# we should show less by removing the redundants as well as non essential things from graph, like box lines, ticks

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
         top20_deathtoll['Total_Deaths'], 
         height=0.1, 
         color='#af0b1e')
# height=0.8 default thickness of the bars/candles, to reduce non dataink
# color for bar color

for location in ['left', 'right', 'bottom', 'top']:
    ax.spines[location].set_visible(False)
    # axes.spines[location] to remove the box, left, right, bottom, top with set_visible(False)
    
ax.tick_params(bottom=False, left=False)
# remove the ticks with tick_params, bottom, top, left, right
ax.set_xticks([0, 100000, 300000])
# only set less numbers of x labels ticks indicators
ax.xaxis.tick_top()
#now the x tick labels are shown at the top
ax.tick_params(top=False, left=False)
#remove the x ticks of the top 

ax.tick_params(axis='x', colors='grey')
# make the tick labels less bold for x axis on the top 

ax.text(x=-80000, y=23.5, s='The Death Toll Worldwide Is 1.5M+',
        size=17, weight='bold')
# x and y for x cordinates and y cordinates
# s for text for title
# size, size of font
# weight for font highlight

ax.text(x=-80000,
        y=22.5,
        size=12,
        s='Top 20 countries by death toll (December 2020)'
       )
ax.set_xticklabels(['0', '150,000', '300,000'])
# to make it more redeable we will label each item/numbers with this instead

ax.set_yticklabels([])
# empty list removes the labels

country_names = top20_deathtoll['Country_Other']
for i, country in zip(range(20), country_names):
    ax.text(x=-80000,
            y=i-0.15,
            s=country)
    # to left align y tick lables

    
# lets add a vertical line,

ax.axvline(x=150000, ymin=0.045, c='grey', alpha=0.5)

# - The ymin parameter to make it shorter — where 0 is the bottom of the plot, and 1 is the top of the plot.
# - The c parameter to change the color to 'grey'.
# - The alpha parameter to add transparency to the line.

plt.show()