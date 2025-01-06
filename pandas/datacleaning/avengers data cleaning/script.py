# https://fivethirtyeight.com/features/avengers-death-comics-age-of-ultron/

# avengers characters death over the years

# from five thirty eight 

# how data were collected
# https://github.com/fivethirtyeight/data/tree/master/avengers
# from 3 years ago

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re 

avengers = pd.read_csv('avengers.csv')

# print(avengers.head())
print(avengers.columns)

# lets only see death over the years

death = ['Death'+str(i) for i in range(1, 6)]

# print(death)

# cols = ['Name/Alias', 'Appearances', 'Current?', 'Gender',
#        'Probationary Introl', 'Full/Reserve Avengers Intro', 'Year',
#        'Years since joining', 'Notes']

print(avengers[['Name/Alias', 'Year', 'Death1']])

# Filtering Out Bad Data

'''
Because the data came from a crowdsourced community site,
 it could contain errors. If you plot a histogram of the 
 values in the Year column, which describes the year Marvel 
 introduced each Avenger, you'll immediately notice some oddities. 
 For example, there are quite a few Avengers who look like they
   were introduced in 1900, which we know is a little fishy -- the Avengers
     weren't introduced in the comic series until the 1960's!

This is obviously a mistake in the data. As a result, you should remove all of
 the Avengers introduced before 1960 from the dataframe.
'''

true_avengers = pd.DataFrame()

avengers['Year'].hist()
plt.show()

# print(avengers['Year'].head())

true_avengers = avengers[avengers['Year'] >= 1960]
# print(true_avengers.head())

true_avengers['Year'].plot.hist()
plt.show()

# Consolidating Deaths

'''
We're interested in the total number of deaths each character experienced, 
so we'd like to have a single field containing that information. Right now, 
there are five fields (Death1 to Death5), each of which contains a binary value
 representing whether a superhero experienced that death or not. For example,
   a superhero could experience Death1, then Death2, and so on until the writers 
   decided not to bring the character back to life.

We'd like to combine that information in a single field so we can perform numerical
 analysis on it more easily.
'''

death = ['Death' + str(i) for i in range(1, 6)]



true_avengers['Deaths'] = true_avengers[death].apply(lambda row: (row == 'YES').sum(), axis=1)
# count total deaths

# Verifying Years Since Joining

'''
For our final task, we want to verify that the Years since joining field accurately reflects 
the Year column. For example, if an Avenger was introduced in the Year 1960, is the Years since 
joining value for that Avenger 55?
'''

joined_accuracy_count = int()

accurate_avengers = true_avengers[true_avengers['Years since joining']<= 55]
print(accurate_avengers.shape)
joined_accuracy_count = 159
