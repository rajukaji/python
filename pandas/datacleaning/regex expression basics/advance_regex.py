import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np


'''
 In this lesson, we're going to build on those foundational principles, and learn:

Several new regex syntax components to allow us to express more complex criteria.
How to combine regular expression patterns to extract and transform data.
How to replace and clean data using regular expressions.
We're going to continue working with the dataset from the previous lesson from technology 
site Hacker News. Let's take a moment to refresh our memory of the different columns in this dataset:

id: The unique identifier from Hacker News for the story
title: The title of the story
url: The URL that the stories links to, if the story has a URL
num_points: The number of points the story acquired, calculated as the total number of 
upvotes minus the total number of downvotes
num_comments: The number of comments that were made on the story
author: The username of the person who submitted the story
created_at: The date and time at which the story was submitted
We'll continue to analyze and count mentions of different programming languages in the dataset, 
and then we'll finish by extracting the different components of the URLs submitted to Hacker News.

As we mentioned in the previous lesson, you shouldn't expect to remember every single detail of
 regular expression syntax. The most important thing is to understand the core principles, 
 what is possible, and where to look up the details. This will mean you can quickly jog your
   memory whenever you need regular expressions.

We'll be building on the foundational concepts that we learned in the previous lesson. 
If you need to refresh any points of the syntax while you complete exercises in this lesson,
 we recommend using a regex syntax reference like RegExr so you can practice looking up syntax as you need it.

Let's start by reading in the dataset using pandas and extracting the story titles from the title column:

import pandas as pd

hn = pd.read_csv("hacker_news.csv")
titles = hn['title']


In the story titles, we have two different capitalizations for the Python language: Python and python.
 In the previous lesson, we learned two techniques for handling cases like these.
   The first is to use a set to match either P or p:

pattern = r"[Pp]ython"
python_counts = titles.str.contains(pattern).sum()
print(python_counts)

160

The second option we learned is to use re.I — the ignorecase flag — to make our pattern case insensitive:

pattern = r"python"
python_counts = titles.str.contains(pattern, flags=re.I).sum()
print(python_counts)

160

The ignorecase flag is particularly useful when we have many different capitalizations for a word or phrase.
 In our dataset, the SQL language has three different capitalizations: SQL, sql, and Sql.

To use sets to capture all of these variations, we would need to use a set for each character:

pattern = r"[Ss][Qq][Ll]"
sql_counts = titles.str.contains(pattern).sum()
print(sql_counts)

108

'''

hn = pd.read_csv("hacker_news.csv")
titles = hn['title']

pattern = 'sql'
sql_counts = titles.str.contains(pattern, flags=re.I).sum()
# case insensitive pattern


# Capture Groups

'''
In the previous exercise, we counted the number of mentions of "SQL" in the titles of stories. As we learned in the previous lesson, to extract those mentions, we need to do two things:

Use the Series.str.extract() method.
Use a regex capture group.
We define a capture group by wrapping the part of our pattern we want to capture in parentheses. If we want to capture the whole pattern, we just wrap the whole pattern in a pair of parentheses
'''
'''
Next, we use Series.str.extract() to extract the different capitalizations:

sql_capitalizations = titles.str.extract(pattern, flags=re.I, expand=False)

Recall that we specify expand=False with the Series.str.extract() method to return a series. Lastly, we use the Series.value_counts() method to create a frequency table of those capitalizations:

sql_capitalizations_freq = sql_capitalizations.value_counts()
print(sql_capitalizations_freq)

SQL    101
Sql      4
sql      3
Name: title, dtype: int64

We can extend this analysis by looking at titles that have letters immediately before the "SQL," which is a convention often used to denote different variations or flavors of SQL:

pattern = r"(\w+SQL)"
sql_flavors = titles.str.extract(pattern, flags=re.I, expand=False)
sql_flavors_freq = sql_flavors.value_counts()
print(sql_flavors_freq)

PostgreSQL    27
NoSQL         16
MySQL         12
CloudSQL       1
SparkSQL       1
MemSQL         1
nosql          1
mySql          1
Name: title, dtype: int64

Notice how there is some duplication due to varied capitalization in this frequency table:

NoSQL and nosql
MySQL and mysql
In this exercise, we're going to extract the mentions of different SQL flavors into a new column and clean those duplicates by making them all lowercase. We'll then analyze the results to look at the average number of comments for each flavor.
'''
hn_sql = hn[hn['title'].str.contains(r"\w+SQL", flags=re.I)].copy()

hn_sql = hn[hn['title'].str.contains(r"\w+SQL", flags=re.I)].copy()

hn_sql['flavor'] = hn_sql['title'].str.extract(r'(\w+sql)', expand=False, flags=re.I)

hn_sql['flavor'] = hn_sql['flavor'].str.lower()

sql_pivot = hn_sql.pivot_table(index='flavor', values='num_comments', aggfunc='mean')


# Using Capture Groups to Extract Data

# [\d.]+

# this means, one or more digit or characters

'''
Instructions
Write a regular expression pattern which will match Python or python, followed by a space, followed by one or more digit characters or periods.
The regular expression should contain a capture group for the digit and period characters (the Python versions)
'''

# pattern = r'[pP]ython ?([\d\.]+)'

# py_versions = titles.str.extract(pattern, expand=False)

# py_versions_freq = dict(py_versions.value_counts())

pattern = r"[Pp]ython ([\d\.]+)"
# we are only capturing the digits and periods
py_versions = titles.str.extract(pattern, expand=False)
py_versions_freq = dict(py_versions.value_counts())
# converting into a dictonary

