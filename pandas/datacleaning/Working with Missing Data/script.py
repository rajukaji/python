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

import matplotlib.pyplot as plt
import seaborn as sns

def plot_null_correlations(df):
    # create a correlation matrix only for columns with at least
    # one missing value
    cols_with_missing_vals = df.columns[df.isnull().sum() > 0]
    missing_corr = df[cols_with_missing_vals].isnull().corr()
    
    # create a mask to avoid repeated values and make
    # the plot easier to read
    missing_corr = missing_corr.iloc[1:, :-1]
    mask = np.triu(np.ones_like(missing_corr), k=1)
    
    # plot a heatmap of the values
    plt.figure(figsize=(20,14))
    ax = sns.heatmap(missing_corr, vmin=-1, vmax=1, cbar=False,
                     cmap='RdBu', mask=mask, annot=True)
    
    # format the text in the plot to make it easier to read
    for text in ax.texts:
        t = float(text.get_text())
        if -0.05 < t < 0.01:
            text.set_text('')
        else:
            text.set_text(round(t, 2))
        text.set_fontsize('x-large')
    plt.xticks(rotation=90, size='x-large')
    plt.yticks(rotation=0, size='x-large')

    plt.show()
    
    
    
'''
Instructions
We created a function, plot_null_correlations(), which will plot correlations
between null values in a dataframe.

Use list comprehension to produce a list of column names containing the substring 'vehicle'.
Use the list of column names to select only those columns from the mvc dataframe. Pass the result
 to the plot_null_correlations() function.
''' 
vehicle_cols = [cols for cols in mvc.columns if 'vehicle' in cols]

plot_null_correlations(mvc[vehicle_cols])


# Analyzing Correlations in Missing Data

'''
We outlined a diagonal strip of five squares in green that have a higher correlation than the rest. The pairs of column names that make up these five correlations are:

vehicle_1 and cause_vehicle_1
vehicle_2 and cause_vehicle_2
vehicle_3 and cause_vehicle_3
vehicle_4 and cause_vehicle_4
vehicle_5 and cause_vehicle_5
If you think about it, this makes sense. When a vehicle is in an accident, 
there is likely to be a cause, and vice-versa.

Let's explore the variations in missing values from these five pairs of columns. 
We'll create a dataframe that counts, for each pair:

The number of values where the vehicle is missing when the cause is not missing.
The number of values where the cause is missing when the vehicle is not missing.
The final structure of our dataframe will look like this:

v_number	vehicle_missing	cause_missing
0	1	[count]	[count]
1	2	[count]	[count]
2	3	[count]	[count]
3	4	[count]	[count]
4	5	[count]	[count]

'''

'''
We provided the start of the loop you are going to build, including code
 that generates each column name as strings: v_col and c_col

Uncomment the commented lines (you can select the lines and press ctrl + / as a
 keyboard shortcut).
Add code to the body of the loop that will:
Count the number of rows where the v_col column is null and the c_col column is not null.
 Assign the result to v_null.
Count the number of rows where the c_col column is null and the v_col column is not null. 
Assign the result to c_null.
Append an item to the vc_null_data list. The item should be a list containing, 
in order: v, v_null, c_null.
Outside the loop, create a dataframe using the vc_null_data list of lists.
Use the columns parameter and the col_labels list to set the column names of the dataframe.
Assign the dataframe to vc_null_df.
'''

col_labels = ['v_number', 'vehicle_missing', 'cause_missing']

vc_null_data = []

for v in range(1,6):
    v_col = f'vehicle_{v}'
    c_col = f'cause_vehicle_{v}'
    
    v_null = (mvc[v_col].isnull() & mvc[c_col].notnull()).sum()
    
    c_null = (mvc[c_col].isnull() & mvc[v_col].notnull()).sum()
    
    vc_null_data.append([v, v_null, c_null])


vc_null_df = pd.DataFrame(data=vc_null_data, columns=col_labels)
print(vc_null_df)


# Finding the Most Common Values Across Multiple Columns

