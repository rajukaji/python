# Regular Expression Basics

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# data set 
# https://www.kaggle.com/datasets/hacker-news/hacker-news-posts

hn = pd.read_csv('hacker_news.csv')

titles = hn["title"].tolist()

python_mentions = 0

pattern = '[Pp]ython'

for i in titles:
    if re.search(pattern, i):
        python_mentions += 1
        
print(python_mentions)


pattern = '[Pp]ython'

titles = hn['title'] 

python_mentions = titles.str.contains(pattern).sum()
# number of true values in the boolean masks 

titles = hn['title']

ruby_titles = titles[titles.str.contains('[rR]uby')]
# find either ruby or Ruby containing in teh titiles series
# passing boolean mask to retrieve the original values of titles

# The `titles` variable is available from 
# the previous screens

# using quantifier, date(year) finding regex

email_bool = titles.str.contains('e-{,1}mail')
# email_bool = titles.str.contains('e-?mail')
# both are the same
# '-' contains 0 or times, 

email_count = email_bool.sum()
print(email_count)
# count the matched emails

email_titles = titles[email_bool]

# To match the substring "[pdf]", we can use backslashes to escape both the open and closing brackets: \[pdf\].

# To match unknown characters using regular expressions, we use character classes. Character classes allow us 
# to match certain groups of characters.
#  We've actually seen two examples of character classes already:

# The set notation using brackets to match any of a number of characters.
# The range notation, which we used to match ranges of digits (like [0-9]).

# for set of characters
# [abc], either f, u, or c match
# range [a-e], any of the characters a, b, c, d, or e
# range [0-3], any of the characters 0, 1, 2, or 3
# range [A-Z], any upper case letter
# set + Range [A-Za-z], any upper or lowercase letter. 

# Ranges can be used for letters as well as numbers.
# Sets and ranges can be combined.
# Just like with quantifiers, there are some other common character classes which we'll use a lot.

# character class       pattern     Explanation
#  digit                \d          any digit character (equivalent to [0-9])
#  word                 \w          any digit, uppercase, lowercase, or underscore character (equivalent to [A-Za-z0-9_])
# whitespace            \s          any space, tab or linebreak character
#dot                    .           any character except newline

'''
The one that we'll be using to match characters in tags is \w, which represents any number or letter. 
Each character class represents a single character, so to match multiple characters 
(e.g. words like video and pdf), we'll need to combine them with quantifiers.

In order to match word characters between our brackets, we can combine the word character class
 (\w) with the 'one or more' quantifier (+), giving us a combined pattern of \w+.

This will match sequences like pdf, video, Python, and 2018 but won't match a sequence containing a
 space or punctuation character like PHP-DEV or XKCD Flowchart. If we wanted to match those tags as well, 
 we could use .+; however, in this case, we're just interested in single-word tags without special characters.

Let's quickly recap the concepts we learned in this screen:

We can use a backslash to escape characters that have special meaning in regular expressions
 (e.g. \[ will match an open bracket character).
Character classes let us match certain groups of characters (e.g. \w will match any word character).
Character classes can be combined with quantifiers when we want to match different numbers of characters.
'''


pattern = '\[\w+\]'

tag_titles = titles.str.contains(pattern)

tag_count = int(tag_titles.sum())
print(tag_count)


# Accessing the Matching Text with Capture Groups

'''
We strongly recommend using raw strings for every regex you write, rather than remember
 which sequences are escape sequences and using raw strings selectively. 
 That way, you'll never encounter a situation where you forget or overlook something which
   causes your regex to break.
'''

'''
In the previous screen, we were able to calculate that 444 of the 20,100 Hacker News stories in our
 dataset contain tags. What if we wanted to find out what the text of these tags were, and how many 
 of each are in the dataset?

In order to do this, we'll need to use capture groups. Capture groups allow us to specify 
one or more groups within our match that we can access separately. In this lesson, we'll learn
 how to use one capture group per regular expression, but in the next lesson we'll learn some more 
 complex capture group patterns.

We specify capture groups using parentheses. Let's add an open and close parentheses to the pattern 
we wrote in the previous screen, and break down how each character in our regular expression works:
'''

#  capture groups
# (                     \[                              \w+                                     \]                              ])
# start capture group   the escaped character '['       one or more word characters     the closing ']' character       end capture group

'''
pattern = r"(\[\w+\])"
tag_5_matches = tag_5.str.extract(pattern)
print(tag_5_matches)
'''
# ie any words between brackets, get words with brackets

'''
pattern = r"\[(\w+)\]"
tag_5_matches = tag_5.str.extract(pattern, expand=False)
print(tag_5_matches)
'''

# only get words, we dont need brackets for display
# based on what to capture, inside (...) is captured


'''
Note that we specify expand=False with the Series.str.extract() method to return a series. If we then use Series.value_counts() we can quickly get a frequency table of the tags:

tag_5_freq = tag_5_matches.value_counts()
print(tag_5_freq)
'''

