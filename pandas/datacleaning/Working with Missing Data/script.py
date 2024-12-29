import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re 
import seaborn as sns

'''
A summary of the columns and their data is below:

unique_key: A unique identifier for each collision.
date, time: Date and time of the collision.
borough: The borough, or area of New York City, where the collision occurred.
location: Latitude and longitude coordinates for the collision.
on_street, cross_street, off_street: Details of the street or
 intersection where the
 collision occurred.
pedestrians_injured: Number of pedestrians who were injured.
cyclist_injured: Number of people traveling on a bicycle who 
were injured.
motorist_injured: Number of people traveling in a vehicle who 
were injured.
total_injured: Total number of people injured.
pedestrians_killed: Number of pedestrians who were killed.
cyclist_killed: Number of people traveling on a bicycle who were killed.
motorist_killed: Number of people traveling in a vehicle who were killed.
total_killed: Total number of people killed.
vehicle_1 through vehicle_5: Type of each vehicle involved in the accident.
cause_vehicle_1 through cause_vehicle_5: Contributing factor for each 
vehicle in the accident.
'''

mvc = pd.read_csv("nypd_mvc_2018.csv")

null_counts = mvc.isnull().sum()

# Verifying the Total Columns

'''
To give us a better picture of the null values in the data, 
let's calculate the percentage of null values in each column. 
Below, we divide the number of null values in each column by the 
total number of values in the data set:

null_counts_pct = null_counts / mvc.shape[0] * 100
null_counts_pct = null_counts / mvc.shape[0] * 100


We'll then add both the counts and percentages to a dataframe 
to make them easier to compare:

null_df = pd.DataFrame({'null_counts': null_counts, 'null_pct': 
null_counts_pct})
# Rotate the dataframe so that rows become columns and vice-versa
null_df = null_df.T.astype(int)
​
print(null_df)

	unique_key	date	time	borough	location	on_street	cross_street	off_street	pedestrians_injured	cyclist_injured	motorist_injured	total_injured	pedestrians_killed	cyclist_killed	motorist_killed	total_killed	vehicle_1	vehicle_2	vehicle_3	vehicle_4	vehicle_5	cause_vehicle_1	cause_vehicle_2	cause_vehicle_3	cause_vehicle_4	cause_vehicle_5
null_counts	0	0	0	20646	3885	13961	29249	44093	0	0	0	1	0	0	0	5	355	12262	54352	57158	57681	175	8692	54134	57111	57671
null_pct	0	0	0	35	6	24	50	76	0	0	0	0	0	0	0	0	0	21	93	98	99	0	15	93	98	99


About a third of the columns have no null values, with the rest ranging from less than 1% to 99%!

To make things easier, let's start by looking at the group of columns that relate to people killed in collisions.

We'll use list comprehension to reduce our summary dataframe to just those columns:

killed_cols = [col for col in mvc.columns if 'killed' in col]
print(null_df[killed_cols])
killed_cols = [col for col in mvc.columns if 'killed' in col]
print(null_df[killed_cols])

	pedestrians_killed	cyclist_killed	motorist_killed	total_killed
null_counts	0	0	0	5
null_pct	0	0	0	0

We can see that each of the individual categories have no missing
 values, but the total_killed column has five missing values.

One option for handling this would be to remove  or drop  those
 five rows. This would be a reasonably valid choice since it's a 
 tiny portion of the data, but let's think about what other options we
   have first.

If you think about it, the total number of people killed should be
 the sum of each of the individual categories. We might be able to
   "fill in" the missing values with the sums of the individual
     columns for that row. The technical name for filling in a
       missing value with a replacement value is called imputation.


'''

killed_cols = [col for col in mvc.columns if 'killed' in col]
killed = mvc[killed_cols].copy()

killed_manual_sum = killed.iloc[:,:3].sum(axis=1)
print(killed_manual_sum)

killed_mask = killed['total_killed'] != killed_manual_sum
                                