'''
The analysis we did on the previous screen indicates that there 
are roughly 4,500 missing values across the 10 columns. 
The easiest option for handling these would be to drop the
 rows with missing values. This would mean losing almost
   10% of the total data, which is something we ideally want to avoid.

A better option is to impute the data, like we did earlier. 
Because the data in these columns is text data, we can't 
perform a numeric calculation to impute missing data like 
we did with the injuries and killed columns.

One common option when imputing is to use the most common value 
to fill in data. Let's look at the common values across 
these columns and see if we can use that to make a decision.

We've previously used the Series.value_counts() method to find 
the most common values in a single column. In this case, 
we want to find the most common values across multiple columns.
 In order to do this, we first need to convert our dataframe
   of multiple columns into one single column, and then we
     can use Series.value_counts() to count the items.

To convert a dataframe to a single column of values, we use the
 DataFrame.stack() method, which stacks a dataframe object into 
 a Series object. Let's look at a diagram of how this works. 
 We'll start with a simple dataframe with three columns
   containing words:

Sample dataframe
When we use DataFrame.stack(), the values become a series object, 
with the values from each row "stacked" on top of each other:

Stacked dataframe
This series object actually has two row indexes. 
The first index is the original row index, and the second
 contains the columns that correspond to the value.

Once we have this stacked series, we can just use 
Series.value_counts() to count the values:

Counting the values
Let's use this technique to count the most common values for 
the cause set of columns. We'll start by selecting only the
 columns containing the substring cause.

cause_cols = [c for c in mvc.columns if "cause_" in c]
cause = mvc[cause_cols]
print(cause.head())

cause_vehicle_1	cause_vehicle_2	cause_vehicle_3	cause_vehicle_4	
cause_vehicle_5
0	Following Too Closely	Unspecified	NaN	NaN	NaN
1	Backing Unsafely	Unspecified	NaN	NaN	NaN
2	Following Too Closely	Unspecified	NaN	NaN	NaN
3	Glare	Passing Too Closely	NaN	NaN	NaN
4	Turning Improperly	Unspecified	NaN	NaN	NaN
Next, we'll stack the values into a single series object:

cause_1d = cause.stack()
print(cause_1d.head())

Explain

Copy
0  cause_vehicle_1    Following Too Closely
   cause_vehicle_2              Unspecified
1  cause_vehicle_1         Backing Unsafely
   cause_vehicle_2              Unspecified
2  cause_vehicle_1    Following Too Closely
dtype: object

You may notice that the stacked version omits null values - 
this is fine, as we're just interested in the most common non-null 
values.

Finally, we count the values in the series:

cause_counts = cause_1d.value_counts()
top10_causes = cause_counts.head(10)
print(top10_causes)

Explain

Copy
Unspecified                       57481
Driver Inattention/Distraction    17650
Following Too Closely              6567
Failure to Yield Right-of-Way      4566
Passing or Lane Usage Improper     3260
Passing Too Closely                3045
Backing Unsafely                   3001
Other Vehicular                    2523
Unsafe Lane Changing               2372
Turning Improperly                 1590
dtype: int64

The most common non-null value for the cause columns is Unspecified,
 which presumably indicates that the officer reporting the collision
   was unable to determine the cause for that vehicle.

Let's use the same technique to identify the most common non-null
 value for the vehicle columns.
'''


'''
Instructions
We provided a list comprehension that identifies columns starting
 with the substring vehicle.

    Create a dataframe containing only the columns from mvc,
 identified by the list comprehension v_cols.

    Use DataFrame.stack() to stack the values from the dataframe 
into a single series object.

    Use Series.value_counts() to count the unique values from 
the stacked series. Assign the first 10 values to top10_vehicles.
'''

v_cols = [c for c in mvc.columns if c.startswith("vehicle")]
# c is all the values in the rows that the condition matches for columns
# list comprehension is used to filter the columns that match the condition
# the condition is c.startswith("vehicle") which means that the 
# columns that start with the word vehicle are selected

