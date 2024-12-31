# Data cleaning walkthrough
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

'''
Data Cleaning Walkthrough
1 of 15 · Introduction
Learn
At many points in your career, you'll need to be able to build 
complete, end-to-end data science projects on your own.
 Data science projects usually consist of one of two things:

An exploration and analysis of a set of data. One example might 
involve analyzing donors to political campaigns, creating a plot,
 and then sharing an analysis of the plot with others.
An operational system that generates predictions based on data
 that updates continually. An algorithm that pulls in daily stock 
 ticker data and predicts which stock prices rise and fall would
   be one example.
You'll find the ability to create data science projects useful
 in several different contexts:

Projects help you build a portfolio, which is critical to
 finding a job as a data analyst or scientist.
Working on projects helps you learn new skills and reinforce 
existing concepts.
Most "real-world" data science and analysis work consists of 
developing internal projects.
Projects allow you to investigate interesting phenomena and
 satisfy your curiosity.
Whether you aim to become a data scientist or analyst or you're 
just curious about the world, building projects can be immensely rewarding.

Here's an example of a finished project.

In this lesson, we'll walk through the first part of a complete
 data science project, including how to acquire the raw data. The project focuses on exploring and analyzing a dataset. We'll develop our data cleaning and storytelling skills, which enables us to build complete projects on our own.

We'll focus primarily on data exploration in this lesson. We'll also combine several messy data sets into a single clean one to make analysis easier. Over the next few lessons, we'll work through the rest of our project and perform the actual analysis.

The first step in creating a project is to decide on a topic. You want the topic to be something you're interested in and motivated to explore. It's very obvious when people are making projects just to make them, rather than out of a genuine interest in the topic.

Here are two ways to find a good topic:

Think about what sectors or angles you're really interested in, then find data sets relating to those sectors.
Review several datasets and find one that seems interesting enough to explore.
Whichever approach you take, you can start your search at these sites:

Data.gov - A directory of government data downloads
/r/datasets - A subreddit that has hundreds of interesting datasets
Awesome datasets - A list of datasets hosted on GitHub
rs.io - A great blog post with hundreds of interesting datasets
In real-world data science, you may not find an ideal dataset. You might have to aggregate disparate data sources instead or do a good amount of data cleaning.

For the purposes of this project, we'll be using data about New York City public schools, which can be found here.


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

'''
Finding All of the Relevant Datasets
Learn
Once you've chosen a topic, you'll want to pick an angle to
 investigate. It's important to choose an angle that has 
 enough depth to analyze but isn't so complicated that it's 
 difficult to get started. You want to finish the project 
 and your results to be interesting to others.

One of the most controversial issues in the U.S. educational 
system is the efficacy of standardized tests and whether they're 
unfair to certain groups. Given our prior knowledge of this
 topic, investigating the correlations between SAT scores 
 and demographics might be an interesting angle to take.
   We could correlate SAT scores with factors like race, 
   gender, income, and more.

The SAT, or Scholastic Aptitude Test, is an exam that U.S.
 high school students take before applying to college. Colleges 
 take the test scores into account when deciding who to admit,
   so it's important to perform well.

The test consists of three sections, each of which has 800
 possible points. The combined score is out of 2,400 possible 
 points (while this number has changed a few times, the dataset
   for our project is based on 2,400 total points). 
   Organizations often rank high schools by their average 
   SAT scores. The scores are also considered a measure of 
   overall school district quality.

New York City makes its data on high school SAT scores 
available online, as well as the demographics for each high 
school. The first few rows of the SAT data look like this:

SAT

Unfortunately, combining both of the datasets won't
 give us all of the demographic information we want to use. 
 We'll need to supplement our data with other sources to 
 do our full analysis.

The same website has several related datasets covering 
demographic information and test scores. Here are the links 
to all of the datasets we'll be using:

SAT scores by school - SAT scores for each high school in 
New York City
School attendance - Attendance information for each school
 in New York City
Class size - Information on class size for each school
AP test results - Advanced Placement (AP) exam results for 
each high school (passing an optional AP exam in a particular
 subject can earn a student college credit in that subject)
Graduation outcomes - The percentage of students who graduated,
 and other outcome information
Demographics - Demographic information for each school
School survey - Surveys of parents, teachers, and students
 at each school
