# Data Cleaning Walkthrough: Combining the Data
import script

'''
In a previous lesson, we began investigating possible relationships 
between SAT scores and demographic factors. In order to do this,
 we acquired several datasets about New York City public schools. We 
 manipulated these datasets and found that we could combine them using the 
 DBN column. All of the datasets are currently stored as keys in the data dictionary. 
 Each dataset is a pandas dataframe.

In this lesson, we'll clean the data more, then combine it. 
Finally, we'll compute correlations and perform some analysis.

The first thing we'll need to do in preparation for the merge
 is condense some of the datasets. In the last lesson, we
   noticed that the values in the DBN column were unique 
   in the sat_results data set. Other data sets like 
   class_size had duplicate DBN values.

We'll need to condense these datasets so that each value 
in the DBN column is unique. If not, we'll run into issues 
when it comes time to combine the datasets.

While the main dataset we want to analyze, sat_results,
 has unique DBN values for every high school in New York City, 
 other datasets aren't as clean. A single row in the sat_results 
 dataset may match multiple rows in the class_size dataset,
   for example. This situation creates problems, because 
   we don't know which of the multiple entries in the 
   class_size dataset we should combine with the single 
   matching entry in sat_results. 


In the diagram above, we can't combine the rows from both datasets,
 because there are several cases where multiple rows in class_size 
 match a single row in sat_results.

To resolve this issue, we'll condense the class_size, graduation 
and demographics datasets so that each DBN is unique
'''

'''
The first dataset that we'll condense is class_size. The first few rows 
of class_size look like this:

CSD	BOROUGH	SCHOOL CODE	SCHOOL NAME	GRADE	PROGRAM TYPE	CORE SUBJECT (MS CORE and 9-12 ONLY)	CORE COURSE (MS CORE and 9-12 ONLY)	SERVICE CATEGORY(K-9* ONLY)	NUMBER OF STUDENTS / SEATS FILLED	NUMBER OF SECTIONS	AVERAGE CLASS SIZE	SIZE OF SMALLEST CLASS	SIZE OF LARGEST CLASS	DATA SOURCE	SCHOOLWIDE PUPIL-TEACHER RATIO	padded_csd	DBN
0	1	M	M015	P.S. 015 Roberto Clemente	0K	GEN ED	-	-	-	19.0	1.0	19.0	19.0	19.0	ATS	NaN	01	01M015
1	1	M	M015	P.S. 015 Roberto Clemente	0K	CTT	-	-	-	21.0	1.0	21.0	21.0	21.0	ATS	NaN	01	01M015
2	1	M	M015	P.S. 015 Roberto Clemente	01	GEN ED	-	-	-	17.0	1.0	17.0	17.0	17.0	ATS	NaN	01	01M015
3	1	M	M015	P.S. 015 Roberto Clemente	01	CTT	-	-	-	17.0	1.0	17.0	17.0	17.0	ATS	NaN	01	01M015
4	1	M	M015	P.S. 015 Roberto Clemente	02	GEN ED	-	-	-	15.0	1.0	15.0	15.0	15.0	ATS	NaN	01	01M015
As you can see, the first few rows all pertain to the same school, which is why the DBN appears more than once. It looks like each school has multiple values for GRADE, PROGRAM TYPE, CORE SUBJECT (MS CORE and 9-12 ONLY), and CORE COURSE (MS CORE and 9-12 ONLY).

If we look at the unique values for GRADE, we get the following:

array(['0K', '01', '02', '03', '04', '05', '0K-09', nan, '06', '07', '08',
       'MS Core', '09-12', '09'], dtype=object)

Since we're dealing with high schools, we're only concerned with grades 9 
through 12. That means we only want to pick rows where the value in the
 GRADE column is 09-12.

If we look at the unique values for PROGRAM TYPE, we get the following:

array(['GEN ED', 'CTT', 'SPEC ED', nan, 'G&T'], dtype=object)

Each school can have multiple program types. Since GEN ED is the largest category by far,
 let's only select rows where PROGRAM TYPE is GEN ED.
'''


# Condensing the Class Size Dataset 2

# Let's condense the class size dataset.

class_size = data['class_size']
# data is a dictionary that contains the dataframes
# data is in script.py

class_size = class_size[class_size['GRADE '] == '09-12']
# filterning the data to only include grades 9-12

class_size = class_size[class_size['PROGRAM TYPE'] == 'GEN ED']
# filtering the data to only include general education

print(class_size.head())


# Computing Average Class Sizes 1