vehicle = mvc[v_cols]
# the columns that match the condition are selected from the mvc dataframe
# and stored in the vehicle dataframe
# the vehicle dataframe contains only the columns that start with the word vehicle
# mvc[v_cols] is used to select the columns that match the condition
# and create a new dataframe

top10_vehicles = pd.DataFrame(data=vehicle).stack().value_counts().head(10)
# we can also convert into a dataframe and use the stack method to stack the values
# and then use the value_counts method to count the unique values
# and then use the head method to select the first 10 values


# Filling Unknown Values with a Placeholder

'''
Let's look at the values analysis we completed on the
 previous screen:

print(top10_vehicles)

Sedan                                  33133
Station Wagon/Sport Utility Vehicle    26124
PASSENGER VEHICLE                      16026
SPORT UTILITY / STATION WAGON          12356
Taxi                                    3482
Pick-up Truck                           2373
TAXI                                    1892
Box Truck                               1659
Bike                                    1190
Bus                                     1162
dtype: int64

print(top_10_causes)

Unspecified                       57481
Driver Inattention/Distraction    17650
Following Too Closely              6567
Failure to Yield Right-of-Way      4566
Passing or Lane Usage Improper     3260
Passing Too Closely                3045
Backing Unsafely                   3001
Other Vehicular                    2523
Unsafe Lane Changing               2372
Turning Improperly                 1590
dtype: int64

The top "cause" is an "Unspecified" placeholder. This is
 useful instead of a null value as it makes the distinction 
 between a value that is missing because there were only a 
 certain number of vehicles in the collision versus one that
   is because the contributing cause for a particular vehicle
     is unknown.

The vehicles columns don't have an equivalent, but we can 
still use the same technique. Here's the logic we'll need
 to do for each pair of vehicle/cause columns:

For values where the vehicle is null and the cause is non-null,
 set the vehicle to Unspecified.
For values where the cause is null and the vehicle is not-null, 
set the cause to Unspecified.
We can use Series.mask() to replace the values, just like we 
did earlier in the lesson. Let's look at code to perform this
 for the vehicle_1 and vehicle_cause_1 columns:

# create a mask for each column
v_missing_mask = mvc['vehicle_1'].isnull() & mvc['cause_vehicle_1'].notnull()
c_missing_mask = mvc['cause_vehicle_1'].isnull() & mvc['vehicle_1'].notnull()

# replace the values matching the mask for each column
mvc['vehicle_1'] =  mvc['vehicle_1'].mask(v_missing_mask, 
"Unspecified")
mvc['cause_vehicle_1'] =  mvc['cause_vehicle_1'].mask(c_missing_mask,
 "Unspecified")

Now let's use a loop to fill in these values across all columns.
 We've created a helper function summarize_missing() which 
 contains the logic we used earlier to count missing values
   across the pairs of columns. Below is a quick demonstration 
   on how it works:

print(summarize_missing())

vehicle_number	vehicle_missing	cause_missing
0	1	204	24
1	2	3793	223
2	3	242	24
3	4	50	3
4	5	10	0
'''


'''
Instructions
In addition to the helper function, we provided the start 
of the loop you are going to build, including code that 
generates each column name as a string.

Uncomment the commented lines (you might want to use this 
keyboard shortcut).

Add code to the body of the loop that:
Creates a boolean mask for values where the vehicle column
 is null and the cause column is non-null.
Creates a boolean mask for values where the cause column is
 null and the vehicle column is non-null.
Uses the first boolean mask to fill matching values from the 
vehicle column with the string Unspecified.
Uses the second boolean mask to fill matching values from the 
cause column with the string Unspecified.
Outside the loop, use the summarize_missing() function to check
 that you have removed all matching values. Assign the result to summary_after.
'''

def summarize_missing(mvc):
    v_missing_data = []

    for v in range(1,6):
        v_col = f'vehicle_{v}'
        c_col = f'cause_vehicle_{v}'

        v_missing = (mvc[v_col].isnull() & mvc[c_col].notnull()).sum()
        c_missing = (mvc[c_col].isnull() & mvc[v_col].notnull()).sum()

        v_missing_data.append([v, v_missing, c_missing])

    col_labels = ["vehicle_number", "vehicle_missing", "cause_missing"]
    return pd.DataFrame(v_missing_data, columns=col_labels)