pattern = r"\[(\w+)\]"

tag_freq = titles.str.extract(pattern, expand=False).value_counts()


# Negative Character Classes

'''
we wrote mostly simple regular expressions. In reality, regular expressions are often complex. 
When creating complex regular expressions, you often need to work iteratively so you can find "bad" 
instances that match your pattern and then exclude them.

In order to work faster as you build your regular expression, it can be helpful to create a function 
that returns the first few matching strings:

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10


Another useful approach is to use an online tool like RegExr that allows you to
build regular expressions and includes syntax highlighting, instant matches, and regex syntax 
reference. For this screen, we'll use the first_10_matches function we just built to iteratively 
build a regular expression.

Earlier, we counted the titles that included Python — let's write a simple regular expression
 to match Java (another popular language), and use our function to look at the matches:

first_10_matches(r"[Jj]ava")
'''

# https://regexr.com/

'''
We can see that there are a number of matches that contain Java as part of the word JavaScript.
 We want to exclude these titles from matching so we get an accurate count.

One way to do this is by using negative character classes. Negative character classes are 
character classes that match every character except a character class. Let's look at a table 
of the common negative character classes:
'''

'''
character class         pattern         Explanation

Negative set            [^fud]          any character except f, u, or d

negative set            [^1-3Z\s]       any character except 1, 2, 3, and Z, or whitespace characters

negative digit          \D              any character except digit characters

negative word           \W              any character except word characters

negative whitespace     \s              any character except whitespace characters

'''

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10


'''
Write a regular expression that will match titles containing Java.

Use the first_10_matches() function to return the first ten matches. You can also use a site like RegExr to build your regular expression.
The regex should match whether or not the first character is capitalized.
The regex shouldn't match where 'Java' is followed by the letter 'S' or 's', or when 'Java' appears at the end of the title, except when the string contains both 'Java' and 'JavaScript' in the title. In this case, the contains() function will always recognize the combined pattern as a match, even if the pattern for 'Java' followed by 'S' or 's' fails."
'''

java_titles = first_10_matches(r'[jJ]ava[^sS]')
# better to use raw expression, r'[jJ]ava[^sS]'
# because we dont want java to be followed by any other character starting with s or S, eg javascript


# Word Boundaries


'''
While the negative set was effective in removing any bad matches that mention JavaScript, 
it also had the side-effect of removing any titles where Java occurs at the end of the string, like this title:

Pippo  Web framework in Java
'''
'''
This is because the negative set [^Ss] must match one character. 
Instances at the end of a string aren't followed by any characters, so there is no match.

A different approach to take in cases like these is to use the word boundary anchor,
 specified using the syntax \b. A word boundary matches the position between a word character 
 and a non-word character, or a word character and the start/end of a string. 


 Let's look at how using a word boundary changes the match from the string in the example above:

string = "Sometimes people confuse JavaScript with Java"
pattern_1 = r"Java[^S]"

m1 = re.search(pattern_1, string)
print(m1)


The regular expression returns None, because there is no substring that contains Java 
followed by a character that isn't S.

Let's instead use word boundaries in our regular expression:

pattern_2 = r"\bJava\b"

m2 = re.search(pattern_2, string)
print(m2)

'''

'''
instruction

Write a regular expression that will match titles containing Java.
You might like to use the first_10_matches() function or a site like RegExr to build your regular expression.
The regex should match whether or not the first character is capitalized.
The regex should match only where 'Java' is preceded and followed by a word boundary.
Note that in cases where our string contains both 'Java' and 'JavaScript' in the title, 
the contains() function will always recognize the combined pattern as a match, even if 
the pattern for 'Java' followed by 'S' or 's' fails."
Select from titles only the items that match the regular expression. Assign the result to java_titles.
'''

pattern = r"\b[jJ]ava\b"
# this is how a boundary is created, 
# the word we are looking for is Java or java only, 
# it cannot be more than this, there shouldn't be any 
# characters before or after the pattern for that boundary 
# search of the word

java_titles = titles[titles.str.contains(pattern)]

# Matching at the Start and End of Strings

'''
So far, we've used regular expressions to match substrings contained anywhere within text.
 There are often scenarios where we want to specifically match a pattern at the start and end of strings.

On the previous screen, we learned that the word boundary anchor matches the space between 
a word character and a non-word character. More generally in regular expressions, an anchor
 matches something that isn't a character, as opposed to character classes which match specific characters.

Other than the word boundary anchor, the other two most common anchors are the beginning anchor
 and the end anchor, which represent the start and the end of the string.
'''

'''
Anchor      Pattern         Explanation

Beginning   ^abc            Matches abc only at the start of the string

End         abc$            Matches abc only at the end of the string
'''

