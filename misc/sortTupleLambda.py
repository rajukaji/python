def sort_tuples(tuples):
    return sorted(tuples, key= lambda x: x[1]) #using lambda function

print(sort_tuples((('c', 3), ('b', 2), ('a', 1))))