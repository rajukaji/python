# Data Cleaning Walkthrough: Analyzing and Visualizing the Data
import script
import script2

'''
In other lessons, we began investigating possible relationships
 between SAT scores and demographics. In order to do this, 
 we acquired several datasets containing information about 
 New York City public schools. We cleaned them, then combined 
 them into a single dataset named combined that we're now 
 ready to analyze and visualize.

In this lesson, we'll discover correlations, create plots, 
and then make maps. The first thing we'll do is find any 
correlations between columns and sat_score. This helps us
 determine which columns might be interesting to plot out 
 or investigate further. Afterwards, we'll perform more 
 analysis and create maps using the columns we've identified.
'''

# Finding Correlations With the r Value

'''
Correlations tell us how closely related two columns are. We'll be using the r 
value, also called Pearson's correlation coefficient, to measure how closely two 
sequences of numbers are correlated.

An r value falls between -1 and 1. The value determines whether two columns are 
positively correlated, not correlated, or negatively correlated. The closer to 1 
the r value is, the stronger the positive correlation between the two columns. 
The closer to -1 the r value is, the stronger the negative correlation (i.e.,
 the more "opposite" the columns are). The closer to 0, the weaker the correlation. 
 To learn more about r values, see the statistics course.

The columns in the following diagram have a strong positive correlation --
 when the value in class_size is high, the corresponding value in sat_score 
 is also high, and vice versa

In general, r values above .25 or below -.25 are enough to qualify a correlation
 as interesting. An r value isn't perfect and doesn't indicate that there's a 
 correlation -- just the possiblity of one. To assess whether a correlation exists,
   we need to look at the data using a scatterplot to see its "shape."

Because we're interested in exploring the fairness of the SAT, a strong positive
 or negative correlation between a demographic factor like race or gender and SAT
   score would be an interesting result meriting investigation. If men tended to 
   score higher on the SAT, for example, that would indicate that the SAT is potentially
     unfair to women and vice-versa.

We can use the pandas pandas.DataFrame.corr() method to find correlations between
columns in a dataframe. The method returns a new dataframe where the index for each 
column and row is the name of a column in the original dataset.

'''

# Finding Correlations With the r Value

correlations = combined.corr(numeric_only=True)
# Filter the correlations to just the column sat_score

correlations = correlations['sat_score']
# Display all of the columns in the correlations dataframe

print(correlations)


#  Plotting Enrollment With the Plot() Accessor

'''
This is the full output of the correlations variable we generated on the last screen:

SAT Critical Reading Avg. Score         0.986820
SAT Math Avg. Score                     0.972643
SAT Writing Avg. Score                  0.987771
sat_score                               1.000000
AP Test Takers                          0.523140
Total Exams Taken                       0.514333
Number of Exams with scores 3 4 or 5    0.463245
Total Cohort                            0.325144
CSD                                     0.042948
NUMBER OF STUDENTS / SEATS FILLED       0.394626
NUMBER OF SECTIONS                      0.362673
AVERAGE CLASS SIZE                      0.381014
SIZE OF SMALLEST CLASS                  0.249949
SIZE OF LARGEST CLASS                   0.314434
SCHOOLWIDE PUPIL-TEACHER RATIO               NaN
schoolyear                                   NaN
fl_percent                                   NaN
frl_percent                            -0.722225
total_enrollment                        0.367857
ell_num                                -0.153778
ell_percent                            -0.398750
sped_num                                0.034933
sped_percent                           -0.448170
asian_num                               0.475445
asian_per                               0.570730
black_num                               0.027979
black_per                              -0.284139
hispanic_num                            0.025744
hispanic_per                           -0.396985
white_num                               0.449559
                                         ...   
rr_p                                    0.047925
N_s                                     0.423463
N_t                                     0.291463
N_p                                     0.421530
saf_p_11                                0.122913
com_p_11                               -0.115073
eng_p_11                                0.020254
aca_p_11                                0.035155
saf_t_11                                0.313810
com_t_11                                0.082419
eng_t_10                                     NaN
aca_t_11                                0.132348
saf_s_11                                0.337639
com_s_11                                0.187370
eng_s_11                                0.213822
aca_s_11                                0.339435
saf_tot_11                              0.318753
com_tot_11                              0.077310
eng_tot_11                              0.100102
aca_tot_11                              0.190966
grade_span_max                               NaN
expgrade_span_max                            NaN
zip                                    -0.063977
total_students                          0.407827
number_programs                         0.117012
priority08                                   NaN
priority09                                   NaN
priority10                                   NaN
lat                                    -0.121029
lon                                    -0.132222
Name: sat_score, dtype: float64

Unsurprisingly, SAT Critical Reading Avg. Score, SAT Math Avg. Score, SAT Writing Avg.
 Score, and sat_score are strongly correlated with sat_score.

We can also make some other observations:

total_enrollment has a strong positive correlation with sat_score. This is surprising 
because we'd expect smaller schools where students receive more attention to have 
higher scores. However, it looks like the opposite is true -- larger schools tend
 to do better on the SAT.
Other columns that are proxies for enrollment correlate similarly. These include 
total_students, N_s, N_p, N_t, AP Test Takers, Total Exams Taken, and NUMBER OF SECTIONS.
Both the percentage of females (female_per) and number of females (female_num) at a
 school correlate positively with SAT score, whereas the percentage of males (male_per) and the number of males (male_num) correlate negatively. This could indicate that women do better on the SAT than men.
Teacher and student ratings of school safety (saf_t_11, and saf_s_11) correlate with 
sat_score.
Student ratings of school academic standards (aca_s_11) correlate with sat_score,
 but this does not hold for ratings from teachers and parents (aca_p_11 and aca_t_11).
There is significant racial inequality in SAT scores (white_per, asian_per, black_per,
 hispanic_per).
The percentage of students eligible for free or reduced school lunch based on household
 income (frl_percent) has a strong negative correlation with SAT scores.
Since enrollment seems to have such a strong correlation, let's make a scatterplot 
of total_enrollment vs sat_score. Each point in the scatterplot represents a high 
school, so we'll be able to see if there are any interesting patterns.

We can plot columns in a dataframe using the pandas.DataFrame.plot() accessor on a
 dataframe. We can also specify a certain plot type. For example, 
 df.plot.scatter(x="A", y="B") creates a scatterplot of columns A and B.

'''

