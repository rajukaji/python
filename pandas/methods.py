import pandas as pd

df = pd.DataFrame({
    'a': [1, 2, 3], 
    'b': [2, 3, 1]
})
print('\n\n\n')

change = df['b'] - df['a']
print(change)

print('\n\n\n')
print(change.min())
print(change.max())
print(change.median())
print(change.sum())
print(change.std())

print(change.describe())
# see non null values