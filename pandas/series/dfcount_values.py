import pandas as pd

# pandas.Series.value_counts
# Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)[source]

df = pd.DataFrame({
    'a': [1, 2, 3], 
    'b': [2, 3, 4]
})

print(df.value_counts)

print('\n\n\n')

dfseries = df['a']
print(dfseries)
print(dfseries.value_counts)