'''
As we saw when we displayed class_size on the last screen, DBN still isn't completely
 unique. This is due to the CORE COURSE (MS CORE and 9-12 ONLY) and CORE SUBJECT
   (MS CORE and 9-12 ONLY) columns.

CORE COURSE (MS CORE and 9-12 ONLY) and CORE SUBJECT (MS CORE and 9-12 ONLY)
 seem to pertain to different kinds of classes. For example, here are the unique 
 values for CORE SUBJECT (MS CORE and 9-12 ONLY):

array(['ENGLISH', 'MATH', 'SCIENCE', 'SOCIAL STUDIES'], dtype=object)

This column only seems to include certain subjects. We want our class size data to
 include every single class a school offers -- not just a subset of them. What we
   can do is take the average across all of the classes a school offers. This gives
     us unique DBN values, while also incorporating as much data as possible into
       the average.

Fortunately, we can use the pandas.DataFrame.groupby() method to help us with this. 
The DataFrame.groupby() method splits a dataframe up into unique groups, based on 
a given column. We can then use the agg() method on the resulting pandas.core.groupby 
object to find the mean of each column.

Using the groupby() method, we'll split this dataframe into four separate groups --
 one with the DBN 01M292, one with the DBN 01M332, one with the DBN 01M378, and 
 one with the DBN 01M448:

Then, we can compute the averages for the AVERAGE CLASS SIZE column in each of the 
four groups using the agg() method:

After we group a dataframe and aggregate data based on it, the column we
 performed the grouping on (in this case DBN) becomes the index and no longer 
 appears as a column in the data itself. To undo this change and keep DBN as a 
 column, we'll need to use pandas.DataFrame.reset_index(). This method resets the
   index to a list of integers and make DBN a column again.

'''

# Computing Average Class Sizes 2

'''
Instructions

Find the average values for each column associated with each DBN in class_size.

Use the pandas.DataFrame.groupby() method to group class_size by DBN.

Use the agg() method on the resulting pandas.core.groupby object, along with the 'mean' 
function as an argument and set numeric_only=True to calculate the average of each 
numeric column in each group.

Assign the result back to class_size.

Reset the index to make DBN a column again.

Use the pandas.DataFrame.reset_index() method, along with the keyword argument inplace=True.
Assign class_size back to the class_size key of the data dictionary.

Display the first few rows of data["class_size"] to verify that everything went okay.
'''


class_size = class_size.groupby(by='DBN').agg('mean', numeric_only=True)
    
# The aggregate() method
# in short agg()
# DBN is acting as an index/label for the dataframe, we will remove this

class_size.reset_index(inplace=True)
# dont need to assign if inplace is used for True value
# if you are using inplace=False, assign the value back to the df

data['class_size'] = class_size

print(data['class_size'].head())


# Condensing the Demographics Dataset 1

# Now that we've finished condensing class_size, let's condense demographics. 

# In this case, the only column that prevents a given DBN from being unique is schoolyear.
#  We only want to select rows where schoolyear is 20112012. This will give us the 
# most recent year of data, and also match our SAT results data.

# Condensing the Demographics Dataset 2


data['demographics'] = data['demographics'][data['demographics']['schoolyear'] == 20112012]
# filtering the data to only include the year 20112012 which is integer values

print(data['demographics'].head())


# Condensing the Graduation Dataset 1

# Finally, we'll need to condense the graduation dataset. 

'''
The Demographic and Cohort columns are what prevent DBN from being unique
 in the graduation data. A Cohort appears to refer to the year the data represents, 
 and the Demographic appears to refer to a specific demographic group. In this case, 
 we want to pick data from the most recent Cohort available, which is 2006. 
 We also want data from the full cohort, so we'll only pick rows where Demographic
   is Total Cohort.

'''

# Condensing the Graduation Dataset 2

'''
Instructions

    Filter graduation, only select rows where the Cohort column equals 2006.

    Filter graduation, only select rows where the Demographic column equals Total Cohort.

    Display the first few rows of data["graduation"] to verify that everything worked properly.
'''

data['graduation'] = data['graduation'][data['graduation']['Cohort'] == '2006']
# filtering the data to only include the Cohort 2006 which is integer values

data['graduation'] = data['graduation'][data['graduation']['Demographic'] == 'Total Cohort']
# filtering the data to only include the Demographic Total Cohort

print(data['graduation'].head())


# Converting AP Test Scores

