import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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