import pandas as pd

df = pd.DataFrame(
    {'a': [1, 2, 3, 4, 5],
     'b': [2, 3, 4, 5, 6]
     })

# DataFrame.median(axis=0, skipna=True, numeric_only=False, **kwargs)

dfmedian = df[['a', 'b']].median(axis=0)
# for row axis = 0 vice versa
# similar as axis = 'index' opp, axis = 'columns' or 1

print(dfmedian)

# series = series.max(numeric_only=True)

# dataframe = dataframe.describe(include=['O'])
# DataFrame.describe(percentiles=None, include=None, exclude=None)

# for only numeric