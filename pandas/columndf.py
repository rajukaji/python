import pandas as pd

df = pd.DataFrame(
    {
        'a': [1, 2, 3],
        'b': [2, 3, 4], 
        'c': [4, 5, 6]
    }
)

al_columns = df.columns
print(al_columns)

# find all the column names head

'''
# clean string

def clean_col(col):
    col = col.strip()
    col = col.replace('Operating System', 'os')
    col = col.replace(' ', '_')
    col = col.replace('(', '')
    col = col.replace(')', '')
    col = col.lower()
    return col


new_columns = []
for c in laptops.columns:
    c = clean_col(c)
    new_columns.append(c)
    # print(c)
    

laptops.columns = new_columns
print(laptops.columns)
'''