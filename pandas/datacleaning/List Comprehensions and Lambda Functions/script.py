# List Comprehensions and Lambda Functions

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

import json

world_cup_str = """
[
    {
        "team_1": "France",
        "team_2": "Croatia",
        "game_type": "Final",
        "score" : [4, 2]
    },
    {
        "team_1": "Belgium",
        "team_2": "England",
        "game_type": "3rd/4th Playoff",
        "score" : [2, 0]
    }
]
"""
 # using json.loads() to convert JSON data from a string to Python objects!
    
    
world_cup_obj = json.loads(world_cup_str)
# to convert into python objects
# load string so loads() is used
# json.load() with no s is used to load from a file object

# reading a json file

'''
One of the places where the JSON format is commonly used is in the results returned by an Application 
programming interface (API). APIs are interfaces that can be used to send and transmit data between
 different computer systems. We'll learn about how to work with APIs in a later course.

The data set from this lesson — hn_2014.json — was downloaded from the Hacker News API. 
It's a different set of data from the CSV we've been using in the previous two lessons, 
and it contains data about stories from Hacker News in 2014.

To read a file from JSON format, we use the json.load() function. Note that the function is json.load() 
without an "s" at the end. The json.loads() function is used for loading JSON data from a string
 ("loads" is short for "load string"), whereas the json.load() function is used to load from a file object.
   Let's look at how we would read that in our data:

Note that we're using with to open the file, which is a better practice than just using open(). 
You can read more about with here.

import json
with open("hn_2014.json", "r") as file:
    hn = json.load(file)

print(type(hn))

class 'list'

Our hn variable is a list. Let's find out how many objects are in the list, and the type of the first
 object (which will almost always be the type of every object in the list in JSON data):

print(len(hn))
print(type(hn[0]))

35806
class 'dict'

Our data set contains 35,806 dictionary objects, each representing a Hacker News story. 
In order to understand the format of our data set, we'll print the keys of the first dictionary:

print(hn[0].keys())
dict_keys(['author', 'numComments', 'points', 'url', 'storyText', 'createdAt', 'tags', 'createdAtI',
 'title', 'objectId'])

Explain

Copy
If we recall the data set we used in the previous two lessons, we can see some similarities. 
There are keys representing the title, URL, points, number of comments, and date, as well as 
some others that are less familiar to us. Here is a summary of the keys and the data that they contain:

author: The username of the person who submitted the story.
createdAt: The date and time at which the story was created.
createdAtI: An integer value representing the date and time at which the story was created.
numComments: The number of comments that were made on the story.
objectId: The unique identifier from Hacker News for the story.
points: The number of points the story acquired, calculated as the total number of upvotes minus the
 total number of downvotes.
storyText: The text of the story (if the story contains text).
tags: A list of tags associated with the story.
title: The title of the story.
url: The URL that the story links to (if the story links to a URL).
'''


with open('hn_2014.json', 'r') as file:
#     open file with open() as a file object
    hn = json.load(file)
#     json.load() function to parse the file object and assign the result


# Deleting Dictionary Keys

'''
The function will use the json.dumps() function ("dump string") which does the opposite of the json.loads() function — it takes a JSON object and returns a string version of it. The json.dumps() function accepts arguments that can specify formatting for the string, which we'll use to make things easier to read:

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
​
first_story = hn[0]
jprint(first_story)

{
    "author": "dragongraphics",
    "createdAt": "2014-05-29T08:07:50Z",
    "createdAtI": 1401350870,
    "numComments": 0,
    "objectId": "7815238",
    "points": 2,
    "storyText": "",
    "tags": [
        "story",
        "author_dragongraphics",
        "story_7815238"
    ],
    "title": "Are we getting too Sassy? Weighing up micro-optimisation vs. maintainability",
    "url": "http://ashleynolan.co.uk/blog/are-we-getting-too-sassy"
}

You may notice that the createdAt and createdAtI keys both have the date and time data in two different formats. Because the format of createdAt is much easier to understand, let's do some data cleaning by deleting the createdAtI key from every dictionary.

To delete a key from a dictionary, we can use the del statement. Let's learn the syntax by looking at a simple example:

d = {'a': 1, 'b': 2, 'c': 3}
del d['a']
print(d)


'''

def del_key(dict_, key):
    # create a copy so we don't
    # modify the original dict
    modified_dict = dict_.copy()
    del modified_dict[key]
    return modified_dict


