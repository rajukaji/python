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

# [\d\.]+

# this means, one or more digit or period

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

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10

pattern = r"\b[Cc]\b[^\.\+]"
# \b is a word boundary
# we only want C or c characters to search for, not C++ or C., we dont want anything
#  after C which is why, we are avoiding '.' or '+'

first_ten = first_10_matches(pattern)


#  Using Lookarounds to Control Matches Based on Surrounding Text

'''
Let's look at the result of the previous exercise:

365                                             The new C standards are worth it
444                                  Moz raises $10m Series C from Foundry Group
521                                 Fuchsia: Micro kernel written in C by Google
1307                                   Show HN: Yupp, yet another C preprocessor
1326                                            The C standard formalized in Coq
1365                                                 GNU C Library 2.23 released
1429    Cysignals: signal handling (SIGINT, SIGSEGV, ) for calling C from Python
1620                                               SDCC  Small Device C Compiler
1949         Rewriting a Ruby C Extension in Rust: How a Naive One-Liner Beats C
2195                    MyHTML  HTML Parser on Pure C with POSIX Threads Support
Name: title, dtype: object

Explain

Copy
It looks like we're getting close. In our first 10 matches we have one irrelevant result,
 which is about "Series C," a term used to represent a particular type of startup fundraising.

Additionally, we've run into the same issue as we did in the previous lesson — by using a negative set,
 we may have eliminated any instances where the last character of the title is "C" (the second last line 
 of output matches in spite of the fact that it ends with "C," because it also has "C" earlier in the string).

Neither of these can be avoided using negative sets, which are used to allow multiple matches for a 
single character. Instead we'll need a new tool: lookarounds.

Lookarounds let us define a character or sequence of characters that either must or must not come 
before or after our regex match. There are four types of lookarounds:


'''

'''
lookaround              Pattern         Explanation

positive lookahead      zzz(?=abc)      matches zzz only when it is followed by abc

negative lookahead      zzz(?!abc)      matches zzz only when it is not followed by abc

positive lookbehind     (?<=abc)zzz     matches zzz only when it is preceded by abc

negative lookbehind     (?<!abc)zzz     matches zzz only when it is not preceded by abc
'''

'''
These tips can help you remember the syntax for lookarounds:

Inside the parentheses, the first character of a lookaround is always ?.
If the lookaround is a lookbehind, the next character will be <, 
which you can think of as an arrow head pointing behind the match.
The next character indicates whether the lookaround is positive (=) or negative (!).
While building regular expressions, you can also use the OR operator |.
 The | operator allows the expression to match either the condition preceding it or the one following it. 
 For example, the expression ((?![+.])|\.$) matches either instances that are not
   followed by . or + or instances where the match is at the end of the sentence.
     This becomes handy in complex lookaround operations.

Let's create some test data that we'll use to illustrate how lookarounds work:

test_cases = ['Red_Green_Blue',
              'Yellow_Green_Red',
              'Red_Green_Red',
              'Yellow_Green_Blue',
              'Green']

We'll also create a function that will loop over our test cases and tell us whether our pattern matches.
 We'll use the re module rather than pandas since it tells us the exact text that matches,
   which will help us understand how the lookaround is working:

def run_test_cases(pattern):
    for tc in test_cases:
        result = re.search(pattern, tc)
        print(result or "NO MATCH")


In each instance, we'll aim to match the substring Green depending on the characters that precede or
 follow it. Let's start by using a positive lookahead to include instances where the match is followed 
 by the substring _Blue. We'll include the underscore character in the lookahead, otherwise
   we will get zero matches:

run_test_cases(r"Green(?=_Blue)")


_sre.SRE_Match object; span=(4, 9), match='Green'
NO MATCH
NO MATCH
_sre.SRE_Match object; span=(7, 12), match='Green'
NO MATCH

Notice how the matches themselves are purely the text Green and don't include the lookahead. 
Let's look at a negative lookahead to include instances where the match is not followed by the substring _Red:

run_test_cases(r"Green(?!_Red)")


_sre.SRE_Match object; span=(4, 9), match='Green'
NO MATCH
NO MATCH
_sre.SRE_Match object; span=(7, 12), match='Green'
_sre.SRE_Match object; span=(0, 5), match='Green'


Next we'll use a positive lookbehind to include instances where the match is preceded by the substring Red_:

run_test_cases(r"(?<=Red_)Green")

_sre.SRE_Match object; span=(4, 9), match='Green'
NO MATCH
_sre.SRE_Match object; span=(4, 9), match='Green'
NO MATCH
NO MATCH


And finally, using a negative lookbehind to include instances where the match isn't preceded
 by the substring Yellow_:

run_test_cases(r"(?


_sre.SRE_Match object; span=(4, 9), match='Green'
NO MATCH
_sre.SRE_Match object; span=(4, 9), match='Green'
NO MATCH
_sre.SRE_Match object; span=(0, 5), match='Green'


The contents of a lookaround can include any other regular expression component. For instance, 
here is an example where we match only cases that are followed by exactly five characters:

run_test_cases(r"Green(?=.{5})")


_sre.SRE_Match object; span=(4, 9), match='Green'
NO MATCH
NO MATCH
_sre.SRE_Match object; span=(7, 12), match='Green'
NO MATCH


The second and third test cases are followed by four characters, not five, and the last test case
 isn't followed by anything.

Sometimes programming languages won't implement support for all lookarounds (notably, 
lookbehinds are not in the official JavaScript specification). As an example, to get full support 
in the RegExr tool, you'll need to set it to use the PCRE regex engine.

In this exercise, we're going to use lookarounds to refine the regular expression we built on 
the last screen to capture mentions of the "C" programming language. As a reminder, here is the
last of the regular expressions we attempted to use with this exercise earlier, and the resultant 
titles that match:

first_10_matches(r"\b[Cc]\b[^.+]")


364                                             The new C standards are worth it
444                                  Moz raises $10m Series C from Foundry Group
521                                 Fuchsia: Micro kernel written in C by Google
1308                                   Show HN: Yupp, yet another C preprocessor
1327                                            The C standard formalized in Coq
1366                                                 GNU C Library 2.23 released
1430    Cysignals: signal handling (SIGINT, SIGSEGV, ) for calling C from Python
1621                                               SDCC  Small Device C Compiler
1950         Rewriting a Ruby C Extension in Rust: How a Naive One-Liner Beats C
2196                    MyHTML  HTML Parser on Pure C with POSIX Threads Support
Name: title, dtype: object


Let's now use lookarounds to exclude the matches we don't want. We want to:

Keep excluding matches that are followed by . or +, but still match cases where "C" 
falls at the end of the sentence.
Exclude matches that have the word 'Series' immediately preceding them.
'''