killed_non_eq = killed[killed_mask]                                

# Filling and Verifying the Killed and Injured Data

'''
The killed_non_eq dataframe we created in the previous exercise
 contained six rows:

 	pedestrians_killed	cyclist_killed	motorist_killed	total_killed
3508	0	0	0	NaN
20163	0	0	0	NaN
22046	0	0	1	0.0
48719	0	0	0	NaN
55148	0	0	0	NaN
55699	0	0	0	NaN

We can categorize these into two categories:

Five rows where the total_killed is not equal to the sum of the 
other columns because the total value is missing.
One row where the total_killed is less than the sum of the other columns.


From this, we can conclude that filling null values with the sum of
the columns is a fairly good choice for our imputation, given that 
only six rows out of around 58,000 don't match this pattern.

We've also identified a row that has suspicious data - one that 
doesn't sum correctly. Once we have imputed values for all rows 
with missing values for total_killed, we'll mark this suspect
 row by setting its value to NaN.

 In order to execute this, we'll learn to use the Series.mask() 
 method. Series.mask() is useful when you want to replace certain
   values in a series based off a boolean mask. The syntax for 
   the method is:

Series.mask(bool_mask, val_to_replace)

Series.mask(cond, other=<no_default>, *, inplace=False, axis=None, 
level=None)
other
scalar, Series/DataFrame, or callable
Entries where cond is True are replaced with corresponding value
 from other. If other is callable, it is computed on the Series/DataFrame
   and should return scalar or Series/DataFrame. The callable must
   not change input Series/DataFrame (though pandas doesn’t check it). 
   If not specified, entries will be filled with the corresponding NULL
     value (np.nan for numpy dtypes, pd.NA for extension dtypes).

we use Series.mask() to replace all the values
 that match the boolean series with a new value,
'''

'''
Let's look at how we'd use this technique to update the values 
in the total_killed column. First, we'll replace all null values
 with the equivalent values from our killed_manual_sum series:

killed_null = killed['total_killed'].isnull()
killed['total_killed'] = killed['total_killed'].mask(killed_null,
 killed_manual_sum)

 
 Next, we'll replace any values where the manual sum and
   the total column aren't equal with np.nan. This time we'll
     define the boolean series directly into Series.mask():

killed['total_killed'] = killed['total_killed'].mask(killed['total_killed'] 
    != killed_manual_sum, np.nan)
'''

# Create a killed dataframe and manually sum values
killed_cols = [col for col in mvc.columns if 'killed' in col]
killed = mvc[killed_cols].copy()
killed_manual_sum = killed.iloc[:, :3].sum(axis=1)

# fix the killed values
killed['total_killed'] = killed['total_killed'].mask(killed['total_killed'].isnull(), killed_manual_sum)
killed['total_killed'] = killed['total_killed'].mask(killed['total_killed'] != killed_manual_sum, np.nan)

# Create an injured dataframe and manually sum values
injured = mvc[[col for col in mvc.columns if 'injured' in col]].copy()
injured_manual_sum = injured.iloc[:, :3].sum(axis=1)


'''
Instructions
We included the code to clean the killed columns. 
In addition, we've created an injured dataframe with just 
the injured columns and injured_manual_sum, a series manually
summing the three individual injured columns.

Use Series.mask() to replace any null values from the total_injured 
column with their equivalents from the injured_manual_sum series.
Use Series.mask() to replace any numbers from total_injured that
 aren't equal to their equivalents in injured_manual_sum with np.nan.

'''

# Create a killed dataframe and manually sum values
killed_cols = [col for col in mvc.columns if 'killed' in col]
killed = mvc[killed_cols].copy()
killed_manual_sum = killed.iloc[:, :3].sum(axis=1)

# fix the killed values
killed['total_killed'] = killed['total_killed'].mask(killed['total_killed'].isnull(), killed_manual_sum)
killed['total_killed'] = killed['total_killed'].mask(killed['total_killed'] != killed_manual_sum, np.nan)