hn_clean = []

for i in hn:
    hn_clean.append(del_key(i, 'createdAtI'))
    # delete createdAI key from each dictionary in hn


# Writing List Comprehensions

# List Comprehensions. A list comprehension provides a concise way of creating lists in a single line of code.

# LOOP VERSION
#
# hn_clean = []
#
# for d in hn:
#     new_d = del_key(d, 'createdAtI')
#     hn_clean.append(new_d)


hn_clean = [del_key(d, 'createdAtI') for d in hn]
# same thing in the single line of code, list comprehension

# Using List Comprehensions to Transform and Create Lists

'''
List comprehensions can be used for many different things. Three common applications are:

Transforming a list
Creating a new list
Reducing a list
On this screen, we're going to look at the first two of these applications.

The first application, transforming a list, is the category that all the examples you've 
seen so far fit under. You are taking an existing list, applying a transformation to every
 value, and assigning it to a variable.
'''

# Use a list comprehension to extract the url value from each dictionary in hn_clean. Assign the result to urls.

urls = [d['url'] for d in hn_clean]
# get urls


#  Using List Comprehensions to Reduce a List

thousand_points = [value for value in hn_clean if value['points'] > 1000]

num_thousand_points = len(thousand_points)


# Passing Functions as Arguments


def keyFunc(dict_):
    return dict_['numComments']


most_comments = max(hn_clean, key=keyFunc)
# key is a function
# max() function to find the dictionary in hn_clean that has the most comments

'''
Lambda Functions
Learn
Usually, we create functions when we want to perform the same task many times. 
In the previous exercise, we created a function to use just once — as an argument to max().

Python provides a special syntax to create temporary functions for situations like these.
These functions are called lambda functions. Lambda functions can be defined in a single line, 
which allows you to define a function you want to pass as an argument at the time you need it.

While it's uncommon to assign a lambda function to a variable name in practice, we'll do
 that here to help illustrate how lambda functions work through some simple examples. 
 We'll start with a function that returns a single argument without modifying it:

def unchanged(x):
    return x
'''

'''
To create a lambda function equivalent of this function, we:

Use the lambda keyword, followed by
The parameter and a colon, and then
The transformation we wish to perform on our argument
'''

'''
If a function is particularly complex, it may be a better 
choice to define a regular function rather than create a lambda, 
even if it will only be used once. For instance, this function below,
 which extracts digits from a string and then adds one to the resultant 
 integer:

def extract_and_increment(string):
    digits = re.search(r"\d+", string).group()
    incremented = int(digits) + 1
    return incremented

It becomes tough to understand in its lambda form:

extract_and_increment = lambda string: int(re.search(r"\d+", string).group()) + 1

Being mindful of this will ensure our code remains easy to read and
 understand. In general, it's a good practice to use regular functions 
 for more complex operations and reserve lambda functions for simple,
   one-line operations.
'''

# def multiply(a, b):
#    return a * b
# traditional syntax

multiply = lambda a, b: a*b

# Using Lambda Functions to Analyze JSON data

'''
assigning a lambda to a variable so it can be called by name 
is a pretty uncommon pattern. The primary use of lambda functions
 is to define a function in place, like when we are providing a 
 function as an argument.

So we have a more precise understanding of how a lambda function works,


'''


hn_sorted_points = sorted(hn_clean, key=(lambda i: i['points']), reverse=True)
# sort hn_clean by points
# key is a lambda function that takes a dictionary and returns the value of the points key
# reverse=True to sort in descending order
# sorted() function to sort the list of dictionaries hn_clean by points in descending order
# lambda function to specify the value we want to use to sort the dictionaries

top_5_titles = [(i['title']) for i in hn_sorted_points[:5]]
# get top 5 titles
# get the titles of the top 5 stories by points, we already sorted the list hn_clean by points



# Reading JSON files into pandas

