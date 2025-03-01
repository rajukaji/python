# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

# to extract a column that we need with index


def freq_table(lst):
# create a frequency table
    the_dict = {}
    
    for i in lst:
        if i in the_dict:
            the_dict[i] += 1
        else:
            the_dict[i] = 1

            
    return the_dict



genres_ft = freq_table(genres)

print(genres)
print(genres_ft)

print(extract(4))
print(freq_table(extract(4)))