summary_before = summarize_missing(mvc)

for v in range(1,6):
    v_col = f"vehicle_{v}"
    c_col = f"cause_vehicle_{v}"
    
    v_null_mask = mvc[v_col].isnull() & mvc[c_col].notnull()
    c_null_mask = mvc[c_col].isnull() & mvc[v_col].notnull()
    
    # Series.mask(cond, other=<no_default>, *, inplace=False, axis=None, level=None)
    
    mvc[v_col] = mvc[v_col].mask(v_null_mask, 'Unspecified')
#     to replace the missing values in vehicle_ columns with 'Unspecified'
    mvc[c_col] = mvc[c_col].mask(c_null_mask, 'Unspecified')
    
    
summary_after = summarize_missing(mvc)   


#  Missing Data in the "Location" Columns

'''
Working with Missing Data
9 of 11 · Missing Data in the "Location" Columns
Learn
Let's view the work we've done across the past few screens by looking at the null correlation plot for the last 10 columns:

veh_cols = [c for c in mvc.columns if 'vehicle' in c]
plot_null_correlations(mvc[veh_cols])

Plot output
You can see the perfect correlation between each pair of vehicle/cause columns represented by 
1.0
 in each square, which means that there is a perfect relationship between the five pairs of vehicle/cause columns.

Let's now turn our focus to the final set of columns that contain missing values — the columns that relate to the location of the accident. We'll start by looking at the first few rows to refamiliarize ourselves with the data:

loc_cols = ['borough', 'location', 'on_street', 'off_street', 'cross_street']
location_data = mvc[loc_cols]
print(location_data.head())

borough	location	on_street	off_street	cross_street
0	MANHATTAN	(40.742832, -74.00771)	WEST 15 STREET	NaN	10 AVENUE
1	BROOKLYN	(40.623714, -73.99314)	16 AVENUE	NaN	62 STREET
2	NaN	(40.591755, -73.9083)	BELT PARKWAY	NaN	NaN
3	QUEENS	(40.73602, -73.87954)	GRAND AVENUE	NaN	VANLOON STREET
4	BRONX	(40.884727, -73.89945)	NaN	208 WEST 238 STREET	NaN
Next, let's look at counts of the null values in each column:

print(location_data.isnull().sum())

borough         20646
location         3885
on_street       13961
off_street      44093
cross_street    29249
dtype: int64

These columns have a lot of missing values! Keep in mind that
 all of these five columns represent the same thing — the 
 location of the collision. We can potentially use the
   non-null values to impute some of the null values.

To see where we might be able to do this, let's look for 
correlations between the missing values:

plot_null_correlations(location_data)

Plot output
None of these columns have strong correlations except 
for off_street and on_street which have a near perfect
 negative correlation. That means for almost every row
   that has a null value in one column, the other has a
     non-null value and vice-versa.

The final way we'll look at the null values in these
 columns is to plot a null matrix, but we'll sort the
   data first. This will gather some of the null and
     non-null values together and make patterns more obvious:

sorted_location_data = location_data.sort_values(loc_cols)
plot_null_matrix(sorted_location_data)

Explain

Copy
Plot output
Let's make some observations about the missing values 
across these columns:

About two-thirds of rows have non-null values for borough,
 but of those values that are missing, most have non-null 
 values for location and one or more of the street name columns.
Less than one-tenth of rows have missing values in the location
 column, but most of these have non-null values in one or 
 more of the street name columns.
Most rows have a non-null value for either on_street or 
off_street, and some also have a value for cross_street.
Combined, this means that we will be able to impute a lot
 of the missing values by using the other columns in each 
 row. To do this, we can use geolocation APIs that take
 either an address or location coordinates, and return 
 information about that location.

Because the focus of this lesson is working with missing
 data, we have pre-prepared supplemental data using APIs. 
 On the next screen, we'll learn more about how that data was
   prepared and then use it to fill in missing values.


Next
Help Center
Search for help
FAQs and Guides
Site Status
Message Us
Feedback & Bug Reports
Career Masterclass
Ask Chandra
Elevio by Dixa
'''

