import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

happiness2015 = pd.read_csv('World_Happiness_2015.csv')


world_dev = pd.read_csv("World_dev.csv")
col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}

merged = pd.merge(left=happiness2015, right=world_dev, how='left', left_on = 'Country', right_on='ShortName')

merged = merged.rename(col_renaming, axis=1)
# df.rename(mapper, axis=1) 
# column renaming


def extract_last_word(element):
#     convert element into string
    element = str(element)
    element_list = element.split()
    return element_list[-1]


merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last_word)

print(merged['Currency Apply'].head())

'''
Instead, we could've split each element in the CurrencyUnit column 
into a list of strings with the Series.str.split() method,
 the vectorized equivalent of Python's string.split() method
'''

'''
Method	Description
Series.str.split()	Splits each element in the Series.
Series.str.strip()	Strips whitespace from each string in the Series.
Series.str.lower()	Converts strings in the Series to lowercase.
Series.str.upper()	Converts strings in the Series to uppercase.
Series.str.get()	Retrieves the ith element of each element in the Series.
Series.str.replace()	Replaces a regex or string in the Series with another string.
Series.str.cat()	Concatenates strings in a Series.
Series.str.extract()	Extracts substrings from the Series matching a regex pattern.
We access these vectorized string methods by adding a str between the Series name and method name:

'''

'''
The str attribute indicates that each object in the Series should
 be treated as a string, without us having to explicitly change
   the type to a string like we did when using the apply method.

Note that we can also slice each element in the Series to extract 
characters, but we'd still need to use the str attribute. 
For example, below we access the first five characters in each
 element of the CurrencyUnit column:
'''

'''
It's also good to know that vectorized string methods can be 
chained. For example, suppose we needed to split each element
 in the CurrencyUnit column into a list of strings using the 
 Series.str.split() method and capitalize the letters using the 
 Series.str.upper() method. You can use the following syntax
   to apply more than one method at once:

merged['CurrencyUnit'].str.upper().str.split()
'''

merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(1)
# get the last word

print(merged['Currency Vectorized'].head())

lengths = merged['CurrencyUnit'].str.len()

value_counts = lengths.value_counts(dropna=False)

# should you use series.apply() to calculate length, it will also count NaN as string

#  Finding Specific Words in Strings

# we will use regex for this, ie. regular expression

pattern = r"[Nn]ational accounts"
 # The brackets, [], indicate that either "national accounts" or "National accounts" should produce a match.
    
national_accounts = merged['SpecialNotes'].str.contains(pattern)
print(national_accounts.head())

pattern = r"[Nn]ational accounts"

national_accounts = merged['SpecialNotes'].str.contains(pattern, na=False, regex=True)
# Fill value for missing values. The default depends on dtype of the array. For object-dtype, numpy.nan is used. For StringDtype, pandas.NA is used.

merged_national_accounts = merged[national_accounts]

print(merged_national_accounts.head())

# Extracting Substrings from a Series


'''
With regular expressions, we use the following syntax to indicate a character could be a range of numbers:

pattern = r"[0-9]"

And we use the following syntax to indicate a character could be a range of letters:

#lowercase letters
pattern1 = r"[a-z]"
​
#uppercase letters
pattern2 = r"[A-Z]"

We could also make these ranges more restrictive. For example, if we wanted to find a three character substring in a column that starts with a number between 1 and 6 and ends with two letters of any kind, we could use the following syntax:

pattern = r"[1-6][a-z][a-z]"

If we have a pattern that repeats, we can also use curly brackets { and } to indicate the number of times it repeats:

pattern = r"[1-6][a-z][a-z]" = r"[1-6][a-z]{2}"
'''

pattern = r"([1-2][0-9]{3})"
# {3} is to repeat [0-9] 3 times ie r'[1-2][0-9][0-9][0-9]'
# dont forget the bracket r'()'
# Create a regular expression that will match years and assign it to the variable pattern. eg, 2015, 1999

years = merged['SpecialNotes'].str.extract(pattern)

'''
In the last exercise, we learned how to identify more complex 
patterns with regular expressions and extract substrings from a 
column using that pattern.

When we used the Series.str.extract() method, we enclosed our
 regular expression in parentheses. The parentheses indicate that
   only the character pattern matched should be extracted and
     returned in a series. We call this a capturing group.
'''

# However, the Series.str.extract() method will only extract 
# the first match of the pattern. If we wanted to extract all 
# of the matches, we can use the Series.str.extractall() method.

