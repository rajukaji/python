import pandas as pd

df = pd.DataFrame(
    {
        'a': [1, 2, 3, 2, 3, 1],
        'b': [2, 3, 4, 5, 6, 7]
    }
)

unique_value = df['a'].unique()
print(unique_value)
# numpy array
print(type(unique_value))
# you can convert into list, tolist() method

print(type(unique_value.tolist()))

'''
series.str.strmethod()

laptops["screen_size"] = laptops["screen_size"].str.replace('"', '')

laptops['ram'] = laptops['ram'].str.replace('GB', '')
print(laptops['ram'].unique())
print(type(laptops))
'''