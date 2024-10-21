from csv import reader
apple_data = open(r"C:\Users\h9\Desktop\Notebook\files\AppleStore.csv")
google_data = open(r"C:\Users\h9\Desktop\Notebook\files\googleplaystore.csv")

data_apple = reader(apple_data)
apple_data_list = list(data_apple)
apple_header = apple_data_list[0]

data_google = reader(google_data)
google_data_list = list(data_google)
google_header = google_data_list[0]

def explore_data(data_set, first_index, last_index, rows_and_columns=False):
    data_list = data_set[first_index: last_index]
    for row in data_list:
        print(row, '\n')
        
    if rows_and_columns:
        print('Number of rows: ', len(data_list))
        print('Number of columns: ', len(data_list[0]))


print(apple_header, '\n')
explore_data(apple_data_list, 1, 5, True)
print('\n')

print(google_header)
explore_data(google_data_list, 1, 5, True)