All of these datasets are interrelated. We'll need to combine 
them into a single dataset before we can find correlations.
'''

'''
Finding Background Information

Before we move into coding, we'll need to do some background 
research. A thorough understanding of the data helps us avoid 
costly mistakes, such as thinking that a column represents 
something other than what it does. Background research gives us a better 
understanding of how to combine and analyze the data.

In this case, we'll want to research:

New York City
The SAT
Schools in New York City
Our data
We can learn a few different things from these resources. For example:

Only high school students take the SAT, so we'll want to focus on high schools.
New York City is made up of five boroughs, which are essentially distinct regions.
New York City schools fall within several different school districts, each of which
 can contain dozens of schools.
Our datasets include several different types of schools. We'll need to clean them so
 that we can focus on high schools only.
Each school in New York City has a unique code called a DBN or district borough number.
Aggregating data by district allows us to use the district mapping data to plot
 district-by-district differences.

'''

'''
Once we've done our background research, we're ready to read in the data.
 For your convenience, we've placed all the data into the schools folder.
   Here are all of the files in the folder:

ap_2010.csv - Data on AP test results
class_size.csv - Data on class size
demographics.csv - Data on demographics
graduation.csv - Data on graduation outcomes
hs_directory.csv - A directory of high schools
sat_results.csv - Data on SAT scores
survey_all.txt - Data on surveys from all schools
survey_d75.txt - Data on surveys from New York City district 75
survey_all.txt and survey_d75.txt are in more complicated formats than the other files.
 For now, we'll focus on reading in the CSV files only, and then explore them.
'''

data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

for file in data_files:
    key = file[:-4]
    data[key] = pd.read_csv("schools/" + file)
#     in schools folder
    

print(data)

'''
Exploring the SAT Data

What we're mainly interested in is the SAT dataset, which corresponds to the
 dictionary key sat_results. This dataset contains the SAT scores for each high 
 school in New York City. We eventually want to correlate selected information 
 from this dataset with information in the other datasets.

Let's explore sat_results to see what we can discover. Exploring the dataframe
 helps us understand the structure of the data and make it easier for us to analyze it.
'''

print(pd.DataFrame(data['sat_results']).head())
# converting to dataframe to see the first 5 rows


# exploring the remaining data

'''
We can make a few observations based on this output:

The DBN appears to be a unique ID for each school.
We can tell from the first few rows of names that we only have data about high schools.
There's only a single row for each high school, so each DBN is unique in the SAT data.
We may eventually want to combine the three columns that contain SAT scores --
 SAT Critical Reading Avg. Score, SAT Math Avg. Score, and SAT Writing Avg. Score --
   into a single column to make the scores easier to analyze.
Given these observations, let's explore the other datasets to see if we can gain any 
insight into how to combine them.
'''

for key in data:
    print(data[key][:5])
#    printing the first 5 rows of each dataset by looping through the dictionary keys

# Reading in the Survey Data

'''
In the last step, we saw a group of dataframes that looked like this:

CSD BOROUGH SCHOOL CODE                SCHOOL NAME GRADE  PROGRAM TYPE  \
0    1       M        M015  P.S. 015 Roberto Clemente     0K       GEN ED
1    1       M        M015  P.S. 015 Roberto Clemente     0K          CTT
2    1       M        M015  P.S. 015 Roberto Clemente     01       GEN ED
3    1       M        M015  P.S. 015 Roberto Clemente     01          CTT
4    1       M        M015  P.S. 015 Roberto Clemente     02       GEN ED

We can make some observations based on the first few rows of each one.

Each dataset appears to either have a DBN column or the information we need to create one. 
That means we can use a DBN column to combine the datasets. First we'll pinpoint matching rows 
from different datasets by looking for identical DBNs, then group all of their columns 
together in a single dataset.
Some fields look interesting for mapping -- particularly Location 1, which contains 
coordinates inside a larger string.
Some of the datasets appear to contain multiple rows for each school (because the
 rows have duplicate DBN values). That means we’ll have to do some preprocessing 
 to ensure that each DBN is unique within each dataset. If we don't do this, we'll
   run into problems when we combine the datasets, because we might be merging two
     rows in one data set with one row in another dataset.
Before we proceed with the merge, we should make sure we have all of the data we
 want to unify. We mentioned the survey data earlier (survey_all.txt and survey_d75.txt),
   but we didn't read those files in because they're in a slightly more complex format.

