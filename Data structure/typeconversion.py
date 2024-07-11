''' python type conversion
list() - converts to list
tuple() - converts to tuple
dict() - converts to dictionary
set() - converts to set
'''
#dictionery  converted into a list would only contain the key of the pairs, not the value
dictionary = {'a': 97, 'b': 98, 'c': 99}
listing = list(dictionary)
print(listing)

#removing the duplicates in a list, by using set() and again converting it back to the list()

duplicate_list = [1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6]
print(duplicate_list)
unique_list = list(set(duplicate_list))
print(unique_list)