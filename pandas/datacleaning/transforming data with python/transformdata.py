'''
 each of the columns below contains the estimated extent to which each factor contributes to the happiness score:

Economy (GDP per Capita)
Family
Health (Life Expectancy)
Freedom
Trust (Government Corruption)
Generosity
'''

'''
Below are descriptions for some of the other columns we'll work with in this lesson:

Country - Name of the country
Region - Name of the region the country belongs to
Happiness Rank - The rank of the country, as determined by its happiness score
Happiness Score - A score assigned to each country based on the answers to a poll
 question that asks respondents to rate their happiness on a scale of 0-10
Dystopia Residual- Represents the extent to which the factors above over or under
 explain the happiness score. 
'''

'''
Which of the factors above contribute the most to the happiness score?

However, in order to answer this question, we need to manipulate our data into a format that makes it easier 
to analyze. We'll explore the following functions and methods to perform this task:

Series.map()
Series.apply()
DataFrame.applymap()
DataFrame.apply()
pd.melt()
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# we will work on 2015 world happiness data

happiness2015 = pd.read_csv('World_Happiness_2015.csv')

mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health', 'Trust (Government Corruption)': 'Trust' }
# mapper
# changing column names

'''
pandas.DataFrame.rename
DataFrame.rename(mapper=None, *, index=None, columns=None, axis=None, copy=None, inplace=False, level=None, errors='ignore')[source]
'''
happiness2015 = happiness2015.rename(mapping, axis=1)


# passing function in series.map() and series.apply()

def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
    
    
economy_impact_map = happiness2015['Economy'].map(label)
# map to series. series.map(function)

economy_impact_apply = happiness2015['Economy'].apply(label)
# series.apply()

equal = economy_impact_map.equals(economy_impact_apply)

'''
we applied a function to the Economy column using the Series.map() and Series.apply() 
methods and confirmed that both methods produce the same results.

Note that these methods don't modify the original series. If we want to work with the new series 
in the original dataframe, we must either assign the results back to the original column 
or create a new column. We recommend creating a new column, in case you need to reference the original values.
'''

def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
economy_impact_apply = happiness2015['Economy'].apply(label)

def label(element, x):
    if element > x:
        return 'High'
    else:
        return 'Low'
    
    
economy_impact_apply = happiness2015['Economy'].apply(label, x=0.8)
# we cannot pass x arguement series.map()


# now applying in multiple columns
'''
pandas.DataFrame.map
DataFrame.map(func, na_action=None, **kwargs)[source]
Apply a function to a Dataframe elementwise.
'''

'''
At first it migt look like the same function,
 but the subtle difference is that now the function is 
 DataFrame.map() instead of Series.map().
   This distinction is important because DataFrame.map()
     applies the function to every element in the DataFrame,
       whereas Series.map() only works on a single column.

We'll use the following syntax to work with the DataFrame.map() method:
'''

'''
A note on the DataFrame.map() method:
In versions of pandas prior to 2.1.0, DataFrame.applymap() method
 was used to apply a function element-wise to multiple columns.
   However, this method has been deprecated in favor of
     DataFrame.map(). We recommend using the DataFrame.map()
       method instead of the DataFrame.applymap() method to avoid 
       any potential issues.
'''

def label(element):
    if element > 1:
        return 'High'
    else:
        return 'Low'
economy_apply = happiness2015['Economy'].apply(label)
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']

factors_impact = happiness2015[factors].map(label)

# Apply Functions along an Axis using the Apply Method

'''
You can also use the apply() method on a dataframe,
 but the DataFrame.apply() method has different capabilities. 
 Instead of applying functions element-wise, the df.apply() method 
 applies functions along an axis, either column-wise or row-wise. 
 When we create a function to use with df.apply(), we set 
 it up to accept a series, most commonly a column.
'''

'''
Let's use the df.apply() method to calculate the number of
 'High' and 'Low' values in each column of the result from the 
 last exercise, factors_impact. In order to do so, we'll apply 
 the pd.value_counts function to all of the columns in the 
 dataframe:
'''

'''
Apply Functions along an Axis using the Apply Method
'''

def v_counts(col):
    num = col.value_counts()
#     series.value_counts()
    
    den = col.size
#     number of rows
    
    return num/den


v_counts_pct = factors_impact.apply(v_counts)

# Apply Functions along an Axis using the Apply Method Continued

'''
In general, we should only use the apply() method when a 
vectorized function does not exist. Recall that pandas uses
 vectorization, the process of applying operations to whole
   series at once, to optimize performance. When we use the 
   apply() method, we're actually looping through rows, 
   so a vectorized method can perform an equivalent task faster
     than the apply() method.
'''


factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']

def percentages(col):
#     col is a series
    div = col / happiness2015['Happiness Score']
    return div * 100


factor_percentages = happiness2015[factors].apply(percentages)


# Reshaping Data with the Melt Function


main_cols = ['Country', 'Region', 'Happiness Rank', 'Happiness Score']
factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']

# we use the melt function to reshape happy_two so that the values for Economy, Family, and Health reside in the same column

melt = pd.melt(happiness2015, id_vars=main_cols, value_vars=factors)

melt['Percentage'] = round(melt['value']/melt['Happiness Score'] * 100, 2)
# new column percentage, with round(data, 2)


# Aggregate the Data and Create a Visualization

'''
The melt function moved the values in the seven columns -
 Economy, Health, Family, Freedom, Generosity, Trust, and Dystopia Residual -
 to the same column, which meant we could transform them all at once.

You may have also noticed that now the data is in a format that makes it easier to aggregate. 
We refer to data in this format as tidy data. 
'''

# df.pivot_table()
pv_melt = melt.pivot_table(index='variable', values='value')


pv_melt.plot(kind='pie', y='value', legend=False)
plt.show()

