# Reading euro-daily-hist_1999_2020.csv file

import pandas as pd
# Importing pandas
import matplotlib.pyplot as plt
# Importing matplotlib.pyplot

exchange_rates = pd.read_csv('euro-daily-hist_1999_2020.csv')
# Reading file

exchange_rates.info()
# See info, number of rows columns, null values, data types

exchange_rates.rename(columns={'[US dollar ]': 'US_dollar',
                               'Period\\Unit:': 'Time'},
                      inplace=True)
# Rename '[US dollar]' column to 'US_dollar'
# Rename '[Period\\Unit:]' column to 'Time'

exchange_rates['Time'] = pd.to_datetime(exchange_rates['Time'])
# Convert '[Time]' column to datetime 

exchange_rates.sort_values('Time', inplace=True)
# Sorting In ascending order as per '[Time]' column

exchange_rates.reset_index(drop=True, inplace=True)
# Reset the index(and drop the initial index)

euro_to_dollar = exchange_rates[['Time', 'US_dollar']]
# Isolating ['Time'] and ['US_dollar'] columns only

print(euro_to_dollar.head())
euro_to_dollar['US_dollar'].value_counts()

# Dropping '-'
euro_to_dollar = euro_to_dollar[euro_to_dollar['US_dollar'] != '-']
# Only data without '-' character
euro_to_dollar.value_counts()

euro_to_dollar['US_dollar'] = euro_to_dollar['US_dollar'].astype(float)
# Converting ['Us_dollar'] column to floating type

euro_to_dollar.info()

# Plotting line graph
plt.plot(euro_to_dollar['Time'], euro_to_dollar['US_dollar'])
plt.show()

euro_to_dollar['rolling_mean'] = euro_to_dollar['US_dollar'].rolling(30).mean()
# Creating a new column 'rolling_mean' this is a moving average of 30 days apart.

euro_to_dollar.tail(5)


plt.plot(euro_to_dollar['Time'], euro_to_dollar['rolling_mean'])
# Plotting the US dollar with moving avera

before_corona = euro_to_dollar.copy()[(euro_to_dollar['Time'].dt.year >= 2016) & (euro_to_dollar['Time'].dt.year <= 2019)]
# data before corona period from 2016 to 2019
before_corona.head()

after_corona = euro_to_dollar.copy()[(euro_to_dollar['Time'].dt.year >= 2019) & (euro_to_dollar['Time'].dt.year <= 2021)]
# data after corona period from 2019 to 2021
after_corona.head()

# before and after corona period
before_and_after_corona = euro_to_dollar.copy()[(euro_to_dollar['Time'].dt.year >= 2016) & (euro_to_dollar['Time'].dt.year <= 2021)]
before_and_after_corona  

# adding fivethirtyeight style
plt.style.available
plt.style.use('fivethirtyeight')

# we will create 3 graphs, one before corona period, after corona period, and including both period
# using subplots, grid chart
plt.figure(figsize=(15, 6))
ax1 = plt.subplot(2, 2, 1) 
# first row first column first graph

ax2 = plt.subplot(2, 2, 2)
# first row 2nd column 2nd graph

ax3 = plt.subplot(2, 1, 2)
# second row with only 1 column, only 1 graph

axes = [ax1, ax2, ax3]

# making the same changes to all the plots
for ax in axes:
    ax.set_ylim(0.8, 1.7)
#     only from 0.8 to 1.7 limit
    ax.set_yticks([1.0, 1.2, 1.4, 1.6])
    ax.set_yticklabels(['1.0', '1.2', '1.4', '1.6'], alpha = 0.3)
#     y ticks labeled
    ax.grid(alpha=0.5)
#     alpha is transparency


# ax1 before corona
ax1.plot(before_corona['Time'], before_corona['rolling_mean'], color='#BF5FFF')

# print(ax1.get_xticks())
# to see the xticks positions

ax1.set_xticks([16801, 16983, 17167, 17348, 17532, 17713, 17897, 18078, 18262])
# these are the positions we get

ax1.set_xticklabels(['', '2016', '', '2017', '', '2018', '',  '2019', ''], alpha=0.3)
# we set the tick labels now with a perfect combination of positions for a redeable placements

ax1.text(17250, 1.92, 'Before Corona', weight='bold', fontsize=18, color='#BF5FFF')
ax1.text(17300, 1.8, '(2016-2019)', weight='light', fontsize=16, color='grey', alpha=0.5)
# text to legend/label the type of graph

# ax2 after corona
ax2.plot(after_corona['Time'], after_corona['rolling_mean'], color='#ffa500')
# print(ax2.get_xticks())

ax2.set_xticks([17897, 17987, 18078, 18170, 18262, 18353, 18444, 18536, 18628])
ax2.set_xticklabels(['2019', '', '', '', '2020', '', '', '', '2021'], alpha=0.3)

ax2.text(18078, 1.92, s='After Corona', weight='bold', fontsize=18, color='#ffa500')
ax2.text(18100, 1.8, s='(2019-2021)', weight='light', fontsize=16, color='grey', alpha=0.5)

# ax3 before and after corona
ax3.plot(before_corona['Time'], before_corona['rolling_mean'], color='#BF5FFF')
ax3.plot(after_corona['Time'], after_corona['rolling_mean'], color='#ffa500')

ax3.grid(alpha=0.5)
# print(ax3.get_xticks())
# to see the xticks positions to set the signature later on
         
ax3.set_xticks([])
# removing x ticks for the last graph

# finally adding signature
ax3.text(16670, 0.70, '©Raju' + ' '*155+ 'Source: European Central Bank',
        color = '#f0f0f0', backgroundcolor = '#4d4d4d',
        size=14)