'''
We're almost ready to combine all of the datasets. The last thing to do is convert
 the Advanced Placement (AP) test scores from strings to numeric values. High school 
 students take the AP exams before applying to college. There are several AP exams,
   each corresponding to a school subject. High school students who earn high scores
     may receive college credit.

AP exams have a 1 to 5 scale; 3 or higher is a passing score. Many high school
 students take AP exams -- particularly those who attend academically challenging
 institutions. AP exams are rarer in schools that lack funding or academic rigor.

It will be interesting to find out whether AP exam scores are correlated with SAT
scores across high schools. To determine this, we'll need to convert the AP exam scores 
in the ap_2010 data set to numeric values first.

There are three columns we'll need to convert:

AP Test Takers (note that there's a trailing space in the column name)
Total Exams Taken
Number of Exams with scores 3 4 or 5
'''


cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
# columns to convert to numeric

data['ap_2010'][cols] = data['ap_2010'][cols].apply(pd.to_numeric, errors='coerce')
# converting the columns to numeric values
# errors='coerce' will convert the non-numeric values to NaN
# pd.to_numeric() is a function that converts the values to numeric
# apply() is a method that applies the function to the columns

'''
for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col], errors="coerce")

# you can also do this way
'''

print(data['ap_2010'][cols].dtypes)



# Left, Right, Inner, and Outer Joins

'''
Before we merge our data, we'll need to decide on the merge strategy we want
 to use. We'll be using the pandas pandas.DataFrame.merge() function,
   which supports four types of joins -- left, right, inner, and outer.
     Each of these join types dictates how pandas combines the rows.

We'll be using the DBN column to identify matching rows across datasets.
 In other words, the values in that column help us know which row from the
   first dataset to combine with which row in the second dataset.

There may be DBN values that exist in one dataset but not in another. 
This is partly because the data is from different years. Each data set 
also has inconsistencies in terms of how it was gathered. Human error
 (and other types of errors) may also play a role. Therefore, we may not 
 find matches for the DBN values in sat_results in all of the other datasets 
 and other datasets may have DBN values that don't exist in sat_results.

We'll merge two datasets at a time. For example, we'll merge sat_results and
 hs_directory, then merge the result with ap_2010, then merge the result of that 
 with class_size. We'll continue combining datasets in this way until we've merged
   all of them. Afterwards, we'll have roughly the same number of rows, but
     each row has columns from all of the datasets.

     With an inner merge, we'd only combine rows where the same DBN exists in both
       datasets. 
     With a left merge, we'd only use DBN values from the dataframe on the "left"
       of the merge. In this case, sat_results is on the left. Some of the DBNs
         in sat_results don't exist in class_size, though. The merge handles this 
         by assiging null values to the columns in sat_results that don't have
           corresponding data in class_size.

With a right merge, we'll only use DBN values from the dataframe on the
 "right" of the merge. In this case, class_size is on the right:

 With an outer merge, we'll take any DBN values from either sat_results 
 or class_size:

As you can see, each merge strategy has its advantages. Depending on the 
strategy we choose, we may preserve rows at the expense of having more missing
 column data or minimize missing data at the expense of having fewer rows.
   Choosing a merge strategy is an important decision; it's worth thinking
     about your data carefully and what trade-offs you're willing to make.

Since this project is concerned with determining demographic factors that 
correlate with SAT score, we'll want to preserve as many rows as possible
 from sat_results while minimizing null values.

This means that we may need to use different merge strategies with different
 datasets. Some of the datasets have a lot of missing DBN values. This makes
   a left join more appropriate, because we don't want to lose too many rows
     when we merge. If we did an inner join, we would lose the data for many
       high schools.

Some datasets have DBN values that are almost identical to those in sat_results.
 Those datasets also have information we need to keep. Most of our analysis 
 would be impossible if a significant number of rows was missing from demographics,
   for example. Therefore, we'll do an inner join to avoid missing data in these columns.

'''

# Performing the Left Joins

'''
Both the ap_2010 and the graduation datasets have many missing DBN values,
 so we'll use a left join when we merge the sat_results data set with them.
   Since we're using a left join, our final dataframe will have all of the same 
   DBN values as the original sat_results dataframe.

   We'll need to use the pandas df.merge() method to merge dataframes.
     The "left" dataframe is the one we call the method on, and the "right" 
     dataframe is the one we pass into df.merge().

     Because we're using the DBN column to join the dataframes, 
     we'll need to specify the keyword argument on="DBN" when calling 
     pandas.DataFrame.merge().

First, we'll assign data["sat_results"] to the variable combined. Then,
 we'll merge the other dataframes with combined. When we're finished, 
 combined has columns from all of the datasets.

'''

combined = data["sat_results"]

ap_merge = data['ap_2010']

combined = combined.merge(right=ap_merge, how='left', on='DBN')

grad_merge = data['graduation']

combined = combined.merge(right=grad_merge, how='left', on='DBN')

print(combined.head())
print(combined.shape)

# Performing the Inner Joins