# Create an injured dataframe and manually sum values
injured = mvc[[col for col in mvc.columns if 'injured' in col]].copy()
injured_manual_sum = injured.iloc[:, :3].sum(axis=1)


injured['total_injured'] = injured['total_injured'].mask(injured['total_injured'].isnull(), injured_manual_sum)

injured['total_injured'] = injured['total_injured'].mask(injured['total_injured'] != injured_manual_sum, np.nan)

# Assigning the Corrected Data Back to the Main Dataframe

'''
Let's summarize the count of null values before and after our changes:

summary = {
    'injured': [
        mvc['total_injured'].isnull().sum(),
        injured['total_injured'].isnull().sum()
    ],
    'killed': [
        mvc['total_killed'].isnull().sum(),
        killed['total_killed'].isnull().sum()
    ]
}
print(pd.DataFrame(summary, index=['before','after']))

	injured	killed
before	1	5
after	21	1

For the total_killed column, the number of values has gone down 
from 5 to 1. For the total_injured column, the number of values
 has actually gone up — from 1 to 21. This might sound like we've
   done the opposite of what we set out to do, but what we've
     actually done is fill all the null values and identify 
     alues that have suspect data. This will make any analysis 
     we do on this data more accurate in the long run.
'''
# Let's assign the values from the killed and injured dataframe back to the main mvc dataframe:

mvc['total_injured'] = injured['total_injured']

mvc['total_killed'] = killed['total_killed']

# Visualizing Missing Data with Plots

'''
Earlier, we used a table of numbers to understand the number of 
missing values in our dataframe. A different approach we can take
 is to use a plot to visualize the missing values. The function
   below uses seaborn.heatmap() to represent null values as light 
   squares and non-null values as dark squares:

def plot_null_matrix(df, figsize=(18,15)):
    # initiate the figure
    plt.figure(figsize=figsize)
    # create a boolean dataframe based on whether values are null
    df_null = df.isnull()
    # create a heatmap of the boolean dataframe
    sns.heatmap(~df_null, cbar=False, yticklabels=False)
    plt.xticks(rotation=90, size='x-large')
    plt.show()

    Let's look at how the function works by using it to plot just the first row of our
    mvc dataframe. We'll display the first row as a table immediately below so it's 
    easy to compare:

plot_null_matrix(mvc.head(1), figsize=(18,1))

Each value is represented by a dark square, and each missing value is represented by a 
light square.

Let's look at what a plot matrix looks like for the whole dataframe:

plot_null_matrix(mvc)

We can make some immediate interpretations about our dataframe:

The first three columns have few to no missing values.
The next five columns have missing values scattered throughout, with each 
column seeming to have its own density of missing values.
The next eight columns are the injury and killed columns we just cleaned,
and only have a few missing values.
The last 10 columns seem to break into two groups of five, with each group
 of five having similar patterns of null/non-null values.

 
 Let's examine the pattern in the last 10 columns a little more closely.
   We can calculate the relationship between two sets of columns, known as correlation.
     To calculate this we use the dataframe.corr() method
       (You'll learn more about correlation in a later course). Here's what that looks like:

cols_with_missing_vals = mvc.columns[mvc.isnull().sum() > 0]
missing_corr = mvc[cols_with_missing_vals].isnull().corr()
print(missing_corr)

Each value is between 
−
1
 and 
1
, and represents the relationship between two columns. A number close to 
−
1
 or 
1
 represents a strong relationship, where a number in the middle (close to 
0
) represents a weak relationship.

If you look closely, you can see a diagonal line of 
1
s going from top left to bottom right. These values represent each columns 
relationship with itself, which of course is a perfect relationship. 
The values on the top/right of this "line of 
1
s" mirror the values on the bottom/left of this line: The table actually
 repeats every value twice!

 Let's create a correlation plot of just those last 10 columns to see if we can 
 more closely identify  the pattern we saw earlier in the matrix plot.
'''