# Plotting Enrollment With the Plot() Accessor

# Let's explore the relationship between total_enrollment and sat_score further. 
# We'll create a scatterplot to visualize the relationship between these two columns.

combined.plot.scatter(x='total_enrollment', y='sat_score')
plt.show()

# Exploring Schools with Low SAT Scores and Enrollment

'''
Judging from the plot we just created, it doesn't appear there's a strong 
correlation between sat_score and total_enrollment. If there was a strong correlation,
 we'd expect all of the points to line up. Instead, there's a large cluster of 
 schools and then a few others going off in three different directions.

However, there's an interesting cluster of points at the bottom left where 
total_enrollment and sat_score are both low. This cluster may be what's making 
the r value so high. It's worth extracting the names of the schools in this 
cluster so we can research them further.

'''

'''
Instructions

Behind the scenes we have imported pandas as pd and loaded the combined dataframe.

Filter the combined dataframe to keep only those rows where total_enrollment is under
 1000 and sat_score is under 1000. Assign the result to low_enrollment.

Display all of the items in the School Name column of low_enrollment.

Use Wikipedia and Google to research the names of the schools. Can you discover
 anything interesting about them?


'''
low_enrollment = combined[(combined['total_enrollment'] < 1000) & (combined['sat_score'] < 1000)]

print(low_enrollment['School Name'])

'''
 Output
91       INTERNATIONAL COMMUNITY HIGH SCHOOL
125                                        0
126          BRONX INTERNATIONAL HIGH SCHOOL
139    KINGSBRIDGE INTERNATIONAL HIGH SCHOOL
141    INTERNATIONAL SCHOOL FOR LIBERAL ARTS
176                                        0
179            HIGH SCHOOL OF WORLD CULTURES
188       BROOKLYN INTERNATIONAL HIGH SCHOOL
225    INTERNATIONAL HIGH SCHOOL AT PROSPECT
237               IT TAKES A VILLAGE ACADEMY
253                MULTICULTURAL HIGH SCHOOL
286    PAN AMERICAN INTERNATIONAL HIGH SCHOO
Name: School Name, dtype: object
'''

# things that are intersting is that these schools are international schools
# multicultural schools, and schools that are for students who are new to the country
# also schools that are for students who are learning english as a second language
# also where immigrated students go to school

# Plotting Language Learning Percentage

'''
Our research on the last screen revealed that most of the high schools with low 
total enrollment and low SAT scores have high percentages of English language learners. 
This indicates that it's actually ell_percent that correlates strongly with sat_score,
 rather than total_enrollment. To explore this relationship further, let's plot out 
 ell_percent vs sat_score.

'''

combined.plot.scatter(x='ell_percent', y='sat_score')
plt.show()


# Calculating District-Level Statistics

'''
One way to make very granular statistics easier to read is to aggregate them. 
In this case, we aggregate by district, which enables us to understand how 
ell_percent varies district-by-district instead of the unintelligibly granular 
school-by-school variation.

In a previous lesson, we used the pandas.DataFrame.groupby() method followed
 by the agg() method on the resulting object to find the mean class size for each 
 unique DBN. The principle is exactly the same, except that here we'd find the mean
   of each column for each unique value in school_dist.

'''

'''
Instructions

Find the average values for each column for each school_dist in combined.

Use the pandas.DataFrame.groupby() method to group combined by school_dist.

Use the agg() methodwith the string 'mean' as an argument to calculate the average 
of each group. This approach leverages pandas' built-in functionality for better
readability and performance.

Assign the result to the variable districts.

Reset the index of districts, making school_dist a column again.

Use the pandas.DataFrame.reset_index() method with the keyword argument inplace=True.

Display the first few rows of districts to verify that everything went okay.

'''

districts = combined.groupby(by='school_dist', axis=0).agg('mean', numeric_only=True)
# print(combined.value_counts)
# split, apply, combine
# https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

# use numeric_only=True to only include numeric columns in the aggregation
# otherwise, the non-numeric columns will be included in the aggregation and
# it will cause an error

districts.reset_index(inplace=True)
# resetting the index to make school_dist a column again

print(districts.head())