'''
Note that the ^ character is used both as a beginning anchor and to indicate a negative set,
 depending on whether the character preceding it is a [ or not.

Let's start with a few test cases that all contain the substring Red at different parts of the string,
 as well as a test function:

test_cases = pd.Series([
    "Red Nose Day is a well-known fundraising event",
    "My favorite color is Red",
    "My Red Car was purchased three years ago"
])
print(test_cases)


If we want to match the word Red only if it occurs at the start of the string,
 we add the beginning anchor to the start of our regular expression:

test_cases.str.contains(r"^Red")

If we want to match the word Red only if it occurs at the end of the string, we add the end anchor to the end of our regular expression:

test_cases.str.contains(r"Red$")
'''

beginning_count = titles.str.contains(r'^\[\w+\]').sum()
# ^ is a starting anchor
# ie, the [word] type word comes at the beginning of each row

print(beginning_count)

ending_count = titles.str.contains(r'\[\w+\]$').sum()
# $ ending anchor
# ie. the [word] comes at the end


# Challenge: Using Flags to Modify Regex Patterns

'''
Up until now, we've been using sets like [Pp] to match different capitalizations in our regular expressions. 
This strategy works well when there is only one character that has capitalization, but becomes cumbersome 
when we need to cater for multiple instances.

Within the titles, there are many different formatting styles used to represent the word "email."
 Here is a list of the variations:

email
Email
e Mail
e mail
E-mail
e-mail
eMail
E-Mail
EMAIL
emails
Emails
E-Mails

To write a regular expression for this, we would need to use a set for all five letters in email, 
which would make our regular expression very hard to read.

Instead, we can use flags to specify that our regular expression should ignore case.

Both re.search() and the pandas regular expression methods accept an optional flags argument. 
This argument accepts one or more flags, which are special variables in the re module that 
modify the behavior of the regex interpreter.

A list of all available flags is in the documentation, but by far the most common and the most
 useful is the re.IGNORECASE flag, which is also available using the alias re.I for convenience.

When you use this flag, all uppercase letters will match their lowercase equivalents and 
vice versa. Let's look at an example without using the flag:

email_tests = pd.Series(['email', 'Email', 'eMail', 'EMAIL'])
email_tests.str.contains(r"email")


0     True
1    False
2    False
3    False
dtype: bool


Now let's look at what happens when we use the flag:

import re
email_tests.str.contains(r"email",flags=re.I)


0    True
1    True
2    True
3    True
dtype: bool


No matter what the capitalization is, our regular expression matches.

We'll finish this lesson by writing a regular expression and count the number of times that 
email is mentioned in story titles. You'll need to use both ignorecase as well as some of the 
other regex components you've already learned in this lesson.

This screen is a challenge screen, so it's a little less guided than the exercises so far.
 As we mentioned at the start of this lesson, regular expressions can be very complex, and
 unless you write them frequently, it's unlikely that you will remember all the syntax.

With that in mind, we don't expect that you will immediately remember how to perform this 
task so don't get disheartened if this exercise takes you more attempts than the other exercises 
in this lesson. If you get stuck, you might try one or more of the following:

Scanning over the regex concepts we've taught in the previous lessons.
Using the test cases that we'll provide.
Using a web tool like RegExr that lets you write a regex iteratively and see how it matches the test cases.
We've also provided a number of hints, however we strongly recommend trying to complete the challenge
 without them first. The skills you build as you try to solve the puzzle will be extremely valuable 
 for you as you continue on your journey to becoming a data expert!

To help you test the regular expression that you build, we have provided a variable that includes 
each of the different ways "email" is included in the data.
'''

# flags
# https://docs.python.org/3/library/re.html#re.I

email_tests = pd.Series(['email', 'Email', 'e Mail', 'e mail', 'E-mail',
              'e-mail', 'eMail', 'E-Mail', 'EMAIL', 'emails', 'Emails',
              'E-Mails'])


'''
Instructions
Write a regular expression that will match all variations of email included in the starter code. Write your regular expression in a way that will be compatible with the ignorecase flag, and should not match the word "emailing" or any other words that contain "email" as a substring.
As you build your regular expression, you might like to use Series.str.contains() like we did in the examples earlier in this screen.
Once your regular expression matches all the test cases, use it to count the number of mentions of email in titles in the dataset. Assign the result to email_mentions.
'''
# pattern = r'\be[- ]{0,1}mail[s]?\b'
# \b creates word boundary,
# [- ] ie, search for '-' or ' ' space characters that either repeats 0 or 1 times
# ? is a quantifier that matches 0 or 1 of the preceding character that is equal to {0,1}
# or
pattern = r'\be[- ]?mail[s]?\b'
# we can also write as
# pattern = r'\be-? ?mails?\b'


email_mentions = titles.str.contains(pattern, flags=re.I).sum() 
# flags = re.I or re.IGNORECASE to ignore cases