'''
we've worked with our JSON data using pure Python. One other option available to us is to convert the JSON to a pandas dataframe and then use pandas methods to manipulate it.

Pandas has the pd.read_json() function, which is designed to read JSON from either a file or a JSON string. In our case, our JSON exists as Python objects already, so we don't need to use this function.

Because the structure of JSON objects can vary a lot, sometimes you will need to prepare your data in order to be able to convert it to a tabular form. In our case, our data is a list of dictionaries, which pandas is easily able to convert to a dataframe.

Let's look at our JSON example again:

jprint(json_obj)
# jprint is a function that prints JSON objects in a more readable way

[
    {
        "age": 36,
        "favorite_foods": ["Pumpkin", "Oatmeal"],
        "name": "Sabine"
    },
    {
        "age": 40,
        "favorite_foods": ["Chicken", "Pizza", "Chocolate"],
        "name": "Zoe"
    },
    {
        "age": 40,
        "favorite_foods": ["Caesar Salad"],
        "name": "Heidi"
    }
]

We can convert this JSON to a pandas dataframe by passing it to
 the pd.DataFrame() constructor:

Each of the dictionaries will become a row in the dataframe, 
with each key corresponding to a column name.


We can use the pd.DataFrame() constructor and pass the list of 
dictionaries directly to it to convert the JSON to a dataframe:

json_df = pd.DataFrame(json_obj)
because the JSON data is already in a list of dictionaries, 
json in python is list of dictionaries or an object,

print(json_df)

age                 favorite_foods    name
0   36             [Pumpkin, Oatmeal]  Sabine
1   40    [Chicken, Pizza, Chocolate]     Zoe
2   40                 [Caesar Salad]   Heidi

In this case, the favorite_foods column contains the list 
from the JSON. We'll see a similar thing with the tags column
 for our Hacker News data.
'''

hn_df = pd.DataFrame(hn_clean)
# convert hn_clean to a pandas dataframe
# hn_clean is a list of dictionaries
# each dictionary will become a row in the dataframe, with each key corresponding
# to a column name

# Exploring Tags Using the Apply Function

'''
Just like the favorite_food column in our example data on the
 previous screen, the tags column is a column where each item 
 contains the list of data from our original JSON.

 At first glance, it looks like each values in this JSON list
   contain three items:

The string story
The name of the author
The story ID

If that's the case, then the column doesn't contain any 
unique data, and we can remove it. We're going to analyze this
 column to make sure that's the case.

tags = hn_df['tags']
print(tags.dtype)

object

The tags column is stored as an object type. Whenever pandas uses the object type, each item in the series uses a Python object to store the data. Most commonly we see this type used for string data.

We previously learned that we could use the Series.apply() method to apply a function to every item in a series. Let's look at what we get when we pass the type() function as an argument to the column:

tags_types = tags.apply(type)
type_counts = tags_types.value_counts(dropna=False)
print(type_counts)

class 'list'    35806
Name: tags, dtype: int64

All 35,806 items in the column are a Python list type.

Next, let's use Series.apply() to check the length of each of those lists. If our hypothesis from earlier is correct, every row will have a list containing three items:

tags_types = tags.apply(len)
type_lengths = tags_types.value_counts(dropna=False)
print(type_lengths)

3    33459
4     2347
Name: tags, dtype: int64

While most of the item have three values in the list, about 2,000 
values contain four values. Let's use a boolean mask to look 
at the items where the list has four items:

'''

'''
Instructions

1. Use Series.apply() and len() to create a boolean mask based
 on whether each item in tags has a length of 4.

2. Use the boolean mask to filter tags. Assign the result to four_tags.

'''

tags = hn_df['tags']

# Series.apply(func, convert_dtype=<no_default>, args=(), *, by_row='compat', **kwargs)

four_tags = tags[tags.apply(func=len) == 4]
# boolean mask


# Extracting Tags Using Apply with a Lambda Function

'''
 we're going to use a lambda function to extract this fourth value in cases where there is one. To do this for any single list, we'll need to:

Check the length of the list.
If the length of the list is equal to four, return the last value.
If the length of the list isn't equal to four, return a null value.
This is how we could create this as a standard function:

def extract_tag(l):
    if len(l) == 4:
        return l[-1]
    else:
        return None


We could use Series.apply() to apply this function as is, but to practice working with lambda functions, let's look at how we can complete this operation in a single line.

To achieve this, we'll have to use a special version of an if statement known as a ternary operator. You can use the ternary operator whenever you need to return one of two values depending on a boolean expression. The syntax is as follows:

[on_true] if [expression] else [on_false]
'''

def extract_tag(l):
    return l[-1] if len(l) == 4 else None


cleaned_tags = tags.apply(extract_tag)

hn_df['tags'] = cleaned_tags
# updated tags
# apply extract_tag to each item in tags
# assign the result to cleaned_tags
# update the tags column in hn_df with the cleaned_tags
# use the apply() method to apply the extract_tag function to each item in the tags column