Each survey text file looks like this:

dbn bn  schoolname  d75 studentssurveyed    highschool  schooltype  rr_s
"01M015"    "M015"  "P.S. 015 Roberto Clemente" 0   "No"    0   "Elementary School"     88

The files are tab delimited and encoded with Windows-1252 encoding. An encoding defines how a computer stores
 the contents of a file in binary. The most common encodings are UTF-8 and ASCII. Windows-1252 is rarely
   used and can cause errors if we read such a file in without specifying the encoding. If you'd like 
   to read more about encodings, here's a good primer.

We'll need to specify the encoding and delimiter to the pandas pandas.read_csv() function to ensure it reads the
 surveys in properly.

After we read in the survey data, we'll want to combine it into a single dataframe. We can do this by calling the 
pandas.concat() function:

z = pd.concat([x,y], axis=0)

The code above combines dataframes x and y by essentially appending y to the end of x. The combined dataframe z
 has the number of rows in x plus the number of rows in y.
'''

'''
Reading in the Survey Data

Now, let's read in the survey data.

Instructions


We have imported pandas as pd and, behind the scenes, loaded the data files into a dictionary named data. 
These are available for your use.

Read in survey_all.txt.
Use the pandas.read_csv() function to read survey_all.txt into the variable all_survey. Recall that
 this file is located in the schools folder.

Specify the keyword argument delimiter="\t".

Specify the keyword argument encoding="windows-1252".

Read in survey_d75.txt.

Use the pandas.read_csv() function to read schools/survey_d75.txt into the variable d75_survey. 

Recall that this file is located in the schools folder.

Specify the keyword argument delimiter="\t".

Specify the keyword argument encoding="windows-1252".

Combine d75_survey and all_survey into a single dataframe.

Use the pandas concat() function with the keyword argument axis=0 to combine d75_survey
 and all_survey into the dataframe survey.

Pass in all_survey first, then d75_survey when calling the pandas.concat() function.

Display the first five rows of survey using the pandas.DataFrame.head() function.
'''

all_survey = pd.read_csv('schools/survey_all.txt', delimiter='\t', encoding='windows-1252')


d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter='\t', encoding='windows-1252')

# combining the data frames

survey = pd.concat([all_survey, d75_survey], axis=0, join='outer')

print(survey.head())


# Cleaning Up the Surveys

'''
In the last step, the expected output was:

dbn    bn                      schoolname  d75 studentssurveyed  \
0  01M015  M015       P.S. 015 Roberto Clemente    0               No   
1  01M019  M019             P.S. 019 Asher Levy    0               No   
2  01M020  M020            P.S. 020 Anna Silver    0               No   
3  01M034  M034  P.S. 034 Franklin D. Roosevelt    0              Yes   
4  01M063  M063       P.S. 063 William McKinley    0               No   

   highschool                  schooltype  rr_s  rr_t  rr_p  ...  s_q14_2  \
0         0.0           Elementary School   NaN    88    60  ...      NaN   
1         0.0           Elementary School   NaN   100    60  ...      NaN   
2         0.0           Elementary School   NaN    88    73  ...      NaN   
3         0.0  Elementary / Middle School  89.0    73    50  ...      NaN   
4         0.0           Elementary School   NaN   100    60  ...      NaN   

   s_q14_3  s_q14_4  s_q14_5  s_q14_6  s_q14_7  s_q14_8  s_q14_9  s_q14_10  \
0      NaN      NaN      NaN      NaN      NaN      NaN      NaN       NaN   
1      NaN      NaN      NaN      NaN      NaN      NaN      NaN       NaN   
2      NaN      NaN      NaN      NaN      NaN      NaN      NaN       NaN   
3      NaN      NaN      NaN      NaN      NaN      NaN      NaN       NaN   
4      NaN      NaN      NaN      NaN      NaN      NaN      NaN       NaN   

   s_q14_11  
0       NaN  
1       NaN  
2       NaN  
3       NaN  
4       NaN  

[5 rows x 2773 columns]

There are two immediate facts that we can see in the data:

There are over 2000 columns, nearly all of which we don't need. We'll have to filter
 the data to remove the unnecessary ones. Working with fewer columns makes it easier
   to print the dataframe out and find correlations within it.
The survey data has a dbn column that we'll want to convert to uppercase (DBN).
 The conversion makes the column name consistent with the other data sets.