# Imputing Location Data

'''
We prepared the supplemental data using the GeoPy package, 
which makes working with Geocoding APIs like the Google Maps
 API easier. Here's the strategy we used to prepare the 
 supplemental data:

For rows with location values but missing values in either 
borough or the street name columns, we used geocoding APIs to
 look up the location coordinates to find the missing data.
For rows with values in the street name columns missing borough 
and/or location data, we used geocoding APIs to look up the address 
to find the missing data.
You can learn more about working with APIs in our APIs and
Web Scraping course.

The supplemental data is in a CSV called supplemental_data.csv,
 let's read this into a pandas dataframe and familiarize ourself with the data:

sup_data = pd.read_csv('supplemental_data.csv')
sup_data.head()

'''

'''
The supplemental data has five columns from our original
data set — the unique_key that identifies each collision,
 and four of the five location columns. The cross_street 
 column is not included because the geocoding APIs we used
   don't include data on the nearest cross street to any 
   single location.

Let's take a look at a null matrix for the supplemental data:

plot_null_matrix(sup_data)
'''

'''
Apart from the unique_key column, you'll notice 
that there are a lot more missing values than our main data set.
 This makes sense, as we didn't prepare supplemental data where 
 the original data set had non-null values.

If the unique_key column in both the original and supplemental
 data has the same values in the same order, we'll be able to
   use Series.mask() to add our supplemental data to our
     original data. We can check this using the Series.equals() method:

mvc_keys = mvc['unique_key']
sup_keys = sup_data['unique_key']

is_equal = mvc_keys.equals(sup_keys)
print(is_equal)

True

Now that we've verified the data, it's time to use it to impute missing values.
'''

'''
Instructions
We read the supplemental data into a dataframe called sup_data.
 Additionally, we provided a list of the location columns, 
 location_cols, and calculated the number of null values in 
 these columns.

Loop over the column names in location_cols. In each iteration
 of the loop, use Series.mask() to replace values in the column
   in the mvc dataframe:
The mask should represent whether the values in column in the
 mvc has a null value or not.
Where the mask is true, the value should be replaced with the
 equivalent value in sup_data.
Calculate the number of null values across the location_cols
 columns in mvc after you adding the supplemental data. 
 Assign the result to null_after.
'''

sup_data = pd.read_csv('supplemental_data.csv')
location_cols = ['location', 'on_street', 'off_street', 'borough']
null_before = mvc[location_cols].isnull().sum()

for location in location_cols:
    mvc[location] = mvc[location].mask(mvc[location].isnull(), sup_data[location])
    
    
null_after = mvc[location_cols].isnull().sum()
print(null_after)
    

'''
In this lesson, we've imputed thousands of values to reduce
 the number of missing values across our data set.
   Let's look at a summary of the null values before and
     after our data cleaning:

original	final	pct_change
borough	20646	232	-0.989
location	3885	77	-0.980
on_street	13961	13734	-0.016
cross_street	29249	29249	0.000
off_street	44093	36131	-0.181
total_injured	1	21	20.000
total_killed	5	1	-0.800
vehicle_1	355	151	-0.575
vehicle_2	12262	8469	-0.309
vehicle_3	54352	54110	-0.004
vehicle_4	57158	57108	-0.001
vehicle_5	57681	57671	-0.000
cause_vehicle_1	175	151	-0.137
cause_vehicle_2	8692	8469	-0.026
cause_vehicle_3	54134	54110	-0.000
cause_vehicle_4	57111	57108	-0.000
cause_vehicle_5	57671	57671	0.000
If you'd like to continue working with this data, you can:

Drop the rows that had suspect values for injured and killed totals.
Clean the values in the vehicle_1 through vehicle_5 
columns by analyzing the different values and merging
 duplicates and near-duplicates.
Analyze whether collisions are more likely in certain
 locations, at certain times, or for certain vehicle types.
'''