'''
Instructions
Write a regular expression and assign it to pattern. The regular expression should:
Match instances of C or c where they are not preceded or followed by another word character.
From the match above:
Exclude instances where it is followed by a . or + character, without removing instances where the match occurs at the end of the sentence. The end anchor (\.$) will help to preserve occurrences of c or C at the end of the sentence.
Exclude instances where the word 'Series' immediately precedes the match.
'''
# pattern = r'(?<!Series\s)\b[Cc]\b((?![ +.])|\.$)'


# c_mentions = titles.str.contains(pattern).sum()

pattern = r"(?<!Series\s)\b[Cc]\b((?![+.])|\.$)" 
# | or operator, we are using it to match the end of the sentence
# we are using negative lookbehind to exclude the word Series
# we are using negative lookahead to exclude the characters + and . after C
# we are using word boundary to match C or c
# \s is a whitespace character
# $ is an end of the sentence

c_mentions = titles.str.contains(pattern).sum()


# BackReferences: Using Capture Groups in a RegEx Pattern


'''
Let's say we wanted to identify strings that had words with double letters, like the "ee" in "feed."
 Because we don't know ahead of time what letters might be repeated, we need a way to specify a 
 capture group and then to repeat it. We can do this with backreferences.

Whenever we have one or more capture groups, we can refer to them using integers left to right as shown 
in this regex that matches the string HelloGoodbye:
'''

'''
# (hello)(goodbye)
# hello in one groupd and goodbye in another


# (hello)(goodbye)\2\1

# 2 is the contents of group 2,
# 2 is the contents of group 1. 

# The regular expression above will match the text HelloGoodbyeGoodbyeHello.

# we could write a regex to capture instances of the same two word characters in a row

# (\w)\1
# (start group 1
# \w ; a word character
# ) end group 1
# \1 ; the contents of group 1


# uppercase and lowercase are two different characters

'''


'''
Instructions
Write a regular expression to match cases of repeated words:
We'll define a word as a series of one or more word characters preceded and followed by a boundary anchor.
We'll define repeated words as the same word repeated twice, separated by a single whitespace character.
'''

pattern = r"\b(\w+)\s\1\b"
repeated_words = titles[titles.str.contains(pattern)]

#  Substituting Regular Expression Matches

'''
When we learned to work with basic string methods, we used the str.replace() method to replace simple
 substrings. We can achieve the same with regular expressions using the re.sub() function. 
 The basic syntax for re.sub() is:

re.sub(pattern, repl, string, flags=0)

The repl parameter is the text that you would like to substitute for the match. Let's look at a simple 
example where we replace all capital letters in a string with dashes:

string = "aBcDEfGHIj"
​
print(re.sub(r"[A-Z]", "-", string))

a-c--f---j

When working in pandas, we can use the Series.str.replace() method, which uses similar syntax:

Series.str.replace(pat, repl, flags=0, regex=False)

In pandas 2.0.1, it's important to note that when using regular expressions, you need to explicitly set 
regex=True. Additionally, if you want to use the flags parameter, you must also set regex=True.

Earlier, we discovered that there were multiple different capitalizations for SQL in our dataset. 
Let's look at how we could make these uniform with the Series.str.replace() method and a regular expression:

sql_variations = pd.Series(["SQL", "Sql", "sql"])

sql_uniform = sql_variations.str.replace(r"sql", "SQL", flags=re.I, regex=True)
print(sql_uniform)


0    SQL
1    SQL
2    SQL
dtype: object
'''

email_variations = pd.Series(['email', 'Email', 'e Mail',
                        'e mail', 'E-mail', 'e-mail',
                        'eMail', 'E-Mail', 'EMAIL'])


'''
Use a regular expression to replace each of the matches in email_variations with "email" and assign the result to email_uniform.Your regular expression should be compatible with the ignorecase flag, and should not match the word "emailing" or any other words that contain "email" as a substring.
You may need to iterate several times when writing your regular expression in order to match every item.
'''

pattern = r'e[\s-]?mail'
# \s is a whitespace character
# [\s-] is a whitespace or a hyphen
# ? is a zero or one occurence of the character before it, or we can write it as {0,1}

email_uniform = email_variations.str.replace(pat=pattern, repl='email', flags=re.I, regex=True)


'''
Use a regular expression to replace all mentions of email in titles with "email". Assign the result to titles_clean.
Note that passing the cases in email_variations does not guarantee passing all the cases in the titles column.
'''

titles_clean = titles.str.replace(pat=pattern, repl='email', flags=re.I, regex=True)


# Extracting Domains from URLs