'''
 let's use the same regular expression from the last screen
   to extract all the years from the Special Notes column, 
   except this time, we'll use a named capturing group. 
   Using a named capturing group means that we can refer 
   to the group by the specified name instead of just a number. 
   We can use the following syntax to add a name: 
   (?P<Column_Name>...).

Below, we name the capturing group Years:

pattern = r"(?P<Years>[1-2][0-9]{3})"
merged['SpecialNotes'].str.extractall(pattern)

'''

merged = merged.set_index('Country')
# we set index the rows by country

pattern = r"(?P<Years>[1-2][0-9]{3})"

years = merged['IESurvey'].str.extractall(pattern)

value_counts = years.value_counts

print(value_counts)

'''
Let's add those two groups to our regex and try to extract
 them again:

pattern = r"(?P[1-2][0-9]{3})(/)?(?P[0-9]{2})?"
years = merged['IESurvey'].str.extractall(pattern)

Explain

Copy
Note that we also added a question mark, ?, after each of
 the two new groups to indicate that a match for those groups 
 is optional. This allows us to extract years listed in the
   yyyy format AND the yyyy/yy format at once.
'''

pattern = r"(?P<First_Year>[1-2][0-9]{3})/?(?P<Second_Year>[0-9]{2})?"

# created a regular expression that extracts the pattern "yyyy/yy" and saved it to a variable called pattern. Notice that we didn't enclose /? in parentheses so that the resulting dataframe will only contain a First_Year and Second_Year column.

# We've created a regular expression that extracts the pattern "yyyy/yy" and saved it to a variable called pattern. Notice that we didn't enclose /? in parentheses so that the resulting dataframe will only contain a First_Year and Second_Year column. and not include for '/' column


years = merged['IESurvey'].str.extractall(pattern)
# Use the Series.str.extractall() method to extract pattern from the IESurvey column. Assign the result to years.


first_two_year = years['First_Year'].str.slice(start=0, stop=2)
# Use vectorized slicing to extract the first two numbers from the First_Year column in years (For example, extract "20" from "2000"). Assign the result to first_two_year.


years['Second_Year'] = first_two_year + years['Second_Year']
# Add first_two_year to the Second_Year column in years, so that Second_Year contains the full year (ex: "2000"). Assign the result to years['Second_Year'].


'''
Instructions
As a reminder, we would like to clean the values in the IncomeGroup column to a standardized format shown in the table below.

Current Values
Updated Values
Upper middle income	UPPER MIDDLE
Lower middle income	LOWER MIDDLE
High income: OECD	HIGH OECD
Low income	LOW
High income: nonOECD	HIGH NONOECD
Use some of the string methods above to clean the IncomeGroup column.
Make sure to remove the whitespace at the end of the strings.

'''
'''
Let's use some of the vectorized string methods below to update the values in the IncomeGroup column next:

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

# merged[merged['IncomeGroup'] == 'Upper middle income'] = 'UPPER MIDDLE'
# DONT DO THIS  it will update all the avlues with the assigned values for all the fields related to that data


# merged[merged['IncomeGroup'] == 'Lower middle income'] = 'LOWER MIDDLE'

# merged[merged['IncomeGroup'] == 'High income: OECD'] = 'HIGH OECD'

# merged[merged['IncomeGroup'] == 'Low income'] = 'LOW'

# merged[merged['IncomeGroup'] == 'High income: nonOECD'] = 'HIGH NONOECD'

# instead using series.str.replace()

merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(pat='Upper middle income', repl='UPPER MIDDLE')


merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(pat='Lower middle income', repl='LOWER MIDDLE')

merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(pat='High income: OECD', repl='HIGH OECD')

merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(pat='Low income', repl='LOW')

merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(pat='High income: nonOECD', repl='HIGH NONOECD')

print(merged['IncomeGroup'].head(25))

# Use the df.pivot_table() method to return the mean of each income group in the IncomeGroup column. Set the index parameter equal to the IncomeGroup column and the values parameter equal to the Happiness Score column. Assign the result to pv_incomes.
pv_incomes = merged.pivot_table(values='Happiness Score', index='IncomeGroup')
# by default mean as aggfunc


# Use the df.plot() method to plot the results. Set the kind parameter equal to bar, the rot parameter equal to 30, and the ylim parameter equal to (0,10).
pv_incomes.plot(kind='bar', rot=30, ylim=(0, 10))
plt.show()

# https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#method-summary