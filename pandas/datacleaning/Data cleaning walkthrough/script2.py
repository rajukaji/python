# Data Cleaning Walkthrough: Combining the Data

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

