import pandas as pd

df = pd.DataFrame({'a':[1, 2, 3], 'b':[4, 5, 6]})

print(df.iloc[0, 0])
# access unique elements
# index location

# df.iloc[row_index, column_index]

first_row = df.iloc[0]
print(first_row)

first_column = df.iloc[:, 0]
# like in numpy
print(first_column)

list_of_columns = df.iloc[:, [0, 1]]
print(list_of_columns)

slice_of_columns = df.iloc[:, [0:2]]

rows_from_df = df.iloc[[0, 1]]

single_row = df.iloc[1]

'''
profited = f500[f500['profits'].notnull()]
print(profited)

costs = profited['revenues'] - profited['profits']

f500['costs'] = costs
print(costs)
'''