import pandas as pd

# DataFrame.rename(mapper=None, *, index=None, columns=None, axis=None, copy=None, inplace=False, level=None, errors='ignore')

# axis{0 or ‘index’, 1 or ‘columns’}, default 0

df = pd.DataFrame(
    {
        'a' : [1, 2, 3, 5, 6], 
        'b' : [2, 4, 5, 6, 7]
    }
)

df.rename({'a':'A', 'b': 'B'}, inplace=True, axis=1)
# df.rename(columns={'a':'A', 'b': 'B'}, inplace=True)
# or without axis put columns = {dict}

print(df)