'''
Now that we've performed the left joins, we still have to merge class_size, 
demographics, survey, and hs_directory into combined. Since these files contain 
information that's more valuable to our analysis and also have fewer missing DBN 
values, we'll use the inner join type.
'''

combined = data['class_size']

class_merge = data['class_size']

combined = combined.merge(right=class_merge, how='inner', on='DBN')

demo_merge = data['demographics']

combined = combined.merge(right=demo_merge, how='inner', on='DBN')

sur_merge = data['survey']

combined = combined.merge(right=sur_merge, how='inner', on='DBN')

hs_merge = data['hs_directory']

combined = combined.merge(right=hs_merge, how='inner', on='DBN')

print(combined.head())
print(combined.shape)

'''
# using a loop

to_merge = ["class_size", "demographics", "survey", "hs_directory"]
combined = data["class_size"]

for m in to_merge:
    combined = combined.merge(data[m], on="DBN", how="inner")
'''

# Filling in Missing Values 1

'''
You may have noticed that the inner joins resulted in 116 fewer rows in
 sat_results. This is because pandas couldn't find the DBN values that existed
   in sat_results in the other datasets. While this is worth investigating, 
   we're currently looking for high-level correlations, so we don't need to dive 
   into which DBNs are missing.

You may also have noticed that we now have many columns with null (NaN) values.
 This is because we chose to do left joins, where some columns may not have had data. 
 The dataset also had some missing values to begin with. If we hadn't performed a 
 left join, all of the rows with missing data would have been lost in the merge
   process, which wouldn't have left us with many high schools in our data set.

There are several ways to handle missing data and we'll cover them in more detail 
later on. For now, we'll just fill in the missing values with the overall mean for
 the column, 

 In the diagram above, the mean of the first column is (1800 + 1600 + 2200 + 2300) / 4,
   or 1975, and the mean of the second column is (20 + 30 + 30 + 50) / 4, or 32.5.
     We replace the missing values with the means of their respective columns,
       which allows us to proceed with analyses that can't handle missing values
         (like correlations).

We can fill in missing data in pandas using the pandas.DataFrame.fillna() method. 
This method replaces any missing values in a dataframe with the values we specify. 
We can compute the mean of every column using the pandas.DataFrame.mean() method.
 If we pass the results of the df.mean() method into the df.fillna() method, pandas 
 fills in the missing values in each column with the mean of that column.

Here's an example of how we would accomplish this:

means = df.mean()
df = df.fillna(means)

In this case, since the means are calculated on numeric columns, there’s no
 need to worry about the data types of non-numeric columns. However, when we 
 fill remaining missing values with 0, we need to ensure that all columns,
   especially object-type columns, are treated properly. If there are columns
     with mixed or object types, filling missing values with 0 could lead to 
     unexpected results or incorrect data types.

To address this, we use the pandas.DataFrame.infer_objects() method. This method 
ensures that object-type columns in combined are converted to their appropriate 
inferred data types before filling the missing values with 0. We also use the 
copy=False parameter to avoid creating an unnecessary copy of the data.

After inferring the correct data types, we fill any remaining NaN or null 
values with 0:

df = df.infer_objects(copy=False).fillna(0)

This step is important because infer_objects() ensures the data types are
 corrected before filling in values like 0, which could otherwise introduce
   type issues in object columns (e.g., trying to fill strings with 0).
     By doing this, we make sure all missing values are filled, and the data
       is ready for further analysis.
'''

# Filling in Missing Values 2

means = combined.mean(numeric_only=True)

combined = combined.fillna(value=means)

combined = combined.infer_objects().fillna(0)
# filling remaining missing values with 0

print(combined.head())

# Adding a School District Column for Mapping

'''
We've finished cleaning and combining our data! We now have a clean dataset we
 can base our analysis. Mapping the statistics out on a school district level 
 might be an interesting way to analyze them. Adding a column to the dataset
   that specifies the school district helps us accomplish this.

The school district is just the first two characters of the DBN. We can apply a
 function over the DBN column of combined that pulls out the first two letters.

For example, we can use indexing to extract the first few characters of a string, 
like this:

name = "Sinbad"
print(name[0:2])
'''

'''
Instructions
Write a function that extracts the first two characters of a string and returns them.

Apply the function to the DBN column of combined and assign the result to the school_dist
 column of combined.

Display the first few items in the school_dist column of combined to verify the results.
'''

def returnChar(string):
    return string[:2]
# function that extracts the first two characters of a string


combined['school_dist'] = combined['DBN'].apply(returnChar)
# applying the function to the DBN column and assigning the result to the school_dist column

print(combined['school_dist'].head())
# displaying the first few items in the school_dist column
# verifying the results