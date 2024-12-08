import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import os
# print(os.getcwd())

happiness2015 = pd.read_csv('2015.csv')
# to work with file, first make the cwd the current folder, python/datacleaning

first_5 = happiness2015.head(5)

happiness2015.info()

# visualize
happiness2015['Happiness Score'].plot(kind='bar', title='Happiness Scores', ylim=(0,10))
plt.show()

unique_regions = happiness2015['Region'].unique()
# finding unique regions

so_asia = happiness2015[happiness2015['Region'] == 'Southern Asia']
so_asia.plot(x='Country', y='Happiness Score', kind='barh', title='Southern Asia Happiness Scores', xlim=(0,10))
# plotting only one region
plt.show()

'''
In this lesson, we'll learn how to perform different kinds of aggregations, applying a statistical operation to groups of our data, and create visualizations like the one above.

Our process will look like this:

Identify each unique group in the data set.
For each group, we'll do the following:
select only the rows corresponding to that group
calculate the average for those rows
Let's use this process to find the mean happiness score
for each region.
'''

mean_happiness = {}

regions = happiness2015['Region'].unique()
print(mean_happiness)
# there are 10 regions

for region in regions:
    region_group = happiness2015[happiness2015['Region'] == region]
    # aggregate region group for specific region
    #1. Split the DataFrame into groups.

    region_mean = region_group['Happiness Score'].mean()
    #2. Apply a function to each group.

    mean_happiness[region] = region_mean
    # adding to the dictionary
    #3. Combine the results into one data structure.

''''
    The groupby operation performs the "split-apply-combine" 
    process on a DataFrame, but it condenses it into two steps:
- create a GroupBy object
- call a function on the GroupBy object
    '''


# using df.groupby() method

grouped = happiness2015.groupby('Region')

# using groupby.get_group() method to select the data
aus_nz = grouped.get_group('Australia and New Zealand')
print(aus_nz)

print(grouped.groups)
# getting more information
# gives indest of the corresponding region/column name

# now checking one of the result if the index given by groupby.groups
# is either correct or not
# print(grouped.groups)
#  to analyze index of North America countries only
# result:
# 'North America': Int64Index([4, 14], dtype='int64'

north_america = happiness2015.iloc[[4, 14]]
print(north_america)

na_group = grouped.get_group('North America')
print(na_group)


equal = north_america == na_group
# comparing

print(equal)


print(grouped.size())
# aggregation methods, basic
# https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
# common aggregation methods
''''
Methods	Description
mean()	Calculates the mean of groups.
sum()	Calculates the sum of group values.
size()	Calculates the size of the groups.
count()	Calculates the count of values in groups.
min()	Calculates the minimum of group values.
max()	Calculates the maximum of group values.
'''


'''
Because we might be working with columns of dfferent data types,
it's often good practice to specify the numeric_only parameter for
 aggregation methods like mean(), sum(), min(), and max() to avoid 
 TypeErrors. This parameter determines whether to include
   only numeric columns in the computation. By setting 
   numeric_only=True, we ensure that only numeric columns are
   considered for the aggregation, avoiding potential errors 
   with non-numeric data.
'''
# same as 
print(happiness2015['Region'].value_counts())


means = grouped.mean(numeric_only=True)
print(means)

# we can do is 
# happiness2015.groupby('Region').mean()
# mean is an aggregation function that returns value now
# since grouped is an object, we used object.method() previously
# like grouped.mean()

# after groupby, we can either include all the columns as default
# or only choose the column(s) as needed as follows
'''
Select by Label	Syntax

Single column	=> GroupBy["col1"]
List of columns	=> GroupBy[["col1", "col2"]]

'''

happy_grouped = grouped['Happiness Score']
happy_mean = happy_grouped.mean()
# numeric_only=True is optional as we are only working
# with one column which we know is numeric type

print(happy_grouped)
# the column is still an object

print(happy_mean)

# if we want multiple aggregation(function) to implement at the sametime
'''
pandas.core.groupby.DataFrameGroupBy.agg
DataFrameGroupBy.agg(func=None, *args, engine=None,
 engine_kwargs=None, **kwargs)

 ie. groupby.agg([function1, function2, function3, function4])
'''

'''
Note that when we pass the functions into the agg() method
 as arguments, we don't use parentheses after the function names. 
 For example, when we use np.mean, we refer to the function object 
 itself and treat it like a variable, whereas np.mean() would 
 be used to call the function and get the returned value.
'''

grouped = happiness2015.groupby('Region')
happy_grouped = grouped['Happiness Score']

happy_mean_max = happy_grouped.agg([np.mean, np.max])
# we can either pass without the numpy, but, 
# mean and max method only can also be passed

def dif(group):
    return group.max() - group.mean()


mean_max_dif = happy_grouped.agg(dif)


happiness_means = happiness2015.groupby('Region')['Happiness Score'].mean()
# combined 


pv_happiness = happiness2015.pivot_table(values='Happiness Score', index='Region', aggfunc=np.mean)
# we can also use the pivot table for the aggregation same as above
# note: mean is the default aggregation of pivot table
'''
pandas.DataFrame.pivot_table
DataFrame.pivot_table(values=None, index=None, columns=None,
 aggfunc='mean', fill_value=None, margins=False, dropna=True,
   margins_name='All', observed=<no_default>, sort=True)[source]

'''

pv_happiness = happiness2015.pivot_table('Happiness Score', 'Region')
pv_happiness.plot(kind='barh', title='Mean Happiness Scores by Region', xlim=(0,10), legend=False)
plt.show()


mean_min_max_by_region = happiness2015.pivot_table(
    value = 'Happiness Score', index='Region', aggfunc=[np.mean, np.min , np.max], margins=True)
# applying multiple function
# setting margins == True 


# Let's compare the results returned by the groupby
# operation and the pivot_table method.


grouped = happiness2015.groupby(by='Region')[['Happiness Score', 'Family']]
'''
Group happiness2015 by the Region column.
Select the Happiness Score and Family columns. Assign the result to grouped.
'''

happy_family_stats = grouped.agg([np.min, np.max, np.mean])
'''
Apply the GroupBy.agg() method to grouped. Pass a list containing np.min, np.max, and np.mean into the method.
Assign the result to happy_family_stats.
'''


'''
Use the pivot_table method to return the same information, but also calculate the minimum, maximum, and mean for the entire Family and Happiness Score columns.
'''
pv_happy_family_stats = happiness2015.pivot_table(values=['Happiness Score', 'Family'], index='Region', aggfunc=[np.min, np.max, np.mean], margins=True)
