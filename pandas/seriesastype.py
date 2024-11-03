import pandas as pd

df = pd.DataFrame(
    {
        'a' : ['1', '2', '3'],
        'b' : ['3', '5', '4']
    }
)

# series.astype(type)

col_update = df['a'].astype(int)
print(col_update)

print(df)