import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns

happiness2015 = pd.read_csv('wh_2015.csv')
happiness2016 = pd.read_csv('wh_2016.csv')
happiness2017 = pd.read_csv('wh_2017.csv')

shape_2015 = happiness2015.shape
shape_2016 = happiness2016.shape 
shape_2017 = happiness2017.shape

# confirm the number of missing values in happiness2016 and happiness2017 next.

missing_2016 = happiness2016.isnull().sum()
# df.isnull() gives all the null values, while df.sum() calculates the total missing value of each columns

missing_2017 = happiness2017.isnull().sum()

'''
It's good to check for missing values before transforming data to make sure we don't unintentionally introduce missing values.

If we do introduce missing values after transforming data, we'll have to determine if the data is really missing or if it's the result of some kind of error. As we progress through this lesson, we'll use the following workflow to clean our missing values, starting with checking for errors:

Check for errors in data cleaning/transformation.
Use data from additional sources to fill missing values.
Drop row/column.
Fill missing values with reasonable estimates computed from the available data.
Let's return to a task we completed in a previous lesson - combining the 2015, 2016, and 2017 World Happiness Reports. Recall that we can use the pd.concat() function to combine them:

happiness2015 = pd.read_csv("wh_2015.csv")
happiness2016 = pd.read_csv("wh_2016.csv")
happiness2017 = pd.read_csv("wh_2017.csv")
combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)

Explain

Copy
Next, let's check for missing values in combined:

print(combined.isnull().sum())
'''

'''
As a reminder, below is a list of common string methods you can use to clean the columns:

Method	Description
Series.str.split()	Splits each element in the Series.
Series.str.strip()	Strips whitespace from each string in the Series.
Series.str.lower()	Converts strings in the Series to lowercase.
Series.str.upper()	Converts strings in the Series to uppercase.
Series.str.get()	Retrieves the ith element of each element in the Series.
Series.str.replace()	Replaces a regex or string in the Series with another string.
Series.str.cat()	Concatenates strings in a Series.
Series.str.extract()	Extracts substrings from the Series matching a regex pattern.

'''

# https://stackoverflow.com/questions/39741429/pandas-replace-a-character-in-all-column-names


# updating the columns name
happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ', regex=True).str.strip().str.upper()


happiness2015.columns = happiness2015.columns.str.replace('[\(\)]', '', regex=True).str.upper()
# replacing parenthesis '(' and ')' with '' nonspace and converting into uppercase
# always use regex=True when using regex combination

happiness2016.columns = happiness2016.columns.str.replace('[\(\)]', '', regex=True).str.upper()

combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True, axis=0, join='outer')
# axis 0 and join outer are default

missing = combined.isnull().sum()
# to see the missing values
print(missing)
# only year and country columns dont have any missing values

# we corrected some of the missing values by fixing the column names. 
# Note that we could have cleaned the column names without changing the capitalization. 
# t's good practice, however, to make the capitalization uniform, because a stray uppercase or
# lowercase letter could've reintroduced missing values.


# visualizing themissing data

combined_updated = combined.set_index('YEAR')
sns.heatmap(combined_updated.isnull(), cbar=False)
plt.show()
# missing values in region

regions_2017 = combined[combined['YEAR'] == 2017]['REGION']

missing = regions_2017.isnull().sum()
# calculate the total numbers of missing values in 2017 for missing column of 'REGION'

print(missing)
# 164 missing values
# we have in total 164 rows in 2017


# Using Data From Additional Sources to Fill in Missing Values

