import pandas as pd

df = pd.DataFrame({
    'a': [1, 2, 3], 
    'b': [1, 2, 2]
})
# use df.loc['row_name'] for row selection with all columns
# use dfobj['colname'] for column selection all rows

# df.loc[row_label, column_label]
# list of labels
print(df.loc[:, ['a']])
# all rows or a list
print('\n\n\n')
print(df[['a']])
# same as above

'''
Since the object returned is two-dimensional, we've got a DataFrame,
 not a Series. As an alternative to using df.loc[:, ["col1", "col2"]]
   to select a specific list of columns, we can use the shorthand 
   syntax df[["col1", "col2"]] to achieve the same result.
'''

toyota = f500.loc["Toyota Motor"]
print(toyota)
# selection of single row and all columns must, no shortcut

drink_companies = f500.loc[['Anheuser-Busch InBev', 'Coca-Cola', 'Heineken Holding']]
# selection of multiple rows with row index/axis, all column, with no shortcuts available

middle_companies = f500['Tata Motors':'Nationwide']
# but, there is shortcut to select from start row to end row, inclusive, shortcut for slice

print(drink_companies)
print(middle_companies)