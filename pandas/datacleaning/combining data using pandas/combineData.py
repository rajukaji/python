import pandas as pd

'''
We'll use what we learned in the last lesson to analyze the 2015, 2016, and 2017 World Happiness Reports. 
Specifically, we'll look to answer the following question:

Did world happiness increase, decrease, or stay about the same from 2015 to 2017?

As a reminder, these reports assign each country a happiness score based on a poll question that asks
 respondents to rank their life on a scale of 0 - 10, so "world happiness" refers to this definition specifically.
'''

happiness2015 = pd.read_csv("World_Happiness_2015.csv")
happiness2016 = pd.read_csv('World_Happiness_2016.csv')
happiness2017 = pd.read_csv('World_Happiness_2017.csv')

'''
Add a column called Year to each dataframe with the corresponding year. For example, the Year column in happiness2015 should contain the value 2015 for each row.
'''
happiness2015['Year'] = 2015
happiness2016['Year'] = 2016
happiness2017['Year'] = 2017


head_2015 = happiness2015[['Country','Happiness Score', 'Year']].head(3)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)

# use the concat() function to combine head_2015 and head_2016 next.
# combining for same shape and size/rows and columns

concat_axis0 = pd.concat([head_2015, head_2016], axis=0)

concat_axis1 = pd.concat([head_2015, head_2016], axis=1)

# with different shape
head_2015 = happiness2015[['Year','Country','Happiness Score', 'Standard Error']].head(4)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)

concat_axis0 = pd.concat([head_2015, head_2016], axis=0)



head_2015 = happiness2015[['Year','Country','Happiness Score', 'Standard Error']].head(4)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)

concat_update_index = pd.concat([head_2015, head_2016], ignore_index = True)

