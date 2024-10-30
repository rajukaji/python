# find unique element of data frame column
import pandas as pd

df['data_column_name'].unique()

# suppose df1 is a new table/dataframe
df1 = df[df['released']>= 1990]
# this new df1 data frame is the table of all the released items after 1990 suppose
df1.to_csv('new_csv_filename.csv')