import numpy as np

ndarray = np.array([
    [1, 2, 3, 4, 5],
    [2, 4, 5, 6, 7],
    [2, 4, 5, 8, 7]
])

print(ndarray[2, 3])
# 3rd row 4th column


'''
Instructions
From the provided taxi ndarray:

Select every row for the columns at indices 1, 4, and 7. 
Assign the result to columns_1_4_7.
Select the columns at indices 5 to 8 inclusive for the row at index 99. 
Assign the result to row_99_columns_5_to_8.
Select the rows at indices 100 to 200 inclusive for the column at index 14. 
Assign the result to rows_100_to_200_column_14.
'''

columns_1_4_7 = taxi[:,[1, 4, 7]]
                     
row_99_columns_5_to_8 = taxi[99, 5:9]

rows_100_to_200_column_14 = taxi[100:201, 14]

sums = my_numbers[:, 0] + my_numbers[:, 1]
# sum of column 0 and column 1 all rows