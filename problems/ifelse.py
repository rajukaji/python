opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data = []
n_apps_more_9 = 0
n_apps_less_9 = 0

for row in apps_data[1:]:
    rating = float(row[7])
    
    price = float(row[4])
    
    if price > 9:
        data.append(rating)
        n_apps_more_9 += 1
    else:
        n_apps_less_9 += 1
    
avg_rating = sum(data) / len(data)