def lists_to_dict(list1, list2):
    dic = dict(zip(list1, list2))
    return dic


list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [1, 2, 3, 4, 5]

dictionary_file = dict(zip(list1, list2))

print(dictionary_file)
print(type(dictionary_file))