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