def combine_dictionaries(dict1, dict2):
    dict1.update(dict2)
    #update the diciontary 1 with dictionary 2, and print dictionary 1
    return dict1
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print(combine_dictionaries(dict1, dict2))