'''
we confirmed that the REGION column is missing from the 2017 data. Since we need the regions to analyze our data, let's turn our attention there next.

Before we drop or replace any values, let's first see if there's a way we can use other available data to correct the values.

Check for errors in data cleaning/transformation.
Use data from additional sources to fill missing values.
Drop row/column.
Fill missing values with reasonable estimates computed from the available data.
Recall once more that each year contains the same countries. Since the regions are fixed values - the region a country was assigned to in 2015 or 2016 won't change - we should be able to assign the 2015 or 2016 region to the 2017 row.

In order to do so, we'll use the following strategy:

Create a dataframe containing all of the countries and corresponding regions from the happiness2015, happiness2016, and happiness2017 dataframes.
Use the pd.merge() method to assign the REGION in the dataframe above to the corresponding country in combined.
The result will have two region columns - the original column with missing values will be named REGION_x. The updated column without missing values will be named REGION_y. We'll drop REGION_x to eliminate confusion.
Note that there are other ways to complete this task. We encourage you to explore them on your own.
'''

region_2015 = happiness2015[['COUNTRY', 'REGION']]
region_2016 = happiness2016[['COUNTRY', 'REGION']]
region_2017 = happiness2017[['COUNTRY']]
region_2017['REGION'] = False

# combined = pd.merge(region_2016, region_2017, how='outer')

regions = pd.merge(left=region_2015, right=region_2016, how='outer')

combined = pd.merge(left = combined, right = regions, on = 'COUNTRY', how = 'left')

# now drop REGION_x in combined, as it has missing values, while
# REGION_y doesn't have any missing values

combined = combined.drop('REGION_x', axis=1)

missing = combined.isnull().sum()
print(missing)

# you can rename REGION_y to REGION again
# df.rename(mapper, axis)
# mapper is a dictionary
combined = combined.rename({'REGION_y': 'REGION'}, axis=1)

'''
Before we decide how to handle the rest of our missing values, let's first check our dataframe for duplicate rows.

We'll use the DataFrame.duplicated() method to check for duplicate values. If no parameters are specified, the method will check for any rows in which all columns have the same values.

Since we should only have one country for each year, we can be a little more thorough by defining rows with ONLY the same country and year as duplicates. To accomplish this, let's pass a list of the COUNTRY and YEAR column names into the df.duplicated() method:

dups = combined.duplicated(['COUNTRY', 'YEAR'])
combined_dups = combined[dups]
'''

# Identifying duplicate values
combined['COUNTRY'] = combined['COUNTRY'].str.upper()

dups = combined.duplicated(['COUNTRY', 'YEAR'])

combined_dups = combined[dups]


# Correcting Duplicates Values

# Now, we can see that there are two rows for 2015, 2016, and 2017 each.

# Next, let's use the df.drop_duplicates() method to drop the duplicate rows. 
# Like the df.duplicated() method, the df.drop_duplicates() method will define duplicates as rows
#  in which all columns have the same values. We'll have to specify that rows with the same values
#  in only the COUNTRY and YEAR columns should be dropped.
'''
It's also important to note that by default, the drop_duplicates() method will only keep the first duplicate row. 
To keep the last duplicate row, set the keep parameter to 'last'. Sometimes, this will mean sorting the dataframe
 before dropping the duplicate rows.

In our case, since the second duplicate row above contains more missing values than the first row, 
we'll keep the first row.
'''

# pandas.DataFrame.drop_duplicates
# DataFrame.drop_duplicates(subset=None, *, keep='first', inplace=False, ignore_index=False)[source]


combined['COUNTRY'] = combined['COUNTRY'].str.upper()

combined = combined.drop_duplicates(['COUNTRY', 'YEAR'])

print(combined.duplicated())


# Handle Missing Values by Dropping Columns

'''
Now that we've corrected the duplicate values in the dataframe, 
let's turn our attention back to the rest of our missing values. So far, to correct missing values we:

Corrected the errors we made when combining our dataframes.
Used the 2015 and 2016 region values to fill in the missing regions for 2017.
Many of the methods in pandas are designed to exclude missing values without removing them,
 so at this point, we could leave the rest of the missing values as is, depending on the question
   we're trying to answer.

However, leaving missing values in the dataframe could cause issues with other transformation
 tasks and change the distribution of our data set. Also note that missing data has to be dropped
   or replaced to work with machine learning algorithms, so if you're interested in continuing in
     the data science path, it's important to know how to handle them.

Next, we'll consider dropping columns with missing data:

Check for errors in data cleaning/transformation.
Use data from additional sources to fill missing values.
Drop row/column.
Fill missing values with reasonable estimates computed from the available data.
First, let's confirm how many missing values are now left in the dataframe:

print(combined.isnull().sum())
'''

