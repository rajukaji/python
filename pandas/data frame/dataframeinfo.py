import pandas as pd

df = pd.DataFrame(
    {
        'col 1': [[1, 2, 3], [1, 2, 3]],
        'col 2': [[1, 2, 3], [1, 2, 3]],
        'col 3': [[1, 2, 3], [1, 2, 3]],
        'col 4': [[1, 2, 3], [1, 2, 3]]
        
    }
)

print(df.dtypes)
print(df.info())