First, we'll need to filter the columns to remove the ones we don't need. Luckily, 
there's a data dictionary at the original data download location. The dictionary 
tells us what each column represents. Based on our knowledge of the problem and the
 analysis we're trying to do, we can use the data dictionary to determine which columns to use.

Here's a preview of the data dictionary:


Based on the dictionary, it looks like these are the relevant columns:

["dbn", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11",
 "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11",
   "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]

These columns give us aggregate survey data about how parents, teachers, and students 
feel about school safety, academic performance, and more. It also gives us the DBN, 
which allows us to uniquely identify the school.

Before we filter columns out, we'll want to copy the data from the dbn column into a 
new column called DBN. We can copy columns like this:

survey["new_column"] = survey["old_column"]

Additionally, it's important to use the .copy() method when working with pandas DataFrames. 
This ensures that we are working with a separate copy of the data, so any changes
 we make don't accidentally affect the original data.
'''

survey = survey.copy()
# working with copy of survey data

survey['DBN'] = survey['dbn'].copy()
# copying the dbn column to new column DBN

# print(survey)
# survey = survey.rename(columns={'dbn':'DBN'})

survey = survey.loc[:, ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]]
# filtering the columns, keeping only the relevant ones
# all the rows, and the columns mentioned above
    
data['survey'] = survey
# adding the survey data to the data dictionary

print(data['survey'].shape)


# Inserting DBN Fields

'''
When we explored all of the datasets, we noticed that some of them, like class_size 
and hs_directory, don't have a DBN column. hs_directory does have a dbn column,
though, so we can just rename it.

However, class_size doesn't appear to have the column at all. Here are the first few rows of the data set:

CSD BOROUGH SCHOOL CODE                SCHOOL NAME GRADE  PROGRAM TYPE  \
0    1       M        M015  P.S. 015 Roberto Clemente     0K       GEN ED
1    1       M        M015  P.S. 015 Roberto Clemente     0K          CTT
2    1       M        M015  P.S. 015 Roberto Clemente     01       GEN ED
3    1       M        M015  P.S. 015 Roberto Clemente     01          CTT
4    1       M        M015  P.S. 015 Roberto Clemente     02       GEN ED

Explain

Copy
Here are the first few rows of the sat_results data, which does have a DBN column:

DBN                                    SCHOOL NAME  \
0  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448            UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                     EAST SIDE COMMUNITY SCHOOL
3  01M458                      FORSYTH SATELLITE ACADEMY
4  01M509                        MARTA VALLE HIGH SCHOOL

From looking at these rows, we can tell that the DBN in the sat_results data
is just a combination of the CSD and SCHOOL CODE columns in the class_size data.
The main difference is that the DBN is padded, so that the CSD portion of 
it always consists of two digits. That means we'll need to add a leading 0
to the CSD if the CSD is less than two digits long. 


As you can see, whenever the CSD is less than two digits long, 
we need to add a leading 0. We can accomplish this using the pandas.Series.apply() 
method, along with a custom function that:

Takes in a number.
Converts the number to a string using the str() function.
Check the length of the string using the len() function.
If the string is two digits long, returns the string.
If the string is one digit long, adds a 0 to the front of the string, then returns it.
You can use the string method zfill() to do this.
Once we've padded the CSD, we can use the addition operator (+) to combine the 
values in the CSD and SCHOOL CODE columns. Here's an example of how we would do this:

dataframe["new_column"] = dataframe["column_one"] + dataframe["column_two"]
'''

# Inserting DBN Fields

hs_directory = data['hs_directory']
# copying the hs_directory data to a new variable

hs_directory['DBN'] = hs_directory['dbn']
# new column DBN with the values of dbn

class_size = data['class_size']
# copying the class_size data to a new variable

def csdApply(val):
    # function to pad the CSD values, to make 1 01, 2 02 etc
    if len(val) == 1:
        return '0'+ val
    
    return val
    
    
    
class_size['padded_csd'] = class_size['CSD'].astype(str).apply(csdApply)
# first converting the CSD column to string, then applying the function to pad the values
# and storing the result in a new column padded_csd

class_size['DBN'] = class_size['padded_csd'] + class_size['SCHOOL CODE']
# combining the padded_csd and SCHOOL CODE columns to create a new column DBN
# this makes DBN that we need

data['hs_directory'] = hs_directory
data['class_size'] = class_size
# assigning the new data to the dictionary with the corresponding keys

print(data['class_size'].head())
# printing the first 5 rows of the class_size data to see the changes

# Combining the SAT Scores

'''
Now we're almost ready to combine our datasets. 
Before we do, let's take some time to calculate 
variables that are useful in our analysis. We've already
 discussed one such variable -- a column that totals up the
   SAT scores for the different sections of the exam. 
   This makes it much easier to correlate scores with 
   demographic factors because we'll be working with a
     single number, rather than three different ones.

Before we can generate this column,
 we'll need to convert the SAT Math Avg.
 Score, SAT Critical Reading Avg. Score, and SAT Writing Avg. 
 Score columns in the sat_results dataset from the object
   (string) data type to a numeric data type. We can use
     the pandas.to_numeric() method for the conversion.
       If we don't convert the values, we won't be able
         to add the columns together.

It's important to pass the keyword argument errors="coerce"
 when we call pandas.to_numeric(), so that pandas treats any
   invalid strings it can't convert to numbers as missing
     values instead.

After we perform the conversion, we can use the addition
 operator (+) to add all three columns together.
'''


sat_results = data['sat_results'].copy()
# copying the sat_results data to a new variable

math = sat_results['SAT Math Avg. Score'] = pd.to_numeric(sat_results['SAT Math Avg. Score'], errors='coerce')
# converting the SAT Math Avg. Score column to numeric, and storing the result in the same column

critical = sat_results['SAT Critical Reading Avg. Score'] = pd.to_numeric(sat_results['SAT Critical Reading Avg. Score'], errors='coerce')
# converting the SAT Critical Reading Avg. Score column to numeric, and storing the result in the same column

writing = sat_results['SAT Writing Avg. Score'] = pd.to_numeric(sat_results['SAT Writing Avg. Score'], errors='coerce')
# converting the SAT Writing Avg. Score column to numeric, and storing the result in the same column

sat_results['sat_score'] = math+critical+writing
# sum of all the average sat scores

data['sat_results'] = sat_results
# assigning the changed data back to the data dictionary for sat_results key

print(data['sat_results']['sat_score'].head())
# printing the first 5 rows of the sat_score column to see the changes



# Parsing Geographic Coordinates for Schools

'''
Next, we'll want to parse the latitude and
 longitude coordinates for each school. This enables us to 
 map the schools and uncover any geographic patterns in the data.
   The coordinates are currently in the text field Location 
   1 in the hs_directory dataset.

We can do the extraction with a regular expression.
 The following expression pulls out everything inside 
 the parentheses:

import re
re.findall("\(.+\)", "1110 Boston Road\nBronx, NY
 10456\n(40.8276026690005, -73.90447525699966)")

Explain

Copy
This command returns [(40.8276026690005, -73.90447525699966)]. 
We'll need to process this result further using 
the string methods split() and replace() methods 
to extract each coordinate.
'''

def getLatitude(string):
    # function to extract the coordinates from the string
    return re.findall('\((.+),', string)
# findall returns a list of all the matches, we need the first match only
# we can also use the split and replace method to extract
#     returns the latitude only


hs_directory = data['hs_directory'].copy()
# copying the hs_directory data to a new variable

hs_directory['lat'] = hs_directory['Location 1'].apply(getLatitude)
# applying the function to extract the latitude from the Location 1 column

# print(hs_directory['lat'])

data['hs_directory'] = hs_directory
# assigning the changed data back to the data dictionary for hs_directory key

print(data['hs_directory'].head())
# printing the first 5 rows of the hs_directory data to see the changes

#  Extracting the Longitude

'''
On the last screen, we parsed the latitude from the Location 1 
column. Now we'll just need to do the same for the longitude.

Once we have both coordinates, we'll need to convert them to 
numeric values. We can use the pandas.to_numeric() function 
to convert them from strings to numbers.
'''

def getLongitude(string):
    return re.findall(',(.+)\)', string)
# return the longitude only


data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(getLongitude)
# applying the function to extract the longitude from the Location 1 column

data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors='coerce')
# converting the latitude column to numeric

data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors='coerce')
# converting the longitude column to numeric

print(data['hs_directory'].head())
#  printing the first 5 rows of the hs_directory data to see the changes