'''
We can see above that a couple columns contain over 300 missing values.
 Let's start by analyzing these columns since they account for most of the missing values left in the dataframe.

When deciding if you should drop a row or column, carefully consider whether you'll lose information
that could alter your analysis. Instead of just saying, "If x percentage of the data is missing, we'll drop it.",
 it's better to also ask the following questions:

Is the missing data needed to accomplish our end goal?
How will removing or replacing the missing values affect our analysis?
To answer the first question, let's establish our end goal:

End Goal: We want to analyze happiness scores and the factors that contribute to happiness scores by year.
 and region.
Since missing values make up more than half of the following columns and we don't need them to accomplish 
our end goal, we'll drop them:

STANDARD ERROR
LOWER CONFIDENCE INTERVAL
UPPER CONFIDENCE INTERVAL
WHISKER HIGH
WHISKER LOW
We'll use the DataFrame.drop() method to drop them next.
'''

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html

columns_to_drop = ['LOWER CONFIDENCE INTERVAL', 'STANDARD ERROR', 'UPPER CONFIDENCE INTERVAL', 'WHISKER HIGH', 'WHISKER LOW']

combined = combined.drop(columns_to_drop, axis=1)

missing = combined.isnull().sum()
print(missing)


# Handle Missing Values by Dropping Columns Continued

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html

'''
we used the df.drop() method to drop columns we don't need for our analysis.

However, as you start working with bigger datasets, it can sometimes be tedious to create a 
long list of column names to drop. Instead we can use the DataFrame.dropna() method to complete the same task.

By default, the dropna() method will drop rows with any missing values. To drop columns, we can set
the axis parameter equal to 1, just like with the df.drop() method:

df.dropna(axis=1)

Explain

Copy
However, this would result in dropping columns with any missing values - we only want to drop certain columns. 
Instead, we can also use the thresh parameter to only drop columns if they contain below a certain number of
 non-null values.

So far, we've used the df.isnull() method to confirm the number of missing values in each column. To confirm
the number of values that are NOT missing, we can use the DataFrame.notnull()method:

print(combined.notnull().sum().sort_values())

'''

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.notnull.html

print(combined.notnull().sum().sort_values())

# we can see there are columns below 159 values present, so we drop these columns with dfdropna()

# we can do above by this way too, without creating long list to drop mannually
# just see the non null values, which ever threshhold is minimum consider to other higher thresholds, drop them


combined = combined.dropna(thresh=159, axis=1)

missing = combined.isnull().sum()
print(missing)

#  we dropped columns we don't need for our analysis and confirmed that a couple columns still have missing values:

#  Analyzing Missing Data


