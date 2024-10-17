opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(index, data_set):
    
    frequency_table = {}
    
    for row in data_set:
        
        value = row[index]
        
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table


ratings_ft = freq_table(7, apps_data[1:])
print(ratings_ft)