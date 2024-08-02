def dict_to_lists(dict):
    return ( [i for i in dict], [value for key, value in dict.items()] )

print(dict_to_lists({'a': 1, 'b': 2, "c": 3}))

