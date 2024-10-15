import pandas as pd

homelessness = pd.DataFrame([1, 2, 3, 4, 5], 
                            [1, 3, 4, 5, 6])

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())



# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

homelessness.sort_values('column_name_to_sort')
# ascending order

homelessness.sort_values('column_name_to_sort', ascending=False)
# descending order