'''
To make a decision about how to handle the rest of the missing data, we'll analyze if it's better
to just drop the rows or replace the missing values with other values.

Let's return to the following questions:

Is the missing data needed to accomplish our end goal?
Yes, we need the data to accomplish our goal of analyzing happiness scores and contributing factors 
by region and year.
How will removing or replacing the missing values affect our analysis?
Let's break the second question down into a couple more specific questions:

What percentage of the data is missing?
Will dropping missing values cause us to lose valuable information in other columns?
Can we identify any patterns in the missing data?
Question: What percentage of the data is missing?

As we saw when looking at the results of combined.isnull().sum() above, if missing values exist in a 
column of our dataframe, they account for about 4 percent of the total values (19 missing out of 489 
values per column).

Generally speaking, the lower the percentage of missing values, the less likely dropping them will significantly
 impact the analysis.

Question: Will dropping missing values cause us to lose valuable information in other columns?

To answer this question, let's visualize the missing data once more. Note below that before we create
 the heatmap, we first set the index of combined to the REGION column and sort the values:

sorted = combined.set_index('REGION').sort_values(['REGION', 'HAPPINESS SCORE'])
sns.heatmap(sorted.isnull(), cbar=False)
plt.show()
'''
'''
As a reminder, in the heatmap above, the missing values are represented with light gray and all 
other values with black. From this visualization, we can confirm that if the data is missing, 
it's missing in almost every column. We'll conclude that dropping the missing values won't cause
 us to lose valuable information in other columns.

Question: Can we identify any patterns in the missing data?

From the visualization above, we can also identify that only three regions contain missing values:

Sub-Saharan Africa
Middle East and Northern Africa
Latin America and Carribbean
The Sub-Saharan Africa region contains the most missing values, accounting for about 9 percent 
of that regions's values. Since we'd like to analyze the data according to region, we should also
 think about how these values impact the analysis for this region specifically.
'''

# Handling Missing Values with Imputation

'''
we confirmed:

Only about 4 percent of the values in each column are missing.
Dropping rows with missing values won't cause us to lose information in other columns.
As a result, it may be best to drop the remaining missing values.

However, before we make a decision, let's consider handling the missing values by replacing
 them with estimated values, also called imputation.

Check for errors in data cleaning/transformation.
Use data from additional sources to fill missing values.
Drop row/column.
Fill missing values with reasonable estimates computed from the available data.
There are many options for choosing the replacement value, including:

A constant value
The mean of the column
The median of the column
The mode of the column
For non-numeric columns, common replacement values include the most frequent value or a string like 
"Unknown" that is used to treat missing values as a separate category.

For numeric columns, it's very common to replace missing values with the mean. Since the rest of the columns
 in combined with missing data are all numeric, we'll explore this option next.

First, let's build some intuition around this technique by analyzing how replacing missing values with the 
mean affects the distribution of the data. In order to do so, we'll use the Series.fillna() method to replace
 the missing values with the mean.

Note that we must pass the replacement value into the Series.fillna() method. For example, if we wanted to
 replace all of the missing values in the HAPPINESS SCORE column with 0, we'd use the following syntax:

combined[`HAPPINESS SCORE`].fillna(0)
'''

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.fillna.html

happiness_mean = combined['HAPPINESS SCORE'].mean()
print(happiness_mean)

combined['HAPPINESS SCORE UPDATED'] = combined['HAPPINESS SCORE'].fillna(happiness_mean)

print(combined['HAPPINESS SCORE UPDATED'].mean())

# Based on the results of this exercise, try to answer the question below:
# Did replacing missing values with the mean of a series cause the mean to change?
# answer: no

# Dropping Rows


combined = combined.dropna(axis=0)

missing = combined.isnull().sum()
print(missing)

'''
In the last step, we concluded that in this case, it was better to drop the remaining rows with missing 
values rather than replace the missing values with the mean.

However, it's also good to know that other techniques for handling missing values do exist. Since this 
lesson is meant to be an introduction to this topic, we didn't cover them, but if you're interested in 
learning more, you can start here.

Although there is no perfect way to handle missing values and each situation is different, now we know
 the basic techniques and built some intuition around them to better inform our decisions. Below is the
   workflow we used to clean missing values:

Check for errors in data cleaning/transformation.
Use data from additional sources to fill missing values.
Drop row/column.
Fill missing values with reasonable estimates computed from the available data.
We also started to set a more defined data cleaning workflow, in which we:

Set a goal for the project.
Researched and tried to understand the data.
Determined what data was needed to complete our analysis.
Added columns.
Cleaned specific data types.
Combined data sets.
Removed duplicate values.
Handled the missing values.
Next, we'll synthesize and practice what we've learned in the Guided Project.
'''
