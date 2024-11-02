# DataFrame.sort_values(by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)[source]
# Sort by the values along either axis.

import pandas as pd

df = pd.DataFrame(
    {
        'a': [5, 4, 3], 
        'b': [3, 2, 1]
    }
)

new_df = df.sort_values('b')
print(df)

print('\n\n\n')

print(new_df)