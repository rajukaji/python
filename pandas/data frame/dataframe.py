import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 
                   'b': [6, 7, 8, 9, 10],
                   'c': [2, 3, 4, 5, 6]})

print(df)

print(df.head())
# prints first 5 rows
# DataFrame.head(INT PARA OPTIONAL)
# DataFrame.head(3), displays top 3 rows
print(df.tail(3))


f500 = pd.read_csv('f500.csv', index_col=0)

f500.index.name = None

f500_type    = type(f500)

print(type(f500))
f500_shape = f500.shape

print(f500_shape)